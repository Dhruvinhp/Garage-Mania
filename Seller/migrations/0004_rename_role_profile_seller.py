# Generated by Django 3.2.5 on 2021-08-05 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0003_profile_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='role',
            new_name='seller',
        ),
    ]
