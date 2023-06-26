# Generated by Django 4.2.2 on 2023-06-21 12:59

import MyMusicApp.MyMusicApp.Profile.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), MyMusicApp.MyMusicApp.Profile.validators.valid_username])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]