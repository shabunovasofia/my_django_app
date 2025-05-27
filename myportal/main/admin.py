from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Review

admin.site.register(Review)
User = get_user_model()

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'first_name', 'last_name', 'email', 'is_staff')
