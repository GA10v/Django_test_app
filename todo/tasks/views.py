from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from tasks.models import Todo

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

# def todo_list(request, *args, **kwargs): 
#     return render(request, 'tasks/todo_list.html', {}) # необходимо создать папку templates, добавить в нее шаблон для страницы
#                                                        # и добавить наше приложение "tasks" в файле settings.py в переменную INSTALLED_APPS

def todo_list(request, *args, **kwargs):
    tasks = Todo.objects.all()
    return render(request, 'tasks/todo_list.html', {'tasks': tasks})

def tasks(request, *args, **kwargs):
    todo = [
        'сделать что-то 1',
        'сделать что-то 2',
        'сделать что-то 3'
    ]
    return render(request, 'tasks/tasks.html', {'tasks': todo})

def get_client_ip(request): # в функцию передается объект запроса
    ip = request.META.get('REMOTE_ADDR') # в переменную помещается IP адресс клиента
    session_count = request.session.get('num_visit',0) # В переменную добавляем номер сессии если её не существует возвращается 0
    request.session['num_visit'] = session_count+1 # при повторном запросе от пользователя счётчик сессий увеличивается на 1
    return render(request, 'info/user_info.html', {'ip_address': ip, 'session_count': session_count}) 


class About(View):
    def get(self, request):
        return render(request, 'tasks/about.html', {})

