# Generated by Django 5.1 on 2024-09-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_donorprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorprofile',
            name='image',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
