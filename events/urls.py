from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events import views

app_name = 'events'

router = DefaultRouter()
router.register('',views.EventView, 'events')

urlpatterns = [
    path('events/', include(router.urls)),
    #path('events/all/', views.all_events, name='all-events'),
    path('event/<int:pk>/', views.event_detail, name='event-detail'),
]
