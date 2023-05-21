#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.html.options import OptJsonFormatter
from epyk.core.html.options import OptText
from epyk.core.html.options import OptQrCode

from epyk.core.js.html import JsHtmlStars
from epyk.core.js.html import JsHtmlJson
from epyk.core.js.packages import JsJsonFormatter
from epyk.core.js.packages import JsQrCode
from epyk.core.js.primitives import JsObjects

from epyk.core.js import JsUtils

# The list of CSS classes
from epyk.core.css.styles import GrpClsLayout
from epyk.core.css import Defaults

from epyk.core import data


class Hr(Html.Html):
  name = 'Line delimiter'

  def __init__(self, page: primitives.PageModel, background_color: str, width: tuple, height: tuple, align: str,
               options: Optional[dict], profile: Optional[Union[dict, bool]]):
    super(Hr, self).__init__(page, "", options=options, profile=profile, css_attrs={"height": height, 'width': width,
                             'border-color': background_color or page.theme.greys[5],
                             'background-color': background_color or page.theme.greys[5]})
    if align == "center":
      self.style.css.margin = "auto"

  def margin(self, left: int = 0, right: int = 0, unit: str = '%'):
    """
    Shortcut to set the margin let and right for this HTML component.

    :param left: Optional. The margin left.
    :param right: Optional. The margin right.
    :param unit: Optional. The unit by default percentage.
    """
    if left:
      self.style.css.margin_left = "%s%s" % (left, unit)
    if right:
      self.style.css.margin_right = "%s%s" % (right, unit)
    self.style.css.width = "calc(100%% - %s%s)" % (left+right, unit)
    return self

  @property
  def style(self) -> GrpClsLayout.ClassStandard:
    """ Property to the CSS Style of the component. """
    if self._styleObj is None:
      self._styleObj = GrpClsLayout.ClassStandard(self)
    return self._styleObj

  def __str__(self):
    return '<hr %s>' % (self.get_attrs(css_class_names=self.style.get_classes()))


class Newline(Html.Html):
  name = 'New line'

  def __str__(self):
    return "".join(['<br />'] * self.val)


class Stars(Html.Html):
  name = 'Stars'

  def __init__(self, page: primitives.PageModel, val, label, color, align, best, html_code, helper, options, profile):
    icon_details = page.icons.get("star")
    if icon_details['icon_family'] != 'bootstrap-icons':
      self.requirements = (icon_details['icon_family'],)
    super(Stars, self).__init__(page, val, html_code=html_code, profile=profile, options=options)
    # Add the HTML components
    self._spans = []
    self._jsStyles = {'color': self.page.theme.success.base if color is None else color}
    for i in range(best):
      self.add_span("", position="after", css=False)
      self._sub_htmls[-1].attr['class'].add(icon_details["icon"])
      self._sub_htmls[-1].css({"margin": 0, "padding": 0})
      self._sub_htmls[-1].set_attrs(name="data-level", value=i)
      if i < val:
        self._sub_htmls[-1].css({"color": self._jsStyles['color']})
      self._spans.append(self._sub_htmls[-1])
    self.set_attrs(name='data-level', value=val)
    self.add_label(label, {"margin": "0 0 0 5px", 'height': 'none', "text-align": "left", "display": "inline-block",
                           'float': 'None'}, html_code=self.htmlCode, position="after")
    self.add_helper(helper)
    if self.helper:
      self.helper.css({"margin": '1px 4px'})
    self.css({'text-align': align, "display": 'block'})

  @property
  def dom(self) -> JsHtmlStars.Stars:
    """ The JavaScript dom object to be used in any events. """
    if self._dom is None:
      self._dom = JsHtmlStars.Stars(self, page=self.page)
    return self._dom

  def click(self, js_funcs: types.JS_FUNCS_TYPES = None,
            profile: types.PROFILE_TYPE = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Add the event click and double click to the starts item.

    The Javascript function will be triggered after the change of content of the component.

    Usage::

      stars = page.ui.rich.stars(3, label="test Again")
      stars.click(page.js.console.log("test").toStr())

    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

    :return: self to allow the chains
    """
    self.css({"cursor": "pointer"})
    if js_funcs is None:
      js_funcs = []
    else:
      if not isinstance(js_funcs, list):
        js_funcs = [js_funcs]
    js_funcs = ["var data = parseInt(event.target.dataset.level)+1",
                self.build(data=JsObjects.JsObjects.get("data"), options=self._jsStyles)] + js_funcs
    str_fncs = JsUtils.jsConvertFncs(js_funcs)
    for span in self._spans:
      span.click(str_fncs, profile, source_event=source_event, on_ready=on_ready)
    return self

  def __str__(self):
    return "<div %s>%s</div>" % (self.get_attrs(css_class_names=self.style.get_classes()), self.helper)


class Help(Html.Html):
  name = 'Info'

  def __init__(self, page: primitives.PageModel, val, width: tuple, profile: Optional[Union[bool, dict]],
               options: Optional[dict]):
    icon_details = page.icons.get("info")
    if icon_details['icon_family'] != 'bootstrap-icons':
      self.requirements = (icon_details['icon_family'],)
    super(Help, self).__init__(page, val, css_attrs={"width": width}, profile=profile)
    self.attr['class'].add(icon_details["icon"])
    self.attr['title'] = val
    self._jsStyles = options

  @property
  def style(self) -> GrpClsLayout.ClassHelp:
    """ Property to the CSS Style of the component. """
    if self._styleObj is None:
      self._styleObj = GrpClsLayout.ClassHelp(self)
    return self._styleObj

  def __str__(self):
    return '<i %s></i>' % self.get_attrs(css_class_names=self.style.get_classes())


class Loading(Html.Html):
  name = 'Loading'

  def __init__(self, page: primitives.PageModel, text: str, color: str, size: tuple, options: Optional[dict],
               profile: Optional[Union[bool, dict]]):
    icon_details = self.page.icons.get("spin")
    if icon_details['icon_family'] != 'bootstrap-icons':
      self.requirements = (icon_details['icon_family'],)
    super(Loading, self).__init__(page, text, profile=profile)
    self.color = self.page.theme.greys[-1] if color is None else color
    self.size = size[0]
    self.css({'color': self.color, 'font-size': "%s%s" % (size[0], size[1]), 'z-index': 5, 'margin': 0})
    self.add_icon("%s fa-spin" % icon_details["icon"], html_code=self.htmlCode,
                  css={"font-size": "%spx" % (self.size+8)}, family=icon_details["icon_family"])
    if options.get('fixed', False):
      self.icon.css({"margin-right": '5px', "font-size": 'inherit'})
      self.css({"position": 'fixed', 'bottom': '0px', 'right': '5px'})
      self.add_span("%s..." % text, position="after", css={"width": 'auto'})
    else:
      self.add_span("%s..." % text, position="after", css={"width": '100%', "margin": "5px"})

  def fixed(self, css: Optional[dict] = None, icon_css: Optional[dict] = None):
    """
    Set css attributes of the loading div to be fixed.

    This can be done directly in options in the component constructor options={"fixed": True}.

    :param css: Optional. The css attributes
    :param icon_css: Optional. The CSS attributes

    :return: self to allow the chains.
    """
    dfl_css = {"position": 'fixed', 'bottom': '5px', 'right': '5px'}
    if css is not None:
      dfl_css.update(css)
    dfl_css_icon = {"margin-right": '5px', "font-size": 'inherit'}
    if icon_css is not None:
      dfl_css_icon.update(icon_css)
    self.icon.css(dfl_css_icon)
    self.css(dfl_css)
    return self

  def __str__(self):
    return '<div %s></div>' % (self.get_attrs(css_class_names=self.style.get_classes()))


class HtmlJson(Html.Html):
  name = 'Pretty Json'
  requirements = ('json-formatter-js', )
  _option_cls = OptJsonFormatter.OptionsJsonFmt

  def __init__(self, page: primitives.PageModel, tree_data, width, height, options, profile):
    super(HtmlJson, self).__init__(page, tree_data, profile=profile, options=options,
                                   css_attrs={"height": height, "width": width})

  @property
  def dom(self) -> JsHtmlJson.JsonFormatter:
    """
    Return all the Javascript functions defined for an HTML Component.

    Those functions will use plain javascript available for a DOM element by default.
    """
    if self._dom is None:
      self._dom = JsHtmlJson.JsonFormatter(self, page=self.page)
    return self._dom

  @property
  def jsonId(self):
    """ Return the Javascript variable of the json object. """
    return "%s_obj" % self.htmlCode

  @property
  def options(self) -> OptJsonFormatter.OptionsJsonFmt:
    """
    Property to the component options.

    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  @property
  def js(self) -> JsJsonFormatter.Json:
    """
    Return the Javascript internal object.

    :return: A Javascript object
    """
    if self._js is None:
      self._js = JsJsonFormatter.Json(page=self.page, js_code=self.jsonId, set_var=False, component=self)
    return self._js

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % (self.get_attrs(css_class_names=self.style.get_classes()))


class Breadcrumb(Html.Html):
  name = 'Breadcrumb'
  _option_cls = OptText.OptBreadCrumb

  def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
    super(Breadcrumb, self).__init__(page, [], profile=profile, options=options, html_code=html_code,
                                     css_attrs={"height": height, "width": width})
    self.style.css.line_height = height[0]
    self.style.css.vertical_align = 'middle'
    self.options.height = height[0]
    if records is not None:
      for rec in records:
        if not hasattr(rec, 'options'):
          if isinstance(rec, dict):
            records = page.ui.div(
              rec['text'], width=("auto", '')) if options['selected'] == rec['text'] else page.ui.link(
              rec['text'], rec['url'])
            records.style.css.vertical_align = 'middle'
          else:
            records = page.ui.div(rec, width=("auto", '')) if options['selected'] == rec else page.ui.link(rec)
            records.style.css.vertical_align = 'middle'
          records.style.css.display = 'inline-block'
        self.add(records)
    self.style.background = page.theme.greys[1]

  @property
  def options(self) -> OptText.OptBreadCrumb:
    """ Property to set all the possible object for a breadcrumb definition. """
    return super().options

  def __add__(self, component: Union[primitives.HtmlModel, str]):
    """ Add items to a container """
    if hasattr(component, 'htmlCode'):
      component.options.managed = False
    self.val.append(component)
    return self

  def __str__(self):
    rows = [component.html() if hasattr(component, 'html') else str(component) for component in self.val]
    return '<div %s>%s</div>' % (self.get_attrs(css_class_names=self.style.get_classes()),
                                 self.options.delimiter.join(rows))


class Legend(Html.Html):
  name = 'Legend'
  _option_cls = OptJsonFormatter.OptionsLegend

  def __init__(self, page: primitives.PageModel, record, width: tuple, height: tuple, options: Optional[dict],
               profile: Optional[Union[dict, bool]]):
    super(Legend, self).__init__(page, record, options=options,
                                 css_attrs={"width": width, "height": height}, profile=profile)

  @property
  def options(self) -> OptJsonFormatter.OptionsLegend:
    """
    Property to the component options.

    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  def __str__(self):
    divs = []
    css_inline = Defaults.inline(self.options.style)
    for val in self.val:
      val["css_inline"] = css_inline
      divs.append("<div><div style='background:%(color)s;%(css_inline)s'></div>%(name)s</div>" % val)
    return '<div %s>%s</div>' % (self.get_attrs(css_class_names=self.style.get_classes()), "".join(divs))


class Slides(Html.Html):
  name = 'Slides'
  _option_cls = OptText.OptionsText

  def __init__(self, page: primitives.PageModel, start, width: tuple, height: tuple, options: Optional[dict],
               profile: Optional[Union[dict, bool]]):
    icon_details_right = self.page.icons.get("arrow_right")
    if icon_details_right['icon_family'] != 'bootstrap-icons':
      self.requirements = (icon_details_right['icon_family'],)
    icon_details_left = self.page.icons.get("arrow_left")
    super(Slides, self).__init__(page, [], options=options,
                                 css_attrs={"width": width, 'height': height}, profile=profile)
    self.attr['data-current_slide'] = start
    self.title = self.page.ui.title("")
    self.title.style.css.border_bottom = "1px solid %s" % page.theme.colors[7]
    self.title.style.css.color = page.theme.colors[7]
    self.title.style.css.margin = 0
    self.title.options.managed = False
    if 'contents' in options:
      del page._content_table

      self._content_table = options['contents']
      self._content_table.style.css.z_index = 100
    if 'timer' in options:
      self.page.ui.calendars.timer(options['timer']).css(
        {"position": 'fixed', "font-size": '15px', 'top': '8px', "padding": '8px', "right": '15px', 'width': 'none',
         'color': page.theme.greys[5]})
    self.next = self.page.ui.icon(icon_details_right["icon"]).css(
      {"position": 'fixed', "font-size": '35px', 'bottom': '0',  "padding": '8px', "right": '10px', 'width': 'none'})
    self.previous = self.page.ui.icon(icon_details_left["icon"]).css(
      {"position": 'fixed', "font-size": '35px', 'bottom': '0',  "padding": '8px', "left": '10px', 'width': 'none'})

    self.page_number = self.page.ui.text("").css(
      {"position": 'fixed', 'z-index': 101, "font-size": '25px', 'bottom': '0',  "padding": '8px', "left": '50%',
       'width': 'none'})

    self.next.click([
      self.page.js.getElementsByName(self.htmlCode).all([data.loops.dom_list.hide()]),
        data.primitives.float(self.dom.attr("data-current_slide").toString().parseFloat().add(1), 'slide_index'),

      self.js.if_(page.js.object('slide_index') <= self.dom.attr('data-last_slide'), [
        self.title.build(self.page.js.getElementsByName(
          self.htmlCode)[page.js.object('slide_index')].attr('data-slide_title')),
        self.dom.attr("data-current_slide", page.js.object('slide_index')),
        self.page.js.getElementsByName(self.htmlCode)[page.js.object('slide_index')].show(display_value='flex'),
        self.page.js.getElementById(
          "%s_count" % self.htmlCode).innerHTML(page.js.object('slide_index').toString().parseFloat().add(1)),
      ]).else_([
        self.title.build(self.page.js.getElementsByName(
          self.htmlCode)[page.js.object('slide_index').add(-1)].attr('data-slide_title')),
        self.page.js.getElementsByName(
          self.htmlCode)[page.js.object('slide_index').add(-1)].show(display_value='flex')]),

      self.js.if_(page.js.object('slide_index') > 0, [self.previous.dom.show()]),
      self.js.if_(page.js.object('slide_index') == self.dom.attr('data-last_slide'), [self.next.dom.hide()])
    ])

    self.previous.click([
      self.page.js.getElementsByName(self.htmlCode).all([data.loops.dom_list.hide()]),
      data.primitives.float(self.dom.attr("data-current_slide").toString().parseFloat().add(-1), 'slide_index'),

      self.js.if_(page.js.object('slide_index') >= 0, [
        self.title.build(self.page.js.getElementsByName(
          self.htmlCode)[page.js.object('slide_index')].attr('data-slide_title')),
        self.dom.attr("data-current_slide", page.js.object('slide_index')),
        self.page.js.getElementsByName(self.htmlCode)[page.js.object('slide_index')].show(display_value='flex'),
        self.page.js.getElementById(
          "%s_count" % self.htmlCode).innerHTML(page.js.object('slide_index').toString().parseFloat().add(1)),
      ]).else_([
        self.title.build(self.page.js.getElementsByName(self.htmlCode)[0].attr('data-slide_title')),
        self.page.js.getElementsByName(self.htmlCode)[0].show(display_value='flex')]),

      self.js.if_(page.js.object('slide_index') == 0, [self.previous.dom.hide()]),
      self.js.if_(page.js.object('slide_index') < self.dom.attr('data-last_slide'), [self.next.dom.show()])
    ])

    # Add the keyboard shortcut
    page.body.keydown.right([self.next.dom.events.trigger("click")])
    page.body.keydown.left([self.previous.dom.events.trigger("click")])

    self.style.css.padding = "0 20px 20px 20px"

  @property
  def options(self) -> OptText.OptionsText:
    """
    Property to the component options.

    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  @property
  def dom(self) -> JsHtmlStars.Slides:
    """
    Return all the Javascript functions defined for an HTML Component.

    Those functions will use plain javascript available for a DOM element by default.
    """
    if self._dom is None:
      self._dom = JsHtmlStars.Slides(component=self, page=self.page)
    return self._dom

  def add(self, component: Union[Html.Html, str]):
    """ Add a component to the slide.

    :param component: The HTML component to be added to this component
    """
    if isinstance(component, list):
      for c in component:
        if hasattr(c, 'options'):
          c.options.managed = False
      component = self.page.ui.div(component)
      component.style.css.width = "100%"
      component.style.css.height = "90%"
      component.style.css.display = "flex"
      component.style.css.padding = 5
      component.style.css.justify_content = "center"
      component.style.css.align_items = "center"
      component.style.css.flex_direction = "column"
    if hasattr(component, 'options'):
      component.options.managed = False
      component.style.css.margin_top = '10px'
      component.style.css.overflow = 'auto'
    self.val.append(component)
    return self

  def add_slide(self, title: str, component: Union[Html.Html, str], options: Optional[dict] = None):
    """
    Add a slide.

    :param title: The title value in the slide
    :param component: The HTML component
    :param options: Optional. The various component options
    """
    self.add(component)
    self.val[-1].attr["data-slide_title"] = title
    if options is not None:
      options.get('contents', self._content_table).anchor(
        options.get('contents_title', title), options.get('contents_level', 0))
      options.get('contents', self._content_table)[-1].click([self.dom.goTo(len(self.val))])
    elif hasattr(self, '_content_table'):
      if options is not None:
        self._content_table.anchor(options.get('contents_title', title), options.get('contents_level', 0))
      else:
        self._content_table.anchor(title)
      self._content_table[-1].click([self.dom.goTo(len(self.val))])
    return self

  def __str__(self):
    self.page.body.style.css.height = '100%'
    self.page_number._vals = '<font id="%s_count" ondblclick="this.contentEditable = true" onkeydown="if (event.keyCode == 13){document.getElementById(\'%s\').setAttribute(\'data-current_slide\', Math.min(parseInt(this.innerHTML), %s) -2); %s; this.contentEditable = false}">%s</font> / %s' % (self.htmlCode, self.htmlCode, len(self.val), self.next.dom.events.trigger('click').toStr(), self.attr['data-current_slide']+1, len(self.val))
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
    return '<div %s>%s%s</div>' % (
      self.get_attrs(css_class_names=self.style.get_classes()), self.title.html(), "".join(comps))


class HtmlQRCode(Html.Html):
  name = 'QR Code'
  requirements = ('qrcodejs', )
  _option_cls = OptQrCode.OptionsQrCode

  def __init__(self, page: primitives.PageModel, record, width: tuple, height: tuple, options: Optional[dict],
               profile: Optional[Union[bool, dict]]):
    super(HtmlQRCode, self).__init__(page, record, profile=profile, options=options,
                                     css_attrs={"height": height, "width": width})
    self.options.width = width[0]
    self.options.height = height[0]

  @property
  def options(self) -> OptQrCode.OptionsQrCode:
    """
    Property to the component options.

    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  @property
  def jsonId(self):
    """ Return the Javascript variable of the json object. """
    return "%s_obj" % self.htmlCode

  @property
  def js(self) -> JsQrCode.QrCode:
    """
    Return the Javascript internal object.

    :return: A Javascript object
    """
    if self._js is None:
      self._js = JsQrCode.QrCode(js_code=self.jsonId, set_var=False, component=self, page=self.page)
    return self._js

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % (self.get_attrs(css_class_names=self.style.get_classes()))


class HtmlCaptcha(Html.Html):
  name = 'Google Catch'
  requirements = ('google-captcha', )

  def __init__(self, page: primitives.PageModel, record, width: tuple, height: tuple, options: Optional[dict],
               profile: Optional[Union[bool, dict]]):
    super(HtmlCaptcha, self).__init__(page, record, profile=profile, options=options,
                                      css_attrs={"height": height, "width": width})
    self.attr["data-callback"] = "onSubmit"
    self.attr["data-action"] = "submit"
    self.style.add_classes.external("g-recaptcha")

  def __str__(self):
    return '<button %s>%s</button>' % (self.get_attrs(css_class_names=self.style.get_classes()), self._vals)
