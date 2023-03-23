from django.contrib import admin

from subjects.models import Subject


@admin.register(Subject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'hours', 'image', 'id_group', 'id_teacher', 'exam_form', 'num_cub')
    list_filter = ('name', 'id_group', 'id_teacher', 'exam_form', 'num_cub')
