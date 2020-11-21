#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces import Arguments

from epyk.core.html import Html
from epyk.core.html import Defaults
from epyk.core.html.options import OptPanel
from epyk.core.html.options import OptText
#
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi
from epyk.core.js.html import JsHtml
from epyk.core.js.html import JsHtmlPanels

# The list of CSS classes#
from epyk.core.css import Defaults as css_defaults
from epyk.core.css.styles import GrpClsContainer


class Panel(Html.Html):
  name = 'Panel'

  def __init__(self, report, htmlObj, title, color, width, height, htmlCode, helper, options, profile):
    if isinstance(htmlObj, list) and htmlObj:
      for obj in htmlObj:
        if hasattr(obj, 'options'):
          obj.options.managed = False
    elif htmlObj is not None and hasattr(htmlObj, 'options'):
      htmlObj.options.managed = False # Has to be defined here otherwise it is set to late
    component, self.menu = [], None
    if title is not None:
      self.title = report.ui.title(title)
      self.title.options.managed = False
      component.append(self.title)
    container = report.ui.div(htmlObj)
    container.options.managed = False
    component.append(container)
    self.add_helper(helper)
    super(Panel, self).__init__(report, component, htmlCode=htmlCode, profile=profile,
                                css_attrs={"color": color, "width": width, "height": height})
    container.set_attrs(name="name", value="panel_%s" % self.htmlCode)

  @property
  def style(self):
    """
    Description:
    ------------

    :rtype: GrpClsContainer.ClassDiv
    """
    if self._styleObj is None:
      self._styleObj = GrpClsContainer.ClassDiv(self)
    return self._styleObj

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlPanels.JsHtmlPanel
    """
    if self._dom is None:
      self._dom = JsHtmlPanels.JsHtmlPanel(self, report=self._report)
    return self._dom

  def extend(self, components):
    """
    Description:
    ------------
    Add multiple HTML components to the container.

    Attributes:
    ----------
    :param components: List. The list of components
    """
    for component in components:
      self.add(component)
    return self

  def add_menu(self, close=True, mini=True, info=None, pin=False):
    self.style.css.position = "relative"
    self.style.css.min_height = 25
    self.style.css.min_width = 25
    if self.menu is None:
      self.menu = self._report.ui.div()
      self.menu.options.managed = False
      self.menu.style.css.position = "absolute"
      self.menu.style.css.text_align = "right"
      self.menu.style.css.top = 2
      self.menu.style.css.right = 5
      self.menu.style.css.margin = 0
    margin_right = 5
    if pin:
      pin_comp = self._report.ui.icon("fas fa-thumbtack")
      pin_comp.style.css.margin_right = 10
      pin_comp.tooltip(info)
      pin_comp.style.css.color = self._report.theme.greys[6]
      self.menu.add(pin_comp)
    if info is not None:
      info_comp = self._report.ui.icon("fas fa-question")
      info_comp.style.css.margin_right = 10
      info_comp.style.css.font_factor(-5)
      info_comp.tooltip(info)
      info_comp.click([
        self.dom.querySelector("div[name=panel]").toggle()])
      info_comp.style.css.color = self._report.theme.greys[6]
      self.menu.add(info_comp)
    if mini:
      remove = self._report.ui.icon("far fa-minus-square")
      remove.style.css.margin_right = 10
      remove.click([
        self.dom.querySelector("div[name=panel]").toggle()])
      remove.style.css.color = self._report.theme.greys[6]
      self.menu.add(remove)
    if close:
      remove = self._report.ui.icon("fas fa-times")
      remove.style.css.margin_right = 10
      remove.click([self.dom.remove()])
      remove.style.css.color = self._report.theme.greys[6]
      self.menu.add(remove)
    return self.menu

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    if self.menu is None:
      return "<div %s>%s</div>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_div, self.helper)

    menu_width = "100%"
    if self.style.css.width.endswith('px'):
      menu_width = self.style.css.width
      self.style.css.width = None
    return "<div %s>%s<div style='width:%s' name='panel'>%s</div></div>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.menu.html(), menu_width, str_div, self.helper)


class PanelSplit(Html.Html):
  #requirements = ('jqueryui', )
  name = 'Panel Split'

  def __init__(self, report, width, height, left_width, left_obj, right_obj, resizable, helper, profile):
    super(PanelSplit, self).__init__(report, None, css_attrs={"width": width, "height": height, 'white-space': 'nowrap'}, profile=profile)
    self.left_width, self.resizable = left_width, resizable
    if left_obj is not None:
      self.left(left_obj)
    if right_obj is not None:
      self.right(right_obj)
    self.css_left = {'flex': '0 0 auto', 'overflow': 'auto', 'padding': '5px', 'min-width': '100px', 'width': "%s%s" % (self.left_width[0], self.left_width[1]),
                     'white-space': 'nowrap'}
    self.css_right = {'flex': '0 1 auto', 'overflow': 'auto', 'padding': '5px', 'width': '100%', 'background': self._report.theme.greys[0],
                      'border-left': '3px solid %s' % self._report.theme.success[1]}
    self.css({'display': 'flex', 'flex-direction': 'row', 'overflow': 'hidden', 'xtouch-action': 'none'})

  def left(self, html_obj):
    """
    Description:
    ------------
    Add the left component to the panel

    Attributes:
    ----------
    :param html_obj:
    """
    html_obj.options.managed = False
    self.html_left = html_obj
    return self

  def right(self, html_obj):
    """
    Description:
    ------------
    Add the right component to the panel

    Attributes:
    ----------
    :param html_obj:
    """
    html_obj.options.managed = False
    self.html_right = html_obj
    return self

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).extend([
      '$("#%(htmlCode)s_left").resizable({handleSelector: ".splitter", resizeHeight: false});' % {'htmlCode': self.htmlCode},
      '$("#%(htmlCode)s_right").resizable({handleSelector: ".splitter-horizontal", resizeWidth: true})' % {
        'htmlCode': self.htmlCode}])
    return '''
      <div %(attrs)s>
        <div style="%(css_left)s" id="%(htmlCode)s_left" class="panel-left">%(left)s</div>
        <div style="%(css_right)s" id="%(htmlCode)s_right" class="panel-right">%(right)s</div>
      </div>
      ''' % {"attrs": self.get_attrs(pyClassNames=self.style.get_classes()), "htmlCode": self.htmlCode, 'left': self.html_left.html(),
             'right': self.html_right.html(), 'css_left': css_defaults.inline(self.css_left), 'css_right': css_defaults.inline(self.css_right)}


class PanelSlide(Panel):
  requirements = ('font-awesome', )
  name = 'Slide Panel'

  def __init__(self, report, components, title, color, width, height, htmlCode, helper, options, profile):
    super(PanelSlide, self).__init__(report, components, None, color, width, height, htmlCode, helper, options, profile)
    self.add_helper(helper)
    self.icon = self._report.ui.icon("").css({"display": 'inline-block', 'margin': '0 5px 5px 0',
                                              'line-height': "%spx" % Defaults.LINE_HEIGHT, 'font-size': "%spx" % Defaults.BIG_ICONS})
    self.text = self._report.ui.text(title, htmlCode="%s_title" % self.htmlCode).css({"display": 'inline-block', 'margin': 0})
    self.text.style.css.bold()
    self.text.style.css.font_factor(2)
    self.title = self._report.ui.div([self.icon, self.text])
    self.title.options.managed = False
    self.title.style.css.cursor = "pointer"
    self.title.style.css.white_space = "nowrap"
    self.title.style.css.padding = "5px 5px 0 0"
    self.panel = self._report.ui.div()
    self.panel.options.managed = False
    self._vals, self.__clicks, self.__clicks_open = [self.title] + self._vals, [], []
    self.__options = OptPanel.OptionPanelSliding(self, options)

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptPanel.OptionPanelSliding
    """
    return self.__options

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlPanels.JsHtmlSlidingPanel
    """
    if self._dom is None:
      self._dom = JsHtmlPanels.JsHtmlSlidingPanel(self, report=self._report)
    return self._dom

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------
    Event added to the title bar.
    This will be triggered first

    Attributes:
    ----------
    :param jsFncs: String or List. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__clicks = jsFncs
    return self

  def open(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------
    Event triggered when the sliding panel is open.

    Attributes:
    ----------
    :param jsFncs: String or List. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__clicks_open = [self._report.js.if_(self.icon.dom.content.toString().indexOf(self.options.icon_expanded.split(" ")[-1]) >= 0, jsFncs).toStr()]
    return self

  def __add__(self, component):
    """ Add items to a container """
    self.val[1] += component
    return self

  def __str__(self):
    if self.options.expanded:
      icon_change = self.options.icon_closed
      icon_current = self.options.icon_expanded
      self.icon.set_icon(self.options.icon_expanded)
    else:
      icon_change = self.options.icon_expanded
      icon_current = self.options.icon_closed
      self._vals[1].style.css.display = 'none'
      self.icon.set_icon(self.options.icon_closed)
    if self.options.icon_position == "right":
      self.icon.style.css.float = "right"
    self.title.click(self.__clicks + [
      self._report.js.getElementsByName("panel_%s" % self.htmlCode).first.toggle(),
      self.icon.dom.switchClass(icon_current, icon_change)] + self.__clicks_open)
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    return "<div %s>%s</div>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_div, self.helper)


class Div(Html.Html):
  name = 'Simple Container'

  def __init__(self, report, htmlObj, label, color, width, icon, height, editable, align, padding, htmlCode, tag,
               helper, options, profile):
    super(Div, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"color": color, "width": width, "height": height}, profile=profile)
    self.__options = OptPanel.OptionsDiv(self, options)
    if not isinstance(htmlObj, list):
      htmlObj = [htmlObj]
    for obj in htmlObj:
      if isinstance(obj, list) and obj:
        component = report.ui.div(obj, label, color, width, icon, height, editable, align, padding, htmlCode, tag, helper, profile)
      else:
        component = obj

      if hasattr(component, 'options'):
        self.__add__(component)
      else:
        self.val.append(obj)
    self.tag = tag
    # Add the component predefined elements
    self.add_icon(icon, htmlCode=self.htmlCode, family=options.get("icon_family"))
    self.add_label(label, htmlCode=self.htmlCode)
    self.add_helper(helper)

    self.css({'text-align': align})
    if padding is not None:
      self.css('padding', '%s' % padding)
    if editable:
      self.set_attrs(name='contenteditable', value="true")
      self.css('overflow', 'auto')

  def goto(self, url, jsFncs=None, profile=False, name="_blank", source_event=None):
    """
    Description:
    -----------
    Click event which redirect to another page.

    Attributes:
    ----------
    :param jsFncs: List. The Javascript Events triggered before the redirection
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param name: String. Optional.
    :param source_event: String. Optional. The event source.
    """
    self.style.css.cursor = "pointer"
    jsFncs = jsFncs or []
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    jsFncs.append(self.js.location.open_new_tab(url, name))
    return self.click(jsFncs, profile, source_event)

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, report=self._report)
    return self._dom

  def __add__(self, htmlObj):
    """ Add items to a container """
    if isinstance(htmlObj, list):
      htmlObj = self._report.ui.row(htmlObj)
    htmlObj.options.managed = False # Has to be defined here otherwise it is set to late
    if self.options.inline:
      htmlObj.style.css.display = 'inline-block'
      htmlObj.style.css.font_weight = 900
    if not isinstance(self.val, list):
      self._vals = [self.val]
    self.val.append(htmlObj)
    self.components[htmlObj.htmlCode] = htmlObj
    return self

  def extend(self, components):
    """
    Description:
    ------------
    Add multiple HTML components to the container.

    Attributes:
    ----------
    :param components: List. The list of components
    """
    for component in components:
      self.add(component)
    return self

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    :rtype: OptPanel.OptionsDiv
    """
    return self.__options

  @property
  def style(self):
    """

    :rtype: GrpClsContainer.ClassDiv
    """
    if self._styleObj is None:
      self._styleObj = GrpClsContainer.ClassDiv(self)
    return self._styleObj

  def build(self, data=None, options=None, profile=False):
    if isinstance(data, dict):
      # check if there is no nested HTML components in the data
      js_data = "{%s}" % ",".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in data.items()])
    else:
      js_data = JsUtils.jsConvertData(data, None)
    options, js_options = options or {}, []
    for k, v in options.items():
      if isinstance(v, dict):
        row = ["%s: %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
        js_options.append("%s: {%s}" % (k, ", ".join(row)))
      else:
        js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
    return "%s.innerHTML = %s" % (self.dom.varId, js_data) #, "{%s}" % ",".join(js_options))

  def __str__(self):
    rows = []
    for htmlObj in self.val:
      if hasattr(htmlObj, 'html'):
        if self._sort_propagate:
          htmlObj.sortable(self._sort_options)
        rows.append(htmlObj.html())
      else:
        rows.append(str(htmlObj))

    return "<div %s>%s</div>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(rows), self.helper)


class Td(Html.Html):
  name = 'Cell'

  def __init__(self, report, htmlObjs, header, position, width, height, align, options, profile):
    self.position, self.rows_css, self.row_css_dflt, self.header = position, {}, {}, header
    super(Td, self).__init__(report, [], css_attrs={"width": width, "height": height, 'white-space': 'nowrap'}, profile=profile)
    self.__options = options
    self.attr["align"] = options.cell_align or align
    if htmlObjs is not None:
      for htmlObj in htmlObjs:
        self.__add__(htmlObj)

  def colspan(self, i):
    """
    Description:
    ------------
    The colspan attribute defines the number of columns a cell should span.

    Related Pages:

      https://www.w3schools.com/tags/att_td_colspan.asp

    Attributes:
    ----------
    :param i:
    """
    self.attr['colspan'] = i
    return self

  def rowspan(self, i):
    """
    Description:
    ------------
    The rowspan attribute specifies the number of rows a cell should span.

    Related Pages:

      https://www.w3schools.com/tags/att_td_rowspan.asp

    Attributes:
    ----------
    :param i:
    """
    self.attr['rowspan'] = i
    return self

  def __str__(self):
    content = [htmlObj.html() if hasattr(htmlObj, 'options') else str(htmlObj) for htmlObj in self.val]
    if self.header:
      return '<th %s>%s</th>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(content))

    return '<td %s>%s</td>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(content))


class Tr(Html.Html):
  name = 'Column'

  def __init__(self, report, htmlObjs, header, position, width, height, align, options, profile):
    self.position, self.header = position, header
    super(Tr, self).__init__(report, [], css_attrs={"width": width, "height": height, 'text-align': align}, profile=profile)
    self.__options = options
    if htmlObjs is not None:
      for htmlObj in htmlObjs:
        self.__add__(htmlObj)
    self.style.justify_content = self.position

  def __add__(self, htmlObj):
    """ Add items to a container """
    if not isinstance(htmlObj, Td):
      if not isinstance(htmlObj, list):
        htmlObj = [htmlObj]
      htmlObj = Td(self._report, htmlObj, self.header, None, (None, "%"), (None, "%"), 'center', self.__options, False)
    super(Tr, self).__add__(htmlObj)
    return self

  @property
  def dom(self):
    """
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlPanels.JsHtmlTr
    """
    if self._dom is None:
      self._dom = JsHtmlPanels.JsHtmlTr(self, report=self._report)
    return self._dom

  def __str__(self):
    cols = [htmlObj.html() for i, htmlObj in enumerate(self.val)]
    return '<tr %s>%s</tr>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(cols))


class Caption(Html.Html):
  name = 'Table Caption'

  def __init__(self, report, text, color, align, width, height, htmlCode, tooltip, options, profile):
    super(Caption, self).__init__(report, text, css_attrs={"width": width, "height": height, "color": color, 'text-align': align},
                                  htmlCode=htmlCode, profile=profile)
    self.__options = OptText.OptionsText(self, options)
    if tooltip is not None:
      self.tooltip(tooltip)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    :rtype: OptText.OptionsText
    """
    return self.__options

  def __str__(self):
    val = self._report.py.markdown.all(self.val) if self.options.showdown else self.val
    return '<caption %s>%s</caption>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val)


class TSection(Html.Html):
  name = 'Table Section'

  def __init__(self, report, type, rows=None, options=None, profile=None):
    super(TSection, self).__init__(report, [])
    self.__section = type
    self.__options = OptPanel.OptionPanelTable(self, options)
    if rows is not None:
      for row in rows:
        self.__add__(row)

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptPanel.OptionPanelTable
    """
    return self.__options

  def __add__(self, row_data):
    """ Add items to a container """
    if not isinstance(row_data, Tr):
      row_data = Tr(self._report, row_data, self.__section == 'thead', None, (100, "%"), (100, "%"), 'center', self.options, False)

    super(TSection, self).__add__(row_data)
    return self

  def __str__(self):
    cols = []
    for htmlObj in self.val:
      if self._sort_propagate:
        htmlObj.sortable(self._sort_options)
      cols.append(htmlObj.html())
    return '<%(section)s %(attr)s>%(cols)s</%(section)s>' % {'section': self.__section, 'cols': "".join(cols),
                  'attr': self.get_attrs(pyClassNames=self.style.get_classes())}


class Table(Html.Html):
  name = 'Table'

  def __init__(self, report, rows, width, height, helper, options, profile):
    super(Table, self).__init__(report, [], css_attrs={"width": width, "height": height, 'table-layout': 'auto',
            'white-space': 'nowrap', 'border-collapse': 'collapse', 'box-sizing': 'border-box'}, profile=profile)
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.__options = OptPanel.OptionPanelTable(self, options)
    self.header, self.body, self.footer = TSection(self._report, 'thead', options=options), TSection(self._report, 'tbody', options=options), TSection(self._report, 'tfoot', options=options)
    self.header.options.managed = False
    self.body.options.managed = False
    self.footer.options.managed = False
    self.caption = None
    if rows is not None:
      for row in rows:
        self.__add__(row)

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptPanel.OptionPanelTable
    """
    return self.__options

  def __add__(self, row_data):
    """ Add items to a container """
    if isinstance(row_data, Tr):
      row = row_data
    else:
      if not self.header.val and not self.body.val and self.options.header:
        row = Tr(self._report, row_data, True, None, (100, "%"), (100, "%"), 'center', self.options, False)
      else:
        row = Tr(self._report, row_data, False, None, (100, "%"), (100, "%"), 'left', self.options, False)
    if row.header:
      self.header += row
    else:
      self.body += row
    return self

  def from_array(self, data, dim):
    """
    Description:
    ------------
    Load data from a 2D array

    Attributes:
    ----------
    :param data: Array. The list of data
    :param dim: Integer. The number of columns in the table
    """
    v_count = len(data)
    modulo_rest = v_count % dim
    modulo_result = v_count // dim
    for i in range(0, modulo_result):
      row = [data[i * dim + j] for j in range(0, dim)]
      self += row
    if modulo_rest:
      self += data[-modulo_rest:]

  def line(self, text="&nbsp;", align="left", dim=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param align:
    :param dim: Integer. The number of columns in the table
    """
    cell = Td(self._report, [text], False, None, (None, "%"), (None, "%"), align, self.options, False)
    cell.colspan(dim or len(self.body.val[0].val))
    self += Tr(self._report, [cell], False, None, (100, "%"), (100, "%"), align, self.options, False)
    return cell

  def add_caption(self, text, color=None, align=None, width=(100, "%"), height=(100, "%"), htmlCode=None, tooltip=None,
                  options=None, profile=False):
    """
    Description:
    ------------
    The <caption> tag defines a table caption.

    Related Pages:

      https://www.w3schools.com/tags/tag_caption.asp

    Attributes:
    ----------
    :param text:
    :param color:
    :param align:
    :param width:
    :param height:
    :param htmlCode:
    :param tooltip:
    :param options:
    :param profile:
    """
    self.caption = Caption(self._report, text, color, align, width, height, htmlCode, tooltip, options, profile)
    return self.caption

  def get_header(self, i=0):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i: Integer.

    :return:
    """
    return self.header.val[i]

  def get_footer(self, i=0):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i: Integer.

    :return:
    """
    return self.footer.val[i]

  def col(self, i):
    """

    :param i:
    """
    cells = []
    if self.header:
      for h in self.header:
        cells.append(h[i])
    if self.body:
      for b in self.body:
        cells.append(b[i])
    if self.footer:
      for f in self.footer:
        cells.append(f[i])
    for c in cells:
      yield c

  def __getitem__(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i: Integer. The internal row based on the index

    :rtype: Tr
    """
    if not self.body.val:
      return []

    return self.body.val[i]

  def __str__(self):
    caption = "" if self.caption is None else self.caption.html()
    return '<table %s>%s%s%s%s</table>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), caption, self.header.html(), self.body.html(), self.footer.html(), self.helper)


class Col(Html.Html):
  name = 'Column'

  def __init__(self, report, htmlObjs, position, width, height, align, helper, options, profile):
    self.position,  self.rows_css, self.row_css_dflt = position, {}, {}
    super(Col, self).__init__(report, [], profile=profile)
    self.__options, self.__set_size = OptPanel.OptionGrid(self, options), None
    self.style.clear_all(no_default=True)
    self.css({"width": width, "height": height})
    if htmlObjs is not None:
      for htmlObj in htmlObjs:
        self.add(htmlObj)
    if align == "center":
      self.css({'margin-left': 'auto', 'margin-right': 'auto', 'display': 'inline-block', 'text-align': 'center'})
    else:
      self.css({'display': 'inline-block'})
    self.attr["class"].add('col')
    self.style.justify_content = self.position
    if self.position == 'middle':
      # Bootstrap vertical align middle
      self.attr["class"].add('my-auto')

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptPanel.OptionGrid
    """
    return self.__options

  def add(self, htmlObj):
    """
    Description:
    ------------
    Add items to a container

    Attributes:
    ----------
    :param htmlObj:

    :return:
    """
    if not hasattr(htmlObj, 'options'):
      htmlObj = self._report.ui.div(htmlObj)
    super(Col, self).__add__(htmlObj)
    return self

  def build(self, data=None, options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param options:
    :param profile:
    """
    return self.val[0].build(data, options, profile)

  def set_size(self, n):
    """
    Description:
    ------------
    Set the column size

    Usage::

      ps = rptObj.ui.layouts.grid()
    ps += [rptObj.ui.text("test %s" % i) for i in range(5)]
    ps[0][0].set_size(10)

    Attributes:
    ----------
    :param n: Integer. Teh size of the component in the bootstrap row
    """
    if self.__set_size is None:
      if not n:
        self.__set_size = False
        return self

      if isinstance(n, int) or n.is_integer():
        self.__set_size = "col-lg-%s" % int(n)
      else:
        self.__set_size = "col-lg"
      self.attr["class"].add(self.__set_size)
      if self.options.responsive:
        self.attr["class"].add("col-md-%s" % min(int(n) * 2, 12))
        self.attr["class"].add("col-12")
    return self

  def __str__(self):
    content = [htmlObj.html() for htmlObj in self.val]
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(content))


class Row(Html.Html):
  name = 'Column'
  requirements = ('bootstrap', )

  def __init__(self, report, htmlObjs, position, width, height, align, helper, options, profile):
    self.position, self.align = position, align
    super(Row, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptPanel.OptionGrid(self, options)
    if htmlObjs is not None:
      for htmlObj in htmlObjs:
        self.add(htmlObj)
    self.attr["class"].add('row')
    self.style.css.justify_content = self.position
    if align == 'center':
      self.css({'margin': 'auto'})

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptPanel.OptionGrid
    """
    return self.__options

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlPanels.JsHtmlRow
    """
    if self._dom is None:
      self._dom = JsHtmlPanels.JsHtmlRow(self, report=self._report)
    return self._dom

  def __len__(self):
    return len(self.val)

  def add(self, htmlObj):
    """ Add items to a container """
    if not isinstance(htmlObj, Col):
      if not isinstance(htmlObj, list):
        htmlObj = [htmlObj]
      # hack to propagate the height of the row to the underlying columns
      htmlObj = self._report.ui.layouts.col(htmlObj, align=self.align, height=(self.css("height"), ''), position=self.position, options=self.options._attrs)
      htmlObj.style.css.margin_left = "auto"
      htmlObj.style.css.margin_right = "auto"
      htmlObj.options.managed = False
    super(Row, self).__add__(htmlObj)
    return self

  def __str__(self):
    cols = []
    if self.options.noGutters:
      self.attr["class"].add('no-gutters')
    for i, htmlObj in enumerate(self.val):
      if hasattr(htmlObj, 'set_size') and self.options.autoSize:
        htmlObj.set_size(12.0 / len(self.val))
      cols.append(htmlObj.html() if hasattr(htmlObj, 'htmlObj') else str(htmlObj))
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(cols))


class Grid(Html.Html):
  name = 'Grid'
  requirements = ('bootstrap', )

  def __init__(self, report, rows, width, height, align, position, options, profile):
    super(Grid, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.__options, self.position = OptPanel.OptionGrid(self, options), position
    self.style.clear(no_default=True)
    self.css({'overflow-x': 'hidden', 'padding': 0})
    self.attr["class"].add(self.options.classe)
    if align == 'center':
      self.css({'margin': 'auto'})
    if rows is not None:
      for row in rows:
        self.__add__(row)

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptPanel.OptionGrid
    """
    return self.__options

  def __add__(self, row_data):
    """ Add items to a container """
    if isinstance(row_data, Row):
      row = row_data
    else:
      row = self._report.ui.layouts.row(position=self.position, options=self.options._attrs)
      row.style.clear(no_default=True)
      row.style.css.margin = 'auto'
      row.attr["class"].add("row")
      for htmlObjWithDim in row_data:
        if isinstance(htmlObjWithDim, tuple):
          htmlObj, dim = htmlObjWithDim
        else:
          htmlObj, dim = htmlObjWithDim, None
        row.add(htmlObj)
        if dim is not None:
          row[-1].attr["class"].add("col-%s" % dim)
    super(Grid, self).__add__(row)
    #self.colsAlign.append("left")
    return self

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlPanels.JsHtmlGrid
    """
    if self._dom is None:
      self._dom = JsHtmlPanels.JsHtmlGrid(self, report=self._report)
    return self._dom

  def resize(self):
    """
    Description:
    ------------
    For the resizing of the space for the containers.

    This will rescale based on the number of items and the fact that the max per row is 12
    It will update the colsDim list
    """
    max_size = int(12 / len(self.colsDim))
    self.colsDim = [max_size] * len(self.colsDim)
    return self

  def __str__(self):
    rows = []
    for htmlObj in self.val:
      if self._sort_propagate:
        htmlObj.sortable(self._sort_options)
      rows.append(htmlObj.html())
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(rows))


class Tabs(Html.Html):
  name = 'Tabs'

  def __init__(self, report, color, width, height, htmlCode, helper, options, profile):
    super(Tabs, self).__init__(report, "", htmlCode=htmlCode, css_attrs={"width": width, "height": height, 'color': color}, profile=profile)
    self.__panels, self.__panel_objs, self.__selected = [], {}, None
    self.tabs_name, self.panels_name = "button_%s" % self.htmlCode, "panel_%s" % self.htmlCode
    self.tabs_container = self._report.ui.div([])
    self.tabs_container.options.managed = False
    self.add_helper(helper)
    self.__options = OptPanel.OptionPanelTabs(self, options)

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptPanel.OptionPanelTabs
    """
    return self.__options

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlPanels.JsHtmlTabs
    """
    if self._dom is None:
      self._dom = JsHtmlPanels.JsHtmlTabs(self, report=self._report)
    return self._dom

  def __getitem__(self, name):
    return self.__panel_objs[name]

  def select(self, name):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    """
    self.__selected = name
    return self

  def panel(self, name):
    """
    Description:
    ------------
    Get the panel obkect

    Attributes:
    ----------
    :param name: String. The tab name

    :rtype: Div
    """
    return self.__panel_objs[name]["content"]

  def tab(self, name):
    """
    Description:
    ------------
    Get the tab container

    Attributes:
    ----------
    :param name: String. The tab name

    :rtype: Div
    """
    return self.__panel_objs[name]["tab"][0]

  def tab_holder(self, name):
    """
    Description:
    ------------
    Get the tab container

    Attributes:
    ----------
    :param name: String. The tab name

    :rtype: Div
    """
    return self.__panel_objs[name]["tab"]

  def tabs(self):
    """
    Description:
    ------------
    Get the tab container

    Attributes:
    ----------
    :param name: String. The tab name

    :rtype: Div
    """
    for tab_obj in self.__panel_objs.values():
      yield tab_obj["tab"]

  def add_panel(self, name, div, icon=None, selected=False, css_tab=None, css_tab_clicked=None, width=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param div:
    :param icon:
    :param selected: Boolean. Flag to set the selected panel
    :param css_tab:
    :param css_tab_clicked:
    :param width:
    """
    width = Arguments.size(width or self.options.width, unit="px")
    if not hasattr(div, 'options'):
      if div is None:
        div = self._report.ui.div()
        show_div = []
      else:
        div = self._report.ui.div(div)
        show_div = [div.dom.show()]
    else:
      show_div = [div.dom.show()]
    div.css({"display": 'none'})
    div.options.managed = False
    div.set_attrs(name="name", value=self.panels_name)

    self.__panels.append(name)
    if icon is not None:
      tab = self._report.ui.div([
        self._report.ui.icon(icon).css({"display": 'block', 'color': 'inherit', "width": '100%', "font-size": css_defaults.font(4)}),
        name], width=width)
    else:
      if hasattr(name, "html"):
        tab = self._report.ui.div(name, width=width)
      else:
        tab = self._report.ui.div(name, width=width, htmlCode="%s_%s" % (self.htmlCode, JsUtils.getJsValid(name, False)))
    tab_style = self.options.tab_style(name, css_tab)
    tab_style_clicked = self.options.tab_clicked_style(name, css_tab_clicked)
    tab.css(tab_style).css({"padding": '5px 0'})
    tab.set_attrs(name="name", value=self.tabs_name)
    tab.set_attrs(name="data-index", value=len(self.__panels) - 1)
    tab_container = self._report.ui.div(tab, width=width)
    tab_container.options.managed = False
    tab_container.css({'display': 'inline-block'})
    css_cls_name = None
    tab.click([
      self.dom.deselect_tabs(),
      tab.dom.setAttribute("data-selected", True).r,
      self._report.js.getElementsByName(self.panels_name).all([
        #self._report.js.getElementsByName(self.tabs_name).all([
        #  self._report.js.data.all.element.css(self.options.tab_not_clicked_style(name))]),
        tab.dom.css(tab_style_clicked),
        self._report.js.data.all.element.hide(),
        tab_container.dom.toggleClass(css_cls_name, propagate=True) if css_cls_name is not None else "",
        ] + show_div)])
    tab.options.managed = False
    self.__panel_objs[name] = {"tab": tab_container, "content": div}
    if selected:
      self.__selected = name
    return self

  def __str__(self):
    if self.__selected is not None:
      self.__panel_objs[self.__selected]["content"].style.css.display = 'block'
      self.__panel_objs[self.__selected]["tab"][0].css(self.options.tab_clicked_style(self.__selected))
      self.__panel_objs[self.__selected]["tab"][0].attr["data-selected"] = 'true'
    content = []
    self.tabs_container._vals = []
    self.tabs_container.components = {}
    for p in self.__panels:
      self.tabs_container.add(self.__panel_objs[p]["tab"])
      content.append(self.__panel_objs[p]["content"].html())
    return "<div %s>%s%s</div>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.tabs_container.html(), "".join(content), self.helper)


class TabsArrowsDown(Tabs):
  name = 'Tabs Arrow Down'

  def add_panel(self, name, div, icon=None, selected=False, css_tab=None, css_tab_clicked=None):
    super(TabsArrowsDown, self).add_panel(name, div, icon, selected, css_tab, css_tab_clicked)
    self.tab_holder(name).style.add_classes.layout.panel_arrow_down()
    return self


class TabsArrowsUp(Tabs):
  name = 'Tabs Arrow Up'

  def add_panel(self, name, div, icon=None, selected=False, css_tab=None, css_tab_clicked=None):
    super(TabsArrowsUp, self).add_panel(name, div, icon, selected, css_tab, css_tab_clicked)
    self.tab_holder(name).style.add_classes.layout.panel_arrow_up()
    return self


class IFrame(Html.Html):
  name = 'IFrame'

  def __init__(self, report, url, width, height, helper, profile):
    super(IFrame, self).__init__(report, url, css_attrs={"width": width, "height": height}, profile=profile)
    self.css({"overflow-x": 'hidden'})
    self.add_helper(helper)

  @property
  def _js__builder__(self):
    return 'htmlObj.src = data'

  @property
  def dom(self):
    """
    Description:
    ------------

    :return: A Javascript Dom object

    :rtype: JsHtmlPanels.JsHtmlIFrame
    """
    if self._dom is None:
      self._dom = JsHtmlPanels.JsHtmlIFrame(self, report=self._report)
    return self._dom

  def scrolling(self, bool=True):
    """
    Description:
    ------------

    Usage::

      https://www.w3schools.com/tags/tag_iframe.ASP

    """
    if bool:
      self.style.css.overflow_y = "visible"
      self.attr["scrolling"] = "yes"
    else:
      self.attr["scrolling"] = "no"
    return self

  def sandbox(self, text):
    """
    Description:
    ------------

    Usage::

      https://www.w3schools.com/tags/att_iframe_sandbox.asp

    Attributes:
    ----------
    :param text: String. Mandatory. Enables an extra set of restrictions for the content in an <iframe>
    """
    self.attr["sandbox"] = text
    return self

  def allowfullscreen(self, bool=True):
    """
    Description:
    ------------

    Usage::

      https://www.w3schools.com/tags/tag_iframe.ASP

    Attributes:
    ----------
    :param bool: Boolean. optional. Set to true if the <iframe> can activate fullscreen mode by calling the requestFullscreen() method
    """
    self.attr["allowfullscreen"] = 'true' if bool else 'false'
    return self

  def referrerpolicy(self, text):
    """
    Description:
    ------------

    Usage::

      https://www.w3schools.com/tags/att_iframe_referrerpolicy.asp

    Attributes:
    ----------
    :param text:
    """
    self.attr["referrerpolicy"] = text
    return self

  def __str__(self):
    return "<iframe src='%s' %s frameborder='0' scrolling='no'></iframe>%s" % (self.val, self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class Dialog(Html.Html):
  name = 'DialogMenu'
  requirements = ('jqueryui', )

  def __init__(self, report, recordSet, width, height, helper, profile):
    super(Dialog, self).__init__(report, recordSet, css_attrs={"width": width, 'height': height}, profile=profile)
    self.css({"border": '2px solid %s' % self._report.theme.greys[3], "display": "block", "position": "relative",
              "background": self._report.theme.greys[0]})
    #self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.dom.jquery_ui.draggable().toStr())

  @property
  def _js__builder__(self):
    return '''
      var div = %(jqId)s;
      div.dialog({title: "rrrr", autoOpen: false});
      %(jqHtmlObj)s.append(div);
      ''' % {"jqId": JsQuery.decorate_var("'<div>'", convert_var=False), "jqHtmlObj": JsQuery.decorate_var("htmlObj", convert_var=False)}

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Related Pages:

      https://api.jqueryui.com/progressbar

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsQueryUi.ProgressBar
    """
    if self._js is None:
      self._js = JsQueryUi.Dialog(self, report=self._report)
    return self._js

  # def jsAdd(self, title='data.event_val', isPyData=False):
  #   if isPyData:
  #     title = json.loads(title)
  #
  #   return '''
  #   var dialogWindow = $("<div>");
  #   var table = $("table");
  #   dialogWindow.append(table);
  #   dialogWindow.append('<input type="text">');
  #   var d = dialogWindow.dialog( { modal: false, title: %(title)s, show: 'puff', fluid: true,
  #       close: function () {$(this).remove()}, appendTo: "#%(htmlCode)s", resizable: false,
  #       buttons: [{text: "Close", click: function() { $( this ).dialog("close")} } ]
  #   });
  #   d.parent().draggable({containment: '#%(htmlCode)s'});
  #   event.preventDefault()''' % {'title': title, 'htmlCode': self.htmlCode}

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.style.get_classes())


class IconsMenu(Html.Html):
  name = 'Icons Menu'
  requirements = ('font-awesome', )

  def __init__(self, icon_names, report, width, height, htmlCode, helper, profile):
    super(IconsMenu, self).__init__(report, None, css_attrs={"width": width, "height": height}, htmlCode=htmlCode,
                                    profile=profile)
    self._jsActions, self._definedActions = {}, []
    self._icons, self.icon = [], None
    self.css({"margin": "5px 0"})
    for i in icon_names:
      self.add_icon(i)

  def __getitem__(self, i):
    return self._icons[i]

  def add_icon(self, text, css=None, position="after"):
    """
    Add an icon to the HTML object

    Example
    checks.title.add_icon("fas fa-align-center")

    Documentation

    :param text: The icon reference from font awsome website
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    :return: The Html object
    """
    if text is not None:
      self._icons.append(self._report.ui.images.icon(text).css({"margin-right": '5px', 'cursor': "pointer"}))
      self.icon = self._icons[-1]
      if position == "before":
        self.prepend_child(self.icon)
      else:
        self.append_child(self.icon)
      if css is not None:
        self.icon.css(css)
    return self

  def add_select(self, action, data, width=150):
    options = ["<option>%s</option>" % d for d in data]
    self._jsActions[action] = '<select id="inputState" class="form-control" style="width:%spx;display:inline-block">%s</select>' % (width, "".join(options))
    self._definedActions.append(action)
    return self

  def __str__(self):
    htmlIcons = [htmlDef for action, htmlDef in self._jsActions.items()]
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(htmlIcons))


class Form(Html.Html):
  name = 'Generic Form'

  def __init__(self, report, htmlObjs, helper):
    super(Form, self).__init__(report, [])
    self.style.css.padding = "5px"
    self.add_helper(helper)
    self.__submit, self._has_container = None, False
    for i, htmlObj in enumerate(htmlObjs):
      self.__add__(htmlObj)

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.css({'text-align': 'left'})
    super(Form, self).__add__(htmlObj)
    return self

  def submit(self, method, action="#", text="Submit"):
    if action is not None and method is not None:
      self.attr.update({"action": action, "method": method})

    self.__submit = self._report.ui.button(text).set_attrs({"type": 'submit'})
    self.__submit.options.managed = False
    if self._has_container:
      self[0] + self.__submit
    return self

  def __str__(self):
    if self.__submit is None:
      raise Exception("Submit must be defined in a form ")

    str_vals = "".join([i.html() for i in self.val]) if self.val is not None else ""
    return '<form %s>%s%s</form>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), str_vals, self.__submit.html(), self.helper)


class Modal(Html.Html):
  name = 'Modal Popup'

  def __init__(self, report, htmlObjs, header, footer, submit, helper):
    """
    Description:
    -----------
    Constructor for the modal item.
    This object is composed of three parts:  a header, which is a row of object, a body which is a column and a footer which is a row
    they all accept collections of html objects and are configurable just like the normal rows and column objects

    """
    super(Modal, self).__init__(report, [])
    self.add_helper(helper)
    self.doSubmit = submit
    if self.doSubmit:
      self.submit = report.ui.buttons.important("Submit").set_attrs({"type": 'submit'})
      self.submit.options.managed = False
    self.closeBtn = report.ui.texts.span('&times', width='auto')
    self.closeBtn.css(None, reset=True)
    self.closeBtn.style.add_classes.div.span_close()
    self.closeBtn.click(report.js.getElementById(self.htmlCode).css({'display': "none"}))
    self.__header = report.ui.row([])
    self.__header.options.managed = False
    if header:
      for obj in header:
        self.__header + obj
    self.__header += self.closeBtn
    if footer:
      for obj in footer:
        self.__footer + obj
    self.__footer = report.ui.row([])
    self.__footer.options.managed = False
    self.__body = report.ui.col([]).css({'position': 'relative',  'overflow-y': 'scroll'})
    self.__body.options.managed = False
    self.col = report.ui.col([self.__header, self.__body, self.__footer]).css({'width': 'auto'}, reset=True)
    self.col.style.add_classes.div.modal_content()
    self.col.options.managed = False
    self.val.append(self.col)
    self.__outOfScopeClose = True
    for htmlObj in htmlObjs:
      self.__add__(htmlObj)

  @property
  def outOfScopeClose(self):
    return self.__outOfScopeClose

  @outOfScopeClose.setter
  def outOfScopeClose(self, val):
    self.__outOfScopeClose = val

  @property
  def style(self):
    """
    Property to the CSS Style of the component

    :rtype: GrpClsButton.ClassButton
    """
    if self._styleObj is None:
      self._styleObj = GrpClsContainer.ClassModal(self)
    return self._styleObj

  @property
  def header(self):
    return self.__header

  @property
  def footer(self):
    return self.__footer

  @property
  def body(self):
    return self.__body

  def show(self):
    return self._report.js.getElementById(self.htmlCode).css({'display': 'block'})

  def close(self):
    return self._report.js.getElementById(self.htmlCode).css({'display': 'none'})

  def close_on_background(self):
    """
    Description:
    ------------
    Will allow an event to close the modal if a click event is detected anywhere outside the modal
    """
    modal = self._report.js.getElementById(self.htmlCode)
    self._report.js.onReady(self._report.js.window.events.addClickListener(self._report.js.if_('event.target == %s' % modal, modal.css({'display': 'none'})),
                                                       subEvents=['event']))

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.options.managed = False # Has to be defined here otherwise it is set too late
    self.__body += htmlObj
    return self

  def __str__(self):
    if self.__outOfScopeClose:
      self.close_on_background()
    str_vals = "".join([i.html() for i in self.val]) if self.val is not None else ""
    self.set_attrs({'css': self.style.css.attrs})
    if self.doSubmit:
      self.col += self.submit
    return '<div %s>%s</div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), str_vals, self.helper)


class Indices(Html.Html):
  name = 'Index'
  requirements = ('font-awesome', )

  def __init__(self, report, count, width, height, htmlCode, options, profile):
    super(Indices, self).__init__(report, count, css_attrs={"width": width, "height": height}, profile=profile)
    self.items = []
    self.__options = OptPanel.OptionsPanelPoints(self, options)
    for i in range(count):
      div = self._report.ui.div(i, width=(15, "px"))
      div.attr["name"] = self.htmlCode
      div.attr["data-position"] = i + 1
      div.css({"display": 'inline-block', "padding": "2px", "text-align": "center"})
      div.css(self.options.div_css)
      div.style.add_classes.div.background_hover()
      div.options.managed = False
      self.items.append(div)
    #
    self.first = self._report.ui.icon("fas fa-angle-double-left", width=(20, 'px')).css({"display": 'inline-block'})
    self.first.options.managed = False
    self.prev = self._report.ui.icon("fas fa-chevron-left", width=(20, 'px')).css({"display": 'inline-block'})
    self.prev.options.managed = False
    self.next = self._report.ui.icon("fas fa-chevron-right", width=(20, 'px')).css({"display": 'inline-block'})
    self.next.options.managed = False
    self.last = self._report.ui.icon("fas fa-angle-double-right", width=(20, 'px')).css({"display": 'inline-block'})
    self.last.options.managed = False

  @property
  def options(self):
    """

    :rtype: OptPanel.OptionsPanelPoints
    """
    return self.__options

  def __getitem__(self, i):
    return self.items[i]

  def click_item(self, i, jsFncs, profile=False):
    """
    Description:
    ------------

    :param i:
    :param jsFncs:
    :param profile:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return self[i].on("click", [
      self[i].dom.by_name.css({"border-bottom": "1px solid %s" % self._report.theme.colors[0]}).r,
      self[i].dom.css({"border-bottom": "1px solid %s" % self.options.background_color})] + jsFncs, profile)

  def __str__(self):
    str_vals = "".join([self.first.html(), self.prev.html()] + [i.html() for i in self.items] + [self.next.html(), self.last.html()])
    return '<div %s>%s</div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), str_vals, self.helper)


class Points(Html.Html):
  name = 'Index'

  def __init__(self, report, count, width, height, htmlCode, options, profile):
    super(Points, self).__init__(report, count, css_attrs={"width": width, "height": height}, htmlCode=htmlCode, profile=profile)
    self.items = []
    self.css({"text-align": "center"})
    self.__options = OptPanel.OptionsPanelPoints(self, options)
    for i in range(count):
      div = self._report.ui.div(self._report.entities.non_breaking_space)
      div.attr["name"] = htmlCode
      div.attr["data-position"] = i # keep the python indexation
      div.css({"border": "1px solid %s" % self._report.theme.greys[5], "border-radius": "10px", "width": "15px", "height": "15px"})
      div.css(self.options.div_css)
      div.style.add_classes.div.background_hover()
      div.options.managed = False
      self.items.append(div)
    self[self.options.selected].css({"background-color": self.options.background_color})

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptPanel.OptionsPanelPoints
    """
    return self.__options

  def on(self, event, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------
    Add Javascript events to all the items in the component

    Attributes:
    ----------
    :param event:
    :param jsFncs: Array. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    str_fnc = JsUtils.jsConvertFncs(jsFncs, toStr=True)
    if event == "click":
      for i in range(len(self.items)):
        self.click_item(i, str_fnc)
    else:
      for i in range(len(self.items)):
        self.on_item(i, event, str_fnc)
    return self

  def on_item(self, i, event, jsFncs, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i: Integer. The item index
    :param event: String. The Javascript event reference
    :param jsFncs: Array. The Javascript functions
    :param profile:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return self[i].on(event, [
      'var data = {position: this.getAttribute("data-position")}'] + jsFncs, profile)

  def click_item(self, i, jsFncs, profile=False, onReady=False):
    """
    Description:
    ------------
    Add a click event on a particular item of the component

    Attributes:
    ----------
    :param i: Integer. The item index
    :param jsFncs: Array. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return self[i].on("click", [
      'var data = {position: this.getAttribute("data-position")}',
      self[i].dom.by_name.css({"background-color": ""}).r,
      self[i].dom.css({"background-color": self.options.background_color})] + jsFncs, profile, onReady=onReady)

  def __getitem__(self, i):
    return self.items[i]

  def __str__(self):
    str_vals = "".join([i.html() for i in self.items])
    return '<div %s>%s</div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), str_vals, self.helper)


class Header(Html.Html):
  name = 'Header'

  def __init__(self, report, htmlObj, width, height, htmlCode, helper, options, profile):
    super(Header, self).__init__(report, htmlObj, htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptPanel.OptionsDiv(self, options)
    self.add_helper(helper)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    :rtype: OptPanel.OptionsDiv
    """
    return self.__options

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.options.managed = False # Has to be defined here otherwise it is set to late
    if self.options.inline:
      htmlObj.style.css.display = 'inline-block'
    self.val.append(htmlObj)
    return self

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    return "<header %s>%s</header>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_div, self.helper)


class Section(Html.Html):
  name = 'Section'

  def __init__(self, report, htmlObj, width, height, htmlCode, helper, options, profile):
    super(Section, self).__init__(report, htmlObj, htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptPanel.OptionsDiv(self, options)
    self.add_helper(helper)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    :rtype: OptPanel.OptionsDiv
    """
    return self.__options

  def __add__(self, htmlObj):
    """ Add items to a container """
    if self.options.inline:
      htmlObj.style.css.display = 'inline-block'
    super(Section, self).__add__(htmlObj)
    return self

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    return "<section %s>%s</section>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_div, self.helper)

