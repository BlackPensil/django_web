from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
        <h1 style='background-color: yellow; text-align: center; border: solid; border-radius: 5px;'>Все ок!</h1>
    ''')
