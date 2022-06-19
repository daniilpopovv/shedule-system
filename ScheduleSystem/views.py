import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

import ScheduleSystem
from .forms import UserLoginForm, AttendanceForm
from .models import *


def index(request):
    context = {
        'ScheduleSystem': ScheduleSystem,
        'title': 'Ваше расписание',
    }
    return render(request, template_name='ScheduleSystem/index.html', context=context)


class HomeNews(ListView):
    model = News
    template_name = 'ScheduleSystem/news_list.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ViewNews(DetailView):
    model = News
    template_name = 'ScheduleSystem/view_news.html'
    context_object_name = 'news_item'


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'ScheduleSystem/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


class ViewLessons(LoginRequiredMixin, DetailView):
    model = Schedules
    context_object_name = 'schedule_item'
    template_name = 'ScheduleSystem/schedule_detail.html'
    form = AttendanceForm

    # Handle POST GTTP requests
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        primary_key = self.kwargs.get('pk')
        schedule = Schedules.objects.get(id=primary_key)
        attendance = Attendance(date_attendance=datetime.datetime.today(), id_lesson=schedule.id_lessons_time,
                                attendance=False,
                                id_student_id=request.user.students.id, id_subject=schedule.id_subject)

        if form.is_valid():
            print(form.cleaned_data)
            attendance.attendance = True
            attendance.save()
            return redirect('home')

        return render(request, self.template_name, {'form': form})

    def get_context_data(self, *args, **kwargs):
        # получение объекта авторизованного пользователя
        auth_user = self.request.user

        # создание формы
        form = self.form()

        # получение контекста и pk для работы с БД
        context = super(ViewLessons, self).get_context_data(**kwargs)  # returns a dictionary of context
        primary_key = self.kwargs.get('pk')

        # получение экзмепляра модели по pk отображаемого предмета
        schedule = Schedules.objects.get(id=primary_key)

        # значения по умолчанию для проверки
        canattend = 1

        try:
            attendance = Attendance.objects.get(date_attendance=datetime.datetime.today(),
                                                id_lesson=schedule.id_lessons_time,
                                                id_student=auth_user.students.id,
                                                id_subject=schedule.id_subject).attendance
        except Attendance.DoesNotExist:
            attendance = 0

        # получение текущего времени
        time_now = datetime.datetime.now()
        h_now = int(time_now.hour)
        m_now = int(time_now.minute)
        now = h_now * 60 + m_now

        # проверка времени и возможности отметиться
        if schedule.id_lessons_time.number_lesson == 1:
            start = 510
            end = 605
            if start < now < end:
                canattend = 1
        elif schedule.id_lessons_time.number_lesson == 2:
            start = 615
            end = 710
            if start < now < end:
                canattend = 1
        elif schedule.id_lessons_time.number_lesson == 3:
            start = 740
            end = 835
            if start < now < end:
                canattend = 1
        elif schedule.id_lessons_time.number_lesson == 4:
            start = 840
            end = 935
            if start < now < end:
                canattend = 1

        # передача объектов в контексте
        new_context_objects = {'schedule': schedule, 'form': form, 'attendance': attendance,
                               'canattend': canattend}
        context.update(new_context_objects)
        return context
