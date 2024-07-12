# Generated by Django 5.0.6 on 2024-07-05 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgn2', '0026_mastercompany_rename_company_bachelorcompany_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bachelorplan',
            options={'verbose_name': 'Учебный план (бакалавриат)', 'verbose_name_plural': 'Учебный план (бакалавриат)'},
        ),
        migrations.AlterModelOptions(
            name='masterplan',
            options={'verbose_name': 'Учебный план (магистратура)', 'verbose_name_plural': 'Учебный план (магистратура)'},
        ),
        migrations.CreateModel(
            name='BachelorDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('bachelor_semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disciplines', to='sgn2.bachelorplan')),
            ],
        ),
        migrations.CreateModel(
            name='MasterDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('master_semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disciplines', to='sgn2.masterplan')),
            ],
            options={
                'verbose_name': 'дисциплина',
                'verbose_name_plural': 'дисциплины',
            },
        ),
        migrations.DeleteModel(
            name='Discipline',
        ),
    ]