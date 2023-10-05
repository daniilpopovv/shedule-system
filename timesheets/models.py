from django.db import models
from django.urls import reverse


class Lesson(models.Model):
    id_subject = models.ForeignKey(
        'subjects.Subject',
        verbose_name='Предмет',
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    weekday_choices = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    weekday = models.CharField(
        verbose_name='День недели',
        max_length=10,
        choices=weekday_choices,
        null=False,
        blank=False
    )

    time_start = models.TimeField(verbose_name='Время начала занятия', null=False, blank=False)
    time_end = models.TimeField(verbose_name='Время окончания занятия', null=False, blank=False)

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
        ordering = ['id_subject']


class Attendance(models.Model):
    date = models.DateField(verbose_name='Дата посещения', null=False, blank=False)
    subject = models.CharField(verbose_name='Название предмета', null=False, blank=False, max_length=50)
    id_student = models.ForeignKey(
        'accounts.Student',
        verbose_name='Студент',
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
        ordering = ['-date']


class Department(models.Model):
    name = models.CharField(verbose_name='Название кафедры', max_length=70)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'
        ordering = ['name']


class Group(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=30, null=False, blank=False)

    id_department = models.ForeignKey(
        'timesheets.Department',
        verbose_name='Кафедра',
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    educational_form_choices = [
        ('o', 'Очная'),
        ('zo', 'Заочная'),
    ]
    educational_form = models.CharField(
        verbose_name='Название формы обучения',
        max_length=30,
        choices=educational_form_choices,
        null=False,
        blank=False
    )

    course_choices = [
        (1, '1'),
        (1, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    course = models.IntegerField(
        verbose_name='Номер курса',
        choices=course_choices,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']


class Teacher(models.Model):
    name = models.CharField(verbose_name='ФИО преподавателя', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['name']
