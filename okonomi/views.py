from django.core.cache import cache
from django.http import Http404, HttpResponse
from django.views.generic.base import View

# TODO good cache headers

class OkonomiJavascript(object):
    """
    OkonomiJavascript serves combined javascript files from cache.
    """

    def get(self, request):
        combined_path = '' # TODO in urls.py
        cache_key = okonomi.utils.make_cache_key(combined_path)
        js = cache.get(cache_key)
        if js is None:
            # TODO need to get a list of paths here from combined_path...
            js = okonomi.utils.generate_js(combined_path)

        cache.set(cache_key, js)
        
        # here, filters can be applied (like minifying gzipping etc)

        return HttpResponse(js, mimetype="text/javascript")

