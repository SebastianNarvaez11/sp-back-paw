# Generated by Django 2.2.3 on 2020-10-22 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0013_auto_20201022_1056'),
        ('payment', '0005_auto_20200827_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompromisePay',
            fields=[
                ('id', models.CharField(blank=True, max_length=40, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('value', models.IntegerField(verbose_name='Valor')),
                ('date_pay', models.DateField(verbose_name='Fecha de Pago')),
                ('state', models.PositiveSmallIntegerField(choices=[(1, 'Pendiente'), (2, 'Incumplido'), (3, 'Cumplido')], default=1, verbose_name='Estado')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compromises', to='users.Student', verbose_name='Estudiante')),
                ('user_create', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_update', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Compromiso',
                'verbose_name_plural': 'Compromisos',
                'ordering': ['-create'],
            },
        ),
    ]
