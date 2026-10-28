from django.urls import path
from . import views

urlpatterns = [
    # path('file/', views.file, name='file'),
    path("set", views.Set),
    path("get", views.Get),
    path("delete", views.delete),
]