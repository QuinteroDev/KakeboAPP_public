# Generated by Django 5.0.6 on 2024-07-26 07:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('necesidades', 'Necesidades Básicas'), ('ahorro', 'Ahorro e Inversión'), ('educacion', 'Formación y Educación'), ('ocio', 'Ocio y Entretenimiento'), ('donaciones', 'Donaciones'), ('proyectos', 'Proyectos y Emprendimiento')], max_length=20)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'category')},
            },
        ),
    ]