from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from GameStats.Profile.validators import letters_numbers_underscores, only_letters, image_size


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, validators=[MinLengthValidator(
        2, message="Username must be at least 2 characters long!"
    ), letters_numbers_underscores], unique=True, error_messages={
        "unique": "User with this username already exists!"
    })

    USERNAME_FIELD = "username"

    email = models.EmailField(unique=True, error_messages={"unique": "User with this email address already exists!"})

    first_name = models.CharField(max_length=25, validators=[only_letters], blank=True, null=True)
    last_name = models.CharField(max_length=25, validators=[only_letters], blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    image = models.ImageField(upload_to="images", validators=[image_size], blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

