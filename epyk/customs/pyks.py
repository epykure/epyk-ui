import epyk.customs.data.UI


class Bespoke:

  def __init__(self, page):
    self.page = page

  @property
  def data(self):
    return epyk.customs.data.UI.Components(self.page)
