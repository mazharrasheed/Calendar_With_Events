import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Event
from django.shortcuts import redirect,render

def calendar_view(request):
    return render(request, 'calendar.html')

@require_http_methods(["POST"])
def add_event(request):
    data = json.loads(request.body)
    title = data.get('title')
    date = data.get('date')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    start_time_obj = datetime.strptime(start_time, '%H:%M').time()
    end_time_obj = datetime.strptime(end_time, '%H:%M').time()
    
    event = Event.objects.create(
        title=title,
        date=date_obj,
        start_time=start_time_obj,
        end_time=end_time_obj
    )
    return JsonResponse({
        'id': event.id,
        'title': event.title,
        'date': event.date.isoformat(),
        'start_time': event.start_time.strftime('%H:%M'),
        'end_time': event.end_time.strftime('%H:%M')
    })

@require_http_methods(["PUT"])
def update_event(request, event_id):
    data = json.loads(request.body)
    title = data.get('title')
    date = data.get('date')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    start_time_obj = datetime.strptime(start_time, '%H:%M').time()
    end_time_obj = datetime.strptime(end_time, '%H:%M').time()

    try:
        event = Event.objects.get(id=event_id)
        event.title = title
        event.date = date_obj
        event.start_time = start_time_obj
        event.end_time = end_time_obj
        event.save()
        return JsonResponse({
            'id': event.id,
            'title': event.title,
            'date': event.date.isoformat(),
            'start_time': event.start_time.strftime('%H:%M'),
            'end_time': event.end_time.strftime('%H:%M')
        })
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)

def get_events(request):
    events = Event.objects.all()
    event_list = []
    for event in events:
        start_datetime = f"{event.date.isoformat()}T{event.start_time.isoformat()}"
        end_datetime = f"{event.date.isoformat()}T{event.end_time.isoformat()}"

        event_list.append({
            'id': event.id,
            'title': event.title,
            'start': start_datetime,
            'end': end_datetime
        })
    return JsonResponse(event_list, safe=False)
