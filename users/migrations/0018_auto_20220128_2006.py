# Generated by Django 2.2.3 on 2022-01-29 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_student_date_retiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_retiro',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Retiro'),
        ),
    ]
