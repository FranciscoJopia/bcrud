# Generated by Django 5.1.2 on 2024-10-21 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudweb', '0005_alter_cliente_telefono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominio',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dominios', to='crudweb.cliente'),
        ),
    ]
