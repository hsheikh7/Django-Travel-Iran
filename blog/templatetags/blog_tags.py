from django import template
from blog.models import Post

register = template.Library() 

@register.simple_tag(name= 'totlaposts') 
def function():
    posts = Post.objects.filter(status=1)
    return posts 


@register.inclusion_tag('latest-posts.html')
def latestposts(arg=3):
    posts= Post.objects.filter(status= 1).order_by('-publish_date')[:arg]
    return {'posts': posts}
