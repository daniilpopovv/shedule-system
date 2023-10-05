from django.contrib import admin

from timesheets.models import *


@admin.register(Lesson)
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('id_subject', 'weekday', 'time_start', 'time_end',)
    list_filter = ('id_subject', 'weekday', 'time_start')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'subject', 'id_student',)
    list_filter = ('subject',)


@admin.register(Department)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_department', 'educational_form', 'course',)
    list_filter = ('id_department', 'educational_form', 'course',)


@admin.register(Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name',)
