from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html', takes_context=True)
def get_category_list(context, current_category=None):
    return {
        'categories': Category.objects.all(),
        'current_category': current_category
    }
