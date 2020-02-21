
class OptionsTree(object):

  def __init__(self, src, options):
    self._icon_open, self._icon_close, self._expanded = "fas fa-folder-open", "fas fa-folder", True
    self.src = src

  @property
  def icon_open(self):
    """

    :return:
    """
    return self._icon_open

  @property
  def icon_close(self):
    """

    :return:
    """
    return self._icon_close

  @property
  def expanded(self):
    """

    :return:
    """
    return self._expanded

  @expanded.setter
  def expanded(self, bool):
    self._expanded = bool
    self.src.items = None
    self.src.set(self.src, self.src.val)

  @icon_open.setter
  def icon_open(self, icon):
    self._icon_open = icon
    self.src.items = []
    self.src.set(self.src, self.src.val)

  @icon_close.setter
  def icon_close(self, icon):
    self._icon_close = icon
    self.src.items = []
    self.src.set(self.src, self.src.val)
