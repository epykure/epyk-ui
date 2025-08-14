from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlEditor, JsHtml
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState

from epyk.core.html.options import OptText


class Console(Html.Html):
    name: str = 'EkConsole'
    _option_cls = OptText.OptionsConsole
    tag: str = "div"

    def __init__(self, page: primitives.PageModel, data: Union[str, list], width: tuple, height: tuple,
                 html_code: Optional[str],
                 helper: Optional[str], options: Optional[dict], profile: Optional[Union[dict, bool]],
                 verbose: bool = False):
        options = options or {}
        super(Console, self).__init__(page, data, html_code=html_code, options=options,
                                      css_attrs={"width": width, "height": height}, profile=profile, verbose=verbose)
        self.css({"overflow": 'auto', 'box-sizing': 'border-box', 'color': self.page.theme.greys[-1],
                  'background': self.page.theme.colors[0]})
        self.add_helper(helper, options=options.get("helper"))

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
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
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


class Tags(Html.Html):
    name: str = 'Tags'

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
            "htmlCode": self.html_code, "breadCrumVar": self.page.jsGlobal.breadCrumVar}

    def jsEmpty(self):
        return "%(breadCrumVar)s['params']['%(htmlCode)s'] = []; $('#%(htmlCode)s_tags').text('')" % {
            "htmlCode": self.html_code, "breadCrumVar": self.page.jsGlobal.breadCrumVar}

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
      ''' % {"htmlCode": self.html_code, "jsData": data, 'whiteColor': self.page.theme.greys[0],
             "baseColor": self.page.theme.colors[9], "close": icon_details["icon"]}

    def __str__(self):
        return '''
      <div %(attr)s>
        <div style='margin:0;display:inline-block;vertical-align:middle;width:90px;float:left;padding:2px 5px 0 5px;height:30px;border:1px solid %(greyColor)s'>
          <i class="%(icon)s" style="margin-right:10px"></i>%(title)s</div>
        <div id='%(htmlCode)s_tags' style='padding:2px 5px 0 5px;border:1px solid %(greyColor)s;height:30px'></div>
      </div>''' % {"attr": self.get_attrs(css_class_names=self.style.get_classes()), "title": self.title,
                   'icon': self.icon, 'htmlCode': self.html_code, 'greyColor': self.page.theme.greys[2]}


class MarkdownReader(MixHtmlState.HtmlOverlayStates, Html.Html):
    name: str = 'Markdown Reader'
    tag: str = "div"
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
