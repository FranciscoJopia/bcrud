# Generated by Django 5.1.2 on 2024-10-12 02:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_vencimiento', models.DateField()),
                ('costo_renovacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notas', models.TextField(blank=True)),
            ],
        ),
    ]
