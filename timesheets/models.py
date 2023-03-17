from django.db import models
from django.urls import reverse


class Lesson(models.Model):
    id_subject = models.ForeignKey('subjects.Subject', verbose_name='Предмет', on_delete=models.PROTECT, default=1)

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
        choices=weekday_choices
    )

    time_start_choices = [
        (1, '09:00'),
        (2, '11:00'),
        (3, '13:00'),
    ]
    time_start = models.IntegerField(
        verbose_name='Время занятия',
        choices=time_start_choices,
    )

    time_end_choices = [
        (1, '10:30'),
        (2, '12:30'),
        (3, '14:30'),
    ]
    time_end = models.IntegerField(
        verbose_name='Время занятия',
        choices=time_end_choices,
    )

    def get_absolute_url(self):
        return reverse('view_lessons', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        ordering = ['-id']


class Attendance(models.Model):
    date = models.DateField(verbose_name='Дата посещения')
    is_attendance = models.BooleanField(verbose_name='Присутствие', default=False)
    id_lesson = models.ForeignKey('timesheets.Lesson', on_delete=models.PROTECT)
    id_student = models.ForeignKey('accounts.Student', on_delete=models.PROTECT, default=1)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Посещаемость'
        verbose_name_plural = 'Посещаемость'
        ordering = ['-id']


class Department(models.Model):
    name = models.CharField(verbose_name='Название кафедры', max_length=70)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название кафедры'
        verbose_name_plural = 'Кафедры'
        ordering = ['-id']


class Course(models.Model):
    number = models.IntegerField(verbose_name='Номер курса')

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-id']


class Group(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['-id']


class Teacher(models.Model):
    name = models.CharField(verbose_name='ФИО преподавателя', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['-id']


class EducationalForm(models.Model):
    name = models.CharField(verbose_name='Название формы обучения', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обучения'
        verbose_name_plural = 'Формы обучения'
        ordering = ['-id']
