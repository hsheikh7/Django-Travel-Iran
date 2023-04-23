from django.shortcuts import render, get_object_or_404 
from blog.models import Post, Comment 
from blog.forms import CommentForm
from django.db.models.functions import Now
from django.db.models import OuterRef, Subquery

#from django.core.pageintiator import Paginator, 

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = 1).filter(publish_date__lte = Now()).order_by('-publish_date')
    #if kwargs.get('tag_name')  != None:
    #posts = posts.filter(
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context )
 
def blog_single(request, pid ):
    #posts = Post.objects.filter(status = 1) 
    posts = Post.objects.filter(status = 1).filter(publish_date__lte = Now()).order_by('publish_date')
    post = get_object_or_404(posts, pk = pid) 

    #Counting the Number of Views 
    post.counted_view = post.counted_view + 1 
    post.save()
    
    #Previous and Next Posts :) 
    previous_post = posts.filter(pk__lt= post.pk).order_by('-publish_date').first()
    next_post = posts.filter(pk__gt= post.pk).order_by('publish_date').first()
    previous_post = posts.filter(pk__lt= post.pk).order_by('-publish_date').first()
    next_post = posts.filter(pk__gt= post.pk).order_by('publish_date').first()

    comments = Comment.objects.filter(post = post.id, approved = True).order_by('-created_date') 
    form = CommentForm()
    context = {'post': post, 'comments': comments, 'form': form, 'previouspost': previous_post, 'nextpost': next_post} 
    return render(request, 'blog/blog-single.html', context)

#def test(request, pid ):
#    post = get_object_or_404(Post, pk = pid ) 
#    context = {'post': post} 
#    return render(request, 'test.html', context)

def test(request):
    posts = Post.objects.filter(status = 1).filter(publish_date__lte = Now()).order_by('publish_date')
    post = posts.get(pk = 7)
    
    previous_post = posts.filter(pk__lt= post.pk).order_by('-publish_date').first()
    next_post = posts.filter(pk__gt= post.pk).order_by('publish_date').first()

    context = {'posts': posts, 'post': post, 'previouspost': previous_post, 'nextpost': next_post} 
    return render(request, 'test.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.all()
    #posts = posts.filter(category__name = cat_name)
    context = {'post': posts} 
    return render(request, 'blog/blog-home.html', context)
 
