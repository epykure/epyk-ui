import epyk.customs.data.UI


class Bespoke:

  def __init__(self, page):
    self.page = page

  @property
  def data(self) -> epyk.customs.data.UI.Components:
    """

    :return:
    """
    return epyk.customs.data.UI.Components(self.page)

  @property
  def progress(self) -> epyk.customs.data.UI.ProgressComponents:
    """
    Add a circular progress bar.

    Usage::

      cl = page.ui.pyk.progress.circle(80)
      page.ui.button("Click").click([cl.build(20)])
    """
    return epyk.customs.data.UI.ProgressComponents(self.page)
