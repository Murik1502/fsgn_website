# Generated by Django 5.0.6 on 2024-07-03 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgn2', '0023_alter_discipline_bachelor_semester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='bachelor_semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disciplines', to='sgn2.bachelorplan'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='master_semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disciplines', to='sgn2.masterplan'),
        ),
    ]
