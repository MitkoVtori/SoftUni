from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from GameStats.Games.models import Game, Comment
from GameStats.Profile.forms import AppUserCreationForm, LoginForm, EditAppUserForm, ChangePasswordForm, \
    DeleteAppUserForm

UserModel = get_user_model()


class CreateUser(CreateView):
    template_name = "Profile/create-profile.html"
    form_class = AppUserCreationForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserLogin(LoginView):
    template_name = "Profile/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True


class LogoutPageView(TemplateView):
    template_name = 'Profile/logout.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("home")
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class UserLogout(LogoutView):
    template_name = 'Profile/logout.html'


class UserDetails(LoginRequiredMixin, TemplateView):
    template_name = "Profile/details.html"

    def get_context_data(self, **kwargs):
        context = {
            "games": Game.objects.filter(creator=self.request.user.get_username())
        }
        return context


class EditUser(LoginRequiredMixin, UpdateView):
    model = UserModel
    template_name = "Profile/edit-profile.html"
    form_class = EditAppUserForm
    success_url = reverse_lazy("user")

    def get_object(self, **kwargs):
        return self.request.user


class ChangeUserPassword(LoginRequiredMixin, UpdateView):
    model = UserModel
    template_name = "Profile/change-password.html"
    form_class = ChangePasswordForm
    success_url = reverse_lazy("user")

    def get_object(self, **kwargs):
        return self.request.user

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class DeleteUser(LoginRequiredMixin, DeleteView):
    template_name = "Profile/delete.html"
    form_class = DeleteAppUserForm
    success_url = reverse_lazy("home")

    def get_object(self, **kwargs):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['username'].initial = self.request.user.get_username()
        return form

    def form_invalid(self, form):
        form.add_error("password", "Invalid password")
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.request.user.delete()
        for game in Game.objects.filter(creator=self.request.user.get_username()):
            game.delete()
            for comment in Comment.objects.filter(game=game.title):
                comment.delete()
        return HttpResponseRedirect(success_url)