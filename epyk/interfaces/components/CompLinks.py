#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


class Links:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def external(self, text, url, icon=None, align="left", helper=None, height=(None, 'px'), decoration=False,
               html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.links.external('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Related Pages:

      https://www.w3schools.com/TagS/att_a_href.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param url: String. Optional. The string url of the link
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome
    :param align: String. Optional. The text-align property within this component.
    :param helper: String. Optional. A tooltip helper
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    dft_options = {"target": '_blank'}
    if options is not None:
      dft_options.update(options)
    text = self.page.py.encode_html(text)
    html_link = html.HtmlLinks.ExternalLink(self.page, text, url, icon, helper, height, decoration, html_code,
                                            dft_options, profile)
    if align == "center":
      self.page.ui.div(html_link, align=align)
    return html_link

  @html.Html.css_skin()
  def button(self, text="", url="", icon=None, helper=None, height=(None, 'px'), decoration=False, html_code=None,
             options=None, profile=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Usage:
    -----

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param url: String. The destination page when clicked
    :param icon: String. Optional. The component icon content from font-awesome references
    :param helper: String. Optional. A tooltip helper
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param html_code:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    dft_options = {"target": '_blank'}
    if options is not None:
      dft_options.update(options)
    html_link = html.HtmlLinks.ExternalLink(self.page, text, url, icon, helper, height, decoration,
                                            html_code, dft_options, profile)
    html_link.style.add_classes.button.basic()
    html_link.style.css.padding = "0 10px"
    return html_link

  @html.Html.css_skin()
  def link(self, text="", url="", icon=None, align="left", tooltip=None, helper=None, height=(None, 'px'),
           decoration=False, html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Python interface to the common Hyperlink.

    Usage:
    -----

      page.ui.link({"text": "Profiling results", "url": '#'})
      l = page.ui.links.link('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
      b = page.ui.images.badge("new")
      l.append_child(b)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param url: String. Optional. The string url of the link
    :param align: String. Optional. The text-align property within this component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome
    :param tooltip: String. Optional. The tooltip displayed when the mouse is on the component
    :param helper: String. Optional. A tooltip helper
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    options = options or {}
    if url is not None and not hasattr(url, 'toStr') and url.startswith("www."):
      url = "//%s" % url
    html_link = html.HtmlLinks.ExternalLink(self.page, text, url, icon, helper, height, decoration, html_code,
                                            options, profile)
    if tooltip is not None:
      html_link.tooltip(tooltip)
    if align == "center":
      self.page.ui.div(html_link, align=align)
    return html_link

  @html.Html.css_skin()
  def data(self, text, value, width=(None, '%'), height=(None, 'px'), fmt='txt', options=None, profile=None):
    """
    Description:
    ------------
    Python interface to the Hyperlink to retrieve data.

    Usage:
    -----

      data_link = page.ui.links.data("link", "test#data")
      data_link.build({"text": 'new link Name', 'data': "new content"})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.DataLink`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    Attributes:
    ----------
    :param text: String. The string value to be displayed in the component
    :param value: String. The value to be displayed to this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param fmt: String. Optional. The downloaded data format.
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storag.e
    """
    height = Arguments.size(height, unit="px")
    html_data = html.HtmlLinks.DataLink(self.page, text, value, width=width, height=height, fmt=fmt, options=options,
                                        profile=profile)
    return html_data

  @html.Html.css_skin()
  def colored(self, text="", url="", icon=None, helper=None, color=None, height=(None, 'px'), decoration=False,
              html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Display a link with the same layout than a buttons.colored HTML component.

    Usage:
    -----

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param url: String. Optional. The string url of the link
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome
    :param helper: String. Optional. A tooltip helper
    :param color: String. Optional. The font color in the component. Default inherit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: String. Optional. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    dft_options = {"target": '_blank'}
    if options is not None:
      dft_options.update(options)
    html_link = html.HtmlLinks.ExternalLink(self.page, text, url, icon, helper, height, decoration, html_code,
                                            dft_options, profile)
    html_link.style.add_classes.button.basic()
    html_link.style.css.padding = "0 10px"
    html_link.style.css.background = color or self.page.theme.colors[-1]
    html_link.style.css.border = "1px solid %s" % (color or self.page.theme.colors[-1])
    if icon is not None:
      html_link.icon.style.css.color = self.page.theme.colors[0]
    html_link.style.css.color = self.page.theme.colors[0]
    html_link.style.css.margin_top = 5
    html_link.style.css.line_height = Defaults_html.LINE_HEIGHT
    html_link.style.css.margin_bottom = 5
    return html_link

  @html.Html.css_skin()
  def upload(self, url="#", text="", icon="fas fa-upload", helper=None, height=(None, 'px'), decoration=False,
             align="left", html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    HTML component to upload files.

    Usage:
    -----

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param url: String. Optional. The string url of the link
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome
    :param helper: String. Optional. A tooltip helper
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param align:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    dft_options = {"target": '_self'}
    if options is not None:
      dft_options.update(options)
    html_link = html.HtmlLinks.ExternalLink(self.page, text, url, icon, helper, height, decoration, html_code,
                                            dft_options, profile)
    html_link.style.add_classes.button.basic()
    html_link.style.css.padding = "0 10px"
    html_link.style.css.remove("border", set_none=True)
    if not text:
      html_link.icon.style.css.remove("margin-right")
    html_link.style.css.border_radius = 20
    html_link.style.css.margin_top = 5
    html_link.style.css.line_height = False
    html_link.style.css.margin_bottom = 5
    if align == "center":
      html_link.style.css.margin = "auto"
      html_link.style.css.display = "block"
    elif align == "right":
      html_link.style.css.float = align
    return html_link

  @html.Html.css_skin()
  def download(self, url="#", text="", icon="fas fa-file-download", helper=None, height=(None, 'px'), decoration=False,
               align="left", html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    HTML component to upload files.

    Usage:
    -----

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param url: String. Optional. The string url of the link
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome
    :param helper: String. Optional. A tooltip helper
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param align:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    dft_options = {"target": '_self'}
    if options is not None:
      dft_options.update(options)
    html_link = html.HtmlLinks.ExternalLink(self.page, text, url, icon, helper, height, decoration, html_code,
                                            dft_options, profile)
    html_link.style.add_classes.button.basic()
    html_link.style.css.padding = "0 10px"
    html_link.style.css.remove("border", set_none=True)
    if not text:
      html_link.icon.style.css.remove("margin-right")
    html_link.style.css.border_radius = 20
    html_link.style.css.margin_top = 5
    html_link.style.css.line_height = False
    html_link.style.css.margin_bottom = 5
    if icon is not None:
      html_link.icon.style.css.margin_top = -3
    if align == "center":
      html_link.style.css.margin = "auto"
      html_link.style.css.display = "block"
    elif align == "right":
      html_link.style.css.float = align
    return html_link
