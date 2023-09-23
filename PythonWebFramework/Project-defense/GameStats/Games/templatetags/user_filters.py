from django import template
from django.contrib.auth import get_user_model
from GameStats.Common.models import Problem

UserModel = get_user_model()
register = template.Library()


@register.filter(name="UserModel")
def user_model(value):
    if UserModel.objects.filter(username=value):
        return UserModel.objects.get(username=value)

    class Unknown:
        image = False

    return Unknown


@register.filter(name="exists")
def user_exists(value):
    return value if UserModel.objects.filter(username=value) else "Unknown"