import imp
from django.shortcuts import render

from django.http import HttpResponse

def hotel(request):
    return render(request, 'pages/hotel-form.html')