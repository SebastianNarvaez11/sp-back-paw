# Generated by Django 2.2.3 on 2021-04-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20201022_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Codigo'),
        ),
    ]
