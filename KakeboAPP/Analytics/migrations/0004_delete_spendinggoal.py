# Generated by Django 5.0.6 on 2024-07-29 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0003_alter_monthlyanalytics_unique_together_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SpendingGoal',
        ),
    ]
