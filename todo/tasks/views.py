from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todo_list(requset, *args, **kwargs):
    return HttpResponse(
        '<ul>'
        '<li> - сделать 1</li>'
        '<li> - сделать 2</li>'
        '<li> - сделать 3</li>'
        '<li> - сделать 4</li>'
        '</ul>'
    )