from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'city', 'is_active',)
    list_filter = ('is_active',)
    raw_id_fields = ('city',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('city',)}),
    )
