from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blog_counter = Blog.objects.count
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, "blog/all_blogs.html", {'blog': blogs, 'blog_counter': blog_counter})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
