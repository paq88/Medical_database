# Generated by Django 5.0.3 on 2024-04-25 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_employes_id_experiments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employes',
            name='id_lab',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.laboratory'),
        ),
    ]