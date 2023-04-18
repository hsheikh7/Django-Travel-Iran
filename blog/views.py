from django.shortcuts import render, get_object_or_404 
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = 1).order_by('-publish_date')
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context )
 
def blog_single(request, pid ):
    posts = Post.objects.filter(status = 1) 
    post = get_object_or_404(posts, pk = pid) 
    context = {'post': post} 
    return render(request, 'blog/blog-single.html', context)

def test(request, pid ):
    post = get_object_or_404(Post, pk = pid ) 
    context = {'post': post} 
    return render(request, 'test.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.all()
    #posts = posts.filter(category__name = cat_name)
    context = {'post': posts} 
    return render(request, 'blog/blog-home.html', context)
 