# Generated by Django 5.1 on 2024-09-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_donorprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorprofile',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
