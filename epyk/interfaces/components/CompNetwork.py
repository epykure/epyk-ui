#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging

from typing import Union

from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.css import Defaults as Defaults_css


class Network:

  def __init__(self, ui):
    self.page = ui.page

  def comments(self, html_code, record=None, width: Union[tuple, int] = (100, '%'),
               height: Union[tuple, int] = (200, 'px'), profile: Union[dict, bool] = None, options: dict = None):
    """
    Description:
    ------------
    Python wrapper to a div item composed to several sub html items to display message

    Usage::

      db = page.db(database="test.db")
      page.comments('Test', dbService={'db': db, 'com_table': 'comments', 'reply_table': 'replyComments',
        'reply_service': 'post_reply/url', 'user_coms': 'user_comments', 'privacy': 'public', 'service': your/url})

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
    component = html.HtmlNetwork.Comments(self.page, record, width, height, html_code, dflt_options, profile)
    html.Html.set_component_skin(component)
    return component

  def chat(self, html_code, record=None, width: Union[tuple, int] = (100, '%'),
           height: Union[tuple, int] = (200, 'px'), profile=None, options=None):
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
    dfl_options = {'readonly': False, 'markdown': True, 'dated': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlNetwork.Chat(self.page, record, width, height, html_code, dfl_options, profile)
    html.Html.set_component_skin(component)
    return component

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
    dfl_options = {'readonly': False, 'markdown': True, 'dated': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlNetwork.Bot(self.page, width, height, html_code, dfl_options, profile)
    html.Html.set_component_skin(component)
    return component

  def alert(self, type, value="", width: Union[tuple, int] = (320, 'px'), height: Union[tuple, int] = (None, None),
            html_code: str = None, options: dict = None, profile=False):
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
    component = html.HtmlNetwork.Alert(self.page, value, width, height, html_code, dflt_options, profile)
    html.Html.set_component_skin(component)
    return component

  def danger(self, value="", html_code: str = None, width: Union[tuple, int] = (320, 'px'),
             height: Union[tuple, int] = (None, None), options=None, profile=False):
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
    component = self.alert('danger', value, width, height, html_code, options, profile)
    html.Html.set_component_skin(component)
    return component

  def info(self, value: str = "", html_code: str = None, width: Union[tuple, int] = (320, 'px'),
           height: Union[tuple, int] = (None, None), options: dict = None, profile: Union[bool, dict] = False):
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
    component = self.alert('info', value, width, height, html_code, options, profile)
    html.Html.set_component_skin(component)
    return component

  def success(self, value: str = "", html_code: str = None, width: Union[tuple, int] = (320, 'px'),
              height: Union[tuple, int] = (None, None), options: dict = None, profile: Union[dict, bool] = False):
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
    component = self.alert('success', value, width, height, html_code, options, profile)
    html.Html.set_component_skin(component)
    return component

  def warning(self, value: str = "", html_code: str = None, width: Union[tuple, int] = (320, 'px'),
              height: Union[tuple, int] = (None, None), options: dict = None, profile: Union[dict, bool] = False):
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
    component = self.alert('warning', value, width, height, html_code, options, profile)
    html.Html.set_component_skin(component)
    return component

  def news(self, value: str = "", html_code: str = None, width: Union[tuple, int] = (320, 'px'),
           height: Union[tuple, int] = (None, None), options: dict = None, profile: Union[dict, bool] = False):
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
    dfl_options = {"dated": True, 'markdown': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlNetwork.News(self.page, value, width, height, html_code, dfl_options, profile)
    html.Html.set_component_skin(component)
    return component

  def room(self, img: str, html_code: str = None, width: Union[tuple, int] = (60, 'px'),
           height: Union[tuple, int] = (60, 'px'), options: dict = None, profile: Union[dict, bool] = False):
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
    dfl_options = {"dated": True, 'markdown': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlNetwork.Room(self.page, img, width, height, html_code, dfl_options, profile)
    html.Html.set_component_skin(component)
    return component

  def dropfile(self, placeholder: str = '', delimiter: str = "TAB", width: Union[tuple, int] = (100, '%'),
               height: Union[tuple, int] = ('auto', ''), tooltip: str = None,
               html_code: str = None, options: dict = None, profile: Union[dict, bool] = None):
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
    html.Html.set_component_skin(component)
    return component

  def upload(self, icon: str = None, width: Union[tuple, int] = (25, 'px'), height: Union[tuple, int] = (25, 'px'),
             html_code: str = None, options: dict = None, profile: Union[dict, bool] = None):
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
    file = self.page.ui.icons.awesome(
      icon, width=width, height=height, html_code=html_code, options=options, profile=profile)
    html.Html.set_component_skin(file)
    return file

  def download(self, name: str, icon: str = None, path: str = None, width: Union[tuple, int] = (25, 'px'),
               height: Union[tuple, int] = (25, 'px'), html_code: str = None, options: dict = None,
               profile: Union[dict, bool] = None):
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
    options = options or {}
    mapped_file = {
      "excel": Defaults_css.get_icon("excel"), 'pdf': Defaults_css.get_icon("pdf"), 'code':
      Defaults_css.get_icon("code"), 'csv': Defaults_css.get_icon("csv"), 'word': Defaults_css.get_icon("word")}
    extension = name.split(".")[-1]
    if extension in mapped_file:
      icon = mapped_file[extension]["icon"]
      options["icon_family"] = mapped_file[extension]["icon_family"]
    if icon is None:
      icon = Defaults_css.get_icon("upload")["icon"]
      options["icon_family"] = Defaults_css.get_icon("upload")["icon_family"]
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
    html.Html.set_component_skin(file)
    return file

  def assistant(self, image, name: str = "", path: str = None, html_code: str = None,
                size: Union[tuple, int] = (50, 'px'), profile: Union[dict, bool] = None, options: dict = None):
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
    dfl_options = {'readonly': False, 'markdown': True, 'dated': True}
    if options is not None:
      dfl_options.update(options)
    image = self.page.ui.images.avatar(image, path=path, width=size, height=size, align='left')
    image.options.managed = False
    container = html.HtmlNetwork.Assistant(image, name, self.page, html_code, dfl_options, profile)
    container.style.css.position = 'fixed'
    container.style.css.bottom = 0
    container.style.css.right = 0
    container.style.css.z_index = 200
    html.Html.set_component_skin(container)
    return container

  def logs(self, records=None, width=(100, "%"), height=("auto", ""), options: dict = None, html_code: str = None,
           profile: Union[bool, dict] = None, helper: str = None):
    component = self.page.ui.lists.items(records, width, height, options, html_code, profile, helper)
    component.options.items_type = "logs"
    html.Html.set_component_skin(component)
    return component
