from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .query import schema


urlpatterns = [
    path('project', views.funcProject, name='funcProject'),
    path('backlog/<idProject>', views.funcBacklog, name='funcBacklog'),
    url(r'^graphql',csrf_exempt(GraphQLView.as_view(graphiql=True,schema=schema)) ),
]