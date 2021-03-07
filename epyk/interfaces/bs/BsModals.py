
from epyk.fwk.bs.html import BsHtml


class Modals:

  def __init__(self, ui):
    self.page = ui.page

  def modal(self, component=None, title=None, width=(100, "%"), height=(None, "px"), sizing=None, options=None,
            profile=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/

    Attributes:
    ----------
    :param component:
    :param title:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = BsHtml.BsModals(self.page, component or [], title, width, height, options or {}, profile)
    if sizing is not None:
      container.dialog.attr["class"].add("modal-%s" % sizing)
    return container

  def popup(self, component=None, title=None, width=(100, "%"), height=(None, "px"), sizing=None, options=None,
            profile=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/

    Attributes:
    ----------
    :param component:
    :param title:
    :param width:
    :param height:
    :param sizing:
    :param options:
    :param profile:
    """
    container = BsHtml.BsModals(self.page, component or [], title, width, height, options or {}, profile)
    if sizing is not None:
      container.dialog.attr["class"].add("modal-%s" % sizing)
    return container

  def static(self, component=None, title=None, width=(100, "%"), height=(None, "px"), sizing=None, options=None,
             profile=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/

    Attributes:
    ----------
    :param component:
    :param title:
    :param width:
    :param height:
    :param sizing:
    :param options:
    :param profile:
    """
    container = BsHtml.BsModals(self.page, component or [], title, width, height, options or {}, profile)
    if sizing is not None:
      container.dialog.attr["class"].add("modal-%s" % sizing)
    container.attr['data-backdrop'] = "static"
    return container

  def confirmation(self, component=None, title=None, event='Valid', category='primary', width=(100, "%"),
                   height=(None, "px"), sizing=None, options=None, profile=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/

    Attributes:
    ----------
    :param component:
    :param title:
    :param event:
    :param category:
    :param width:
    :param height:
    :param sizing:
    :param options:
    :param profile:
    """
    container = BsHtml.BsModals(self.page, component or [], title, width, height, options or {}, profile)
    if sizing is not None:
      container.dialog.attr["class"].add("modal-%s" % sizing)
    self.button = self.page.web.bs.button(event, category=category)
    self.button.options.managed = False
    self.button.attr["data-dismiss"] = "modal"
    footer = container.footer
    footer += self.button
    return container

  def actions(self, component=None, title=None, events=None, category='primary', width=(100, "%"),
              height=(None, "px"), sizing=None, options=None, profile=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/

    Attributes:
    ----------
    :param component:
    :param title:
    :param events:
    :param category:
    :param width:
    :param height:
    :param sizing:
    :param options:
    :param profile:
    """
    container = BsHtml.BsModals(self.page, component or [], title, width, height, options or {}, profile)
    if sizing is not None:
      container.dialog.attr["class"].add("modal-%s" % sizing)
    self.buttons = []

    header = container.header
    closure = self.page.web.bs.buttons.close(dismiss='modal')
    closure.options.managed = False
    header += closure
    footer = container.footer
    for b in events:
      button = self.page.web.bs.button(b, category=category)
      button.options.managed = False
      footer += button
    return container
