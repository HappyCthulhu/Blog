from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('article/<str:slug>/', views.post, name="post"),
    path('lenta/', views.lenta, name="lenta"),
    path('article_create/', views.ArticleCreate.as_view(), name="create"),
    path('', views.index, name="index")
]
