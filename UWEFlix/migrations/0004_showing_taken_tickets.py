# Generated by Django 4.0.2 on 2022-03-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlix', '0003_alter_booking_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='showing',
            name='taken_tickets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]