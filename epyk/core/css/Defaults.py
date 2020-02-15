"""
Default style in the module.

This can be overridden during a report run time
"""


class Font(object):
  size, header_size, unit = 12, 14, "px"
  family = "Calibri"


class Icon(object):
  small, normal, big, unit = 10, 15, 20, 'px'


def font(step=0):
  """

  :param step:
  :return:
  """
  return "%s%s" % (Font.size+step, Font.unit)


def header(step=0):
  """

  :param step:
  :return:
  """
  return "%s%s" % (Font.header_size+step, Font.unit)


# Default CSS Styles
BODY_CONTAINER = None # The body CSS dictionary
BACKGROUND = ('greys', 0)
MEDIA = 600


# Default CSS
CSS_EXCEPTIONS = True
CSS_EXCEPTIONS_FORMAT = "CSS - %s - invalid %s"
