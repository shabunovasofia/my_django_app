from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser
import re
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    email = forms.EmailField(label='Ваш email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'email', 'password1', 'password2')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.match(r'^[A-ZА-Я][a-zа-я]*$', first_name):
            raise ValidationError("Имя должно содержать только буквы и начинаться с заглавной.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.match(r'^[A-ZА-Я][a-zа-я]*$', last_name):
            raise ValidationError("Фамилия должна содержать только буквы и начинаться с заглавной.")
        return last_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+?[0-9]{10,15}$', phone):
            raise ValidationError("Пожалуйста, введите корректный номер телефона.")
        return phone

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('phone',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Номер телефона')

    def clean_username(self):
        phone = self.cleaned_data['username']
        if not re.match(r'^\+?[0-9]{10,15}$', phone):
            raise ValidationError("Пожалуйста, введите корректный номер телефона.")
        return phone
