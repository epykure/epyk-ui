#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlEditor, JsHtml
from epyk.core.js.packages import JsCodeMirror
from epyk.core.html import Html

from epyk.core.html.options import OptCodeMirror
from epyk.core.html.options import OptText

# The list of CSS classes
from epyk.core.css.styles import GrpClsCodeMirror
from epyk.core.css import Defaults as cssDefaults


class Console(Html.Html):
  name = 'Console'
  _option_cls = OptText.OptionsConsole

  def __init__(self, page: primitives.PageModel, data: Union[str, list], width: tuple, height: tuple, html_code: Optional[str],
               helper: Optional[str], options: Optional[dict], profile: Optional[Union[dict, bool]]):
    super(Console, self).__init__(page, data, html_code=html_code, options=options,
                                  css_attrs={"width": width, "height": height}, profile=profile)
    self.css({"overflow": 'auto', 'box-sizing': 'border-box', 'color': self.page.theme.greys[-1],
              'background': self.page.theme.colors[0]})
    self.add_helper(helper)

  @property
  def dom(self) -> JsHtmlEditor.Console:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlEditor.Console
    """
    if self._dom is None:
      self._dom = JsHtmlEditor.Console(self, page=self.page)
    return self._dom

  @property
  def options(self) -> OptText.OptionsConsole:
    """
    Description:
    ------------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptText.OptionsConsole
    """
    return super().options

  _js__builder__ = ''' 
      if(options.showdown){var converter = new showdown.Converter(options.showdown);
        converter.setOption("display", "inline-block");
        data = converter.makeHtml(data).replace("<p>", "<p style='display:inline-block;margin:0'>")}
      htmlObj.innerHTML = data +'<br/>' '''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<div %s></div>%s" % (self.get_attrs(css_class_names=self.style.get_classes()), self.helper)


class Editor(Html.Html):
  name = 'Code Editor'
  requirements = ('codemirror', )

  def __init__(self, page: primitives.PageModel, vals, language, width, height, html_code, options, profile):
    super(Editor, self).__init__(page, vals, html_code=html_code, profile=profile,
                                 css_attrs={"width": width, "height": height, 'box-sizing': 'border-box',
                                            'margin': '5px 0'})
    self.textarea = self.page.ui.texts.code(vals, height=height, language=language, options=options)
    self.textarea.options.managed = False
    self.actions = []

  @property
  def dom(self) -> JsHtmlEditor.Editor:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlEditor.Editor
    """
    if self._dom is None:
      self._dom = JsHtmlEditor.Editor(self, page=self.page)
    return self._dom

  def action(self, icon: str, js_funcs: Union[list, str], tooltip: Optional[str] = None):
    """
    Description:
    ------------
    Add a bespoke action to the action panel.

    Attributes:
    ----------
    :param str icon: The font awesome icon.
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[str] tooltip: Optional. Text to be displayed when mouse is hover.
    """
    icon_button = self.page.ui.icon(icon, tooltip=tooltip).css({"margin-right": '5px'}).click(js_funcs)
    self.actions.append((icon, icon_button))
    icon_button.options.managed = False
    return self

  def toggle(self, js_funcs: Union[list, str], icons: tuple = ("show", "hide"), tooltip: Optional[str] = None):
    """
    Description:
    ------------
    Add an event action to the console object.

    Attributes:
    ----------
    :param tuple icons: The font awesome icon.
    :param Union[list, str] js_funcs: Optional. The Javascript functions.
    :param Optional[str] tooltip: Optional. Text to be displayed when mouse is hover.
    """
    icon_button = self.page.ui.icon(icons[0], tooltip=tooltip).css({"margin-right": '5px'})
    js_funcs.append(self.textarea.dom.toggle())
    js_funcs.append(icon_button.dom.switchClass(icons[0], icons[1]).r)
    icon_button.click(js_funcs)
    icon_button.options.managed = False
    self.actions.append((icons[0], icon_button))
    return self

  def copy(self, js_funcs: Union[list, str], icon: str = "capture", tooltip: Optional[str] = None):
    """
    Description:
    ------------
    Copy the content of the editor component to the clipboard.

    Attributes:
    ----------
    :param str icon: The font awesome icon.
    :param Union[list, str] js_funcs: Optional. The Javascript functions.
    :param Optional[str] tooltip: Optional. Text to be displayed when mouse is hover.
    """
    js_funcs.append(self.textarea.dom.select())
    js_funcs.append('document.execCommand("copy")')
    return self.action(icon, js_funcs, tooltip)

  def run(self, js_funcs: Union[list, str], icon: str = "play", tooltip: Optional[str] = None):
    """
    Description:
    ------------
    Emtpy run button.
    This function will just add the icon on the actions panel.

    Attributes:
    ----------
    :param str icon: The font awesome icon.
    :param Union[list, str] js_funcs: Optional. The Javascript functions.
    :param Optional[str] tooltip: Optional. Text to be displayed when mouse is hover.
    """
    return self.action(icon, js_funcs, tooltip)

  def save(self, js_funcs: Union[list, str], icon: str = "save", tooltip: Optional[str] = None):
    """
    Description:
    ------------
    Emtpy save button.
    This function will just add the icon on the actions panel.

    Attributes:
    ----------
    :param str icon: The font awesome icon.
    :param Union[list, str] js_funcs: Optional. The Javascript functions.
    :param Optional[str] tooltip: Optional. Text to be displayed when mouse is hover.
    """
    return self.action(icon, js_funcs, tooltip)

  def clear(self, js_funcs: Union[list, str], icon: str = "remove", tooltip: Optional[str] = None):
    """
    Description:
    ------------
    Add an event action to the console object.

    Attributes:
    ----------
    :param str icon: The font awesome icon.
    :param Union[list, str] js_funcs: Optional. The Javascript functions.
    :param Optional[str] tooltip: Optional. Text to be displayed when mouse is hover.
    """
    js_funcs.append(self.textarea.dom.clear())
    return self.action(icon, js_funcs, tooltip)

  def __str__(self):
    actions = "".join([b.html() for _, b in self.actions])
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return '''
        <div %(attr)s>%(actions)s
          <span style="display:inline-block;float:right;margin-right:5px;font-style:italic">%(timestamp)s</span>
        </div> 
        %(textarea)s''' % {'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'timestamp': timestamp,
                           "textarea": self.textarea.html(), 'actions': actions}


class Cell(Html.Html):
  name = 'Python Cell Runner'
  requirements = ('codemirror', )

  def __init__(self, page: primitives.PageModel, vals: Union[list, str], language: str, width: tuple, height: tuple,
               html_code: Optional[str], options: Optional[dict], profile: Optional[Union[dict, bool]]):
    super(Cell, self).__init__(page, vals, html_code=html_code, options=options,
                               css_attrs={"width": width, "height": height}, profile=profile)
    self.textarea = self.page.ui.texts.code(vals, language, height=height, options=options)
    self.textarea.options.managed = False
    self.textarea.style.add_classes.input.textarea()
    self.textarea.style.add_classes.input.textarea()
    self._jsRun, self._jsSave = '', ''
    self.css({'padding': '10px', "min-height": "30px", 'box-sizing': 'border-box', 'display': 'inline-block'})
    self.actions = []

  def action(self, icon: str, js_funcs: Union[list, str], tooltip: Optional[str] = None):
    """
    Description:
    ------------
    Add a bespoke action to the action panel.

    Attributes:
    ----------
    :param str icon: The font awesome icon.
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[str] tooltip: Optional. Text to be displayed when mouse is hover.
    """
    icon_button = self.page.ui.icon(icon, tooltip=tooltip).css({"margin-right": '5px'}).click(js_funcs)
    self.actions.append((icon, icon_button))
    icon_button.options.managed = False

  def run(self, js_funcs: Union[list, str], icon: str = "play", tooltip: Optional[str] = None):
    """
    Description:
    ------------
    Emtpy run button.
    This function will just add the icon on the actions panel.

    Attributes:
    ----------
    :param str icon: The font awesome icon.
    :param Union[list, str] js_funcs: Optional. The Javascript functions.
    :param Optional[str] tooltip: Optional. Text to be displayed when mouse is hover.
    """
    js_funcs.append(self.dom.querySelector("span").innerHTML(1, append=True, val_type=int))
    return self.action(icon, js_funcs, tooltip)

  def save(self, js_funcs: Union[list, str], icon: str = "save", tooltip: Optional[str] = None):
    """
    Description:
    ------------
    Emtpy save button.
    This function will just add the icon on the actions panel.

    Attributes:
    ----------
    :param str icon: The font awesome icon.
    :param Union[list, str] js_funcs: Optional. The Javascript functions.
    :param Optional[str] tooltip: Optional. Text to be displayed when mouse is hover.
    """
    return self.action(icon, js_funcs, tooltip)

  def __str__(self):
    actions = "".join([b.html() for _, b in self.actions])
    return '''
      <div %(attrs)s>
          <div style="padding:10px 5px;float:left;width:50px;height:100%%;vertical-align:middle">
            In [ <span data=count=0 style="display:inline-block;margin-bottom:5px">0</span> ]<br/>%(actions)s
          </div>
          %(textarea)s
      </div>''' % {'attrs': self.get_attrs(css_class_names=self.style.get_classes()),
                   'actions': actions, "textarea": self.textarea.html()}


class Code(Html.Html):
  name = 'Code'
  requirements = ('codemirror', )
  _option_cls = OptCodeMirror.OptionsCode

  def __init__(self, page: primitives.PageModel, vals: str, color: str, width: tuple, height: tuple,
               html_code: Optional[str], options: Optional[dict], helper: str, profile: Optional[Union[dict, bool]]):
    super(Code, self).__init__(page, vals, html_code=html_code, options=options,
                               css_attrs={"width": width, "height": height, "color": color}, profile=profile)
    self.add_helper(helper)
    self.css({'display': 'block', 'margin': '5px 0'})

  @property
  def style(self) -> GrpClsCodeMirror.Code:
    """
    Description:
    ------------
    Property to the Style property of the component.

    :rtype: GrpClsCodeMirror.Code
    """
    if self._styleObj is None:
      self._styleObj = GrpClsCodeMirror.Code(self)
    return self._styleObj

  @property
  def options(self) -> OptCodeMirror.OptionsCode:
    """
    Description:
    ------------
    Property to set all the possible object for a button.

    :rtype: OptCodeMirror.OptionsCode
    """
    return super().options

  @property
  def js(self) -> JsCodeMirror.CM:
    """
    Description:
    -----------
    A lot of CodeMirror features are only available through its API.
    Thus, you need to write code (or use add-ons) if you want to expose them to your users.

    Related Pages:

      https://codemirror.net/doc/manual.html#api

    :rtype: JsCodeMirror.CM
    """
    if self._js is None:
      self._js = JsCodeMirror.CM(self, page=self.page)
    return self._js

  @property
  def dom(self) -> JsHtmlEditor.CodeMirror:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlEditor.CodeMirror
    """
    if self._dom is None:
      self._dom = JsHtmlEditor.CodeMirror(self, page=self.page)
    return self._dom

  @property
  def addon(self):
    """
    Description:
    ------------
    The add-on directory in the distribution contains a number of reusable components that implement extra
    editor functionality.

    Related Pages:

      https://codemirror.net/doc/manual.html#addons
    """
    return self.options.addons

  def placeholder(self, text: str):
    """
    Description:
    ------------
    Adds a placeholder option that can be used to make content appear in the editor when it is empty and not focused.

    Attributes:
    ----------
    :param str text: The text displayed if empty editor.
    """
    self.options.addons.placeholder()
    self.attr["placeholder"] = text
    return self

  def build(self, data=None, options: Optional[dict] = None, profile: Optional[Union[bool, dict]] = None,
            component_id: Optional[str] = None):
    """
    Description:
    ------------
    This is a specific version of the common build as the function is not applied to the dom ID but
    the HTML code set as a proper global variable on the JavaScript side.

    Attributes:
    ----------
    :param data: String. Optional. The component input data.
    :param Optional[dict] options: Optional. Specific Python options available for this component.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] component_id:
    """
    return super().build(data, options, profile, component_id=self.htmlCode)

    # if not self.builder_name or self._js__builder__ is None:
    #   raise Exception("No builder defined for this HTML component %s" % self.__class__.__name__)
    #
    # self.page.properties.js.add_constructor(self.builder_name, "function %s(htmlObj, data, options){%s}" % (
    #   self.builder_name, self._js__builder__))
    # self.options.builder = self.builder_name
    #
    # # check if there is no nested HTML components in the data
    # if isinstance(data, dict):
    #   tmp_data = ["%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)) for k, v in data.items()]
    #   js_data = "{%s}" % ",".join(tmp_data)
    # else:
    #   js_data = JsUtils.jsConvertData(data, None)
    # fnc_call = "%s(%s, %s, %s)" % (self.builder_name, self.htmlCode, js_data, self.options.config_js(options))
    # profile = self.with_profile(profile, event="Builder")
    # if profile:
    #   fnc_call = JsUtils.jsConvertFncs(
    #     ["var result = %s(htmlObj, data, options)" % fnc_call], toStr=True, profile=profile)
    #   fnc_call = "(function(htmlObj, data, options){%s; return result})" % fnc_call
    # return fnc_call

  _js__builder__ = ''' 
       var editor_alias = "editor_"+ htmlObj.id;
       if (typeof window[editor_alias] === 'undefined'){
          window[editor_alias] = CodeMirror.fromTextArea(htmlObj, options)}
       window[editor_alias].setValue(data); 
       Object.keys(options).forEach(
          function(key){ window[editor_alias].setOption(key, options[key])})
       '''

  @property
  def editorId(self):
    """
    Description:
    ------------
    Return the Javascript variable of the bespoke.
    """
    return "editor_%s" % self.htmlCode

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    self.page.body.onReady(
      'window["%(editor)s"].setSize("%(width)s", "%(height)s"); window["%(editor)s"].refresh()' % {
        "editor": self.editorId, "width": self.css("width"), "height": self.css("height")})
    return '<textarea %s></textarea>%s' % (self.get_attrs(css_class_names=self.style.get_classes()), self.helper)


class Tags(Html.Html):
  name = 'Tags'

  def __init__(self, page: primitives.PageModel, vals: list, title: str, icon: str, size: tuple, width: tuple,
               height: tuple, html_code: Optional[str], profile: Optional[Union[bool, dict]]):
    super(Tags, self).__init__(page, vals, css_attrs={"width": width, "height": height},
                               html_code=html_code, profile=profile)
    self.title, self.icon = title, icon
    self.css({"margin-top": "5px", "font-size": "%s%s" % (size[0], size[1]),
              "font-family": page.style.defaults.font.family})

  @property
  def val(self):
    """
    Description:
    ------------

    """
    return "%(breadCrumVar)s['params']['%(htmlCode)s']" % {
      "htmlCode": self.htmlCode, "breadCrumVar": self.page.jsGlobal.breadCrumVar}

  def jsEmpty(self):
    """
    Description:
    ------------

    """
    return "%(breadCrumVar)s['params']['%(htmlCode)s'] = []; $('#%(htmlCode)s_tags').text('')" % {
      "htmlCode": self.htmlCode, "breadCrumVar": self.page.jsGlobal.breadCrumVar}

  def jsAdd(self, data):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    """
    data = JsUtils.jsConvertData(data, None)
    icon_details = cssDefaults.get_icon("close")
    self.page.properties.js.add_builders('RemoveSelection(srcObj, htmlCode)', 'srcObj.parent().remove()',
       func_dsc="Remove the item from the Tags Html component but also from the underlying javascript variable")
    return '''
      $('#%(htmlCode)s_tags').append("<span style='margin:2px;background:%(baseColor)s;color:%(whiteColor)s;border-radius:8px;1em;vertical-align:middle;display:inline-block;padding:0 2px 1px 10px;cursor:pointer'>"+ %(jsData)s +"<i onclick='RemoveSelection($(this), \\\"%(htmlCode)s\\\")' style='margin-left:10px' class='%(close)s'></i></span>")
      ''' % {"htmlCode": self.htmlCode, "jsData": data, 'whiteColor': self.page.theme.greys[0],
             "baseColor": self.page.theme.colors[9], "close": icon_details["icon"]}

  def __str__(self):
    return '''
      <div %(attr)s>
        <div style='margin:0;display:inline-block;vertical-align:middle;width:90px;float:left;padding:2px 5px 0 5px;height:30px;border:1px solid %(greyColor)s'>
          <i class="%(icon)s" style="margin-right:10px"></i>%(title)s</div>
        <div id='%(htmlCode)s_tags' style='padding:2px 5px 0 5px;border:1px solid %(greyColor)s;height:30px'></div>
      </div>''' % {"attr": self.get_attrs(css_class_names=self.style.get_classes()), "title": self.title,
                   'icon': self.icon, 'htmlCode': self.htmlCode, 'greyColor': self.page.theme.greys[2]}


class MarkdownReader(Html.Html):
  name = 'markdown'
  requirements = ('highlight.js', 'showdown')
  _option_cls = OptText.OptionsText

  def __init__(self, page: primitives.PageModel, vals: Union[str, list], width: tuple, height: tuple, html_code: Optional[str],
               options: Optional[dict], profile: Optional[Union[bool, dict]]):
    super(MarkdownReader, self).__init__(page, vals, html_code=html_code, profile=profile, options=options,
                                         css_attrs={"width": width, "height": height, 'box-sizing': 'border-box'})
    self.actions = []

  @property
  def dom(self) -> JsHtml.JsHtmlRich:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript available for a DOM element by default.

    Usage::

      div = page.ui.div(htmlCode="testDiv")
      print(div.dom.content)

    :return: A Javascript Dom object.

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, page=self.page)
    return self._dom

  @property
  def options(self) -> OptText.OptionsText:
    """
    Description:
    ------------
    Property to set all the input TimePicker component properties.

    Related Pages:

      https://timepicker.co/options/

    :rtype: OptText.OptionsText
    """
    return super().options

  def tooltips(self, data):
    """
    Description:
    ------------
    Add automatically tooltips to the words.

    Attributes:
    ----------
    :param data: Dictionary. The list of word to be automatically changed.
    """
    from epyk.core.data import components

    if "markdown_tooltip" not in self.page.components:
      div = self.page.ui.div(html_code="markdown_tooltip", width=("auto", ""))
      div.style.css.display = False
      div.style.css.position = "absolute"
      div.style.css.background = self.page.theme.greys[0]
      div.style.css.padding = 5
      div.style.css.border_radius = 5
      div.style.css.border = "1px solid %s" % self.page.theme.greys[5]
      self.onReady('''
        function showTooltip(source, content){
            source.style.cursor = 'help'; document.querySelector('#markdown_tooltip').innerHTML = content;  
            document.querySelector('#markdown_tooltip').style.left = event.pageX + 15 + 'px'; 
            document.querySelector('#markdown_tooltip').style.top = event.pageY + 5 + 'px';
            document.querySelector('#markdown_tooltip').style.display = 'block'; 
            document.querySelector('#markdown_tooltip').style.position = 'absolute'}
        function hideTooltip(){ document.querySelector('#markdown_tooltip').style.display = 'none' }
      ''')
    self._vals = components.markdown(self._vals, data)

  _js__builder__ = '''
      if (data !== ''){ 
        var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data); htmlObj.innerHTML = data;
        document.querySelectorAll('pre code').forEach((block) => {hljs.highlightBlock(block)});
      }'''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '''<div %(attr)s></div> ''' % {'attr': self.get_attrs(css_class_names=self.style.get_classes())}
