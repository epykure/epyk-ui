#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.js.packages import JsFontAwesome
from epyk.core.css import Defaults as Defaults_css
from epyk.interfaces import Arguments


class Icons(object):
  def __init__(self, context):
    self.context = context

  @property
  def get(self):
    return JsFontAwesome

  @html.Html.css_skin()
  def awesome(self, icon, text=None, tooltip=None, position=None, width=(25, 'px'), height=(25, 'px'),
              htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.icons.awesome(icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/icons.py

    Attributes:
    ----------
    :param icon: String. The font awesome icon reference
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_edit = html.HtmlButton.IconEdit(self.context.rptObj, position, icon, text, tooltip, width, height, htmlCode, options or {}, profile)
    html_edit.css({"margin": "5px 0", 'cursor': 'pointer'})
    html_edit.style.css.float = position
    html_edit.style.css.display = "inline"
    return html_edit

  def fluent(self, icon, text=None, tooltip=None, position=None, width=(25, 'px'), height=(25, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.icons.awesome(icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`
    ms-Icon ms-Icon--AdminDLogoInverse32

    Attributes:
    ----------
    :param icon: String. The fluentui icon reference
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_edit = html.HtmlButton.IconEdit(self.context.rptObj, position, icon, text, tooltip, width, height, htmlCode, options or {}, profile)
    html_edit.css({"margin": "5px 0", 'cursor': 'pointer'})
    html_edit.style.css.float = position
    html_edit.style.css.display = "inline-block"
    return html_edit

  def edit(self, text=None, position=None, tooltip="Edit", width=(None, 'px'), height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-edit <https://fontawesome.com/icons/edit>`_ icon

    Usage::

      rptObj.ui.icons.edit()
      rptObj.ui.icons.edit().color("red")

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
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-edit', text, tooltip, position, width, height, htmlCode, profile)

  def clock(self, text=None, position=None, tooltip="Last Updated Time", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-clock <https://fontawesome.com/icons/clock>`_ icon

    Usage::

      rptObj.ui.icons.clock()
      rptObj.ui.icons.clock().color("red")

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
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-clock', text, tooltip, position, width, height, htmlCode, profile)

  def next(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    components = self.awesome('fas fa-caret-right', text, tooltip, position, width, height, htmlCode, profile)
    components.icon.style.css.font_factor(10)
    return components

  def previous(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    components = self.awesome('fas fa-caret-left', text, tooltip, position, width, height, htmlCode, profile)
    components.icon.style.css.font_factor(10)
    return components

  def zoom_out(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    components = self.awesome('fas fa-search-minus', text, tooltip, position, width, height, htmlCode, profile)
    components.style.css.color = self.context.rptObj.theme.greys[-6]
    return components

  def zoom_in(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    components = self.awesome('fas fa-search-plus', text, tooltip, position, width, height, htmlCode, profile)
    components.style.css.color = self.context.rptObj.theme.greys[-6]
    return components

  def save(self, text=None, position=None, tooltip="", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome("fas fa-save", text, tooltip, position, width, height, htmlCode, profile)

  def refresh(self, text=None, position=None, tooltip="Refresh Component", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-sync-alt <https://fontawesome.com/icons/sync-alt>`_ icon

    Usage::

      rptObj.ui.icons.refresh()
      rptObj.ui.icons.refresh().color("red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-sync-alt', text, tooltip, position, width, height, htmlCode, profile)

  def pdf(self, text=None, position=None, tooltip="Convert to PDF", width=(None, 'px'), height=(None, 'px'),
          htmlCode=None,  profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-file-pdf <https://fontawesome.com/icons/file-pdf>`_ icon

    Usage::

      rptObj.ui.icons.pdf(tooltip="helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-file-pdf', text, tooltip, position, width, height, htmlCode, profile)

  def plus(self, text=None, position=None, tooltip="Add line", width=(None, 'px'), height=(None, 'px'),
           htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-file-pdf <https://fontawesome.com/icons/plus-square>`_ icon

    Usage::

      rptObj.ui.icons.plus()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-plus-square', text, tooltip, position, width, height, htmlCode, profile)

  def excel(self, text=None, position=None, tooltip="Convert to Excel", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-file-excel <https://fontawesome.com/icons/file-excel>`_ icon

    Usage::

      rptObj.ui.icons.excel()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-file-excel', text, tooltip, position, width, height, htmlCode, profile)

  def download(self, text=None, position=None, tooltip="Download", width=(None, 'px'), height=(None, 'px'),
               htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-download <https://fontawesome.com/icons/download>`_ icon

    Usage::

      rptObj.ui.icons.download()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-download', text, tooltip, position, width, height, htmlCode, profile)

  def delete(self, text=None, position=None, align='left', tooltip="Delete Component on the page", width=(None, 'px'),
             height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-trash-alt <https://fontawesome.com/icons/trash-alt>`_ icon

    Usage::

      rptObj.ui.icons.delete()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    component = self.awesome('far fa-trash-alt', text, tooltip, position, width, height, htmlCode, profile)
    component.hover_color = 'danger'
    component.style.css.white_space = "nowrap"
    component.style.css.margin = align
    return component

  def zoom(self, text=None, position=None, tooltip="Zoom on Component", width=(None, 'px'), height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-search-plus <https://fontawesome.com/icons/search-plus>`_ icon

    Usage::

      rptObj.ui.icons.zoom()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-search-plus', text, tooltip, position, width, height, htmlCode, profile)

  def capture(self, text=None, position=None, tooltip="Save to clipboard", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-clipboard <https://fontawesome.com/icons/clipboard>`_ icon

    Usage::

      rptObj.ui.icons.capture()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-clipboard', text, tooltip, position, width, height, htmlCode, profile)

  def remove(self, text=None, position=None, tooltip="Remove Item", width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-times-circle <https://fontawesome.com/icons/times-circle>`_ icon

    Usage::

      rptObj.ui.icons.remove()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    component = self.awesome('fas fa-times-circle', text, tooltip, position, width, height, htmlCode, profile)
    component.hover_color = 'danger'
    component.style.css.white_space = "nowrap"
    return component

  def clear(self, text=None, align='left', position=None, tooltip="", width=(None, 'px'), height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-times-circle <https://fontawesome.com/icons/fas fa-eraser>`_ icon

    Usage::

      rptObj.ui.icons.clear()

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
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    component = self.awesome('fas fa-eraser', text, tooltip, position, width, height, htmlCode, profile)
    component.hover_color = 'danger'
    component.style.css.white_space = "nowrap"
    component.style.css.margin = align
    return component

  def table(self, text=None, position=None, tooltip="Convert to Table", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-table <https://fontawesome.com/icons/table>`_ icon

    Usage::

      rptObj.ui.icons.table(tooltip="helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-table', text, tooltip, position, width, height, htmlCode, profile)

  def wrench(self, text=None, position=None, tooltip="Processing Time", width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-wrench <https://fontawesome.com/icons/wrench>`_ icon

    Usage::

      rptObj.ui.icons.wrench()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-wrench', text, tooltip, position, width, height, htmlCode, profile)

  def rss(self, text="RSS", position=None, align="left", tooltip="", width=('auto', ''), height=(25, 'px'),
             htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-wrench <https://fontawesome.com/icons/rss-square?style=solid>`_ icon

    Usage::

      rptObj.ui.icons.rss()

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
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    icon = self.awesome('fas fa-rss-square', text, tooltip, position, width, height, htmlCode, profile)
    icon.style.css.color = "#cc9547"
    icon.style.css.display = "inline-block"
    icon.icon.style.css.font_size = Defaults_css.font(5)
    if text is not None:
      icon.span.style.css.text_align = "left"
      icon.span.style.css.float = None
    if align == "center":
      icon.style.css.width = "100%"
      icon.style.css.text_align = "center"
    return icon

  def facebook(self, text=None, url="https://en-gb.facebook.com/", position=None, tooltip="Facebook", width=(25, 'px'),
               htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-facebook-f <https://fontawesome.com/icons/facebook-f>`_ icon

    Usage::

      rptObj.ui.icons.facebook()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    icon = self.awesome('fab fa-facebook-f', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#4267B2', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def messenger(self, text=None, url="https://en-gb.facebook.com/", position=None, tooltip="Facebook", width=(25, 'px'),
                htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-facebook-f <https://fontawesome.com/icons/facebook-f>`_ icon

    Usage::

      rptObj.ui.icons.facebook()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed to this component. Default None
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-facebook-messenger', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#0078FF', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def twitter(self, text=None, url="https://twitter.com", position=None, tooltip="", width=(25, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-twitter <https://fontawesome.com/icons/twitter>`_ icon

    Usage::

      rptObj.ui.icons.twitter()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-twitter', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#1DA1F2', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def twitch(self, text=None, url="https://www.twitch.tv/", position=None, tooltip="Twitter", width=(25, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-twitch <https://fontawesome.com/icons/twitch?style=brands`_ icon

    Usage::

      rptObj.ui.icons.twitter()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-twitch', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#6441a5', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def instagram(self, text=None, url="https://www.instagram.com/?hl=en", position=None, tooltip="Twitter", width=(25, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-instagram-square <https://fontawesome.com/icons/instagram-square?style=brands

    Usage::

      rptObj.ui.icons.twitter()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-instagram-square', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#3f729b', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def linkedIn(self, text=None, url="https://www.linkedin.com/home/?originalSubdomain=uk", position=None, tooltip="",
               width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-linkedin-in <https://fontawesome.com/icons/linkedin-in>`_ icon

    Usage::

      rptObj.ui.icons.linkedIn()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-linkedin-in', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#0e76a8', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def youtube(self, text=None, url="https://www.youtube.com/", position=None, tooltip="Follow us on Youtube",
              width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-youtube <https://fontawesome.com/icons/youtube>`_ icon

    Usage::

      rptObj.ui.icons.youtube()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-youtube', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": '#FF0000', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()# addCls("CssDivOnHoverBackgroundLight")
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def github(self, text=None, url="https://github.com/", position=False, tooltip="Go the the Github project",
             width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-github <https://fontawesome.com/icons/github>`_ icon

    Usage::

      rptObj.ui.icons.github()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-github', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def python(self, text=None, url="https://pypi.org/", position=None, tooltip="Like or package",
             width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-python <https://fontawesome.com/icons/python>`_ icon

    Usage::

      rptObj.ui.icons.python()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome("fab fa-python", text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def stackoverflow(self, text=None, url="https://stackoverflow.com/", position=None, tooltip="Share your comments",
                    width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-stack-overflow <https://fontawesome.com/icons/stack-overflow>`_ icon

    Usage::

      rptObj.ui.icons.stackoverflow()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome("fab fa-stack-overflow", text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue', 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def mail(self, text=None, url="", position=None, tooltip="Share by mail", width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-stack-overflow <https://fontawesome.com/icons/stack-overflow>`_ icon

    Usage::

      rptObj.ui.icons.mail()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome("far fa-envelope", text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", 'padding': '3px'})
    icon.style.add_classes.div.background_hover()
    return icon

  def tick(self, flag=True, text=None, icons=(JsFontAwesome.ICON_CHECK, JsFontAwesome.ICON_TIMES), position=None,
           tooltip="", width=(None, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------
    Display a tick box component

    Usage::

      rptObj.ui.icons.tick()

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
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    dftl_options = {"true": icons[0], "false": icons[1]}
    dftl_options.update(options or {})
    # report, position, icon, text, tooltip, width, height, htmlCode, profile
    icon = html.HtmlRadio.Tick(self.context.rptObj, position, icons[0] if flag else icons[1], text, tooltip, width, width,
                               htmlCode, dftl_options, profile)
    icon.click([
      icon.icon.dom.switchClass(icons[0] if flag else icons[1], icons[1] if flag else icons[0]),
      icon.icon.dom.transition('background', self.context.rptObj.theme.success[0], duration=.2, reverse=True)
    ])
    return icon

  def epyk(self, align="center", format='logo'):
    """
    Description:
    ------------
    Add the Epyk Icon

    Usage::

      rptObj.ui.icons.epyk()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    Attributes:
    ----------
    :param align: String. Optional. A string with the horizontal position of the component
    :param format: String. optional. The type of component (logo, small...)
    """
    if format == 'logo':
      img, width, height = "epyklogo.ico", (32, 'px'), (32, 'px')
    elif format == 'small':
      img, width, height = "epyklogo_whole_small.png", (45, 'px'), (32, 'px')
    else:
      img, width, height = "epyklogo_whole_big.png", ("auto", ''), ('auto', '')
    icon = self.context.rptObj.ui.img(img, path="https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images",
                                      align=align, width=width, height=height)
    icon.css({"text-align": "center", "padding": "auto", "vertical-align": "middle"})
    icon.style.add_classes.div.background_hover()
    return icon

  def signin(self, text, width=(40, "px"), icon=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.icons.signin("test")

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
    bar = html.HtmlEvent.SignIn(self.context.rptObj, text, width, icon)
    return bar

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
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    records = records or []
    options = options or {}
    html_opts = html.HtmlEvent.OptionsBar(self.context.rptObj, records, width, height, color, options, profile)
    return html_opts

  def avatar(self, img, name=None, width=(30, 'px'), height=(None, ''), options=None, profile=None):
    """
    Description:
    ------------
    Display an avatar component

    Attributes:
    ----------
    :param img: String. The image full path
    :param name: String. Optional.The tooltip name
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    img = img.replace("\\", "/")
    if height[0] is None:
      height = width
    avatar = self.context.rptObj.ui.div("&nbsp;", width=width, height=height, options=options, profile=profile)
    avatar.css({"padding": '5px', 'border-radius': '30px', 'background-repeat': 'no-repeat',
                'background-position': 'center', 'background-size': 'cover', 'cursor': 'pointer',
                'background-image': 'url(%s)' % img})
    if name is not None:
      avatar.tooltip(name)
    return avatar

  def badge(self, text="", icon=None, width=(25, "px"), height=(25, "px"), background_color=None, color=None, url=None,
            tooltip=None, options=None, profile=None):
    """
    Description:
    ------------
    Display a badge component using Bootstrap

    Usage::

      rptObj.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")
      rptObj.ui.images.badge("This is a badge", background_color="red", color="white")
      rptObj.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'right'})

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
    :param tooltip: Optional, The text to display in the tooltip
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Optional, A boolean to store the performances for each components
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    if background_color is None:
      background_color = self.context.rptObj.theme.greys[0]
    if color is None:
      color = self.context.rptObj.theme.success[1]
    html_badge = html.HtmlImage.Badge(self.context.rptObj, text, width, height, None, icon, background_color, color, url,
                                      tooltip, options or {}, profile)
    return html_badge

  def date(self, value, label=None, icon="far fa-calendar-alt", color=None, width=(None, "px"), height=(None, "px"),
           htmlCode=None, profile=None, options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    Usage::

      rptObj.ui.fields.date('2020-04-08', label="Date").included_dates(["2020-04-08", "2019-09-06"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

      https://jqueryui.com/datepicker/

    Attributes:
    ----------
    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dftl_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dftl_options.update(options)
    html_dt = html.HtmlDates.DatePicker(self.context.rptObj, value, label, icon, width, height, color, htmlCode, profile, dftl_options, helper)
    html_dt.input.style.css.width = 0
    return html_dt

  def timer(self, time, jsFncs, icon="far fa-clock", width=(15, "px"), height=(15, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param time: Integer. Interval time in second
    :param jsFncs: String or List. The Javascript functions
    :param icon: String. The font awesome icon reference
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    dflt_options = {"started": True}
    if options is not None:
      dflt_options.update(options)
    t = self.awesome(icon, width=width, height=height, profile=profile)
    if dflt_options["started"]:
      t.spin().attr["data-active"] = 1
      self.context.rptObj.body.onReady([self.context.rptObj.js.window.setInterval(jsFncs, "%s_timer" % t.htmlCode, time * 1000)])
    else:
      t.attr["data-active"] = 0
    t.click([
      self.context.rptObj.js.if_(t.dom.getAttribute("data-active") == 1, [
        t.icon.dom.removeClass("fa-spin").r, t.dom.setAttribute("data-active", 0),
        self.context.rptObj.js.window.clearInterval("%s_timer" % t.htmlCode)
      ]).else_([
        t.icon.dom.addClass("fa-spin"), t.dom.setAttribute("data-active", 1),
        self.context.rptObj.js.window.setInterval(jsFncs, "%s_timer" % t.htmlCode, time)
      ]),
    ])
    return t

  def large(self, icon=None, family=None, width=(None, 'px'), htmlCode=None, height=(None, "px"), color=None, tooltip=None, align="left", options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon:
    :param family:
    :param width:
    :param htmlCode:
    :param height:
    :param color:
    :param tooltip:
    :param align:
    :param options:
    :param profile:
    """
    icon = self.context.rptObj.ui.icon(icon, family, width, htmlCode, height, color, tooltip, align, options, profile)
    icon.style.css.font_factor(30)
    icon.style.css.border_radius = 40
    icon.style.css.padding = 20
    icon.style.css.color = self.context.rptObj.theme.greys[0]
    icon.style.css.background = self.context.rptObj.theme.colors[2]
    if align == "center":
      icon.style.css.margin = "auto"
      icon.style.css.display = "inline-block"
      self.context.rptObj.ui.div(icon, align="center")
    return icon

  @property
  def toggles(self):
    """
    Description:
    ------------
    More custom toggles icons
    """
    return Toggles(self.context)


class Toggles(object):

  def __init__(self, context):
    self.context = context

  def collapse(self, icon_on="fas fa-compress", icon_off="fas fa-expand", family=None, width=(None, 'px'), htmlCode=None,
               height=(None, "px"), color=None, tooltip=None, align="left", options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.images.icon("fab fa-angellist")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Icon`

    Related Pages:

      https://fontawesome.com/icons?m=free

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references
    :param family:
    :param htmlCode:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: String. Optional. The font color in the component. Default inherit
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param align: String. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    options = options or {}
    options['icon_family'] = family or 'font-awesome'
    html_icon = html.HtmlImage.IconToggle(self.context.rptObj, icon_on, width=width, height=height,
         color=color, tooltip=tooltip, options=options, htmlCode=htmlCode, profile=profile)
    html_icon.icon_on = icon_on
    html_icon.icon_off = icon_off
    return html_icon

  def lock(self, icon_on="fas fa-lock-open", icon_off="fas fa-lock", family=None, width=(None, 'px'), htmlCode=None,
               height=(None, "px"), color=None, tooltip=None, align="left", options=None, profile=None):
    """
    Description:
    ------------
    Add a lock toggle button.

    Usage::

      rptObj.ui.icons.toggles.lock()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Icon`

    Related Pages:

      https://fontawesome.com/icons?m=free

    Attributes:
    ----------
    :param icon_on: String. Optional. The component icon content from font-awesome references
    :param icon_off: String. Optional. The component icon content from font-awesome references
    :param family:
    :param htmlCode:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: String. Optional. The font color in the component. Default inherit
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param align: String. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    options = options or {}
    options['icon_family'] = family or 'font-awesome'
    html_icon = html.HtmlImage.IconToggle(self.context.rptObj, icon_on, width=width, height=height,
         color=color, tooltip=tooltip, options=options, htmlCode=htmlCode, profile=profile)
    html_icon.icon_on = icon_on
    html_icon.icon_off = icon_off
    return html_icon
