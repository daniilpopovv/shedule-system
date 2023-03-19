from django.conf.urls.static import static
from django.urls import path

from ScheduleSystem import settings
from .views import *

urlpatterns = [
                  path('', ViewTimesheet.as_view(), name='timesheet'),
                  path('<int:pk>/', ViewLessonDetail.as_view(), name='view_lessons'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
