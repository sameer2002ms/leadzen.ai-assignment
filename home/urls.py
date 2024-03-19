from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='todo_list'),
    path('add_todo/', views.Add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('complete_todo/<int:todo_id>/', views.todo_completed, name='complete_todo'),
]