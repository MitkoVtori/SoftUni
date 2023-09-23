from django.core.validators import MinLengthValidator
from django.db import models


class Problem(models.Model):

    problem_type = models.CharField(max_length=7, choices=[
        ("Game", "Game"),
        ("Profile", "Profile"),
        ("Site", "Site"),
        ("Other", "Other")
    ])

    title = models.CharField(max_length=30, validators=[MinLengthValidator(
        10, message="Title must be at least 10 characters long!"
    )])

    description = models.TextField(max_length=500, validators=[MinLengthValidator(
        50, message="Description must be at least 50 characters long!")],
                                   help_text="Try to describe the problem in as much detail as possible!")

    video_image = models.URLField(
        help_text="Please submit a link to a video and/or image that shows the problem, if you have one.",
        blank=True, null=True)

    creator = models.CharField()

    date_reported = models.DateTimeField(auto_now_add=True)


class StaffNotes(models.Model):
    content = models.TextField(max_length=500, validators=[MinLengthValidator(10)])
    date = models.DateTimeField(auto_now_add=True)
