from django.contrib import admin

from CBVPractice.Profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username",)

