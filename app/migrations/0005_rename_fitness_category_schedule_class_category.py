# Generated by Django 5.1.4 on 2025-01-15 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_trainer_specialties_delete_specialty_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='fitness_category',
            new_name='class_category',
        ),
    ]
