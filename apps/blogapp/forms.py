from django import forms
from .models import Article,  Contact

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Введите заголовок поста"}),
            'body': forms.Textarea(attrs={'class':'form-control mt-3', 'type':'text', 'rows': 7, 'cols':30, 'style':'resize:none;', 'placeholder':"Введите тело поста",}),
            'images': forms.FileInput(attrs={'type':'file', 'class':'form-control-file mt-3 mb-3', 'id':'exampleFormControlFile1'}),
            }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control", 'placeholder':"Name", 'id':"name", 'data-validation-required-message':"Please enter your name."}),
            'email': forms.EmailInput(attrs={'class':"form-control", 'placeholder':"Email Address", 'id':"email", 'data-validation-required-message':"Please enter your email address."}),
            'phone': forms.TextInput(attrs={'type':"tel", 'class':"form-control", 'placeholder':"Phone Number", 'id':"phone", 'data-validation-required-message':"Please enter your phone number."}),
            'message': forms.Textarea(attrs={'rows':"5", 'class':"form-control", 'placeholder':"Message", 'id':"message", 'data-validation-required-message':"Please enter a message."})
        }
