#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptJsonFormatter
from epyk.core.html.options import OptText

from epyk.core.js.html import JsHtmlStars
from epyk.core.js.packages import JsJsonFormatter
from epyk.core.js.primitives import JsObjects

from epyk.core.js import JsUtils

# The list of CSS classes
from epyk.core.css.styles import GrpClsLayout
from epyk.core.css import Defaults

from epyk.core import data


class Hr(Html.Html):
  name = 'Line delimiter'

  def __init__(self, report, background_color, width, height, align, profile):
    super(Hr, self).__init__(report, "", profile=profile, css_attrs={"height": height, 'width': width,
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
    self.add_icon("fas fa-spinner fa-spin", css={"font-size": "%spx" % (self.size+8)}, family=options.get("icon_family"))
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
    super(HtmlJson, self).__init__(report, data, profile=profile, css_attrs={"height": height, "width": width})
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
    Description:
    -----------

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


class Breadcrumb(Html.Html):
  name = 'Breadcrumb'

  def __init__(self, report, data, width, height, options, profile):
    super(Breadcrumb, self).__init__(report, [], profile=profile, css_attrs={"height": height, "width": width})
    self.style.css.line_height = height[0]
    self.style.css.vertical_align = 'middle'
    if data is not None:
      for rec in data:
        if not hasattr(rec, 'options'):
          if isinstance(rec, dict):
            data = report.ui.div(rec['text'], width=("auto", '')) if options['selected'] == rec['text'] else report.ui.link(rec['text'], rec['url'])
          else:
            data = report.ui.div(rec, width=("auto", '')) if options['selected'] == rec else report.ui.link(rec)
          data.style.css.display = 'inline-block'
        self.add(data)
    self.style.background = report.theme.greys[1]

  def __add__(self, component):
    """ Add items to a container """
    if hasattr(component, 'htmlCode'):
      component.options.managed = False
    self.val.append(component)
    return self

  def __str__(self):
    rows = [htmlObj.html() if hasattr(htmlObj, 'html') else str(htmlObj) for htmlObj in self.val]
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), " / ".join(rows))


class Legend(Html.Html):
  name = 'Legend'

  def __init__(self, report, recordse, width, height, align, options, profile):
    super(Legend, self).__init__(report, recordse, css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptJsonFormatter.OptionsLegend(self, options)

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the input component properties

    :rtype: OptJsonFormatter.OptionsLegend
    """
    return self.__options

  def __str__(self):
    divs = []
    css_inline = Defaults.inline(self.options.style)
    for val in self.val:
      val["css_inline"] = css_inline
      divs.append("<div><div style='background:%(color)s;%(css_inline)s'></div>%(name)s</div>" % val)
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(divs))


class Slides(Html.Html):
  requirements = ('font-awesome', )
  name = 'Slides'

  def __init__(self, report, start, width, height, options, profile):
    super(Slides, self).__init__(report, [], css_attrs={"width": width, 'height': height}, profile=profile)
    self.__options = OptText.OptionsText(self, options)
    self.attr['data-current_slide'] = start
    self.title = self._report.ui.title("")
    self.title.style.css.border_bottom = "1px solid %s" % report.theme.colors[7]
    self.title.style.css.color = report.theme.colors[7]
    self.title.style.css.margin = 0
    self.title.options.managed = False
    if 'timer' in options:
      self._report.ui.calendars.timer(options['timer']).css({"position": 'fixed', "font-size": '15px', 'top': '8px',
          "padding": '8px', "right": '15px', 'width': 'none', 'color': report.theme.greys[5]})
    self.next = self._report.ui.icon("fas fa-arrow-alt-circle-right").css({"position": 'fixed',
          "font-size": '35px', 'bottom': '0',  "padding": '8px', "right": '10px', 'width': 'none'})

    self.previous = self._report.ui.icon("fas fa-arrow-alt-circle-left").css({"position": 'fixed',
          "font-size": '35px', 'bottom': '0',  "padding": '8px', "left": '10px', 'width': 'none'})

    self.page_number = self._report.ui.text("").css({"position": 'fixed',
          "font-size": '25px', 'bottom': '0',  "padding": '8px', "left": '50%', 'width': 'none'})

    self.next.click([
      self._report.js.getElementsByName(self.htmlCode).all([data.loops.dom_list.hide()]),
        data.primitives.float(self.dom.attr("data-current_slide").toString().parseFloat().add(1), 'slide_index'),

      self.js.if_(report.js.object('slide_index') <= self.dom.attr('data-last_slide'), [
        self.title.build(self._report.js.getElementsByName(self.htmlCode)[report.js.object('slide_index')].attr('data-slide_title')),
        self.dom.attr("data-current_slide", report.js.object('slide_index')),
        self._report.js.getElementsByName(self.htmlCode)[report.js.object('slide_index')].show(display_value='flex'),
        self._report.js.getElementById("%s_count" % self.htmlCode).innerHTML(report.js.object('slide_index').toString().parseFloat().add(1)),
      ]).else_([
        self.title.build(self._report.js.getElementsByName(self.htmlCode)[report.js.object('slide_index').add(-1)].attr('data-slide_title')),
        self._report.js.getElementsByName(self.htmlCode)[report.js.object('slide_index').add(-1)].show(display_value='flex')]),

      self.js.if_(report.js.object('slide_index') > 0, [self.previous.dom.show()]),
      self.js.if_(report.js.object('slide_index') == self.dom.attr('data-last_slide'), [self.next.dom.hide()])
    ])

    self.previous.click([
      self._report.js.getElementsByName(self.htmlCode).all([data.loops.dom_list.hide()]),
      data.primitives.float(self.dom.attr("data-current_slide").toString().parseFloat().add(-1), 'slide_index'),

      self.js.if_(report.js.object('slide_index') >= 0, [
        self.title.build(self._report.js.getElementsByName(self.htmlCode)[report.js.object('slide_index')].attr('data-slide_title')),
        self.dom.attr("data-current_slide", report.js.object('slide_index')),
        self._report.js.getElementsByName(self.htmlCode)[report.js.object('slide_index')].show(display_value='flex'),
        self._report.js.getElementById("%s_count" % self.htmlCode).innerHTML(report.js.object('slide_index').toString().parseFloat().add(1)),
      ]).else_([
        self.title.build(self._report.js.getElementsByName(self.htmlCode)[0].attr('data-slide_title')),
        self._report.js.getElementsByName(self.htmlCode)[0].show(display_value='flex')]),

      self.js.if_(report.js.object('slide_index') == 0, [self.previous.dom.hide()]),
      self.js.if_(report.js.object('slide_index') < self.dom.attr('data-last_slide'), [self.next.dom.show()])
    ])

    # Add the keyboard shortcut
    report.body.keydown.right([self.next.dom.events.trigger("click")])
    report.body.keydown.left([self.previous.dom.events.trigger("click")])

    self.style.css.padding = "0 20px 10px 20px"

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    :rtype: OptText.OptionsText
    """
    return self.__options

  @property
  def dom(self):
    """
    Description:
    ------------
    The JavaScript dom object to be used in any events

    :rtype: JsHtmlStars.Slides
    """
    if self._dom is None:
      self._dom = JsHtmlStars.Slides(self, report=self._report)
    return self._dom

  def add(self, component):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param component:
    """
    if isinstance(component, list):
      for c in component:
        if hasattr(c, 'options'):
          c.options.managed = False
      component = self._report.ui.div(component)
      component.style.css.width = "100%"
      component.style.css.height = "90%"
      component.style.css.display = "flex"
      component.style.css.padding = 5
      component.style.css.justify_content = "center"
      component.style.css.align_items = "center"
      component.style.css.flex_direction = "column"
    if hasattr(component, 'options'):
      component.options.managed = False
    self.val.append(component)
    return self

  def add_slide(self, title, component):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param component:
    """
    self.add(component)
    self.val[-1].attr["data-slide_title"] = title
    return self

  @property
  def _js__builder__(self):
    return '''
      let index = htmlObj.getAttribute("data-current_slide");
      if(options.showdown){var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data)} 
      document.getElementsByName(htmlObj.id)[index].innerHTML = data;
      '''

  def __str__(self):
    self._report.body.style.css.height = '100%'
    self.page_number._vals = "<font id='%s_count' ondblclick='this.contentEditable = true' onkeydown='if (event.keyCode == 13) {this.contentEditable = false}'>%s</font> / %s" % (self.htmlCode, self.attr['data-current_slide']+1, len(self.val))
    comps = []
    self.attr['data-last_slide'] = len(self.val)-1
    for i, s in enumerate(self.val):
      s.attr['name'] = self.htmlCode
      if i != self.attr['data-current_slide']:
        s.style.css.display = False
      else:
        self.title._vals = s.attr.get("data-slide_title", "")
        s.style.css.display = 'flex'

      comps.append(s.html())
    return '<div %s>%s%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.title.html(), "".join(comps))
