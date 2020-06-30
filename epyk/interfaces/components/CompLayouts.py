
from epyk.core import html


class Layouts(object):
  def __init__(self, context):
    self.context = context

  def br(self, count=1, profile=None):
    """
    Description:
    ------------
    Wrapper around the Br html tag.

    The <br> tag inserts a single line break.

    Usage::

      rptObj.ui.layouts.new_line(10)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Newline`

    Related Pages:

      https://www.w3schools.com/tags/tag_br.asp

    Attributes:
    ----------
    :param count: Optional, The number of empty line to put. Default 1
    :param profile: Optional, Activate the profiler
    """
    html_new_line = html.HtmlOthers.Newline(self.context.rptObj, count, profile=profile)
    return html_new_line

  def new_line(self, count=1, profile=None):
    """
    Description:
    ------------
    Wrapper around the Br html tag.

    The <br> tag inserts a single line break.

    Usage::

      rptObj.ui.layouts.new_line(10)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Newline`

    Related Pages:

      https://www.w3schools.com/tags/tag_br.asp

    Attributes:
    ----------
    :param count: Optional, The number of empty line to put. Default 1
    :param profile: Optional, Activate the profiler
    """
    return self.br(count, profile)

  def hr(self, count=1, background_color=None, height=(None, 'px'), align=None, profile=None):
    """
    Description:
    ------------
    Wrapper around the HT html tag.

    The <hr> tag defines a thematic break in an HTML page (e.g. a shift of topic).

    Usage::

      rptObj.ui.layouts.hr(10)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Hr`

    Related Pages:

      https://www.w3schools.com/tags/tag_hr.asp

    Attributes:
    ----------
    :param count: The number of HR tag to be added
    :param background_color: Optional. The component background color
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. The content position. Values (left, right, center). Default center
    :param profile: Optional. A flag to set the component performance storage
    """
    hr_html = self.context.rptObj.ui.div()
    for _ in range(count):
      hr_item = html.HtmlOthers.Hr(self.context.rptObj, background_color, height, align, profile)
      hr_html += hr_item
    return hr_html

  def col(self, htmlObjs=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Python wrapper for a column of HTML elements from Bootstrap

    This component is a container and it is used to display multiple Ares components in column.
    You can first add a component in the data list then add the + operator to add more.

    Usage::

      rptObj.ui.layouts.col([
      rptObj.ui.text("test C"),
      rptObj.ui.text("test D"),
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Col`

    Related Pages:

      https://getbootstrap.com/docs/4.0/layout/grid/
    https://www.alsacreations.com/tuto/lire/1493-css3-flexbox-layout-module.html

    Attributes:
    ----------
    :param htmlObjs:
    :param position:
    :param width:
    :param height:
    :param align:
    :param helper:
    :param options:
    :param profile:
    """
    html_col = html.HtmlContainer.Col(self.context.rptObj, htmlObjs, position, width, height, align, helper, options or {}, profile)
    return html_col

  def row(self, htmlObjs=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Python wrapper for a column of HTML elements from Bootstrap

    This component is a container and it is used to display multiple Ares components in column.
    You can first add a component in the data list then add the + operator to add more.

    Usage::

      row = rptObj.ui.layouts.row()
      row += rptObj.ui.layouts.col([
      rptObj.ui.text("test A"),
      rptObj.ui.text("test B"),
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Row`

    Related Pages:

      https://getbootstrap.com/docs/4.0/layout/grid/
    https://www.alsacreations.com/tuto/lire/1493-css3-flexbox-layout-module.html

    Attributes:
    ----------
    :param htmlObjs:
    :param position:
    :param width:
    :param height:
    :param align:
    :param helper:
    :param profile:
    """
    dft_option = {"autoSize": True}
    if options is not None:
      dft_option.update(options)
    html_col = html.HtmlContainer.Row(self.context.rptObj, htmlObjs, position, width, height, align, helper, dft_option, profile)
    return html_col

  def table(self, htmlObjs=None, width=(100, '%'), height=(None, 'px'), helper=None, options=None, profile=None):
    """
    Description:
    ------------
    table layout for HTML components

    Usage::

      row = rptObj.ui.layouts.table()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Table`

    Attributes:
    ----------
    :param htmlObjs:
    :param width:
    :param height:
    :param helper:
    :param options:
    :param profile:
    """
    html_row = html.HtmlContainer.Table(self.context.rptObj, htmlObjs, width, height, helper, options, profile)
    return html_row

  def grid(self, rows=None, width=(100, '%'), height=(None, 'px'), align=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Python wrapper to the HTML Bootstrap Grid

    Usage::

      gr = rptObj.ui.layouts.grid()
      gr += [rptObj.ui.text("test %s" % i) for i in range(5)]

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Grid`

    Related Pages:

      https://getbootstrap.com/docs/4.0/layout/grid/

    Attributes:
    ----------
    :param rows:
    :param width:
    :param height:
    :param align:
    :param helper:
    :param profile:
    """
    html_grid = html.HtmlContainer.Grid(self.context.rptObj, rows, width, height, align, helper, options, profile)
    return html_grid

  def panel(self, htmlObjs=None, title=None, color=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
            helper=None, options=None, profile=False):
    """

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Panel`

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
    if htmlObjs is not None and not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]
    html_panel = html.HtmlContainer.Panel(self.context.rptObj, htmlObjs or [], title, color, width, height, htmlCode, helper, options, profile)
    return html_panel

  def div(self, htmlObjs=None, label=None, color=None, width=(100, "%"), icon=None, height=(None, "px"), editable=False,
          align='left', padding=None, htmlCode=None, tag='div', helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      div = rptObj.ui.div([html])
      div += html_2

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Attributes:
    ----------
    :param htmlObjs:
    :param label:
    :param color:
    :param width:
    :param icon:
    :param height:
    :param editable:
    :param align:
    :param padding:
    :param htmlCode:
    :param tag:
    :param profile:
    """
    if htmlObjs is not None and not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]

    html_div = html.HtmlContainer.Div(self.context.rptObj, htmlObjs or [], label, color, width, icon, height,
                                      editable, align, padding, htmlCode, tag, helper, options or {}, profile)
    if width[0] == 'auto':
      html_div.style.css.display = "inline-block"
    return html_div

  def popup(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      popup = report.popup(report.title('Test'), color="red")
      popup + report.paragraph('Test')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Attributes:
    ----------
    :param components:
    :param width:
    :param height:
    :param options:
    :param profile:

    :rtype: html.HtmlPopup.Popup
    """
    dfl_options = {"background": True, 'draggable': False, 'margin': 10}
    if options is not None:
      dfl_options.update(options)
    if not dfl_options["background"] and width[0] == 100:
      width = (None, '%')
    return html.HtmlPopup.Popup(self.context.rptObj, components, width, height, dfl_options, profile)

  def iframe(self, url, width=(100, "%"), height=(100, "%"), helper=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.layouts.iframe("http://www.google.com")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.IFrame`

    Attributes:
    ----------
    :param url:
    :param width:
    :param height:
    :param helper:
    :param profile:
    """
    html_frame = html.HtmlContainer.IFrame(self.context.rptObj, url, width, height, helper, profile)
    return html_frame

  def dialogs(self, record=None, width=(100, "%"), height=(200, "px"), helper=None, profile=None):
    """

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Dialog`

    :param record:
    :param width:
    :param height:
    :param helper:
    :param profile:
    """
    html_dialog = html.HtmlContainer.Dialog(self.context.rptObj, record, width, height, helper, profile)
    return html_dialog

  def icons(self, icon_names=None, width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------

    Usage::

      menu = rptObj.ui.layouts.icons(["fas fa-bell", "fas fa-calendar-check"])
      menu.icon.click([menu.icon.dom.css({"color": 'red'})])
      menu[0].click([menu[0].dom.css({"color": 'red'})])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.IconsMenu`

    Attributes:
    ----------
    :param icon_names:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:
    """
    icon_names = icon_names or None
    if not isinstance(icon_names, list):
      icon_names = [icon_names]
    html_icon = html.HtmlContainer.IconsMenu(icon_names, self.context.rptObj, width, height, htmlCode, helper, profile)
    return html_icon

  def form(self, htmlObj=None, helper=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`

    Attributes:
    ----------
    :param htmlObj:
    :param helper:
    """
    form = html.HtmlContainer.Form(self.context.rptObj, htmlObj, helper)
    return form

  def header(self, htmlObjs=None, width=(100, "%"),  height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
      """
      Description:
      ------------
      The HTML <header> element represents introductory content, typically a group of introductory or navigational aids.
      It may contain some heading elements but also a logo, a search form, an author name, and other elements

      Usage::

        div = rptObj.ui.header([html])
        div += html_2

      Underlying HTML Objects:

        - :class:`epyk.core.html.HtmlContainer.Header`

      Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header

      Attributes:
      ----------
      :param htmlObjs:
      :param width:
      :param height:
      :param htmlCode:
      :param profile:
      """
      if htmlObjs is not None and not isinstance(htmlObjs, list):
        htmlObjs = [htmlObjs]
      html_obj = html.HtmlContainer.Header(self.context.rptObj, htmlObjs or [], width, height, htmlCode, helper, options or {}, profile)
      return html_obj

  def section(self, htmlObjs=None, width=(100, "%"),  height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
      """
      Description:
      ------------
      The <section> tag defines sections in a document, such as chapters, headers, footers, or any other sections of the document.

      Usage::

        div = rptObj.ui.header([html])
        div += html_2

      Underlying HTML Objects:

        - :class:`epyk.core.html.HtmlContainer.Header`

      Related Pages:

      https://www.w3schools.com/tags/tag_section.asp

      Attributes:
      ----------
      :param htmlObjs:
      :param width:
      :param height:
      :param htmlCode:
      :param tag:
      :param profile:
      """
      if htmlObjs is not None and not isinstance(htmlObjs, list):
        htmlObjs = [htmlObjs]
      html_obj = html.HtmlContainer.Section(self.context.rptObj, htmlObjs or [], width, height, htmlCode, helper, options or {}, profile)
      return html_obj
