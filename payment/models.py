from django.db import models
from base.models import Base
from users.models import Student

# Create your models here.


class Payment(Base):
    value = models.IntegerField('Valor')
    reference = models.CharField('Referencia', max_length=50, null=True, blank=True)
    description = models.CharField('Concepto', max_length=100)
    method = models.CharField('Metodo de Pago', max_length=30, null=True, blank=True)
    student = models.ForeignKey(Student, verbose_name='Estudiante', related_name='payments', on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['-create']

    def __str__(self):
        return self.description


class CompromisePay(Base):
    STATES = (
        (1, 'Pendiente'),
        (2, 'Incumplido'),
        (3, 'Cumplido'),)

    student = models.ForeignKey(Student, verbose_name='Estudiante', related_name='compromises', on_delete=models.CASCADE)
    person_charge = models.CharField('Responsable', max_length=100)
    document = models.CharField('Documento', max_length=100)
    value = models.IntegerField('Valor')
    month_owed = models.IntegerField('Cantidad de Mensualidades')
    date_pay = models.DateField('Fecha de Pago')
    state = models.PositiveSmallIntegerField('Estado', choices=STATES, default=1)
    

    class Meta():
        verbose_name = 'Compromiso'
        verbose_name_plural = 'Compromisos'
        ordering = ['-create']

    def __str__(self):
        return self.person_charge
