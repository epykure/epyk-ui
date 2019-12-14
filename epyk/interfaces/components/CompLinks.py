"""

"""

import importlib

from epyk.core import html


class Links(object):
  def __init__(self, context):
    self.context = context

  def external(self, text, url, icon=None, helper=None, height=(None, 'px'), decoration=False, options=None, profile=None):
    """

    Example
    rptObj.ui.links.external('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})

    Documentation
    https://www.w3schools.com/TagS/att_a_href.asp

    :param text: The string value to be displayed in the component
    :param url: The string url of the link
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param helper:
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    dft_options = {"target": '_blank'}
    if options is not None:
      dft_options.update(options)

    #if url.startswith("http"):
    #  url = "/%s" % url
    html_link = html.HtmlLinks.ExternalLink(self.context.rptObj, text, url, icon, helper, height, decoration, dft_options, profile)
    self.context.register(html_link)
    return html_link

  def script(self, script_name, report_name=None, icon="fab fa-python", options=None, profile=None):
    """
    Direct link to another report within the server.

    This is only dedicated to move between reports internally.
    If the target is to move between nodes, the function to use is rather bridge

    Example
    rptObj.ui.links.script("TestParams")

    :param script_name: The destination script name
    :param report_name: Optional, the report name. Default current one
    :param options: Optional, the link properties

    :rtype: html.HtmlLinks.ExternalLink

    :return:
    """
    script_name = script_name.replace(".py", "")
    text = script_name
    if report_name is None:
      report_name = self.context.rptObj.run.report_name
      mod = importlib.import_module("%s.%s" % (self.context.rptObj.run.report_name, script_name))
      text = mod.TITLE
    if 'name' in options:
      text = options['name']
      del options['name']

    url = "%s/run/%s/%s" % (self.context.rptObj._urlsApp['report'], report_name, script_name)
    return self.link(text, url, icon=icon, options=options, profile=profile)

  def link(self, text="", url="", icon=None, helper=None, height=(None, 'px'), decoration=False, options=None, profile=None):
    """
    Python interface to the common Hyperlink

    Example:
    rptObj.ui.link({"text": "Profiling results", "url": '#'})

    l = rptObj.ui.links.link('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
    b = rptObj.ui.images.badge("new")
    l.append_child(b)

    Documentation

    :param text: The string value to be displayed in the component
    :param url: The string url of the link
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param helper:
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param decoration:
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlLinks.ExternalLink

    :return:
    """
    if options is None:
      options = {}
    return self.context.register(html.HtmlLinks.ExternalLink(self.context.rptObj, text, url, icon, helper, height, decoration, options, profile))

  def data(self, text, value, width=(100, '%'), height=(None, 'px'), format='txt', profile=None):
    """
    Python interface to the Hyperlink to retrieve data

    Example
    data_link = rptObj.ui.links.data("link", "test#data")
    data_link.build({"text": 'new link Name', 'data': "new content"})

    :param text: The string value to be displayed in the component
    :param value:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param format: Optional. The downloaded data format
    :param profile: Optional. A flag to set the component performance storage
    """
    html_data = html.HtmlLinks.DataLink(self.context.rptObj, text, value, width=width, height=height, format=format, profile=profile)
    self.context.register(html_data)
    return html_data

  def bridge(self, text, script_name, report_name, url, jsData=None, context=None):
    """

    Example

    Documentation

    :param text:
    :param script_name:
    :param report_name:
    :param url:
    :param jsData:
    :param context:

    :rtype: html.HtmlLinks.Bridge

    :return:
    """
    return self.context.register(html.HtmlLinks.Bridge(self.context.rptObj, text, script_name, report_name, url, jsData, context))
