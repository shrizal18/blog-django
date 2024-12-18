from django.shortcuts import render, HttpResponse ,get_object_or_404
from .models import Blog
 
def homepage(request) :
    posts = Blog.objects.filter(published=True).order_by('-created_at')[:5]
    return render (request , "homepage.html" , {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'post.html', {'post': post})
