from django.contrib import admin
from django.urls  import path , include
from .import views

from django.conf.urls.static import static

app_name = 'articles'

urlpatterns = [
    path('', views.articlesHome, name ='articlesHome'),
    path('<str:slug>', views.articlesPost, name ='articlesPost'),
    
] 