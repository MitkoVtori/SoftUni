from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from GameStats.Profile.forms import AppUserAdministrationForm


UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    list_display = (
        "username", "email", "first_name", "last_name",
        "date_joined", "is_superuser", "is_staff", "is_active"
    )
    list_display_links = ("username", "email")

    form = AppUserAdministrationForm
    readonly_fields = ['password', 'date_joined']
