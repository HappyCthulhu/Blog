from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={'lol': 'lol'})

def about(request):
    return render(request, 'about.html', context={'lol': 'lol'})

def contact(request):
    return render(request, 'contact.html', context={'lol': 'lol'})

def post(request):
    return render(request, 'post.html', context={'lol': 'lol'})
