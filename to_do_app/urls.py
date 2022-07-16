from django.contrib import admin
from django.urls import path
from . import views

app_name = 'to_do'
urlpatterns = [
    path('todos', views.index, name='todos'),
    path('todos/new', views.to_do, name='todo'),
    path('todos/<int:id>', views.view_details, name='details'),
    path('todos/<int:id>/edit', views.edit_details, name='edit'),
    path('todos/<int:id>/delete', views.delete, name='delete'),
    path('log_in', views.log_in, name='log_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('log_out', views.log_out, name='log_out'),
]
