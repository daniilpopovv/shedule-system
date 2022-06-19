from django.contrib import admin
from .models import *


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name_student','student_group')
    search_fields = ('name_student', 'id_group')

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
    list_display_links = ('id_teacher',)


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

# admin.site.register(Students, StudentsAdmin)
# admin.site.register(Courses, CoursesAdmin)
# admin.site.register(Departments, DepartmentsAdmin)
# admin.site.register(Subjects, SubjectsAdmin)
# admin.site.register(Groups, GroupsAdmin)
# admin.site.register(LessonsTime, LessonsTimeAdmin)
# admin.site.register(Attendance, AttendanceAdmin)
# admin.site.register(Teachers, TeachersAdmin)
# admin.site.register(EducationalForms, EducationalFormsAdmin)
# admin.site.register(Support, SupportAdmin)
# admin.site.register(WeekDays, WeekDaysAdmin)
# admin.site.register(Schedules, SchedulesAdmin)

# from .models import News, Category
#
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'content')
#     list_editable = ('is_published',)
#     list_filter = ('is_published', 'category')
#     fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
#     readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
#     save_on_top = True
#
#
#     def get_photo(self, obj):
#         if obj.photo:
#             return mark_safe(f'<img src="{obj.photo.url}" width="75" >')
#         else: return 'Фото не установлено'
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#
# admin.site.register(News, NewsAdmin)
# admin.site.register(Category, CategoryAdmin)
