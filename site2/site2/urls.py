from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home.urls' , namespace='home')),
    path('' , include('post.urls' , namespace='post')),
    path('account/' , include('account.urls' , namespace='account')),
]
