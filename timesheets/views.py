import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from timesheets.models import Lesson, Attendance
from .forms import AttendanceForm


class ViewTimesheet(ListView):
    model = Lesson
    template_name = 'timesheets/timesheet.html'
    context_object_name = 'schedule_today'
    weekday_today = datetime.datetime.now().strftime('%A').lower()

    def get_queryset(self):
        id_group = self.request.user.student.id_group
        return Lesson.objects.filter(id_subject__id_group=id_group, weekday=self.__class__.weekday_today)


class ViewLessons(LoginRequiredMixin, FormMixin, DetailView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'timesheets/lesson_detail.html'
    form_class = AttendanceForm
    success_url = reverse_lazy('timesheets:timesheet')

    weekday_today = datetime.datetime.now().strftime('%A').lower()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_group = self.request.user.student.id_group

        context['schedule_today'] = Lesson.objects.filter(
            id_subject__id_group=id_group,
            weekday=self.__class__.weekday_today
        )

        context['attendance_form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            lesson = self.get_object()
            attendance = Attendance(
                date=datetime.datetime.now(),
                is_attendance=True,
                id_lesson=lesson.id,
                id_student=self.request.user.student.id,
                id_subject=lesson.id_subject
            )
            attendance.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # Handle POST GTTP requests
    # def post(self, request, *args, **kwargs):
    #     form = self.form(request.POST)
    #     primary_key = self.kwargs.get('pk')
    #     schedule = Schedule.objects.get(id=primary_key)
    #     attendance = Attendance(date_attendance=datetime.datetime.today(), id_lesson=schedule.id_lessons_time,
    #                             attendance=False,
    #                             id_student_id=request.user.students.id, id_subject=schedule.id_subject)
    #
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         attendance.attendance = True
    #         attendance.save()
    #         return redirect('timesheet')
    #
    #     return render(request, self.template_name, {'form': form})

    # def get_context_data(self, *args, **kwargs):
    #     # получение объекта авторизованного пользователя
    #     auth_user = self.request.user
    #
    #     # создание формы
    #     form = self.form()
    #
    #     # получение контекста и pk для работы с БД
    #     context = super(ViewLessons, self).get_context_data(**kwargs)  # returns a dictionary of context
    #     primary_key = self.kwargs.get('pk')
    #
    #     # получение экзмепляра модели по pk отображаемого предмета
    #     schedule = Schedule.objects.get(id=primary_key)
    #
    #     # значения по умолчанию для проверки
    #     canattend = 1
    #     subject_started = 0
    #
    #     try:
    #         attendance = Attendance.objects.get(date_attendance=datetime.datetime.today(),
    #                                             id_lesson=schedule.id_lessons_time,
    #                                             id_student=auth_user.student.id,
    #                                             id_subject=schedule.id_subject).attendance
    #     except Attendance.DoesNotExist:
    #         attendance = 0
    #
    #     # получение текущего времени
    #     time_now = datetime.datetime.now()
    #     h_now = int(time_now.hour)
    #     m_now = int(time_now.minute)
    #     now = h_now * 60 + m_now
    #
    #     # проверка времени и возможности отметиться
    #     if schedule.id_lessons_time.number_lesson == 1:
    #         start = 510
    #         end = 605
    #         if start < now < end:
    #             subject_started = 1
    #         if now > end:
    #             canattend = 0
    #     elif schedule.id_lessons_time.number_lesson == 2:
    #         start = 615
    #         end = 710
    #         if start < now < end:
    #             subject_started = 1
    #         if now > end:
    #             canattend = 0
    #     elif schedule.id_lessons_time.number_lesson == 3:
    #         start = 740
    #         end = 835
    #         if start < now < end:
    #             subject_started = 1
    #         if now > end:
    #             canattend = 0
    #     elif schedule.id_lessons_time.number_lesson == 4:
    #         start = 840
    #         end = 935
    #         if start < now < end:
    #             subject_started = 1
    #         if now > end:
    #             canattend = 0
    #
    #     # передача объектов в контексте
    #     new_context_objects = {'schedule': schedule, 'form': form, 'attendance': attendance,
    #                            'canattend': canattend, 'subject_started': subject_started}
    #     context.update(new_context_objects)
    #     return context
