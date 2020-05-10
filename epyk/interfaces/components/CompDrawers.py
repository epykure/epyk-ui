
from epyk.core import html


class Drawers(object):

  def __init__(self, context):
    self.context = context

  def drawer(self, width=(100, '%'), height=(100, '%'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the right.

    Attributes:
    ----------
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper:
    """
    h_drawer = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, options, helper, profile)
    h_drawer.style.css.min_height = 200
    self.context.register(h_drawer)
    return h_drawer

  def left(self, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the left.

    Attributes:
    ----------
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile: Optional. A flag to set the component performance storage
    :param helper:
    """
    options = options or {}
    options["side"] = 'right'
    h_drawer = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, options, helper, profile)
    self.context.register(h_drawer)
    return h_drawer

  def right(self, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer with handle on the left.

    Attributes:
    ----------
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper:
    """
    options = options or {}
    options["side"] = 'right'
    h_drawer = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, options, helper, profile)
    self.context.register(h_drawer)
    return h_drawer

  def no_handle(self, component, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    """
    Description:
    ------------
    Bespoke drawer without handle.
    The event to display the panel will be attached to the component.

    Attributes:
    ----------
    :param component: Html component. Object in charge of managing the panel display
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper:
    """
    options = options or {}
    options["side"] = 'right'
    h_drawer = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, options, helper, profile)
    h_drawer.set_handle(component)
    self.context.register(h_drawer)
    return h_drawer

