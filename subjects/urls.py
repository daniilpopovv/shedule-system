from django.urls import path

from .views import *

urlpatterns = [
    path('', SubjectsList.as_view(), name='subjects_list'),
    path('<int:pk>/', ViewSubjects.as_view(), name='view_subjects'),
]
