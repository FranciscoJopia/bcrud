# Generated by Django 5.1.2 on 2024-10-14 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=20, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='dominio',
            name='nombre',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AddField(
            model_name='dominio',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dominios', to='crudweb.cliente'),
        ),
    ]
