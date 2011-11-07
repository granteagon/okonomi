# ([str]|str) -> str
def make_cache_key(paths):
    """given a list of javascript media paths,
    generate a cache key
    """

    if type(paths) == type(''):
        return 'okonomi:%s' % paths

    if type(paths) == type([]):
        return 'okonomi:%s' % make_combined_path(paths)

# [str] -> str
def make_combined_path(paths):
    """given a list of javascript media paths,
    generate a string suitable for use in a url that
    combines the paths
    """
    # TODO hash this
    return paths.join('|')

# [str] -> str
def generate_js(paths):
    """given a list of javascript media paths, read
    them from disk and return their concatenation
    """
    # TODO write this
    return ''
