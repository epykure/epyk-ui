#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core import html
from epyk.core.html import Defaults_html
from epyk.interfaces import Arguments


class Buttons:

  def __init__(self, ui):
    self.page = ui.page

  @staticmethod
  def __align(component, align):
    """
    Description:
    ------------
    Set the component align in the page.

    Attributes:
    ----------
    :param component: HTML component. The component to be aligned in the page.
    :param align: String. The text-align property within this component.
    """
    if align == "center":
      component.style.css.margin = "auto"
      component.style.css.display = "block"
    elif align == "right":
      component.style.css.float = "right"

  @html.Html.css_skin()
  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
             tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
    Standard button.

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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    html_button = html.HtmlButton.Button(
      self.page, text, icon, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    html_button.style.css.margin = "0"
    html_button.style.css.padding = 0
    html_button.style.css.padding_h = 5
    html_button.style.css.line_height = Defaults_html.LINE_HEIGHT
    self.__align(html_button, align)
    return html_button

  @html.Html.css_skin()
  def colored(self, text="", icon=None, color=None, width=(None, "%"), height=(None, "px"), align="left",
              html_code=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    component = self.button(text, icon, width, height, align, html_code, tooltip, profile, options)
    component.style.css.background = color or self.page.theme.notch(4)
    component.style.css.border = "1px solid %s" % (color or self.page.theme.colors[-1])
    component.style.css.color = self.page.theme.colors[0]
    component.style.css.margin_top = 5
    component.style.css.margin_bottom = 5
    component.style.css.padding_left = 10
    component.style.css.padding_right = 10
    return component

  @html.Html.css_skin()
  def clear(self, text="", icon="fas fa-eraser", color=None, width=(None, "%"), height=(None, "px"), align="left",
            html_code=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
    Standard clear button with a font-awesome icon.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.clear("Clear")

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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    component = self.button(text, icon, width, height, align, html_code, tooltip, profile, options)
    component.style.css.background = color or self.page.theme.danger[-1]
    component.style.css.border = "1px solid %s" % (color or self.page.theme.danger[-1])
    component.style.css.color = self.page.theme.colors[0]
    component.style.css.margin_top = 5
    component.style.css.margin_bottom = 5
    component.style.hover({"background-color": "%s !IMPORTANT" % self.page.theme.danger[0]})
    return component

  @html.Html.css_skin()
  def large(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
            tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
    Large button.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.large("Test")

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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. The integer for the component width and its unit.
    :param height: Tuple. Optional. The integer for the component height and its unit.
    :param align: String. Optional. The horizontal position of the component.
    :param icon: String. Optional. The value of the icon to display from font-awesome.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. The value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    html_button = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                         tooltip=tooltip, profile=profile, options=options)
    self.__align(html_button, align)
    return html_button

  @html.Html.css_skin()
  def absolute(self, text, size_notch=None, icon="", top=(50, "%"), left=(50, "%"), bottom=None, width=('auto', ""),
               height=(None, "px"), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Display a button on the page regardless the current layout of components.
    By default the button will be center on the page.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Usage::

      page.ui.buttons.absolute("Test")

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param size_notch: Integer. Optional. A value to be added to the number font size.
    :param bottom: Integer. Optional. The position of the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param top: Tuple. Optional. A tuple with the integer for the component's distance to the top of the page.
    :param left: Tuple. Optional. A tuple with the integer for the component's distance to the left of the page.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    left = Arguments.size(left, unit="%")
    top = Arguments.size(top, unit="%")
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_button = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                         tooltip=None, profile=profile, options=options)
    html_button.style.position = "absolute"
    html_button.style.display = "block"
    if bottom is not None:
      html_button.style.bottom = "%s%s" % (bottom[0], bottom[1])
    else:
      html_button.style.top = "%s%s" % (top[0], top[1])
    html_button.style.left = "%s%s" % (left[0], left[1])
    html_button.style.transform = "translate(-%s, -%s)" % (html_button.style.left, html_button.style.top)
    if size_notch is not None:
      html_button.style.font_size = self.page.body.style.globals.font.normal(size_notch)
    if width[0] == 'auto':
      html_button.style.css.display = "inline-block"
    return html_button

  @html.Html.css_skin()
  def small(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
            tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
    Standard button with a small layout.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Usage::

      page.ui.buttons.small("Small button")

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_button = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                         tooltip=tooltip, profile=profile, options=options)
    html_button.style.css.line_height = 12
    html_button.style.css.padding = 2
    self.__align(html_button, align)
    return html_button

  @html.Html.css_skin()
  def normal(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
             tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
    Standard button with a standard layout.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Usage::

      page.ui.buttons.normal("Standard button")

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_button = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                         tooltip=tooltip, profile=profile, options=options)
    html_button.style.css.line_height = 18
    self.__align(html_button, align)
    return html_button

  @html.Html.css_skin()
  def important(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
                tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_button = html.HtmlButton.Button(self.page, text, icon, width, height, html_code=html_code,
                                         tooltip=tooltip, profile=profile, options=options)
    html_button.style.add_classes.button.important()
    self.__align(html_button, align)
    return html_button

  @html.Html.css_skin()
  def validate(self, text="", width=(None, "%"), height=(None, "px"), html_code=None, align="left", tooltip=None,
               profile=None, options=None):
    """
    Description:
    -----------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param align: String. Optional. The text-align property within this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    component = html.HtmlButton.Button(self.page, text, 'fas fa-check-circle', width, height,
                                       html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    self.__align(component, align)
    return component

  @html.Html.css_skin()
  def run(self, text="", width=(None, "%"), height=(None, "px"), align="left", html_code=None, tooltip=None,
          profile=None, options=None):
    """
    Description:
    -----------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    component = html.HtmlButton.Button(self.page, text, 'fas fa-play', width, height, html_code=html_code,
                                       tooltip=tooltip, profile=profile, options=options)
    if options.get("colored"):
      component.style.css.background = self.page.theme.colors[-1]
      component.style.css.border = "1px solid %s" % self.page.theme.colors[-1]
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
      component.style.css.line_height = Defaults_html.LINE_HEIGHT
    return component

  @html.Html.css_skin()
  def remove(self, text="", width=(None, "%"), height=(None, "px"), html_code=None, align="left", tooltip=None,
             profile=None, options=None):
    """
    Description:
    -----------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"category": "delete"}
    if options is not None:
      dflt_options.update(options)
    component = html.HtmlButton.Button(self.page, text, 'fas fa-trash-alt', width, height,
                                       html_code=html_code, tooltip=tooltip, profile=profile, options=dflt_options)
    self.__align(component, align)
    return component

  @html.Html.css_skin()
  def cancel(self, text="Cancel", width=(None, "%"), height=(None, "px"), html_code=None, align="left", tooltip=None,
             profile=None, options=None):
    """
    Description:
    -----------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param align: String. Optional. The text-align property within this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"category": "delete"}
    if options is not None:
      dflt_options.update(options)
    component = html.HtmlButton.Button(self.page, text, 'fas fa-window-close', width, height,
                                       html_code=html_code, tooltip=tooltip, profile=profile, options=dflt_options)
    self.__align(component, align)
    return component

  @html.Html.css_skin()
  def phone(self, text="", width=(None, "%"), height=(None, "px"), html_code=None, align="left", tooltip=None,
            profile=None, options=None):
    """
    Description:
    -----------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_button = html.HtmlButton.Button(self.page, text, 'fas fa-phone', width, height, html_code=html_code,
                                         tooltip=tooltip, profile=profile, options=options)
    self.__align(html_button, align)
    return html_button

  @html.Html.css_skin()
  def mail(self, text="", width=(None, "%"), height=(None, "px"), html_code=None, align="left", tooltip=None,
           profile=None, options=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_but = html.HtmlButton.Button(self.page, text, 'fas fa-envelope', width, height, html_code=html_code,
                                      tooltip=tooltip, profile=profile, options=options)
    self.__align(html_but, align)
    return html_but

  @html.Html.css_skin()
  def radio(self, record=None, html_code=None, group_name=None, width=(100, '%'), height=(None, "px"),
            align='left', options=None, profile=None):
    """
    Description:
    ------------
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

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    Attributes:
    ----------
    :param record: List of dict. The Python list of dictionaries.
    :param group_name: String. Optional.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_radio = html.HtmlRadio.Radio(
      self.page, record or [], html_code, group_name, width, height, options or {}, profile)
    for c in html_radio:
      c.style.css.display = "inline-block"
      c.style.css.margin = "0 2px"
      c.style.css.padding = "0 2px"
    html_radio.style.css.text_align = align
    return html_radio

  @html.Html.css_skin()
  def toggle(self, record=None, label=None, color=None, width=(None, '%'), height=(None, 'px'), align="left",
             html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a toggle component.

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

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the data.
    :param label: String. Optional. The toggle static label displayed.
    :param color: String. Optional. String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    record = record or {"off": "Off", "on": "On"}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if height[0] is None:
      height = (Defaults_html.LINE_HEIGHT, height[1])
    html_toggle = html.HtmlRadio.Switch(self.page, record, color, width, height, html_code, options or {}, profile)
    if label is not None:
      label = self.page.ui.texts.label(label, options=options, html_code="%s_label" % html_toggle.htmlCode)
      html_toggle.style.css.display = "inline-block"
      html_toggle.style.css.padding_top = 2
      container = self.page.ui.div([label, html_toggle])
      container.label = label
    else:
      container = self.page.ui.div([html_toggle])
    container.input = html_toggle
    return container

  @html.Html.css_skin()
  def checkboxes(self, record=None, color=None, width=(100, "%"), height=(None, "px"), align='left',
                 html_code=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    Python wrapper to the HTML checkbox elements.

    Tips: record data should be in the format expected by the component. If needed a data helper can be used.
    from the data package in the component property, the various functions available for the checkboxes will help.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.checkboxes(data)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Checkbox`

    Related Pages:

      https://www.w3schools.com/howto/howto_css_custom_checkbox.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_checkboxes.py

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the data.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_boxes = html.HtmlButton.Checkbox(
      self.page, record or [], color, width, height, align, html_code, tooltip, options or {}, profile)
    return html_boxes

  @html.Html.css_skin()
  def check(self, flag=False, tooltip=None, width=(None, "px"), height=(20, "px"), label=None, icon=None,
            html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    Wrapper to the check box button object.

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

    Attributes:
    ----------
    :param flag: Boolean. Optional. The value of the checkbox. Default False.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param label: String. Optional. The component label content.
    :param icon: String. Optional. The icon to be used in the check component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = html.HtmlButton.CheckButton(
      self.page, flag, tooltip, width, height, icon, label, html_code, options or {}, profile)
    html_but.css({'display': 'inline-block', 'margin-right': '10px'})
    return html_but

  @html.Html.css_skin()
  def menu(self, record, text="", icon=None, width=(None, "%"), height=(None, "px"), html_code=None, tooltip=None,
           profile=None, options=None):
    """
    Description:
    -----------
    Button with an underlying items menu.

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

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the data.
    :param text: String. Optional. The value to be displayed to the button.
    :param icon: String. Optional. The icon to be used in the check component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_button = html.HtmlButton.ButtonMenu(self.page, record, text, icon, width, height,
                                             html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    html_button.container.css({"display": "none", "position": "absolute", "z-index": 5})
    return html_button

  @html.Html.css_skin()
  def store(self, image, url, width=(7.375, "rem"), height=(2.375, "rem"), html_code=None, align="left", options=None,
            profile=None):
    """
    Description:
    -----------
    Button for a badge which point to the various application stores (Google and Apple).
    The badge must be issued from teh Google play store.

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Related Pages:

      https://play.google.com/intl/en_us/badges/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py

    Attributes:
    ----------
    :param image: String. The url of the image.
    :param url: String. The link to the app in the store.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param align: String. The text-align property within this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="rem")
    height = Arguments.size(height, unit="rem")
    split_url = os.path.split(image)
    badge = self.page.ui.img(split_url[1], path=split_url[0], width=width, height=height, html_code=html_code,
                             options=options, profile=profile)
    badge.style.css.display = "inline-block"
    badge.goto(url)
    self.__align(badge, align)
    return badge

  @html.Html.css_skin()
  def live(self, time, js_funcs, icon="fas fa-circle", width=(15, "px"), height=(15, "px"), align="left",
           html_code=None, profile=None, options=None):
    """
    Description:
    -----------
    Live component which will trigger event every x second.
    This will then allow other components to be refreshed in the page.

    :tags:
    :categories:

    Usage::

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button_icon.py

    Attributes:
    ----------
    :param time: Integer. Interval time in second.
    :param js_funcs: String | List. The Javascript functions.
    :param icon: String. Optional. The font awesome icon reference.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    dflt_options = {"started": True}
    if options is not None:
      dflt_options.update(options)
    live = self.page.ui.icons.awesome(
      icon, width=width, height=height, html_code=html_code, options=options, profile=profile)
    live.style.css.border_radius = "50px"
    live.style.css.padding = 0
    live.style.css.margin = 0
    live.icon.style.css.font_factor(2)
    live.icon.style.css.margin_right = 0
    live.icon.style.css.margin = "-2px 0 0 -2px"
    live.icon.style.css.padding_bottom = 10
    if dflt_options["started"]:
      live.attr["data-active"] = 1
      live.icon.style.css.color = self.page.theme.success[1]
      live.icon.style.effects.blink(2)
      live.style.css.border = "1px solid %s" % self.page.theme.success[1]
      self.page.body.onReady([
        self.page.js.window.setInterval(js_funcs, "%s_timer" % live.htmlCode, time * 1000)], profile=profile)
    else:
      live.icon.style.css.color = self.page.theme.danger[1]
      live.style.css.border = "1px solid %s" % self.page.theme.danger[1]
      live.attr["data-active"] = 0
    live.click([
      self.page.js.if_(live.dom.getAttribute("data-active") == 1, [
        live.dom.setAttribute("data-active", 0).r,
        live.dom.css("border-color", self.page.theme.danger[1]).r,
        live.icon.dom.css("color", self.page.theme.danger[1]).r,
        live.icon.dom.css("animation", 'none').r,
        self.page.js.window.clearInterval("%s_timer" % live.htmlCode)
      ]).else_([
        live.dom.setAttribute("data-active", 1).r,
        live.dom.css("border-color", self.page.theme.success[1]).r,
        live.icon.dom.css("color", self.page.theme.success[1]).r,
        live.icon.dom.effects.blink(2),
        self.page.js.window.setInterval(js_funcs, "%s_timer" % live.htmlCode, time * 1000, profile=profile)
      ]),
    ])
    self.__align(live, align)
    return live

  @html.Html.css_skin()
  def text(self, text, icon=None, width=('auto', ""), tooltip=None, height=(None, "px"), align="left", html_code=None,
           profile=None, options=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    c = self.page.ui.text(
      text, tooltip=tooltip, width=width, html_code=html_code, height=height, profile=profile, options=options)
    c.add_icon(icon, html_code=c.htmlCode)
    self.__align(c, align)
    return c

  @html.Html.css_skin()
  def thumbs_up(self, width=("auto", ""), height=(None, "px"), align="left", html_code=None, tooltip=None, profile=None,
                options=None):
    """
    Description:
    ------------
    Button with the font awesome icon far fa-thumbs-up.

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    but = self.button(icon="far fa-thumbs-up", width=width, height=height, html_code=html_code, tooltip=tooltip,
                      profile=profile, options=options, align=align)
    but.style.css.background = self.page.theme.success[1]
    but.style.css.border_color = self.page.theme.success[1]
    but.style.css.padding = "0 10px"
    but.icon.style.css.color = "white"
    return but

  @html.Html.css_skin()
  def thumbs_down(self, width=("auto", ""), height=(None, "px"), align="left", html_code=None, tooltip=None,
                  profile=None, options=None):
    """
    Description:
    ------------
    Button with the font awesome icon far fa-thumbs-down.

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    but = self.button(icon="far fa-thumbs-down", width=width, height=height, html_code=html_code, tooltip=tooltip,
                      profile=profile, options=options, align=align)
    but.style.css.background = self.page.theme.danger[1]
    but.style.css.border_color = self.page.theme.danger[1]
    but.style.css.padding = "0 10px"
    but.icon.style.css.color = "white"
    return but

  @html.Html.css_skin()
  def pill(self, text, value=None, group=None, width=("auto", ""), height=(None, "px"), align="left", html_code=None,
           tooltip=None, profile=None, options=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to the button.
    :param value: String. Optional. The value to be displayed in the pill.
    :param group: String. Optional. The group value fot the pill.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    but = self.page.ui.text(
      text, width=width, height=height, align=align, html_code=html_code, tooltip=tooltip, profile=profile,
      options=options)
    but.style.css.background = self.page.theme.greys[3]
    but.options.style_select = "pill_selected"
    but.style.css.border_radius = 20
    but.style.css.padding = "0 5px"
    but.attr["data-value"] = value or text
    but.style.add_classes.div.color_background_hover()
    if group is not None:
      self.page.body.style.custom_class({
        "background": self.page.theme.colors[6], "color": self.page.theme.greys[0],
      }, classname="pill_selected", important=True)
      but.attr["data-group"] = group
    return but

  @html.Html.css_skin()
  def more(self, items, text="More", width=("auto", ""), height=(None, "px"), html_code=None,
           tooltip=None, profile=None, options=None):
    """
    Description:
    ------------

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

    Attributes:
    ----------
    :param items: List. List of items to be added to the menu.
    :param text: String. Optional. The text visible in the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    # report, record, text, width, height, html_code, tooltip, profile, options
    html_button = html.HtmlButton.ButtonMore(
      self.page, items, text, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    return html_button

  @html.Html.css_skin()
  def filter(self, text, is_number=False, width=("auto", ""), height=(None, "px"), html_code=None,
             tooltip=None, profile=None, options=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param text:
    :param is_number:
    :param width:
    :param height:
    :param html_code:
    :param tooltip:
    :param profile:
    :param options:
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
    html_button = html.HtmlButton.ButtonFilter(
      self.page, text, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=dfl_options)
    return html_button

  @html.Html.css_skin()
  def refresh(self, text="Refresh", icon="fas fa-sync-alt", width=(None, "%"), height=(None, "px"), align="left",
              html_code=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_but = html.HtmlButton.Button(
      self.page, text, icon, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    self.__align(html_but, align)
    html_but.style.css.padding = "5px 10px"
    html_but.style.css.margin_top = "5px !IMPORTANT"
    html_but.style.css.color = self.page.theme.greys[0]
    html_but.style.css.line_height = 0
    html_but.style.css.background = self.page.theme.colors[-1]
    html_but.style.css.border_color = self.page.theme.colors[-1]
    return html_but

  @html.Html.css_skin()
  def data(self, filename, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left",
           html_code=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param filename: String. Optional. The filename.
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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
    html_but = html.HtmlButton.ButtonData(
      self.page, text, icon, width, height, html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    self.__align(html_but, align)
    html_but.filename = filename
    html_but.style.css.padding = 5
    html_but.style.css.visibility = "hidden"
    html_but.style.css.margin_top = "5px !IMPORTANT"
    html_but.style.css.line_height = 0
    html_but.style.css.color = self.page.theme.colors[-1]
    return html_but
