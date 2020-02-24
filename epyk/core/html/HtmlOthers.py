from epyk.core.html import Html

from epyk.core.js.html import JsHtmlWorkflow
from epyk.core.js.html import JsHtmlStars
from epyk.core.js.primitives import JsObjects
from epyk.core.html.entities import EntHtml4

from epyk.core.js import JsUtils

# The list of CSS classes
from epyk.core.css.styles import GrpClsLayout


class Hr(Html.Html):
  name, category, callFnc = 'Line delimiter', 'Layouts', 'hr'

  def __init__(self, report, background_color, height, align, profile):
    super(Hr, self).__init__(report, "", profile=profile, css_attrs={"height": height,
                             'border-color': background_color or report.theme.greys[2],
                             'background-color': background_color or report.theme.greys[2]})
    if align == "center":
      self.style.css.margin = "auto"

  @property
  def style(self):
    """
    Property to the CSS Style of the component

    :return: GrpClsLayout.ClassStandard
    """
    if self._styleObj is None:
      self._styleObj = GrpClsLayout.ClassStandard(self)
    return self._styleObj

  def __str__(self):
    return '<hr %s>' % (self.get_attrs(pyClassNames=self.style.get_classes()))

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val): return True if val.strip() == '***' else None

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report=None):
    if report is not None:
      getattr(report, cls.callFnc)()
    return ["report.%s()" % cls.callFnc]

  @classmethod
  def jsMarkDown(self, vals): return "***"

  def to_word(self, document):
    document.add_paragraph("_________________________________")


class Newline(Html.Html):
  name, category, callFnc = 'New line', 'Layouts', 'new_line'

  def __str__(self):
    return "".join(['<br />'] * self.val)

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val): return True if val.strip() == '' else None

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report=None):
    if report is not None:
      getattr(report.ui.layouts, cls.callFnc)()
    return ["report.ui.%s.%s()" % (cls.category.lower(), cls.callFnc)]

  @classmethod
  def jsMarkDown(self, vals): return ""

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    document.add_page_break()


class Stars(Html.Html):
  name, category, callFnc = 'Stars', 'Rich', 'stars'
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']

  def __init__(self, report, val, label, color, align, best, htmlCode, helper, profile):
    super(Stars, self).__init__(report, val, htmlCode=htmlCode, profile=profile)
    # Add the HTML components
    self._spans = []
    self._jsStyles = {'color': self._report.theme.success[1] if color is None else color}
    for i in range(best):
      self.add_span("", position="after", css=False)
      self._sub_htmls[-1].attr['class'].add("fa fa-star")
      self._sub_htmls[-1].css({"margin": 0, "padding": 0})
      self._sub_htmls[-1].set_attrs(name="data-level", value=i)
      if i < val:
        self._sub_htmls[-1].css({"color": self._jsStyles['color']})
      self._spans.append(self._sub_htmls[-1])
    self.set_attrs(name='data-level', value=val)
    self.add_label(label, {"margin": "0 0 0 5px", 'height': 'none', "text-align": "left", "display": "inline-block",
                           'float': 'None'}, position="after")
    self.add_helper(helper).helper.css({"margin": '1px 4px'})
    self.css({'text-align': align, "display": 'block'})

  @property
  def dom(self):
    """
    Description:
    ------------
    The JavaScript dom object to be used in any events

    :rtype: JsHtmlStars.Stars
    """
    if self._dom is None:
      self._dom = JsHtmlStars.Stars(self, report=self._report)
    return self._dom

  def click(self, js_fncs=None, profile=False):
    """
    Description:
    ------------
    Add the event click and double click to the starts item
    The Javascript function will be triggered after the change of content of the component

    Usage:
    ------
    stars = rptObj.ui.rich.stars(3, label="test Again")
    stars.click(rptObj.js.console.log("test").toStr())

    Attributes:
    ----------
    :param js_fncs: An array of Js functions or string. Or a string with the Js
    :param profile: Boolean.

    :return: self to allow the chains
    """
    self.css({"cursor": "pointer"})
    if js_fncs is None:
      js_fncs = []
    else:
      if not isinstance(js_fncs, list):
        js_fncs = [js_fncs]
    js_fncs = ["var data = parseInt(event.target.dataset.level)+1",
               self.build(data=JsObjects.JsObjects.get("data"), options=self._jsStyles)] + js_fncs
    str_fncs = JsUtils.jsConvertFncs(js_fncs)
    for span in self._spans:
      span.click(str_fncs, profile)
    return self

  @property
  def _js__builder__(self):
    return '''
      htmlObj.dataset.level = data;
      htmlObj.querySelectorAll("span").forEach(function(span, i){
        if (i < data){span.style.color = options.color}
        else {span.style.color = ''}})'''

  def __str__(self):
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class Help(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Info', 'Rich', 'info'

  def __init__(self, report, val, width, profile, options):
    super(Help, self).__init__(report, val, css_attrs={"width": width}, profile=profile)
    self.attr['class'].add("fas fa-question-circle")
    self.attr['title'] = val
    self._jsStyles = options

  @property
  def style(self):
    """
    Property to the CSS Style of the component

    :rtype: GrpClsLayout.ClassHelp
    """
    if self._styleObj is None:
      self._styleObj = GrpClsLayout.ClassHelp(self)
    return self._styleObj

  @property
  def _js__builder__(self):
    return '''
      htmlObj.setAttribute("title", data);
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<i %s></i>' % self.get_attrs(pyClassNames=self.style.get_classes())

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document): pass

  def to_pdf(self, document): pass

  def to_xls(self, workbook, worksheet, cursor): pass


class Loading(Html.Html):
  name, category = 'Loading', 'Others'
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']

  def __init__(self, report, text, color, size, options):
    super(Loading, self).__init__(report, text)
    self.color = self._report.theme.greys[-1] if color is None else color
    self.size = size[0]
    self.css({'color': self.color, 'font-size': "%s%s" % (size[0], size[1]), 'z-index': 5, 'margin': 0})
    self.add_icon("fas fa-spinner fa-spin", css={"font-size": "%spx" % (self.size+8)})
    if options.get('fixed', False):
      self.icon.css({"margin-right": '5px', "font-size": 'inherit'})
      self.css({"position": 'fixed', 'bottom': '0px', 'right': '5px'})
      self.add_span("%s..." % text, position="after", css={"width": 'auto'})
    else:
      self.add_span("%s..." % text, position="after", css={"width": '100%', "margin": "5px"})

  def fixed(self, css=None, icon_css=None):
    """
    Set css attributes of the loading div to be fixed
    This can be done directly in options in the component constructor options={"fixed": True}

    :param css: Dictionary with the css attributes
    :param icon_css: Dictionary with the CSS attributes

    :return: self to allow the chains
    """
    dflt_css = {"position": 'fixed', 'bottom': '5px', 'right': '5px'}
    if css is not None:
      dflt_css.update(css)
    dflt_css_icon = {"margin-right": '5px', "font-size": 'inherit'}
    if dflt_css_icon is not None:
      dflt_css_icon.update(icon_css)
    self.icon.css(dflt_css_icon)
    self.css(dflt_css)
    return self

  def __str__(self):
    return '<div %s></div>' % (self.get_attrs(pyClassNames=self.style.get_classes()))


class Workflow(Html.Html):
  name = "workflow"

  def __init__(self, report, records, width, height, color, options):
    super(Workflow, self).__init__(report, records, css_attrs={"width": width, "height": height})
    self.color = self._report.theme.greys[-1] if color is None else color
    self.css({'color': self.color, "display": "inline-block", "margin": '5px'})
    self.status_colors = {
      "success": {"border": self._report.theme.success[1], "background": self._report.theme.success[0], "stroke-width": 2, "stroke": self._report.theme.greys[-1]},
      "error": {"border": self._report.theme.danger[1], "background": self._report.theme.danger[0], "stroke-width": 2, "stroke": self._report.theme.greys[-1]},
      "pending": {"border": self._report.theme.warning[1], "background": self._report.theme.warning[1], "stroke-width": 1, "stroke": self._report.theme.greys[-1]},
      "default": {"border": self._report.theme.greys[5], "background": self._report.theme.greys[3], "stroke-width": 1, "stroke": self._report.theme.greys[-1]}}

  @property
  def dom(self):
    """

    :rtype: JsHtmlWorkflow.Workflow
    """
    if self._dom is None:
      self._dom = JsHtmlWorkflow.Workflow(self, report=self._report)
    return self._dom

  def __str__(self):
    divs = []
    # Add the first step
    colors = self.status_colors.get(self.val[0].get('status', 'default'), self.status_colors['default'])
    step = self._report.ui.div(EntHtml4.NO_BREAK_SPACE).tooltip(self.val[0]['value'])
    step.css({"border": '1px solid %s' % colors["border"], "border-radius": "20px", "width": '20px', "height": '20px',
              'padding': '2px', "background": colors["background"]})
    step.inReport = False
    divs.append("<div style='display:inline-block;width:auto;height:auto'>%s<span>%s</span></div>" % (step, self.val[0].get("label", EntHtml4.NO_BREAK_SPACE)))

    for v in self.val[1:]:
      colors = self.status_colors.get(v.get('status', 'default'), self.status_colors['default'])
      # Add the link to the next step
      line = self._report.ui.charts.svg.line(y1=10, y2=10, width=(40, "px"), height=(60, "px"), options={"stroke": colors["stroke"], "stroke-width": colors["stroke-width"]})
      line.inReport = False
      divs.append(str(line))

      # Add the following step
      step = self._report.ui.div(EntHtml4.NO_BREAK_SPACE).tooltip(v['value'])
      step.css({"border": '1px solid %s' % colors["border"], "border-radius": "20px", "width": '20px', "height": '20px',
                'padding': '2px', "background": colors["background"]})
      step.inReport = False
      divs.append("<div style='display:inline-block;width:auto;height:auto'>%s<span>%s</span></div>" % (step, v.get("label", EntHtml4.NO_BREAK_SPACE)))
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(divs))
