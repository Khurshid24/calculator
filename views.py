from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def free(request):

    return render(request, 'calculator/main.html')


def add(request):
    item1 = int(request.GET['val1'])
    item2 = int(request.GET['val2'])
    ans = item1 + item2
    return render(request, "calculator/result.html", {'answer':ans})

def subtract(request):
    item1 = int(request.GET['val1'])
    item2 = int(request.GET['val2'])
    ans = item1 - item2
    return render(request, "calculator/result.html", {'answer':ans})

def divide(request):
    item1 = int(request.GET['val1'])
    item2 = int(request.GET['val2'])
    ans = item1 / item2
    return render(request, "calculator/result.html", {'answer':ans})

def multiply(request):
    item1 = int(request.GET['val1'])
    item2 = int(request.GET['val2'])
    ans = item1 * item2
    return render(request, "calculator/result.html", {'answer':ans})

def blog(request):

    return render(request, 'calculator/index.html')
