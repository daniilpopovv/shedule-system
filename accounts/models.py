from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, verbose_name='Логин студента', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='ФИО студента', max_length=50)

    id_course = models.ForeignKey('timesheets.Course', verbose_name='Номер курса', on_delete=models.PROTECT, null=True)
    id_group = models.ForeignKey('timesheets.Group', verbose_name='Группа', on_delete=models.PROTECT, null=True)
    id_department = models.ForeignKey(
        'timesheets.Department',
        verbose_name='Кафедра',
        on_delete=models.PROTECT,
        null=True
    )
    id_educational_form = models.ForeignKey(
        'timesheets.EducationalForm',
        verbose_name='Форма обучения',
        on_delete=models.PROTECT,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['-id_course']
