"""

"""

from epyk.core import html
from epyk.core.html import Defaults


class Navigation(object):
  def __init__(self, context):
    self.context = context

  def up(self, icon="fas fa-arrow-up", tooltip=None, size=(None, "px"), width=(100, '%'), options=None, profile=False):
    """

    :param icon:
    :param tooltip:
    :param size:
    :param width:
    :param options:
    :param profile:
    :return:
    """
    du = self.context.rptObj.ui.icon(icon).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                                                "border-radius": '20px', "padding": '8px', "right": '20px',
                                                "bottom": "20px"})
    du.style.addCls("CssDivOnHoverBackgroundLight")
    self.context.rptObj.js.addOnReady(
      self.context.rptObj.js.window.events.addScrollListener([
        self.context.rptObj.js.if_(self.context.rptObj.js.window.scrollY > 50, [du.dom.show()]).else_(du.dom.hide())
      ]))
    if tooltip is not None:
      du.tooltip(tooltip)
    du.click([
      self.context.rptObj.js.window.scrollUp(),
      self.context.rptObj.js.objects.this.hide()])
    return du

  def down(self, icon="fas fa-arrow-down", tooltip=None, size=(None, "px"), width=(100, '%'), options=None, profile=False):
    """

    :param icon:
    :param tooltip:
    :param size:
    :param width:
    :param options:
    :param profile:
    :return:
    """
    dd = self.context.rptObj.ui.icon(icon).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                                                  "border-radius": '20px', "padding": '8px', "right": '20px'})
    dd.style.addCls("CssDivOnHoverBackgroundLight")
    self.context.rptObj.js.addOnReady(
      self.context.rptObj.js.window.events.addScrollListener([
        self.context.rptObj.js.if_(self.context.rptObj.js.window.scrollY > 50, [dd.dom.show()]).else_(dd.dom.hide())
      ]))
    if tooltip is not None:
      dd.tooltip(tooltip)
    dd.click([
      self.context.rptObj.js.window.scrollTo(),
      self.context.rptObj.js.objects.this.hide()])
    return dd

  def to(self, y, x=None, icon="fas fa-map-pin", tooltip=None, size=(None, "px"), width=(100, '%'), options=None, profile=False):
    """

    Example
    rptObj.ui.navigation.to(100, tooltip="test")
    
    :param y:
    :param x:
    :param icon:
    :param tooltip:
    :param size:
    :param width:
    :param options:
    :param profile:
    :return:
    """
    dd = self.context.rptObj.ui.icon(icon).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                                                "border-radius": '20px', "padding": '8px', "right": '20px'})
    dd.style.addCls("CssDivOnHoverBackgroundLight")
    if tooltip is not None:
      dd.tooltip(tooltip)
    self.context.rptObj.js.addOnReady(
      self.context.rptObj.js.window.events.addScrollListener([
        self.context.rptObj.js.if_(self.context.rptObj.js.window.scrollY > y, [dd.dom.show()]).else_(dd.dom.hide())
      ]))
    dd.click([
      self.context.rptObj.js.window.scrollTo(x=x, y=y),
      self.context.rptObj.js.objects.this.hide()])
    return dd

  def indices(self, count, selected=1, size=(None, "px"), width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """

    Example

    :param count:
    :param selected:
    :param size:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    size = self.context._size(size)
    html_indices = html.HtmlContainer.Indices(self.context.rptObj, count, size, width, height, dflt_options, profile)
    self.context.register(html_indices)
    return html_indices

  def points(self, count, selected=1, size=(None, "px"), width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """

    Example
    p = rptObj.ui.panels.points(10)
    for i, _ in enumerate(p):
      p.click(i, [])

    :param count:
    :param selected:
    :param size:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    size = self.context._size(size)
    html_points = html.HtmlContainer.Points(self.context.rptObj, count, size, width, height, dflt_options, profile)
    self.context.register(html_points)
    return html_points

  def dots(self, count, selected=1, position="right", size=(None, "px"), width=(100, '%'), height=(None, 'px'), options=None,
           profile=False):
    """

    Example
    d = rptObj.ui.panels.dots(10)

    :param count:
    :param selected:
    :param position:
    :param size:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    dflt_options = {"div_css": {"margin": "2px", "float": position}, "selected": selected}
    dflt_options.update(options or {})
    size = self.context._size(size)
    html_points = html.HtmlContainer.Points(self.context.rptObj, count, size, width, height, dflt_options, profile)
    self.context.register(html_points)
    return html_points
