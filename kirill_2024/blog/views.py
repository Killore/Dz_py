from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog_index.html', {'posts': posts})

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'post': post})
