#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core import html
from epyk.core.css import Defaults_css
from epyk.interfaces import Arguments


class Navigation(object):
  def __init__(self, context):
    self.context = context

  def up(self, icon="fas fa-arrow-up", top=20, right=20, bottom=None, tooltip=None, width=(25, 'px'), height=(25, 'px'),
         options=None, profile=False):
    """
    Description:
    ------------
    Navigation button to go to the top of the page directly

    Usage:
    -----

      page.ui.navigation.up()

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-arrow-up
    :param top: Integer. Optional. The top property affects the vertical position of a positioned element
    :param right: Integer. Optional. The right property affects the horizontal position of a positioned element.
    :param bottom: Integer. Optional. The top property affects the vertical position of a positioned element
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    du = self.context.rptObj.ui.icon(icon, width=width, height=height, options=options, profile=profile).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                                                "border-radius": '20px', "padding": '8px', "right": '%spx' % right})
    if top is not None:
      du.style.css.top = top
    else:
      du.style.css.bottom = bottom
    du.style.add_classes.div.background_hover()
    self.context.rptObj.js.onReady(
      self.context.rptObj.js.window.events.addScrollListener([
        self.context.rptObj.js.if_(self.context.rptObj.js.window.scrollY > 50, [du.dom.show()]).else_(du.dom.hide())
      ]))
    if tooltip is not None:
      du.tooltip(tooltip)
    du.click([
      self.context.rptObj.js.window.scrollUp(),
      self.context.rptObj.js.objects.this.hide()])
    return du

  def down(self, icon="fas fa-arrow-down", top=20, right=20, bottom=None, tooltip=None, width=(25, 'px'), height=(25, 'px'),
         options=None, profile=False):
    """
    Description:
    ------------
    Navigation button to go to the bottom of the page directly

    Usage:
    -----

      page.ui.navigation.down()

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-arrow-up
    :param top: Integer. Optional. The top property affects the vertical position of a positioned element
    :param right: Integer. Optional. The right property affects the horizontal position of a positioned element.
    :param bottom: Integer. Optional. The top property affects the vertical position of a positioned element
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    dd = self.context.rptObj.ui.icon(icon, width=width, height=height, options=options, profile=profile).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
        "border-radius": '20px', "padding": '8px', "right": '%spx' % right})
    if bottom is not None:
      dd.style.css.bottom = bottom
    else:
      dd.style.css.top = top
    dd.style.add_classes.div.background_hover()
    self.context.rptObj.js.onReady(
      self.context.rptObj.js.window.events.addScrollListener([
        self.context.rptObj.js.if_(self.context.rptObj.js.window.scrollY < (self.context.rptObj.js.window.scrollMaxY - 50), [dd.dom.show()]).else_(dd.dom.hide())
      ]))
    if tooltip is not None:
      dd.tooltip(tooltip)
    dd.click([
      self.context.rptObj.js.window.scrollTo(),
      self.context.rptObj.js.objects.this.hide()])
    return dd

  def to(self, y, x=None, icon="fas fa-map-pin", top=20, right=20, bottom=None, tooltip=None, width=(25, 'px'), height=(25, 'px'),
         options=None, profile=False):
    """
    Description:
    ------------
    Navigation button to go to a specific point in the page directly

    Usage:
    -----

      page.ui.navigation.to(100, tooltip="test")

    Attributes:
    ----------
    :param y: Integer. The y position on the page.
    :param x: Integer. Optional. The x position on the page.
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-arrow-up
    :param top: Integer. Optional. The top property affects the vertical position of a positioned element
    :param right: Integer. Optional. The right property affects the horizontal position of a positioned element.
    :param bottom: Integer. Optional. The top property affects the vertical position of a positioned element
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    dd = self.context.rptObj.ui.icon(icon, width=width, height=height, options=options, profile=profile).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                                                "border-radius": '20px', "padding": '8px', "right": '%spx' % right})
    if bottom is not None:
      dd.style.css.bottom = bottom
    else:
      dd.style.css.top = top
    dd.style.add_classes.div.background_hover()
    if tooltip is not None:
      dd.tooltip(tooltip)
    self.context.rptObj.js.onReady(
      self.context.rptObj.js.window.events.addScrollListener([
        self.context.rptObj.js.if_(self.context.rptObj.js.window.scrollY > y, [dd.dom.show()]).else_(dd.dom.hide())
      ]))
    dd.click([
      self.context.rptObj.js.window.scrollTo(x=x, y=y),
      self.context.rptObj.js.objects.this.hide()])
    return dd

  def pin(self, text, url="#", icon="fas fa-map-pin", top=20, right=20, bottom=None, tooltip=None,
          width=(25, 'px'), height=(25, 'px'), options=None, profile=False):
    """
    Description:
    ------------
    Shortcut to a specific position in the page

    Usage:
    -----

      page.ui.navigation.pin("anchor", tooltip="test", bottom=20)

    Attributes:
    ----------
    :param text: String. The shortcut name.
    :param url: String. Optional. The anchor name.
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-arrow-up
    :param top: Integer. Optional. The top property affects the vertical position of a positioned element
    :param right: Integer. Optional. The right property affects the horizontal position of a positioned element.
    :param bottom: Integer. Optional. The top property affects the vertical position of a positioned element
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    dd = self.context.rptObj.ui.icon(icon, width=width, height=height, options=options, profile=profile)
    h_url = self.context.rptObj.ui.link(text, url=url) # .css({"padding-left": "10px"})
    div = self.context.rptObj.ui.div([dd, h_url]).css({"border": '1px solid black', "position": 'fixed', "width": 'none',
                          "border-radius": '30px', "padding": '10px 15px', "right": '%spx' % right,
                          "background-color": self.context.rptObj.theme.greys[0]})
    if bottom is not None:
      div.style.css.bottom = bottom
    else:
      div.style.css.top = top
    div.attr['class'].add("CssDivOnHoverWidth")
    h_url.css({"display": 'none', "white-space": 'nowrap'})
    div.on("mouseover", [h_url.dom.css({"display": 'inline-block', "padding-left": "10px"})])
    div.on("mouseout", [h_url.dom.css({"display": 'none', "padding-left": "0px"})])
    if tooltip is not None:
      div.tooltip(tooltip)
    return div

  def scroll(self, progress=0, height=(3, 'px'), options=None, profile=False):
    """
    Description:
    ------------
    Add a horizontal progressbar to display the status of the page scrollbar.

    Usage:
    -----

      page.ui.navigation.scroll()

    Attributes:
    ----------
    :param progress: Integer. Optional. The progression on the page.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    p = self.context.rptObj.ui.sliders.progressbar(progress, height=height, options=options, profile=profile)
    self.context.rptObj.js.onReady(
      self.context.rptObj.js.window.events.addScrollListener([
        p.build(self.context.rptObj.js.window.scrollPercentage)]))
    return p

  def indices(self, count, selected=1, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.navigation.indices(10)

    Attributes:
    ----------
    :param count:
    :param selected:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    html_indices = html.HtmlContainer.Indices(self.context.rptObj, count, width, height, None, dflt_options, profile)
    return html_indices

  def points(self, count, selected=0, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

      p = page.ui.navigation.points(10)
      for i, _ in enumerate(p):
        p.click_item(i, [])

    Attributes:
    ----------
    :param count:
    :param selected:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    html_points = html.HtmlContainer.Points(self.context.rptObj, count, width, height, htmlCode, dflt_options, profile)
    return html_points

  def dots(self, count, selected=1, position="right", width=(100, '%'), height=(None, 'px'), options=None,
           profile=False):
    """
    Description:
    ------------

    Usage:
    -----

      d = page.ui.navigation.dots(10)

    Attributes:
    ----------
    :param count:
    :param selected:
    :param position: String. Optional. A string with the vertical position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"div_css": {"margin": "2px", "float": position}, "selected": selected}
    dflt_options.update(options or {})
    html_points = html.HtmlContainer.Points(self.context.rptObj, count, width, height, None, dflt_options, profile)
    return html_points

  def path(self, record, divider=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

      record = [{"text": "Lin 1", 'url': 'report_list.html'}, {"text": "Link 2"}]
      page.ui.navigation.path(record)

    Attributes:
    ----------
    :param record:
    :param divider:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    if divider is None:
      divider = self.context.rptObj.symbols.shapes.BLACK_RIGHT_POINTING_TRIANGLE
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    for rec in record[:-1]:
      div += self.context.rptObj.ui.link(rec['text'], url=rec.get('url', '#')).css({"display": 'inline-block'})
      div += self.context.rptObj.ui.text(divider).css({"display": 'inline-block', 'margin': '0 5px', 'font-size': Defaults_css.font(-2)})
    div += self.context.rptObj.ui.link(record[-1]['text'], url=record[-1].get('url', '#')).css({"display": 'inline-block'})
    return div

  def bar(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

      nav = page.ui.navigation.bar(title="test")
      nav.add_text("Test text")
      nav + page.ui.button("Click")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMenu.HtmlNavBar`

    Attributes:
    ----------
    :param logo:
    :param title:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    components = []
    options, scroll_height = options or {}, -5
    options['logo_height'] = tuple(height) if 'logo_height' not in options else Arguments.size(options['logo_height'], unit="px")
    options['logo_width'] = tuple(height) if 'logo_width' not in options else Arguments.size(options['logo_width'], unit="px")

    if logo is None:
      logo = self.context.rptObj.ui.icons.epyk()
      components.append(logo)
    else:
      # if it is not an option it is considered as a path
      if not hasattr(logo, 'options'):
        logo_url = logo
        logo = self.context.rptObj.ui.div(height=options['logo_height'], width=options['logo_width'])
        if logo_url:
          logo.style.css.background_url(logo_url, size="auto %s%s" % (options['logo_height'][0], options['logo_height'][1]))
      components.append(logo)
    components[-1].style.css.margin_right = 20
    if title is not None:
      title = self.context.rptObj.ui.div(title, height=(100, "%"))
      title.style.css.text_transform = "uppercase"
      title.style.css.margin_left = 5
      title.style.css.margin_right = 5
      title.style.css.bold()
      components.append(title)
    if options.get('status', False):
      scroll = self.context.rptObj.ui.navigation.scroll()
      scroll_height = 5
      scroll.style.css.display = "block"
      scroll.options.managed = False
      scroll.style.css.height = scroll_height
    html_nav = html.HtmlMenu.HtmlNavBar(self.context.rptObj, components, width=width, height=height, options=options, profile=profile)
    if options.get('status', False):
      html_nav.scroll = scroll
    html_nav.logo = logo
    html_nav.title = title
    html_nav.logo.style.css.display = "inline-block"
    html_nav.style.css.line_height = height[0]
    Defaults_css.BODY_CONTAINER = {"padding-top": height[0] + scroll_height}
    self.context.rptObj.body.style.custom_class({"padding-top": '%spx' % (height[0] + scroll_height)}, "body", is_class=False)
    return html_nav

  def banner(self, image, text, link, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlImage.Image`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlContainer.Row`
      - :class:`epyk.core.html.HtmlText.Text`
      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Attributes:
    ----------
    :param image:
    :param text:
    :param link:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    h_image = self.context.rptObj.ui.img(image)
    h_text = self.context.rptObj.ui.text(text)
    h_link = self.context.rptObj.ui.links.button("click", link)
    h_row = self.context.rptObj.ui.row(
      [h_image, self.context.rptObj.ui.col([h_text, h_link])])
    div + h_row
    div.style.css.background_color = self.context.rptObj.theme.colors[3]
    div.style.css.color = "white"
    div.style.css.font_size = Defaults_css.font(5)
    div.style.css.text_align = 'center'
    div.style.css.padding = "5px 15px"
    return div

  def footer(self, components=None, width=(100, '%'), height=(80, 'px'), fixed=False, options=None, profile=False):
    """
    Description:
    ------------

    Will create a footer object in the body of the report

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMenu.HtmlFooter`

    Attributes:
    ----------
    :param components: list of html components
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param fixed:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    footer = html.HtmlMenu.HtmlFooter(self.context.rptObj, components, width=width, height=height, options=options, profile=profile)
    if fixed:
      self.context.rptObj.body.style.css.padding_bottom = height[0]
    else:
      footer.style.css.position = None
    return footer

  def side(self, components=None, anchor=None, size=262, position='right', options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/st_news.py

    Attributes:
    ----------
    :param components:
    :param anchor:
    :param size:
    :param position: String. Optional. A string with the vertical position of the component
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    d = self.context.rptObj.ui.div(components)
    d.css({"background": self.context.rptObj.theme.colors[2], "position": 'absolute', 'top': 0, 'height': '100%',
           'overflow-x': 'hidden', 'width': "%spx" % size, 'z-index': 20})
    if position == 'left':
      d.css({'left': 0, 'margin-left': "-%spx" % size, 'border-right': '1px solid %s' % self.context.rptObj.theme.colors[5], 'padding': '5px'})
    else:
      d.css({'right': 0, 'margin-right': "-%spx" % size, 'border-left': '1px solid %s' % self.context.rptObj.theme.colors[5], 'padding': '5px'})
    self.context.rptObj.body.style.custom_class({"overflow-x": 'hidden', "position": 'relative', 'min-height': '100%'}, "html, body", is_class=False)

    def close():
      return d.dom.toggle_transition("margin-left", "0px", "-%spx" % size)
    d.close = close

    if Defaults_css.BODY_CONTAINER is not None:
      d.style.padding_top = Defaults_css.BODY_CONTAINER.get("padding-top", -10) + 10
    if anchor is None:
      if position == 'left':
        i = self.context.rptObj.ui.icon("fas fa-bars").click([d.dom.toggle_transition("margin-left", "0px", "-%spx" % size)])
        i.style.css.float = 'right'
      else:
        i = self.context.rptObj.ui.icon("fas fa-bars").click([d.dom.toggle_transition("margin-right", "0px", "-%spx" % size)])
      i.css({"padding": '5px'})
    else:
      if position == 'left':
        anchor.click([d.dom.toggle_transition("margin-left", "0px", "-%spx" % size)])
      else:
        anchor.click([d.dom.toggle_transition("margin-right", "0px", "-%spx" % size)])
    return d

  def pilcrow(self, text=""):
    """
    Description:
    ------------
    Add an anchor on the page and move to this when it is clicked.

    Attributes:
    ----------
    :param text: String. Optional.
    """
    p = self.context.rptObj.ui.div("%s&#182" % text)
    p.style.css.font_size = Defaults_css.font(5)
    p.style.css.cursor = "pointer"
    p.click([self.context.rptObj.js.window.scrollTo(y=self.context.rptObj.js.objects.this.offsetTop)])
    return p

  def panel(self, width=(100, '%'), height=(100, '%'), options=None, profile=None, helper=None):
    """
    Description:
    ------------

    Usage:
    -----

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/bars.py

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    :param helper: String. Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    dflt_options = {"position": 'top'}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlMenu.PanelsBar(self.context.rptObj, width, height, dflt_options, helper, profile)
    return h_drawer

  def shortcut(self, components=None, logo=None, size=(40, 'px'), options=None, profile=None, htmlCode=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param components:
    :param logo:
    :param size:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    :param htmlCode:
    """
    size = Arguments.size(size, unit="px")
    dflt_options = {"position": 'left'}
    if options is not None:
      dflt_options.update(options)
    if dflt_options["position"] in ['top', 'bottom']:
      width = (100, '%')
      height = size
    else:
      width = size
      height = (100, '%')
    h_drawer = html.HtmlMenu.Shortcut(self.context.rptObj, components or [], logo, width, height, htmlCode, dflt_options, profile)
    return h_drawer


class Banners(object):

  def __init__(self, context):
    self.context = context

  def top(self, data, background=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py

    Attributes:
    ----------
    :param data:
    :param background:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(data, width=width, height=height, options=options, profile=profile)
    div.style.css.background_color = background or self.context.rptObj.theme.colors[3]
    div.style.css.color = "white"
    div.style.css.position = "fixed"
    div.style.css.top = 0
    div.style.css.padding = "5px 15px"
    return div

  def bottom(self, data, background=None, align="center", width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py

    Attributes:
    ----------
    :param data:
    :param background: String. Optional.
    :param align: String. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(data, width=width, height=height, options=options, profile=profile)
    div.style.css.background_color = background or self.context.rptObj.theme.greys[1]
    div.style.css.z_index = 110
    div.style.css.text_align = align
    div.style.css.position = "fixed"
    div.style.css.padding = "5px 15px"
    div.style.css.bottom = 0
    return div

  def cookies(self, text, url, align="center", width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    page.ui.banners.cookies("Test", "#")

    Attributes:
    ----------
    :param text:
    :param url:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    link = self.context.rptObj.ui.link("Learn more", url=url).css({"margin-right": "10px"})
    link.style.css.margin_right = 10
    link.style.css.color = self.context.rptObj.theme.greys[-1]
    button = self.context.rptObj.ui.button("Ok")
    container = self.bottom([
      self.context.rptObj.ui.div([text,
        self.context.rptObj.ui.div([link, button], align="center")
      ])
    ], align=align, width=width, height=height, options=options, profile=profile)
    button.click([container.dom.hide()])
    container.button = button
    container.link = link
    return container

  def corner(self, data, background=None, position="bottom", width=(180, 'px'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py

    Attributes:
    ----------
    :param data:
    :param background:
    :param position: String. Optional. A string with the vertical position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(data, width=width, height=height, options=options, profile=profile)
    div.style.css.background_color = background or self.context.rptObj.theme.colors[3]
    div.style.css.color = "white"
    div.style.css.z_index = 401
    div.style.css.position = "fixed"
    div.style.css.padding = "5px 15px"
    div.style.css.text_align = "center"
    div.style.css.right = 0
    if position == 'bottom':
      div.style.css.bottom = 0
      div.style.css.transform = "rotate(-40deg)"
      div.style.css.margin = "0 -30px 15px 0"
    else:
      div.style.css.top = 0
      div.style.css.transform = "rotate(40deg)"
      div.style.css.margin = "20px -45px 0 0"
    return div

  def info(self, data, icon="fas fa-info-circle", background=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-info-circle
    :param background:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    if not hasattr(data, 'options'):
      data = self.context.rptObj.ui.div(data, width=("auto", ""))
      data.style.css.font_size = "inline-block"
      data.style.css.font_size = Defaults_css.font(4)
    if not hasattr(icon, 'options'):
      icon = self.context.rptObj.ui.icons.awesome(icon)
      icon.style.css.font_size = "inline-block"
    div.add(icon)
    div.add(data)
    div.style.css.background_color = background or self.context.rptObj.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.font_size = Defaults_css.font(4)
    div.style.css.color = self.context.rptObj.theme.greys[-1]
    div.style.css.top = 0
    return div

  def text(self, data="", size_notch=0, background=None, width=(100, '%'), align="center", height=(None, 'px'), options=None, htmlCode=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param size_notch:
    :param background:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(data, 'options'):
      data = self.context.rptObj.ui.div(self.context.rptObj.py.encode_html(data), htmlCode=htmlCode, width=("auto", ""))
      data.style.css.display = "inline-block"
      data.style.css.text_align = align
      data.style.css.font_size = Defaults_css.font(size_notch)
    div.add(data)
    div.style.css.background_color = background or self.context.rptObj.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.font_size = Defaults_css.font(size_notch)
    div.style.css.color = self.context.rptObj.theme.greys[-1]
    div.style.css.top = 0
    return div

  def title(self, title, content, size_notch=0, background=None, width=(100, '%'), align="center", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param title:
    :param content:
    :param size_notch:
    :param background:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    options = options or {}
    if not hasattr(title, 'options'):
      title = self.context.rptObj.ui.titles.title(title)
      title.style.css.text_align = align
      title.style.css.font_weight = 800
      if 'title_color' in options:
        title.style.css.color = options['title_color']
      title.style.css.font_size = Defaults_css.font(options.get("title_notch", 20) + size_notch)
    div.add(title)
    if not hasattr(content, 'options'):
      content = self.context.rptObj.ui.div(content, width=("auto", ""))
      content.style.css.text_align = align
      content.style.css.font_size = "inline-block"
      content.style.css.font_size = Defaults_css.font(size_notch)
    div.add(content)
    div.style.css.background_color = background or self.context.rptObj.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.font_size = Defaults_css.font(size_notch)
    div.style.css.color = self.context.rptObj.theme.greys[-1]
    div.style.css.top = 0
    return div

  def quote(self, content, author, avatar=None, background=None, size_notch=0, width=(100, '%'), align="center", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param content:
    :param author:
    :param avatar:
    :param background:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(content, 'options'):
      content = self.context.rptObj.ui.div('"%s"' % content, width=("auto", ""))
      content.style.css.display = "inline-block"
      content.style.css.text_align = align
      content.style.css.font_size = Defaults_css.font(size_notch)
    div.add(content)
    div.style.css.background_color = background or self.context.rptObj.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.color = self.context.rptObj.theme.greys[-1]
    div.style.css.top = 0
    line = self.context.rptObj.ui.layouts.hr(width=(20, 'px'))
    line.style.css.margin_right = 10
    line.style.css.display = "inline-block"
    if not hasattr(author, 'options'):
      author = self.context.rptObj.ui.div(author, width=("auto", ""))
      author.style.css.display = "inline-block"
    div.add(self.context.rptObj.ui.div([line, author]))
    return div

  def disclaimer(self, copyright=None, links=None, width=(100, '%'), height=("auto", ''), align="center", options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param copyright:
    :param links:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    now = datetime.datetime.now()
    copyright = self.context.rptObj.py.encode_html(copyright or "© 2018 - %s, Epyk studio" % now.year)
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if links is not None:
      for link in links:
        if not isinstance(link, dict):
          link = {"text": link}
        url = self.context.rptObj.ui.link(text=link['text'], url=link.get("url", '#'))
        url.style.css.color = self.context.rptObj.theme.greys[6]
        url.style.css.margin = "0 5px"
        div.add(url)
    text = self.context.rptObj.ui.text(copyright)
    text.style.css.color = self.context.rptObj.theme.greys[-1]
    div.add(text)
    div.style.css.background_color = self.context.rptObj.theme.greys[4]
    div.style.css.color = self.context.rptObj.theme.greys[6]
    div.style.css.padding = "5px 0"
    return div

  def follow(self, text, width=(100, '%'), height=("auto", ''), align="left", options=None, profile=False,
             youtube=True, twitter=True, facebook=True, twitch=True, instagram=True, linkedIn=True):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param text:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    :param youtube: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param twitter: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param facebook: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param twitch: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param instagram: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param linkedIn: Boolean. Optional. Add the icon to the follow bar. Default True.
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.style.css.padding = "10px 0"
    text = self.context.rptObj.ui.text(text)
    div.add(text)

    icon_size = int(Defaults_css.font(8)[:-2])
    if youtube:
      div.youtube = self.context.rptObj.ui.icons.youtube(width=(icon_size, 'px'))
      div.youtube.style.css.margin = "0 2px"
      div.add(div.youtube)

    if twitter:
      div.twitter = self.context.rptObj.ui.icons.twitter(width=(icon_size, 'px'))
      div.twitter.style.css.margin = "0 2px"
      div.add(div.twitter)

    if facebook:
      div.facebook = self.context.rptObj.ui.icons.facebook(width=(icon_size, 'px'))
      div.facebook.style.css.margin = "0 2px"
      div.add(div.facebook)

    if twitch:
      div.twitch = self.context.rptObj.ui.icons.twitch(width=(icon_size, 'px'))
      div.twitch.style.css.margin = "0 2px"
      div.add(div.twitch)

    if instagram:
      div.instagram = self.context.rptObj.ui.icons.instagram(width=(icon_size, 'px'))
      div.instagram.style.css.margin = "0 2px"
      div.add(div.instagram)

    if linkedIn:
      div.linkedIn = self.context.rptObj.ui.icons.linkedIn(width=(icon_size, 'px'))
      div.linkedIn.style.css.margin = "0 2px"
      div.add(div.linkedIn)

    if width != (100, "%"):
      div.style.css.margin = "auto"
      div.style.css.display = "block"
    else:
      div.style.css.background_color = self.context.rptObj.theme.greys[2]
    return div

  def row(self, headers, links, size_notch=0, background=None, width=(100, '%'), align="left", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param headers:
    :param links:
    :param size_notch:
    :param background:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    row = []
    for i, header in enumerate(headers):
      col = self.context.rptObj.ui.col([self.context.rptObj.ui.subtitle(header)], position='top')
      for link in links[i]:
        html_link = self.context.rptObj.ui.link(link)
        html_link.style.css.display = 'block'
        html_link.style.css.margin = "5px 0"
        col.add(html_link)
      row.append(col)
    div.add(self.context.rptObj.ui.row(row))
    div.style.css.background_color = background or self.context.rptObj.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.font_size = Defaults_css.font(size_notch)
    div.style.css.color = self.context.rptObj.theme.greys[-1]
    div.style.css.top = 0

  def contact_us(self, title="Contact Us", background=None, width=(100, '%'), align="left", height=(None, 'px'),
                 htmlCode="contactus", options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param title:
    :param background:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.style.css.padding = 5
    div.add(self.context.rptObj.ui.title(title))
    row = self.context.rptObj.ui.row([self.context.rptObj.ui.input(placeholder="First Name", width=("calc(100% - 5px)", ""), htmlCode="%s_first_name" % htmlCode),
          self.context.rptObj.ui.input(placeholder="Last Name", htmlCode="%s_last_name" % htmlCode)]).css({"padding-top": '5px', "margin": '5px', "width": "calc(100% - 10px)"})
    row.attr["class"].add("no-gutters")
    div.add(row)
    div.add(self.context.rptObj.ui.input(placeholder="Email", htmlCode="%s_email" % htmlCode).css({"margin": '5px', "width": "calc(100% - 10px)"}))
    div.add(self.context.rptObj.ui.input(placeholder="Subject", htmlCode="%s_subject" % htmlCode).css({"margin": '5px', "width": "calc(100% - 10px)"}))
    div.add(self.context.rptObj.ui.textarea(placeholder="Leave us a message", htmlCode="%s_message" % htmlCode).css({"margin": '5px', "width": "calc(100% - 10px)"}))
    div.button = self.context.rptObj.ui.button("Submit", align="center")
    div.add(div.button)
    div.style.css.background_color = background or self.context.rptObj.theme.greys[0]
    div.style.css.margin_bottom = 10
    div._internal_components = ["%s_email" % htmlCode, "%s_first_name" % htmlCode, "%s_last_name" % htmlCode,
                                "%s_subject" % htmlCode, "%s_message" % htmlCode]
    return div

  def sponsor(self, logos, title="Sponsors", content='', background=None, width=(100, '%'), height=("auto", ''), align="center", options=None,
                 profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param logos:
    :param title:
    :param content:
    :param background:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(title, 'options'):
      div.title = self.context.rptObj.ui.titles.title(title)
      div.title.style.css.text_align = align
      div.title.style.css.font_weight = 800
      div.title.style.css.font_size = Defaults_css.font(15)
    else:
      div.title = title
    div.add(div.title)
    if not hasattr(content, 'options'):
      content = self.context.rptObj.ui.div(content, width=("auto", ""))
      content.style.css.text_align = align
      content.style.css.font_size = "inline-block"
    div.add(content)

    div_logos = self.context.rptObj.ui.div("", align=align)
    div.logos = []
    for logo in logos:
      img = self.context.rptObj.ui.img("%s?raw=true" % logo, path="https://github.com/epykure/ressources/blob/master/logos", width=("auto", ''))
      div.logos.append(img)
      img.style.css.display = 'inline-block'
      img.style.css.cursor = 'pointer'
      img.style.css.filter = 'grayscale(100%)'
      img.style.hover({'filter': 'grayscale(0%)'})
      img.style.css.margin = '0 5px'
      div_logos.add(img)
    div.add(div_logos)
    div.style.css.background_color = background or self.context.rptObj.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.color = self.context.rptObj.theme.greys[-1]
    div.style.css.top = 0
    return div


class NavBars(object):

  def __init__(self, context):
    self.context = context

  def fixed(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param logo:
    :param title:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    bar = self.context.rptObj.ui.navbar(logo, title, width, height, options, profile)
    return bar

  def top(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param logo:
    :param title:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    bar = self.context.rptObj.ui.navbar(logo, title, width, height, options, profile)
    bar.style.css.position = False
    return bar

  def transparent(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param logo:
    :param title:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    bar = self.context.rptObj.ui.navbar(logo, title, width, height, options, profile)
    bar.style.css.position = "absolute"
    bar.style.css.top = 0
    bar.no_background()
    return bar

  def dark(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param logo:
    :param title:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    bar = self.context.rptObj.ui.navbar(logo, title, width, height, options, profile)
    bar.style.css.position = "absolute"
    bar.style.css.top = 0
    bar.no_background()
    bar.style.css.opacity = 0.5
    bar.style.css.background = 'black'
    return bar
