#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO Fix problem context menu in Status
from pathlib import Path
from typing import Union, Optional, List
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.css import Colors
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsMathjax

from epyk.core.html.options import OptText
from epyk.core.js.html import JsHtml

# The list of CSS classes
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles import GrpClsText


class UpDown(Html.Html):
    name = 'Up and Down'
    tag = "div"
    requirements = ('accounting',)
    _option_cls = OptText.OptionsNumberMoves

    def __init__(self, page: primitives.PageModel, record: dict, components: List[Html.Html], color: Optional[str],
                 label: Optional[str], width: tuple, height: tuple, options: Optional[dict], helper: Optional[str],
                 profile: Optional[Union[bool, dict]]):
        options = options or {}
        if record is None:
            record = {'value': 0, 'previous': 0}
        if label is not None:
            record["label"] = label
        super(UpDown, self).__init__(
            page, record, profile=profile, options=options, css_attrs={"width": width, "height": height})
        self.add_helper(helper, options=options.get("helper"))
        self.style.css.position = "relative"
        if self.helper:
            self.helper.style.css.position = "absolute"
            self.helper.style.css.bottom = 5
            self.helper.style.css.right = 5
        if components is not None:
            for component in components:
                self.add(component)
        self.val['color'] = self.page.theme.colors[-1] if color is None else color
        self.options.label = record.get('label', '')

    @classmethod
    def get_requirements(cls, page: primitives.PageModel, options: types.OPTION_TYPE = None) -> tuple:
        """Update requirements with the defined Icons' family.

        :param page: Page context
        :param options: Component input options
        """
        if options and options.get('icon_family') is not None:
            return (options['icon_family'],) + cls.requirements

        return (page.icons.family,) + cls.requirements

    @property
    def options(self) -> OptText.OptionsNumberMoves:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.

        Usage::
          move = page.ui.numbers.move(100, 60, height=120, helper="Show delta with yesterday")
          move.options.digits_percent = 4
        """
        return super().options

    def __add__(self, component: Html.Html):
        """Add items to a container"""
        if hasattr(component, 'options'):
            component.options.managed = False
        self.components[component.html_code] = component
        return self

    def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Add a click event to the HTML component.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.style.css.cursor = "pointer"
        self.style.add_classes.div.color_light_background_hover()
        return super(UpDown, self).click(js_funcs, profile, source_event, on_ready)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        rows = [str(component) for component in self.components.values()]
        return '<%s %s>%s<div id="%s_content"></div>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(rows), self.html_code,
            self.helper, self.tag)


class BlockText(Html.Html):
    name = 'Block text'
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, record: list, color: Optional[str], border: str, width: tuple,
                 height: tuple, helper: Optional[str], html_code: str, options: Optional[dict],
                 profile: Optional[Union[bool, dict]]):
        options = options or {}
        super(BlockText, self).__init__(page, record, profile=profile, options=options, html_code=html_code,
                                        css_attrs={'color': color, "width": width, "height": height})
        self.add_helper(helper, options=options.get("helper"))
        self.css({'padding': '5px'})
        if border != 'auto':
            self.css('border', str(border))

    @property
    def options(self) -> OptText.OptionsText:
        """Property to set all the possible object for a button"""
        return super().options

    def __str__(self):
        items = [
            '<div %s>' % self.get_attrs(css_class_names=self.style.get_classes()),
            '<div id="%s_title" style="font-size:%spx;text-align:left"><a></a></div>' % (
                self.html_code, self.page.body.style.globals.font.normal(3)),
            '<div id="%s_p" style="width:100%%;text-justify:inter-word;text-align:justify;"></div>' % self.html_code,
            '</div>']
        self.page.properties.js.add_builders(self.refresh())
        return ''.join(items)


class TextWithBorder(Html.Html):
    name = 'Text with Border and Icon'
    _option_cls = OptText.OptionsText

    def __init__(self, page: primitives.PageModel, record: list, width: tuple, height: tuple, align: Optional[str],
                 helper: Optional[str], html_code: str, options: Optional[dict], profile: Optional[Union[dict, bool]]):
        options = options or {}
        super(TextWithBorder, self).__init__(
            page, record, html_code=html_code, options=options, css_attrs={"width": width, "height": height}, profile=profile)
        self.add_helper(helper, options=options.get("helper"))
        self.align = align
        if 'colorTitle' not in self.val:
            self.val['colorTitle'] = self.page.theme.colors[-1]
        if 'color' not in self.val:
            self.val['color'] = self.page.theme.colors[-1]
        self.css({"border-color": self.val['colorTitle'], 'margin-top': '20px'})

    @classmethod
    def get_requirements(cls, page: primitives.PageModel, options: types.OPTION_TYPE = None) -> tuple:
        """Update requirements with the defined Icons' family.

        :param page: Page context
        :param options: Component input options
        """
        if options and options.get('icon_family') is not None:
            return (options['icon_family'],)

        return (page.icons.family,)

    @property
    def options(self) -> OptText.OptionsText:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    _js__builder__ = '''if(options.showdown){var converter = new showdown.Converter(options.showdown); 
  data.title = converter.makeHtml(data.title); data.value = converter.makeHtml(data.value)} 
htmlObj.querySelector('legend').innerHTML = data.title; htmlObj.querySelector('span').innerHTML = data.value'''

    def __str__(self):
        item = ['<fieldset %s>' % self.get_attrs(css_class_names=self.style.get_classes())]
        if 'icon' in self.val:
            self.val['align'] = self.align
            item.append(
                '<i class="%(icon)s fa-5x" style="width:100%%;text-align:%(align)s;margin:2px 0 10px 0;color:%(color)s"></i>' % self.val)
        if 'url' in self.val:
            item.append(
                '<legend style="font-size:%spx;color:%s"></legend><span></span><br><a style="float:right" href="%s">+ more details</a></fieldset>' % (
                    self.page.body.style.globals.font.normal(10), self.val['colorTitle'], self.val['url']))
        else:
            item.append('<legend style="font-size:%spx;color:%s"></legend><span></span></fieldset>' % (
                self.page.body.style.globals.font.normal(10), self.val['colorTitle']))
        item.append(self.helper)
        self.page.properties.js.add_builders(self.refresh())
        return "".join(item)


class Number(Html.Html):
    name = 'Number'
    tag = "div"

    def __init__(
            self, page: primitives.PageModel, number, components, label, width, height, html_code, profile, options, helper):
        super(Number, self).__init__(
            page, number, html_code=html_code, css_attrs={"width": width, "height": height}, profile=profile)
        if options.get('url', None) is not None:
            self.add_link(number, url=options['url'], css={
                "width": "100%", 'text-decoration': 'none', 'display': 'inline-block', "text-align": 'center',
                'margin': 0, 'color': 'inherit', 'padding': 0}, options=options)
            self.span = self.link
        else:
            self.add_link(number, url="#", options=options, css={
                "width": "100%", 'text-decoration': 'none', 'cursor': 'default',
                'display': 'inline-block', "text-align": 'center', 'margin': 0, 'color': 'inherit', 'padding': 0})
            self.link.attr['target'] = '_self'
            self.span = self.link
        self.link.style.css.font_factor(10)
        self.add_label(label, css={'text-align': 'center', 'float': 'none', "width": "auto", "margin": "auto"},
                       position=options.get('label', 'before'), html_code=self.html_code)
        self.css({"display": "inline-block", 'padding': '5%', 'clear': 'both', 'margin': '2px'})
        self.style.css.text_align = "center"
        self.__comps = []
        self.add_helper(helper, options=options.get("helper"))
        if helper is not None:
            self.helper.style.css.position = "absolute"
            self.helper.style.css.bottom = 10
            self.helper.style.css.right = 25
        if components is not None:
            for component in components:
                self.add(component)

    def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        return self.span.click(js_funcs, profile, source_event, on_ready)

    def build(self, data=None, options: Optional[dict] = None,
              profile: Optional[Union[bool, dict]] = None, component_id: Optional[str] = None,
              dataflows: List[dict] = None, **kwargs):
        return self.span.build(data, options, profile, self.span.html_code, dataflows=dataflows)

    def __add__(self, component: Html.Html):
        """ Add items to a container """
        if hasattr(component, 'options'):
            component.options.managed = False
        self.components[component.html_code] = component
        self.__comps.append(component.html_code)
        return self

    def __str__(self):
        rows = [str(self.components[html_code]) for html_code in self.__comps]
        return "<%s %s>%s</%s>%s" % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(rows), self.tag, self.helper)


class Delta(Html.Html):
    requirements = ('jqueryui', 'accounting')
    name = 'Delta Figures'
    _option_cls = OptText.OptionsNumberDelta

    def __init__(self, page: primitives.PageModel, records, components, width, height, options, helper, profile):
        options = options or {}
        super(Delta, self).__init__(page, records, options=options,
                                    css_attrs={"width": width, "height": height}, profile=profile)
        self.add_helper(helper, options=options.get("helper"))
        if 'color' not in self.val:
            self.val['color'] = self.page.theme.colors[-1]
        if 'thresold1' not in self.val:
            self.options.threshold1 = 100
        if 'thresold2' not in self.val:
            self.options.threshold2 = 50
        self.css({"color": self.val['color']})
        self.options.label = records.get('label', '')
        self.style.css.position = "relative"
        if self.helper is not None and self.helper:
            self.helper.style.css.position = "absolute"
            self.helper.style.css.bottom = 5
            self.helper.style.css.right = 0
            self.style.css.padding_right = 17
        if 'url' in records:
            self._jsStyles["url"] = records['url']
        if components is not None:
            for component in components:
                self.add(component)

    def __add__(self, component: Html.Html):
        """ Add items to a container """
        if hasattr(component, 'options'):
            component.options.managed = False
        self.components[component.html_code] = component
        return self

    @property
    def options(self) -> OptText.OptionsNumberDelta:
        """Property to set all the possible object for a button"""
        return super().options

    _js__builder__ = '''
jHtmlObj = jQuery(htmlObj); 
if(typeof data === "number"){data = {number: data}};
if(typeof data.prevNumber === 'undefined'){data.prevNumber = accounting.unformat(jHtmlObj.find('div').first().text())};
var variation = 100 * (data.number - data.prevNumber) / data.prevNumber; var warning = ''; 
var currVal = accounting.formatNumber(data.number, options.digits, options.thousand_sep, options.decimal_sep); 
if(typeof data.thresold1 === 'undefined'){data.thresold1 = options.thresold1};
if(typeof data.thresold2 === 'undefined'){data.thresold2 = options.thresold2};
if(variation > data.thresold1){warning = '<i style="color:'+ options.red +';" title="'+ variation +' increase" class="fas fa-exclamation-triangle"></i>&nbsp;&nbsp;'};
if(typeof data.url !== 'undefined'){currVal = '<a style="text-decoration:none;color:'+ data.color +'" href="' + data.url+ '">'+ currVal +'</a>'}
else if(typeof options.url !== 'undefined'){currVal = '<a style="text-decoration:none;color:'+ data.color +'" href="' + options.url+ '">'+ currVal +'</a>'}
if(typeof data.label !== 'undefined'){currVal = data.label +" "+ currVal} else {currVal = options.label +" "+ currVal}
var progressElt = jHtmlObj.find('#progress');
progressElt.attr("title", variation + "%");
progressElt.progressbar({value: variation}).tooltip({track: true});
if(variation > data.thresold1){progressElt.children().css({'background': options.red})} 
else if(variation > data.thresold2){progressElt.children().css({'background': options.orange})} 
else{progressElt.children().css({'background': options.green})}
jHtmlObj.find('div').first().html(warning + currVal);
jHtmlObj.find('div').first().css({"white-space": "nowrap"});
jHtmlObj.find('div').last().html(options.previous_label + accounting.formatNumber(data.prevNumber, options.digits, options.thousand_sep, options.decimal_sep));
      '''

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        rows = [str(component) for component in self.components.values()]
        return '''<div %(strAttr)s> 
      %(components)s
      <div style="width:100%%;text-align:right;font-size:%(size)s"></div>
      <div id="progress" style="height:10px;color:%(color)s;border:1px solid %(greyColor)s"></div>
      <div style="font-size:10px;font-style:italic;color:%(greyColor)s;padding-bottom:5px;text-align:left"></div>
      %(helper)s
      </div>''' % {"strAttr": self.get_attrs(css_class_names=self.style.get_classes()),
                   "size": self.page.body.style.globals.font.normal(6),
                   'htmlCode': self.html_code, "color": self.val['color'], "components": "".join(rows),
                   "greyColor": self.page.theme.greys[6], "helper": self.helper}


class Formula(Html.Html):
    requirements = ('mathjax',)
    name = 'Latex Formula'

    def __init__(self, page: primitives.PageModel, text, width, height, color, html_code, helper, options, profile):
        options = options or {}
        super(Formula, self).__init__(page, text, options=options, html_code=html_code,
                                      css_attrs={"color": color, "width": width, "height": height}, profile=profile)
        self.add_helper(helper, options=options.get("helper"))

    _js__builder__ = '''htmlObj.innerHTML = data; MathJax.typeset([htmlObj])'''

    @property
    def style(self) -> GrpClsText.ClsFormula:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsText.ClsFormula(self)
        return self._styleObj

    @property
    def js(self) -> JsMathjax.Mathjax:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._js is None:
            self._js = JsMathjax.Mathjax(self, selector=self.dom.varId)
        return self._js

    def __str__(self):
        return '<font %s>%s</font>%s' % (
        self.get_attrs(css_class_names=self.style.get_classes()), self.content, self.helper)


class TrafficLight(Html.Html):
    name = 'Traffic Light'
    tag = "div"
    _option_cls = OptText.OptionsTrafficLight

    def __init__(self, page: primitives.PageModel, color, label, height, tooltip, helper, options, profile,
                 html_code: str=None):
        options = options or {}
        # Small change to allow the direct use of boolean and none to define the color
        # Those standards will simplify the creation of themes going forward
        super(TrafficLight, self).__init__(page, color, css_attrs={"width": height, "height": height},
                                           options=options, profile=profile, html_code=html_code)
        self.add_helper(helper, css={"margin-top": "-17px"}, options=options.get("helper"))
        self.add_label(label, css={"width": 'auto', 'float': 'none', 'vertical-align': 'middle', 'height': '100%',
                                   "margin": '0 5px', 'display': 'inline-block', "min-width": '100px'},
                       html_code=self.html_code, options=options.get("label"))
        self.css({'border-radius': '60px', 'background-color': self.val, 'display': 'inline-block',
                  'vertical-align': 'middle'})
        self.set_attrs(name="title", value=tooltip)
        self.set_attrs(name="data-status", value=color)
        self.action = None
        if tooltip is not None:
            self.tooltip(tooltip)

    @property
    def options(self) -> OptText.OptionsTrafficLight:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def dom(self) -> JsHtml.JsHtmlBackground:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlBackground(self, page=self.page)
        return self._dom

    def colors(self, green: Optional[str] = None, red: Optional[str] = None, neutral: Optional[str] = None):
        """Set the 3 colors of the traffic light.

        :param green: Optional. The color used in case of result true
        :param red: Optional. The color used in case of result false
        :param neutral: Optional. The color used in case of null

        :return: self to allow the chains.
        """
        if neutral is not None:
            self.options.orange = neutral
        if green is not None:
            self.options.green = green
        if red is not None:
            self.options.red = red
        return self

    def resolve(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None):
        """Turn a error warning to a green one.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self.action = self.page.ui.icon("wrench")
        self.action.options.managed = False
        self.action.tooltip("Click to try to resolve the issue")
        self.action.style.css.font_size = 8
        self.action.style.css.margin_top = 8
        self.action.style.css.cursor = 'pointer'
        self.action.style.css.vertical_align = 'top'
        self.action.click(js_funcs, profile)
        return self

    def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Add a click event to the HTML component.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        success = Colors.getHexToRgb(self.page.theme.success.base)
        self.style.css.cursor = "pointer"
        js_funcs = [self.dom.querySelector("div").toggle(
            "background-color", "rgb(%s, %s, %s)" % (
                success[0], success[1], success[2]), self.page.theme.danger.base)] + js_funcs
        return super(TrafficLight, self).click(js_funcs, profile, source_event, on_ready)

    def __str__(self):
        if self.action is not None:
            return '<div id="%s"><div %s></div>%s</div>%s' % (
                self.html_code, self.get_attrs(css_class_names=self.style.get_classes(), with_id=False),
                self.action.html(), self.helper)

        return '<%s id="%s"><div %s></div></%s>%s' % (
            self.tag, self.html_code, self.get_attrs(css_class_names=self.style.get_classes(), with_id=False),
            self.tag, self.helper)


class ContentsTable(Html.Html):
    name = 'Contents Table'
    tag = "div"
    _option_cls = OptText.OptContents

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "contents-table.css"
    ]
    style_refs = {
        "contents-table-item": "contents-table-item",
        "contents-table-title": "contents-table-title",
        "contents-table": "contents-table",
        "contents-table-levels": "contents-table-level-%s",
    }

    def __init__(self, page: primitives.PageModel, title, width, height, html_code, options, profile):
        self.indices, self.first_level, self.entries_count, self.ext_links = [], None, 0, {}
        super(ContentsTable, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                            css_attrs={"width": width, "height": height})
        self.title = self.page.ui.div(html_code="%s_title" % self.html_code)
        self.title += self.page.ui.text(title, html_code="%s_title_text" % self.html_code).css(
            {"width": 'auto', 'display': 'inline-block'})
        self.title += self.page.ui.text("[hide]", html_code="%s_title_toggle" % self.html_code).css({
            "width": '30px', 'display': 'inline-block', 'margin-left': '5px',
            'font-size': self.page.body.style.globals.font.normal(-5)})
        self.title[0].attr["class"].add(self.style_refs["contents-table-title"])
        self.title[0].style.css.font_size = self.page.body.style.globals.font.normal(6)
        self.title.options.managed = False
        self.title.style.css.white_space = "nowrap"
        self.attr["class"].add(self.style_refs["contents-table"])
        self.anchors_count = 0

    @property
    def options(self) -> OptText.OptContents:
        """Property to set all the possible object for the content menu on the page.
        This object can be defined only once on the page.
        """
        return super().options

    _js__builder__ = '''var menu = htmlObj.querySelector("div[name=menu]"); menu.innerHTML = "";
if ((data == null) || (data.length == 0)){htmlObj.style.display = 'none'}
else{ 
  data.forEach(function(rec){
    var link = document.createElement("a");  
    link.innerHTML = rec.text; link.href = rec.anchor;
    link.style.display = 'block'; link.style.width = '100%';
    link.style.paddingLeft = Math.max(0, (rec.level - 1) * 5) + "px";
    menu.appendChild(link)
})} '''

    def anchor(self, text: str, level: int = 0, anchor: str = '#', options: Optional[dict] = None, html_code: str = None):
        """Add link to the content table.
        `w3schools <https://www.w3schools.com/tags/tag_a.asp>`_

        :param text: The link label
        :param level: Optional. The depth of the link in the document tree
        :param anchor: Optional. The internal reference to another component in the page
        :param options: Optional. The component options for the link
        :param html_code: Optional. Anchor's HTML codee
        """
        self.anchors_count += 1
        anchor_code = html_code or "%s_anchor_%s" % (self.html_code, self.anchors_count)
        if anchor is not None:
            href = self.page.ui.link(text, url=anchor, html_code=anchor_code, options=options)
            href.style.css.font_size = self.page.body.style.globals.font.normal(2)
            href.style.add_classes.link.no_decoration()
        else:
            min_links = self.page.ui.text("-", html_code=anchor_code)
            min_links.style.css.margin_left = 10
            min_links.click([
                '''var components = %(dom)s.querySelectorAll("[data-group='%(group)s']");
var puceIcon = %(icon)s.innerText;
if (puceIcon == "-"){components.forEach(function(comp){comp.style.display = "none"}); %(icon)s.innerText = "+";}
else {components.forEach(function(comp){comp.style.display = "block"}); %(icon)s.innerText = "-";}''' % {
                  'icon': min_links.dom.varName, 'dom': self.dom.varName, 'group': "%s_%s" % (text, level)}])
            if options is not None and options.get("hidden", False):
                self.page.body.onReady(min_links.dom.events.trigger("click"))
            href = self.page.ui.div([
                self.page.ui.text(text, options=options),
                min_links
            ])
            href.attr["name"] = "%s_%s" % (text, level)
            href.attr["data-level"] = level
        if level is not None:
            href.style.css.padding_left = (level - 1) * 5
        href.options.managed = False
        for item in self.val[::-1]:
            if item.attr.get("name") is not None and item.attr.get("data-level", 0) < level:
                href.attr["data-group"] = item.attr["name"]
                break

        self.val.append(href)
        href.attr["class"].add(self.style_refs["contents-table-item"])
        href.attr["class"].add(self.style_refs["contents-table-levels"] % level)
        href.click(['''
let contentMenuItems = document.querySelectorAll(".contents-table-item");
if(contentMenuItems){contentMenuItems.forEach(function(menuItem){menuItem.classList.remove("contents-item-active");})};
event.target.classList.add("contents-item-active")'''])
        return href

    def move(self):
        super(ContentsTable, self).move()
        self.style.css.position = None
        self.style.css.margin = 5
        return self

    def add_category(self, text: str, level: Optional[int] = None, options: Optional[dict] = None,
                     html_code_content: str = "content"):
        """Add a bespoke title to the page without click event.

        :param text: The text visible on the page
        :param level: Optional. The depth for the title in the document
        :param options: Optional. The options for the title component
        :param html_code_content: Optional. The Html code of the component Content table
        """
        return self.page.components[html_code_content].anchor(text, level or 4, None, options=options)

    def add_title(self, component: Html.Html, level: Optional[int] = None, css: Optional[dict] = None,
                  position: str = "before", options: Optional[dict] = None, html_code_content: str = "content"):
        """Add a bespoke title to the page.

        :param component: An HTML component
        :param level: Optional. The depth for the title in the document
        :param css: Optional. The CSS style for the link
        :param position: Optional. The position in the content table (append or prepend)
        :param options: Optional. The options for the title component
        :param html_code_content: Optional. The Html code of the component Content table
        """
        # Special attribute set in the base component interface
        div = self.page.ui.div(html_code="%s_anchor" % component.html_code)
        if self.page.body.css('padding-top') is None:
            div.style.css.margin_top = - 10
        else:
            div.style.css.margin_top = - int(self.page.body.css('padding-top')[:-2]) - 10
        div.style.css.position = "absolute"
        div.style.css.z_index = -1
        link = self.page.components[html_code_content].anchor(component.val, level or 4, "#%s_anchor" % self.html_code)
        self.page.components[html_code_content][-1].click([
            component.dom.transition(
                ["color", "font-size"], [self.page.theme.colors[-1], '101%'], duration=[0.5, 0.5], reverse=True)])
        return link

    def add_url(self, component: Html.Html, url: str, level: Optional[int] = None,
                options: Optional[dict] = None, html_code_content: str = "content"):
        """Add a bespoke link to the content table.
        Those links can redirect to external pages.

        :param component: An HTML component
        :param url: The url link with component clicked
        :param level: Optional. The depth for the title in the document
        :param options: Optional. The options for the title component
        :param html_code_content: Optional. The Html code of the component Content table
        """
        component.options.managed = False
        div = self.page.ui.div(html_code="%s_anchor" % component.html_code)
        if self.page.body.css('padding-top') is None:
            div.style.css.margin_top = - 10
        else:
            div.style.css.margin_top = - int(self.page.body.css('padding-top')[:-2]) - 10
        div.style.css.position = "absolute"
        div.style.css.z_index = -1
        dflt_options = {"target": '_blank'}
        if options is not None:
            dflt_options.update(options)
        link = self.page.components[html_code_content].anchor(component.val, level or 4, url, options=dflt_options)
        self.page.components[html_code_content][-1].click([
            component.dom.transition(["color", "font-size"], [self.page.theme.colors[-1], '101%'], duration=[0.5, 0.5],
                                     reverse=True)])
        return link

    def __str__(self):
        self.menu._vals = self.val
        self.menu.attr["name"] = "menu"
        self.menu.options.managed = False
        self.title[-1].click([self.menu.dom.toggle(), self.title[-1].dom.toggleText('[show]', '[hide]')])
        return '''<%(tag)s %(attr)s>%(title)s%(links)s</%(tag)s> ''' % {
            'attr': self.get_attrs(css_class_names=self.style.get_classes()), "tag": self.tag,
            'title': self.title.html(), 'htmlCode': self.html_code, 'links': self.menu.html()}


class SearchResult(Html.Html):
    name = 'Search Result'
    tag = "div"
    requirements = ('jquery',)
    _option_cls = OptText.OptSearchResult

    def __init__(self, page: primitives.PageModel, records, width, height, options, profile):
        super(SearchResult, self).__init__(
            page, records, options=options, profile=profile, css_attrs={"width": width, "height": height})
        self.style.css.margin = "5px 10px 5px 10px"

    _js__builder__ = '''
      jHtmlObj = %(jquery)s; jHtmlObj.empty();
      if (typeof options.currPage == 'undefined'){options.currPage = 0}; var pageNumber = options.pageNumber;
      data.slice(options.currPage * pageNumber).forEach( function(rec){
        var newItem = $('<div style="margin:5px 10px 5px 10px;"></div>') ; 
        var title = $('<div>'+ rec['title'] + '</div>').css( options.title );
        if (rec['urlTitle'] != undefined){
          title.css({'cursor': 'pointer'}); title.click(function(e){window.open(rec['urlTitle'], '_blank')})}
        newItem.append(title);
        if (rec.icon != undefined){
          var item = $('<div></div>').css(options.url);
          item.append( $('<i class="'+ rec['icon'] +'" style="margin-right:5px"></i>')).append(rec['url']);
          newItem.append(item)} 
        else if(rec.url != undefined) {newItem.append($('<div>'+ rec['url'] +'</div>').css(options.url))}
        newItem.append( $('<div>'+ rec['dsc'] +'</div>').css(options.dsc));
        if(rec.visited != undefined){newItem.append($('<div>'+ rec.visited +'</div>').css(options.visited))}
        if(rec.links != undefined){
          rec.links.forEach(function(link){ 
            if (link.url == undefined) {link.url = link.val};
            newItem.append($('<a href='+ link.url +' target="_blank">'+ link.val +'</a><br>').css(options.link))})};
        jHtmlObj.append(newItem);
      }); 
      if(data.length > 0) {
        var reste = data.length/ pageNumber; var currIndex = options.currPage+1; var roundRest = Math.trunc(reste);
        if (roundRest > reste) {reste ++};
        var paginate = $('<div style="display:inline-block;height:35px;padding:0;width:100%%;text-align:center;margin-top:10px" class="py_cssdivpagination"></div>');
        if (currIndex > 1){
          var href = $('<a href="#">&laquo;</a>');
          href.click({page: options.currPage-1, rec: data}, function(e){options.builder(htmlObj, e.data.rec, options, e.data.page)});
          paginate.append(href)};
        for (var i = 0; i < reste; i++){
          var indexPage = i + 1;
          if (options.currPage == i) { 
            var href = $('<a href="#" style="background-color:'+ options.grey +';padding:5px;color:'+ options.white +'">'+ indexPage +'</a>');
            href.click({page: i, rec: data}, function(e) {options.builder(htmlObj, e.data.rec, options, e.data.page)});
            paginate.append(href)}
          else{
            var href = $('<a href="#" style="padding:5px;">'+ indexPage +'</a>') ;
            href.click({page: i, rec: data}, function(e){options.builder(htmlObj, e.data.rec, options, e.data.page)});
            paginate.append(href)}}
        if(currIndex < reste){
          var href = $('<a href="#">&raquo;</a>');
          href.click({page: options.currPage+1, rec: data}, function(e){options.builder(htmlObj, e.data.rec, options, e.data.page)});
          paginate.append(href)};
        jHtmlObj.append(paginate)
      } ''' % {'jquery': JsQuery.decorate_var("htmlObj", convert_var=False)}

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%s %s></%s> ' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class Composite(Html.Html):
    name = 'Composite'
    _option_cls = OptText.OptionsComposite

    def __init__(self, page: primitives.PageModel, schema, width, height, html_code, options, profile, helper):
        options = options or {}
        super(Composite, self).__init__(page, None, html_code=html_code, profile=profile, options=options,
                                        css_attrs={"width": width, "height": height})
        self.__builders, ref_map, self.main = set(), {}, None
        self.add_helper(helper, options=options.get("helper"))
        self._set_comp(None, schema, self.__builders, ref_map)
        self.attr = self.val.attr
        self._js = self.val._js
        self._dom = self.val._dom
        self._styleObj = self.val._styleObj

    @property
    def options(self) -> OptText.OptionsComposite:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript by default.
        This is the only flexible component in which this DOM object can be changed.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self.val, page=self.page)
        return self._dom

    @dom.setter
    def dom(self, js_html):
        self._dom = js_html

    @property
    def style(self) -> GrpCls.ClassHtmlEmpty:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpCls.ClassHtmlEmpty(self)
        return self._styleObj

    def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        return self.val.click(js_funcs, profile, source_event, on_ready)

    def __getitem__(self, i):
        return self.val.val[i]

    def __add__(self, component: Html.Html):
        """ Add items to a container """
        # Has to be defined here otherwise it is set to late
        component.options.managed = False
        if not isinstance(self.val.val, list):
            self._vals = self.val._vals
        self.val.val.append(component)
        return self

    @property
    def _get_comp_map(self):
        comp_ui = self.page.ui
        if hasattr(self.page.ui, 'std'):
            comp_ui = getattr(self.page.ui, 'std')
        return {
            'div': comp_ui.div,
            'textarea': comp_ui.textarea,
            'button': comp_ui.button,
            'label': comp_ui.label,
            'img': comp_ui.img,
            'header': comp_ui.header,
            'section': comp_ui.section,
            'icon': comp_ui.icon,
            'span': comp_ui.texts.span,
            'checkbox': comp_ui.inputs.checkbox,
            'radio': comp_ui.inputs.d_radio,
            'input': comp_ui.inputs.d_text,
            'circle': comp_ui.charts.svg.circle,
            'svg': comp_ui.charts.svg.new,
            'path': comp_ui.charts.svg.path,
            'list': comp_ui.list,
            'item': comp_ui.lists.item,
            'nav': comp_ui.tags.nav,
            'p': comp_ui.tags.p,
            'link': comp_ui.tags.a,
            'ol': comp_ui.tags.ol,
            'aside': comp_ui.tags.aside,
            'hr': comp_ui.layouts.hr,
        }

    def _set_comp(self, comp: Optional[Html.Html], schema_child, builders, ref_map):
        """

        :param comp:
        :param schema_child:
        :param builders:
        :param ref_map:
        """
        if 'args' in schema_child and 'url' in schema_child['args']:
            schema_child['args']['url'] = schema_child['args']['url'] % ref_map
        # delegate the htmlCode to the main component
        if comp is None:
            del self.page.components[self.html_code]

            new_comp = self._get_comp_map[schema_child['type']](html_code=self.html_code, **schema_child.get('args', {}))
            self._vals = new_comp
        else:
            new_comp = self._get_comp_map[schema_child['type']](**schema_child.get('args', {}))
        if 'builder' in schema_child:
            builders.add(schema_child['builder'])
        if self.options.reset_class and not schema_child.get('class-keep', False):
            new_comp.style.clear()
        if 'class' in schema_child:
            new_comp.style.clear(True)
            if schema_child['class'] is None:
                new_comp.set_attrs({'class': schema_child['class']})
            else:
                for cls in schema_child['class'].split(" "):
                    new_comp.attr['class'].add(cls)
        if 'arias' in schema_child:
            if 'describedby' in schema_child['arias']:
                schema_child['arias']['describedby'] = schema_child['arias']['describedby'] % ref_map
            new_comp.aria.set(schema_child['arias'])
        if 'css' in schema_child:
            if schema_child['css'] is None:
                new_comp.style.clear_style()
            else:
                new_comp.css(schema_child['css'], reset=True)
        if 'attrs' in schema_child:
            if 'data-target' in schema_child['attrs']:
                schema_child['attrs']['data-target'] = schema_child['attrs']['data-target'] % ref_map
            new_comp.set_attrs(schema_child['attrs'])
        if 'ref' in schema_child:
            ref_map[schema_child['ref']] = new_comp.html_code
        for child in schema_child.get('children', []):
            self._set_comp(new_comp, child, builders, ref_map)
        if comp is not None:
            comp += new_comp
        if self.main is None:
            self.main = self.val

    def set_builder(self, builder: str, **kwargs):
        self.page.properties.js.add_builders(builder)

    def __str__(self):
        self.page.properties.js.add_builders(list(self.__builders))
        return self.val.html()


class Status(Html.Html):
    name = 'status'
    tag = "div"
    _option_cls = OptText.OptionsStatus

    def __init__(self, page: primitives.PageModel, status, width, height, html_code, profile, options):
        super(Status, self).__init__(page, status, html_code=html_code, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height})
        self.style.css.text_align = 'center'
        self.style.css.line_height = 30
        self.style.css.margin = 2
        self.style.css.padding = '10px auto'

    @property
    def options(self) -> OptText.OptionsStatus:
        """Property to the component options. Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    _js__builder__ = '''if(options.showdown){
var converter = new showdown.Converter(options.showdown); var content = converter.makeHtml(data)}  
else {var content = data};htmlObj.innerHTML = content;
if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

    def __str__(self):
        color_map = self.page.js.data.datamap().attrs(self.options.states)
        if self.options.change_menu:
            for k, v in self.options.states.items():
                item = self.context.add(k)
                item.click([
                    self.context.source.build(item.dom.content),
                    self.context.source.dom.css({"background": color_map.get(item.dom.content)}),
                    self.context.dom.hide()])
        self.style.css.background = self.options.states.get(self.val.upper(), self.options.background)
        self.style.css.color = self.options.color
        return "<%s %s>%s</%s>" % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val, self.tag)
