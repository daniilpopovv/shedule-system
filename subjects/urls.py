from django.urls import path

from .views import *

urlpatterns = [
    path('', ViewSubjects.as_view(), name='subjects'),
    path('<int:pk>/', ViewSubjectDetail.as_view(), name='subject_detail'),
]
