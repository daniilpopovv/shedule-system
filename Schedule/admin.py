from django.contrib import admin

from .models import *


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name_student', 'student_group')
    search_fields = ('name_student', 'id_group')
    list_filter = ('id_group', 'id_course__number_course', 'id_department__name_department', 'id_educational_form')

    def student_group(self, obj):
        return obj.id_group.name_group

    student_group.short_description = 'Название группы'


@admin.register(Department)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name_department',)
    list_display_links = ('name_department',)
    search_fields = ('name_department',)


@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('number_course',)
    list_display_links = ('number_course',)


@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name_group',)
    list_display_links = ('name_group',)
    search_fields = ('name_group',)


@admin.register(LessonTime)
class LessonsTimeAdmin(admin.ModelAdmin):
    list_display = ('number_lesson', 'time_lesson')
    list_display_links = ('number_lesson',)
    search_fields = ('number_lesson',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date_attendance', 'id_lesson',
                    'attendance', 'id_student', 'id_subject')
    list_display_links = ('attendance',)
    list_filter = ('date_attendance', 'id_subject__name_subject', 'id_student__id_group__name_group')


@admin.register(Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name_teacher',)
    list_display_links = ('name_teacher',)
    search_fields = ('name_teacher',)


@admin.register(EducationalForm)
class EducationalFormsAdmin(admin.ModelAdmin):
    list_display = ('name_educational_form',)


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('name_support', 'email_support',
                    'message_support')
    list_display_links = ('name_support', 'email_support')
    search_fields = ('name_support', 'email_support')


@admin.register(WeekDay)
class WeekDaysAdmin(admin.ModelAdmin):
    list_display = ('name_day',)


@admin.register(Schedule)
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('id_group', 'id_subject', 'id_lessons_time', 'id_week_day',)
    list_display_links = ('id_subject',)
    list_filter = ('id_group', 'id_subject__name_subject', 'id_lessons_time__time_lesson', 'id_week_day',)
    ordering = ('id_lessons_time__number_lesson',)
