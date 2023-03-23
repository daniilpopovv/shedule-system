from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, verbose_name='Логин студента', on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(verbose_name='ФИО студента', max_length=50, null=False, blank=False)
    id_group = models.ForeignKey(
        'timesheets.Group',
        verbose_name='Группа',
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name + self.id_group.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['name']
