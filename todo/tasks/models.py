from django.db import models
from django.forms import IntegerField

# Create your models here.

class Todo(models.Model): # Класс описывает структуру Палей в таблице Todo базы данных 
    title = models.CharField(max_length=1000) # Поле title имеет строковый тип длиной 1000 знаков
    description = models.CharField(max_length=1000, default='', verbose_name='описание')
    created_at = models.DateField(auto_now_add=True) 
    updated = models.DateField(auto_now=True)
    prace = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров0', default=0)
    status = models.ForeignKey('TodoStatus', default=None, null=True, on_delete= models.CASCADE) # внешний ключ, зависит от класса TodoStatus 
                                                                                                # on_delete= models.CASCADE говори каскадном удалении значений

    class Meta: # Мета данные модели которые позволяют изменять структуру таблицы в bd
        db_table = 'Tasks' # Переименование таблицы "tasks_Todo" в "Tasks"
        ordering = ['title'] # Сортировка таблицы аналогично "ODRER BY"

    def __str__(self): 
        return self.title

class TodoStatus(models.Model):
    name = models.CharField(max_length=100)

class TodoListView(generic.ListView):
    model = Todo