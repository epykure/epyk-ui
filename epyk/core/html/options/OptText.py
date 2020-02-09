"""

"""


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

