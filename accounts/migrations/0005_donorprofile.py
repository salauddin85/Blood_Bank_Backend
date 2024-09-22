# Generated by Django 5.1 on 2024-09-07 09:41

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_donorprofile'),
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(max_length=3)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Product_images')),
                ('address', models.TextField()),
                ('mobaile_no', models.PositiveIntegerField(max_length=12)),
                ('blood_donation_count', models.PositiveIntegerField(default=0)),
                ('blood_group', models.CharField(max_length=3)),
                ('last_donation_date', models.DateField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('health_screening_passed', models.BooleanField(default=False)),
                ('reciver_blood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.donationhistory')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
