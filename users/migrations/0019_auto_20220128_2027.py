# Generated by Django 2.2.3 on 2022-01-29 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20220128_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_retiro',
            field=models.DateField(verbose_name='Fecha de Retiro'),
        ),
    ]