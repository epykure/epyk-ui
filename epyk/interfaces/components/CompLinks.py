#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Links(object):

  def __init__(self, context):
    self.context = context

  def external(self, text, url, icon=None, helper=None, height=(None, 'px'), decoration=False, htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.links.external('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Related Pages:

      https://www.w3schools.com/TagS/att_a_href.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    Attributes:
    ----------
    :param text: The string value to be displayed in the component
    :param url: The string url of the link
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param helper: String. Optional. A tooltip helper
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    dft_options = {"target": '_blank'}
    if options is not None:
      dft_options.update(options)
    html_link = html.HtmlLinks.ExternalLink(self.context.rptObj, text, url, icon, helper, height, decoration, htmlCode, dft_options, profile)
    return html_link

  def button(self, text, url, icon=None, helper=None, height=(None, 'px'), decoration=False, htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    Attributes:
    ----------
    :param text:
    :param url: String. The destination page when clicked
    :param icon: String. Optional. The component icon content from font-awesome references
    :param helper: String. Optional. A tooltip helper
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    dft_options = {"target": '_blank'}
    if options is not None:
      dft_options.update(options)
    html_link = html.HtmlLinks.ExternalLink(self.context.rptObj, text, url, icon, helper, height, decoration, htmlCode, dft_options, profile)
    html_link.style.add_classes.button.basic()
    html_link.style.css.padding = "0 10px"
    return html_link

  def link(self, text="", url="", icon=None, helper=None, height=(None, 'px'), decoration=False, htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------
    Python interface to the common Hyperlink

    Usage::

      rptObj.ui.link({"text": "Profiling results", "url": '#'})
      l = rptObj.ui.links.link('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
      b = rptObj.ui.images.badge("new")
      l.append_child(b)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Attributes:
    ----------
    :param text: The string value to be displayed in the component
    :param url: The string url of the link
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param helper: String. Optional. A tooltip helper
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    options = options or {}
    if url is not None and not hasattr(url, 'toStr') and url.startswith("www."):
      url = "//%s" % url
    html_link = html.HtmlLinks.ExternalLink(self.context.rptObj, text, url, icon, helper, height, decoration, htmlCode, options, profile)
    return html_link

  def data(self, text, value, width=(None, '%'), height=(None, 'px'), format='txt', profile=None):
    """
    Description:
    ------------
    Python interface to the Hyperlink to retrieve data

    Usage::

      data_link = rptObj.ui.links.data("link", "test#data")
      data_link.build({"text": 'new link Name', 'data': "new content"})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.DataLink`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    Attributes:
    ----------
    :param text: String. The string value to be displayed in the component
    :param value: String. The value to be displayed to this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param format: String. Optional. The downloaded data format
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    html_data = html.HtmlLinks.DataLink(self.context.rptObj, text, value, width=width, height=height, format=format, profile=profile)
    return html_data
