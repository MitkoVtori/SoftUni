from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from GameStats.Games.validators import image_size


class Game(models.Model):
    image = models.ImageField(upload_to="images", validators=[image_size])

    title = models.CharField(max_length=25, validators=[MinLengthValidator(
        2, message="game title must be at least 2 characters long!"
    )], unique=True, error_messages={"unique": "Game with this name already exists!"})

    genre = models.CharField(max_length=10, choices=[
        ("Action", "Action"),
        ("Sports", "Sports"),
        ("Adventure", "Adventure"),
        ("Role-play", "Role-play"),
        ("Racing", "Racing"),
        ("Other", "Other")
    ])

    description = models.TextField(max_length=500)

    creator = models.CharField() # request.user


class Comment(models.Model):

    rating = models.IntegerField(choices=[
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐")
    ])
    comment = models.TextField(validators=[MaxLengthValidator(250,
                                                              message="Comment can't be more than 250 characters long!")])
    game = models.CharField() # game title
    creator = models.CharField()  # AppUser username
