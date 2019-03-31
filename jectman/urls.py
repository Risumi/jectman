from django.urls import path
from . import views

urlpatterns = [
    path('project', views.funcProject, name='funcProject'),
    path('backlog/<idProject>', views.funcBacklog, name='funcBacklog'),
]