from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from post.models import Post
from post.models import *
from post.forms import PostSearchForm

class HomeView(View):
    form_class = PostSearchForm

    def get(self , request):
        posts = Post.objects.all()
        if request.GET.get('search'):
            posts = posts.filter(body__contains = request.GET['search'])
            if not posts:
                return render(request , 'home/not_found.html' , {'form':self.form_class})
        return render(request , 'home/index.html' , {'posts' : posts , 'form':self.form_class})

