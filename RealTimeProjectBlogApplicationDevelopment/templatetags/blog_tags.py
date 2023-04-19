from taggit.models import Tag
from django.db.models import Count
from django import template
from ..models import *

register=template.Library() 

# Define Custom Tags

# Way 1
@register.simple_tag
def total_posts():
    return Post.objects.count()

# Way 2
@register.inclusion_tag('blog/latest_posts123.html')
def show_latest_posts(count=5):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts} 

# Way 3
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]