
from epyk.core.html.options import Options


class OptionDays(Options):

  @property
  def style(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css_attrs:
    """
    return self.get({})

  @style.setter
  def style(self, css_attrs):
    self.set(css_attrs)

  @property
  def overload(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css_attrs:
    """
    return self.get({})

  @overload.setter
  def overload(self, css_attrs):
    self.set(css_attrs)

  @property
  def number(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css_attrs:
    """
    return self.get({})

  @number.setter
  def number(self, css_attrs):
    self.set(css_attrs)

  @property
  def today(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css_attrs:
    """
    return self.get({})

  @today.setter
  def today(self, css_attrs):
    self.set(css_attrs)

  @property
  def header(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css_attrs:
    """
    return self.get({})

  @header.setter
  def header(self, css_attrs):
    self.set(css_attrs)
