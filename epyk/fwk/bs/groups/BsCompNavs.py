
class Components:

  def __init__(self, ui):
    self.page = ui.page

  def title(self, value="", level=5, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param value:
    :param level:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.page.ui.tags.hn(level, value, width=width, height=height, options=options, profile=profile)
    component.add_style(["modal-title"], clear_first=True)
    return component

  def link(self, text, url, icon=None, align="left", helper=None, height=(None, 'px'), decoration=False,
           html_code=None, options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param text:
    :param url:
    :param icon:
    :param align:
    :param helper:
    :param height:
    :param decoration:
    :param html_code:
    :param options:
    :param profile:
    """
    component = self.page.ui.link(text, url, icon, align, helper, height, decoration, html_code, options, profile)
    component.add_style(["nav-link"], clear_first=True)
    return component

  def brand(self, text, url, icon=None, align="left", helper=None, height=(None, 'px'), decoration=False,
            html_code=None, options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param text:
    :param url:
    :param icon:
    :param align:
    :param helper:
    :param height:
    :param decoration:
    :param html_code:
    :param options:
    :param profile:
    """
    component = self.page.ui.link(text, url, icon, align, helper, height, decoration, html_code, options, profile)
    component.add_style(["navbar-brand"], clear_first=True)
    return component

  def toggler(self):
    """

    :return:
    """
