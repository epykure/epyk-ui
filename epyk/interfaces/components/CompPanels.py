#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Union
from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.css import Defaults as Defaults_css


class Panels:

  def __init__(self, ui):
    self.page = ui.page

  def panel(self, components: List[html.Html.Html] = None, title=None, color=None, width=(100, "%"),
            height=(None, "px"), html_code: str = None, helper: str = None, options: dict = None,
            profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Add a simple div panel to the page.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Panel`

    Usage::


    Attributes:
    ----------
    :param components: List. Optional. The different HTML objects to be added to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      components = [components]
    html_panel = html.HtmlContainer.Panel(self.page, components or [], title, color, width, height, html_code,
                                          helper, options, profile)
    html.Html.set_component_skin(html_panel)
    return html_panel

  def pills(self, color: str = None, width=(100, '%'), height=(None, 'px'), align="left", html_code: str = None,
            helper: str = None, options: dict = None, profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Python wrapper to the Bootstrap Pills interface.

    :tags:
    :categories:

    Usage::

      tab = page.ui.panels.pills()
      for i in range(5):
        tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Tabs`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

    Attributes:
    ----------
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"css_tab": {'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                                'border-radius': '5px', 'color': self.page.theme.greys[-1]}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(
      self.page, color, width, height, html_code, helper, dflt_options, profile)
    html_tabs.options.css_tab_clicked = {
      'color': html_tabs.page.theme.greys[0],
      'background': html_tabs.page.theme.colors[-1]}
    html_tabs.style.css.overflow_x = "auto"
    html_tabs.tabs_container.style.css.text_align = align
    html_tabs.style.css.white_space = "nowrap"
    html.Html.set_component_skin(html_tabs)
    return html_tabs

  def boxes(self, color=None, width=(100, '%'), height=(None, 'px'), align: str = "left", html_code: str = None,
            helper: str = None, options: dict = None, profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Python wrapper to the Bootstrap rectangle boxes interface.

    :tags:
    :categories:

    Usage::

      tab = page.ui.panels.boxes()
      for i in range(5):
        tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Tabs`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

    Attributes:
    ----------
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"css_tab": {'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                                'color': self.page.theme.greys[-1]}}
    if options is not None:
      dfl_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(
      self.page, color, width, height, html_code, helper, dfl_options, profile)
    html_tabs.options.css_tab_clicked = {
      'color': html_tabs.page.theme.greys[0],
      'background': html_tabs.page.theme.colors[-1]}
    html_tabs.style.css.overflow_x = "auto"
    html_tabs.tabs_container.style.css.text_align = align
    html_tabs.tabs_container.style.css.border_bottom = "1px solid %s" % html_tabs.page.theme.colors[-1]
    html_tabs.style.css.white_space = "nowrap"
    html.Html.set_component_skin(html_tabs)
    return html_tabs

  def tabs(self, color=None, width=(100, '%'), height=(None, 'px'), html_code=None, helper=None, options=None,
           profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component.

    :tags:
    :categories:

    Usage::

      tab = page.ui.panels.tabs()
      for i in range(5):
        tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Tabs`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

    Attributes:
    ----------
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer',
                               'margin': '0 2px 5px 0', "border-bottom": "2px solid %s" % self.page.theme.greys[0]}}
    if options is not None:
      dfl_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(
      self.page, color, width, height, html_code, helper, dfl_options, profile)
    html.Html.set_component_skin(html_tabs)
    return html_tabs

  def arrows_up(self, color=None, width=(100, '%'), height=(None, 'px'), html_code=None, helper=None, options=None,
                profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.TabsArrowsUp`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

    Usage::

    Attributes:
    ----------
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer',
                               'margin': '0 2px 0 0', "border-bottom": "2px solid %s" % self.page.theme.greys[0]}}
    if options is not None:
      dfl_options.update(options)
    html_tabs = html.HtmlContainer.TabsArrowsUp(
      self.page, color, width, height, html_code, helper, dfl_options, profile)
    for t in html_tabs.tabs():
      t.style.add_classes.layout.panel_arrow_up()
    html_tabs.options.css_tab["color"] = html_tabs.page.theme.greys[-1]
    html_tabs.options.css_tab["height"] = "30px"
    html_tabs.options.css_tab_clicked = {
      "background": html_tabs.page.theme.colors[-1], "color": self.page.theme.greys[0]}
    html.Html.set_component_skin(html_tabs)
    return html_tabs

  def arrows_down(self, color=None, width=(100, '%'), height=(None, 'px'), html_code=None, helper=None, options=None,
                  profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.TabsArrowsDown`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

    Usage::

    Attributes:
    ----------
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {
      "css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                  "border-bottom": "2px solid %s" % self.page.theme.greys[0]}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.TabsArrowsDown(
      self.page, color, width, height, html_code, helper, dflt_options, profile)
    for t in html_tabs.tabs():
      t.style.add_classes.layout.panel_arrow_down()
    html_tabs.options.css_tab["color"] = html_tabs.page.theme.greys[-1]
    html_tabs.options.css_tab["height"] = "30px"
    html_tabs.options.css_tab_clicked = {
      "background": html_tabs.page.theme.colors[-1], "color": self.page.theme.greys[0]}
    html.Html.set_component_skin(html_tabs)
    return html_tabs

  def menu(self, color=None, width=(100, '%'), height=(None, 'px'), html_code=None, helper=None, options=None,
           profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Python wrapper to the Bootstrap Pills interface.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Tabs`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

    Usage::

    Attributes:
    ----------
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer',
                                'margin': '0 2px 0 0', 'border-radius': '10px 10px 0 0'}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(
      self.page, color, width, height, html_code, helper, dflt_options, profile)
    html_tabs.options.css_tab["color"] = html_tabs.page.theme.greys[-1]
    html_tabs.options.css_tab["background"] = html_tabs.page.theme.greys[0]
    html_tabs.options.css_tab_clicked = {
      'color': html_tabs.page.theme.greys[0], 'background': html_tabs.page.theme.colors[-1]}
    html_tabs.tabs_container.css({"border-bottom": "2px solid %s" % html_tabs.page.theme.colors[-1]})
    html.Html.set_component_skin(html_tabs)
    return html_tabs

  def sliding(self, components, title, color=None, align="center", width=(100, "%"), height=(None, "px"),
              html_code=None, helper=None, options=None, profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Add a sliding panel.

    TODO: Animate the CSS to make a transition.

    :tags:
    :categories:

    Usage::

      text = page.ui.text("Test")
      page.ui.panels.sliding([text], title="Panel title")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.PanelSlide`

    Attributes:
    ----------
    :param components: List. Optional. The different HTML objects to be added to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param align: String. Optional. The text-align property within this component (Default center).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      _components = [components]
    else:
      _components = components
    components = []
    for component in _components:
      if not hasattr(component, 'options'):
        components.append(self.page.ui.texts.paragraph(component, options={"markdown": True}))
      else:
        components.append(component)
    html_slide = html.HtmlContainer.PanelSlide(
      self.page, components, title, color, width, height, html_code, helper, options or {}, profile)
    if align == "center":
      html_slide.style.css.margin = "auto"
      html_slide.style.css.display = "block"
    html.Html.set_component_skin(html_slide)
    return html_slide

  def split(self, left=None, right=None, width=(100, '%'), height=(200, 'px'), left_width=(160, 'px'), resizable=True,
            helper=None, options=None, profile: Union[dict, bool] = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      number = page.ui.rich.number(500, "Test", height=(150, 'px'))
      number_2 = page.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
      div = page.ui.layouts.panelsplit(left=number, right=number_2)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.PanelSlide`

    Related Pages:

      https://codepen.io/rstrahl/pen/eJZQej

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param left_width:
    :param left:
    :param right:
    :param resizable:
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_split = html.HtmlContainer.PanelSplit(self.page, width, height, left_width, left, right, resizable,
                                               helper, options, profile)
    html.Html.set_component_skin(html_split)
    return html_split

  def filters(self, items=None, category='group', width=(100, "%"), height=(60, "px"), html_code=None, helper=None,
              options=None, profile: Union[dict, bool] = None):
    """
    Description:
    -----------
    Chip component with only the filtering section.

    :tags:
    :categories:

    Usage::

      filters = page.ui.panels.filters()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Filters`

    Related Pages:

      https://www.w3schools.com/howto/howto_css_contact_chips.asp

    Attributes:
    ----------
    :param items:
    :param category:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"item_css": {'border': '1px solid %s' % self.page.theme.success.light,
                                'border-radius': '5px', "padding": "0 4px",
                                "margin-left": "5px", "width": 'auto', 'display': 'inline-block',
                                'background': options.get("colored", 'inherit'), 'white-space': 'nowrap'}}
    if options:
      dfl_options.update(options)
    chip = self.page.ui.chips(
      items, category, width=width, height=height, html_code=html_code, helper=helper, options=dfl_options,
      profile=profile)
    chip.input.style.css.display = False
    html.Html.set_component_skin(chip)
    return chip

  def nav(self, width=(100, '%'), height=(100, '%'), options=None, profile: Union[dict, bool] = None, helper=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/bars.py

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. A dictionary with the components properties.
    :param profile: Optional. A flag to set the component performance storage.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"position": 'top'}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlMenu.PanelsBar(self.page, width, height, dflt_options, helper, profile)
    html.Html.set_component_skin(h_drawer)
    return h_drawer

  def hamburger(self, components: List[html.Html.Html] = None, title: Union[str, dict] = "", color: str = None,
                align: str = "center", width=(100, "%"), height=(None, "px"),
                html_code: str = None, helper: str = None, options: dict = None, profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Add hamburger panel.

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.PanelSlide`

    Attributes:
    ----------
    :param components: List. Optional. The different HTML objects to be added to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param align: String. Optional. The text-align property within this component (Default center).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      _components = [components]
    else:
      _components = components or []
    components = []
    for component in _components:
      if not hasattr(component, 'options'):
        components.append(self.page.ui.texts.paragraph(component, options={"markdown": True}))
      else:
        components.append(component)
    dfl_options = {"icon_expanded": "", "expanded": False, "icon_closed": "", "click_type": 'icon'}
    if options is not None:
      dfl_options.update(options)
    html_slide = html.HtmlContainer.PanelSlide(
      self.page, components, title, color, width, height, html_code, helper, dfl_options, profile)
    html_slide.icon = self.page.ui.icons.hamburger()
    html_slide.icon.options.managed = False
    html_slide.icon.style.css.float = "right"
    html_slide.icon.style.css.margin_top = 3
    #html_slide.icon.style.css.margin_right = 2
    html_slide.style.css.border = "1px solid %s" % self.page.theme.greys[2]
    html_slide._vals[1].style.css.padding = 5
    html_slide.title.add(html_slide.icon)
    html_slide.style.css.margin_top = 5
    html_slide.style.css.margin_bottom = 5
    if align == "center":
      html_slide.style.css.margin = "5px auto"
      html_slide.style.css.display = "block"
    html.Html.set_component_skin(html_slide)
    return html_slide

  @property
  def slidings(self):
    """
    Description:
    ------------
    More custom sliding panels.
    """
    return Slidings(self)


class Slidings:

  def __init__(self, ui):
    self.page = ui.page

  def right(self, components, title, color=None, align="center", width=(100, "%"), height=(None, "px"), html_code=None,
            helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Sliding panels with the arrow on the right.

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dfl_options = {"icon_position": "right"}
    if options is not None:
      dfl_options.update(options)
    sliding = self.page.ui.panels.sliding(
      components, color=color, title=title, align=align, width=width, height=height,
      html_code=html_code, helper=helper, options=dfl_options, profile=profile)
    sliding.options.icon_closed = Defaults_css.get_icon("chevron_up")["icon"]
    sliding.options.icon_expanded = Defaults_css.get_icon("chevron_down")["icon"]
    sliding.style.css.width = "80%"
    sliding.style.css.border_bottom = "1px solid black"
    html.Html.set_component_skin(sliding)
    return sliding

  def left(self, components, title="", color=None, align="center", width=(100, "%"), height=(None, "px"), html_code=None,
           helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Sliding panels with the arrow on the left.

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    sliding = self.page.ui.panels.sliding(components, color=color, title=title, align=align, width=width, height=height,
                                          html_code=html_code, helper=helper, options=options, profile=profile)
    sliding.options.icon_closed = Defaults_css.get_icon("chevron_up")["icon"]
    sliding.options.icon_expanded = Defaults_css.get_icon("chevron_down")["icon"]
    sliding.style.css.width = "80%"
    sliding.style.css.border_bottom = "1px solid black"
    html.Html.set_component_skin(sliding)
    return sliding

  def plus(self, components, title="", color=None, align="center", width=(100, "%"), height=(None, "px"), html_code=None,
           helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Same component than sliding with a different style.

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_slide = self.page.ui.panels.sliding(
      components, title, color, align, width, height, html_code, helper, options, profile)
    html_slide.title.style.css.padding = 0
    html_slide.title[1].style.css.margin_left = 15
    html_slide.options.icon_closed = Defaults_css.get_icon("plus")["icon"]
    html_slide.options.icon_expanded = Defaults_css.get_icon("minus")["icon"]
    html_slide.val[1].style.padding_left = 40
    html.Html.set_component_skin(html_slide)
    return html_slide
