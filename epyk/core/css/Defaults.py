"""
Default style in the module.

This can be overridden during a report run time
"""


class Font(object):
  size, header_size, unit = 12, 14, "px"
  family = "Calibri"


class Icon(object):
  small, normal, big, unit = 10, 15, 20, 'px'


# Default CSS Styles
BODY_CONTAINER = None # The body CSS dictionary
BACKGROUND = ('greys', 0)
MEDIA = 600
