#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptButton

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery
from epyk.core.js.statements import JsIf
from epyk.core.js.objects import JsComponents

# The list of CSS classes
from epyk.core.css.styles import GrpClsButton
from epyk.core.css import Defaults_css


class Button(Html.Html):
  name = 'button'
  _option_cls = OptButton.OptionsButton

  def __init__(self, report, text=None, icon=None, width=None, height=None, html_code=None, tooltip=None, profile=None,
               options=None):
    text = text or []
    if not isinstance(text, list):
      text = [text]
    for obj in text:
      if hasattr(obj, 'options'):
        obj.options.managed = False
    super(Button, self).__init__(report, text, html_code=html_code, options=options, profile=profile,
                                 css_attrs={"width": width, "height": height})
    self.add_icon(icon, html_code=self.htmlCode)
    if icon is not None and not text:
      self.icon.style.css.margin_right = None
    if icon is not None:
      self.icon.style.css.color = "inherit"
    self.tooltip(tooltip)
    self.set_attrs(name="data-count", value=0)

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for a button.

    Usage:
    -----

      but = page.ui.button("Click Me")
      but.options.multiple = False

    :rtype: OptButton.OptionsButton
    """
    return super().options

  @property
  def dom(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript available for a DOM element by default.

    Usage:
    -----

      but = page.ui.button("Click Me")
      page.js.console.log(but.dom.content)

    :rtype: JsHtml.JsHtmlButton
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButton(self, report=self._report)
    return self._dom

  _js__builder__ = "htmlObj.setAttribute('data-processing', false); htmlObj.innerHTML = data"

  def loading(self, status=True):
    """
    Description:
    -----------
    Show / Hide the loading event predefined for this component.

    Usage:
    -----

      but = page.ui.button("Loading")
      page.body.onReady([but.loading()])

    Attributes:
    ----------
    :param status: Boolean. Optional. A flag to specify the status of the loading event.
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

    Usage:
    -----

      but = page.ui.button("Click Me")
      but.no_background()

    """
    self.style.css.background_color = "#11ffee00"
    return self

  def goto(self, url, js_funcs=None, profile=None, target="_blank", source_event=None):
    """
    Description:
    -----------
    Click event which redirect to another page.

    Usage:
    -----

      but = page.ui.button("Click Me")
      but.goto("http://www.epyk-studio.com")

    Attributes:
    ----------
    :param url: String. The destination path.
    :param js_funcs: List | String. Optional. The Javascript Events triggered before the redirection.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param target: String. Optional. The type of link to the next page.
    :param source_event: String. Optional. The event source.
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.js.location.open_new_tab(url, target))
    return self.click(js_funcs, profile, source_event)

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    Usage:
    -----

      but = page.ui.button("Click Me")
      but.style.css.margin = "5px"

    :rtype: GrpClsButton.ClassButton
    """
    if self._styleObj is None:
      self._styleObj = GrpClsButton.ClassButton(self)
    return self._styleObj

  def disable(self, background_color=None, color=None):
    """
    Description:
    -----------
    Add the HTML tag to disable the button.

    Usage:
    -----

      but = page.ui.button("Click Me")
      but.disable()

    Attributes:
    ----------
    :param background_color: String. Optional. An hexadecimal color code.
    :param color: String. Optional. An hexadecimal color code.

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

  def press(self, js_press_funcs=None, js_release_funcs=None, profile=None, on_ready=False):
    """
    Description:
    -----------
    Special click event to keep in memory the state of the component.

    Usage:
    -----

      but = page.ui.button("Click Me")

    Attributes:
    ----------
    :param js_press_funcs: List | String. Optional. Javascript functions.
    :param js_release_funcs: List | String. Optional. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
        raise Exception("Press Event must be defined")

      if not isinstance(js_release_funcs, list):
        js_release_funcs = [js_release_funcs]
      js_release_funcs.append(self.dom.release())
      str_fnc = "%s else{%s}" % (str_fnc, JsUtils.jsConvertFncs(js_release_funcs, toStr=True))
    return self.on("click", str_fnc, profile, on_ready=on_ready)

  def color(self, color):
    """
    Description:
    -----------
    Change the color of the button background when the mouse is hover.

    Usage:
    -----

      page.ui.buttons.remove("remove").color("blue")

    Attributes:
    ----------
    :param color: String. the color of the component (text and borders).
    """
    self.style.css.border = "1px solid %s" % color
    self.set_attrs(name="onmouseover", value="this.style.backgroundColor='%s';this.style.color='white'" % color)
    self.set_attrs(name="onmouseout", value="this.style.backgroundColor=\'white\';this.style.color=\'%s\';" % color)
    return self

  def properties(self):
    """
    Description:
    -----------
    Return the full properties of the HTML component.
    This property should allow another JavaScript framework to build the component.

    Usage:
    -----

      but = page.ui.button("Click Me")
      but.properties

    """
    return {"tag": self.name, 'selector': self.htmlCode}

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    return '<button %s>%s</button>' % (self.get_attrs(pyClassNames=self.style.get_classes()), str_div)


class Checkbox(Html.Html):
  name = 'Check Box'
  requirements = ('font-awesome', 'bootstrap', 'jquery')
  _option_cls = OptButton.OptCheckboxes

  def __init__(self, report, records, color, width, height, align, html_code, tooltip, options, profile):
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
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for check boxes.

    Usage:
    -----


    :rtype: OptButton.OptCheckboxes
    """
    return super().options

  @property
  def dom(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript available for a DOM element by default.

    Usage:
    -----

    :rtype: JsHtml.JsHtmlButtonChecks
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButtonChecks(self, report=self._report)
    return self._dom

  def tooltip(self, value, location='top', options=None):
    """
    Description:
    -----------
    Add the Tooltip feature when the mouse is over the component.
    This tooltip version is coming from Bootstrap.

    TODO: Use the options parameter.

    Usage:
    -----

      check = page.ui.buttons.check()
      check.tooltip("Tooltip")

    Attributes:
    ----------
    :param value: String. The tooltip value.
    :param location: String. Optional. The location of the tooltip compared to the HTML component.
    :param options: Dictionary. Optional. The tooltip options (not used yet)
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

  def click(self, js_funcs, profile=None, source_event="$(document)", on_ready=False):
    """
    Description:
    -----------

    TODO: Find way to remove jquery

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
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
      self._report.body.onReady([self.dom.check(True)])
    self.page.properties.js.add_builders(self.refresh())
    return '<div %(strAttr)s><div name="checks"></div></div>' % {
      'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}


class CheckButton(Html.Html):
  name = 'Check Button'
  _option_cls = OptButton.OptCheck

  def __init__(self, report, flag=False, tooltip=None, width=None, height=None, icon=None, label=None, html_code=None,
               options=None, profile=None):
    super(CheckButton, self).__init__(report, 'Y' if flag else 'N', html_code=html_code, options=options,
                                      css_attrs={"width": width, "height": height}, profile=profile)
    self.input = report.ui.images.icon(self.options.icon_check if flag else self.options.icon_not_check).css(
      {"width": Defaults_css.font()})
    self.input.style.css.color = self._report.theme.success[1] if flag else self._report.theme.danger[1]
    self.input.style.css.middle()
    self.input.options.managed = False
    self.add_label(label, {"width": "none", "float": "none"}, html_code=self.htmlCode, position="after")
    self.add_icon(icon, {"float": 'none'}, html_code=self.htmlCode, position="after", family=options.get("icon_family"))
    if tooltip is not None:
      self.tooltip(tooltip)

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for check button.

    Usage:
    -----


    :rtype: OptButton.OptCheck
    """
    return super().options

  @property
  def dom(self):
    """
    Description:
    ------------
    The Javascript Dom object.

    Usage:
    -----

    :rtype: JsHtml.JsHtmlButtonMenu
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlButtonMenu(self, report=self._report)
    return self._dom

  @property
  def js(self):
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsComponents.CheckButton
    """
    if self._js is None:
      self._js = JsComponents.CheckButton(self, report=self._report)
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
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    Usage:
    -----

    :rtype: GrpClsButton.ClassButtonCheckBox
    """
    if self._styleObj is None:
      self._styleObj = GrpClsButton.ClassButtonCheckBox(self)
    return self._styleObj

  def click(self, js_fnc_true, js_fnc_false=None, with_colors=True, profile=None, on_ready=False):
    """
    Description:
    ------------
    Click even on the checkbox item.

    Usage:
    -----

      ch = page.ui.buttons.check(label="Label")
      ch.click(page.js.alert("true"), page.js.alert("false"))

    Attributes:
    ----------
    :param js_fnc_true: List | String. Js function or a list of JsFunction to be triggered when checked
    :param js_fnc_false: Boolean. Optional. Js function or a list of JsFunction to be triggered when unchecked
    :param with_colors: Boolean. Optional. Add default colors to the icons.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded

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
      js_fnc_true.append(self.input.dom.css({"color": self._report.theme.success[1]}).r)
      js_fnc_false.append(self.input.dom.css({"color": self._report.theme.danger[1]}).r)
    js_fncs = [
      self.input.dom.switchClass(self.options.icon_check.split(" ")[-1],
                                 self.options.icon_not_check.split(" ")[-1]),
      JsIf.JsIf(self.input.dom.hasClass(self.options.icon_check.split(" ")[-1]), js_fnc_true).else_(js_fnc_false)]
    return super(CheckButton, self).click(js_fncs, profile, on_ready=on_ready)

  def __str__(self):
    return '''<div %s>%s</div>''' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.input.html())


class IconEdit(Html.Html):
  name = 'Icon'

  def __init__(self, report, position, icon, text, tooltip, width, height, html_code, options, profile):
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
      self.add_icon(icon, {"margin": "2px", 'font-size': Defaults_css.font(-notches)}, html_code=self.htmlCode,
                    family=options.get("icon_family"))
    self.hover_color = True

  def spin(self):
    """
    Description:
    ------------
    Add a spin effect to the icon.

    Usage:
    -----

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

    Usage:
    -----

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

    Usage:
    -----

      icon = page.ui.icons.awesome("")
      icon.border()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons
    """
    self.icon.border()
    return self

  def rotate(self, angle):
    """
    Description:
    ------------
    To arbitrarily rotate and flip icons, use the fa-rotate-* and fa-flip-* classes when you reference an icon.

    Usage:
    -----

      icon = page.ui.icons.awesome("")
      icon.rotate(90)

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/rotating-icons

    Attributes:
    ----------
    :param angle: Integer. The rotation angle.
    """
    self.icon.rotate(angle)
    return self

  def pull(self, position='left'):
    """
    Description:
    ------------
    Use fa-border and fa-pull-right or fa-pull-left for easy pull quotes or article icons.

    Usage:
    -----

      icon = page.ui.icons.awesome("")
      icon.pull()

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons

    Attributes:
    ----------
    :param position: String. Optional. The position of the icon in the page.
    """
    self.icon.pull(position)
    return self

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Add a JavaScript click event on this component.

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if self.hover_color:
      if self.hover_color == 'danger':
        self.icon.style.add_classes.div.danger_hover()
      else:
        self.icon.style.add_classes.icon.basic()
    return super(IconEdit, self).click(js_funcs, profile, source_event, on_ready=on_ready)

  def goto(self, url, js_funcs=None, profile=None, target="_blank", source_event=None):
    """
    Description:
    -----------
    Create a link to a new page when component is clicked.

    Related Pages:

      https://www.w3schools.com/tags/att_a_target.asp

    Usage:
    -----

    Attributes:
    ----------
    :param url: String. The target url.
    :param js_funcs: List | String. Optional. Javascript functions.
    :param target: String. Optional. The type of link in the browser (new tab or same one).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The event source reference.
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

  def __init__(self, report, data, color, width, height, html_code, helper, options, profile):
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

  def __init__(self, report, selector, parent):
    self._report, self._selector = report, selector
    self._src, self._js, self._events = parent, None, []

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript module of the items in the menu.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsComponents.Menu
    """
    if self._js is None:
      self._js = JsComponents.Menu(self._src, varName=self._selector, report=self._report)
    return self._js

  def on(self, event, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Javascript generic events of the items in the menu.

    Usage:
    -----

    Attributes:
    ----------
    :param event: String. The JavaScript event.
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean. Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. Override the source component on which the component is defined.
    :param on_ready: Boolean. Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._events.append("%s.addEventListener('%s', function (event) {%s})" % (
      source_event or self._selector, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    if on_ready:
      self._report.body.onReady([self._selector.dom.events.trigger(event)])
    return self._src

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Javascript click events of the items in the menu.

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean. Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. Override the source component on which the component is defined.
    :param on_ready: Boolean. Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    return self.on("click", js_funcs, profile, source_event, on_ready)


class ButtonMenu(Html.Html):
  name = 'Button Menu'

  def __init__(self, report, record, text, icon, width, height, html_code, tooltip, profile, options):
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

  def __getitem__(self, i):
    if i not in self.components:
      self.components[i] = ButtonMenuItem(self._report, "document.getElementById('%s').querySelectorAll('a')[%s]" % (
        self.htmlCode, i), self)
    return self.components[i]

  _js__builder__ = '''
      var panel = htmlObj.querySelector("div");
      data.forEach(function(rec){
        var href = document.createElement("a"); href.innerHTML = rec;
        Object.keys(options).forEach(function(key){href.style[key] = options[key]});
        panel.appendChild(href)})'''

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    Usage:
    -----

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
    return '<div %s>%s%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.button.html(),
                                   self.container.html())


class ButtonFilter(Html.Html):
  name = 'Button Filter'

  def __str__(self):
    events = []
    for comp in self.components.values():
      events.extend(comp._events)
    self.onReady(events)
    return '<div %s>%s%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()),
                                   self.button.html(), self.container.html())
