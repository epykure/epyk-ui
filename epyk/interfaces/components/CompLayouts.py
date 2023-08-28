#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, List
from epyk.core.py import types

from epyk.core import html
from epyk.interfaces import Arguments


class Layouts:

  def __init__(self, ui):
    self.page = ui.page

  def br(self, count: int = 1, profile: types.PROFILE_TYPE = None) -> html.HtmlOthers.Newline:
    """
    Wrapper around the Br html tag.

    The <br> tag inserts a single line break.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.new_line(10)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Newline`

    Related Pages:

      https://www.w3schools.com/tags/tag_br.asp

    :param count: Integer. Optional. The number of empty line to put. Default 1.
    :param profile: Boolean | Dictionary. Optional. Activate the profiler.
    """
    html_new_line = html.HtmlOthers.Newline(self.page, count, profile=profile)
    html.Html.set_component_skin(html_new_line)
    return html_new_line

  def new_line(self, count: int = 1, profile: types.PROFILE_TYPE = None) -> html.HtmlOthers.Newline:
    """
    Wrapper around the Br html tag.

    The <br> tag inserts a single line break.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.new_line(10)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Newline`

    Related Pages:

      https://www.w3schools.com/tags/tag_br.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    :param count: Integer. Optional. The number of empty line to put. Default 1.
    :param profile: Boolean | Dictionary. Optional. Activate the profiler.
    """
    html_new_line = self.br(count, profile)
    html.Html.set_component_skin(html_new_line)
    return html_new_line

  def hr(self, count: int = 1, background_color: str = None, margins: int = 0,
         width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, 'px'),
         align: str = None, options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """
    Wrapper around the HT html tag.

    The <hr> tag defines a thematic break in an HTML page (e.g. a shift of topic).

    Tips: If background_color is True, the theme color will be used.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.hr(10)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Hr`

    Related Pages:

      https://www.w3schools.com/tags/tag_hr.asp

    Templates:

    :param count: Optional. The number of HR tag to be added.
    :param background_color: Optional. The component background color.
    :param margins: Optional. The margin top and bottom in pixels.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align:  Optional. The content position. Values (left, right, center). Default center.
    :param options: Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    hr_html = self.page.ui.div(width=Arguments.size(width))
    if background_color is True:
      background_color = self.page.theme.notch()
    for _ in range(count):
      hr_html.hr = html.HtmlOthers.Hr(
        self.page, background_color, (100, '%'), Arguments.size(height), align, options, profile)
      hr_html += hr_html.hr
    if align == 'center':
      hr_html.style.css.margin = "auto"
      hr_html.style.css.display = "block"
    hr_html.margin = hr_html.hr.margin
    if margins > 0:
      hr_html.style.css.margin_top = margins
      hr_html.style.css.margin_bottom = margins
    html.Html.set_component_skin(hr_html)
    return hr_html

  def underline(self, width: types.SIZE_TYPE = (10, '%'), height: types.SIZE_TYPE = (3, 'px'),
                align: str = None, options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """
    Add a styles hr component to underline another component.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.underline()

    Templates:


    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align: Optional. The content position. Values (left, right, center). Default center.
    :param options: Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    hr = self.hr(
      1, self.page.theme.colors[-1], 0, width=width, height=height, align=align, options=options, profile=profile)
    hr.style.css.margin_top = -5
    hr.style.css.border_radius = 10
    hr.style.css.margin_bottom = 10
    html.Html.set_component_skin(hr)
    return hr

  def accentuate(self, width: types.SIZE_TYPE = (10, '%'), height: types.SIZE_TYPE = (1, 'px'), align: str = None,
                 options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """
    Add a styles hr component to lightly underline another component.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.accentuate()

    Templates:

    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align: Optional. The content position. Values (left, right, center). Default center.
    :param options: Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    hr = self.hr(
      1, self.page.theme.colors[6], 0, width=width, height=height, align=align, options=options, profile=profile)
    hr.style.css.margin_top = -5
    hr.style.css.border_radius = 10
    hr.style.css.margin_bottom = 10
    html.Html.set_component_skin(hr)
    return hr

  def col(self, components: List[html.Html.Html] = None, position: str = 'middle',
          width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, 'px'), align: str = None,
          helper: str = None, options: dict = None,
          profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Col:
    """
    Python wrapper for a column of HTML elements from Bootstrap.

    This component is a container and it is used to display multiple Ares components in column.
    You can first add a component in the data list then add the + operator to add more.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.col([
        page.ui.text("test C"),
        page.ui.text("test D"),
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Col`

    Related Pages:

      https://getbootstrap.com/docs/4.0/layout/grid/
      https://www.alsacreations.com/tuto/lire/1493-css3-flexbox-layout-module.html

    Templates:


    :param components: The different HTML objects to be added to the component.
    :param position: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align: Optional. A string with the horizontal position of the component.
    :param helper: Optional. A tooltip helper.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    html_col = html.HtmlContainer.Col(self.page, components, position, width, height, align, helper, options, profile)
    html.Html.set_component_skin(html_col)
    return html_col

  def row(self, components: List[html.Html.Html] = None, position: str = 'middle', width: types.SIZE_TYPE = (100, '%'),
          height: types.SIZE_TYPE = (None, 'px'), align: str = None, helper: str = None,
          options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Row:
    """
    Python wrapper for a column of HTML elements from Bootstrap.

    This component is a container and it is used to display multiple Ares components in column.
    You can first add a component in the data list then add the + operator to add more.

    :tags:
    :categories:

    Usage::

      row = page.ui.layouts.row()
      row += page.ui.layouts.col([
        page.ui.text("test A"),
        page.ui.text("test B"),
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Row`

    Templates:

    Related Pages:

      https://getbootstrap.com/docs/4.0/layout/grid/
      https://www.alsacreations.com/tuto/lire/1493-css3-flexbox-layout-module.html

    :param components: The different HTML objects to be added to the component.
    :param position: Optional. The CSS justify-content attribute
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align: Optional. A string with the horizontal position of the component.
    :param helper: Optional. A tooltip helper.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_option = {"autoSize": True}
    if options is not None:
      dft_option.update(options)
    html_col = html.HtmlContainer.Row(
      self.page, components, position, width, height, align, helper, dft_option, profile)
    html.Html.set_component_skin(html_col)
    return html_col

  def table(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (None, 'px'), helper: str = None, options: dict = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Table:
    """
    table layout for HTML components.

    :tags:
    :categories:

    Usage::

      row = page.ui.layouts.table()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Table`

    Templates:


    :param components: The different HTML objects to be added to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param helper:  Optional. A tooltip helper.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_row = html.HtmlContainer.Table(self.page, components, width, height, helper, options, profile)
    html.Html.set_component_skin(html_row)
    return html_row

  def grid(self, rows=None, width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, 'px'),
           align: str = None, position: str = None, options: dict = None,
           profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Grid:
    """
    Python wrapper to the HTML Bootstrap Grid.

    :tags:
    :categories:

    Usage::

      gr = page.ui.layouts.grid()
      gr += [page.ui.text("test %s" % i) for i in range(5)]

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Grid`

    Related Pages:

      https://getbootstrap.com/docs/4.0/layout/grid/

    Templates:

    :param rows:
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align: Optional. A string with the horizontal position of the component.
    :param position: Optional. A string with the vertical position of the component.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_grid = html.HtmlContainer.Grid(self.page, rows, width, height, align, position, options, profile)
    html.Html.set_component_skin(html_grid)
    return html_grid

  def panel(self, components: List[html.Html.Html] = None, title: str = None, color: str = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
            helper: str = None, options: dict = None,
            profile: types.PROFILE_TYPE = False) -> html.HtmlContainer.Panel:
    """

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Panel`

    :tags:
    :categories:

    Usage::

    Templates:


    :param components: The different HTML objects to be added to the component.
    :param title:
    :param color: Optional. The font color in the component. Default inherit.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional. A tooltip helper.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      components = [components]
    html_panel = html.HtmlContainer.Panel(
      self.page, components or [], title, color, width, height, html_code, helper, options, profile)
    html.Html.set_component_skin(html_panel)
    return html_panel

  def div(self, components: Union[html.Html.Html, List[html.Html.Html]] = None, label: str = None, color: str = None,
          width: types.SIZE_TYPE = (100, "%"), icon: str = None, height: types.SIZE_TYPE = (None, "px"),
          editable: bool = False, align: str = 'left', padding: int = None, html_code: str = None, tag: str = 'div',
          helper: str = None, options: dict = None, profile: types.PROFILE_TYPE = None,
          position: Union[bool, dict] = None) -> html.HtmlContainer.Div:
    """
    Add a simple div container to the page.
    The <div> tag defines a division or a section in an HTML document.

    The <div> tag is used as a container for HTML elements - which is then styled with CSS or manipulated with
    JavaScript.

    :tags:
    :categories:

    Usage::

      div = page.ui.div([html])
      div += html_2

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/bars.py

    :param components: The different HTML objects to be added to the component
    :param label: Optional.
    :param color: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param icon: Optional.
    :param position: Optional.
    :param editable: Optional.
    :param align: Optional. A string with the horizontal position of the component
    :param padding: Optional.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tag: Optional. The HTML tag (Default div)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      components = [components]

    dfl_options = {"position": position}
    if options is not None:
      dfl_options.update(options)
    html_div = html.HtmlContainer.Div(self.page, components or [], label, color, width, icon, height,
                                      editable, align, padding, html_code, tag, helper, dfl_options, profile)
    if width[0] == 'auto' or width[1] == 'px':
      html_div.style.css.display = "inline-block"
    html.Html.set_component_skin(html_div)
    return html_div

  def inline(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (None, "%"),
             height: types.SIZE_TYPE = (None, "px"), align: str = 'left', html_code: str = None,
             options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """

    :tags:
    :categories:

    Usage::

    Templates:

    :param components: The different HTML objects to be added to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    html_comp = self.div(
      components=components, width=width, height=height, align=align, html_code=html_code, options=options,
      profile=profile)
    html_comp.style.css.display = "inline-block"
    html.Html.set_component_skin(html_comp)
    return html_comp

  def centered(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = ("auto", ""),
               height: types.SIZE_TYPE = (None, "px"), align: str = 'left', html_code: str = None,
               options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """

    :tags:
    :categories:

    Usage::

    Templates:

    :param components: The different HTML objects to be added to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    html_comp = self.div(components=components, width=width, height=height, align=align, options=options,
                         html_code=html_code, profile=profile)
    self.div(html_comp, align="center")
    html.Html.set_component_skin(html_comp)
    return html_comp

  def popup(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (None, 'px'),
            options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlPopup.Popup:
    """
    Add a generic popup component to the page.

    :tags:
    :categories:

    Usage::

      popup = page.ui.layouts.popup(page.ui.title('Test'), color="red")
      popup.add(page.ui.texts.paragraph('Test'))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

    :param components: The different HTML objects to be added to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {'margin': 10, 'closure': "fas fa-times-circle", 'top': 100}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile)
    html.Html.set_component_skin(component)
    return component

  def iframe(self, url: str = "", width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (100, "%"),
             helper: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.IFrame:
    """
    Add a iframe component to the page.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.iframe("http://www.google.com")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.IFrame`

    Templates:

    :param url: Optional. The link to the underlying page.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param helper: Optional. A tooltip helper.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    component = html.HtmlContainer.IFrame(self.page, url, width, height, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def dialogs(self, text: str = "", width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (20, 'px'),
              html_code: str = None, helper: str = None,
              options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlEvent.Dialog:
    """
    Simple Jquery UI modal with a text.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Dialog`

    Related Pages:

      https://jqueryui.com/dialog/

    Usage::


    :param text: Optional. The value to be displayed to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional. A tooltip helper.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlEvent.Dialog(self.page, text, width, height, helper, options or {}, html_code, profile)
    html.Html.set_component_skin(component)
    return component

  def icons(self, icon_names=None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"),
            html_code: str = None, helper: str = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.IconsMenu:
    """

    :tags:
    :categories:

    Usage::

      menu = page.ui.layouts.icons(["fas fa-bell", "fas fa-calendar-check"])
      menu.icon.click([menu.icon.dom.css({"color": 'red'})])
      menu[0].click([menu[0].dom.css({"color": 'red'})])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.IconsMenu`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/icons.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    :param icon_names:
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional. A tooltip helper.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    icon_names = icon_names or None
    if not isinstance(icon_names, list):
      icon_names = [icon_names]
    component = html.HtmlContainer.IconsMenu(icon_names, self.page, width, height, html_code, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def form(self, components: List[html.Html.Html] = None, helper: str = None) -> html.HtmlContainer.Form:
    """

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`

    Templates:

    :param components: The different HTML objects to be added to the component.
    :param helper: Optional. A tooltip helper.
    """
    component = html.HtmlContainer.Form(self.page, components, helper)
    html.Html.set_component_skin(component)
    return component

  def header(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (None, "px"), html_code: str = None, helper: str = None,
             options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Header:
    """
    The HTML <header> element represents introductory content, typically a group of introductory or navigational aids.
    It may contain some heading elements but also a logo, a search form, an author name, and other elements.

    :tags:
    :categories:

    Usage::

      div = page.ui.header([html])
      div += html_2

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Header`

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header

    Templates:

    :param components: The different HTML objects to be added to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper:
    :param options: Optional. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      components = [components]
    component = html.HtmlContainer.Header(
      self.page, components or [], width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def section(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, "%"),
              height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
              helper: str = None, options: dict = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Section:
    """
    The <section> tag defines sections in a document, such as chapters, headers, footers, or any other sections
    of the document.

    :tags:
    :categories:

    Usage::

      div = page.ui.header([html])
      div += html_2

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Header`

    Related Pages:

      https://www.w3schools.com/tags/tag_section.asp

    Templates:

    :param components: The different HTML objects to be added to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional. A tooltip helper.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      components = [components]
    component = html.HtmlContainer.Section(
      self.page, components or [], width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def columns(self, components: List[html.Html.Html], cols, width: types.SIZE_TYPE = (100, '%'),
              height: types.SIZE_TYPE = (None, 'px'), align: str = None, position: str = None,
              options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Grid:
    """

    :tags:
    :categories:

    Usage::

    Templates:

    :param components: List. The different HTML objects to be added to the component.
    :param cols:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param position: String. Optional. A string with the vertical position of the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    rows, row = [], []
    dflt_options = {"responsive": False}
    if options:
      dflt_options.update(options)
    for i, c in enumerate(components):
      if not i % cols and len(row):
        rows.append(row)
        row = []
      row.append(c)
    if len(row):
      rows.append(row)
    component = self.grid(
      rows, width=width, height=height, align=align, position=position, options=dflt_options, profile=profile)
    html.Html.set_component_skin(component)
    return component


class Delimiter:

  def __init__(self, ui):
    self.page = ui.page

  def line(self, count: int = 1, width: types.SIZE_TYPE = (100, '%'), align: str = None, options: dict = None,
           profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """
    Wrapper around the HT html tag.

    :tags:
    :categories:

    Usage::

    Templates:

    :param count: Optional. The number of HR tag to be added.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param align: Optional. The content position. Values (left, right, center). Default center.
    :param options: Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    hrs = self.page.ui.layouts.hr(count, width=width, align=align, options=options, profile=profile)
    hrs.style.css.margin = "10px 0"
    html.Html.set_component_skin(hrs)
    return hrs

  def double(self, count: int = 1, width: types.SIZE_TYPE = (100, '%'), align: str = "center", options: dict = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """
    Wrapper around the HT html tag.

    :tags:
    :categories:

    Usage::

    Templates:

    :param count: Optional. The number of HR tag to be added.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param align: Optional. The content position. Values (left, right, center). Default center.
    :param options: Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    hrs = self.page.ui.layouts.hr(count, width=width, align=align, options=options, profile=profile)
    for hr in hrs:
      hr.style.css.border = "1px double %s" % self.page.theme.colors[-1]
    html.Html.set_component_skin(hrs)
    return hrs

  def dashed(self, count: int = 1, width: types.SIZE_TYPE = (100, '%'), align: str = "center", options: dict = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """
    Wrapper around the HT html tag.

    :tags:
    :categories:

    Usage::

    Templates:

    :param count: Optional. The number of HR tag to be added.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param align: Optional. The content position. Values (left, right, center). Default center.
    :param options: Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    hrs = self.page.ui.layouts.hr(count, width=width, align=align, options=options, profile=profile)
    hrs.style.css.margin_top = 10
    hrs.style.css.margin_bottom = 10
    for hr in hrs:
      hr.style.css.border = "1px dashed %s" % self.page.theme.colors[-1]
    html.Html.set_component_skin(hrs)
    return hrs

  def dotted(self, count: int = 1, width: types.SIZE_TYPE = (100, '%'), align: str = "center", options: dict = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """
    Wrapper around the HT html tag.

    :tags:
    :categories:

    Usage::

    Templates:

    :param count: Optional. The number of HR tag to be added.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param align: Optional. The content position. Values (left, right, center). Default center.
    :param options: Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    hrs = self.page.ui.layouts.hr(count, width=width, align=align, options=options, profile=profile)
    for hr in hrs:
      hr.style.css.border = "1px dotted %s" % self.page.theme.colors[-1]
    html.Html.set_component_skin(hrs)
    return hrs
