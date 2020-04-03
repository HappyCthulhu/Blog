from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
import blogproject.templates

def main(request):
    return render(request, 'index.html')

