# Generated by Django 3.1.2 on 2022-04-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlix', '0009_auto_20220409_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubrepresentative',
            name='clubRepNumber',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
