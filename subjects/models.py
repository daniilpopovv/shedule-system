from django.db import models
from django.urls import reverse


class Subject(models.Model):
    id_teacher = models.ForeignKey('Schedule.Teacher', verbose_name='Преподаватель', on_delete=models.PROTECT,
                                   default=1)
    id_department = models.ForeignKey('Schedule.Department', verbose_name='Название кафедры', on_delete=models.PROTECT,
                                      default=1)
    id_course = models.ForeignKey('Schedule.Course', verbose_name='Курс', on_delete=models.PROTECT, default=1)
    id_educational_form = models.ForeignKey('Schedule.EducationalForm', verbose_name='Форма обучения',
                                            on_delete=models.PROTECT,
                                            default=1)
    id_group = models.ForeignKey('Schedule.Group', verbose_name='Номер группы', on_delete=models.PROTECT, default=1)
    name_subject = models.CharField(verbose_name='Название предмета', max_length=50)
    hours = models.IntegerField(verbose_name='Часы', default=1)
    exam_form = models.CharField(verbose_name='Экзаменационная форма', max_length=20)
    image_subject = models.ImageField(upload_to='subjects_images/', default='subjects_images/default.jpg')
    num_cub = models.CharField(verbose_name='Кабинет', max_length=20, blank=True)

    def __str__(self):
        return self.name_subject

    def get_absolute_url(self):
        return reverse('view_subjects', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['-id']
