# Generated by Django 5.1 on 2024-10-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_bank_releted', '0005_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
