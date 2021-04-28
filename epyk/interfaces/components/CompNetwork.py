#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging

from epyk.core import html
from epyk.interfaces import Arguments


class Network:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def comments(self, html_code, record=None, width=(100, '%'), height=(200, 'px'), profile=None, options=None):
    """
    Description:
    ------------
    Python wrapper to a div item composed to several sub html items to display message

    Usage::

      db = page.db(database="test.db")
      page.comments('Test', dbService={'db': db, 'com_table': 'comments', 'reply_table': 'replyComments', 'reply_service': 'post_reply/url', 'user_coms': 'user_comments', 'privacy': 'public', 'service': your/url})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Comments`

    Related Pages:

      https://leaverou.github.io/bubbly/
      http://manos.malihu.gr/jquery-custom-content-scroller/

    Attributes:
    ----------
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param record: List of dict. The Python list of dictionaries.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {'readonly': True, 'markdown': True, 'dated': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.Comments(self.page, record, width, height, html_code, dflt_options, profile)

  @html.Html.css_skin()
  def chat(self, html_code, record=None, width=(100, '%'), height=(200, 'px'), profile=None, options=None):
    """
    Description:
    ------------

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Chat`

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/chat.py

    Attributes:
    ----------
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param record: List of dict. The Python list of dictionaries.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {'readonly': False, 'markdown': True, 'dated': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.Chat(self.page, record, width, height, html_code, dflt_options, profile)

  @html.Html.css_skin()
  def bot(self, html_code, width=(100, '%'), height=(200, 'px'), profile=None, options=None):
    """
    Description:
    ------------

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Bot`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/bot.py

    Attributes:
    ----------
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {'readonly': False, 'markdown': True, 'dated': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.Bot(self.page, width, height, html_code, dflt_options, profile)

  @html.Html.css_skin()
  def alert(self, type, value="", width=(320, 'px'), height=(None, None), html_code=None, options=None, profile=False):
    """
    Description:
    ------------
    Function to add when the python run some tags to put on the top of your report messages.

    The type of the messages can be different according to its criticallity.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    All the notification can be hidden directly from the report by setting the flag alerts = False
    e.g: rptObj.alerts = False

    Usage::

      page.ui.messaging.alert('WARNING', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/alerts.py

    Attributes:
    ----------
    :param type: String. The warning level.
    :param value: String. Optional. The content of the notification.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"time": 1000, 'delay': 1000, 'type': type, 'close': True, 'markdown': True,
                    'classes': ['alert', 'alert-%s' % type]}
    if options is not None:
      dflt_options.update(options)
    alert_types = ("danger", "info", "success", "warning")
    if self.page.verbose or dflt_options.get("verbose"):
      if type not in alert_types:
        logging.warning("Alert type not recognized: %s, %s " % (type, alert_types))

    return html.HtmlNetwork.Alert(self.page, value, width, height, html_code, dflt_options, profile)

  @html.Html.css_skin()
  def danger(self, value="", html_code=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------
    Function to add when the python run some tags to put on the top of your report messages.

    The type of the messages can be different according to its criticality.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    All the notification can be hidden directly from the report by setting the flag alerts = False
    e.g: rptObj.alerts = False

    Usage::

      page.ui.messaging.alert('danger', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Attributes:
    ----------
    :param value: String. Optional. The content of the notification.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.alert('danger', value, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def info(self, value="", html_code=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------
    Function to add when the python run some tags to put on the top of your report messages.
    The type of the messages can be different according to its criticallity.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    Usage::

      page.ui.messaging.alert('info', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Attributes:
    ----------
    :param value: String. Optional. The content of the notification.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.alert('info', value, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def success(self, value="", html_code=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------
    unction to add when the python run some tags to put on the top of your report messages.
    The type of the messages can be different according to its criticallity.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    Usage::

      page.ui.messaging.alert('success', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Attributes:
    ----------
    :param value: String. Optional. The content of the notification.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.alert('success', value, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def warning(self, value="", html_code=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------
    Function to add when the python run some tags to put on the top of your report messages.
    The type of the messages can be different according to its criticallity.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    Usage::

      page.ui.messaging.alert('warning', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/

    Attributes:
    ----------
    :param value: String. Optional. The content of the notification.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.alert('warning', value, width, height, html_code, options, profile)

  @html.Html.css_skin()
  def news(self, value="", html_code=None, width=(320, 'px'), height=(None, None), options=None, profile=False):
    """
    Description:
    ------------

    Usage::

      b = page.ui.button("Display")
      n = page.ui.messaging.news("This is a title", "This is the content", link_script="TestSlider")
      b.click(n.jsGenerate("Updated content", isPyData=True))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.News`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/st_news.py

    Attributes:
    ----------
    :param value: String. Optional.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"dated": True, 'markdown': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.News(self.page, value, width, height, html_code, dflt_options, profile)

  @html.Html.css_skin()
  def room(self, img, html_code=None, width=(60, 'px'), height=(60, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage::


    Attributes:
    ----------
    :param img: String. Optional. The image path on the server or locally to be used.
    :param html_code: String. Optional. The id for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"dated": True, 'markdown': True}
    if options is not None:
      dflt_options.update(options)
    return html.HtmlNetwork.Room(self.page, img, width, height, html_code, dflt_options, profile)

  @html.Html.css_skin()
  def dropfile(self, placeholder='', delimiter="TAB", width=(100, '%'), height=('auto', ''), tooltip=None,
               html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add an HTML component to drop files. The files will be dropped by default to the OUTPUT folder of the
    defined environment.

    Files will also be recorded in the database in order to ensure that those data will not be shared.
    The data sharing is and should be defined only by the user from the UI.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlFiles.DropFile`

    Usage::

      page.ui.network.dropfile()

    Related Pages:


    Attributes:
    ----------
    :param placeholder: String. Optional. The placeholder text when input empty.
    :param delimiter: String. Optional. The column delimiter.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param html_code: String. Optional. The id for this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = html.HtmlNetwork.DropFile(
      self.page, placeholder, delimiter, tooltip, width, height, html_code, options, profile)
    return component

  @html.Html.css_skin()
  def upload(self, icon=None, width=(25, 'px'), height=(25, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. The id for this component
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    if icon is None:
      icon = "fas fa-file-upload"
    file = self.page.ui.icons.awesome(
      icon, width=width, height=height, html_code=html_code, options=options, profile=profile)
    return file

  @html.Html.css_skin()
  def download(self, name, icon=None, path=None, width=(25, 'px'), height=(25, 'px'), html_code=None, options=None,
               profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param name: String. Optional.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param path: String. Optional. String. The image file path.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. The id for this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    mapped_file = {
      "excel": 'far fa-file-excel', 'pdf': 'far fa-file-pdf', 'code': 'far fa-file-code', 'csv': 'fas fa-file-csv',
      'word': 'fa-file-word'}
    extension = name.split(".")[-1]
    if extension in mapped_file:
      icon = mapped_file[extension]
    if icon is None:
      icon = "fas fa-file-upload"
    file = self.page.ui.icons.awesome(
      icon, width=width, height=height, html_code=html_code, options=options, profile=profile)
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

  @html.Html.css_skin()
  def assistant(self, image, name="", path=None, html_code=None, size=(50, 'px'), profile=None, options=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param image:
    :param name:
    :param path:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param size: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    dflt_options = {'readonly': False, 'markdown': True, 'dated': True}
    if options is not None:
      dflt_options.update(options)
    image = self.page.ui.images.avatar(image, path=path, width=size, height=size, align='left')
    image.options.managed = False
    container = html.HtmlNetwork.Assistant(image, name, self.page, html_code, dflt_options, profile)
    container.style.css.position = 'fixed'
    container.style.css.bottom = 0
    container.style.css.right = 0
    container.style.css.z_index = 200
    return container
