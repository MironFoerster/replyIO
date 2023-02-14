from django.urls import path
from . import views

app_name = 'FileInOut'

urlpatterns = [
    path('', views.index, name='index'),
]
