from django.urls import path
from . import views
# feedback/urls.py

urlpatterns = [
    path('send-feedback/', views.send_to_telegram, name='send_feedback'),
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('reviews/', views.reviews, name='reviews'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('reviews/add/', views.add_review, name='add_review'),

]
