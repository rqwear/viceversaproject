from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['text-to-txet']
    reverse_text = user_text[::-1]
    return render(request, 'reverse.html', {'user_text': reverse_text})