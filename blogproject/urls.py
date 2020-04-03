from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('', views.main)
]
