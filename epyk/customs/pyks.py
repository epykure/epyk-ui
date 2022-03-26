import epyk.customs.data.UI


class Bespoke:

  def __init__(self, page):
    self.page = page

  @property
  def data(self) -> epyk.customs.data.UI.Components:
    """
    Description:
    ------------

    :return:
    """
    return epyk.customs.data.UI.Components(self.page)

  @property
  def progress(self) -> epyk.customs.data.UI.ProgressComponents:
    """
    Description:
    ------------

    """
    return epyk.customs.data.UI.ProgressComponents(self.page)
