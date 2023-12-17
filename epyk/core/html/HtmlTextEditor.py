#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from typing import Union, Optional, List
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlEditor, JsHtml
from epyk.core.js.packages import JsCodeMirror
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState

from epyk.core.html.options import OptCodeMirror
from epyk.core.html.options import OptText

# The list of CSS classes
from epyk.core.css.styles import GrpClsCodeMirror


class Console(Html.Html):
    name = 'Console'
    _option_cls = OptText.OptionsConsole
    tag = "div"

    def __init__(self, page: primitives.PageModel, data: Union[str, list], width: tuple, height: tuple,
                 html_code: Optional[str],
                 helper: Optional[str], options: Optional[dict], profile: Optional[Union[dict, bool]],
                 verbose: bool = False):
        super(Console, self).__init__(page, data, html_code=html_code, options=options,
                                      css_attrs={"width": width, "height": height}, profile=profile, verbose=verbose)
        self.css({"overflow": 'auto', 'box-sizing': 'border-box', 'color': self.page.theme.greys[-1],
                  'background': self.page.theme.colors[0]})
        self.add_helper(helper)

    @property
    def dom(self) -> JsHtmlEditor.Console:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.
        """
        if self._dom is None:
            self._dom = JsHtmlEditor.Console(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptText.OptionsConsole:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    _js__builder__ = '''if(options.showdown){var converter = new showdown.Converter(options.showdown);
  converter.setOption("display", "inline-block");
  data = converter.makeHtml(data).replace("<p>", "<p style='display:inline-block;margin:0'>")}
htmlObj.innerHTML = data +'<br/>' '''

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return "<%s %s></%s>%s" % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag, self.helper)


class Editor(Html.Html):
    name = 'Code Editor'
    requirements = ('codemirror',)

    def __init__(self, page: primitives.PageModel, vals, language, width, height, html_code, options, profile,
                 verbose: bool = False):
        super(Editor, self).__init__(page, vals, html_code=html_code, profile=profile,
                                     css_attrs={"width": width, "height": height, 'box-sizing': 'border-box',
                                                'margin': '5px 0'}, verbose=verbose)
        self.textarea = self.page.ui.texts.code(vals, height=height, language=language, options=options)
        self.textarea.options.managed = False
        self.actions = []

    @property
    def dom(self) -> JsHtmlEditor.Editor:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.
        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlEditor.Editor(self, page=self.page)
        return self._dom

    def action(self, icon: str, js_funcs: Union[list, str], tooltip: Optional[str] = None):
        """Add a bespoke action to the action panel.

        :param icon: The font awesome icon
        :param js_funcs: The Javascript functions
        :param tooltip: Optional. Text to be displayed when mouse is hover
        """
        icon_button = self.page.ui.icon(icon, tooltip=tooltip).css({"margin-right": '5px'}).click(js_funcs)
        self.actions.append((icon, icon_button))
        icon_button.options.managed = False
        return self

    def toggle(self, js_funcs: Union[list, str], icons: tuple = ("show", "hide"), tooltip: Optional[str] = None):
        """Add an event action to the console object.

        :param icons: The font awesome icon
        :param js_funcs: Optional. The Javascript functions
        :param tooltip: Optional. Text to be displayed when mouse is hover
        """
        icon_button = self.page.ui.icon(icons[0], tooltip=tooltip).css({"margin-right": '5px'})
        js_funcs.append(self.textarea.dom.toggle())
        js_funcs.append(icon_button.dom.switchClass(icons[0], icons[1]).r)
        icon_button.click(js_funcs)
        icon_button.options.managed = False
        self.actions.append((icons[0], icon_button))
        return self

    def copy(self, js_funcs: Union[list, str], icon: str = "capture", tooltip: Optional[str] = None):
        """Copy the content of the editor component to the clipboard.

        :param icon: The font awesome icon
        :param js_funcs: Optional. The Javascript functions
        :param tooltip: Optional. Text to be displayed when mouse is hover
        """
        js_funcs.append(self.textarea.dom.select())
        js_funcs.append('document.execCommand("copy")')
        return self.action(icon, js_funcs, tooltip)

    def run(self, js_funcs: Union[list, str], icon: str = "play", tooltip: Optional[str] = None):
        """Emtpy run button.
        This function will just add the icon on the actions panel.

        :param icon: The font awesome icon
        :param js_funcs: Optional. The Javascript functions
        :param tooltip: Optional. Text to be displayed when mouse is hover
        """
        return self.action(icon, js_funcs, tooltip)

    def save(self, js_funcs: Union[list, str], icon: str = "save", tooltip: Optional[str] = None):
        """Emtpy save button.
        This function will just add the icon on the actions panel.

        :param icon: The font awesome icon
        :param js_funcs: Optional. The Javascript functions
        :param tooltip: Optional. Text to be displayed when mouse is hover
        """
        return self.action(icon, js_funcs, tooltip)

    def clear(self, js_funcs: Union[list, str], icon: str = "remove", tooltip: Optional[str] = None):
        """Add an event action to the console object.

        :param icon: The font awesome icon
        :param js_funcs: Optional. The Javascript functions
        :param tooltip: Optional. Text to be displayed when mouse is hover
        """
        js_funcs.append(self.textarea.dom.clear())
        return self.action(icon, js_funcs, tooltip)

    def __str__(self):
        actions = "".join([b.html() for _, b in self.actions])
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return '''<div %(attr)s>%(actions)s
  <span style="display:inline-block;float:right;margin-right:5px;font-style:italic">%(timestamp)s</span>
</div>%(textarea)s''' % {
          'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'timestamp': timestamp,
          "textarea": self.textarea.html(), 'actions': actions}


class Cell(Html.Html):
    name = 'Python Cell Runner'
    requirements = ('codemirror',)

    def __init__(self, page: primitives.PageModel, vals: Union[list, str], language: str, width: tuple, height: tuple,
                 html_code: Optional[str], options: Optional[dict], profile: Optional[Union[dict, bool]],
                 verbose: bool = False):
        super(Cell, self).__init__(page, vals, html_code=html_code, options=options,
                                   css_attrs={"width": width, "height": height}, profile=profile, verbose=verbose)
        self.textarea = self.page.ui.texts.code(vals, language, height=height, options=options)
        self.textarea.options.managed = False
        self.textarea.style.add_classes.input.textarea()
        self._jsRun, self._jsSave = '', ''
        self.css({'padding': '10px', "min-height": "30px", 'box-sizing': 'border-box', 'display': 'inline-block'})
        self.actions = []

    def action(self, icon: str, js_funcs: Union[list, str], tooltip: Optional[str] = None):
        """Add a bespoke action to the action panel.

        :param icon: The font awesome icon
        :param js_funcs: The Javascript functions
        :param tooltip: Optional. Text to be displayed when mouse is hover
        """
        icon_button = self.page.ui.icon(icon, tooltip=tooltip).css({"margin-right": '5px'}).click(js_funcs)
        self.actions.append((icon, icon_button))
        icon_button.options.managed = False

    def run(self, js_funcs: Union[list, str], icon: str = "play", tooltip: Optional[str] = None):
        """Emtpy run button.
        This function will just add the icon on the actions panel.

        :param icon: The font awesome icon
        :param js_funcs: Optional. The Javascript functions
        :param tooltip: Optional. Text to be displayed when mouse is hover
        """
        js_funcs.append(self.dom.querySelector("span").innerHTML(1, append=True, val_type=int))
        return self.action(icon, js_funcs, tooltip)

    def save(self, js_funcs: Union[list, str], icon: str = "save", tooltip: Optional[str] = None):
        """Emtpy save button.
        This function will just add the icon on the actions panel.

        :param icon: The font awesome icon
        :param js_funcs: Optional. The Javascript functions
        :param tooltip: Optional. Text to be displayed when mouse is hover
        """
        return self.action(icon, js_funcs, tooltip)

    def __str__(self):
        actions = "".join([b.html() for _, b in self.actions])
        return '''<div %(attrs)s>
    <div style="font-size:12px;padding:10px 5px;float:left;width:50px;height:100%%;vertical-align:middle;white-space:nowrap">
      In [ <span data=count=0 style="display:inline-block;margin-bottom:5px">0</span> ]<br/>%(actions)s
    </div>
    %(textarea)s
</div>''' % {'attrs': self.get_attrs(css_class_names=self.style.get_classes()),
             'actions': actions, "textarea": self.textarea.html()}


class CodeEditor(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'Code'
    requirements = ('codemirror',)
    _option_cls = OptCodeMirror.OptionsCode
    tag = "div"

    def __init__(self, page: primitives.PageModel, vals: str, color: str, width: tuple, height: tuple,
                 html_code: Optional[str], options: Optional[dict], helper: str,
                 profile: Optional[Union[dict, bool]], verbose: bool = False):
        super(CodeEditor, self).__init__(page, vals, html_code=html_code, options=options,
                                         css_attrs={"width": width, "height": height, "color": color},
                                         profile=profile, verbose=verbose)
        self.add_helper(helper)
        self.css({'display': 'block', 'margin': '5px 0'})

    @property
    def style(self) -> GrpClsCodeMirror.Code:
        """Property to the Style property of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsCodeMirror.Code(self)
        return self._styleObj

    @property
    def options(self) -> OptCodeMirror.OptionsCode:
        """ Property to set all the possible object for a button. """
        return super().options

    @property
    def js(self) -> JsCodeMirror.CM:
        """A lot of CodeMirror features are only available through its API.
        Thus, you need to write code (or use add-ons) if you want to expose them to your users.

        `Package Doc <https://codemirror.net/doc/manual.html#api>`_
        """
        if self._js is None:
            self._js = JsCodeMirror.CM(self, page=self.page)
        return self._js

    @property
    def dom(self) -> JsHtmlEditor.CodeMirror:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtmlEditor.CodeMirror(self, page=self.page)
            self._dom._container = "%s.parentNode" % self._dom.varId
        return self._dom

    @property
    def addon(self):
        """The add-on directory in the distribution contains a number of reusable components that implement extra
        editor functionality.

        `Package Doc <https://codemirror.net/doc/manual.html#addons>`_
        """
        return self.options.addons

    def placeholder(self, text: str):
        """Adds a placeholder option that can be used to make content appear in the editor when it is empty and not
        focused.

        :param text: The text displayed if empty editor
        """
        self.options.addons.placeholder()
        self.attr["placeholder"] = text
        return self

    def _set_js_code(self, html_code: str, js_code: str):
        self.dom.varName = js_code
        self.js.varName = js_code

    def build(self, data: str = None, options: Optional[dict] = None, profile: Optional[Union[bool, dict]] = None,
              component_id: Optional[str] = None, dataflows: List[dict] = None, **kwargs):
        """This is a specific version of the common build as the function is not applied to the dom ID but
        the HTML code set as a proper global variable on the JavaScript side.

        :param data: Optional. The component input data
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional.
        :param dataflows: Chain of data transformations
        """
        return super().build(data, options, profile, component_id=component_id or self.js_code, dataflows=dataflows)

    def __str__(self):
        set_val = ""
        if self._vals:
            set_val = '%(editor)s.setValue(%(content)s)' % {
                "editor": self.js_code, "content": JsUtils.jsConvertData(self._vals, None)}
        self.page.properties.js.add_builders('''
%(editor)s = CodeMirror.fromTextArea(document.getElementById('%(htmlId)s'),%(options)s); 
%(editor)s.setSize("%(width)s", "%(height)s"); %(setVal)s; %(editor)s.refresh()''' % {
            "editor": self.js_code, "width": self.css("width"), "height": self.css("height"),
            "options": self.options.config_js(), "htmlId": self.html_code, "setVal": set_val})
        return '<%s><textarea %s></textarea><div id="%s_loading"></div>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.html_code, self.helper, self.tag)


class Tags(Html.Html):
    name = 'Tags'

    def __init__(self, page: primitives.PageModel, vals: list, title: str, icon: str, size: tuple, width: tuple,
                 height: tuple, html_code: Optional[str], profile: Optional[Union[bool, dict]], verbose: bool = False):
        super(Tags, self).__init__(page, vals, css_attrs={"width": width, "height": height},
                                   html_code=html_code, profile=profile, verbose=verbose)
        self.title, self.icon = title, icon
        self.css({"margin-top": "5px", "font-size": "%s%s" % (size[0], size[1]),
                  "font-family": page.style.defaults.font.family})

    @property
    def val(self):
        return "%(breadCrumVar)s['params']['%(htmlCode)s']" % {
            "htmlCode": self.htmlCode, "breadCrumVar": self.page.jsGlobal.breadCrumVar}

    def jsEmpty(self):
        return "%(breadCrumVar)s['params']['%(htmlCode)s'] = []; $('#%(htmlCode)s_tags').text('')" % {
            "htmlCode": self.htmlCode, "breadCrumVar": self.page.jsGlobal.breadCrumVar}

    def jsAdd(self, data):
        """
        :param data:
        """
        data = JsUtils.jsConvertData(data, None)
        icon_details = self.page.icons.get("close")
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


class MarkdownReader(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'markdown'
    tag = "div"
    requirements = ('highlight.js', 'showdown')
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, vals: Union[str, list], width: tuple, height: tuple,
                 html_code: Optional[str],
                 options: Optional[dict], profile: Optional[Union[bool, dict]], verbose: bool = False):
        super(MarkdownReader, self).__init__(page, vals, html_code=html_code, profile=profile, options=options,
                                             css_attrs={"width": width, "height": height, 'box-sizing': 'border-box'},
                                             verbose=verbose)
        self.actions = []

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript available for a DOM element by default.

        Usage::

          div = page.ui.div(htmlCode="testDiv")
          print(div.dom.content)

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptText.OptionsText:
        """Property to set all the input TimePicker component properties"""
        return super().options

    def tooltips(self, data: dict):
        """Add automatically tooltips to the words.

        :param data: The list of word to be automatically changed
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
function hideTooltip(){ document.querySelector('#markdown_tooltip').style.display = 'none' }''')
        self._vals = components.markdown(self._vals, data)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '''<%(tag)s %(attr)s></%(tag)s> ''' % {
          "tag": self.tag, 'attr': self.get_attrs(css_class_names=self.style.get_classes())}
