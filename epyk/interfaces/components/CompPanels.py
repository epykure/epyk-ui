#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Panels(object):

  def __init__(self, context):
    self.context = context

  def pills(self, color=None, width=(100, '%'), height=(None, 'px'), align="left", htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper to the Bootstrap Pills interface

    Usage::

      tab = rptObj.ui.panels.pills()
      for i in range(5):
        tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Tabs`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

		Attributes:
    ----------
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"css_tab": {'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0', 'border-radius': '5px',
                                'color': self.context.rptObj.theme.greys[-1]}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper, dflt_options, profile)
    html_tabs.options.css_tab_clicked = {'color': html_tabs._report.theme.greys[0], 'background': html_tabs._report.theme.colors[-1]}
    html_tabs.style.css.overflow_x = "auto"
    html_tabs.tabs_container.style.css.text_align = align
    html_tabs.style.css.white_space = "nowrap"
    return html_tabs

  def tabs(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component

    Usage::

      tab = rptObj.ui.panels.tabs()
      for i in range(5):
        tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Tabs`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

		Attributes:
    ----------
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 5px 0',
                                "border-bottom": "2px solid %s" % self.context.rptObj.theme.greys[0]}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper,
                                        dflt_options, profile)
    return html_tabs

  def arrows_up(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.TabsArrowsUp`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

		Attributes:
    ----------
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                                "border-bottom": "2px solid %s" % self.context.rptObj.theme.greys[0]}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.TabsArrowsUp(self.context.rptObj, color, width, height, htmlCode, helper, dflt_options, profile)
    for t in html_tabs.tabs():
      t.style.add_classes.layout.panel_arrow_up()
    html_tabs.options.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.options.css_tab["height"] = "30px"
    html_tabs.options.css_tab_clicked = {"background": html_tabs._report.theme.colors[-1], "color": self.context.rptObj.theme.greys[0]}
    return html_tabs

  def arrows_down(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.TabsArrowsDown`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

		Attributes:
    ----------
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {
      "css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 "border-bottom": "2px solid %s" % self.context.rptObj.theme.greys[0]}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.TabsArrowsDown(self.context.rptObj, color, width, height, htmlCode, helper, dflt_options, profile)
    for t in html_tabs.tabs():
      t.style.add_classes.layout.panel_arrow_down()
    html_tabs.options.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.options.css_tab["height"] = "30px"
    html_tabs.options.css_tab_clicked = {"background": html_tabs._report.theme.colors[-1], "color": self.context.rptObj.theme.greys[0]}
    return html_tabs

  def menu(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper to the Bootstrap Pills interface

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Tabs`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/navs/

		Attributes:
    ----------
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 'border-radius': '10px 10px 0 0'}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper, dflt_options, profile)
    html_tabs.options.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.options.css_tab["background"] = html_tabs._report.theme.greys[0]
    html_tabs.options.css_tab_clicked = {'color': html_tabs._report.theme.greys[0], 'background': html_tabs._report.theme.colors[-1]}
    html_tabs.tabs_container.css({"border-bottom": "2px solid %s" % html_tabs._report.theme.colors[-1]})
    return html_tabs

  def sliding(self, htmlObjs, title, color=None, align="center", width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.PanelSlide`

    Attributes:
    ----------
    :param htmlObjs:
    :param title:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if htmlObjs is not None and not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]
    components = []
    for component in htmlObjs:
      if not hasattr(component, 'options'):
        components.append(self.context.rptObj.ui.texts.paragraph(component, options={"markdown": True}))
      else:
        components.append(component)
    html_slide = html.HtmlContainer.PanelSlide(self.context.rptObj, components, title, color, width, height,
                                               htmlCode, helper, options or {}, profile)
    if align == "center":
      html_slide.style.css.margin = "auto"
      html_slide.style.css.display = "block"
    return html_slide

  def split(self, left=None, right=None, width=(100, '%'), height=(200, 'px'), left_width=(160, 'px'), resizable=True,
            helper=None, profile=None):
    """
    Description:
    ------------

    Usage::

      number = rptObj.ui.rich.number(500, "Test", height=(150, 'px'))
      number_2 = rptObj.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
      div = rptObj.ui.layouts.panelsplit(left=number, right=number_2)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.PanelSlide`

    Related Pages:

      https://codepen.io/rstrahl/pen/eJZQej

    Attributes:
    ----------
    :param width:
    :param height:
    :param left_width:
    :param left:
    :param right:
    :param resizable:
    :param helper:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_split = html.HtmlContainer.PanelSplit(self.context.rptObj, width, height, left_width, left, right, resizable, helper, profile)
    return html_split

  def filters(self, items=None, category='group', width=(100, "%"), height=(60, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    -----------
    Chip component wiht only the filtering eection.

    Usage::

      filters = rptObj.ui.panels.filters()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Filters`

    Related Pages:

      https://www.w3schools.com/howto/howto_css_contact_chips.asp

    Attributes:
    ----------
    :param items:
    :param category:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    chip = self.context.rptObj.ui.chips(items, category, width=width, height=height, htmlCode=htmlCode, helper=helper, options=options, profile=profile)
    chip.input.style.css.display = False
    return chip

  def nav(self, width=(100, '%'), height=(100, '%'), options=None, profile=None, helper=None):
    """
    Description:
    ------------

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/bars.py

    Attributes:
    ----------
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. A dictionary with the components properties
    :param profile: Optional. A flag to set the component performance storage
    :param helper:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"position": 'top'}
    if options is not None:
      dflt_options.update(options)
    h_drawer = html.HtmlMenu.PanelsBar(self.context.rptObj, width, height, dflt_options, helper, profile)
    return h_drawer

  @property
  def slidings(self):
    """
    Description:
    ------------
    More custom sliding panels
    """
    return Slidings(self.context)


class Slidings(object):

  def __init__(self, context):
    self.context = context

  def right(self, htmlObjs, title, color=None, align="center", width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Sliding panels with the arrown on the right

    Attributes:
    ----------
    :param htmlObjs:
    :param title:
    :param color:
    :param align:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    sliding = self.context.rptObj.ui.panels.sliding(htmlObjs, title=title, align="center", options={"icon_position": "right"})
    sliding.options.icon_closed = "fas fa-chevron-up"
    sliding.options.icon_expanded = "fas fa-chevron-down"
    sliding.style.css.width = "80%"
    sliding.style.css.border_bottom = "1px solid black"
    return sliding

  def left(self, htmlObjs, title, color=None, align="center", width=(100, "%"), height=(None, "px"), htmlCode=None,
            helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Sliding panels with the arrown on the left

    Attributes:
    ----------
    :param htmlObjs:
    :param title:
    :param color:
    :param align:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    sliding = self.context.rptObj.ui.panels.sliding(htmlObjs, title=title, align="center")
    sliding.options.icon_closed = "fas fa-chevron-up"
    sliding.options.icon_expanded = "fas fa-chevron-down"
    sliding.style.css.width = "80%"
    sliding.style.css.border_bottom = "1px solid black"
    return sliding

  def plus(self, components, title, color=None, align="center", width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Same component than sliding with a different style.

    Attributes:
    ----------
    :param components:
    :param title:
    :param color:
    :param align:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    html_slide = self.context.rptObj.ui.panels.sliding(components, title, color, align, width, height, htmlCode, helper, options, profile)
    html_slide.title.style.css.padding = 0
    html_slide.title[1].style.css.margin_left = 15
    html_slide.options.icon_closed = "fas fa-plus"
    html_slide.options.icon_expanded = "fas fa-minus"
    html_slide.val[1].style.padding_left = 40
    return html_slide
