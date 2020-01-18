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
      self._badge_css = {"border-radius": "20px", "position": 'relative', "bottom": "-5px", "background": 'white',
                         "right": "-6px"}
    else:
      self._badge_css = {"border-radius": "20px", "position": 'relative', "top": "-4px", "right": "11px",
                         "background": 'white'}
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


class OptionsLi(object):
  def __init__(self, src, options):
    self.src = src
    self._li_css = options.get("li_css", {})
    self.li_class = options.get("li_class", [])

  @property
  def li_css(self):
    """
    """
    return self._li_css

  @li_css.setter
  def li_css(self, css):
    self._li_css = css

  @property
  def li_class(self):
    """
    """
    return self._li_class

  @li_class.setter
  def li_class(self, cls_names):
    self._li_class = cls_names


class OptionsText(object):
  def __init__(self, src, options):
    self.src = src
    self.__reset = options.get("reset", True)
    self.__limit_char = options.get("limit_char", False)
    self.__markdown = options.get("markdown", True)

  @property
  def reset(self):
    """

    :return:
    """
    return self.__reset

  @reset.setter
  def reset(self, bool):
    """

    :return:
    """
    self.src._jsStyles["reset"] = bool
    self.__reset = bool

  @property
  def markdown(self):
    """

    :return:
    """
    return self.__markdown

  @markdown.setter
  def markdown(self, bool):
    """

    :return:
    """
    self.src._jsStyles["markdown"] = bool
    self.__markdown = bool

  @property
  def limit_char(self):
    """

    :return:
    """
    return self.__limit_char

  @limit_char.setter
  def limit_char(self, value):
    """

    :param value:
    :return:
    """
    self.src._jsStyles["maxlength"] = value
    self.__limit_char = value


class OptionsSelect(object):
  def __init__(self, src):
    self.src = src
