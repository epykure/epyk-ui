#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from typing import Union, Optional, List
from epyk.core.py import types

from epyk.core import html
from epyk.core.html import Defaults_html
from epyk.interfaces import Arguments


COLOR_EXPR = "1px solid {}"


class Buttons:
  """
  Buttons Interface.
  """
  
  def __init__(self, ui):
    self.page = ui.page

  @staticmethod
  def __align(component: html.Html.Html, align: str):
    """
    Set the component align in the page.

    :param component: The component to be aligned in the page
    :param align: Optional. The text-align property within this component
    """
    if align == "center":
      component.style.css.margin = "auto"
      component.style.css.display = "block"
    elif align == "right":
      component.style.css.float = "right"

  def __set_color(self, component: html.Html.Html, color: Union[str, bool]):
    """
    Set the background color for the button.
    By default, it will use the theme's color.

    :param component: The component to be aligned in the page
    :param color: The color to set
    """
    if color is True:
      component.style.css.background = self.page.theme.notch(-5) if self.page.theme.dark else self.page.theme.notch(4)
      component.style.css.border = COLOR_EXPR.format(
        self.page.theme.notch(-6) if self.page.theme.dark else self.page.theme.colors[-1])
      component.style.css.color = self.page.theme.colors[-1] if self.page.theme.dark else self.page.theme.colors[0]
    else:
      component.style.css.background = color
      component.style.css.border = color
      component.style.css.color = self.page.theme.colors[0]

  def button(self, text: str = "", icon: str = None, width: types.SIZE_TYPE = (None, "%"),
             height: types.SIZE_TYPE = (None, "px"), align: str = "left", html_code: str = None,
             tooltip: str = None, profile: types.PROFILE_TYPE = None,
             options: types.OPTION_TYPE = None) -> html.HtmlButton.Button:
    """
    Standard button

    :tags:
    :categories:

    Usage::

      page.ui.button("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/alerts.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_link.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    component = html.HtmlButton.Button(
      self.page, text, icon, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    if options is not None and options.get("colored", False):
      self.__set_color(component, options["colored"])
    component.style.css.line_height = self.page.body.style.globals.line_height
    component.style.css.margin = "0"
    component.style.css.padding = 0
    component.style.css.padding_h = 5
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def colored(self, text: str = "", icon: str = None, color: str = None,
              width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"), align: str = "left",
              html_code: str = None, tooltip: str = None, profile: types.PROFILE_TYPE = None,
              options: types.OPTION_TYPE = None) -> html.HtmlButton.Button:
    """
    Standard colored button.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.colored("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/alerts.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_link.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    :param text: Optional. The value to be displayed to the button
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align:  Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    dft_options = {"colored": color or True}
    if options is not None:
      dft_options.update(options)
    component = self.button(text, icon, width, height, align, html_code, tooltip, profile, dft_options)
    component.style.css.margin_top = 2
    component.style.css.margin_bottom = 2
    html.Html.set_component_skin(component)
    return component

  def clear(self, text: str = "", icon: str = "fas fa-eraser", color: str = None,
            width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"),
            align: str = "left", html_code: str = None, tooltip: str = None,
            profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None) -> html.HtmlButton.Button:
    """
    Standard clear button with a font-awesome icon.

    Usage::

      page.ui.buttons.clear("Clear")

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/alerts.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_link.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    :param text: Optional. The value to be displayed to the button
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    component = self.button(text, icon, width, height, align, html_code, tooltip, profile, options)

    component.style.css.background = color or self.page.theme.danger.base
    component.style.css.border = COLOR_EXPR.format(color or self.page.theme.danger.base)
    component.style.css.color = self.page.theme.colors[0]
    component.style.css.margin_top = 5
    component.style.css.margin_bottom = 5
    component.style.hover({"background-color": "%s !IMPORTANT" % self.page.theme.danger.light})
    html.Html.set_component_skin(component)
    return component

  def large(self, text: str = "", icon: str = None, width: types.SIZE_TYPE = (None, "%"),
            height: types.SIZE_TYPE = (None, "px"), align: str = "left", html_code: str = None,
            tooltip: str = None, profile: types.PROFILE_TYPE = None,
            options: types.OPTION_TYPE = None) -> html.HtmlButton.Button:
    """
    Large button.

    Usage::

      page.ui.buttons.large("Test")

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/alerts.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_link.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. The integer for the component width and its unit
    :param height: Optional. The integer for the component height and its unit
    :param align: Optional. The horizontal position of the component
    :param icon: Optional. The value of the icon to display from font-awesome
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. The value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    component = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                       tooltip=tooltip, profile=profile, options=options)
    self.__align(component, align)
    if options is not None and options.get("colored", False):
      self.__set_color(component, options["colored"])
    html.Html.set_component_skin(component)
    return component

  def absolute(self, text: str, size_notch=None, icon: str = "", top: types.SIZE_TYPE = (50, "%"),
               left: types.SIZE_TYPE = (50, "%"), bottom=None, width: types.SIZE_TYPE = ('auto', ""),
               height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
               options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlButton.Button:
    """
    Display a button on the page regardless the current layout of components.
    By default, the button will be center on the page.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Usage::

      page.ui.buttons.absolute("Test")

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param size_notch: Optional. A value to be added to the number font size
    :param bottom: Optional. The position of the component
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param top: Optional. A tuple with the integer for the component's distance to the top of the page
    :param left: Optional. A tuple with the integer for the component's distance to the left of the page
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    left = Arguments.size(left, unit="%")
    top = Arguments.size(top, unit="%")
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                       tooltip=None, profile=profile, options=options)
    component.style.position = "absolute"
    component.style.display = "block"
    if bottom is not None:
      component.style.bottom = "%s%s" % (bottom[0], bottom[1])
    else:
      component.style.top = "%s%s" % (top[0], top[1])
    component.style.left = "%s%s" % (left[0], left[1])
    component.style.transform = "translate(-%s, -%s)" % (component.style.left, component.style.top)
    if size_notch is not None:
      component.style.font_size = self.page.body.style.globals.font.normal(size_notch)
    if width[0] == 'auto':
      component.style.css.display = "inline-block"
    html.Html.set_component_skin(component)
    return component

  def small(self, text: str = "", icon: str = None, width: types.SIZE_TYPE = (None, "%"),
            height: types.SIZE_TYPE = (None, "px"), align: str = "left", html_code: str = None,
            tooltip: str = None, profile: types.PROFILE_TYPE = None,
            options: types.OPTION_TYPE = None) -> html.HtmlButton.Button:
    """
    Standard button with a small layout.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Usage::

      page.ui.buttons.small("Small button")

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                       tooltip=tooltip, profile=profile, options=options)
    component.style.css.line_height = 12
    component.style.css.padding = 2
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def normal(self, text: str = "", icon: str = None, width: types.SIZE_TYPE = (None, "%"),
             height: types.SIZE_TYPE = (None, "px"), align: str = "left", html_code: str = None,
             tooltip: str = None, profile: types.PROFILE_TYPE = None,
             options: types.OPTION_TYPE = None) -> html.HtmlButton.Button:
    """
    Standard button with a standard layout.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Usage::

      page.ui.buttons.normal("Standard button")

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                       tooltip=tooltip, profile=profile, options=options)
    component.style.css.line_height = 18
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def important(self, text: str = "", icon: str = None, width: Union[tuple, int] = (None, "%"),
                height: Union[tuple, int] = (None, "px"), align: str = "left", html_code: Optional[str] = None,
                tooltip: Optional[str] = None, profile: Union[dict, bool] = None,
                options: Optional[dict] = None) -> html.HtmlButton.Button:
    """
    Same as Standard button but used to attract user attention.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Usage::

      page.ui.buttons.important("Important")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                       tooltip=tooltip, profile=profile, options=options)
    component.style.add_classes.button.important()
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def validate(self, text: str = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
               html_code: Optional[str] = None, align: str = "left", tooltip: Optional[str] = None,
               profile: Union[dict, bool] = None, options: Optional[dict] = None) -> html.HtmlButton.Button:
    """
    Add a validate button with a predefined icon from font awesome.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.validate("Validate")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param align: Optional. The text-align property within this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    component = html.HtmlButton.Button(self.page, text, 'fas fa-check-circle', width, height,
                                       html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def run(self, text: str = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
          align: str = "left", html_code: Optional[str] = None, tooltip: Optional[str] = None,
          profile: Union[dict, bool] = None, options: Optional[dict] = None) -> html.HtmlButton.Button:
    """
    Add a run button with a predefined icon from font awesome.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Usage::

      page.ui.buttons.run("Run")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. The text-align property within this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    component = html.HtmlButton.Button(self.page, text, 'fas fa-play', width, height, html_code=html_code,
                                       tooltip=tooltip, profile=profile, options=options)
    if options.get("colored"):
      component.style.css.background = self.page.theme.colors[-1]
      component.style.css.border = COLOR_EXPR.format(self.page.theme.colors[-1])
      component.style.css.color = self.page.theme.colors[0]
      component.style.css.margin_top = 5
      component.style.css.margin_bottom = 5
    if align == "center":
      component.style.css.margin = "auto"
      component.style.css.display = "block"
    else:
      component.style.css.margin = 0
      component.style.css.padding = "0 20px"
      component.style.css.display = "inline-block"
      component.style.css.line_height = self.page.body.style.globals.line_height
    html.Html.set_component_skin(component)
    return component

  def remove(self, text: str = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
             html_code: Optional[str] = None, align: str = "left", tooltip: Optional[str] = None,
             profile: Union[dict, bool] = None, options: Optional[dict] = None) -> html.HtmlButton.Button:
    """
    Button with cross icon.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.remove("Remove")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"category": "delete"}
    if options is not None:
      dflt_options.update(options)
    component = html.HtmlButton.Button(self.page, text, 'fas fa-trash-alt', width, height,
                                       html_code=html_code, tooltip=tooltip, profile=profile, options=dflt_options)
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def cancel(self, text: str = "Cancel", width: Union[tuple, int] = (None, "%"),
             height: Union[tuple, int] = (None, "px"), html_code: Optional[str] = None, align: str = "left",
             tooltip: Optional[str] = None, profile: Union[dict, bool] = None,
             options: Optional[dict] = None) -> html.HtmlButton.Button:
    """
    Button with cross icon to cancellation actions.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.cancel("Cancel")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param align: Optional. The text-align property within this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"category": "delete"}
    if options is not None:
      dflt_options.update(options)
    component = html.HtmlButton.Button(self.page, text, 'fas fa-window-close', width, height,
                                       html_code=html_code, tooltip=tooltip, profile=profile, options=dflt_options)
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def phone(self, text: str = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
            html_code: Optional[str] = None, align: str = "left", tooltip: Optional[str] = None,
            profile: Union[dict, bool] = None, options: Optional[dict] = None) -> html.HtmlButton.Button:
    """
    Add a phone button with a predefined icon from font-awesome.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.phone()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.Button(self.page, text, 'fas fa-phone', width, height, html_code=html_code,
                                       tooltip=tooltip, profile=profile, options=options)
    component.style.css.line_height = self.page.body.style.globals.line_height
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def mail(self, text: str = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
           html_code: Optional[str] = None, align: str = "left", tooltip=None,
           profile: Union[dict, bool] = None, options: Optional[dict] = None) -> html.HtmlButton.Button:
    """
    Add a mail button with a predefined icon from font-awesome.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.mail()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.Button(self.page, text, 'fas fa-envelope', width, height, html_code=html_code,
                                       tooltip=tooltip, profile=profile, options=options)
    component.style.css.line_height = self.page.body.style.globals.line_height
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def radio(self, record: List[dict] = None, html_code: Optional[str] = None, group_name: Optional[str] = None,
            width: Union[tuple, int] = (100, '%'), height: Union[tuple, int] = (None, "px"), align: str = 'left',
            checked: str = None, options: Optional[dict] = None, profile: Union[dict, bool] = None) -> html.HtmlRadio.Radio:
    """
    Creates a radio HTML component.

    Tips: record data should be in the format expected by the component. If needed a data helper can be used.
    from the data package in the component property, the various functions available for the radio will help.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.radio(df, dfColumn="A", htmlCode="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlRadio.Radio`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_forms_inputs.asp

    `Templates <https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py>`_

    :param record: Optional. The Python list of dictionaries
    :param group_name: Optional. Group name for multi radio buttons
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param checked:
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if checked:
      for rec in record:
        if rec['value'] == checked:
          rec["checked"] = True
    component = html.HtmlRadio.Radio(
      self.page, record or [], html_code, group_name, width, height, options or {}, profile)
    component.style.css.line_height = self.page.body.style.globals.line_height
    for c in component:
      c.style.css.display = "inline-block"
      c.style.css.margin = "0 2px"
      c.style.css.padding = "0 2px"
    component.style.css.text_align = align
    html.Html.set_component_skin(component)
    return component

  def toggle(self, record: dict = None, label: str = None, color: str = None,
             width: types.SIZE_TYPE = (None, '%'), height: types.SIZE_TYPE = (None, 'px'), align: str = "left",
             html_code: str = None, options: types.OPTION_TYPE = None,
             profile: types.OPTION_TYPE = None) -> html.HtmlContainer.Div:
    """
    Add a toggle component.

    Component Structure::

      component.input: :class:`html.HtmlRadio.Switch`
      component.label: :class:`html.HtmlText.Label`

    :tags:
    :categories:

    Usage::

      page.ui.buttons.toggle({'on': "true", 'off': 'false'})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlRadio.Switch`

    Related Pages:

      http://thecodeplayer.com/walkthrough/pure-css-on-off-toggle-switch
      https://codepen.io/mburnette/pen/LxNxNg

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/switch.py

    :param record: Optional. component data
    :param label: Optional. The toggle static label displayed
    :param color: Optional. String. Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    record = record or {"off": "Off", "on": "On"}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if height[0] is None:
      height = (self.page.body.style.globals.line_height, height[1])
    html_toggle = html.HtmlRadio.Switch(self.page, record, color, width, height, html_code, options or {}, profile)
    if label is not None:
      label = self.page.ui.texts.label(label, align=align, options=options, html_code="%s_label" % html_toggle.htmlCode)
      html_toggle.style.css.display = "inline-block"
      html_toggle.style.css.padding_top = 2
      component = self.page.ui.div([label, html_toggle], width=width)
      component.label = label
    else:
      component = self.page.ui.div([html_toggle], width=width)
    component.input = html_toggle
    component.style.css.line_height = self.page.body.style.globals.line_height
    html.Html.set_component_skin(component)
    return component

  def checkboxes(self, record=None, color: str = None, width: types.SIZE_TYPE = (100, "%"),
                 height: types.SIZE_TYPE = (None, "px"), align: str = 'left',
                 html_code: str = None, tooltip: str = '', options: types.OPTION_TYPE = None,
                 profile: types.PROFILE_TYPE = None):
    """
    Python wrapper to the HTML checkbox elements.

    Tips: record data should be in the format expected by the component. If needed a data helper can be used.
    from the data package in the component property, the various functions available for the checkboxes will help.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.checkboxes(data)

      cb2 = page.ui.buttons.checkboxes(data, color="red", width=(100, "px"))
      cb2.style.configs.shadow()
      cb2.click([page.js.console.log(cb2.dom.current)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Checkbox`

    Related Pages:

      https://www.w3schools.com/howto/howto_css_custom_checkbox.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_checkboxes.py

    :param record: Optional. The list of dictionaries with the data
    :param color: Optional. The color code
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. The text-align property within this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.Checkbox(
      self.page, record or [], color, width, height, align, html_code, tooltip, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def check(self, flag: bool = False, tooltip: str = None, width: types.SIZE_TYPE = (None, "px"),
            height: types.SIZE_TYPE = (20, "px"), label: str = None, icon: str = None,
            html_code: str = None, profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None
            ) -> html.HtmlButton.CheckButton:
    """
    Wrapper to the checkbox button object.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.check(label="Label")
      page.ui.buttons.check(True, label="Label")
      page.ui.buttons.check(True, label="Label", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.CheckButton`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    :param flag: Optional. The value of the checkbox. Default False
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param label: Optional. The component label content
    :param icon: Optional. The icon to be used in the check component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.CheckButton(
      self.page, flag, tooltip, width, height, icon, label, html_code, options or {}, profile)
    component.css({'display': 'inline-block', 'margin-right': '10px'})
    html.Html.set_component_skin(component)
    return component

  def menu(self, record: list = None, text: str = "", icon: Optional[Union[str, bool]] = None,
           width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"),
           html_code: str = None, tooltip: str = None,
           profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None) -> html.HtmlButton.ButtonMenu:
    """
    Button with underlying items menu.

    :tags:
    :categories:

    Usage::

      tree5 = page.ui.buttons.menu(["A", "B", "C"], 'Menu')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.ButtonMenu`

    Related Pages:

      https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_js_dropdown_hover

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/tree.py

    :param record: Optional. The list of dictionaries with the data
    :param text: Optional. The value to be displayed to the button
    :param icon: Optional. The icon to be used in the check component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.ButtonMenu(self.page, record, text, icon, width, height,
                                           html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    component.container.css({"display": "none", "position": "absolute", "z-index": 5})
    html.Html.set_component_skin(component)
    return component

  def store(self, image, url, width: types.SIZE_TYPE = (7.375, "rem"), height: types.SIZE_TYPE = (2.375, "rem"),
            html_code: str = None, align: str = "left", options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None):
    """
    Button for a badge which point to the various application stores (Google and Apple).
    The badge must be issued from the Google Play Store.

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Related Pages:

      https://play.google.com/intl/en_us/badges/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    :param image: The url of the image
    :param url: The link to the app in the store
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param align: Optional. The text-align property within this component
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="rem")
    height = Arguments.size(height, unit="rem")
    split_url = os.path.split(image)
    component = self.page.ui.img(split_url[1], path=split_url[0], width=width, height=height, html_code=html_code,
                                 options=options, profile=profile)
    component.style.css.display = "inline-block"
    component.goto(url)
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def live(self, time: int, js_funcs: types.JS_FUNCS_TYPES, icon: Optional[Union[str, bool]] = "fas fa-circle",
           width: types.SIZE_TYPE = ('auto', "px"), height: types.SIZE_TYPE = ('auto', "px"), align: str = "left",
           html_code: str = None, profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None):
    """
    Live component which will trigger event every x second.
    This will then allow other components to be refreshed in the page.

    :tags:
    :categories:

    Usage::

      b7 = page.ui.buttons.live(3, page.js.console.log("Click"), options={"started": False})
      b8 = page.ui.buttons.live(2, page.js.console.log("refresh data"), profile=True)

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_icon.py

    :param time: Interval time in second
    :param js_funcs: The Javascript functions
    :param icon: Optional. The font awesome icon reference
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    dflt_options = {"started": True}
    if options is not None:
      dflt_options.update(options)
    component = self.page.ui.icons.awesome(
      icon, width=width, height=height, html_code=html_code, options=options, profile=profile)
    component.style.css.border_radius = "50px"
    component.style.css.vertical_align = "middle"
    component.style.css.line_height = self.page.body.style.globals.line_height
    component.style.css.padding = 0
    component.style.css.margin = 0
    component.style.css.position = "relative"
    component.icon.style.css.font_factor(1)
    component.icon.style.css.margin = 0
    component.icon.style.css.position = "absolute"
    component.icon.style.css.vertical_align = "middle"
    component.icon.style.css.text_align = "center"
    if dflt_options["started"]:
      component.attr["data-active"] = 1
      component.icon.style.css.color = self.page.theme.success.base
      component.icon.style.effects.blink(2)
      component.style.css.border = "1px solid %s" % self.page.theme.success.base
      self.page.body.onReady([
        self.page.js.window.setInterval(js_funcs, "%s_timer" % component.htmlCode, time * 1000)], profile=profile)
    else:
      component.icon.style.css.color = self.page.theme.danger.base
      component.style.css.border = "1px solid %s" % self.page.theme.danger.base
      component.attr["data-active"] = 0
    component.click([
      self.page.js.if_(component.dom.getAttribute("data-active") == 1, [
        component.dom.setAttribute("data-active", 0).r,
        component.dom.css("border-color", self.page.theme.danger.base).r,
        component.icon.dom.css("color", self.page.theme.danger.base).r,
        component.icon.dom.css("animation", 'none').r,
        self.page.js.window.clearInterval("%s_timer" % component.htmlCode)
      ]).else_([
        component.dom.setAttribute("data-active", 1).r,
        component.dom.css("border-color", self.page.theme.success.base).r,
        component.icon.dom.css("color", self.page.theme.success.base).r,
        component.icon.dom.effects.blink(2),
        self.page.js.window.setInterval(js_funcs, "%s_timer" % component.htmlCode, time * 1000, profile=profile)
      ]),
    ])
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def text(self, text: str, icon: Optional[Union[str, bool]] = None, width: Union[tuple, int] = ('auto', ""),
           tooltip: Optional[str] = None, height: Union[tuple, int] = (None, "px"),
           align: str = "left", html_code: Optional[str] = None, profile: Union[dict, bool] = None,
           options: Optional[dict] = None):
    """
    Add a text button.

    :tags:
    :categories:

    Usage::

    Templates:

    :param text: Optional. The value to be displayed to the button
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    component = self.page.ui.text(
      text, tooltip=tooltip, width=width, html_code=html_code, height=height, profile=profile, options=options)
    component.add_icon(icon, html_code=component.htmlCode)
    component.style.css.line_height = self.page.body.style.globals.line_height
    self.__align(component, align)
    html.Html.set_component_skin(component)
    return component

  def thumbs_up(self, width: Union[tuple, int] = ("auto", ""), height: Union[tuple, int] = (None, "px"),
                align: str = "left", html_code: Optional[str] = None, tooltip: Optional[str] = None,
                profile: Union[dict, bool] = None, options: Optional[dict] = None):
    """
    Button with the font awesome icon far fa-thumbs-up.

    :tags:
    :categories:

    Usage::

      b6 = page.ui.buttons.thumbs_up(tooltip="Like")

    Templates:

    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip:  Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    component = self.button(
      icon="far fa-thumbs-up", width=width, height=height, html_code=html_code, tooltip=tooltip, profile=profile,
      options=options, align=align)
    component.options.templateError = Defaults_html.TEMPLATE_ERROR_ICON
    component.options.templateLoading = Defaults_html.TEMPLATE_LOADING_ICON
    component.style.css.background = self.page.theme.success.base
    component.style.css.border_color = self.page.theme.success.base
    component.style.css.padding = "0 10px"
    component.icon.style.css.color = "white"
    component.icon.style.add_classes.div.color_hover(self.page.theme.success.base)
    html.Html.set_component_skin(component)
    return component

  def thumbs_down(self, width: Union[tuple, int] = ("auto", ""), height: Union[tuple, int] = (None, "px"),
                  align: str = "left", html_code: Optional[str] = None, tooltip: Optional[str] = None,
                  profile: Union[dict, bool] = None, options: Optional[dict] = None):
    """
    Button with the font awesome icon far fa-thumbs-down.

    :tags:
    :categories:

    Usage::

    Templates:

    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    component = self.button(icon="far fa-thumbs-down", width=width, height=height, html_code=html_code, tooltip=tooltip,
                            profile=profile, options=options, align=align)
    component.options.templateError = Defaults_html.TEMPLATE_ERROR_ICON
    component.options.templateLoading = Defaults_html.TEMPLATE_LOADING_ICON
    component.style.css.background = self.page.theme.danger.base
    component.style.css.border_color = self.page.theme.danger.base
    component.style.css.padding = "0 10px"
    component.icon.style.css.color = "white"
    component.icon.style.add_classes.div.color_hover(self.page.theme.danger.base)
    html.Html.set_component_skin(component)
    return component

  def pill(self, text: str, value=None, group: Optional[str] = None,
           width: Union[tuple, int] = ("auto", ""), height: Union[tuple, int] = (None, "px"), align: str = "left",
           html_code: Optional[str] = None, tooltip: Optional[str] = None, profile: Union[dict, bool] = None,
           options: Optional[dict] = None):
    """
    Add a pill button.

    :tags:
    :categories:

    Usage::

    Templates:

    :param text: Optional. The text to be displayed to the button
    :param value: Optional. The value to be displayed in the pill
    :param group: Optional. The group value fot the pill
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    component = self.page.ui.text(
      text, width=width, height=height, align=align, html_code=html_code, tooltip=tooltip, profile=profile,
      options=options)
    component.style.css.background = self.page.theme.greys[3]
    component.style.css.line_height = self.page.body.style.globals.line_height
    component.options.style_select = "pill_selected"
    component.style.css.border_radius = 20
    component.style.css.padding = "0 5px"
    component.attr["data-value"] = value or text
    component.style.add_classes.div.color_background_hover()
    if group is not None:
      self.page.body.style.custom_class({
        "background": self.page.theme.colors[6], "color": self.page.theme.greys[0],
      }, classname="pill_selected", important=True)
      component.attr["data-group"] = group
    html.Html.set_component_skin(component)
    return component

  def more(self, items, text: str = "More", width: types.SIZE_TYPE = ("auto", ""),
           height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
           tooltip: str = None, profile: types.PROFILE_TYPE = None,
           options: types.OPTION_TYPE = None) -> html.HtmlButton.ButtonMore:
    """

    :tags:
    :categories:

    Usage::

      b = page.ui.buttons.more([
        {"text": "Add", "target": "_blank", "icon": "fab fa-500px",
         "url": "https://stackoverflow.com/questions/5884066/hashing-a-dictionary"},
        {"text": "Delete", "target": "_blank", "icon": "fab fa-500px",
         "url": "https://stackoverflow.com/questions/5884066/hashing-a-dictionary"},
      ])
      b.click([page.js.console.log("Click event")])

    Templates:

    Related Pages:

    :param items: List of items to be added to the menu
    :param text: Optional. The text visible in the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    component = html.HtmlButton.ButtonMore(
      self.page, items, text, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    component.style.css.line_height = self.page.body.style.globals.line_height
    html.Html.set_component_skin(component)
    return component

  def filter(self, text: str = "", is_number: bool = False, width: Union[tuple, int] = ("auto", ""),
             height: Union[tuple, int] = (None, "px"), html_code: Optional[str] = None,
             tooltip: Optional[str] = None, profile: Union[dict, bool] = None, options: Optional[dict] = None):
    """

    :tags:
    :categories:

    Usage::

    :param text: Optional. The filter value
    :param is_number: Optional. The filter property type
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {
      "is_number": False,
      "categories": ["Contains", "Not contains", "Equals", "Not equals", "Starts with", "Ends with"]}

    if is_number:
      dfl_options = {
        "is_number": True,
        "categories": ["Is Lower than", "Inferior or equals", "Equals", "Not equals", "Superior or equals",
                       "Is Greater than"]}
    if options is not None:
      dfl_options.update(options)
    # report, record, text, width, height, html_code, tooltip, profile, options
    component = html.HtmlButton.ButtonFilter(
      self.page, text, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=dfl_options)
    html.Html.set_component_skin(component)
    return component

  def refresh(self, text: str = "Refresh", icon: Optional[Union[str, bool]] = "fas fa-sync-alt",
              width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"), align: str = "left",
              html_code: Optional[str] = None, tooltip: Optional[str] = None, profile: Union[dict, bool] = None,
              options: Optional[dict] = None):
    """
    Standard refresh button with a font-awesome icon.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.refresh("Refresh")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/alerts.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_link.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.Button(
      self.page, text, icon, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    self.__align(component, align)
    component.style.css.padding = "5px 10px"
    component.style.css.margin_top = "5px !IMPORTANT"
    component.style.css.color = self.page.theme.greys[0]
    component.style.css.line_height = self.page.body.style.globals.line_height
    component.style.css.background = self.page.theme.colors[-1]
    component.style.css.border_color = self.page.theme.colors[-1]
    html.Html.set_component_skin(component)
    return component

  def data(self, filename, text: str = "", icon: Optional[Union[str, bool]] = None,
           width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"), align: str = "left",
           html_code: Optional[str] = None, tooltip: Optional[str] = None, profile: Union[dict, bool] = None,
           options: Optional[dict] = None):
    """
    Standard refresh button with a font-awesome icon.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.refresh("Refresh")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/alerts.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_link.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    :param filename: Optional. The filename
    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if icon is None:
      mapped_file = {
        "excel": 'far fa-file-excel', 'pdf': 'far fa-file-pdf', 'code': 'far fa-file-code', 'csv': 'fas fa-file-csv',
        'word': 'fa-file-word'}
      extension = filename.split(".")[-1]
      if extension in mapped_file:
        icon = mapped_file[extension]
    component = html.HtmlButton.ButtonData(
      self.page, text, icon, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    self.__align(component, align)
    component.filename = filename
    component.style.css.padding = 5
    component.style.css.visibility = "hidden"
    component.style.css.margin_top = "5px !IMPORTANT"
    component.style.css.line_height = 0
    component.style.css.color = self.page.theme.colors[-1]
    html.Html.set_component_skin(component)
    return component
