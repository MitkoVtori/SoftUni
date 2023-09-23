from django.db import models
from django.urls import reverse


class Profile(models.Model):
    username = models.CharField()

    email = models.EmailField()

    password = models.CharField()


class Article(models.Model):
    title = models.CharField()
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('details', kwargs={"pk": self.pk})
