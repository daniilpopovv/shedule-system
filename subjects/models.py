from django.db import models
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField(verbose_name='Название предмета', max_length=50, null=False, blank=False)
    hours = models.IntegerField(verbose_name='Часы', null=False, blank=False)
    image = models.ImageField(upload_to='subjects_images/', default='subjects_images/default.jpg')

    id_group = models.ForeignKey(
        'timesheets.Group',
        verbose_name='Номер группы',
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    id_teacher = models.ForeignKey(
        'timesheets.Teacher',
        verbose_name='Преподаватель',
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    exam_form_choices = [
        ('ex', 'Экзамен'),
        ('zch', 'Зачет'),
        ('zo', 'Зачет с оценкой'),
        ('kr', 'Курсовая работа'),
    ]
    exam_form = models.CharField(
        verbose_name='Экзаменационная форма',
        max_length=20,
        choices=exam_form_choices,
        null=False,
        blank=False
    )

    num_cub = models.IntegerField(verbose_name='Кабинет', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subject_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['name']
