# encoding=utf8
from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag()
def leaf_cat_list():
    return Category.objects.filter(Parent__isnull=True)
