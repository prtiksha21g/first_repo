from django.shortcuts import render
from django.http import HttpResponse
#function base view
#tke web req(http) and return respo(http)
#overall control over the functions
def first_fun(req):
       return HttpResponse('hello Team')

def home_fun(req):
       return HttpResponse('<h1>my home page </h1>')

#class base view
# Create your views here.
