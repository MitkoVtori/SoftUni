# Generated by Django 4.1.1 on 2022-10-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_create_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]
