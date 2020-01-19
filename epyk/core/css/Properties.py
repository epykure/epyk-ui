"""

"""


class CssMixin(object):
  """

  """

  @property
  def display(self):
    """

    :return:
    """
    return self.htmlObj.css("display")

  @display.setter
  def display(self, val):
    if val is None:
      self.htmlObj.css({"display": 'None'})
    else:
      self.htmlObj.css({"display": val})

  @property
  def font_size(self):
    """

    :return:
    """
    return self.htmlObj.css("font-size")

  @font_size.setter
  def font_size(self, val):
    if val is None:
      self.htmlObj.css({"font-size": 'None'})
    else:
      self.htmlObj.css({"font-size": val})
