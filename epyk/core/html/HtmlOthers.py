from epyk.core.html import Html
from epyk.core.html.options import OptJsonFormatter

from epyk.core.js.html import JsHtmlStars
from epyk.core.js.packages import JsJsonFormatter
from epyk.core.js.primitives import JsObjects

from epyk.core.js import JsUtils

# The list of CSS classes
from epyk.core.css.styles import GrpClsLayout


class Hr(Html.Html):
  name = 'Line delimiter'

  def __init__(self, report, background_color, height, align, profile):
    super(Hr, self).__init__(report, "", profile=profile, css_attrs={"height": height,
                             'border-color': background_color or report.theme.greys[5],
                             'background-color': background_color or report.theme.greys[5]})
    if align == "center":
      self.style.css.margin = "auto"

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component

    :return: GrpClsLayout.ClassStandard
    """
    if self._styleObj is None:
      self._styleObj = GrpClsLayout.ClassStandard(self)
    return self._styleObj

  def __str__(self):
    return '<hr %s>' % (self.get_attrs(pyClassNames=self.style.get_classes()))


class Newline(Html.Html):
  name = 'New line'

  def __str__(self):
    return "".join(['<br />'] * self.val)


class Stars(Html.Html):
  name = 'Stars'
  requirements = ('font-awesome', )

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
    self.add_helper(helper)
    if self.helper:
      self.helper.css({"margin": '1px 4px'})
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

  def click(self, js_fncs=None, profile=False, source_event=None):
    """
    Description:
    ------------
    Add the event click and double click to the starts item
    The Javascript function will be triggered after the change of content of the component

    Usage::

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
      span.click(str_fncs, profile, source_event=source_event)
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
  requirements = ('font-awesome', )
  name = 'Info'

  def __init__(self, report, val, width, profile, options):
    super(Help, self).__init__(report, val, css_attrs={"width": width}, profile=profile)
    self.attr['class'].add("fas fa-question-circle")
    self.attr['title'] = val
    self._jsStyles = options

  @property
  def style(self):
    """
    Description:
    ------------
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


class Loading(Html.Html):
  requirements = ('font-awesome', )
  name = 'Loading'

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
    Description:
    ------------
    Set css attributes of the loading div to be fixed
    This can be done directly in options in the component constructor options={"fixed": True}

    Attributes:
    ----------
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


class HtmlJson(Html.Html):
  name = 'Pretty Json'
  requirements = ('json-formatter', )

  def __init__(self, report, data, width, height, options, profile):
    super(HtmlJson, self).__init__(report, data, profile=profile, css_attrs={"height": height, width: "width"})
    self.__options = OptJsonFormatter.OptionsJsonFmt(self, options)

  @property
  def jsonId(self):
    """
    Return the Javascript variable of the json object
    """
    return "%s_obj" % self.htmlCode

  @property
  def _js__builder__(self):
    return '''
      window[ htmlObj.id + '_obj'] = new JSONFormatter(data, options.open, options.opts); htmlObj.innerHTML = '';
      htmlObj.appendChild(window[ htmlObj.id + '_obj'].render());
      '''

  @property
  def options(self):
    """

    :rtype: OptJsonFormatter.OptionsJsonFmt
    """
    return self.__options

  @property
  def js(self):
    """
    Return the Javascript internal object

    :return: A Javascript object

    :rtype: JsJsonFormatter.Json
    """
    if self._js is None:
      self._js = JsJsonFormatter.Json(self._report, varName=self.jsonId, setVar=False, parent=self)
    return self._js

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % (self.get_attrs(pyClassNames=self.style.get_classes()))
