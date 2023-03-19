from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, verbose_name='Логин студента', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='ФИО студента', max_length=50)
    id_group = models.ForeignKey('timesheets.Group', verbose_name='Группа', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
