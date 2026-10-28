from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home_page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('404/', views.page_not_found, name='404'),
    path('first/', views.first, name='first'),
    path('second/',views.second, name='second'),
    path('conditional_statement/', views.conditions, name='conditional_statement'),
    path('image/', views.image, name='image'),
    path('question/', views.question, name='question'),
    path('question2/', views.question2, name='question2'),
    path('file/', views.file, name='file'),
]