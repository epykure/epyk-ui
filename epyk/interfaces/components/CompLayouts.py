
from epyk.core import html


class Layouts(object):
  def __init__(self, context):
    self.context = context

  def new_line(self, count=1, profile=None):
    """
    Description:
    ------------
    Wrapper around the Br html tag.

    The <br> tag inserts a single line break.

    Usage:
    ------
    rptObj.ui.layouts.new_line(10)

    Related Pages:
    --------------
    https://www.w3schools.com/tags/tag_br.asp

    Attributes:
    ----------
    :param count: Optional, The number of empty line to put. Default 1
    :param profile: Optional, Activate the profiler
    """
    html_new_line = html.HtmlOthers.Newline(self.context.rptObj, count, profile=profile)
    self.context.register(html_new_line)
    return html_new_line

  def hr(self, count=1, color=None, background_color=None, height=(None, 'px'), align=None, profile=None):
    """
    Description:
    ------------
    Wrapper around the HT html tag.

    The <hr> tag defines a thematic break in an HTML page (e.g. a shift of topic).

    Usage:
    ------
    rptObj.ui.layouts.hr(10)

    Related Pages:
    --------------
    https://www.w3schools.com/tags/tag_hr.asp

    Attributes:
    ----------
    :param count: The number of HR tag to be added
    :param color: Optional. The color code for the font
    :param background_color: Optional. The component background color
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. The content position. Values (left, right, center). Default center
    :param profile: Optional. A flag to set the component performance storage
    """
    hr_html = self.context.rptObj.ui.div()
    for _ in range(count):
      hr_item = html.HtmlOthers.Hr(self.context.rptObj, background_color, height, align, profile)
      self.context.register(hr_item)
      hr_html += hr_item
    return hr_html

  def col(self, htmlObjs=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None, profile=None):
    """
    Description:
    ------------
    Python wrapper for a column of HTML elements from Bootstrap

    This component is a container and it is used to display multiple Ares components in column.
    You can first add a component in the data list then add the + operator to add more.

    Usage:
    ------
    rptObj.ui.layouts.col([
      rptObj.ui.text("test C"),
      rptObj.ui.text("test D"),
    ])

    Related Pages:
    --------------
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
    html_col = html.HtmlContainer.Col(self.context.rptObj, htmlObjs, position, width, height, align, helper, profile)
    self.context.register(html_col)
    return html_col

  def row(self, htmlObjs=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None, profile=None):
    """
    Description:
    ------------
    Python wrapper for a column of HTML elements from Bootstrap

    This component is a container and it is used to display multiple Ares components in column.
    You can first add a component in the data list then add the + operator to add more.

    Usage:
    ------
    row = rptObj.ui.layouts.row()
    row += rptObj.ui.layouts.col([
      rptObj.ui.text("test A"),
      rptObj.ui.text("test B"),
    ])

    Related Pages:
    --------------
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
    html_col = html.HtmlContainer.Row(self.context.rptObj, htmlObjs, position, width, height, align, helper, profile)
    self.context.register(html_col)
    return html_col

  def table(self, htmlObjs=None, width=(100, '%'), height=(None, 'px'), align='left', helper=None, options=None, profile=None):
    """
    Description:
    ------------
    table layout for HTML components

    Attributes:
    ----------
    :param htmlObjs:
    :param width:
    :param height:
    :param align:
    :param helper:
    :param options:
    :param profile:
    """
    html_row = html.HtmlContainer.Table(self.context.rptObj, htmlObjs, width, height, align, helper, options, profile)
    self.context.register(html_row)
    return html_row

  def grid(self, rows=None, width=(100, '%'), height=(None, 'px'), align=None, helper=None, profile=None):
    """
    Description:
    ------------
    Python wrapper to the HTML Bootstrap Grid

    Usage:
    ------
    gr = rptObj.ui.layouts.grid()
    gr += [rptObj.ui.text("test %s" % i) for i in range(5)]

    Related Pages:
    --------------
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
    html_grid = html.HtmlContainer.Grid(self.context.rptObj, rows, width, height, align, helper, profile)
    self.context.register(html_grid)
    return html_grid

  def panel(self, htmlObjs=None, title=None, color=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
            helper=None, options=None, profile=False):
    """

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
    self.context.register(html_panel)
    return html_panel

  def div(self, htmlObjs=None, label=None, color=None, width=(100, "%"), icon=None, height=(None, "px"), editable=False,
          align='left', padding=None, htmlCode=None, tag='div', helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    div = rptObj.ui.div([html])
    div += html_2

    Related Pages:
    --------------
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
                                      editable, align, padding, htmlCode, tag, helper, profile)
    self.context.register(html_div)
    return html_div

  def popup(self, htmlObj=None, title=None, color=None, width=(100, '%'), height=(None, 'px'),
            withBackground=True, draggable=False, margin=10, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    popup = report.popup(report.title('Test'), color="red")
    popup + report.paragraph('Test')

    Related Pages:
    --------------
    https://www.w3schools.com/tags/tag_div.asp

    Attributes:
    ----------
    :param htmlObj:
    :param title:
    :param color:
    :param width:
    :param height:
    :param withBackground:
    :param draggable:
    :param margin:
    :param profile:
    :rtype: html.HtmlPopup.Popup
    :return:
    """
    return self.context.register(html.HtmlPopup.Popup(self.context.rptObj, htmlObj, title, color, width, height,
                                                      withBackground, draggable, margin, profile))

  def iframe(self, url, width=(100, "%"), height=(100, "%"), helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.layouts.iframe("http://www.google.com")

    Attributes:
    ----------
    :param url:
    :param width:
    :param height:
    :param helper:
    :param profile:
    """
    html_frame = html.HtmlContainer.IFrame(self.context.rptObj, url, width, height, helper, profile)
    self.context.register(html_frame)
    return html_frame

  def dialogs(self, record=None, width=(100, "%"), height=(200, "px"), helper=None, profile=None):

    html_dialog = html.HtmlContainer.Dialog(self.context.rptObj, record, width, height, helper, profile)
    self.context.register(html_dialog)
    return html_dialog

  def icons(self, icon_names=None, width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    menu = rptObj.ui.layouts.icons(["fas fa-bell", "fas fa-calendar-check"])
    menu.icon.click([menu.icon.dom.css({"color": 'red'})])
    menu[0].click([menu[0].dom.css({"color": 'red'})])

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
    self.context.register(html_icon)
    return html_icon

  def multiFilter(self, items=None, title=None, width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None,
                  profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param items:
    :param title:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:

    :rtype: html.HtmlEvent.Filters
    :return:
    """
    items = items or []
    return self.context.register(html.HtmlEvent.Filters(self.context.rptObj, items, title, width, height, htmlCode, helper, profile))

  def form(self, htmlObj=None, helper=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param htmlObj:
    :param helper:
    :return:
    """
    form = html.HtmlContainer.Form(self.context.rptObj, htmlObj, helper)
    self.context.register(form)
    return form
