from django.urls import path

from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', index, name='home'),
    path('ScheduleSystem/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/',get_category, name='category'),
    # path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('ScheduleSystem/<int:news_id>/', view_news, name='view_news'),
    # path('ScheduleSystem/add-ScheduleSystem/', add_news, name='add_news'),
    # path('ScheduleSystem/add-ScheduleSystem/', CreateNews.as_view(), name='add_news'),

]
