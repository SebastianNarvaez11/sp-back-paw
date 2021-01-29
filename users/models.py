from django.db import models
from base.models import Base
from school.models import Grade
from django.contrib.auth.models import AbstractUser
from base.utils import get_guid
import uuid
from datetime import datetime
import math

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
        ordering = ['last_name']

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
    code = models.CharField('Codigo',max_length=10, unique=True)
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
    
    # valor de la mensualidad
    def monthly_payment(self):
        return self.grade.monthly_pay - ((self.grade.monthly_pay * self.discount)/100)

    # cantidad de meses en mora
    def monthOwed(self):
        month = 8
        # calculamos los meses pagados
        month_pay = math.floor(self.total_paid() / self.monthly_payment())
        # total valor en mora restante
        total_remaining = self.total_year() - self.total_paid()

        if month == 2 and total_remaining > (self.monthly_payment() * 9):
            return (self.initial_charge - 9 - month_pay)

        elif month == 3 and total_remaining > (self.monthly_payment() * 8):
            return (self.initial_charge - 8 - month_pay)
        
        elif month == 4 and total_remaining > (self.monthly_payment() * 7):
            return (self.initial_charge - 7 - month_pay)
        
        elif month == 5 and total_remaining > (self.monthly_payment() * 6):
            return (self.initial_charge - 6 - month_pay)
        
        elif month == 6 and total_remaining > (self.monthly_payment() * 5):
            return (self.initial_charge - 5 - month_pay)
        
        elif month == 7 and total_remaining > (self.monthly_payment() * 4):
            return (self.initial_charge - 4 - month_pay)
        
        elif month == 8 and total_remaining > (self.monthly_payment() * 3):
            return (self.initial_charge - 3 - month_pay)
        
        elif month == 9 and total_remaining > (self.monthly_payment() * 2):
            return (self.initial_charge - 2 - month_pay)

        elif month == 10 and total_remaining > (self.monthly_payment() * 1):
            return (self.initial_charge - 1 - month_pay)
        
        elif month == 11 and total_remaining > (self.monthly_payment() * 0):
            return (self.initial_charge - month_pay)
        
        elif month == 12 and total_remaining > (self.monthly_payment() * 0):
            return (self.initial_charge - month_pay)
        else :
            return 0
    
    # valor en mora
    def amountOwed(self):
        month = 8
        # calculamos los meses pagados
        month_pay = math.floor(self.total_paid() / self.monthly_payment())
        # total valor en mora restante
        total_remaining = self.total_year() - self.total_paid()

        if month == 2 and total_remaining > (self.monthly_payment() * 9):
            meses_mora = self.initial_charge - 9 - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))

        elif month == 3 and total_remaining > (self.monthly_payment() * 8):
            meses_mora = self.initial_charge - 8 - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))
        
        elif month == 4 and total_remaining > (self.monthly_payment() * 7):
            meses_mora = self.initial_charge - 7 - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))
        
        elif month == 5 and total_remaining > (self.monthly_payment() * 6):
            meses_mora = self.initial_charge - 6 - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))
        
        elif month == 6 and total_remaining > (self.monthly_payment() * 5):
            meses_mora = self.initial_charge - 5 - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))
        
        elif month == 7 and total_remaining > (self.monthly_payment() * 4):
            meses_mora = self.initial_charge - 4 - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))
        
        elif month == 8 and total_remaining > (self.monthly_payment() * 3):
            meses_mora = self.initial_charge - 3 - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))
        
        elif month == 9 and total_remaining > (self.monthly_payment() * 2):
            meses_mora = self.initial_charge - 2 - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))

        elif month == 10 and total_remaining > (self.monthly_payment() * 1):
            meses_mora = self.initial_charge - 1 - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))
        
        elif month == 11 and total_remaining > (self.monthly_payment() * 0):
            meses_mora = self.initial_charge - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))
        
        elif month == 12 and total_remaining > (self.monthly_payment() * 0):
            meses_mora = self.initial_charge - month_pay
            return ((meses_mora * self.monthly_payment())- (self.total_paid() -(month_pay * self.monthly_payment())))
        else :
            return 0



    def save(self, force_insert=False, force_update=False, update_fields=None, using=None, request=None):
        is_new = False
        if not self.id:
            is_new = True
            self.id = get_guid()
            # self.code = str(Student.objects.count() + 1).zfill(4)

        super(Student, self).save(force_insert,
                                  force_update, using, update_fields)
