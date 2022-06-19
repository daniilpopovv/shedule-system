from django.urls import path

from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('schedule/', index, name='home'),
    path('logout/', user_logout, name='logout'),
    path('news/', HomeNews.as_view(), name='news'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    path('schedule/<int:pk>/', ViewLessons.as_view(), name='view_lessons'),
]
