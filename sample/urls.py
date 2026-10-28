from django.urls import path, include

urlpatterns = [
    path('', include('sample.app.urls')),
    path('test1/', include('test1.urls')),
]
