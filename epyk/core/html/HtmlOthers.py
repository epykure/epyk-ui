"""
HTML Definition for extra layouts and feedbacks components
"""

from epyk.core.html import Html

from epyk.core.js.primitives import JsObjects
from epyk.core.html.entities import EntHtml4

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls


class Hr(Html.Html):
  name, category, callFnc = 'Line delimiter', 'Layouts', 'hr'
  _grpCls = CssGrpCls.CssClassHr
  builder_name = False

  def __init__(self, report, color, count, size, background_color, height, align, profile):
    super(Hr, self).__init__(report, count, height=height[0], heightUnit=height[1], profile=profile)
    if color is not None:
      self.css('color', color)
    if align == "center":
      self.css('margin', "auto")
    self.size, self.background_color = size, background_color if background_color is not None else self._report.getColor('greys', 2)

  def __str__(self):
    hr = '<hr style="height:%spx;background-color:%s">' % ("%s%s" % (self.size[0], self.size[1]), self.background_color) if self.size is not None else '<hr style="background-color:%s" />' % self.backgroundColor
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.defined), "".join(self.val * [hr]))

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
  builder_name = False

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
    for i in range(best):
      self.add_span("", position="after", css=False)
      self._sub_htmls[-1].style.addCls("fa fa-star")
      self._sub_htmls[-1].css({"margin": '0', "padding": 0})
      self._sub_htmls[-1].set_attrs(name="data-level", value=i)
      self._spans.append(self._sub_htmls[-1])
    self.add_label(label, {"margin": "0 0 0 5px", 'height': 'none', "text-align": "left", "display": "inline-block",
                           'float': 'None'}, position="after")
    self.add_helper(helper).helper.css({"margin": '1px 4px'})
    self.css({'text-align': align, "display": 'block'})
    self._jsStyles = {'color':  self.getColor("success", 1) if color is None else color}

  def click(self, js_fncs=None, profile=False):
    """
    Add the event click and double click to the starts item

    Example
    stars = rptObj.ui.rich.stars(3, label="test Again")
    stars.click(rptObj.js.console.log("test").toStr())

    :param js_fncs: An array of Js functions or string. Or a string with the Js
    :param profile:

    :return: self to allow the chains
    """
    self.css({"cursor": "pointer"})
    if js_fncs is None:
      js_fncs = []
    else:
      if not isinstance(js_fncs, list):
        js_fncs = [js_fncs]
    js_fncs = ["var data = parseInt(event.target.dataset.level)+1"] + js_fncs
    js_fncs.append(self.build(data=JsObjects.JsObjects.get("data"), options=self._jsStyles))
    for span in self._spans:
      span.click(js_fncs, profile)
    return self

  @property
  def _js__builder__(self):
    return '''
      htmlObj.dataset.level = data;
      htmlObj.querySelectorAll("span").forEach(function(span, i){
        if (i < data){span.style.color = options.color; console.log(options.color)}
        else {span.style.color = ''}})'''

  def __str__(self):
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.defined), self.helper)


class Help(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Info', 'Rich', 'info'

  def __init__(self, report, val, width, profile, options):
    super(Help, self).__init__(report, val, width=width[0], widthUnit=width[1], profile=profile)
    self.css({"cursor": "pointer", "float": "right", 'margin': '1px 4px'})
    self.attr['class'].add("fas fa-question-circle")
    self.attr['title'] = val
    self._jsStyles = options

  @property
  def _js__builder__(self):
    return '''
      htmlObj.setAttribute("title", data);
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<i %s></i>' % self.get_attrs()

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document): pass

  def to_pdf(self, document): pass

  def to_xls(self, workbook, worksheet, cursor): pass


class Loading(Html.Html):
  name, category = 'Loading', 'Others'
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  _grpCls = CssGrpCls.CssClassLoading
  builder_name = False

  def __init__(self, report, text, color, size, options):
    super(Loading, self).__init__(report, text)
    self.color = self.getColor('greys', -1) if color is None else color
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
    return '<div %s></div>' % (self.get_attrs(pyClassNames=self.defined))


class Workflow(Html.Html):
  name = "workflow"

  def __init__(self, report, records, width, height, color, size, options):
    super(Workflow, self).__init__(report, records, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1])
    self.color = self.getColor('greys', -1) if color is None else color
    self.size = size[0]
    self.css({'color': self.color, 'font-size': "%s%s" % (size[0], size[1]), "display": "inline-block", "margin": '5px'})
    self.status_colors = {
      "success": {"border": self.getColor("success", 1), "background": self.getColor("success", 0), "stroke-width": 2, "stroke": self.getColor("greys", -1)},
      "error": {"border": self.getColor("danger", 1), "background": self.getColor("danger", 0), "stroke-width": 2, "stroke": self.getColor("greys", -1)},
      "pending": {"border": self.getColor("warning", 1), "background": self.getColor("warning", 1), "stroke-width": 1, "stroke": self.getColor("greys", -1)},
      "default": {"border": self.getColor("greys", 5), "background": self.getColor("greys", 3), "stroke-width": 1, "stroke": self.getColor("greys", -1)}}

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
      line = self._report.ui.charts.svg.line(options={"stroke": colors["stroke"], "stroke-width": colors["stroke-width"]})
      line.inReport = False
      divs.append(str(line))

      # Add the following step
      step = self._report.ui.div(EntHtml4.NO_BREAK_SPACE).tooltip(v['value'])
      step.css({"border": '1px solid %s' % colors["border"], "border-radius": "20px", "width": '20px', "height": '20px',
                'padding': '2px', "background": colors["background"]})
      step.inReport = False
      divs.append("<div style='display:inline-block;width:auto;height:auto'>%s<span>%s</span></div>" % (step, v.get("label", EntHtml4.NO_BREAK_SPACE)))
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.defined), "".join(divs))
