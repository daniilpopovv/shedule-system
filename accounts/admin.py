from django.contrib import admin

from accounts.models import *


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'id_course', 'id_group', 'id_department', 'id_educational_form')

    def student_group(self, obj):
        return obj.id_group.name

    student_group.short_description = 'Название группы'
