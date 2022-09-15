from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



# def say_hello(request):
#     return HttpResponse('Hello World') 
#     # Here we are returning an instance of the HttpResponse Class. 
    # return render(request, 'hello.html')

def say_hello(request):
    # return HttpResponse('Hello World') 
    # Here we are returning an instance of the HttpResponse Class. 
    return render(request, 'hello.html', {'name': 'Mosh'})
