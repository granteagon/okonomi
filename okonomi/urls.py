from django.conf.urls.defaults import patterns, url

from okonomi.views import OkonomiJavascript

urlpatterns = patterns('',
    url(r'^(?P<combined_path>.+)$', OkonomiJavascript.as_view()),
)
