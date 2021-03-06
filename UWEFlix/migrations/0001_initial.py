# Generated by Django 3.1.2 on 2022-04-02 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('name', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=300)),
                ('landline', models.CharField(max_length=11)),
                ('mobile', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=30)),
                ('representative', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('card_number', models.IntegerField()),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('duration', models.IntegerField()),
                ('short_description', models.CharField(max_length=300)),
                ('long_description', models.CharField(max_length=300)),
                ('image_URL', models.URLField()),
                ('upload_date', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
        migrations.CreateModel(
            name='Screens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('taken_tickets', models.IntegerField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UWEFlix.film')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UWEFlix.screens')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketType', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ticketPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='tempBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField()),
                ('student_tickets', models.IntegerField()),
                ('child_tickets', models.IntegerField()),
                ('adult_tickets', models.IntegerField()),
                ('cost', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('showing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UWEFlix.showing')),
            ],
        ),
        migrations.CreateModel(
            name='ClubAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_title', models.CharField(max_length=300)),
                ('card_number', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('discountRate', models.FloatField(default=0.0)),
                ('balance', models.FloatField(default=0.0)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UWEFlix.club')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_tickets', models.IntegerField()),
                ('child_tickets', models.IntegerField()),
                ('adult_tickets', models.IntegerField()),
                ('cost', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('showing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UWEFlix.showing')),
            ],
        ),
    ]
