#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core import html
from epyk.interfaces import Arguments


class Network(object):

  def __init__(self, context):
    self.context = context

  def comments(self, htmlCode, recordSet=None, width=(100, '%'), height=(200, 'px'), profile=None, options=None):
    """
    Description:
    ------------
    Python wrapper to a div item composed to several sub html items to display message

    Usage::

      db = report.db(database="test.db")
      report.comments('Test', dbService={'db': db, 'com_table': 'comments', 'reply_table': 'replyComments', 'reply_service': 'post_reply/url', 'user_coms': 'user_comments', 'privacy': 'public', 'service': your/url})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Comments`

    Related Pages:

      https://leaverou.github.io/bubbly/
    http://manos.malihu.gr/jquery-custom-content-scroller/

    Attributes:
    ----------
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param recordSet:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {'readonly': True, 'markdown': True, 'dated': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.Comments(self.context.rptObj, recordSet, width, height, htmlCode, dflt_options, profile)

  def chat(self, htmlCode, recordSet=None, width=(100, '%'), height=(200, 'px'), profile=None, options=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Chat`

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/chat.py

    Attributes:
    ----------
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param recordSet:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {'readonly': False, 'markdown': True, 'dated': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.Chat(self.context.rptObj, recordSet, width, height, htmlCode, dflt_options, profile)

  def bot(self, htmlCode, width=(100, '%'), height=(200, 'px'), profile=None, options=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Bot`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/bot.py

    Attributes:
    ----------
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param width:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {'readonly': False, 'markdown': True, 'dated': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.Bot(self.context.rptObj, width, height, htmlCode, dflt_options, profile)

  def alert(self, type, value="", width=(320, 'px'), height=(None, None), htmlCode=None, options=None, profile=False):
    """
    Description:
    ------------
    Function to add when the python run some tags to put on the top of your report messages.

    The type of the messages can be different according to its criticallity.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    All the notification can be hidden directly from the report by setting the flag alerts = False
    e.g: rptObj.alerts = False

    Usage::

      report.ui.messaging.alert('WARNING', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/alerts.py

    Attributes:
    ----------
    :param value: The content of the notification
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"time": 1000, 'delay': 1000, 'type': type, 'close': True, 'markdown': True,
                    'classes': ['alert', 'alert-%s' % type]}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.Alert(self.context.rptObj, value, width, height, htmlCode, dflt_options, profile)

  def danger(self, value="", htmlCode=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------
    Function to add when the python run some tags to put on the top of your report messages.

    The type of the messages can be different according to its criticality.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    All the notification can be hidden directly from the report by setting the flag alerts = False
    e.g: rptObj.alerts = False

    Usage::

      rptObj.ui.messaging.alert('danger', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Attributes:
    ----------
    :param value: The content of the notification
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    return self.alert('danger', value, width, height, htmlCode, options, profile)

  def info(self, value="", htmlCode=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------
    Function to add when the python run some tags to put on the top of your report messages.
    The type of the messages can be different according to its criticallity.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    Usage::

      rptObj.ui.messaging.alert('info', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Attributes:
    ----------
    :param value: The content of the notification
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    return self.alert('info', value, width, height, htmlCode, options, profile)

  def success(self, value="", htmlCode=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------
    unction to add when the python run some tags to put on the top of your report messages.
    The type of the messages can be different according to its criticallity.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    Usage::

      rptObj.ui.messaging.alert('success', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Attributes:
    ----------
    :param value: The content of the notification
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    return self.alert('success', value, width, height, htmlCode, options, profile)

  def warning(self, value="", htmlCode=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------
    Function to add when the python run some tags to put on the top of your report messages.
    The type of the messages can be different according to its criticallity.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    Usage::

      rptObj.ui.messaging.alert('warning', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Attributes:
    ----------
    :param value: The content of the notification
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    return self.alert('warning', value, width, height, htmlCode, options, profile)

  def news(self, value="", htmlCode=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------

    Usage::

      b = rptObj.ui.button("Display")
      n = rptObj.ui.messaging.news("This is a title", "This is the content", link_script="TestSlider")
      b.click(n.jsGenerate("Updated content", isPyData=True))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.News`

    Temapltes:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/news.py

    Attributes:
    ----------
    :param value:
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"dated": True, 'markdown': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.News(self.context.rptObj, value, width, height, htmlCode, dflt_options, profile)

  def room(self, img, htmlCode=None, width=(60, 'px'), height=(60, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param img: String. The image path on the server or locally to be used
    :param htmlCode: String. Optional. The id for this component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"dated": True, 'markdown': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.Room(self.context.rptObj, img, width, height, htmlCode, dflt_options, profile)

  def dropfile(self, placeholder='Drop your files here', tooltip='Drop your files here', options=None, profile=None):
    """
    Description:
    ------------
    Add an HTML component to drop files. The files will be dropped by default to the OUTPUT folder of the defined environment.
    Files will also be recorded in the database in order to ensure that those data will not be shared.
    The data sharing is and should be defined only by the user from the UI.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlFiles.DropFile`

    Usage::

      rptObj.ui.network.dropfile()

    Related Pages:


    Attributes:
    ----------
    :param placeholder:
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    return html.HtmlNetwork.DropFile(self.context.rptObj, placeholder, tooltip, options, profile)

  def upload(self, icon=None, width=(25, 'px'), height=(25, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. The id for this component
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    if icon is None:
      icon = "fas fa-file-upload"
    file = self.context.rptObj.ui.icons.awesome(icon, width=width, height=height, htmlCode=htmlCode, profile=profile)
    return file

  def download(self, name, icon=None, path=None, width=(25, 'px'), height=(25, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param icon: String. Optional. The component icon content from font-awesome references
    :param path:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. The id for this component
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    mapped_file = {"excel": 'far fa-file-excel', 'pdf': 'far fa-file-pdf', 'code': 'far fa-file-code', 'csv': 'fas fa-file-csv',
                   'word': 'fa-file-word'}
    extension = name.split(".")[-1]
    if extension in mapped_file:
      icon = mapped_file[extension]
    if icon is None:
      icon = "fas fa-file-upload"
    file = self.context.rptObj.ui.icons.awesome(icon, width=width, height=height, htmlCode=htmlCode, profile=profile)
    file.tooltip(r"Download file: %(path)s\%(name)s" % {"path": path, "name": name})
    if path is not None:
      file.click(['''
        var link = document.createElement("a");
        link.href = 'file://localhost/%(path)s';
        link.target="_blank";
        link.setAttribute('download', '%(name)s');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        ''' % {"path": os.path.join(path, name), "name": name}])
    return file
