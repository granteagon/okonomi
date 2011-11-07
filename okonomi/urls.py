from django.conf.urls.defaults import patterns, url

from okonomi.views import OkonomiJavascript

urlpatterns = patterns('',
    # TODO take arg here
    url(r'^$', OkonomiJavascript.as_view()),
)
