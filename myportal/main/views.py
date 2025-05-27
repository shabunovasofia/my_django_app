import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, FeedbackForm
from django.utils.timezone import localtime
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import ReviewForm
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

from .models import Review


@require_POST
@login_required
def add_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.name = f"{request.user.first_name} {request.user.last_name}"
        review.save()

        # Рендерим HTML-отзыв
        review_html = render_to_string('main/review_item.html', {'review': review}, request=request)

        # Отправляем по WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "reviews",
            {
                "type": "new_review",
                "review_html": review_html
            }
        )

        # Возвращаем HTML в AJAX
        return JsonResponse({'status': 'success', 'review_html': review_html})
    return JsonResponse({'status': 'error', 'errors': form.errors})

def send_to_telegram(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            telegram_bot_token = "7575487584:AAEl8o_RaOeBuFA_zp57r0Z39AXtBk8q75g"
            chat_id = 884379984

            text = f"✉ Новое сообщение!\n👤 Имя: {name}\n📧 Email: {email}\n💬 Сообщение: {message}"

            telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"

            try:
                response = requests.post(
                    telegram_url,
                    json={
                        'chat_id': chat_id,
                        'text': text
                    }
                )
                data = response.json()

                if data.get('ok'):
                    return JsonResponse({'status': 'success', 'message': 'Сообщение успешно отправлено!'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Ошибка при отправке сообщения!'})

            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f'Ошибка: {str(e)}'})

        return JsonResponse({'status': 'error', 'message': 'Неверные данные формы'})

    return JsonResponse({'status': 'error', 'message': 'Метод не разрешен'}, status=405)
def home(request):
    return render(request, 'main/home.html')
def product(request):
    return render(request, 'main/product.html')
def reviews(request):
    all_reviews = Review.objects.select_related("user").order_by('-created_at')  # сортируем от новых к старым
    return render(request, 'main/reviews.html', {'reviews': all_reviews})
def contact(request):
    return render(request, 'main/contact.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = f"user_{user.phone}"
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'main/registration/register.html', {'form': form})
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=phone, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'main/registration/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')
@login_required

def profile_view(request):
    user = request.user
    user.last_login_local = localtime(user.last_login) if user.last_login else None
    return render(request, 'main/profile.html', {'user': user})

