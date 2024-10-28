
import re

from pelican import signals


def read_more(value, url):
    """ handles 'Read more' functionality """
    pattern = '<!--MORE-->.*'
    replacement = (f'<p class="readmore"><a href="{url}">'
                   f'Read more&hellip;</a></p>')

    _re = re.compile(pattern, flags=re.DOTALL)
    return _re.sub(replacement, value)


def add_read_more(pelican):
    """Add (register) read_more filter to Pelican."""
    pelican.env.filters.update({"read_more": read_more})


def register():
    """Plugin registration."""
    signals.generator_init.connect(add_read_more)
