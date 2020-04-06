from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('article/<str:slug>/', views.post, name="post"),
    path('lenta/', views.lenta, name="lenta"),
    path('', views.index, name="index")
]
