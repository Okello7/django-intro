from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# take request and return response handler.

def say_hello(request):
    x=1
    y=2

    return render(request, 'hello.html', {'name':'Okello'})

    #Pull data fromm a database
    #Transformdata 
    #Send emails etc

