"""
Admin Panel URLs
"""

from django.urls import path
from Core.admin_views import (
    admin_login,
    admin_dashboard,
    admin_appointments,
    approve_appointment,
    reject_appointment,
    admin_logout,
    # Event management
    admin_events,
    add_event,
    edit_event,
    delete_event,
    approve_event,
    reject_event,
)

urlpatterns = [
    path('login/', admin_login, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('appointments/', admin_appointments, name='admin_appointments'),
    path('approve/<str:appointment_id>/', approve_appointment, name='approve_appointment'),
    path('reject/<str:appointment_id>/', reject_appointment, name='reject_appointment'),
    
    # Event management
    path('events/', admin_events, name='admin_events'),
    path('events/add/', add_event, name='add_event'),
    path('events/edit/<str:event_id>/', edit_event, name='edit_event'),
    path('events/delete/<str:event_id>/', delete_event, name='delete_event'),
    path('events/approve/<str:event_id>/', approve_event, name='approve_event'),
    path('events/reject/<str:event_id>/', reject_event, name='reject_event'),
    
    path('logout/', admin_logout, name='admin_logout'),
]
