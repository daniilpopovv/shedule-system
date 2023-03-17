from django.views.generic import ListView, DetailView

from subjects.models import *


class SubjectsList(ListView):
    model = Subject
    template_name = 'subjects/subjects_list.html'
    context_object_name = 'subjects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        auth_user = self.request.user
        if auth_user.is_staff == 0:
            subjects = Subject.objects.filter(id_group=auth_user.student.id_group)
            return subjects
        else:
            return Subject.objects.all()


class ViewSubjects(DetailView):
    model = Subject
    template_name = 'subjects/view_subjects.html'
    context_object_name = 'subjects_item'
