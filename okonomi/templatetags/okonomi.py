from django import template

register = template.Library()

@register.tag(name="jsrequire")
def jsrequire(parse, token):
    """
        Syntax::
            {% jsrequire path_relative_to_STATIC_URL|url %}

        Examples::
            {% jsrequire /formcheckin.js %}
            {% jsrequire /jqueryui/accordian.js %}
            {% jsinclde https://maps.google.com/api/?key=123 %}

    """
    tokens = token.split_contents()
    if len(tokens) < 2:
        raise template.TemplateSyntaxError('Need a path relative to STATIC_URL or a fully qualified url.')

    path_or_url = tokens.pop()
    path = None
    url = None
    if path_or_url.startswith('/'):
        path = path_or_url
    elif path_or_url.startswith('http'):
        url = path_or_url
    else:
        raise template.TemplateSyntaxError('Expected either a relative path (starting with /) or a fully qualified url (starting with http). Got %s' % path_or_url)

    return JSIncludeNode(path, url)

class JSRequireNode(template.Node):
    def __init__(self, path=None, url=None):
        if not (path and url):
            raise template.TemplateSyntaxError('Expected either a relative path or a fully qualified url. Got nothing')
        if path and url:
            raise template.TemplateSyntaxError('Expected either a relative path or a fully qualified url. Got both')

        if path:
            self.path = path
            self.url = None
        if url:
            self.path = None
            self.url = url

    def render(self, context):
        if self.path:
            context['okonomi_paths'].add(self.path)
        if self.url:
            context['okonomi_urls'].add(self.url)

        return '<!-- requires %s -->' % (self.path or self.url)
