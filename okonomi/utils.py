import os

from django.conf import settings

# ([str]|str) -> str
def make_cache_key(paths):
    """given a list of javascript media paths,
    generate a cache key
    """

    if type(paths) == type(''):
        return 'okonomi:%s' % paths

    if type(paths) in (type([]), type(set())):
        return 'okonomi:%s' % make_combined_path(paths)

# [str] -> str
def make_combined_path(paths):
    """given a list of javascript media paths,
    generate a string suitable for use in a url that
    combines the paths
    """
    # TODO hash this using a key in settings
    return paths.join('|')

# ([str]|str) -> str
def generate_js(paths):
    """given a list of javascript media paths, read
    them from disk and return their concatenation
    """
    if type(paths) == type(''):
        # TODO decrypt
        paths = paths.split('|')

    combined = ''
    for path in paths:
        # TODO use actual setting
        full_path = os.path.join(settings.STATIC_PATH, path)
        with open(full_path, 'r') as f:
            combined += f.read()+'\n/* --- okonomi --- */\n' # TODO slurp file

    return combined
