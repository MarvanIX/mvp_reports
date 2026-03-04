from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('reports.urls')),
    path('logout/', LogoutView.as_view(next_page='users/login.html'), name='logout'),
]
