# Generated by Django 4.0.3 on 2022-05-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlix', '0015_clubrepresentative_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='email',
        ),
        migrations.AlterField(
            model_name='clubrepresentative',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
