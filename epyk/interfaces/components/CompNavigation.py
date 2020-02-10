"""

"""

from epyk.core import html


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
    du.style.add_classes.div.background_hover()
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

  def down(self, icon="fas fa-arrow-down", tooltip=None, width=(100, '%'), options=None, profile=False):
    """

    Example
    rptObj.ui.navigation.down()

    :param icon:
    :param tooltip:
    :param width:
    :param options:
    :param profile:
    """
    dd = self.context.rptObj.ui.icon(icon).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
        "border-radius": '20px', "padding": '8px', "right": '20px', 'top': '20px'})
    dd.style.add_classes.div.background_hover()
    self.context.rptObj.js.addOnReady(
      self.context.rptObj.js.window.events.addScrollListener([
        self.context.rptObj.js.if_(self.context.rptObj.js.window.scrollY < (self.context.rptObj.js.window.scrollMaxY - 50), [dd.dom.show()]).else_(dd.dom.hide())
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
    dd.style.add_classes.div.background_hover()
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

  def pin(self, top=50, right=20, bottom=None, left=None, icon="fas fa-map-pin", tooltip=None, size=(None, "px"),
          width=(100, '%'), options=None, profile=False):
    """

    Example
    rptObj.ui.navigation.to(100, tooltip="test")

    :param top:
    :param right:
    :param bottom:
    :param left:
    :param icon:
    :param tooltip:
    :param size:
    :param width:
    :param options:
    :param profile:
    """
    dd = self.context.rptObj.ui.icon(icon)
    url = self.context.rptObj.ui.link(icon).css({"margin-left": "10px"})
    div = self.context.rptObj.ui.div([dd, url]).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                                      "border-radius": '30px', "padding": '10px 15px', "right": '20px', 'top': '20px',
                                      "background-color": self.context.rptObj.theme.greys[0]})
    div.attr['class'].add("CssDivOnHoverWidth")
    url.css({"display": 'none', "white-space": 'nowrap'})
    div.on("mouseover", [url.dom.css({"display": 'inline-block'})])
    div.on("mouseout", [url.dom.css({"display": 'none'})])
    if tooltip is not None:
      div.tooltip(tooltip)
    return div

  def indices(self, count, selected=1, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """

    Example
    rptObj.ui.navigation.indices(10)

    :param count:
    :param selected:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    html_indices = html.HtmlContainer.Indices(self.context.rptObj, count, width, height, None, dflt_options, profile)
    self.context.register(html_indices)
    return html_indices

  def points(self, count, selected=1, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """

    Example
    p = rptObj.ui.navigation.points(10)
    for i, _ in enumerate(p):
      p.click(i, [])

    :param count:
    :param selected:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    html_points = html.HtmlContainer.Points(self.context.rptObj, count, width, height, None, dflt_options, profile)
    self.context.register(html_points)
    return html_points

  def dots(self, count, selected=1, position="right", width=(100, '%'), height=(None, 'px'), options=None,
           profile=False):
    """

    Example
    d = rptObj.ui.navigation.dots(10)

    :param count:
    :param selected:
    :param position:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    dflt_options = {"div_css": {"margin": "2px", "float": position}, "selected": selected}
    dflt_options.update(options or {})
    html_points = html.HtmlContainer.Points(self.context.rptObj, count, width, height, None, dflt_options, profile)
    self.context.register(html_points)
    return html_points
