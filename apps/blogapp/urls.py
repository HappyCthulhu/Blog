from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('post/', views.post, name="post"),
    path('', views.index, name="index")
]
