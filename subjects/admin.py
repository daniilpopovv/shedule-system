from django.contrib import admin

from .models import Subject


@admin.register(Subject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = (
        'name_subject', 'id_teacher', 'id_department', 'id_course', 'id_educational_form', 'id_group', 'exam_form',
        'hours')
    list_display_links = ('name_subject',)
    list_filter = ('id_teacher__name_teacher', 'id_department__name_department', 'id_course__number_course',
                   'id_educational_form__name_educational_form', 'id_group')
