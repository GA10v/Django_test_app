from django.urls import path
from .import views # Импортируем модуль из внутреннего каталога

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('tasks', views.tasks, name='tasks'),
    path('user_info', views.get_client_ip, name='get_client_ip' ),
    path('about', views.About.as_view, name='about') # метод as_view класса About, автоматически определяет тип запроса (GET или POST)
                                                    # и сам подставляет нужную функцию
] 