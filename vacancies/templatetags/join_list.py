from django import template

register = template.Library()


@register.filter
def join_list(skills):
    return " • ".join(skills.split(','))
