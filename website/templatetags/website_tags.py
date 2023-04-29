from django import template
from blog.models import Post 
from django.db.models.functions import Now

register = template.Library() 

@register.inclusion_tag('website/latestposts-landing.html')
def latestpostslanding(arg=6):
    posts = Post.objects.filter(status = 1).filter(publish_date__lte = Now()).order_by('-publish_date')[:arg]
    return {'posts': posts} 
