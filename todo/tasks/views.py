from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
''' простое представление страницы без использования шаблонов '''
# def todo_list(requset, *args, **kwargs):
    # return HttpResponse(
    #     '<ul>'
    #     '<li> - сделать 1</li>'
    #     '<li> - сделать 2</li>'
    #     '<li> - сделать 3</li>'
    #     '<li> - сделать 4</li>'
    #     '</ul>'
    # )

def todo_list(request, *args, **kwargs): 
    return render(request, 'tasks/todo_list.html', {}) # необходимо создать папку templates, добавить в нее шаблон для страницы
                                                       # и добавить наше приложение "tasks" в файле settings.py в переменную INSTALLED_APPS

def tasks(request, *args, **kwargs):
    return render(request, 'tasks/tasks.html', {})