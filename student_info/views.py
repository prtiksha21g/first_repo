from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student_fun(request):
     #s='<h1>hello welcm </h1>'
     return HttpResponse('Hello Brainworks')