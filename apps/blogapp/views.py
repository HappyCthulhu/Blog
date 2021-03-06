from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm, ContactForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
import re
from .service import send
from .tasks import send_spam_email

def index(request):
    articles = Article.objects.all()[:5]
    if request.method == "GET":
        form = ArticleForm()
        context = {
            'form': form,
            'articles': articles
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        bound_form = ArticleForm(request.POST, request.FILES)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('index')
        return render(request, 'index.html', context={'form': bound_form, 'articles': articles})

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
            #send(name, message, phone, email)
            send_spam_email.delay(name, message, phone, email)
            return redirect('index')
        return render(request, 'contact.html', context={'form': form})


def post(request, slug=None, **kwargs):
    if request.method == 'GET':
        article = get_object_or_404(Article, slug=slug)
        context = {
            'article':article,
        }
        return render(request, 'post.html', context)

def lenta(request):
    article = Article.objects.all()
    return render(request, 'lenta.html', context={'lenta':article})

class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'body', 'image']
    template_name = 'article_create.html'

    def form_valid(self, form):
        stringer = form.instance.body
        stringer.replace("""    """, '<br>')
        stringer = re.sub(r'   ', '<br>', stringer)
        form.save(stringer)
        return super().form_valid(form)
