from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, ContactForm
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html', context={'lol': 'lol'})

def about(request):
    return render(request, 'about.html', context={'lol': 'lol'})

def contact(request):
    form = ContactForm()
    if request.method == "GET":
        context = {
            'form': form,
        }
        return render(request, 'contact.html', context)
    elif request.method == "POST":
        bound_form = ContactForm(request.POST)
        if bound_form.is_valid():
            name = bound_form.cleaned_data['name']
            email = bound_form.cleaned_data['email']
            message = bound_form.cleaned_data['message']
            phone = bound_form.cleaned_data['phone']
            print(name)
            send_mail(
                f'От {name}',
                f'Письмо: {message} . Телефон: {phone}',
                'твоя почта',
                [f'{email}'],
            )
            return redirect('index')
        return render(request, 'contact.html', context={'form': form})

def post(request):
    articles = Article.objects.all()
    if request.method == "GET":
        form = ArticleForm()
        context = {
            'form': form,
            'articles': articles
        }
        return render(request, 'post.html', context)
    elif request.method == 'POST':
        bound_form = ArticleForm(request.POST, request.FILES)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('post')
        return render(request, 'post.html', context={'form': bound_form, 'articles': articles})
