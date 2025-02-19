# Generated by Django 5.1.4 on 2025-01-14 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_classcategory_fitnessclass_membershipplan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('specialties', models.ManyToManyField(to='app.specialty')),
            ],
        ),
        migrations.DeleteModel(
            name='FitnessClass',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trainer'),
        ),
        migrations.DeleteModel(
            name='MemberProfile',
        ),
        migrations.DeleteModel(
            name='TrainerProfile',
        ),
    ]
