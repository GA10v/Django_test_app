from django.urls import path
from .import views # Импортируем модуль из внутреннего каталога

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('tasks', views.tasks, name='tasks')
]