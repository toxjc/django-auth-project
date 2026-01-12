from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.list_projects, name='list_projects'),
    path('projects/create/', views.create_project, name='create_project'),
]