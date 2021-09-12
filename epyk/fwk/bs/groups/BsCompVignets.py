
class Components:
  def __init__(self, ui):
    self.page = ui.page

  def card(self, records=None, width=(70, "px"), height=("auto", ''), color=None, background_color=None,
           helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Bootstrap’s cards provide a flexible and extensible content container with multiple variants and options.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/card/

    Attributes:
    ----------
    :param records:
    :param width:
    :param height:
    :param color:
    :param background_color:
    :param helper:
    :param options:
    :param profile:
    """
