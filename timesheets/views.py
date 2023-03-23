from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from timesheets.models import Lesson, Attendance
from .forms import AttendanceForm

weekday_today = timezone.now().strftime('%A').lower()


class ViewTimesheet(LoginRequiredMixin, ListView):
    model = Lesson
    template_name = 'timesheets/timesheet.html'
    context_object_name = 'timesheet'

    def get_queryset(self):
        return Lesson.objects.filter(
            id_subject__id_group=self.request.user.student.id_group,
            weekday=weekday_today
        )


class ViewLessonDetail(LoginRequiredMixin, FormMixin, DetailView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'timesheets/lesson_detail.html'
    form_class = AttendanceForm

    def get_success_url(self):
        lesson = self.get_object()
        pk = lesson.id
        return reverse_lazy('lesson_detail', kwargs={'pk': pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_group = self.request.user.student.id_group

        context['attendance_form'] = self.get_form()
        context['timesheet'] = Lesson.objects.filter(
            id_subject__id_group=id_group,
            weekday=weekday_today
        )
        self.update_attendance_status(context)

        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            lesson = self.get_object()
            attendance = Attendance(
                date=timezone.localdate(),
                subject=f"{lesson.id_subject.name} {lesson.time_start}-{lesson.time_end}",
                id_student=self.request.user.student
            )
            attendance.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def update_attendance_status(self, context):
        lesson = self.get_object()
        lesson_start_time = lesson.time_start
        lesson_end_time = lesson.time_end
        time_now = timezone.localtime().time()

        if time_now < lesson_start_time:
            context['attendance_status'] = 'wait'
        elif lesson_start_time <= time_now <= lesson_end_time:
            context['attendance_status'] = 'can'
        elif time_now > lesson_end_time:
            context['attendance_status'] = 'late'

        if Attendance.objects.filter(
                date=timezone.localdate(),
                subject=f"{lesson.id_subject.name} {lesson.time_start}-{lesson.time_end}",
                id_student=self.request.user.student
        ).exists():
            context['attendance_status'] = 'visited'
