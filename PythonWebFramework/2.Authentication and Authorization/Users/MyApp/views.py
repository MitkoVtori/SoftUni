from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views.generic import View
from Users.MyApp.decorators import allowed_groups
# from django.contrib.auth import authenticate


def index(request):
    if request.user.is_authenticated:
        context = {"user": True}
    else:
        context = {"user": False}

    # if authenticate(username="peter", password="peterpass"):
    #     context = {"user": True}
    # else:
    #     User.objects.create_user("peter", "peter@gmail.com", "peterpass")
    #     context = {"user": False}

    return render(request, "index.html", context)


def details(request):
    some_user = User.objects.get(username="peter")
    print(request.user.__class__.__name__)
    login(request, some_user)
    print(request.user.__class__.__name__)
    return render(request, "details.html")


def details_logout(request):
    print(request.user.__class__.__name__)
    logout(request)
    print(request.user.__class__.__name__)
    return render(request, "details.html")


@login_required(login_url="/login")
def login_required(request):
    return render(request, "basic.html")


class LoginRequired(auth_mixins.LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "basic.html")


def log_in(request):
    return render(request, "login_required.html")


@allowed_groups(groups=["Staff"])
def info(request):
    return HttpResponse("Private information!")