#!/usr/bin/python
# -*- coding: utf-8 -*-
# TODO Add JS builder to Button Filter

from typing import Union, Optional
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.html.options import OptButton
from epyk.core.html import Defaults as Default_html

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils
from epyk.core.js.statements import JsIf
from epyk.core.js.objects import JsComponents

# The list of CSS classes
from epyk.core.css.styles import GrpClsButton


class Button(Html.Html):
  name = 'button'
  _option_cls = OptButton.OptionsButton

  def __init__(self, page: primitives.PageModel, text: str = None, icon: str = None, width: Optional[tuple] = None,
               height: Optional[tuple] = None, html_code: Optional[str] = None, tooltip: Optional[str] = None,
               profile: Optional[Union[dict, bool]] = None, options: Optional[dict] = None):
    text = text or []
    if not isinstance(text, list):
      text = [text]
    for obj in text:
      if hasattr(obj, 'options'):
        obj.options.managed = False
    super(Button, self).__init__(
      page, text, html_code=html_code, options=options, profile=profile, css_attrs={"width": width, "height": height})
    self.add_icon(icon, html_code=self.htmlCode)
    if icon is not None and not text:
      self.icon.style.css.margin_right = None
    if icon is not None:
      self.icon.style.css.color = "inherit"
    self.tooltip(tooltip)
    self.set_attrs(name="data-count", value=0)

  @property
  def options(self) -> OptButton.OptionsButton:
    """ Property to set all the possible object for a button.

    Usage::

      but = page.ui.button("Click Me")
      but.options.multiple = False
    """
    return super().options

  @property
  def dom(self) -> JsHtml.JsHtmlButton:
    """ Return all the Javascript functions defined for an HTML Component.

    Those functions will use plain javascript available for a DOM element by default.

    Usage::

      but = page.ui.button("Click Me")
      page.js.console.log(but.dom.content)
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButton(component=self, page=self.page)
    return self._dom

  def no_background(self):
    """ Remove the default button background and remove the padding.

    Usage::

      but = page.ui.button("Click Me")
      but.no_background()
    """
    self.style.css.background_color = "#11ffee00"
    return self

  def goto(self, url: str, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
           target: str = "_blank", source_event: Optional[str] = None):
    """ Click event which redirect to another page.

    Usage::

      but = page.ui.button("Click Me")
      but.goto("http://www.epyk-studio.com")

      # Create a link to a page within the same tab
      button2 = page.ui.button("Go go Google")
      button2.goto("www.google.fr", target="_self")
 
    :param url: The destination path
    :param js_funcs: The Javascript Events triggered before the redirection
    :param profile: Optional. A flag to set the component performance storage
    :param target: Optional. The type of link to the next page
    :param source_event: Optional. The event source
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.js.location.open_new_tab(url, target))
    return self.click(js_funcs, profile, source_event)

  @property
  def style(self) -> GrpClsButton.ClassButton:
    """ Property to the CSS Style of the component.

    Usage::

      but = page.ui.button("Click Me")
      but.style.css.margin = "5px"
    """
    if self._styleObj is None:
      self._styleObj = GrpClsButton.ClassButton(self)
    return self._styleObj

  def disable(self, background_color: Optional[str] = None, color: Optional[str] = None):
    """ Add the HTML tag to disable the button.

    Usage::

      but = page.ui.button("Click Me")
      but.disable()
 
    :param background_color: Optional. An hexadecimal color code
    :param color: Optional. A hexadecimal color code

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

  def press(self, js_press_funcs: types.JS_FUNCS_TYPES = None, js_release_funcs: types.JS_FUNCS_TYPES = None,
            profile: types.PROFILE_TYPE = None, on_ready: bool = False):
    """ Special click event to keep in memory the state of the component.

    Usage::

      but = page.ui.button("Click Me")
 
    :param js_press_funcs: Optional. Javascript functions
    :param js_release_funcs: Optional. Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param on_ready: Optional. Event when component is ready on HTML side
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
    """ Change the color of the button background when the mouse is hover.

    Usage::

      page.ui.buttons.remove("remove").color("blue")
 
    :param color: the color of the component (text and borders)
    """
    self.style.css.border = "1px solid {}".format(color)
    self.set_attrs(name="onmouseover", value="this.style.backgroundColor='%s';this.style.color='white'" % color)
    self.set_attrs(name="onmouseout", value="this.style.backgroundColor=\'white\';this.style.color=\'%s\';" % color)
    return self

  def properties(self) -> dict:
    """ Return the full properties of the HTML component.

    This property should allow another JavaScript framework to build the component.

    Usage::

      but = page.ui.button("Click Me")
      but.properties
    """
    return {"tag": self.name, 'selector': self.htmlCode}

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    self.onReady([self.dom.setAttribute("data-content", self.dom.content)])
    return '<button {attrs}>{content}</button>'.format(
      attrs=self.get_attrs(css_class_names=self.style.get_classes()), content=str_div)

  def loading(self, status: bool = True, label: str = None,
              data: types.JS_DATA_TYPES = None, disable: bool = True):
    """ Display a loading message in the component.

    Usage::

      btn.click([
          t.loading(True, label="`Loading: ${data.result}`", data={"result": "Waiting for response"}),
      ])

    :param status: The message status (true is active)
    :param label: The message template
    :param data: The message parameter to feed the template
    :param disable: Disable the button
    """
    if label is not None:
      self.options.templateLoading = label
    if self.options.templateLoading is None:
      self.options.templateLoading = Default_html.TEMPLATE_LOADING_ONE_LINE
    if status:
      if disable:
        return self.dom.disable() + self.build(data, options={"templateMode": 'loading'})

      return self.build(data, options={"templateMode": 'loading'})

    if data is None:
      if disable:
        return self.dom.disable(False) + self.dom.innerHTML(self.dom.getAttribute("data-content"))

      return self.dom.innerHTML(self.dom.getAttribute("data-content"))

    if disable:
      return self.dom.disable(False) + self.build(data)

    return self.build(data)

  def error(self, status: bool = True, label: str = None,
            data: types.JS_DATA_TYPES = None, disable: bool = True):
    """ Display an error message in the component.

    Usage::

      btn.click([
          t.error(True, label="`Error: ${data.result}`", data={"result": "Wrong Parameter"}),
      ])

    :param status: The message status (true is active)
    :param label: The message template
    :param data: The message parameter to feed the template
    :param disable: Disable the button
    """
    if label is not None:
      self.options.templateError = label
    if self.options.templateError is None:
      self.options.templateError = Default_html.TEMPLATE_ERROR_ONE_LINE
    if status:
      if disable:
        return self.dom.disable(True) + self.build(data, options={"templateMode": 'error'})

      return self.build(data, options={"templateMode": 'error'})

    if data is None:
      if disable:
        return self.dom.disable(False) + self.dom.innerHTML(self.dom.getAttribute("data-content"))

      return self.dom.innerHTML(self.dom.getAttribute("data-content"))

    if disable:
      return self.dom.disable(False) + self.build(data)

    return self.build(data)


class Checkbox(Html.Html):
  name = 'Check Box'
  requirements = ('font-awesome', 'bootstrap', 'jquery')
  _option_cls = OptButton.OptCheckboxes

  def __init__(self, page: primitives.PageModel, records, color: Optional[str], width: Optional[tuple],
               height: Optional[tuple], align: Optional[str],  html_code: Optional[str],  tooltip: Optional[str],
               options: Optional[dict], profile: Optional[Union[dict, bool]]):
    if page.inputs.get(html_code) is not None:
      selected_vals = set(page.inputs[html_code].split(","))
      for rec in records:
        if rec["value"] in selected_vals:
          rec["checked"] = True
    super(Checkbox, self).__init__(page, records, html_code=html_code, options=options,
                                   css_attrs={"width": width, "height": height}, profile=profile)
    self.css({'text-align': align, 'color': 'inherit' if color is None else color, 'padding': '5px'})
    if tooltip:
      self.tooltip(tooltip)

  @property
  def options(self) -> OptButton.OptCheckboxes:
    """ Property to set all the possible object for check boxes. """
    return super().options

  @property
  def dom(self) -> JsHtml.JsHtmlButtonChecks:
    """ Return all the Javascript functions defined for an HTML Component.

    Those functions will use plain javascript available for a DOM element by default.

    Usage::

      data = [
        {"value": "Test 1", "checked": True, "name": 'name'},
        {"value": "Test 2", "dsc": 'description'},
      ]
      cb = page.ui.buttons.checkboxes(data)

      b = page.ui.button("Add")
      b.click([cb.dom.add([{"value": "test"}])])
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButtonChecks(self, page=self.page)
    return self._dom

  def tooltip(self, value: str, location: str = 'top', options: Optional[dict] = None):
    """ Add the Tooltip feature when the mouse is over the component.

    This tooltip version is coming from Bootstrap.

    TODO: Use the options parameter.

    Usage::

      check = page.ui.buttons.check()
      check.tooltip("Tooltip")
 
    :param value: The tooltip value
    :param location: Optional. The location of the tooltip compared to the HTML component
    :param options: Optional. The tooltip options (not used yet)
    """
    self.options.tooltip = value
    self.options.tooltip_options = options
    return self

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None,
            source_event: str = "$(document)", on_ready: bool = False):
    """ Add a click event on the checkbox component.

    TODO: Find way to remove jquery
 
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param source_event: Optional. The source target for the event
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
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
      'strAttr': self.get_attrs(css_class_names=self.style.get_classes())}


class CheckButton(Html.Html):
  name = 'Check Button'
  _option_cls = OptButton.OptCheck

  def __init__(self, page: primitives.PageModel, flag: bool = False, tooltip: Optional[str] = None,
               width: Optional[tuple] = None, height: Optional[tuple] = None, icon: Optional[str] = None,
               label: Optional[str] = None, html_code: Optional[str] = None,
               options: Optional[dict] = None, profile: Optional[Union[bool, dict]] = None):
    super(CheckButton, self).__init__(page, 'Y' if flag else 'N', html_code=html_code, options=options,
                                      css_attrs={"width": width, "height": height}, profile=profile)
    self.input = page.ui.images.icon(self.options.icon_check if flag else self.options.icon_not_check).css(
      {"width": page.body.style.globals.font.normal()})
    self.input.style.css.color = self.page.theme.success.base if flag else self.page.theme.danger.base
    self.input.style.css.middle()
    self.input.options.managed = False
    self.add_label(label, {"width": "none", "float": "none"}, html_code=self.htmlCode, position="after")
    self.add_icon(icon, {"float": 'none'}, html_code=self.htmlCode, position="after", family=options.get("icon_family"))
    if tooltip is not None:
      self.tooltip(tooltip)

  @property
  def options(self) -> OptButton.OptCheck:
    """ Property to set all the possible object for check button. """
    return super().options

  @property
  def dom(self) -> JsHtml.JsHtmlButtonMenu:
    """ The Javascript Dom object. """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButtonMenu(self, page=self.page)
    return self._dom

  @property
  def js(self) -> JsComponents.CheckButton:
    """ The Javascript functions defined for this component.

    Those can be specific ones for the module or generic ones from the language.

    :return: A Javascript Dom object
    """
    if self._js is None:
      self._js = JsComponents.CheckButton(self, page=self.page)
    return self._js

  @property
  def style(self) -> GrpClsButton.ClassButtonCheckBox:
    """ Property to the CSS Style of the component. """
    if self._styleObj is None:
      self._styleObj = GrpClsButton.ClassButtonCheckBox(self)
    return self._styleObj

  def click(self, js_fnc_true: types.JS_FUNCS_TYPES, js_fnc_false: Optional[Union[list, str]] = None,
            with_colors: bool = True, profile: types.PROFILE_TYPE = None, on_ready: bool = False):
    """ Click even on the checkbox item.

    Usage::

      ch = page.ui.buttons.check(label="Label")
      ch.click(page.js.alert("true"), page.js.alert("false"))
 
    :param js_fnc_true: Js function or a list of JsFunction to be triggered when checked
    :param js_fnc_false: Optional. Js function or a list of JsFunction to be triggered when unchecked
    :param with_colors: Optional. Add default colors to the icons.
    :param profile: Optional. A flag to set the component performance storage
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded

    :return: The component to allow the chaining
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
      js_fnc_true.append(self.input.dom.css({"color": self.page.theme.success.base}).r)
      js_fnc_false.append(self.input.dom.css({"color": self.page.theme.danger.base}).r)
    js_fncs = [
      self.input.dom.switchClass(self.options.icon_check.split(" ")[-1],
                                 self.options.icon_not_check.split(" ")[-1]),
      JsIf.JsIf(self.input.dom.hasClass(self.options.icon_check.split(" ")[-1]), js_fnc_true).else_(js_fnc_false)]
    return super(CheckButton, self).click(js_fncs, profile, on_ready=on_ready)

  def __str__(self):
    return '''<div %s>%s</div>''' % (self.get_attrs(css_class_names=self.style.get_classes()), self.input.html())


class IconEdit(Html.Html):
  name = 'Icon'

  def __init__(self, page: primitives.PageModel, position, icon: Optional[str], text: Optional[str],
               tooltip: Optional[str], width, height, html_code, options, profile: Optional[Union[bool, dict]]):
    super(IconEdit, self).__init__(
      page, '', html_code=html_code, profile=profile, css_attrs={
        "width": width, 'height': height, 'float': 'left' if position is None else position})
    if tooltip is not None:
      self.tooltip(tooltip)
    # Add the internal components icons and helper
    self.add_span(text)
    notches = options.get("font-factor", 0)
    if width[0] is not None and width[1] == 'px':
      self.add_icon(icon, {"margin-right": "None", "margin": "2px", 'font-size': "%s%s" % (width[0]-notches, width[1])},
                    html_code=self.htmlCode, family=options.get("icon_family"))
    else:
      self.add_icon(icon, {"margin-right": "None", "margin": "2px", 'font-size': self.page.body.style.globals.font.normal(-notches)},
                    html_code=self.htmlCode, family=options.get("icon_family"))
    self.hover_color = True

  def spin(self):
    """ Add a spin effect to the icon.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.spin()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons
    """
    self.icon.spin()
    return self

  def pulse(self):
    """ Add a pulse effect to the icon.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.pulse()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons
    """
    self.icon.pulse()
    return self

  def border(self):
    """ Add a border to the icon.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.border()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons
    """
    self.icon.border()
    return self

  def rotate(self, angle: int):
    """ To arbitrarily rotate and flip icons, use the fa-rotate-* and fa-flip-* classes when you reference an icon.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.rotate(90)

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/rotating-icons
 
    :param angle: The rotation angle
    """
    self.icon.rotate(angle)
    return self

  def pull(self, position: str = 'left'):
    """ Use fa-border and fa-pull-right or fa-pull-left for easy pull quotes or article icons.

    Usage::

      icon = page.ui.icons.awesome("")
      icon.pull()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons
 
    :param position: Optional. The position of the icon in the page
    """
    self.icon.pull(position)
    return self

  def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """ Add a JavaScript click event on this component.
 
    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param source_event: Optional. The source target for the event
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if self.hover_color:
      if self.hover_color == 'danger':
        self.icon.style.add_classes.div.danger_hover()
      else:
        self.icon.style.add_classes.icon.basic()
    return super(IconEdit, self).click(js_funcs, profile, source_event, on_ready=on_ready)

  def goto(self, url: str, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
           target: str = "_blank", source_event: Optional[str] = None):
    """ Create a link to a new page when component is clicked.

    Related Pages:

      https://www.w3schools.com/tags/att_a_target.asp

    :param url: The target url
    :param js_funcs: Optional. Javascript functions
    :param target: Optional. The type of link in the browser (new tab or same one)
    :param profile: Optional. A flag to set the component performance storage
    :param source_event: Optional. The event source reference
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.js.location.open_new_tab(url, target))
    return self.click(js_funcs, profile, source_event)

  def __str__(self):
    return "<span %s></span>" % (self.get_attrs(css_class_names=self.style.get_classes()))


class Buttons(Html.Html):
  name = 'Buttons'

  def __init__(self, page: primitives.PageModel, data, color: Optional[str], width: tuple, height: tuple,
               html_code: Optional[str], helper: Optional[str], options: Optional[dict],
               profile: Optional[Union[bool, dict]]):
    super(Buttons, self).__init__(page, [], html_code=html_code,
                                  css_attrs={"width": width, "height": height, 'color': color}, profile=profile)
    for b in data:
      bt = page.ui.button(b, options={"group": "group_%s" % self.htmlCode}).css({"margin-right": '5px'})
      bt.css(options.get("button_css", {}))
      self.__add__(bt)
    self.add_helper(helper)

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else v for v in self.val])
    return '<div %s>%s</div>%s' % (self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.helper)


class ButtonMenuItem:
  name = 'Button Menu Item'

  def __init__(self, page: primitives.PageModel, component_id: str, container: Html.Html):
    self.component_id, self.page = component_id, page
    self.container, self._js, self._events = container, None, []

  @property
  def js(self) -> JsComponents.Menu:
    """ Javascript module of the items in the menu.

    :return: A Javascript Dom object
    """
    if self._js is None:
      self._js = JsComponents.Menu(self.container, js_code=self.component_id, page=self.page)
    return self._js

  def on(self, event: str, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
         source_event: Optional[str] = None, on_ready: bool = False):
    """ Javascript generic events of the items in the menu.
 
    :param event: The JavaScript event
    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param source_event: Optional. Override the source component on which the component is defined
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._events.append("%s.addEventListener('%s', function (event) {%s})" % (
      source_event or self.component_id, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    if on_ready:
      self.page.body.onReady([self.page.js.getElementById(self.component_id).dom.events.trigger(event)])
    return self.container

  def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """ Javascript click events of the items in the menu.
 
    :param js_funcs: The Javascript functions
    :param profile: Boolean. Optional. A flag to set the component performance storage
    :param source_event: Optional. Override the source component on which the component is defined
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    return self.on("click", js_funcs, profile, source_event, on_ready)


class ButtonMenu(Html.Html):
  name = 'Button Menu'

  def __init__(self, page: primitives.PageModel, record, text: str, icon: Optional[str], width: Optional[tuple],
               height: Optional[tuple], html_code: Optional[str], tooltip: Optional[str],
               profile: Optional[Union[bool, dict]], options: Optional[dict]):
    super(ButtonMenu, self).__init__(page, record, html_code=html_code, profile=profile,
                                     css_attrs={"width": width, "height": height})
    self.button = page.ui.button(text, icon, width, height, html_code, tooltip, profile, options)
    self.button.options.managed = False
    self.set_attrs(name="data-count", value=0)
    self.style.css.position = "relative"
    self.style.css.display = "inline-block"
    self.container = page.ui.div()
    self.container.options.managed = False
    self._jsStyles = {"padding": '5px', 'cursor': 'pointer', 'display': 'block'}

  def __getitem__(self, i: int):
    if i not in self.components:
      self.components[i] = ButtonMenuItem(self.page, "document.getElementById('%s').querySelectorAll('a')[%s]" % (
        self.htmlCode, i), self)
    return self.components[i]

  @property
  def style(self) -> GrpClsButton.ClassButtonMenu:
    """ Property to the CSS Style of the component.

    Usage::

      self.style.css.margin = "5px"
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
      self.get_attrs(css_class_names=self.style.get_classes()), self.button.html(), self.container.html())


class ButtonMore(Html.Html):
  name = 'Button More'

  def __init__(self, page: primitives.PageModel, record, text: Optional[str], width: Optional[tuple],
               height: Optional[tuple], html_code: Optional[str], tooltip: Optional[str],
               profile: Optional[Union[bool, dict]], options: Optional[dict]):
    super(ButtonMore, self).__init__(
      page, "", html_code=html_code, profile=profile, css_attrs={"width": width, "height": height})
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
    self.button.icon.style.css.border_radius = 20
    self.button.icon.style.css.padding = 2
    self.button.icon.style.add_classes.div.color_background_hover(self.page.theme.notch(-3))
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

  def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """ Add an event click to the component.

    Usage::

      b = page.studio.buttons.more([
        {"text": "Item 1"},
        {"text": "Item 2"},
      ], profile=True)

      b.click([page.js.console.log("test")])
 
    :param js_funcs: A Javascript Python function
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console
    :param source_event: Optional. The source target for the event
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
    """
    return self.text.click(js_funcs, profile, source_event, on_ready)

  def __str__(self):
    return '<div %s>%s%s</div>' % (
      self.get_attrs(css_class_names=self.style.get_classes()), self.button.html(), self.menu.html())


class ButtonFilter(Html.Html):
  name = 'Button Filter'
  _option_cls = OptButton.OptionsButtonFilter

  def __init__(self, page: primitives.PageModel, text: str, width: tuple, height: tuple, html_code: str,
               tooltip: str, profile: Optional[Union[bool, dict]], options: Optional[dict]):
    super(ButtonFilter, self).__init__(
      page, "", html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
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
    """ Property to set all the possible object for a button.

    Usage::

      but = page.ui.button("Click Me")
      but.options.multiple = False
    """
    return super().options

  @property
  def dom(self) -> JsHtml.JsHtmlButtonFilter:
    """ Return all the Javascript functions defined for an HTML Component.

    Those functions will use plain javascript available for a DOM element by default.

    Usage::

      but = page.ui.button("Click Me")
      page.js.console.log(but.dom.content)
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButtonFilter(self, page=self.page)
    return self._dom

  def __str__(self):
    events = []
    for comp in self.components.values():
      events.extend(comp._events)
    self.onReady(events)
    return '<div %s>%s%s%s%s</div>' % (
      self.get_attrs(
        css_class_names=self.style.get_classes()), self.text.html(), self.icon_filer.html(), self.icon.html(),
        self.menu.html())


class ButtonData(Button):
  name = 'button data'

  def __init__(self, page: primitives.PageModel, text: Optional[str] = None, icon: Optional[str] = None,
               width: Optional[tuple] = None, height: Optional[tuple] = None, html_code: Optional[str] = None,
               tooltip: Optional[str] = None, profile=None, options: Optional[dict] = None):
    super(ButtonData, self).__init__(page, text, icon, width, height, html_code, tooltip, profile, options)
    self.set_attrs(name="data-content", value="")
    self.filename = None

  def download(self):
    return self.click([self.page.js.location.download(self.page.js.location.getUrlFromArrays(
      self.js.json.parse(self.dom.getAttribute("data-content"))), self.filename)])
