#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from typing import Union, Optional, List

from epyk.core import html
from epyk.core.css import Defaults_css
from epyk.core.html import Defaults_html
from epyk.interfaces import Arguments


class Navigation:

  def __init__(self, ui):
    self.page = ui.page

  def __format_text(self, text: Union[str, dict], size: str = None, italic: bool = True) -> str:
    if isinstance(text, dict):
      sub_title = self.page.ui.div(list(text.values())[0])
      sub_title.options.managed = False
      if italic:
        sub_title.style.css.italic()
      sub_title.style.css.color = self.page.theme.greys[4]
      sub_title.style.css.text_transform = "lowercase"
      sub_title.style.css.display = "inline"
      sub_title.style.css.font_size = size or self.page.body.style.globals.font.normal(-3)
      return "<b>%s</b> %s" % (list(text.keys())[0], sub_title.html())

    return text

  def up(self, icon: str = "fas fa-arrow-up", top: int = 20, right: int = 20, bottom: int = None, tooltip: str = None,
         width: Union[tuple, int] = (25, 'px'), height: Union[tuple, int] = (25, 'px'),
         options: dict = None, profile: Union[bool, dict] = None) -> html.HtmlImage.Icon:
    """Navigation button to go to the top of the page directly.

    :tags:
    :categories:

    Usage::
      page.ui.navigation.up()

    :param icon: Optional. The component icon content from font-awesome references. Default fas fa-arrow-up
    :param top: Optional. The top property affects the vertical position of a positioned element
    :param right: Optional. The right property affects the horizontal position of a positioned element
    :param bottom: Optional. The top property affects the vertical position of a positioned element
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    du = self.page.ui.icon(icon, width=width, height=height, options=options, profile=profile).css(
      {"border": '1px solid black', "position": 'fixed', "width": 'none', "border-radius": '20px', "padding": '8px',
       "right": '%spx' % right})
    if top is not None:
      du.style.css.top = top
    else:
      du.style.css.bottom = bottom
    du.style.add_classes.div.background_hover()
    self.page.js.onReady(
      self.page.js.window.events.addScrollListener([
        self.page.js.if_(self.page.js.window.scrollY > 50, [du.dom.show()]).else_(du.dom.hide())
      ]))
    if tooltip is not None:
      du.tooltip(tooltip)
    du.click([
      self.page.js.window.scrollUp(),
      self.page.js.objects.this.hide()])
    html.Html.set_component_skin(du)
    return du

  def down(self, icon: str = "fas fa-arrow-down", top: int = 20, right: int = 20, bottom: int = None,
           tooltip: str = None, width: Union[tuple, int] = (25, 'px'), height: Union[tuple, int] = (25, 'px'),
           options: dict = None, profile: Union[bool, dict] = None) -> html.HtmlImage.Icon:
    """Navigation button to go to the bottom of the page directly.

    :tags:
    :categories:

    Usage::
      page.ui.navigation.down()

    :param icon: Optional. The component icon content from font-awesome references. Default fas fa-arrow-up
    :param top: Optional. The top property affects the vertical position of a positioned element
    :param right: Optional. The right property affects the horizontal position of a positioned element
    :param bottom: Optional. The top property affects the vertical position of a positioned element
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    dd = self.page.ui.icon(icon, width=width, height=height, options=options, profile=profile).css(
      {"border": '1px solid black', "position": 'fixed', "width": 'none', "border-radius": '20px', "padding": '8px',
       "right": '%spx' % right})
    if bottom is not None:
      dd.style.css.bottom = bottom
    else:
      dd.style.css.top = top
    dd.style.add_classes.div.background_hover()
    self.page.js.onReady(
      self.page.js.window.events.addScrollListener([
        self.page.js.if_(
          self.page.js.window.scrollY < (self.page.js.window.scrollMaxY - 50), [dd.dom.show()]).else_(dd.dom.hide())
      ]))
    if tooltip is not None:
      dd.tooltip(tooltip)
    dd.click([
      self.page.js.window.scrollTo(),
      self.page.js.objects.this.hide()])
    html.Html.set_component_skin(dd)
    return dd

  def to(self, y, x: int = None, icon: str = "fas fa-map-pin", top: int = 20, right: int = 20,
         bottom: Optional[int] = None, tooltip: str = None, width: Union[tuple, int] = (25, 'px'),
         height: Union[tuple, int] = (25, 'px'), options: dict = None, profile: Union[bool, dict] = None
         ) -> html.HtmlImage.Icon:
    """Navigation button to go to a specific point in the page directly.

    :tags:
    :categories:

    Usage::
      page.ui.navigation.to(100, tooltip="test")

    :param y: The y position on the page
    :param x: Optional. The x position on the page
    :param icon: Optional. The component icon content from font-awesome references. Default fas fa-arrow-up
    :param top: Optional. The top property affects the vertical position of a positioned element
    :param right: Optional. The right property affects the horizontal position of a positioned element
    :param bottom: Optional. The top property affects the vertical position of a positioned element
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    dd = self.page.ui.icon(icon, width=width, height=height, options=options, profile=profile).css(
      {"border": '1px solid black', "position": 'fixed', "width": 'none', "border-radius": '20px', "padding": '8px',
       "right": '%spx' % right})
    if bottom is not None:
      dd.style.css.bottom = bottom
    else:
      dd.style.css.top = top
    dd.style.add_classes.div.background_hover()
    if tooltip is not None:
      dd.tooltip(tooltip)
    self.page.js.onReady(
      self.page.js.window.events.addScrollListener([
        self.page.js.if_(self.page.js.window.scrollY > y, [dd.dom.show()]).else_(dd.dom.hide())
      ]))
    dd.click([
      self.page.js.window.scrollTo(x=x, y=y),
      self.page.js.objects.this.hide()])
    html.Html.set_component_skin(dd)
    return dd

  def pin(self, text: str, url: str = "#", icon: str = "fas fa-map-pin", top: int = 20, right: int = 20,
          bottom: int = None, tooltip: str = None, width: Union[tuple, int] = (25, 'px'),
          height: Union[tuple, int] = (25, 'px'), options: dict = None, profile: Union[bool, dict] = None
          ) -> html.HtmlImage.Icon:
    """Shortcut to a specific position in the page.

    :tags:
    :categories:

    Usage::

      page.ui.navigation.pin("anchor", tooltip="test", bottom=20)

    :param text: The shortcut name
    :param url: Optional. The anchor name
    :param icon: Optional. The component icon content from font-awesome references. Default fas fa-arrow-up
    :param top: Optional. The top property affects the vertical position of a positioned element
    :param right: Optional. The right property affects the horizontal position of a positioned element
    :param bottom: Optional. The top property affects the vertical position of a positioned element
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    dd = self.page.ui.icon(icon, width=width, height=height, options=options, profile=profile)
    h_url = self.page.ui.link(text, url=url)
    div = self.page.ui.div([dd, h_url]).css(
      {"border": '1px solid black', "position": 'fixed', "width": 'none', "border-radius": '30px',
       "padding": '10px 15px', "right": '%spx' % right, "background-color": self.page.theme.greys[0]})
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
    html.Html.set_component_skin(div)
    return div

  def scroll(self, progress: int = 0, height: Union[tuple, int] = (3, 'px'), options: dict = None,
             profile: Union[bool, dict] = None, html_code: str = None):
    """
    Add a horizontal progressbar to display the status of the page scrollbar.

    :tags:
    :categories:

    Usage::

      page.ui.navigation.scroll()

    :param progress: Optional. The progression on the page
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    :param html_code: Optional.
    """
    height = Arguments.size(height, unit="px")
    p = self.page.ui.sliders.progressbar(progress, height=height, options=options, profile=profile, html_code=html_code)
    self.page.js.onReady(
      self.page.js.window.events.addScrollListener([
        p.build(self.page.js.window.scrollPercentage)]))
    html.Html.set_component_skin(p)
    return p

  def indices(self, count: int, selected: int = 1, width: Union[tuple, int] = (100, '%'),
              height: Union[tuple, int] = (None, 'px'), html_code: str = None, options: dict = None,
              profile: Union[bool, dict] = None) -> html.HtmlContainer.Indices:
    """

    :tags:
    :categories:

    Usage::
      page.ui.navigation.indices(10)

    :param count: Optional. The number of pages
    :param selected: Optional. The selected index
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    html_indices = html.HtmlContainer.Indices(self.page, count, width, height, html_code, dflt_options, profile)
    html.Html.set_component_skin(html_indices)
    return html_indices

  def more(self, text: str = "See more", icon: Optional[Union[str, bool]] = None,
           width: Union[tuple, int] = ('auto', ""),
           tooltip: Optional[str] = None, height: Union[tuple, int] = (None, "px"),
           align: str = "left", html_code: Optional[str] = None, profile: Union[dict, bool] = None,
           options: Optional[dict] = None):
    """Add a see more button to get the number of calls for a pagination on the server side.

    Usage::
      t = page.ui.text("Rewind")
      btn = page.ui.navigation.more()
      btn.click([page.js.console.log(btn.dom.next())])
      t.click([btn.dom.rewind()])

    :param text: Optional. The value to be displayed to the button
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    btn = self.page.ui.buttons.text(text=text, icon=icon, width=width, tooltip=tooltip, height=height, align=align,
                                    html_code=html_code, profile=profile, options=options)
    btn.style.css.font_factor(-3)
    btn.style.css.cursor = "pointer"
    btn.attr["click-count"] = 0

    def rewind():
      return btn.dom.setAttribute("click-count", 0)

    def next():
      return btn.dom.getAttribute("click-count")

    btn.dom.rewind = rewind
    btn.dom.next = next

    def click(js_funcs, source_event=None, profile=None, on_ready=False):
      if on_ready:
        self.page.body.onReady([btn.dom.events.trigger("click")])
      extra = [
        self.page.js.objects.new(btn.dom.getAttribute("click-count").toNumber() + 1, "countClick"),
        btn.dom.setAttribute("click-count", self.page.js.objects.get("countClick"))]
      return btn.on("click", extra + js_funcs, profile, source_event)

    btn.click = click
    return btn

  def points(self, count: int, selected: int = 0, width: Union[tuple, int] = (100, '%'),
             height: Union[tuple, int] = (None, 'px'), html_code: str = None, options: dict = None,
             profile: Union[dict, bool] = False) -> html.HtmlContainer.Points:
    """

    :tags:
    :categories:

    Usage::
      p = page.ui.navigation.points(10)
      for i, _ in enumerate(p):
        p.click_item(i, [])

    :param count: The number of pages
    :param selected: Optional. The selected index
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"div_css": {"display": "inline-block", "margin": "0 2px"}, "selected": selected}
    dflt_options.update(options or {})
    html_points = html.HtmlContainer.Points(self.page, count, width, height, html_code, dflt_options, profile)
    html.Html.set_component_skin(html_points)
    return html_points

  def dots(self, count: int, selected: int = 1, position: str = "right", width: Union[tuple, int] = (100, '%'),
           height: Union[tuple, int] = (None, 'px'), html_code: str = None, options: dict = None,
           profile: Union[dict, bool] = False):
    """

    :tags:
    :categories:

    Usage::
      d = page.ui.navigation.dots(10)

    :param count: Optional. The number of pages
    :param selected: Optional. The selected index
    :param position: Optional. A string with the vertical position of the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"div_css": {"margin": "2px", "float": position}, "selected": selected}
    dflt_options.update(options or {})
    html_points = html.HtmlContainer.Points(self.page, count, width, height, html_code, dflt_options, profile)
    html.Html.set_component_skin(html_points)
    return html_points

  def path(self, record: List[dict], divider: str = None, width: Union[tuple, int] = (100, '%'),
           height: Union[tuple, int] = (None, 'px'), options: dict = None, profile: Union[dict, bool] = False):
    """

    :tags:
    :categories:

    Usage::
      record = [{"text": "Lin 1", 'url': 'report_list.html'}, {"text": "Link 2"}]
      page.ui.navigation.path(record)

    :param record: Component input data
    :param divider: Optional. A path delimiter
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    if divider is None:
      divider = self.page.symbols.shapes.BLACK_RIGHT_POINTING_TRIANGLE
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    for rec in record[:-1]:
      div += self.page.ui.link(rec['text'], url=rec.get('url', '#')).css({"display": 'inline-block'})
      div += self.page.ui.text(divider).css(
        {"display": 'inline-block', 'margin': '0 5px', 'font-size': self.page.body.style.globals.font.normal(-2)})
    div += self.page.ui.link(record[-1]['text'], url=record[-1].get('url', '#')).css(
      {"display": 'inline-block'})
    html.Html.set_component_skin(div)
    return div

  def nav(self, logo=None, title: str = None, components=None, size: Union[tuple, int] = (40, 'px'),
          options: dict = None, avatar: bool = False, html_code: str = "page_nav_bar", profile: Union[dict, bool] = False
          ) -> html.HtmlMenu.HtmlNavBar:
    """

    :tags:
    :categories:

    Usage::
      page.ui.components_skin = {"nav": {"css": {"background-color": 'pink'}}}
      nav = page.ui.navigation.nav(height=60, options={"center": True, "logo_height": 50})

    :param logo: Optional. The picture for the logo
    :param title: Optional. A panel title. This will be attached to the title property
    :param components: Optional. The Components to be added to the navbar
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param avatar: Optional. Add a avatar picture to the right in the navbar
    :param profile: Optional. A flag to set the component performance storage
    """
    if html_code not in self.page.components:
      nav_bar = self.bar(logo, title, size, options, avatar=avatar, html_code=html_code, profile=profile)
    else:
      nav_bar = self.page.components[html_code]
    if components is not None:
      for component in components:
        nav_bar.add(component)
    html.Html.set_component_skin(nav_bar)
    return nav_bar

  def bar(self, logo=None, title=None, size: Union[tuple, int] = (40, 'px'),
          options=None, html_code: str = None, avatar: Union[bool, str] = False,
          profile: Union[dict, bool] = False) -> html.HtmlMenu.HtmlNavBar:
    """

    :tags:
    :categories:

    Usage::
      nav = page.ui.navigation.bar(title="test")
      nav.add_text("Test text")
      nav + page.ui.button("Click")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMenu.HtmlNavBar`

    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property
    :param size: Tuple. Optional. A tuple with the integer for the component width or height and its unit
    :param options: Optional. Specific Python options available for this component
    :param avatar: Optional.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    options = options or {}
    html_nav = html.HtmlMenu.HtmlNavBar(
      self.page, [], logo=logo, title=title, avatar=avatar, size=Arguments.size(size, unit="px"),
      options=options, html_code=html_code, profile=profile)
    html.Html.set_component_skin(html_nav)
    return html_nav

  def banner(self, image: str = "", text: str = "", link: str = "", width: Union[tuple, int] = (100, '%'),
             height: Union[tuple, int] = (None, 'px'), options: dict = None, profile: Union[dict, bool] = False):
    """

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlImage.Image`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlContainer.Row`
      - :class:`epyk.core.html.HtmlText.Text`
      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    :param image: Optional. The image full path
    :param text: Optional. The value to be displayed to the component
    :param link: Optional. The url link
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    h_image = self.page.ui.img(image)
    h_text = self.page.ui.text(text)
    h_link = self.page.ui.links.button("click", link)
    h_row = self.page.ui.row(
      [h_image, self.page.ui.col([h_text, h_link])])
    div + h_row
    div.style.css.background_color = self.page.theme.colors[3]
    div.style.css.color = "white"
    div.style.css.font_size = self.page.body.style.globals.font.normal(5)
    div.style.css.text_align = 'center'
    div.style.css.padding = "5px 15px"
    html.Html.set_component_skin(div)
    return div

  def footer(self, components=None, logo=None, width: Union[tuple, int] = (100, '%'), height: Union[tuple, int] = (40, 'px'),
             fixed=False, options=None, profile=False) -> html.HtmlMenu.HtmlFooter:
    """

    Will create a footer object in the body of the report.

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMenu.HtmlFooter`

    :param components: list of html components.
    :param logo:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param fixed: Boolean. Optional. Fix the component at the page bottom.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlMenu.HtmlFooter(
      self.page, components, logo=logo, width=width, height=height, options=options, profile=profile)
    if fixed:
      self.page.body.style.css.padding_bottom = height[0]
    else:
      component.style.css.position = 'initial'
    html.Html.set_component_skin(component)
    return component

  def side(self, components=None, anchor=None, size=262, position='right', options=None, profile=False,
           z_index: int = 20, overlay: bool = False, padding: int = None) -> html.HtmlContainer.Div:
    """

    :tags:
    :categories:

    Usage::

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/st_news.py

    :param components: The different HTML objects to be added to the component.
    :param anchor: Optional. The panel button to show / hide.
    :param size: Optional. Panel's width in pixel.
    :param position: Optional. A string with the vertical position of the component.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    :param z_index: Optional.
    :param overlay: Optional.
    :param padding: Optional.
    """
    position_type = "absolute" if self.page.body.template is None else 'fixed'
    d = self.page.ui.div(components, options=options, profile=profile)
    # Default position based on the navbar orient
    position = {"horizontal": "top", "vertical": "left"}.get(position, position)
    d.options.set(position, name="position")
    d.set_style_map(["interf-navs.css"])
    d.classList.add("i-nav-side-panel")
    d.classList.add("i-nav-side-panel-%s" % position[0])
    d.css({'margin-%s' % position: "-%spx" % size, 'z-index': z_index, "position": position_type})
    if padding:
      d.css({'padding-%s' % position: Arguments.size(padding, toStr=True)})
    if d.options.get(name="position") == 'left':
      d.css({'width': "%spx" % size})
    elif d.options.get(name="position") == 'top':
      d.css({'height': "%spx" % size, "width": "100%"})
    else:
      d.css({'width': "%spx" % size})
    self.page.body.style.custom_class({
      "overflow-x": 'hidden', "position": 'relative', 'min-height': '100%'}, "html, body", is_class=False)

    def close():
      return d.dom.toggle_transition("margin-left", "0px", "-%spx" % size)
    d.close = close

    if Defaults_css.BODY_CONTAINER is not None:
      d.style.padding_top = Defaults_css.BODY_CONTAINER.get("padding-top", -10) + 10

    if overlay:
      overlay = self.page.ui.div(width=(100, "vw"), height=(100, "vh"))
      overlay.style.css.z_index = z_index - 1
      overlay.classList.add("i-nav-side-overlay")
      overlay_event = [overlay.dom.toggle()]
      d.overlay = overlay
    else:
      overlay_event = []
    html.Html.set_component_skin(d)
    if anchor is None:
      if d.options.get(name="position") == 'left':
        i = self.page.ui.icon("fas fa-bars").click(
          overlay_event + [d.dom.toggle_transition("margin-left", "0px", "-%spx" % size)])
        i.style.css.float = 'right'
        if position_type == "fixed":
          i.style.css.position = "fixed"
          i.style.css.right = 10
          i.style.css.top = 5
      else:
        i = self.page.ui.icon("fas fa-bars").click(
          overlay_event + [d.dom.toggle_transition("margin-right", "0px", "-%spx" % size)])
        if position_type == "fixed":
          i.style.css.position = "fixed"
          i.style.css.left = 10
          i.style.css.top = 10
      i.css({"padding": '5px'})
      if overlay:
        overlay.click([i.dom.events.trigger("click")])
    else:
      if position == 'left':
        anchor.click(
          overlay_event + [d.dom.toggle_transition("margin-left", "0px", "-%spx" % size)])
      if position == 'top':
        anchor.click(
          overlay_event + [d.dom.toggle_transition("margin-top", "0px", "-%spx" % size)])
      else:
        anchor.click(
          overlay_event + [d.dom.toggle_transition("margin-right", "0px", "-%spx" % size)])
      if overlay:
        overlay.click([anchor.dom.events.trigger("click")])
    return d

  def pilcrow(self, text: str = "", html_code: str = None, options: dict = None,
              profile: Union[dict, bool] = None) -> html.HtmlContainer.Div:
    """Add an anchor on the page and move to this when it is clicked.

    :tags:
    :categories:

    Usage::
      page.ui.navigation.pilcrow()

    :param text: Optional. The value to be displayed to the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    p = self.page.ui.div("%s&#182" % text, html_code=html_code, options=options, profile=profile)
    p.style.css.font_size = self.page.body.style.globals.font.normal(5)
    p.style.css.cursor = "pointer"
    p.click([self.page.js.window.scrollTo(y=self.page.js.objects.this.offsetTop)])
    html.Html.set_component_skin(p)
    return p

  def panel(self, width: Union[tuple, int] = (100, '%'), height: Union[tuple, int] = (100, '%'), options: dict = None,
            profile: Union[dict, bool] = None, helper: str = None) -> html.HtmlMenu.PanelsBar:
    """

    :tags:
    :categories:

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/bars.py

    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    dfl_options = {"position": 'top'}
    if options is not None:
      dfl_options.update(options)
    h_drawer = html.HtmlMenu.PanelsBar(self.page, width, height, dfl_options, helper, profile)
    html.Html.set_component_skin(h_drawer)
    return h_drawer

  def shortcut(self, components=None, logo=None, size=(40, 'px'), options=None,
               profile=None, html_code=None) -> html.HtmlMenu.Shortcut:
    """

    :tags:
    :categories:

    :param components: List. The different HTML objects to be added to the component.
    :param logo:
    :param size: Integer. Optional. Panel's height in pixel.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    size = Arguments.size(size, unit="px")
    dfl_options = {"position": 'left'}
    if options is not None:
      dfl_options.update(options)
    if dfl_options["position"] in ['top', 'bottom']:
      width = (100, '%')
      height = size
    else:
      width = size
      height = (100, '%')
    h_drawer = html.HtmlMenu.Shortcut(
      self.page, components or [], logo, width, height, html_code, dfl_options, profile)
    h_drawer.style.css.padding = "5px 10px"
    html.Html.set_component_skin(h_drawer)
    return h_drawer


class Banners:

  def __init__(self, ui):
    self.page = ui.page

  def top(
          self, data="", background=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None
  ) -> html.HtmlContainer.Div:
    """

    :tags:
    :categories:

    Usage::
      # to Change the CSS style
      top = page.ui.banners.top("text")
      top.style.css.font_size = '40px'

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py

    :param data:
    :param background: String. Optional. Background color code.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(data, width=width, height=height, options=options, profile=profile)
    if div.style.css.height is None:
      div.style.css.min_height = Defaults_html.LINE_HEIGHT
    div.style.css.background_color = background or self.page.theme.colors[3]
    div.style.css.color = "white"
    div.style.css.position = "fixed"
    div.style.css.top = 0
    div.style.css.left = 0
    div.style.css.z_index = 500
    div.style.css.padding = "5px 15px"
    html.Html.set_component_skin(div)
    return div

  def bottom(self, data: Union[str, list] = "", background=None, align="center", width=(100, '%'), height=(None, 'px'),
             options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::
      # Add a banner with HTML content
      icon = page.ui.icon("fab fa-python")
      text = page.ui.text("This is a text")

      # Chang the option to have the content in one line
      bottom = page.ui.banners.bottom([icon, text], options={"inline": True})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py

    :param data:
    :param background: String. Optional. Background color code.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(data, width=width, height=height, options=options, profile=profile)
    if div.style.css.height is None:
      div.style.css.min_height = Defaults_html.LINE_HEIGHT
    div.style.css.background_color = background or self.page.theme.greys[1]
    div.style.css.z_index = 110
    div.style.css.left = 0
    div.style.css.z_index = 500
    div.style.css.text_align = align
    div.style.css.position = "fixed"
    div.style.css.padding = "5px 15px"
    div.style.css.bottom = 0
    html.Html.set_component_skin(div)
    return div

  def cookies(self, text, url, align="center", width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::
      page.ui.banners.cookies("Test", "#")

    :param text: String. The value to be displayed to the component.
    :param url: String. The url link.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile:  Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    link = self.page.ui.link("Learn more", url=url).css({"margin-right": "10px"})
    link.style.css.margin_right = 10
    link.style.css.color = self.page.theme.greys[-1]
    button = self.page.ui.button("Ok")
    container = self.bottom([
      self.page.ui.div([
        text,
        self.page.ui.div([link, button], align="center")
      ])
    ], align=align, width=width, height=height, options=options, profile=profile)
    button.click([container.dom.hide()])
    container.button = button
    container.link = link
    html.Html.set_component_skin(container)
    return container

  def corner(self, data="", background=None, position="bottom", width=(180, 'px'), height=(None, 'px'), options=None,
             profile=None):
    """

    :tags:
    :categories:

    Usage::
      # Add a banner on the bottom right corner
      b = page.ui.banners.corner("bottom", 'red')
      # Add click event on the banner
      b.click([
        # hide the bonner on click
        b.dom.hide()
      ])

      # Add a banner on the top right conner
      corner = page.ui.banners.corner("top", 'red', position='top')
      # Add interactivity on the banner style
      corner.style.hover({"background": "white", 'color': 'red'})
      # display the banner
      corner.hover([b.dom.show()])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py

    :param data:
    :param background: String. Optional. Background color code.
    :param position: String. Optional. A string with the vertical position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    options = options or {}
    div = self.page.ui.div(data, width=width, height=height, options=options, profile=profile)
    if div.style.css.height is None:
      div.style.css.min_height = Defaults_html.LINE_HEIGHT
    div.style.css.background_color = background or self.page.theme.colors[3]
    div.style.css.color = "white"
    div.style.css.z_index = options.get("z_index", 860)
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
    html.Html.set_component_skin(div)
    return div

  def info(self, data, icon="fas fa-info-circle", background=None, width=(100, '%'), height=(None, 'px'), options=None,
           profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param data:
    :param icon: String. Optional. The component icon content from font-awesome references. Default fas fa-info-circle
    :param background: String. Optional. Background color code.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    if not hasattr(data, 'options'):
      data = self.page.ui.div(data, width=("auto", ""))
      data.style.css.font_size = "inline-block"
      data.style.css.font_size = self.page.body.style.globals.font.normal(4)
    if not hasattr(icon, 'options'):
      icon = self.page.ui.icons.awesome(icon)
      icon.style.css.font_size = "inline-block"
    div.add(icon)
    div.add(data)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.font_size = self.page.body.style.globals.font.normal(4)
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    html.Html.set_component_skin(div)
    return div

  def text(self, data="", size_notch=0, background=None, width=(100, '%'), align="center", height=(None, 'px'),
           options=None, html_code=None, profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param data:
    :param size_notch:
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(data, 'options'):
      data = self.page.ui.div(self.page.py.encode_html(data), html_code=html_code, width=("auto", ""))
      data.style.css.display = "inline-block"
      data.style.css.text_align = align
      data.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.add(data)
    if background is not None:
      div.style.css.background_color = background
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    html.Html.set_component_skin(div)
    return div

  def title(self, title, content, size_notch=0, background=None, width=(100, '%'), align="center", height=(None, 'px'),
            options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param title:  String. Optional. A panel title. This will be attached to the title property.
    :param content: String. Optional. The value to be displayed to the component.
    :param size_notch:
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    options = options or {}
    if not hasattr(title, 'options'):
      title = self.page.ui.titles.title(title)
      title.style.css.text_align = align
      title.style.css.font_weight = 800
      if 'title_color' in options:
        title.style.css.color = options['title_color']
      title.style.css.font_size = self.page.body.style.globals.font.normal(options.get("title_notch", 20) + size_notch)
    div.add(title)
    if not hasattr(content, 'options'):
      content = self.page.ui.div(content, width=("auto", ""))
      content.style.css.text_align = align
      content.style.css.font_size = "inline-block"
      content.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.add(content)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    html.Html.set_component_skin(div)
    return div

  def quote(self, content, author, avatar=None, background=None, size_notch=0, width=(100, '%'), align="center",
            height=(None, 'px'), options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param content: String. Optional. The value to be displayed to the component.
    :param author:
    :param avatar:
    :param background: String. Optional. Background color code.
    :param size_notch:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(content, 'options'):
      content = self.page.ui.div('"%s"' % content, width=("auto", ""))
      content.style.css.display = "inline-block"
      content.style.css.text_align = align
      content.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.add(content)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    line = self.page.ui.layouts.hr(width=(20, 'px'))
    line.style.css.margin_right = 10
    line.style.css.display = "inline-block"
    if not hasattr(author, 'options'):
      author = self.page.ui.div(author, width=("auto", ""))
      author.style.css.display = "inline-block"
    div.add(self.page.ui.div([line, author]))
    html.Html.set_component_skin(div)
    return div

  def disclaimer(self, copyright=None, links=None, width=(100, '%'), height=("auto", ''), align="center", options=None,
                 profile=None):
    """

    :tags:
    :categories:

    :param copyright:
    :param links:
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    now = datetime.datetime.now()
    copyright = self.page.py.encode_html(copyright or "© 2018 - %s, Epyk studio" % now.year)
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if links is not None:
      for link in links:
        if not isinstance(link, dict):
          link = {"text": link}
        url = self.page.ui.link(text=link['text'], url=link.get("url", '#'))
        url.style.css.color = self.page.theme.greys[6]
        url.style.css.margin = "0 5px"
        div.add(url)
    text = self.page.ui.text(copyright)
    text.style.css.color = self.page.theme.greys[-1]
    div.add(text)
    div.style.css.background_color = self.page.theme.greys[3]
    div.style.css.color = self.page.theme.greys[6]
    div.style.css.padding = "5px 0"
    div.style.css.left = 0
    div.style.css.margin_top = 40
    div.style.css.position = "absolute"
    html.Html.set_component_skin(div)
    return div

  def follow(self, text, width=(100, '%'), height=("auto", ''), align="left", options=None, profile=None,
             youtube=True, twitter=True, facebook=True, twitch=True, instagram=True, linkedIn=True):
    """

    :tags:
    :categories:

    :param text: String. Optional. The value to be displayed to the component.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param youtube: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param twitter: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param facebook: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param twitch: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param instagram: Boolean. Optional. Add the icon to the follow bar. Default True.
    :param linkedIn: Boolean. Optional. Add the icon to the follow bar. Default True.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.style.css.padding = "10px 0"
    text = self.page.ui.text(text)
    div.add(text)

    icon_size = int(self.page.body.style.globals.font.normal(8)[:-2])
    if youtube:
      div.youtube = self.page.ui.icons.youtube(width=(icon_size, 'px'))
      div.youtube.style.css.margin = "0 2px"
      div.add(div.youtube)

    if twitter:
      div.twitter = self.page.ui.icons.twitter(width=(icon_size, 'px'))
      div.twitter.style.css.margin = "0 2px"
      div.add(div.twitter)

    if facebook:
      div.facebook = self.page.ui.icons.facebook(width=(icon_size, 'px'))
      div.facebook.style.css.margin = "0 2px"
      div.add(div.facebook)

    if twitch:
      div.twitch = self.page.ui.icons.twitch(width=(icon_size, 'px'))
      div.twitch.style.css.margin = "0 2px"
      div.add(div.twitch)

    if instagram:
      div.instagram = self.page.ui.icons.instagram(width=(icon_size, 'px'))
      div.instagram.style.css.margin = "0 2px"
      div.add(div.instagram)

    if linkedIn:
      div.linkedIn = self.page.ui.icons.linkedIn(width=(icon_size, 'px'))
      div.linkedIn.style.css.margin = "0 2px"
      div.add(div.linkedIn)

    if width != (100, "%"):
      div.style.css.margin = "auto"
      div.style.css.display = "block"
    else:
      div.style.css.background_color = self.page.theme.greys[2]
    html.Html.set_component_skin(div)
    return div

  def row(self, headers, links, size_notch=0, background=None, width=(100, '%'), align="left", height=(None, 'px'),
          options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param headers:
    :param links:
    :param size_notch:
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    row = []
    for i, header in enumerate(headers):
      col = self.page.ui.col([self.page.ui.subtitle(header)], position='top')
      for link in links[i]:
        html_link = self.page.ui.link(link)
        html_link.style.css.display = 'block'
        html_link.style.css.margin = "5px 0"
        col.add(html_link)
      row.append(col)
    div.add(self.page.ui.row(row))
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    html.Html.set_component_skin(div)
    return div

  def contact_us(self, title="Contact Us", background=None, width=(100, '%'), align="left", height=(None, 'px'),
                 html_code="contactus", options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.style.css.padding = 5
    div.add(self.page.ui.title(title))
    row = self.page.ui.row([
      self.page.ui.input(
        placeholder="First Name", width=("calc(100% - 5px)", ""), html_code="%s_first_name" % html_code),
      self.page.ui.input(
        placeholder="Last Name", html_code="%s_last_name" % html_code)]).css({"padding-top": '5px', "margin": '5px',
                                                                              "width": "calc(100% - 10px)"})
    row.attr["class"].add("no-gutters")
    div.add(row)
    div.add(self.page.ui.input(placeholder="Email", html_code="%s_email" % html_code).css({
      "margin": '5px', "width": "calc(100% - 10px)"}))
    div.add(self.page.ui.input(placeholder="Subject", html_code="%s_subject" % html_code).css({
      "margin": '5px', "width": "calc(100% - 10px)"}))
    div.add(self.page.ui.textarea(placeholder="Leave us a message", html_code="%s_message" % html_code).css({
      "margin": '5px', "width": "calc(100% - 10px)"}))
    div.button = self.page.ui.button("Submit", align="center")
    div.add(div.button)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.margin_bottom = 10
    div._internal_components = ["%s_email" % html_code, "%s_first_name" % html_code, "%s_last_name" % html_code,
                                "%s_subject" % html_code, "%s_message" % html_code]
    html.Html.set_component_skin(div)
    return div

  def sponsor(self, logos, title="Sponsors", content='', background=None, width=(100, '%'), height=("auto", ''),
              align="center", options=None, profile=False):
    """

    :tags:
    :categories:

    Usage::

    :param logos:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param content:
    :param background: String. Optional. Background color code.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(title, 'options'):
      div.title = self.page.ui.titles.title(title)
      div.title.style.css.text_align = align
      div.title.style.css.font_weight = 800
      div.title.style.css.font_size = self.page.body.style.globals.font.normal(15)
    else:
      div.title = title
    div.add(div.title)
    if not hasattr(content, 'options'):
      content = self.page.ui.div(content, width=("auto", ""))
      content.style.css.text_align = align
      content.style.css.font_size = "inline-block"
    div.add(content)

    div_logos = self.page.ui.div("", align=align)
    div.logos = []
    for logo in logos:
      img = self.page.ui.img(
        "%s?raw=true" % logo, path="https://github.com/epykure/ressources/blob/master/logos", width=("auto", ''))
      div.logos.append(img)
      img.style.css.display = 'inline-block'
      img.style.css.cursor = 'pointer'
      img.style.css.filter = 'grayscale(100%)'
      img.style.hover({'filter': 'grayscale(0%)'})
      img.style.css.margin = '0 5px'
      div_logos.add(img)
    div.add(div_logos)
    div.style.css.background_color = background or self.page.theme.greys[0]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.color = self.page.theme.greys[-1]
    div.style.css.top = 0
    html.Html.set_component_skin(div)
    return div


class NavBars:

  def __init__(self, ui):
    self.page = ui.page

  def fixed(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bar = self.page.ui.navbar(logo=logo, title=title, width=width, height=height, options=options, profile=profile)
    html.Html.set_component_skin(bar)
    return bar

  def top(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bar = self.page.ui.navbar(logo=logo, title=title, width=width, height=height, options=options, profile=profile)
    bar.style.css.position = False
    html.Html.set_component_skin(bar)
    return bar

  def transparent(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bar = self.page.ui.navbar(logo=logo, title=title, width=width, height=height, options=options, profile=profile)
    bar.style.css.position = "absolute"
    bar.style.css.top = 0
    bar.no_background()
    html.Html.set_component_skin(bar)
    return bar

  def dark(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=None):
    """

    :tags:
    :categories:

    Usage::

    :param logo:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bar = self.page.ui.navbar(logo=logo, title=title, width=width, height=height, options=options, profile=profile)
    bar.style.css.position = "absolute"
    bar.style.css.top = 0
    bar.no_background()
    bar.style.css.opacity = 0.5
    bar.style.css.background = 'black'
    html.Html.set_component_skin(bar)
    return bar
