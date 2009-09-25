## tags.py
from django.template import resolve_variable
from django import template
from django.template import Library, Node
 
register = template.Library()
 
class SomeNode(Node):
    def __init__(self, request):
        self.request = request
 
    def render(self, context):
        if var: return var
        else: return ''
 
@register.tag(name="get_request_tag")
def get_section(parser, token):
    try:
        tag_name, request = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents[0]
    section = request.META['REQUEST_URI'][1:].split('/')[0]
    return SomeNode(section)

