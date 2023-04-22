from django.shortcuts import render, get_object_or_404 
from blog.models import Post, Comment 
from blog.forms import CommentForm
from django.db.models.functions import Now

from django.db.models import Count, F, Value

#from django.core.pageintiator import Paginator, 

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = 1).filter(publish_date__lte = Now()).order_by('-publish_date')
    #if kwargs.get('tag_name')  != None:
    #   posts = posts.filter(
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context )
 

def blog_single(request, pid ):
    posts = Post.objects.filter(status = 1) 
    post = get_object_or_404(posts, pk = pid) 

    post.counted_view = post.counted_view + 1 
    post.save()
    
    comments = Comment.objects.filter(post = post.id, approved = True).order_by('-created_date') 
    form = CommentForm()
    context = {'post': post, 'comments': comments, 'form': form } 
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
 
