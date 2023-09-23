# Generated by Django 4.2.4 on 2023-08-04 08:40

import GameStats.Games.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')])),
                ('comment', models.TextField(max_length=250)),
                ('game', models.CharField()),
                ('creator', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', validators=[GameStats.Games.validators.image_size])),
                ('title', models.CharField(error_messages={'unique': 'Game with this name already exists!'}, max_length=25, unique=True, validators=[django.core.validators.MinLengthValidator(2, message='game title must be at least 2 characters long!')])),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Sports', 'Sports'), ('Adventure', 'Adventure'), ('Role-play', 'Role-play'), ('Racing', 'Racing'), ('Other', 'Other')], max_length=10)),
                ('description', models.TextField(max_length=500)),
                ('creator', models.CharField()),
            ],
        ),
    ]
