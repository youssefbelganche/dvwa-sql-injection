from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('setup', views.setup, name='setup'),
    path('query', views.query, name='query'),
    path('check_flag', views.check_flag, name='check_flag'),
]
