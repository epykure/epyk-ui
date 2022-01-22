#!/usr/bin/python
# -*- coding: utf-8 -*-
# TODO Add JS builder to Button Filter

from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.html import Html
from epyk.core.html.options import OptButton

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery
from epyk.core.js.statements import JsIf
from epyk.core.js.objects import JsComponents

# The list of CSS classes
from epyk.core.css.styles import GrpClsButton


class Button(Html.Html):
  name = 'button'
  _option_cls = OptButton.OptionsButton

  def __init__(self, report: primitives.PageModel, text: str = None, icon: str = None, width: Optional[tuple] = None,
               height: Optional[tuple] = None, html_code: Optional[str] = None, tooltip: Optional[str] = None,
               profile: Optional[Union[dict, bool]] = None, options: Optional[dict] = None):
    text = text or []
    if not isinstance(text, list):
      text = [text]
    for obj in text:
      if hasattr(obj, 'options'):
        obj.options.managed = False
    super(Button, self).__init__(
      report, text, html_code=html_code, options=options, profile=profile, css_attrs={"width": width, "height": height})
    self.add_icon(icon, html_code=self.htmlCode)
    if icon is not None and not text:
      self.icon.style.css.margin_right = None
    if icon is not None:
      self.icon.style.css.color = "inherit"
    self.tooltip(tooltip)
    self.set_attrs(name="data-count", value=0)

  @property
  def options(self) -> OptButton.OptionsButton:
    """
    Description:
    -----------
    Property to set all the possible object for a button.

    Usage::

      but = page.ui.button("Click Me")
      but.options.multiple = False

    :rtype: OptButton.OptionsButton
    """
    return super().options

  @property
  def dom(self) -> JsHtml.JsHtmlButton:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript available for a DOM element by default.

    Usage::

      but = page.ui.button("Click Me")
      page.js.console.log(but.dom.content)

    :rtype: JsHtml.JsHtmlButton
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButton(self, report=self.page)
    return self._dom

  _js__builder__ = "htmlObj.setAttribute('data-processing', false); htmlObj.innerHTML = data"

  def loading(self, status: bool = True):
    """
    Description:
    -----------
    Show / Hide the loading event predefined for this component.

    Usage::

      but = page.ui.button("Loading")
      page.body.onReady([but.loading()])

    Attributes:
    ----------
    :param bool status: Optional. A flag to specify the status of the loading event.
    """
    if status:
      self.dom.setAttribute("data-content", self.dom.content)
      self.dom.innerHTML("<i class='fas fa-cog fa-spin' style='margin-right:5px'></i>Processing...")
      self.dom.setAttribute("data-processing", True)
      return self.dom.r

    self.dom.innerHTML(self.dom.getAttribute("data-content"))
    self.dom.setAttribute("data-processing", False)
    return self.dom.r

  def no_background(self):
    """
    Description:
    -----------
    Remove the default button background and remove the padding.

    Usage::

      but = page.ui.button("Click Me")
      but.no_background()

    """
    self.style.css.background_color = "#11ffee00"
    return self

  def goto(self, url: str, js_funcs: Optional[Union[list, str]] = None, profile: Optional[Union[dict, bool]] = None,
           target: str = "_blank", source_event: Optional[str] = None):
    """
    Description:
    -----------
    Click event which redirect to another page.

    Usage::

      but = page.ui.button("Click Me")
      but.goto("http://www.epyk-studio.com")

    Attributes:
    ----------
    :param str url: The destination path.
    :param Optional[Union[list, str]] js_funcs: The Javascript Events triggered before the redirection.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    :param str target: Optional. The type of link to the next page.
    :param Optional[str] source_event: Optional. The event source.
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.js.location.open_new_tab(url, target))
    return self.click(js_funcs, profile, source_event)

  @property
  def style(self) -> GrpClsButton.ClassButton:
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    Usage::

      but = page.ui.button("Click Me")
      but.style.css.margin = "5px"

    :rtype: GrpClsButton.ClassButton
    """
    if self._styleObj is None:
      self._styleObj = GrpClsButton.ClassButton(self)
    return self._styleObj

  def disable(self, background_color: Optional[str] = None, color: Optional[str] = None):
    """
    Description:
    -----------
    Add the HTML tag to disable the button.

    Usage::

      but = page.ui.button("Click Me")
      but.disable()

    Attributes:
    ----------
    :param Optional[str] background_color: Optional. An hexadecimal color code.
    :param Optional[str] color: Optional. A hexadecimal color code.

    :return: The htmlObj to allow the chaining
    """
    css_pmts = {"cursor": "not-allowed"}
    if background_color is not None:
      css_pmts["background"] = background_color
    if color is not None:
      css_pmts["color"] = color
    self.css(css_pmts)
    self.attr['disabled'] = True
    return self

  def press(self, js_press_funcs: Optional[Union[list, str]] = None,
            js_release_funcs: Optional[Union[list, str]] = None,
            profile: Optional[Union[dict, bool]] = None, on_ready: bool = False):
    """
    Description:
    -----------
    Special click event to keep in memory the state of the component.

    Usage::

      but = page.ui.button("Click Me")

    Attributes:
    ----------
    :param Optional[Union[list, str]] js_press_funcs: Optional. Javascript functions.
    :param Optional[Union[list, str]] js_release_funcs: Optional. Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    :param on_ready: Boolean. Optional.
    """
    str_fnc = ""
    if js_press_funcs is not None:
      if not isinstance(js_press_funcs, list):
        js_press_funcs = [js_press_funcs]
      if self.options.group is not None and not self.options.multiple:
        js_press_funcs.append(self.dom.release(by_name=True))
      js_press_funcs.append(self.dom.lock(not_allowed=js_release_funcs is None))
      str_fnc = "if(%s == 'pointer'){%s}" % (self.dom.css('cursor'), JsUtils.jsConvertFncs(js_press_funcs, toStr=True))
    if js_release_funcs is not None:
      if js_press_funcs is None:
        raise ValueError("Press Event must be defined")

      if not isinstance(js_release_funcs, list):
        js_release_funcs = [js_release_funcs]
      js_release_funcs.append(self.dom.release())
      str_fnc = "%s else{%s}" % (str_fnc, JsUtils.jsConvertFncs(js_release_funcs, toStr=True))
    return self.on("click", str_fnc, profile, on_ready=on_ready)

  def color(self, color: str):
    """
    Description:
    -----------
    Change the color of the button background when the mouse is hover.

    Usage::

      page.ui.buttons.remove("remove").color("blue")

    Attributes:
    ----------
    :param str color: the color of the component (text and borders).
    """
    self.style.css.border = "1px solid {}".format(color)
    self.set_attrs(name="onmouseover", value="this.style.backgroundColor='%s';this.style.color='white'" % color)
    self.set_attrs(name="onmouseout", value="this.style.backgroundColor=\'white\';this.style.color=\'%s\';" % color)
    return self

  def properties(self) -> dict:
    """
    Description:
    -----------
    Return the full properties of the HTML component.
    This property should allow another JavaScript framework to build the component.

    Usage::

      but = page.ui.button("Click Me")
      but.properties

    """
    return {"tag": self.name, 'selector': self.htmlCode}

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    return '<button {attrs}>{content}</button>'.format(attrs=self.get_attrs(pyClassNames=self.style.get_classes()),
                                                       content=str_div)


class Checkbox(Html.Html):
  name = 'Check Box'
  requirements = ('font-awesome', 'bootstrap', 'jquery')
  _option_cls = OptButton.OptCheckboxes

  def __init__(self, report: primitives.PageModel, records, color: Optional[str], width: Optional[tuple],
               height: Optional[tuple], align: Optional[str],  html_code: Optional[str],  tooltip: Optional[str],
               options: Optional[dict], profile: Optional[Union[dict, bool]]):
    if report.inputs.get(html_code) is not None:
      selected_vals = set(report.inputs[html_code].split(","))
      for rec in records:
        if rec["value"] in selected_vals:
          rec["checked"] = True
    super(Checkbox, self).__init__(report, records, html_code=html_code, options=options,
                                   css_attrs={"width": width, "height": height}, profile=profile)
    self.css({'text-align': align, 'color': 'inherit' if color is None else color, 'padding': '5px'})
    if tooltip:
      self.tooltip(tooltip)

  @property
  def options(self) -> OptButton.OptCheckboxes:
    """
    Description:
    -----------
    Property to set all the possible object for check boxes.

    :rtype: OptButton.OptCheckboxes
    """
    return super().options

  @property
  def dom(self) -> JsHtml.JsHtmlButtonChecks:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript available for a DOM element by default.

    :rtype: JsHtml.JsHtmlButtonChecks
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButtonChecks(self, report=self.page)
    return self._dom

  def tooltip(self, value: str, location: str = 'top', options: Optional[dict] = None):
    """
    Description:
    -----------
    Add the Tooltip feature when the mouse is over the component.
    This tooltip version is coming from Bootstrap.

    TODO: Use the options parameter.

    Usage::

      check = page.ui.buttons.check()
      check.tooltip("Tooltip")

    Attributes:
    ----------
    :param str value: The tooltip value.
    :param str location: Optional. The location of the tooltip compared to the HTML component.
    :param Optional[dict] options: Optional. The tooltip options (not used yet)
    """
    self.options.tooltip = value
    self.options.tooltip_options = options
    return self

  _js__builder__ = '''htmlObj = %(jquery)s; htmlObj.empty(); data.forEach(function(rec){
        if (rec.color == undefined) {rec.color = 'inherit'};
        var style = {'margin': 0, 'color': rec.color, 'display': 'block', 'position': 'relative', 'cursor': 'pointer'};
        if (rec.style != undefined){for(key in rec.style){style[key] = rec.style[key]}};
        if (rec.dsc == undefined) {rec.dsc = ''};
        if (rec.name == undefined) {rec.name = rec.value};
        var strCss = []; for (key in style){strCss.push(key +":"+ style[key])};
        if (rec.checked){
          var spanContent = '<span data-content="'+ rec.value +'" style="display:inline-block;float:left;margin:0"><i class="'+ options.icon + '" style="margin:2px"></i></span><p style="margin:0;padding:0" title="'+ rec.dsc +'">' + rec.name + '</p>'}
        else {var spanContent = '<span data-content="'+ rec.value +'" style="width:16px;display:inline-block;float:left;margin:0">&nbsp;</span><p style="margin:0" title="'+ rec.dsc +'">' + rec.name + '</p>'}     
        htmlObj.append($('<label style="'+ strCss.join(";") +'">'+ spanContent +'</label>'))}); htmlObj.tooltip(); 
        if (options.tooltip != ""){
          var tip = $('<i class="fas fa-info-circle" style="right:0" title="'+ options.tooltip +'"></i>') ;
          tip.tooltip(); htmlObj.append($("<div style='width:100%%;text-align:right'></div>").append(tip) )}
      ''' % {"jquery": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None,
            source_event: str = "$(document)", on_ready: bool = False):
    """
    Description:
    -----------
    Add a click event on the checkbox component.

    TODO: Find way to remove jquery

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: Optional. The source target for the event.
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    agg_js_fncs = '''
      if(($(this).find("i").attr("class") !== undefined) && ($(this).find("i").attr("class").includes('fas fa-times'))){
        return {}};
      var useAsync = false; var isChecked = false; var htmlContent = $(this).find('span').find('i').length; 
      if (htmlContent == 0) {$(this).find('span').html('<i class="%(icon)s" style="padding:2px"></i>'); 
      isChecked = true} else {$(this).find('span').html('<div style="width:16px;display:inline-block">&nbsp;</div>')};
      %(jsFnc)s
    ''' % {"jsFnc": JsUtils.jsConvertFncs(js_funcs, toStr=True), "icon": self.options.icon}
    self._browser_data['mouse'].setdefault("click", {}).setdefault(source_event, {}).setdefault("content", []).extend(
      [agg_js_fncs])
    self._browser_data['mouse']["click"][source_event]['sub_items'] = '#%s label' % self.htmlCode
    self._browser_data['mouse']["click"][source_event]['profile'] = profile
    return self

  def __str__(self):
    if self.options.all_selected:
      self.page.body.onReady([self.dom.check(True)])
    self.page.properties.js.add_builders(self.refresh())
    return '<div %(strAttr)s><div name="checks"></div></div>' % {
      'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class CheckButton(Html.Html):
  name = 'Check Button'
  _option_cls = OptButton.OptCheck

  def __init__(self, report: primitives.PageModel, flag: bool = False, tooltip: Optional[str] = None,
               width: Optional[tuple] = None, height: Optional[tuple] = None, icon: Optional[str] = None,
               label: Optional[str] = None, html_code: Optional[str] = None,
               options: Optional[dict] = None, profile: Optional[Union[bool, dict]] = None):
    super(CheckButton, self).__init__(report, 'Y' if flag else 'N', html_code=html_code, options=options,
                                      css_attrs={"width": width, "height": height}, profile=profile)
    self.input = report.ui.images.icon(self.options.icon_check if flag else self.options.icon_not_check).css(
      {"width": report.body.style.globals.font.normal()})
    self.input.style.css.color = self.page.theme.success[1] if flag else self.page.theme.danger[1]
    self.input.style.css.middle()
    self.input.options.managed = False
    self.add_label(label, {"width": "none", "float": "none"}, html_code=self.htmlCode, position="after")
    self.add_icon(icon, {"float": 'none'}, html_code=self.htmlCode, position="after", family=options.get("icon_family"))
    if tooltip is not None:
      self.tooltip(tooltip)

  @property
  def options(self) -> OptButton.OptCheck:
    """
    Description:
    -----------
    Property to set all the possible object for check button.

    :rtype: OptButton.OptCheck
    """
    return super().options

  @property
  def dom(self) -> JsHtml.JsHtmlButtonMenu:
    """
    Description:
    ------------
    The Javascript Dom object.

    :rtype: JsHtml.JsHtmlButtonMenu
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButtonMenu(self, report=self.page)
    return self._dom

  @property
  def js(self) -> JsComponents.CheckButton:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    :return: A Javascript Dom object

    :rtype: JsComponents.CheckButton
    """
    if self._js is None:
      self._js = JsComponents.CheckButton(self, report=self.page)
    return self._js

  _js__builder__ = ''' htmlObj.innerHTML = '';
      if (data === true || data == 'Y'){
        var i = document.createElement("i");
        i.classList.add(...options.icon_check.split(' '));
        i.style.color = options.green; i.style.marginBottom = '2px'; i.style.marginLeft = '2px';
        htmlObj.appendChild(i); htmlObj.parentNode.setAttribute('data-isChecked', true)}
      else {
        var i = document.createElement("i");
        i.classList.add(...options.icon_not_check.split(' '));
        i.style.color = options.red; i.style.marginBottom = '2px'; i.style.marginLeft = '2px';
        htmlObj.appendChild(i); htmlObj.parentNode.setAttribute('data-isChecked', false)
      }'''

  @property
  def style(self) -> GrpClsButton.ClassButtonCheckBox:
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsButton.ClassButtonCheckBox
    """
    if self._styleObj is None:
      self._styleObj = GrpClsButton.ClassButtonCheckBox(self)
    return self._styleObj

  def click(self, js_fnc_true: Union[list, str], js_fnc_false: Optional[Union[list, str]] = None,
            with_colors: bool = True, profile: Optional[Union[dict, bool]] = None, on_ready: bool = False):
    """
    Description:
    ------------
    Click even on the checkbox item.

    Usage::

      ch = page.ui.buttons.check(label="Label")
      ch.click(page.js.alert("true"), page.js.alert("false"))

    Attributes:
    ----------
    :param Union[list, str] js_fnc_true: Js function or a list of JsFunction to be triggered when checked
    :param Optional[Union[list, str]] js_fnc_false: Optional. Js function or a list of JsFunction to be triggered when unchecked
    :param bool with_colors: Optional. Add default colors to the icons.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

    :return: The htmlObj to allow the chaining
    """
    if self.label is not None and hasattr(self.label, 'style'):
      self.label.style.css.cursor = 'pointer'
    self.style.css.cursor = "pointer"
    if not isinstance(js_fnc_true, list):
      js_fnc_true = [js_fnc_true]
    if js_fnc_false is None:
      js_fnc_false = []
    elif not isinstance(js_fnc_false, list):
      js_fnc_false = [js_fnc_false]
    if with_colors:
      js_fnc_true.append(self.input.dom.css({"color": self.page.theme.success[1]}).r)
      js_fnc_false.append(self.input.dom.css({"color": self.page.theme.danger[1]}).r)
    js_fncs = [
      self.input.dom.switchClass(self.options.icon_check.split(" ")[-1],
                                 self.options.icon_not_check.split(" ")[-1]),
      JsIf.JsIf(self.input.dom.hasClass(self.options.icon_check.split(" ")[-1]), js_fnc_true).else_(js_fnc_false)]
    return super(CheckButton, self).click(js_fncs, profile, on_ready=on_ready)

  def __str__(self):
    return '''<div %s>%s</div>''' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.input.html())


class IconEdit(Html.Html):
  name = 'Icon'

  def __init__(self, report: primitives.PageModel, position, icon: Optional[str], text: Optional[str],
               tooltip: Optional[str], width, height, html_code, options, profile: Optional[Union[bool, dict]]):
    super(IconEdit, self).__init__(report, '', html_code=html_code, profile=profile,
                                   css_attrs={"width": width, 'height': height,
                                              'float': 'left' if position is None else position})
    if tooltip is not None:
      self.tooltip(tooltip)
    # Add the internal components icons and helper
    self.add_span(text)
    notches = options.get("font-factor", 0)
    if width[0] is not None and width[1] == 'px':
      self.add_icon(icon, {"margin": "2px", 'font-size': "%s%s" % (width[0]-notches, width[1])},
                    html_code=self.htmlCode, family=options.get("icon_family"))
    else:
      self.add_icon(icon, {"margin": "2px", 'font-size': self.page.body.style.globals.font.normal(-notches)},
                    html_code=self.htmlCode, family=options.get("icon_family"))
    self.hover_color = True

  def spin(self):
    """
    Description:
    ------------
    Add a spin effect to the icon.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.spin()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons
    """
    self.icon.spin()
    return self

  def pulse(self):
    """
    Description:
    ------------
    Add a pulse effect to the icon.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.pulse()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons
    """
    self.icon.pulse()
    return self

  def border(self):
    """
    Description:
    ------------
    Add a border to the icon.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.border()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons
    """
    self.icon.border()
    return self

  def rotate(self, angle: int):
    """
    Description:
    ------------
    To arbitrarily rotate and flip icons, use the fa-rotate-* and fa-flip-* classes when you reference an icon.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.rotate(90)

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/rotating-icons

    Attributes:
    ----------
    :param int angle: The rotation angle.
    """
    self.icon.rotate(angle)
    return self

  def pull(self, position: str = 'left'):
    """
    Description:
    ------------
    Use fa-border and fa-pull-right or fa-pull-left for easy pull quotes or article icons.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.pull()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons

    Attributes:
    ----------
    :param str position: Optional. The position of the icon in the page.
    """
    self.icon.pull(position)
    return self

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    -----------
    Add a JavaScript click event on this component.

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] source_event: Optional. The source target for the event.
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if self.hover_color:
      if self.hover_color == 'danger':
        self.icon.style.add_classes.div.danger_hover()
      else:
        self.icon.style.add_classes.icon.basic()
    return super(IconEdit, self).click(js_funcs, profile, source_event, on_ready=on_ready)

  def goto(self, url: str, js_funcs: Optional[Union[list, str]] = None, profile: Optional[Union[bool, dict]] = None,
           target: str = "_blank", source_event: Optional[str] = None):
    """
    Description:
    -----------
    Create a link to a new page when component is clicked.

    Related Pages:

      https://www.w3schools.com/tags/att_a_target.asp

    Attributes:
    ----------
    :param str url: The target url.
    :param Optional[Union[list, str]] js_funcs: Optional. Javascript functions.
    :param str target: Optional. The type of link in the browser (new tab or same one).
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] source_event: Optional. The event source reference.
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.js.location.open_new_tab(url, target))
    return self.click(js_funcs, profile, source_event)

  def __str__(self):
    return "<span %s></span>" % (self.get_attrs(pyClassNames=self.style.get_classes()))


class Buttons(Html.Html):
  name = 'Buttons'

  def __init__(self, report: primitives.PageModel, data, color: Optional[str], width: tuple, height: tuple,
               html_code: Optional[str], helper: Optional[str], options: Optional[dict],
               profile: Optional[Union[bool, dict]]):
    super(Buttons, self).__init__(report, [], html_code=html_code,
                                  css_attrs={"width": width, "height": height, 'color': color}, profile=profile)
    for b in data:
      bt = report.ui.button(b, options={"group": "group_%s" % self.htmlCode}).css({"margin-right": '5px'})
      bt.css(options.get("button_css", {}))
      self.__add__(bt)
    self.add_helper(helper)

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else v for v in self.val])
    return '<div %s>%s</div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), str_div, self.helper)


class ButtonMenuItem:
  name = 'Button Menu Item'

  def __init__(self, report: primitives.PageModel, selector: str, parent: Html.Html):
    self._report, self._selector, self.page = report, selector, report
    self._src, self._js, self._events = parent, None, []

  @property
  def js(self) -> JsComponents.Menu:
    """
    Description:
    -----------
    Javascript module of the items in the menu.

    :return: A Javascript Dom object

    :rtype: JsComponents.Menu
    """
    if self._js is None:
      self._js = JsComponents.Menu(self._src, varName=self._selector, report=self.page)
    return self._js

  def on(self, event: str, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
         source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    -----------
    Javascript generic events of the items in the menu.

    Attributes:
    ----------
    :param str event: The JavaScript event.
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] source_event: Optional. Override the source component on which the component is defined.
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._events.append("%s.addEventListener('%s', function (event) {%s})" % (
      source_event or self._selector, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    if on_ready:
      self.page.body.onReady([self._selector.dom.events.trigger(event)])
    return self._src

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    -----------
    Javascript click events of the items in the menu.

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[Union[bool, dict]] profile: Boolean. Optional. A flag to set the component performance storage.
    :param str source_event: Optional. Override the source component on which the component is defined.
    :param bool on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    return self.on("click", js_funcs, profile, source_event, on_ready)


class ButtonMenu(Html.Html):
  name = 'Button Menu'

  def __init__(self, report: primitives.PageModel, record, text: str, icon: Optional[str], width: Optional[tuple],
               height: Optional[tuple], html_code: Optional[str], tooltip: Optional[str],
               profile: Optional[Union[bool, dict]], options: Optional[dict]):
    super(ButtonMenu, self).__init__(report, record, html_code=html_code, profile=profile,
                                     css_attrs={"width": width, "height": height})
    self.button = report.ui.button(text, icon, width, height, html_code, tooltip, profile, options)
    self.button.options.managed = False
    self.set_attrs(name="data-count", value=0)
    self.style.css.position = "relative"
    self.style.css.display = "inline-block"
    self.container = report.ui.div()
    self.container.options.managed = False
    self._jsStyles = {"padding": '5px', 'cursor': 'pointer', 'display': 'block'}

  def __getitem__(self, i: int):
    if i not in self.components:
      self.components[i] = ButtonMenuItem(self.page, "document.getElementById('%s').querySelectorAll('a')[%s]" % (
        self.htmlCode, i), self)
    return self.components[i]

  _js__builder__ = '''
      var panel = htmlObj.querySelector("div");
      data.forEach(function(rec){
        var href = document.createElement("a"); href.innerHTML = rec;
        Object.keys(options).forEach(function(key){href.style[key] = options[key]});
        panel.appendChild(href)})'''

  @property
  def style(self) -> GrpClsButton.ClassButtonMenu:
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    Usage::

      self.style.css.margin = "5px"

    :rtype: GrpClsButton.ClassButtonMenu
    """
    if self._styleObj is None:
      self._styleObj = GrpClsButton.ClassButtonMenu(self)
    return self._styleObj

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    events = []
    for comp in self.components.values():
      events.extend(comp._events)
    self.onReady(events)
    return '<div %s>%s%s</div>' % (
      self.get_attrs(pyClassNames=self.style.get_classes()), self.button.html(), self.container.html())


class ButtonMore(Html.Html):
  name = 'Button More'

  def __init__(self, report: primitives.PageModel, record, text: Optional[str], width: Optional[tuple],
               height: Optional[tuple], html_code: Optional[str], tooltip: Optional[str],
               profile: Optional[Union[bool, dict]], options: Optional[dict]):
    super(ButtonMore, self).__init__(
      report, "", html_code=html_code, profile=profile, css_attrs={"width": width, "height": height})
    self.text = self.page.ui.text(text, width=("auto", ''), profile=profile)
    self.text.style.css.font_factor(-4)
    self.text.style.css.italic()
    self.text.style.css.display = "inline-block"
    self.text.style.css.text_align = "center"
    self.button = self.page.ui.button(
      text=self.text, icon="fas fa-chevron-down", width=width, height=height, align="center", html_code=html_code,
      tooltip=tooltip, profile=profile, options=options)
    self.button.style.css.border_radius = 5
    self.button.style.css.text_align = 'left'
    self.button.style.css.display = 'inline-block'
    self.button.icon.style.add_classes.div.border_hover()
    self.button.options.managed = False
    self.button.style.css.padding = "0 5px"
    self.menu = self.page.ui.lists.links(record, width=("auto", ""), profile=profile)
    self.menu.options.managed = False
    self.menu.style.css.background = "white"
    self.menu.style.css.z_index = 10
    self.menu.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    self.menu.attr["data-anchor"] = "test_filter"
    self.menu.style.css.invisible()
    self.menu.style.css.position = "absolute"
    self.menu.style.css.top = 25
    self.menu.style.css.left = 5
    self.menu.style.css.padding = "2px 5px"
    self.menu.attr["tabIndex"] = 0
    self.style.css.position = "relative"
    self.style.css.display = "inline-block"
    self.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    self.style.css.border_radius = 10
    self.button.icon.click([
      self.page.js.objects.event.stopPropagation(), self.menu.dom.visible(), self.menu.dom.events.trigger("focus")])
    self.menu.focusout([
      self.page.js.objects.event.stopPropagation(), self.page.js.objects.event.preventDefault(),
      self.menu.dom.invisible()])

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    return self.text.click(js_funcs, profile, source_event, on_ready)

  def __str__(self):
    return '<div %s>%s%s</div>' % (
      self.get_attrs(pyClassNames=self.style.get_classes()), self.button.html(), self.menu.html())


class ButtonFilter(Html.Html):
  name = 'Button Filter'
  _option_cls = OptButton.OptionsButtonFilter

  def __init__(self, report: primitives.PageModel, text: str, width: tuple, height: tuple, html_code: str,
               tooltip: str, profile: Optional[Union[bool, dict]], options: Optional[dict]):
    super(ButtonFilter, self).__init__(
      report, "", html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.text = self.page.ui.text(text, tooltip=tooltip)
    self.text.draggable()
    self.text.style.css.margin_right = 5
    self.text.options.managed = False

    self.icon_filer = self.page.ui.icon(self.options.icon_filer)
    self.icon_filer.style.css.font_factor(-4)
    self.icon_filer.style.css.margin_right = 15
    self.icon_filer.style.css.invisible()
    self.icon_filer.options.managed = False

    self.icon = self.page.ui.icon(self.options.icon)
    self.icon.options.managed = False
    self.icon.style.css.position = "absolute"
    self.icon.style.css.right = 0
    self.icon.style.css.padding = 5
    self.icon.style.css.font_factor(-4)

    filter_categories = [{"text": category, "value": Html.cleanData(category)} for category in options["categories"]]
    self.select = self.page.ui.select(
      filter_categories, width=(180, 'px'), options={"empty_selected": False}, html_code="%s_select" % self.htmlCode)
    self.input = self.page.ui.input(placeholder="Filter", html_code="%s_input" % self.htmlCode)
    self.input.style.css.text_align = "left"
    self.input.attr["type"] = "number" if self.options.is_number else "text"
    self.input.style.css.padding_left = 5
    self.radios = self.page.ui.radio(
      [{"value": "and"}, {"value": "or"}], align="center", html_code="%s_radio" % self.htmlCode)
    self.radios.attr["data-anchor"] = "test_filter"
    self.radios.style.css.hide()

    self.select2 = self.page.ui.select(
      filter_categories, width=(180, 'px'), options={"empty_selected": False}, html_code="%s_select2" % self.htmlCode)
    self.select2.style.css.hide()

    self.input2 = self.page.ui.input(placeholder="Filter", html_code="%s_input2" % self.htmlCode)
    self.input2.style.css.hide()
    self.input2.attr["type"] = "number" if self.options.is_number else "text"

    self.menu = self.page.ui.div([self.select, self.input, self.radios, self.select2, self.input2], width=(200, 'px'))
    self.menu.style.css.background = "white"
    self.menu.style.css.padding = 10
    self.menu.style.css.z_index = 10
    self.menu.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    self.menu.attr["data-anchor"] = "test_filter"
    self.menu.style.css.invisible()
    self.menu.style.css.position = "absolute"
    self.menu.style.css.top = 20
    self.menu.style.css.right = -180
    self.menu.attr["tabIndex"] = 0
    self.menu.options.managed = False

    self.select.change([self.menu.dom.visible()])
    self.select2.change([self.menu.dom.visible()])

    self.icon_filer.click([
      self.input.dom.empty(), self.input2.dom.empty(), self.radios.dom.hide(),
      self.icon_filer.dom.invisible(), self.input2.dom.hide(), self.select2.dom.hide()
    ])
    self.icon.click([
      self.page.js.objects.event.stopPropagation(), self.menu.dom.visible(), self.menu.dom.events.trigger("focus")])

    self.input.enter([self.menu.dom.invisible()])

    self.style.css.position = "relative"
    self.style.css.display = "inline-block"
    self.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    self.style.css.border_radius = 10
    self.style.css.padding = "0 5px"

    self.input.keyup.any([
      self.input.js.isEmpty([
        self.icon_filer.dom.invisible(),
        self.radios.dom.hide(), self.input2.dom.hide(), self.select2.dom.hide()]).else_([
          self.icon_filer.dom.visible(), self.radios.dom.show(), self.input2.dom.show(), self.select2.dom.show()
      ])
    ])

    self.menu.focusout([
      self.page.js.objects.event.stopPropagation(),
      self.page.js.objects.event.preventDefault(),
      self.menu.dom.invisible()])

  @property
  def options(self) -> OptButton.OptionsButtonFilter:
    """
    Description:
    -----------
    Property to set all the possible object for a button.

    Usage::

      but = page.ui.button("Click Me")
      but.options.multiple = False

    :rtype: OptButton.OptionsButtonFilter
    """
    return super().options

  @property
  def dom(self) -> JsHtml.JsHtmlButtonFilter:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript available for a DOM element by default.

    Usage::

      but = page.ui.button("Click Me")
      page.js.console.log(but.dom.content)

    :rtype: JsHtml.JsHtmlButtonFilter
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButtonFilter(self, report=self.page)
    return self._dom

  def __str__(self):
    events = []
    for comp in self.components.values():
      events.extend(comp._events)
    self.onReady(events)
    return '<div %s>%s%s%s%s</div>' % (
      self.get_attrs(pyClassNames=self.style.get_classes()), self.text.html(), self.icon_filer.html(), self.icon.html(),
      self.menu.html())


class ButtonData(Button):
  name = 'button data'

  def __init__(self, report: primitives.PageModel, text: Optional[str] = None, icon: Optional[str] = None,
               width: Optional[tuple] = None, height: Optional[tuple] = None, html_code: Optional[str] = None,
               tooltip: Optional[str] = None, profile=None, options: Optional[dict] = None):
    super(ButtonData, self).__init__(report, text, icon, width, height, html_code, tooltip, profile, options)
    self.set_attrs(name="data-content", value="")
    self.filename = None

  _js__builder__ = '''
    htmlObj.setAttribute("data-content", JSON.stringify(data));
    htmlObj.setAttribute("title", ""+ data.length + " row loaded: " + (new Date()).toISOString().slice(0, 19).replace("T", " "));
    if(data.length > 0){htmlObj.style.visibility = "visible"}
    '''

  def download(self):
    return self.click([self.page.js.location.download(self.page.js.location.getUrlFromArrays(
      self.js.json.parse(self.dom.getAttribute("data-content"))), self.filename)])
