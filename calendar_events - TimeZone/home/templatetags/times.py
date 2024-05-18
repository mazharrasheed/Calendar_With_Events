

from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter(name='times')
def times(start, end):
    times = []
    start_time = datetime.strptime(start, '%H:%M').time()
    end_time = datetime.strptime(end, '%H:%M').time()

    # Convert to datetime objects to compare
    current_datetime = datetime.combine(datetime.today(), start_time)
    end_datetime = datetime.combine(datetime.today(), end_time)

    # Generate times in 30-minute increments
    while current_datetime <= end_datetime:
        times.append(current_datetime.strftime('%H:%M'))
        current_datetime += timedelta(minutes=30)

    return times






















# from django import template
# from datetime import time, timedelta,datetime

# register = template.Library()

# @register.filter(name='times')
# def times(start, end):
#     times = []
#     start_time = datetime.strptime(start, '%H:%M')
#     end_time = datetime.strptime(end, '%H:%M')
#     t = start_time
#     while t <= end_time:
#         times.append(t.strftime('%H:%M'))
#         t = (datetime.combine(datetime.today(), t) + timedelta(minutes=30)).time()
#     return times


# from django import template
# from datetime import datetime, timedelta

# register = template.Library()

# @register.filter(name='times')
# def times(start, end):

#     print("i m times")
#     times = []
#     start_time = datetime.strptime(start, '%H:%M').time()
#     end_time = datetime.strptime(end, '%H:%M').time()
#     current_time = start_time
#     print(current_time)
#     print(end_time)
#     while current_time <= end_time:
#         times.append(current_time.strftime('%H:%M'))
#         current_time = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=30)).time()
#         print(current_time)

    # return times
   
