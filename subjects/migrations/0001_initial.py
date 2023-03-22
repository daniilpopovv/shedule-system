# Generated by Django 4.1.7 on 2023-03-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название предмета')),
                ('hours', models.IntegerField(default=1, verbose_name='Часы')),
                ('image', models.ImageField(default='subjects_images/default.jpg', upload_to='subjects_images/')),
                ('exam_form', models.CharField(choices=[('ex', 'Экзамен'), ('zch', 'Зачет'), ('zo', 'Зачет с оценкой'), ('kr', 'Курсовая работа')], max_length=20, verbose_name='Экзаменационная форма')),
                ('num_cub', models.CharField(blank=True, choices=[('101', '101'), ('102', '102'), ('103', '103')], max_length=3, verbose_name='Кабинет')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['-id'],
            },
        ),
    ]
