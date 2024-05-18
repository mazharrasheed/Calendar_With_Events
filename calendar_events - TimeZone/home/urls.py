from django.urls import path
from .views import calendar_view, add_event, update_event,get_events

urlpatterns = [
    path('', calendar_view, name='calendar'),
    path('add_event/', add_event, name='add_event'),
    path('update_event/<int:event_id>/', update_event, name='update_event'),

    path('', calendar_view, name='calendar'),
    path('get_events/', get_events, name='get_events'),
    path('add_event/', add_event, name='add_event'),
    path('update_event/<int:event_id>/', update_event, name='update_event'),
]