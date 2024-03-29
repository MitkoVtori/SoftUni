# Generated by Django 4.2 on 2023-04-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammingBasics', '0002_alter_lecture_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='Description',
            field=models.TextField(help_text='Short description about the lecture.\n                                    - for new line use <br>                                    - supports html'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='Resources',
            field=models.TextField(blank=True, help_text='Links. Html only...', null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='Title',
            field=models.CharField(help_text='Lecture title', max_length=50),
        ),
    ]
