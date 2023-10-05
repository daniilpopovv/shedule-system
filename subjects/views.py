from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from subjects.models import *


class ViewSubjects(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'subjects/subjects_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        return Subject.objects.filter(id_group=self.request.user.student.id_group)


class ViewSubjectDetail(DetailView):
    model = Subject
    template_name = 'subjects/subject_detail.html'
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.filter(id_group=self.request.user.student.id_group)

        return context
