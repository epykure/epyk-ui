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
    """

    :param val:
    :return:
    """
    if val is None:
      self.htmlObj.css({"display": 'None'})
    else:
      self.htmlObj.css({"display": val})
