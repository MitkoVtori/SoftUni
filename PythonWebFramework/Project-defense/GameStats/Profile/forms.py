from django import forms
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from GameStats.Profile.validators import min_length, must_have_digit_and_letter

UserModel = get_user_model()


class AppUserAdministrationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class AppUserCreationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
                               validators=[min_length, must_have_digit_and_letter])
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Repeat password"}))

    class Meta:
        model = UserModel
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super(AppUserCreationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match!")

        return cleaned_data

    def save(self, commit=True):
        user = super(AppUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}), label='')

    error_messages = {
        'invalid_login': _(
            "Invalid username or password!"
        ),
        'inactive': _("This account is inactive."),
    }

    class Meta:
        model = UserModel
        fields = ["username", "password"]


class EditAppUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["image", "username", "email", "first_name", "last_name"]


class ChangePasswordForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "New password"}),
                               validators=[min_length, must_have_digit_and_letter], label='')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}), label='')

    class Meta:
        model = UserModel
        fields = []

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()

        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            self.add_error('confirm_password', "Password does not match!")

        return cleaned_data

    def save(self, commit=True):
        user = super(ChangePasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data["new_password"])
        if commit:
            user.save()
        return user


class DeleteAppUserForm(AuthenticationForm):
    username = forms.CharField(disabled=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Your password"}), label='')

    class Meta:
        model = UserModel
        fields = ["username", "password"]

