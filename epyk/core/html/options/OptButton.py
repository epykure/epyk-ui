"""

"""


class OptionsButton(object):
  def __init__(self, src, options):
    self.src = src
    self._multiple, self.src.attr['name'] = options.get('multiple', False), options.get('group', None)

  @property
  def multiple(self):
    """
    Property to define if multiple buttons can be selected at the same time
    Default value is false
    """
    return self._multiple

  @multiple.setter
  def multiple(self, bool):
    self._multiple = bool

  @property
  def group(self):
    """
    Property to set the group name of a button
    """
    return self.src.attr['name']

  @group.setter
  def group(self, val):
    self.src.attr['name'] = val


class OptionsBadge(object):
  def __init__(self, src, options):
    self.src = src
    self._badge_prop = options.get('badge_position', "left")
    if self._badge_prop == 'left':
      self._badge_css = {"border-radius": "20px", "position": 'relative',
                         #"bottom": "-5px", "right": "-6px"
                         }
    else:
      self._badge_css = {"border-radius": "20px", "position": 'relative', "top": "-4px", "right": "11px",
                         }
    self._badge_css.update(options.get('badge_css', {}))

  @property
  def badge_css(self):
    """
    """
    return self._badge_css

  @badge_css.setter
  def badge_css(self, css):
    self.src.link.css(css)
    self._badge_css = css

  @property
  def badge_position(self):
    """

    :return:
    """
    return self._badge_prop

  @badge_position.setter
  def badge_position(self, position):
    """

    :param position:
    :return:
    """
    self._badge_prop = position
