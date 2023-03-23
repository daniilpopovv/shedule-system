from django.contrib import admin

from accounts.models import *


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'id_group')
    list_filter = ('id_group',)
