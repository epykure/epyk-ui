#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Layouts:

  def __init__(self, ui):
    self.page = ui.page

  def br(self, count=1, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param count: Integer. Optional. The number of empty line to put. Default 1.
    :param profile: Boolean | Dictionary. Optional. Activate the profiler.
    """
    html_new_line = html.HtmlOthers.Newline(self.page, count, profile=profile)
    return html_new_line

  def new_line(self, count=1, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param count: Integer. Optional. The number of empty line to put. Default 1.
    :param profile: Boolean | Dictionary. Optional. Activate the profiler.
    """
    return self.br(count, profile)

  @html.Html.css_skin()
  def hr(self, count=1, background_color=None, margins=0, width=(100, '%'), height=(None, 'px'), align=None,
         options=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param count: Integer. Optional. The number of HR tag to be added.
    :param background_color: String. Optional. The component background color.
    :param margins: Integer. Optional. The margin top and bottom in pixels.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The content position. Values (left, right, center). Default center.
    :param options: Dictionary. Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
    return hr_html

  @html.Html.css_skin()
  def underline(self, width=(10, '%'), height=(3, 'px'), align=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a styles hr component to underline another component.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.underline()

    Templates:


    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The content position. Values (left, right, center). Default center.
    :param options: Dictionary. Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    hr = self.hr(
      1, self.page.theme.colors[-1], 0, width=width, height=height, align=align, options=options, profile=profile)
    hr.style.css.margin_top = -5
    hr.style.css.border_radius = 10
    hr.style.css.margin_bottom = 10
    return hr

  @html.Html.css_skin()
  def accentuate(self, width=(10, '%'), height=(1, 'px'), align=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a styles hr component to lightly underline another component.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.accentuate()

    Templates:

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The content position. Values (left, right, center). Default center.
    :param options: Dictionary. Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    hr = self.hr(
      1, self.page.theme.colors[6], 0, width=width, height=height, align=align, options=options, profile=profile)
    hr.style.css.margin_top = -5
    hr.style.css.border_radius = 10
    hr.style.css.margin_bottom = 10
    return hr

  @html.Html.css_skin()
  def col(self, components=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None,
          options=None, profile=None):
    """
    Description:
    ------------
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


    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param position: String. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    html_col = html.HtmlContainer.Col(self.page, components, position, width, height, align, helper, options, profile)
    return html_col

  @html.Html.css_skin()
  def row(self, components=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None,
          options=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param position: String. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_option = {"autoSize": True}
    if options is not None:
      dft_option.update(options)
    html_col = html.HtmlContainer.Row(
      self.page, components, position, width, height, align, helper, dft_option, profile)
    return html_col

  @html.Html.css_skin()
  def table(self, components=None, width=(100, '%'), height=(None, 'px'), helper=None, options=None, profile=None):
    """
    Description:
    ------------
    table layout for HTML components.

    :tags:
    :categories:

    Usage::

      row = page.ui.layouts.table()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Table`

    Templates:


    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_row = html.HtmlContainer.Table(self.page, components, width, height, helper, options, profile)
    return html_row

  @html.Html.css_skin()
  def grid(self, rows=None, width=(100, '%'), height=(None, 'px'), align=None, position=None, options=None,
           profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param rows:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param position: String. Optional. A string with the vertical position of the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_grid = html.HtmlContainer.Grid(self.page, rows, width, height, align, position, options, profile)
    return html_grid

  @html.Html.css_skin()
  def panel(self, components=None, title=None, color=None, width=(100, "%"), height=(None, "px"), html_code=None,
            helper=None, options=None, profile=False):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Panel`

    :tags:
    :categories:

    Usage::

    Templates:


    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param title:
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      components = [components]
    html_panel = html.HtmlContainer.Panel(
      self.page, components or [], title, color, width, height, html_code, helper, options, profile)
    return html_panel

  @html.Html.css_skin()
  def div(self, components=None, label=None, color=None, width=(100, "%"), icon=None,
          height=(None, "px"), editable=False, align='left', padding=None, html_code=None, tag='div', helper=None,
          options=None, profile=None, position=None):
    """
    Description:
    ------------

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

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param label:
    :param color:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param icon:
    :param position: String. Optional.
    :param editable:
    :param align: String. Optional. A string with the horizontal position of the component
    :param padding:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param tag:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param helper: String. Optional.
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
    return html_div

  @html.Html.css_skin()
  def inline(self, components=None, width=(None, "%"), height=(None, "px"), align='left', html_code=None, options=None,
             profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param align: String. Optional. A string with the horizontal position of the component
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    html_comp = self.div(
      components=components, width=width, height=height, align=align, html_code=html_code, options=options,
      profile=profile)
    html_comp.style.css.display = "inline-block"
    return html_comp

  @html.Html.css_skin()
  def centered(self, components=None, width=("auto", ""), height=(None, "px"), align='left', html_code=None,
               options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param align: String. Optional. A string with the horizontal position of the component
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    html_comp = self.div(components=components, width=width, height=height, align=align, options=options,
                         html_code=html_code, profile=profile)
    self.div(html_comp, align="center")
    return html_comp

  @html.Html.css_skin()
  def popup(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {'margin': 10, 'closure': "fas fa-times-circle", 'top': 100}
    if options is not None:
      dfl_options.update(options)
    return html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile)

  @html.Html.css_skin()
  def iframe(self, url="", width=(100, "%"), height=(100, "%"), helper=None, profile=None):
    """
    Description:
    ------------
    Add a iframe component to the page.

    :tags:
    :categories:

    Usage::

      page.ui.layouts.iframe("http://www.google.com")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.IFrame`

    Templates:

    Attributes:
    ----------
    :param url: String. Optional. The link to the underlying page.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    html_frame = html.HtmlContainer.IFrame(self.page, url, width, height, helper, profile)
    return html_frame

  @html.Html.css_skin()
  def dialogs(self, text="", width=(100, '%'), height=(20, 'px'), html_code=None, helper=None, options=None,
              profile=None):
    """
    Description:
    ------------
    Simple Jquery UI modal with a text.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Dialog`

    Related Pages:

      https://jqueryui.com/dialog/

    Usage::


    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_pr = html.HtmlEvent.Dialog(self.page, text, width, height, helper, options or {}, html_code, profile)
    return html_pr

  @html.Html.css_skin()
  def icons(self, icon_names=None, width=(100, "%"), height=(None, "px"), html_code=None, helper=None, profile=None):
    """
    Description:
    ------------

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

    Attributes:
    ----------
    :param icon_names:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    icon_names = icon_names or None
    if not isinstance(icon_names, list):
      icon_names = [icon_names]
    html_icon = html.HtmlContainer.IconsMenu(icon_names, self.page, width, height, html_code, helper, profile)
    return html_icon

  @html.Html.css_skin()
  def form(self, components=None, helper=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`

    Templates:

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param helper: String. Optional. A tooltip helper.
    """
    form = html.HtmlContainer.Form(self.page, components, helper)
    return form

  @html.Html.css_skin()
  def header(self, components=None, width=(100, "%"),  height=(None, "px"), html_code=None, helper=None, options=None,
             profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper:
    :param options: Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      components = [components]
    html_obj = html.HtmlContainer.Header(self.page, components or [], width, height, html_code, helper,
                                         options or {}, profile)
    return html_obj

  @html.Html.css_skin()
  def section(self, components=None, width=(100, "%"), height=(None, "px"), html_code=None, helper=None, options=None,
              profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if components is not None and not isinstance(components, list):
      components = [components]
    html_obj = html.HtmlContainer.Section(self.page, components or [], width, height, html_code, helper,
                                          options or {}, profile)
    return html_obj

  @html.Html.css_skin()
  def columns(self, components, cols, width=(100, '%'), height=(None, 'px'), align=None, position=None, options=None,
              profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
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
    g = self.grid(
      rows, width=width, height=height, align=align, position=position, options=dflt_options, profile=profile)
    return g


class Delimiter:

  def __init__(self, ui):
    self.page = ui.page

  def line(self, count=1, width=(100, '%'), align=None, options=None, profile=None):
    """
    Description:
    ------------
    Wrapper around the HT html tag.

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param count: Integer. Optional. The number of HR tag to be added.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: Tuple. Optional. The content position. Values (left, right, center). Default center.
    :param options: Dictionary. Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    hrs = self.page.ui.layouts.hr(count, width=width, align=align, options=options, profile=profile)
    hrs.style.css.margin = "10px 0"
    return hrs

  def double(self, count=1, width=(100, '%'), align="center", options=None, profile=None):
    """
    Description:
    ------------
    Wrapper around the HT html tag.

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param count: Integer. Optional. The number of HR tag to be added.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: Tuple. Optional. The content position. Values (left, right, center). Default center.
    :param options: Dictionary. Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    hrs = self.page.ui.layouts.hr(count, width=width, align=align, options=options, profile=profile)
    for hr in hrs:
      hr.style.css.border = "1px double %s" % self.page.theme.colors[-1]
    return hrs

  def dashed(self, count=1, width=(100, '%'), align="center", options=None, profile=None):
    """
    Description:
    ------------
    Wrapper around the HT html tag.

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param count: Integer. Optional. The number of HR tag to be added.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: Tuple. Optional. The content position. Values (left, right, center). Default center.
    :param options: Dictionary. Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    hrs = self.page.ui.layouts.hr(count, width=width, align=align, options=options, profile=profile)
    hrs.style.css.margin_top = 10
    hrs.style.css.margin_bottom = 10
    for hr in hrs:
      hr.style.css.border = "1px dashed %s" % self.page.theme.colors[-1]
    return hrs

  def dotted(self, count=1, width=(100, '%'), align="center", options=None, profile=None):
    """
    Description:
    ------------
    Wrapper around the HT html tag.

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param count: Integer. Optional. The number of HR tag to be added.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: Tuple. Optional. The content position. Values (left, right, center). Default center.
    :param options: Dictionary. Optional. Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    hrs = self.page.ui.layouts.hr(count, width=width, align=align, options=options, profile=profile)
    for hr in hrs:
      hr.style.css.border = "1px dotted %s" % self.page.theme.colors[-1]
    return hrs
