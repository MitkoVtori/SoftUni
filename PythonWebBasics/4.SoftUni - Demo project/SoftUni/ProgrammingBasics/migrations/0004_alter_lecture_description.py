# Generated by Django 4.2 on 2023-04-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammingBasics', '0003_alter_lecture_description_alter_lecture_resources_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='Description',
            field=models.TextField(help_text='Short description about the lecture.<br>                                    - for new line use &lt;br&gt;<br>                                    - supports html'),
        ),
    ]
