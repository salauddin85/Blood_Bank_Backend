# Generated by Django 5.1 on 2024-09-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_donorprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorprofile',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
