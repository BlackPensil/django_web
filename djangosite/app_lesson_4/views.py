from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
        <h1 style='background-color: orange; text-align: center; border: solid; border-radius: 5px;'>Домашка по 4 занятию</h1>
    ''')
