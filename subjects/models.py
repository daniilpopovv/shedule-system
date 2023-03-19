from django.db import models
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField(verbose_name='Название предмета', max_length=50)
    hours = models.IntegerField(verbose_name='Часы', default=1)
    image = models.ImageField(upload_to='subjects_images/', default='subjects_images/default.jpg')

    id_group = models.ForeignKey('timesheets.Group', verbose_name='Номер группы', on_delete=models.PROTECT, default=1)
    id_teacher = models.ForeignKey(
        'timesheets.Teacher',
        verbose_name='Преподаватель',
        on_delete=models.PROTECT,
        default=1
    )

    exam_form_choices = [
        ('ex', 'Экзамен'),
        ('zch', 'Зачет'),
        ('zo', 'Зачет с оценкой'),
        ('kr', 'Курсовая работа'),
    ]
    exam_form = models.CharField(verbose_name='Экзаменационная форма', max_length=20, choices=exam_form_choices)

    num_cub_choices = [
        ('101', '101'),
        ('102', '102'),
        ('103', '103'),
    ]
    num_cub = models.CharField(verbose_name='Кабинет', max_length=3, blank=True, choices=num_cub_choices)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_subjects', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['-id']
