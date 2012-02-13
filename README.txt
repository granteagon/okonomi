okonomi
-------

unfancy javascript dependency handling for django.

from any template, as many times as you want:

    {% load okonomi %}

    {% jsrequire /path/to/my/js.js %}

or

    {% jsrequire http://google.com/some/api %}

okonomi will take care of getting just the right <script> includes into the HEAD of your template using the hideous ${JSREQUIRE} sigil that you must include in a base template somewhere.

There is a written but totally un-tested bulking feature that combines all the locally-hosted javascript files into a single string stored in memcache and serves them via a django view and a single <script> tag.

django settings
---------------
* OKONOMI_STATIC_URL set this to whatever makes sense for your django project.
* OKONOMI_STATIC_PATH set this to whatever makes sense for your django project.
* OKONOMI_HTML_PATH_TEMPLATE defaults to '<script type="text/javascript" src="%s"></script>\n'
* OKONOMI_HTML_URL_TEMPLATE defaults to '<script type="text/javascript" src="%s"></script>\n'

meta
----
okonomi was written by <nathanielksmith@gmail.com> for Cox Media Group Digital & Strategy and is licensed under the terms of the MIT license.