from django.db import models
from base.models import Base
from school.models import Grade
from django.contrib.auth.models import AbstractUser
from base.utils import get_guid
import uuid

# Create your models here.


class User(AbstractUser, Base):
    USER_TYPE_CHOICES = (
        (1, 'Administrador'),
        (2, 'Asistente'),
        (3, 'Estudiante'))
    type = models.PositiveSmallIntegerField(
        'Perfil', choices=USER_TYPE_CHOICES, default=1)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-create']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Admin(models.Model):
    id = models.CharField(primary_key=True, blank=True,
                          max_length=40, verbose_name="ID")
    user = models.OneToOneField(
        User, verbose_name='Usuario', related_name='admin', on_delete=models.CASCADE)
    position = models.CharField('Cargo', max_length=20, default='Mensajero')

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def save(self, force_insert=False, force_update=False, update_fields=None, using=None, request=None):
        is_new = False
        if not self.id:
            is_new = True
            self.id = get_guid()
        super(Admin, self).save(force_insert,
                                force_update, using, update_fields)


class Student(models.Model):
    DOCUMENT_TYPE_CHOICES = (
        (1, 'T.I'),
        (2, 'R.C'),
        (3, 'C.C'),)

    SCHEDULE_TYPE_CHOICES = (
        (1, 'Mañana'),
        (2, 'Tarde'),
        (3, 'Unica'),)
    
    INITIAL_CHARGE_CHOICES = (
        (10, 'Feb.Nov'),
        (9, 'Mar.Nov'),
        (8, 'Abr.Nov'),
        (7, 'May.Nov'),
        (6, 'Jun.Nov'),
        (5, 'Jul.Nov'),
        (4, 'Ago.Nov'),
        (3, 'Sep.Nov'),
        (2, 'Oct.Nov'),)

    id = models.CharField(primary_key=True, blank=True, max_length=40, verbose_name="ID")
    code = models.IntegerField('Codigo', unique=True, blank=True, null=True)
    user = models.OneToOneField(User, verbose_name='Usuario', related_name='student', on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, verbose_name='Grado', on_delete=models.CASCADE,related_name='students', blank=True, null=True)
    phone1 = models.CharField('Telefono 1', max_length=11, null=True, blank=True)
    phone2 = models.CharField('Telefono 2', max_length=11, null=True, blank=True)
    document_type = models.PositiveSmallIntegerField('Tipo de Documento', choices=DOCUMENT_TYPE_CHOICES, default=1)
    document = models.CharField('No. de Documento', max_length=20)
    attending = models.CharField('Acudiente', max_length=100)
    discount = models.IntegerField('% Descuento Mensual', default=0)
    initial_charge = models.PositiveSmallIntegerField('Periodo de Cobro', choices=INITIAL_CHARGE_CHOICES, default=10)
    coverage = models.BooleanField('Cobertura', default=False)
    schedule = models.PositiveSmallIntegerField(
        'Jornada', choices=SCHEDULE_TYPE_CHOICES, default=1)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.user.last_name + ' ' + self.user.first_name
    
    def total_year(self):
        return (self.grade.monthly_pay - ((self.grade.monthly_pay * self.discount)/100)) * self.initial_charge
    
    def total_paid(self):
        total_value = 0
        for pay in self.payments.all():
            total_value = total_value + pay.value
        return total_value
    
    def monthly_payment(self):
        return self.grade.monthly_pay - ((self.grade.monthly_pay * self.discount)/100)
    


    def save(self, force_insert=False, force_update=False, update_fields=None, using=None, request=None):
        is_new = False
        if not self.id:
            is_new = True
            self.id = get_guid()
            self.code = Student.objects.count() + 1
            
        super(Student, self).save(force_insert,
                                  force_update, using, update_fields)
