from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models.wish import Wish
from app.models.user import User


class MyUserAdmin(UserAdmin):
    list_display = ['username', 'is_active', 'is_staff', 'is_superuser', ]


class WishAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'buy_date', ]


admin.site.register(User, MyUserAdmin)
admin.site.register(Wish, WishAdmin)
