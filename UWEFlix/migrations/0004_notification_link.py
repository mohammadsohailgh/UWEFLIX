# Generated by Django 4.0.2 on 2022-04-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlix', '0003_alter_booking_id_alter_clubaccount_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='link',
            field=models.CharField(default='', max_length=500),
        ),
    ]
