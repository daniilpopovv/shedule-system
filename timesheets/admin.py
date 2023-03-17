from django.contrib import admin

from timesheets.models import *


@admin.register(Lesson)
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('id_subject', 'weekday', 'time_start', 'time_end')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'is_attendance',
                    'id_lesson', 'id_student',)


@admin.register(Department)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(EducationalForm)
class EducationalFormsAdmin(admin.ModelAdmin):
    list_display = ('name',)
