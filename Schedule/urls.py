from django.conf.urls.static import static
from django.urls import path

from ScheduleSystem import settings
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('schedule/', index, name='home'),
    path('logout/', user_logout, name='logout'),
    path('news/', HomeNews.as_view(), name='news'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    path('subjects/', SubjectsList.as_view(), name='subjects_list'),
    path('subjects/<int:pk>', ViewSubjects.as_view(), name='view_subjects'),
    path('schedule/<int:pk>/', ViewLessons.as_view(), name='view_lessons'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
