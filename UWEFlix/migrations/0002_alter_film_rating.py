# Generated by Django 4.0.2 on 2022-03-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.IntegerField(max_length=1),
        ),
    ]
