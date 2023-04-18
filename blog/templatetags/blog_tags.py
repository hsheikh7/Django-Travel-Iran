from django import template
from blog.models import Post
from blog.models import Category
from blog.models import TaggableManager

register = template.Library() 

@register.simple_tag(name= 'totlaposts') 
def function():
    posts = Post.objects.filter(status=1)
    return posts 


@register.inclusion_tag('blog/latest-posts.html')
def latestposts(arg=3):
    posts= Post.objects.filter(status= 1).order_by('-publish_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status = 1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category= name).count()
    return {'categories': cat_dict}

