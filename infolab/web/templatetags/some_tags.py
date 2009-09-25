from django.template import resolve_variable
from django import template
from django.template import Library, Node
 
register = template.Library()
 
class SomeNode(Node):
    def __init__(self, request):
        self.request = request
 
    def render(self, context):
        request = resolve_variable(self.request, context)
 
        # Do something with the session
        var = request.session.get('mycookie', None)
        if var:
            del request.session['mycookie']
            return var
        else:
            return ''
 
@register.tag(name="get_request_tag")
def get_request_tag(parser, token):
    try:
        tag_name, request = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents[0]
 
    return SomeNode(request)

