from django.contrib import admin

from subjects.models import Subject


@admin.register(Subject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'hours', 'image', 'id_course', 'id_group', 'id_group', 'id_teacher',
        'id_department', 'id_educational_form', 'exam_form', 'num_cub')
