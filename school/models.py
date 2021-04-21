from django.db import models
from base.models import Base

# Create your models here.


class Grade(Base):
    name = models.CharField('Nombre', max_length=15)
    abbreviation = models.CharField('Abreviacion', default='00', max_length=4)
    monthly_pay = models.IntegerField('Mensualidad')
    enrollment = models.IntegerField('Matricula')

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
        ordering = ['-create']

    def __str__(self):
        return self.name

    __deleted = None

    # total recaudado
    def total_raised(self):
        total = 0
        for student in self.students.all():
            total = total + student.total_paid()
        return total
    

    def __init__(self, *args, **kwargs):
        super(Grade, self).__init__(*args, **kwargs)
        self.__deleted = self.deleted

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.deleted != self.__deleted:
            for student in self.students.all():
                student.user.deleted = True
                student.user.is_active = False
                student.save()
                student.user.save()

        super(Grade, self).save(force_insert, force_update, *args, **kwargs)
        self.__deleted = self.deleted
