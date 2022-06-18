from django import template
from ScheduleSystem.models import Attendance
from datetime import date
register = template.Library()


@register.inclusion_tag('ScheduleSystem/list_categories.html')
def show_categories():
    schedule_today = Attendance.objects.filter(date_attendance=date.today()).order_by('id_lesson__number_lesson')
    return {"schedule_today": schedule_today}
