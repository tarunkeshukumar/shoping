# Generated by Django 5.0.9 on 2024-11-06 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='discout',
            new_name='discount',
        ),
    ]
