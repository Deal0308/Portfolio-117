from django.urls import path
from content import views

urlpatterns = [
    path('projects_list/', views.projects_list, name='projects_list'),]