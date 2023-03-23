from django.urls import path

from .views import *

urlpatterns = [
    path('', ViewTimesheet.as_view(), name='timesheet'),
    path('<int:pk>/', ViewLessonDetail.as_view(), name='lesson_detail'),
]
