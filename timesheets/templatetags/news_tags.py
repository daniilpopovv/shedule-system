import datetime

from django import template

from timesheets.models import Schedule

register = template.Library()


@register.inclusion_tag('timesheets/schedule.html', takes_context=True)
def show_categories(context):
    # получение request через context
    request = context['request']

    # переменная для отображения оповещения, что сегодня нет занятий
    freeday = 0

    # получение текущего дня недели для фильтрации расписания
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

    # проверка авторизован ли пользователь
    if request.user.is_authenticated:
        # проверка зашел ли именно студент, для корректного отображения расписания
        if request.user.is_staff == 1:
            namegroup = 'ВЫ АДМИН'
            schedule_today = ''
        else:
            namegroup = request.user.students.id_group
            schedule_today = Schedule.objects.filter(id_week_day__name_day=weekdayname, id_group=namegroup).order_by(
                'id_lessons_time__number_lesson')
            if not schedule_today:
                freeday = 1
    else:
        schedule_today = ''
        namegroup = ''

    return {"schedule_today": schedule_today, 'namegroup': namegroup, 'freeday': freeday}
