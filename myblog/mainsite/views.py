from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime

# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals()) # locals() => 存成物件
    return HttpResponse(html)


# def homepage(request):
    # posts = Post.objects.all()
    # post_lists = list() #! [] 寫成這樣?
    
    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count)) +str(post)+"<br>")
    #     return HttpResponse(post_lists)
