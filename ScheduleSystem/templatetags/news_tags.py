import datetime
from django import template
from ScheduleSystem.models import Schedules

register = template.Library()


@register.inclusion_tag('ScheduleSystem/list_categories.html')
def show_categories():
    weekdaynow = datetime.datetime.today().isoweekday()
    weekdayname = 'Неизвестно'
    if weekdaynow == 1:
        weekdayname = 'Понедельник'
    elif weekdaynow == 2:
        weekdayname = 'Вторник'
    elif weekdaynow == 3:
        weekdayname = 'Среда'
    elif weekdaynow == 4:
        weekdayname = 'Четверг'
    elif weekdaynow == 5:
        weekdayname = 'Пятница'
    elif weekdaynow == 6:
        weekdayname = 'Суббота'
    elif weekdaynow == 7:
        weekdayname = 'Воскресенье'

    schedule_today = Schedules.objects.filter(id_week_day__name_day=weekdayname).order_by(
        'id_lessons_time__number_lesson')
    return {"schedule_today": schedule_today}
