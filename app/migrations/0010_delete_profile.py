# Generated by Django 5.1.4 on 2025-01-29 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_profile_bio_profile_is_active_member_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
