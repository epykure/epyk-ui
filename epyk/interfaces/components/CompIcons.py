#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.js.packages import JsFontAwesome
from epyk.interfaces import Arguments


class Icons:

  def __init__(self, ui):
    self.page = ui.page

  @property
  def get(self):
    return JsFontAwesome

  @html.Html.css_skin()
  def awesome(self, icon, text=None, tooltip=None, position=None, width=(25, 'px'), height=(25, 'px'),
              html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      page.ui.icons.awesome(icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/icons.py

    Attributes:
    ----------
    :param icon: String. The font awesome icon reference
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: String. Optional. The position of the icon in the line (left, right, center)
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_edit = html.HtmlButton.IconEdit(
      self.page, position, icon, text, tooltip, width, height, html_code, options or {}, profile)
    html_edit.css({"margin": 0, 'cursor': 'pointer'})
    html_edit.style.css.float = position
    html_edit.style.css.display = "inline-block"
    return html_edit

  @html.Html.css_skin()
  def fluent(self, icon, text=None, tooltip=None, position=None, width=(25, 'px'), height=(25, 'px'), html_code=None,
             options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      page.ui.icons.awesome(icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`
    ms-Icon ms-Icon--AdminDLogoInverse32

    Attributes:
    ----------
    :param icon: String. The fluentui icon reference.
    :param text: String. Optional. The text to be displayed to this component. Default None.
    :param position: Optional. The position of the icon in the line (left, right, center).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_edit = html.HtmlButton.IconEdit(self.page, position, icon, text, tooltip, width, height, html_code,
                                         options or {}, profile)
    html_edit.css({"margin": "5px 0", 'cursor': 'pointer'})
    html_edit.style.css.float = position
    html_edit.style.css.display = "inline-block"
    return html_edit

  @html.Html.css_skin()
  def fixed(self, icon=None, family=None, width=(None, 'px'), html_code=None, height=(None, "px"), color=None,
            tooltip=None, align="left", options=None, profile=None):
    options = options or {}
    component = self.page.ui.icon(icon, family, width, html_code, height, color, tooltip, align, options, profile)
    component.style.css.fixed(bottom=options.get("bottom", 20), right=options.get("right", 20))
    component.style.add_classes.div.background_hover()
    component.style.css.border_radius = 15
    component.style.css.padding = 8
    return component

  @html.Html.css_skin()
  def edit(self, text=None, position=None, tooltip="Edit", width=(None, 'px'), height=(None, 'px'), html_code=None,
           options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      page.ui.icons.edit()
      page.ui.icons.edit().color("red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/icons.py

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('far fa-edit', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def clock(self, text=None, position=None, tooltip="Last Updated Time", width=(None, 'px'), height=(None, 'px'),
            html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      page.ui.icons.clock()
      page.ui.icons.clock().color("red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/icons.py

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('fas fa-clock', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def next(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
           html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    components = self.awesome('fas fa-caret-right', text, tooltip, position, width, height, html_code, options, profile)
    components.icon.style.css.font_factor(10)
    return components

  @html.Html.css_skin()
  def previous(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
               html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    components = self.awesome('fas fa-caret-left', text, tooltip, position, width, height, html_code, options, profile)
    components.icon.style.css.font_factor(10)
    return components

  @html.Html.css_skin()
  def zoom_out(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
               html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    components = self.awesome(
      'fas fa-search-minus', text, tooltip, position, width, height, html_code, options, profile)
    components.style.css.color = self.page.theme.greys[-6]
    return components

  @html.Html.css_skin()
  def zoom_in(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
              html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::


    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    components = self.awesome('fas fa-search-plus', text, tooltip, position, width, height, html_code, options, profile)
    components.style.css.color = self.page.theme.greys[-6]
    return components

  @html.Html.css_skin()
  def warning(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
              html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    components = self.awesome(
      'fas fa-exclamation-triangle', text, tooltip, position, width, height, html_code, options, profile)
    components.style.css.color = self.page.theme.warning[1]
    return components

  @html.Html.css_skin()
  def danger(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
             html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    components = self.awesome('fas fa-stop-circle', text, tooltip, position, width, height, html_code, options, profile)
    components.style.css.color = self.page.theme.danger[1]
    return components

  @html.Html.css_skin()
  def error(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
            html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    components = self.awesome('fas fa-exclamation-triangle', text, tooltip, position, width, height, html_code,
                              options, profile)
    components.style.css.color = self.page.theme.danger[1]
    return components

  @html.Html.css_skin()
  def info(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'), html_code=None,
           options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    components = self.awesome(
      'fas fa-question-circle', text, tooltip, position, width, height, html_code, options, profile)
    return components

  @html.Html.css_skin()
  def save(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'), html_code=None,
           options=None, profile=None):
    """
    Description:
    ------------

    Usage::


    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome("fas fa-save", text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def refresh(self, text=None, position=None, tooltip="Refresh Component", width=(None, 'px'), height=(None, 'px'),
              html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.refresh()
      page.ui.icons.refresh().color("red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('fas fa-sync-alt', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def pdf(self, text=None, position=None, tooltip="Convert to PDF", width=(None, 'px'), height=(None, 'px'),
          html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.pdf(tooltip="helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('far fa-file-pdf', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def plus(self, text=None, position=None, tooltip="Add line", width=(None, 'px'), height=(None, 'px'),
           html_code=None, options=None, profile=None):
    """
    Description:
    ------------


   Usage::

      page.ui.icons.plus()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('fas fa-plus-square', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def excel(self, text=None, position=None, tooltip="Convert to Excel", width=(None, 'px'), height=(None, 'px'),
            html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.excel()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('far fa-file-excel', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def download(self, text=None, position=None, tooltip="Download", width=(None, 'px'), height=(None, 'px'),
               html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.download()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('fas fa-download', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def delete(self, text=None, position=None, align='left', tooltip="Delete Component on the page", width=(None, 'px'),
             height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.delete()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip.
    :param align: String. The text-align property within this component.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.awesome('far fa-trash-alt', text, tooltip, position, width, height, html_code, options, profile)
    component.hover_color = 'danger'
    component.style.css.white_space = "nowrap"
    component.style.css.margin = align
    return component

  @html.Html.css_skin()
  def zoom(self, text=None, position=None, tooltip="Zoom on Component", width=(None, 'px'), height=(None, 'px'),
           html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.zoom()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('fas fa-search-plus', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def capture(self, text=None, position=None, tooltip="Save to clipboard", width=(None, 'px'), height=(None, 'px'),
              html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.capture()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-clipboard', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def remove(self, text=None, position=None, tooltip="Remove Item", width=(None, 'px'), height=(None, 'px'),
             html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.remove()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.awesome('fas fa-times-circle', text, tooltip, position, width, height, html_code, options, profile)
    component.hover_color = 'danger'
    component.style.css.white_space = "nowrap"
    return component

  @html.Html.css_skin()
  def clear(self, text=None, align='left', position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
            html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-times-circle <https://fontawesome.com/icons/fas fa-eraser>`_ icon

    Usage::

      page.ui.icons.clear()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param align:
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.awesome('fas fa-eraser', text, tooltip, position, width, height, html_code, options, profile)
    component.hover_color = 'danger'
    component.style.css.white_space = "nowrap"
    component.style.css.margin = align
    return component

  @html.Html.css_skin()
  def table(self, text=None, position=None, tooltip="Convert to Table", width=(None, 'px'), height=(None, 'px'),
            html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.table(tooltip="helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('fas fa-table', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def wrench(self, text=None, position=None, tooltip="Processing Time", width=(None, 'px'), height=(None, 'px'),
             html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.wrench()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.awesome('fas fa-wrench', text, tooltip, position, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def rss(self, text="RSS", position=None, align="left", tooltip="", width=('auto', ''), height=(25, 'px'),
          html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.rss()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    icon = self.awesome('fas fa-rss-square', text, tooltip, position, width, height, html_code, options, profile)
    icon.style.css.color = "#cc9547"
    icon.style.css.display = "inline-block"
    icon.icon.style.css.font_size = self.page.body.style.globals.font.normal(5)
    if text is not None:
      icon.span.style.css.text_align = "left"
      icon.span.style.css.float = None
    if align == "center":
      icon.style.css.width = "100%"
      icon.style.css.text_align = "center"
    return icon

  @html.Html.css_skin()
  def facebook(self, text=None, url="https://en-gb.facebook.com/", position=None, tooltip="Facebook", width=(25, 'px'),
               html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.facebook()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if width[0] is None:
      width = (self.page.body.style.globals.icon.big, 'px')
    options = options or {"target": "_blank", "font-factor": 8}
    icon = self.awesome('fab fa-facebook-f', text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#4267B2', 'padding-bottom': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url, options=options)])
    return icon

  @html.Html.css_skin()
  def messenger(self, text=None, url="https://en-gb.facebook.com/", position=None, tooltip="Facebook", width=(25, 'px'),
                html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.facebook()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {"target": "_blank", "font-factor": self.page.body.style.globals.font.size - 6}
    icon = self.awesome('fab fa-facebook-messenger', text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#0078FF', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url, options=options)])
    return icon

  @html.Html.css_skin()
  def twitter(self, text=None, url="https://twitter.com/Epykure1", position=None, tooltip="", width=(None, 'px'),
              html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.twitter()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if width[0] is None:
      width = (self.page.body.style.globals.icon.big, 'px')
    options = options or {"target": "_blank", "font-factor": 6}
    icon = self.awesome('fab fa-twitter', text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#1DA1F2', 'padding': '3px 3px 6px 3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url, options=options)])
    return icon

  @html.Html.css_skin()
  def twitch(self, text=None, url="https://www.twitch.tv/epykure1", position=None, tooltip="", width=(None, 'px'),
             html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.twitter()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if width[0] is None:
      width = (self.page.body.style.globals.icon.big, 'px')
    options = options or {"target": "_blank", "font-factor": 6}
    icon = self.awesome(
      'fab fa-twitch', text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#6441a5', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url, options=options)])
    return icon

  @html.Html.css_skin()
  def instagram(self, text=None, url="https://www.instagram.com/?hl=en", position=None, tooltip="Twitter",
                width=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.twitter()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if width[0] is None:
      width = (self.page.body.style.globals.icon.big, 'px')
    options = options or {"target": "_blank", "font-factor": 8}
    icon = self.awesome(
      'fab fa-instagram-square', text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#3f729b', 'padding': '0px 3px 5px 3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url, options=options)])
    return icon

  @html.Html.css_skin()
  def linkedIn(self, text=None, url="https://www.linkedin.com/in/epykure-python-58278a1b8/", position=None, tooltip="",
               width=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Create a linkedIn icon button which will by default point to the epykure account.
    Epykure account is the official account for the development of this framework.

    Usage::

      page.ui.icons.linkedIn()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text for the Icon.
    :param url: String. Optional. The url when clicked.
    :param position:
    :param tooltip: String. Optional. The tooltip when the mouse is hove.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if width[0] is None:
      width = (self.page.body.style.globals.icon.big, 'px')
    options = options or {"target": "_blank", "font-factor": 6}
    icon = self.awesome(
      'fab fa-linkedin-in', text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#0e76a8', 'padding': '3px 3px 6px 3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url, options=options)])
    return icon

  @html.Html.css_skin()
  def youtube(self, text=None, url="https://www.youtube.com/", position=None, tooltip="Follow us on Youtube",
              width=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.youtube()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if width[0] is None:
      width = (self.page.body.style.globals.icon.big, 'px')
    options = options or {"target": "_blank", "font-factor": 8}
    icon = self.awesome(
      'fab fa-youtube', text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#FF0000', 'padding': '3px 3px 8px 3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url, options=options)])
    return icon

  @html.Html.css_skin()
  def github(self, text=None, url="https://github.com/epykure/epyk-ui", position=None, tooltip="Go the the Github project",
             width=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Link to a Github repository.

    By default this icon button will redirect to the Epyk UI repository.

    Usage::

      page.ui.icons.github()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. optional. The text on the icon.
    :param url: String. Optional. The url link.
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {"target": "_blank", "font-factor": -2}
    icon = self.awesome('fab fa-github', text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"text-align": "center", "line-height": '%s%s' % (self.page.body.style.globals.font.size, 'px')})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url, options=options)])
    return icon

  @html.Html.css_skin()
  def python(self, text=None, url="https://pypi.org/", position=None, tooltip="",
             width=(25, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.python()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    icon = self.awesome(
      "fab fa-python", text, tooltip, position, width if text is None else "auto", None, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "padding-bottom": "3px", "text-align": "center",
              "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url)])
    return icon

  @html.Html.css_skin()
  def stackoverflow(self, text=None, url="https://stackoverflow.com/", position=None, tooltip="Share your comments",
                    width=(25, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------


    Usage::

      page.ui.icons.stackoverflow()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    icon = self.awesome("fab fa-stack-overflow", text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.page.js.navigateTo(url)])
    return icon

  @html.Html.css_skin()
  def mail(self, text=None, url="", position=None, tooltip="Share by mail", width=(25, 'px'), html_code=None,
           options=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-stack-overflow <https://fontawesome.com/icons/stack-overflow>`_ icon

    Usage::

      page.ui.icons.mail()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    icon = self.awesome("far fa-envelope", text, tooltip, position, width, width, html_code, options, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    return icon

  @html.Html.css_skin()
  def tick(self, flag=True, text=None, icons=(JsFontAwesome.ICON_CHECK, JsFontAwesome.ICON_TIMES), position=None,
           tooltip="", width=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Display a tick box component

    Usage::

      page.ui.icons.tick()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlRadio.Tick`

    Attributes:
    ----------
    :param flag: Boolean. The state for the tick component
    :param text: String. optional. The text for this component. Default none
    :param icons: Tuple. Optional. The two icons to use for the component state
    :param position: String. Optional. A string with the vertical position of the component
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    dftl_options = {"true": icons[0], "false": icons[1]}
    dftl_options.update(options or {})
    # report, position, icon, text, tooltip, width, height, html_code, profile
    icon = html.HtmlRadio.Tick(self.page, position, icons[0] if flag else icons[1], text, tooltip, width,
                               width, html_code, dftl_options, profile)
    icon.click([
      icon.icon.dom.switchClass(icons[0] if flag else icons[1], icons[1] if flag else icons[0]),
      icon.icon.dom.transition('background', self.page.theme.success[0], duration=.2, reverse=True)
    ])
    return icon

  @html.Html.css_skin()
  def epyk(self, align="center", format='logo'):
    """
    Description:
    ------------
    Add the Epyk Icon.

    Usage::

      page.ui.icons.epyk()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    Attributes:
    ----------
    :param align: String. Optional. A string with the horizontal position of the component
    :param format: String. Optional. The type of component (logo, small...)
    """
    if format == 'logo':
      img, width, height = "epyklogo.ico", (32, 'px'), (32, 'px')
    elif format == 'small':
      img, width, height = "epyklogo_whole_small.png", (45, 'px'), (32, 'px')
    else:
      img, width, height = "epyklogo_whole_big.png", ("auto", ''), ('auto', '')
    icon = self.page.ui.img(img, path="https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images",
                                      align=align, width=width, height=height)
    icon.css({"text-align": "center", "padding": "auto", "vertical-align": "middle"})
    return icon

  @html.Html.css_skin()
  def signin(self, text, width=(40, "px"), icon=None):
    """
    Description:
    ------------

    Usage::

      page.ui.icons.signin("test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.SignIn

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/icons.py

    Attributes:
    ----------
    :param text:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param icon: String. Optional. The component icon content from font-awesome references
    """
    width = Arguments.size(width, unit="px")
    bar = html.HtmlEvent.SignIn(self.page, text, width, icon)
    return bar

  @html.Html.css_skin()
  def bar(self, records=None, color=None, width=(70, 'px'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a bespoke options / actions bar with icons

    Usage::

    Related Pages:

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/chips.py

    Attributes:
    ----------
    :param records:
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    records = records or []
    options = options or {}
    html_opts = html.HtmlEvent.OptionsBar(self.page, records, width, height, color, options, profile)
    return html_opts

  @html.Html.css_skin()
  def avatar(self, img, name=None, width=(30, 'px'), height=(None, ''), options=None, profile=None):
    """
    Description:
    ------------
    Display an avatar component.

    Usage::


    Attributes:
    ----------
    :param img: String. The image full path
    :param name: String. Optional.The tooltip name
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    img = img.replace("\\", "/")
    if height[0] is None:
      height = width
    avatar = self.page.ui.div("&nbsp;", width=width, height=height, options=options, profile=profile)
    avatar.css({"padding": '5px', 'border-radius': '30px', 'background-repeat': 'no-repeat',
                'background-position': 'center', 'background-size': 'cover', 'cursor': 'pointer',
                'background-image': 'url(%s)' % img})
    if name is not None:
      avatar.tooltip(name)
    return avatar

  @html.Html.css_skin()
  def badge(self, text="", icon=None, width=(25, "px"), height=(25, "px"), background_color=None, color=None, url=None,
            tooltip=None, options=None, profile=None):
    """
    Description:
    ------------
    Display a badge component using Bootstrap

    Usage::

      page.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")
      page.ui.images.badge("This is a badge", background_color="red", color="white")
      page.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'right'})

      b = rptObj.ui.images.badge(7688, icon="fab fa-python", options={'badge_css': {'color': 'white', "background": 'red'}})
      b.options.badge_css = {"background": 'green'}

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Badge`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/badge/

    Attributes:
    ----------
    :param text: The content of the badge
    :param icon: Optional, A String with the icon to display from font-awesome
    :param background_color: Optional, The background color of the badge
    :param color: Optional, The text color of the badge
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param url:
    :param tooltip: String. Optional. The text to display in the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    if background_color is None:
      background_color = self.page.theme.greys[0]
    if color is None:
      color = self.page.theme.success[1]
    html_badge = html.HtmlImage.Badge(self.page, text, width, height, None, icon, background_color, color,
                                      url, tooltip, options or {}, profile)
    return html_badge

  @html.Html.css_skin()
  def date(self, value=None, label=None, icon="far fa-calendar-alt", color=None, width=(None, "px"), height=(None, "px"),
           html_code=None, profile=None, options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    Usage::

      page.ui.fields.date('2020-04-08', label="Date").included_dates(["2020-04-08", "2019-09-06"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

      https://jqueryui.com/datepicker/

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to the time component. Default now.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dftl_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dftl_options.update(options)
    html_dt = html.HtmlDates.DatePicker(
      self.page, value, label, icon, width, height, color, html_code, profile, dftl_options, helper)
    html_dt.input.style.css.width = 0
    html_dt.input.style.css.min_width = 0
    html_dt.input.style.css.border = 0
    html_dt.input.style.css.background = "inherit"
    return html_dt

  @html.Html.css_skin()
  def timer(self, time, js_funcs, icon="far fa-clock", width=(15, "px"), height=(15, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Usage::


    Attributes:
    ----------
    :param time: Integer. Interval time in second
    :param js_funcs: String | List. The Javascript functions
    :param icon: String. The font awesome icon reference
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {"started": True}
    if options is not None:
      dflt_options.update(options)
    t = self.awesome(icon, width=width, height=height, profile=profile)
    if dflt_options["started"]:
      t.spin().attr["data-active"] = 1
      self.page.body.onReady(
        [self.page.js.window.setInterval(js_funcs, "%s_timer" % t.htmlCode, time * 1000)])
    else:
      t.attr["data-active"] = 0
    t.click([
      self.page.js.if_(t.dom.getAttribute("data-active") == 1, [
        t.icon.dom.removeClass("fa-spin").r, t.dom.setAttribute("data-active", 0),
        self.page.js.window.clearInterval("%s_timer" % t.htmlCode)
      ]).else_([
        t.icon.dom.addClass("fa-spin"), t.dom.setAttribute("data-active", 1),
        self.page.js.window.setInterval(js_funcs, "%s_timer" % t.htmlCode, time)
      ]),
    ])
    return t

  @html.Html.css_skin()
  def large(self, icon=None, family=None, width=(None, 'px'), height=(None, "px"), html_code=None, color=None,
            tooltip=None, align="left", options=None, profile=None):
    """
    Description:
    ------------

    Usage::


    Attributes:
    ----------
    :param icon:
    :param family:
    :param width:
    :param height:
    :param html_code:
    :param color:
    :param tooltip:
    :param align:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    icon = self.page.ui.icon(icon, family, width, html_code, height, color, tooltip, align, options, profile)
    icon.style.css.font_factor(30)
    icon.style.css.border_radius = 40
    icon.style.css.padding = 20
    icon.style.css.color = self.page.theme.greys[0]
    icon.style.css.background = self.page.theme.colors[2]
    if align == "center":
      icon.style.css.margin = "auto"
      icon.style.css.display = "inline-block"
      self.page.ui.div(icon, align="center")
    return icon

  @html.Html.css_skin()
  def menu(self, data, width=(100, '%'), height=(None, 'px'), align="left", options=None, profile=False):
    """
    Description:
    ------------
    Add a menu bar with multiple icons.

    Usage::

      menu = page.ui.icons.menu([
        {"icon": "fab fa-github-square", "tooltip": "Github path", 'url': 'test'},
        {"icon": "far fa-eye"},
        {"icon": "fas fa-file-code"}
      ])

    Attributes:
    ----------
    :param data: List. The icons definition.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {"margin-right": 5}
    if options is not None:
      dflt_options.update(options)
    div = self.page.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    for d in data:
      div.add(self.page.ui.icons.awesome(
        icon=d["icon"], tooltip=d.get("tooltip", ""), width=self.page.body.style.globals.icon.normal,
        options=options, profile=profile))
      div[-1].style.css.margin_right = dflt_options["margin-right"]
      div[-1].style.css.color = self.page.theme.greys[5]
      div[-1].style.add_classes.div.color_hover()
      if 'url' in d:
        div[-1].goto(d["url"], target="_blank")
    return div

  def hamburger(self, width=(15, 'px'), height=(2, 'px'), color=None, options=None, profile=None):
    """
    Description:
    ------------

    https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_menu_icon_js

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    height = Arguments.size(height, unit="px")
    bar1 = self.page.ui.div(width=width, height=height, profile=profile)
    bar1.style.add_classes.external("bar1")
    bar1.style.css.background_color = color or self.page.theme.colors[-1]
    bar1.style.css.display = "block"
    bar1.style.css.transition = 0.4
    bar1.style.css.margin = "%spx 0" % height[0]
    bar2 = self.page.ui.div(width=width, height=height, profile=profile)
    bar2.style.add_classes.external("bar2")
    bar2.style.css.background_color = color or self.page.theme.colors[-1]
    bar2.style.css.display = "block"
    bar2.style.css.margin = "%spx 0" % height[0]
    bar2.style.css.transition = 0.4
    bar3 = self.page.ui.div(width=width, height=height, profile=profile)
    bar3.style.add_classes.external("bar3")
    bar3.style.css.background_color = color or self.page.theme.colors[-1]
    bar3.style.css.display = "block"
    bar3.style.css.margin = "%spx 0" % height[0]
    bar3.style.css.transition = 0.4
    component = self.page.ui.div([bar1, bar2, bar3], width=width, options=options, profile=profile)
    component.style.add_custom_class({"transform": "rotate(-45deg) translate(-3px, 1px)"}, "change-hamburger .bar1")
    component.style.add_custom_class({"transform": "rotate(45deg) translate(-4px, -3px)"}, "change-hamburger .bar3")
    component.style.add_custom_class({"opacity": 0}, "change-hamburger .bar2")
    component.style.css.cursor = "pointer"
    component.set_icon = str
    component.click([
      component.dom.classList.toggle("change-hamburger")
    ])
    return component

  @property
  def toggles(self):
    """
    Description:
    ------------
    More custom toggles icons.
    """
    return Toggles(self)

  def gallery(self, icons=None, columns=6, width=(None, '%'), height=('auto', ''), options=None, profile=None):
    """
    Description:
    ------------
    Mosaic of pictures.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param icons: List. Optional. The list with the pictures.
    :param columns: Integer. Optional. The number of column for the mosaic component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {}
    if options is not None:
      dflt_options.update(options)
    grid = self.page.ui.grid(width=width, height=height, options=dflt_options, profile=profile)
    grid.style.css.margin_top = 20
    grid.style.css.overflow = 'hidden'
    grid.style.css.margin_bottom = 20
    row = self.page.ui.row(options=dflt_options)
    grid.icons = []
    grid.texts = {}
    for i, icon in enumerate(icons):
      if dflt_options.get("max") is not None and len(grid.icons) > dflt_options.get("max"):
        break

      if i % columns == 0:
        grid.add(row)
        row = self.page.ui.row(options=dflt_options)
      text = None
      if not hasattr(icon, 'options'):
        if isinstance(icon, dict):
          if 'html_code' not in icon:
            icon["html_code"] = "%s_%s" % (grid.htmlCode, i)
          if 'align' not in icon:
            icon['align'] = "center"
          if "text" in icon:
            text = self.page.ui.text(icon["text"], options=dflt_options)
            text.style.css.bold()
            text.style.css.white_space = "nowrap"
            grid.texts[i] = text
            del icon["text"]

          icon = self.page.ui.icon(**icon)
        else:
          icon = self.page.ui.icon(icon, html_code="%s_%s" % (grid.htmlCode, i), align="center")
        icon.style.css.font_factor(15)
        icon.style.css.text_align = "center"
        grid.icons.append(icon)
      if text is not None:
        text.style.css.display = "inline-block"
        text.style.css.width = "100%"
        text.style.css.text_align = "center"
        row.add(self.page.ui.col([icon, text], align="center", options=dflt_options))
      else:
        row.add(icon)
      row.attr["class"].add("mt-3")
      icon.parent = row[-1]
    if len(row):
      for i in range(columns - len(row)):
        row.add(self.page.ui.text("&nbsp;"))
      row.attr["class"].add("mt-3")
      grid.add(row)
    grid.style.css.color = self.page.theme.greys[6]
    grid.style.css.padding_top = 5
    grid.style.css.padding_bottom = 5
    return grid


class Toggles:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def collapse(self, icon_on="fas fa-compress", icon_off="fas fa-expand", family=None, width=(None, 'px'),
               html_code=None, height=(None, "px"), color=None, tooltip=None, align="left", options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      page.ui.images.icon("fab fa-angellist")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Icon`

    Related Pages:

      https://fontawesome.com/icons?m=free

    Attributes:
    ----------
    :param icon_on: String. Optional. The component icon content from font-awesome references
    :param icon_off: String. Optional. The component icon content from font-awesome references
    :param family:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: String. Optional. The font color in the component. Default inherit
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param align: String. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    options = options or {}
    options['icon_family'] = family or 'font-awesome'
    html_icon = html.HtmlImage.IconToggle(
      self.page, icon_on, width=width, height=height, color=color, tooltip=tooltip, options=options,
      html_code=html_code, profile=profile)
    html_icon.icon_on = icon_on
    html_icon.icon_off = icon_off
    return html_icon

  @html.Html.css_skin()
  def lock(self, icon_on="fas fa-lock-open", icon_off="fas fa-lock", family=None, width=(None, 'px'), html_code=None,
           height=(None, "px"), color=None, tooltip=None, align="left", options=None, profile=None):
    """
    Description:
    ------------
    Add a lock toggle button.

    Usage::

      page.ui.icons.toggles.lock()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Icon`

    Related Pages:

      https://fontawesome.com/icons?m=free

    Attributes:
    ----------
    :param icon_on: String. Optional. The component icon content from font-awesome references
    :param icon_off: String. Optional. The component icon content from font-awesome references
    :param family:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: String. Optional. The font color in the component. Default inherit
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param align: String. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    options = options or {}
    options['icon_family'] = family or 'font-awesome'
    html_icon = html.HtmlImage.IconToggle(self.page, icon_on, width=width, height=height, color=color,
                                          tooltip=tooltip, options=options, html_code=html_code, profile=profile)
    html_icon.icon_on = icon_on
    html_icon.icon_off = icon_off
    return html_icon
