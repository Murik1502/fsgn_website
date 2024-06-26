# Generated by Django 5.0.6 on 2024-06-26 13:55

import sgn2.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='ФИО')),
                ('role', models.CharField(max_length=64, verbose_name='Должность')),
                ('description', models.TextField(max_length=2048, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, upload_to=sgn2.models.get_upload_path, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'преподаватель',
                'verbose_name_plural': 'преподаватели',
            },
        ),
    ]