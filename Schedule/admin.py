from django.contrib import admin

from .models import *


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name_student', 'student_group')
    search_fields = ('name_student', 'id_group')
    list_filter = ('id_group', 'id_course__number_course', 'id_department__name_department', 'id_educational_form')

    def student_group(self, obj):
        return obj.id_group.name_group

    student_group.short_description = 'Название группы'


@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name_department',)
    list_display_links = ('name_department',)
    search_fields = ('name_department',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('number_course',)
    list_display_links = ('number_course',)


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = (
        'name_subject', 'id_teacher', 'id_department', 'id_course', 'id_educational_form', 'id_group', 'exam_form',
        'hours')
    list_display_links = ('name_subject',)
    list_filter = ('id_teacher__name_teacher', 'id_department__name_department', 'id_course__number_course',
                   'id_educational_form__name_educational_form', 'id_group')


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name_group',)
    list_display_links = ('name_group',)
    search_fields = ('name_group',)


@admin.register(LessonsTime)
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


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name_teacher',)
    list_display_links = ('name_teacher',)
    search_fields = ('name_teacher',)


@admin.register(EducationalForms)
class EducationalFormsAdmin(admin.ModelAdmin):
    list_display = ('name_educational_form',)


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('name_support', 'email_support',
                    'message_support')
    list_display_links = ('name_support', 'email_support')
    search_fields = ('name_support', 'email_support')


@admin.register(WeekDays)
class WeekDaysAdmin(admin.ModelAdmin):
    list_display = ('name_day',)


@admin.register(Schedules)
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('id_group', 'id_subject', 'id_lessons_time', 'id_week_day',)
    list_display_links = ('id_subject',)
    list_filter = ('id_group', 'id_subject__name_subject', 'id_lessons_time__time_lesson', 'id_week_day',)
    ordering = ('id_lessons_time__number_lesson',)
