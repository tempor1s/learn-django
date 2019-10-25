from django.urls import path
from django.views import generic

from . import views

app_name = 'pizza'
urlpatterns = [
    path('', views.index, name='index')
]