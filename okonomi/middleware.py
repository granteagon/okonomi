import re

OKONOMI_JS_PLACEHOLDER = re.compile("\$\{JS\}")

class Okonomi(object):
    """
    the okonomi middleware prepares unique combinations of javascript includes
    for rendered django templates. it stores the combined javascript in memcache
    for fast serving by a view used as a single point of javascript inclusion.
    """

    def process_request(self, request):
        request.okonomi_paths = []
        request.okonomi_urls = []

    def process_response(self, request, response):
        if not (hasattr(request, 'okonomi_paths') or hasattr(request, 'okonomi_urls')):
            return response
        html = '<script type="text/javascript" src="%s"></script>\n';

        remote_html = ''
        local_html = ''
        for url in request.okonomi_urls:
            remote_html += (html % url)

        if len(request.okonomi_paths) > 0:
            cache_key = okonomi.utils.make_cache_key(request.okonomi_paths)
            combined_path = okonomi.utils.make_combined_path(request.okonomi_paths)
            local_html = html % ('okonomi/%s' % combined_paths)
            js = cache.get(cache_key)
            if js is None:
                combined = okonomi.utils.generate_js(request.okonomi_paths)
                cache.set(cache_key, combined)

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
