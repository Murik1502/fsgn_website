# Generated by Django 5.0.6 on 2024-07-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgn2', '0006_alter_statistics_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bachelorprogram',
            name='title',
            field=models.CharField(max_length=128, null=True, verbose_name='Название программы'),
        ),
    ]