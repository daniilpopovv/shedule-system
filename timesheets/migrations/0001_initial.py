# Generated by Django 4.1.7 on 2023-03-22 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Название кафедры')),
            ],
            options={
                'verbose_name': 'Название кафедры',
                'verbose_name_plural': 'Кафедры',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО преподавателя')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=10, verbose_name='День недели')),
                ('time_start', models.IntegerField(choices=[(1, '09:00'), (2, '11:00'), (3, '13:00')], verbose_name='Время занятия')),
                ('time_end', models.IntegerField(choices=[(1, '10:30'), (2, '12:30'), (3, '14:30')], verbose_name='Время занятия')),
                ('id_subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='subjects.subject', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название группы')),
                ('educational_form', models.CharField(choices=[('o', 'Очная'), ('zo', 'Заочная')], max_length=30, verbose_name='Название формы обучения')),
                ('course', models.IntegerField(choices=[(1, '1'), (1, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Номер курса')),
                ('id_department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='timesheets.department', verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата посещения')),
                ('subject', models.CharField(max_length=50, verbose_name='Название предмета')),
                ('id_student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.student')),
            ],
            options={
                'verbose_name': 'Посещаемость',
                'verbose_name_plural': 'Посещаемость',
                'ordering': ['-id'],
            },
        ),
    ]
