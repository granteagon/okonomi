import re

from django.core.cache import cache
from django.conf import settings

OKONOMI_JS_PLACEHOLDER = re.compile("\$\{JSREQUIRE\}")
OKONOMI_STATIC_URL = settings.OKONOMI_STATIC_URL

class Okonomi(object):
    """
    the okonomi middleware prepares unique combinations of javascript includes
    for rendered django templates. it stores the combined javascript in memcache
    for fast serving by a view used as a single point of javascript inclusion.
    """

    def process_request(self, request):
        request.okonomi_paths = set()
        request.okonomi_urls = set()

    def process_response(self, request, response):
        if not (hasattr(request, 'okonomi_paths') or hasattr(request, 'okonomi_urls')):
            return response
        if len(request.okonomi_urls) == 0 and len(request.okonomi_paths) == 0:
            return response

        html = '<script type="text/javascript" src="%s"></script>\n';

        remote_html = ''
        local_html = ''
        for url in request.okonomi_urls:
            remote_html += (html % url)

        if getattr(settings, 'OKONOMI_JS_BULKING', False):
            if len(request.okonomi_paths) > 0:
                cache_key = okonomi.utils.make_cache_key(request.okonomi_paths)
                combined_path = okonomi.utils.make_combined_path(request.okonomi_paths)
                local_html = html % ('okonomi/%s' % combined_paths)
                js = cache.get(cache_key)
                if js is None:
                    combined = okonomi.utils.generate_js(request.okonomi_paths)
                    cache.set(cache_key, combined)
        else:
            for path in request.okonomi_paths:
                # TODO lack of / works for medley, but...
                url = settings.OKONOMI_STATIC_URL + path
                local_html += (html % url)

        response.content = OKONOMI_JS_PLACEHOLDER.sub(local_html+remote_html, response.content)

        return response

def context_processor(request):
    """ sticks paths and urls arrays into the template context """
    context = {}
    attrs = ['okonomi_paths', 'okonomi_urls']
    for attr in attrs:
        if hasattr(request, attr):
            context[attr] = getattr(request, attr)

    return context
