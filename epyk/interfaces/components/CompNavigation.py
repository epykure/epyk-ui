
from epyk.core import html
from epyk.core.css import Defaults_css


class Navigation(object):
  def __init__(self, context):
    self.context = context

  def up(self, icon="fas fa-arrow-up", top=20, right=20, bottom=None, tooltip=None, width=(100, '%'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.navigation.up()

    Attributes:
    ----------
    :param icon:
    :param top:
    :param right:
    :param bottom:
    :param tooltip:
    :param width:
    :param options:
    :param profile:
    """
    du = self.context.rptObj.ui.icon(icon).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                                                "border-radius": '20px', "padding": '8px', "right": '%spx' % right})
    if top is not None:
      du.style.css.top = top
    else:
      du.style.css.bottom = bottom
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

  def down(self, icon="fas fa-arrow-down", top=20, right=20, bottom=None, tooltip=None, width=(100, '%'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.navigation.down()

    Attributes:
    ----------
    :param icon:
    :param top:
    :param right:
    :param bottom:
    :param tooltip:
    :param width:
    :param options:
    :param profile:
    """
    dd = self.context.rptObj.ui.icon(icon).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
        "border-radius": '20px', "padding": '8px', "right": '%spx' % right})
    if bottom is not None:
      dd.style.css.bottom = bottom
    else:
      dd.style.css.top = top
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

  def to(self, y, x=None, icon="fas fa-map-pin", top=20, right=20, bottom=None, tooltip=None, width=(100, '%'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.navigation.to(100, tooltip="test")

    Attributes:
    ----------
    :param y:
    :param x:
    :param icon:
    :param top:
    :param right:
    :param bottom:
    :param tooltip:
    :param width:
    :param options:
    :param profile:
    :return:
    """
    dd = self.context.rptObj.ui.icon(icon).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                                                "border-radius": '20px', "padding": '8px', "right": '%spx' % right})
    if bottom is not None:
      dd.style.css.bottom = bottom
    else:
      dd.style.css.top = top
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

  def pin(self, text, url="#", icon="fas fa-map-pin", top=20, right=20, bottom=None, tooltip=None, width=(100, '%'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.navigation.pin("anchor", tooltip="test", bottom=20)

    Attributes:
    ----------
    :param text:
    :param url:
    :param icon:
    :param top:
    :param right:
    :param bottom:
    :param tooltip:
    :param width:
    :param options:
    :param profile:
    """
    dd = self.context.rptObj.ui.icon(icon)
    h_url = self.context.rptObj.ui.link(text, url=url).css({"margin-left": "10px"})
    div = self.context.rptObj.ui.div([dd, h_url]).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                          "border-radius": '30px', "padding": '10px 15px', "right": '%spx' % right,
                          "background-color": self.context.rptObj.theme.greys[0]})
    if bottom is not None:
      div.style.css.bottom = bottom
    else:
      div.style.css.top = top
    div.attr['class'].add("CssDivOnHoverWidth")
    h_url.css({"display": 'none', "white-space": 'nowrap'})
    div.on("mouseover", [h_url.dom.css({"display": 'inline-block'})])
    div.on("mouseout", [h_url.dom.css({"display": 'none'})])
    if tooltip is not None:
      div.tooltip(tooltip)
    return div

  def scroll(self, position=0, height=(3, 'px'), options=None, profile=False):
    """
    Description:
    ------------
    Add a horizontal progressbar to display the status of the page scrollbar.

    Usage:
    ------
    rptObj.ui.navigation.scroll()

    Attributes:
    ----------
    :param position:
    :param height:
    :param options:
    :param profile:
    """
    p = self.context.rptObj.ui.sliders.progressbar(position, height=height, options=options, profile=profile)
    self.context.rptObj.js.addOnReady(
      self.context.rptObj.js.window.events.addScrollListener([
        p.build(self.context.rptObj.js.window.scrollPercentage)]))
    return p

  def indices(self, count, selected=1, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.navigation.indices(10)

    Attributes:
    ----------
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

  def points(self, count, selected=0, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    ------
    p = rptObj.ui.navigation.points(10)
    for i, _ in enumerate(p):
      p.click_item(i, [])

    Attributes:
    ----------
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
    Description:
    ------------

    Usage:
    ------
    d = rptObj.ui.navigation.dots(10)

    Attributes:
    ----------
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

  def path(self, records, divider=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    ------
    record = [{"text": "Lin 1", 'url': 'report_list.html'}, {"text": "Link 2"}]
    rptObj.ui.navigation.path(record)

    Attributes:
    ----------
    :param records:
    :param divider:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    if divider is None:
      divider = self.context.rptObj.symbols.shapes.BLACK_RIGHT_POINTING_TRIANGLE
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    for rec in records[:-1]:
      div += self.context.rptObj.ui.link(rec['text'], url=rec.get('url', '#')).css({"display": 'inline-block'})
      div += self.context.rptObj.ui.text(divider).css({"display": 'inline-block', 'margin': '0 5px', 'font-size': Defaults_css.font(-2)})
    div +=self.context.rptObj.ui.link(records[-1]['text'], url=records[-1].get('url', '#')).css({"display": 'inline-block'})
    return div

  def bar(self, icon=None, title=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon:
    :param title:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    div.style.css.margin = 0
    div.style.css.left = 0
    div.style.css.padding = "5px 2px 0 2px"
    div.style.css.position = "fixed"
    div.style.css.background_color = self.context.rptObj.theme.greys[0]
    div.style.css.border_bottom = "1px solid %s" % self.context.rptObj.theme.greys[4]
    div.style.css.top = 0
    if icon is None:
      div += self.context.rptObj.ui.icons.epyk()
    if title is not None:
      html_title = self.context.rptObj.ui.title(title)
      html_title.style.css.width = "auto"
      html_title.style.css.margin = "0 0 0 5px"
      html_title.style.css.vertical_align = 'top'
      html_title.style.css.display = "inline-block"
      html_title.style.css.font_size = 25
      div += html_title
    div += self.context.rptObj.ui.navigation.scroll()
    return div
