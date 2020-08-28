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
