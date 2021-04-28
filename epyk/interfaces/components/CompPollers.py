#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html


class Poller:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def toggle(self, time, js_funcs=None, components=None, label=None, color=None, width=(None, '%'), height=(20, 'px'), align="left",
             html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param time: Integer. Interval time in second.
    :param js_funcs: String | List. The Javascript functions.
    :param components: List. HTML components to be triggered when activated.
    :param label: String. Optional. The text of label to be added to the component
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if components is not None:
      js_funcs = js_funcs or []
      for component in components:
        js_funcs.append(component.dom.trigger("click"))
    container = self.page.ui.div(align=align, height=height, width=width, profile=profile, options=options)
    toggle = self.page.ui.buttons.toggle(None, label, color, width, height, align, html_code, options, profile)
    toggle.style.css.display = "inline-block"
    toggle.switch_text.style.css.hide()
    icon = self.page.ui.icon("far fa-clock")
    toggle.toggle(on_funcs=[
      icon.dom.spin(),
      icon.dom.css({"color": self.page.theme.success[1]}).r,
      self.page.js.window.setInterval(js_funcs, "%s_timer" % toggle.htmlCode, time * 1000, profile=profile)
    ],
      off_funcs=[
        icon.dom.spin(False),
      icon.dom.css({"color": self.page.theme.danger[1]}).r,
        self.page.js.window.clearInterval("%s_timer" % toggle.htmlCode)]
    )
    container.toggle = toggle
    container.add(toggle)
    icon.style.css.margin = "2px 5px 5px 0px"
    # icon.spin()
    container.icon = icon
    container.add(icon)
    return container

  @html.Html.css_skin()
  def live(self, time, js_funcs=None, components=None, icon="fas fa-circle", width=(15, "px"), height=(15, "px"), align="left",
           html_code=None, profile=None, options=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param time: Integer. Interval time in second.
    :param js_funcs: String | List. The Javascript functions.
    :param components: List. HTML components to be triggered when activated.
    :param icon: String. Optional. The font awesome icon reference.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if components is not None:
      js_funcs = js_funcs or []
      for component in components:
        js_funcs.append(component.dom.trigger("click"))
    toggle = self.page.ui.buttons.live(time, js_funcs, icon, width, height, align, html_code, profile, options)
    return toggle
