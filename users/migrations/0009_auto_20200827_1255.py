# Generated by Django 2.2.3 on 2020-08-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200825_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='initial_charge',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Feb.Nov'), (9, 'Mar.Nov'), (8, 'Abr.Nov'), (7, 'May.Nov'), (6, 'Jun.Nov'), (5, 'Jul.Nov'), (4, 'Ago.Nov'), (3, 'Sep.Nov'), (2, 'Oct.Nov')], default=10, verbose_name='Periodo de Cobro'),
        ),
    ]
