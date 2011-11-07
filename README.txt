okonomi
-------

incredibly simply static javascript file handling.

from any template, as many times as you want:
    {% jsrequire /path/to/my/js.js %}

or
    {% jsrequire http://google.com/some/api %}

okonomi will take care of getting just the right <script> includes into the HEAD of your template using the hideous ${JS} sigil that you must include in a base template somewhere.

There is a written but totally un-tested bulking feature that combines all the locally-hosted javascript files into a single string stored in memcache and serves them via a django view and a single <script> tag.

author
------
Nathaniel Smith <nate.smith@coxinc.com>
for Cox Media Group Digital & Strategy

license
-------
okonomi is licensed under the MIT license.
