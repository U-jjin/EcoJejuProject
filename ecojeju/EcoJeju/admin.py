from django.contrib import admin
from .models import user

@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        #'user_pwd',
        'user_name',
        'register_date'
    )
    list_display_links = (
        'user_id',
        'user_name'
    )