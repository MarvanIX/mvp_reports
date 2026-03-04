from django.urls import path
from .views import home , public_reports,company_view, reports_view, mark_notification_read

urlpatterns = [
    path('home/', home, name='home'),
    path('reports/<uuid:token>/',public_reports , name='submit_report'),
    path('company/', company_view, name='company'),
    path('reports/', reports_view, name='manager_reports'),
    path('notifications/read/<int:pk>/', mark_notification_read, name='mark_notification_read'),

]