from django.urls import path
from .views import home , public_reports

urlpatterns = [
    path('home/', home, name='home'),
    path('reports/<uuid:token>/',public_reports , name='reports'),
]