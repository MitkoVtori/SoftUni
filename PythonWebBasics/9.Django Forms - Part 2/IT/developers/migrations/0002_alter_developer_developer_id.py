# Generated by Django 4.2 on 2023-06-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='developer_id',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
