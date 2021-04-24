#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlEditor, JsHtml
from epyk.core.js.packages import JsCodeMirror
from epyk.core.html import Html

from epyk.core.html.options import OptCodeMirror
from epyk.core.html.options import OptText

# The list of CSS classes
from epyk.core.css.styles import GrpClsCodeMirror


class Console(Html.Html):
  name = 'Console'
  _option_cls = OptText.OptionsConsole

  def __init__(self, report, data, width, height, html_code, helper, options, profile):
    super(Console, self).__init__(report, data, html_code=html_code, options=options,
                                  css_attrs={"width": width, "height": height}, profile=profile)
    self.css({"overflow": 'auto', 'box-sizing': 'border-box', 'color': self._report.theme.greys[-1],
              'background': self._report.theme.colors[0]})
    self.add_helper(helper)

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtmlEditor.Console
    """
    if self._dom is None:
      self._dom = JsHtmlEditor.Console(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    Usage:
    -----

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
    return "<div %s></div>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class Editor(Html.Html):
  name = 'Code Editor'
  requirements = ('codemirror', 'font-awesome')

  def __init__(self, report, vals, language, width, height, html_code, options, profile):
    super(Editor, self).__init__(report, vals, html_code=html_code, profile=profile,
                                 css_attrs={"width": width, "height": height, 'box-sizing': 'border-box',
                                            'margin': '5px 0'})
    self.textarea = self._report.ui.texts.code(vals, height=height, language=language, options=options)
    self.textarea.options.managed = False
    self.actions = []

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtmlEditor.Editor
    """
    if self._dom is None:
      self._dom = JsHtmlEditor.Editor(self, report=self._report)
    return self._dom

  def action(self, icon, js_funcs, tooltip=None):
    """
    Description:
    ------------
    Add a bespoke action to the action panel.

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. The font awesome icon.
    :param js_funcs: List | String. The Javascript functions.
    :param tooltip: String. Optional. Text to be displayed when mouse is hover.
    """
    icon_button = self._report.ui.icon(icon, tooltip=tooltip).css({"margin-right": '5px'}).click(js_funcs)
    self.actions.append((icon, icon_button))
    icon_button.options.managed = False
    return self

  def toggle(self, js_funcs, icons=("fas fa-eye", "far fa-eye-slash"), tooltip=None):
    """
    Description:
    ------------
    Add an event action to the console object.

    Usage:
    -----

    Attributes:
    ----------
    :param icons: Tuple. The font awesome icon.
    :param js_funcs: List | String. Optional. The Javascript functions.
    :param tooltip: String. Optional. Text to be displayed when mouse is hover.
    """
    icon_button = self._report.ui.icon(icons[0], tooltip=tooltip).css({"margin-right": '5px'})
    js_funcs.append(self.textarea.dom.toggle())
    js_funcs.append(icon_button.dom.switchClass(icons[0], icons[1]).r)
    icon_button.click(js_funcs)
    icon_button.options.managed = False
    self.actions.append((icons[0], icon_button))
    return self

  def copy(self, js_funcs, icon="far fa-clipboard", tooltip=None):
    """
    Description:
    ------------
    Copy the content of the editor component to the clipboard.

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. The font awesome icon.
    :param js_funcs: List | String. Optional. The Javascript functions.
    :param tooltip: String. Optional. Text to be displayed when mouse is hover.
    """
    js_funcs.append(self.textarea.dom.select())
    js_funcs.append('document.execCommand("copy")')
    return self.action(icon, js_funcs, tooltip)

  def run(self, js_funcs, icon="fas fa-play", tooltip=None):
    """
    Description:
    ------------
    Emtpy run button.
    This function will just add the icon on the actions panel.

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. The font awesome icon.
    :param js_funcs: List | String. Optional. The Javascript functions.
    :param tooltip: String. Optional. Text to be displayed when mouse is hover.
    """
    return self.action(icon, js_funcs, tooltip)

  def save(self, js_funcs, icon="fas fa-save", tooltip=None):
    """
    Description:
    ------------
    Emtpy save button.
    This function will just add the icon on the actions panel.

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. The font awesome icon.
    :param js_funcs: List | String. Optional. The Javascript functions.
    :param tooltip: String. Optional. Text to be displayed when mouse is hover.
    """
    return self.action(icon, js_funcs, tooltip)

  def clear(self, js_funcs, icon="fas fa-times-circle", tooltip=None):
    """
    Description:
    ------------
    Add an event action to the console object.

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. The font awesome icon.
    :param js_funcs: List | String. Optional. The Javascript functions.
    :param tooltip: String. Optional. Text to be displayed when mouse is hover.
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
        %(textarea)s''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'timestamp': timestamp,
                           "textarea": self.textarea.html(), 'actions': actions}


class Cell(Html.Html):
  name = 'Python Cell Runner'
  requirements = ('codemirror', )

  def __init__(self, report, vals, language, width, height, html_code, options, profile):
    super(Cell, self).__init__(report, vals, html_code=html_code, options=options,
                               css_attrs={"width": width, "height": height}, profile=profile)
    self.textarea = self._report.ui.texts.code(vals, language, height=height, options=options)
    self.textarea.options.managed = False
    self.textarea.style.add_classes.input.textarea()
    self.textarea.style.add_classes.input.textarea()
    self._jsRun, self._jsSave = '', ''
    self.css({'padding': '10px', "min-height": "30px", 'box-sizing': 'border-box', 'display': 'inline-block'})
    self.actions = []

  def action(self, icon, js_funcs, tooltip=None):
    """
    Description:
    ------------
    Add a bespoke action to the action panel.

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. The font awesome icon.
    :param js_funcs: List | String. The Javascript functions.
    :param tooltip: String. Optional. Text to be displayed when mouse is hover.
    """
    icon_button = self._report.ui.icon(icon, tooltip=tooltip).css({"margin-right": '5px'}).click(js_funcs)
    self.actions.append((icon, icon_button))
    icon_button.options.managed = False

  def run(self, js_funcs, icon="fas fa-play", tooltip=None):
    """
    Description:
    ------------
    Emtpy run button.
    This function will just add the icon on the actions panel.

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. The font awesome icon.
    :param js_funcs: List | String. Optional. The Javascript functions.
    :param tooltip: String. Optional. Text to be displayed when mouse is hover.
    """
    js_funcs.append(self.dom.querySelector("span").innerHTML(1, append=True, valType=int))
    return self.action(icon, js_funcs, tooltip)

  def save(self, js_funcs, icon="fas fa-save", tooltip=None):
    """
    Description:
    ------------
    Emtpy save button.
    This function will just add the icon on the actions panel.

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. The font awesome icon.
    :param js_funcs: List | String. Optional. The Javascript functions.
    :param tooltip: String. Optional. Text to be displayed when mouse is hover.
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
      </div>''' % {'attrs': self.get_attrs(pyClassNames=self.style.get_classes()),
                   'actions': actions, "textarea": self.textarea.html()}


class Code(Html.Html):
  name = 'Code'
  requirements = ('codemirror', )
  _option_cls = OptCodeMirror.OptionsCode

  def __init__(self, report, vals, color, width, height, html_code, options, helper, profile):
    super(Code, self).__init__(report, vals, html_code=html_code, options=options,
                               css_attrs={"width": width, "height": height, "color": color}, profile=profile)
    self.add_helper(helper)
    self.css({'display': 'block', 'margin': '5px 0'})

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the Style property of the component.

    Usage:
    -----

    :rtype: GrpClsCodeMirror.Code
    """
    if self._styleObj is None:
      self._styleObj = GrpClsCodeMirror.Code(self)
    return self._styleObj

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button.

    Usage:
    -----

    :rtype: OptCodeMirror.OptionsCode
    """
    return super().options

  @property
  def js(self):
    """
    Description:
    -----------
    A lot of CodeMirror features are only available through its API.
    Thus, you need to write code (or use add-ons) if you want to expose them to your users.

    Usage:
    -----

    Related Pages:

      https://codemirror.net/doc/manual.html#api

    :rtype: JsCodeMirror.CM
    """
    if self._js is None:
      self._js = JsCodeMirror.CM(self, report=self._report)
    return self._js

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtmlEditor.CodeMirror
    """
    if self._dom is None:
      self._dom = JsHtmlEditor.CodeMirror(self, report=self._report)
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

  def placeholder(self, text):
    """
    Description:
    ------------
    Adds a placeholder option that can be used to make content appear in the editor when it is empty and not focused.

    Attributes:
    ----------
    :param text: String. The text displayed if empty editor.
    """
    self.options.addons.placeholder()
    self.attr["placeholder"] = text
    return self

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Description:
    ------------
    This is a specific version of the common build as the function is not applied to the dom ID but
    the HTML code set as a proper global variable on the JavaScript side.

    Attributes:
    ----------
    :param data: String. Optional. The component input data.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id:
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

    Usage:
    -----

    """
    return "editor_%s" % self.htmlCode

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    self.page.body.onReady(
      'window["%(editor)s"].setSize("%(width)s", "%(height)s"); window["%(editor)s"].refresh()' % {
        "editor": self.editorId, "width": self.css("width"), "height": self.css("width")})
    return '<textarea %s></textarea>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class Tags(Html.Html):
  name = 'Tags'

  def __init__(self, report, vals, title, icon, size, width, height, html_code, profile):
    super(Tags, self).__init__(report, vals, css_attrs={"width": width, "height": height},
                               html_code=html_code, profile=profile)
    self.title, self.icon = title, icon
    self.css({"margin-top": "5px", "font-size": "%s%s" % (size[0], size[1]),
              "font-family": report.style.defaults.font.family})

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return "%(breadCrumVar)s['params']['%(htmlCode)s']" % {
      "htmlCode": self.htmlCode, "breadCrumVar": self._report.jsGlobal.breadCrumVar}

  def jsEmpty(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return "%(breadCrumVar)s['params']['%(htmlCode)s'] = []; $('#%(htmlCode)s_tags').text('')" % {
      "htmlCode": self.htmlCode, "breadCrumVar": self._report.jsGlobal.breadCrumVar}

  def jsAdd(self, jsData):

    jsData = JsUtils.jsConvertData(jsData, None)
    self.addGlobalFnc('RemoveSelection(srcObj, htmlCode)', 'srcObj.parent().remove()',
       fncDsc="Remove the item from the Tags Html component but also from the underlying javascript variable")
    return '''
      $('#%(htmlCode)s_tags').append("<span style='margin:2px;background:%(baseColor)s;color:%(whiteColor)s;border-radius:8px;1em;vertical-align:middle;display:inline-block;padding:0 2px 1px 10px;cursor:pointer'>"+ %(jsData)s +"<i onclick='RemoveSelection($(this), \\\"%(htmlCode)s\\\")' style='margin-left:10px' class='far fa-times-circle'></i></span>")
      ''' % {"htmlCode": self.htmlCode, "jsData": jsData, 'whiteColor': self._report.theme.greys[0],
             "baseColor": self._report.theme.colors[9]}

  def __str__(self):
    return '''
      <div %(attr)s>
        <div style='margin:0;display:inline-block;vertical-align:middle;width:90px;float:left;padding:2px 5px 0 5px;height:30px;border:1px solid %(greyColor)s'>
          <i class="%(icon)s" style="margin-right:10px"></i>%(title)s</div>
        <div id='%(htmlCode)s_tags' style='padding:2px 5px 0 5px;border:1px solid %(greyColor)s;height:30px'></div>
      </div>''' % {"attr": self.get_attrs(pyClassNames=self.style.get_classes()), "title": self.title,
                   'icon': self.icon, 'htmlCode': self.htmlCode, 'greyColor': self._report.theme.greys[2]}


class MarkdownReader(Html.Html):
  name = 'markdown'
  requirements = ('highlight.js', 'showdown')
  _option_cls = OptText.OptionsText

  def __init__(self, report, vals, width, height, html_code, options, profile):
    super(MarkdownReader, self).__init__(report, vals, html_code=html_code, profile=profile, options=options,
                                         css_attrs={"width": width, "height": height, 'box-sizing': 'border-box'})
    self.actions = []

  @property
  def dom(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript available for a DOM element by default.

    Usage:
    -----

      div = page.ui.div(htmlCode="testDiv")
      print(div.dom.content)

    :return: A Javascript Dom object.

    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the input TimePicker component properties.

    Usage:
    -----

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

    Usage:
    -----

    Attributes:
    ----------
    :param data: Dictionary. The list of word to be automatically changed.
    """
    from epyk.core.data import components

    if "markdown_tooltip" not in self._report.components:
      div = self._report.ui.div(html_code="markdown_tooltip", width=("auto", ""))
      div.style.css.display = False
      div.style.css.position = "absolute"
      div.style.css.background = self._report.theme.greys[0]
      div.style.css.padding = 5
      div.style.css.border_radius = 5
      div.style.css.border = "1px solid %s" % self._report.theme.greys[5]
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
    return '''<div %(attr)s></div> ''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes())}
