# Generated by Django 2.2.3 on 2022-01-29 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20220128_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.CharField(error_messages={'key': 'Ya existe un estudiante con ese codigo'}, max_length=10, null=True, unique=True, verbose_name='Codigo'),
        ),
    ]