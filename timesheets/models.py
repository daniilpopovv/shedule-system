from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Student(models.Model):
    user = models.OneToOneField(User, verbose_name='Логин студента', on_delete=models.CASCADE)
    name_student = models.CharField(verbose_name='ФИО студента', max_length=50)
    id_course = models.ForeignKey('timesheets.Course', verbose_name='Номер курса', on_delete=models.PROTECT, null=True)
    id_department = models.ForeignKey('timesheets.Department', verbose_name='Кафедра', on_delete=models.PROTECT,
                                      null=True)
    id_group = models.ForeignKey('timesheets.Group', verbose_name='Группа', on_delete=models.PROTECT, null=True)
    id_educational_form = models.ForeignKey('timesheets.EducationalForm', verbose_name='Форма обучения',
                                            on_delete=models.PROTECT,
                                            null=True)

    def __str__(self):
        return self.name_student

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['-id_course']

    # @receiver(post_save, sender=User)
    # def create_or_update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Students.objects.create(user=instance)
    #     instance.profile.save()


class Department(models.Model):
    name_department = models.CharField(verbose_name='Название кафедры', max_length=70)

    def __str__(self):
        return self.name_department

    class Meta:
        verbose_name = 'Название кафедры'
        verbose_name_plural = 'Кафедры'
        ordering = ['-id']


class Course(models.Model):
    number_course = models.IntegerField(verbose_name='Номер курса')

    def __str__(self):
        return str(self.number_course)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-id']


class LessonTime(models.Model):
    number_lesson = models.IntegerField(verbose_name='Номер пары')
    time_lesson = models.CharField(verbose_name='Время пары', max_length=20)

    def __str__(self):
        return self.time_lesson

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'
        ordering = ['-number_lesson']


class Attendance(models.Model):
    date_attendance = models.DateField(verbose_name='Дата посещаемости')
    id_lesson = models.ForeignKey('timesheets.LessonTime', on_delete=models.PROTECT, default=1)
    attendance = models.BooleanField(verbose_name='Присутствие', default=False)
    id_student = models.ForeignKey('timesheets.Student', on_delete=models.PROTECT, default=1)
    id_subject = models.ForeignKey('subjects.Subject', on_delete=models.PROTECT, default=1)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Посещаемость'
        verbose_name_plural = 'Посещаемость'
        ordering = ['-id']


class Teacher(models.Model):
    name_teacher = models.CharField(verbose_name='ФИО преподавателя', max_length=50)

    def __str__(self):
        return self.name_teacher

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['-id']


class EducationalForm(models.Model):
    name_educational_form = models.CharField(verbose_name='Название формы обучения', max_length=30)

    def __str__(self):
        return self.name_educational_form

    class Meta:
        verbose_name = 'Форма обучения'
        verbose_name_plural = 'Формы обучения'
        ordering = ['-id']


class Support(models.Model):
    name_support = models.CharField(verbose_name='Имя поддержки', max_length=100)
    email_support = models.EmailField(verbose_name='Почта поддержки')
    message_support = models.CharField(verbose_name='Сообщение', max_length=300)

    def __str__(self):
        return self.name_support

    class Meta:
        verbose_name = 'Поддержка'
        verbose_name_plural = 'Поддержка'
        ordering = ['-id']


class WeekDay(models.Model):
    name_day = models.CharField(verbose_name='Название дня недели', max_length=20)

    def __str__(self):
        return self.name_day

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'
        ordering = ['-id']


class Schedule(models.Model):
    id_group = models.ForeignKey('timesheets.Group', verbose_name='Группа', on_delete=models.PROTECT, default=1)
    id_subject = models.ForeignKey('subjects.Subject', verbose_name='Предмет', on_delete=models.PROTECT, default=1)
    id_lessons_time = models.ForeignKey('timesheets.LessonTime', verbose_name='Номер пары', on_delete=models.PROTECT,
                                        default=1)
    id_week_day = models.ForeignKey('timesheets.WeekDay', verbose_name='День недели', on_delete=models.PROTECT, default=1)

    def get_absolute_url(self):
        return reverse('view_lessons', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        ordering = ['-id']


class Group(models.Model):
    name_group = models.CharField(verbose_name='Название группы', max_length=30)

    def __str__(self):
        return self.name_group

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['-id']
