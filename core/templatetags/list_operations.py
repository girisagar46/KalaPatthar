import ast

from django import template

register = template.Library()


@register.simple_tag
def list_joiner(val):
    lit_eval = ast.literal_eval(val)
    return " ".join(lit_eval)


@register.simple_tag
def literal_eval(val):
    lit_eval = ast.literal_eval(val)
    return lit_eval