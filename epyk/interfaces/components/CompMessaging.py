from epyk.core import html


class Messaging(object):
  """

  """

  def __init__(self, context):
    self.context = context

  def comments(self, htmlCode, recordset=None, title="", pmts=None, dbService=None, width=(100, '%'),
               height=(200, 'px'), httpCodes=None, readonly=False, profile=None):
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
    :param htmlCode:
    :param recordset:
    :param title:
    :param pmts:
    :param dbService:
    :param width:
    :param height:
    :param httpCodes:
    :param readonly:
    :param profile:
    :return:
    """
    if recordset is None:
      recordset = []
    return self.context.register(html.HtmlMessaging.Comments(self.context.rptObj, htmlCode, recordset, title, pmts,
                                                             dbService, width, height, httpCodes, readonly, profile))

  def chat(self, htmlCode, title="", pmts=None, dbService=None, width=(100, '%'),
               height=(200, 'px'), httpCodes=None, readonly=False, profile=None, chatOptions=None):
    """

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Chat`

    :param htmlCode:
    :param title:
    :param pmts:
    :param dbService:
    :param width:
    :param height:
    :param httpCodes:
    :param readonly:
    :param profile:
    :param chatOptions:
    :return:
    """
    return self.context.register(html.HtmlMessaging.Chat(self.context.rptObj, htmlCode, title, pmts, dbService, width,
                                                         height, httpCodes, readonly, profile, chatOptions))

  def bot(self, htmlCode, name="Roxane", pmts=None, dbService=None, width=(250, 'px'),
               height=(200, 'px'), httpCodes=None, profile=None, botOptions=None):
    """

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Bot`

    :param htmlCode:
    :param name:
    :param pmts:
    :param dbService:
    :param width:
    :param height:
    :param httpCodes:
    :param profile:
    :param botOptions:
    :return:
    """
    return self.context.register(html.HtmlMessaging.Bot(self.context.rptObj, htmlCode, name, pmts, dbService, width,
                                                        height, httpCodes, profile, botOptions))

  def alert(self, category, title, value, htmlCode=None, background_color=None, close_button=True, width=(320, 'px'),
             height=(None, None), color='black', profile=False, dataSrc=None):
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

    Attributes:

    :param title: The title of the notification
    :param value: The content of the notification
    :param category:
    :param htmlCode:
    :param background_color: Optional. The background color. Can be also overridden from the .css function
    :param close_button: Optional. Boolean, add a close button to the notification
    :param width:
    :param height:
    :param color:
    :param profile:
    :param dataSrc:
    :rtype: html.HtmlMessaging.Alert
    """
    if not getattr(self.context.rptObj, "alerts", True):
      return

    ui_prop = self.context.rptObj._props.setdefault("ui", {})
    ui_prop.setdefault("notifications", {})["count"] = ui_prop.get("notifications", {}).get("count", 0) + 1
    return self.context.register(html.HtmlMessaging.Alert(self.context.rptObj, title, value, category, width,
                  height, close_button, background_color, color, htmlCode, dataSrc, profile))


  def danger(self, title, value, htmlCode=None, close_button=True, width=(320, 'px'),
             height=(None, None), color='black', profile=False, dataSrc=None):
    """

    Description:
    ------------Function to add when the python run some tags to put on the top of your report messages.

    The type of the messages can be different according to its criticallity.
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
    :param title: The title of the notification
    :param value: The content of the notification
    :param htmlCode:
    :param close_button: Optional. Boolean, add a close button to the notification
    :param width:
    :param height:
    :param color:
    :param profile:
    :param dataSrc:
    :rtype: html.HtmlMessaging.Alert
    """
    if not getattr(self.context.rptObj, "alerts", True):
      return

    ui_prop = self.context.rptObj._props.setdefault("ui", {})
    ui_prop.setdefault("notifications", {})["count"] = ui_prop.get("notifications", {}).get("count", 0) + 1
    return self.context.register(html.HtmlMessaging.Alert(self.context.rptObj, title, value, 'danger', width,
                  height, close_button, self.context.rptObj.getColor('danger', 0), color, htmlCode, dataSrc, profile))

  def info(self, title, value, htmlCode=None, close_button=True, width=(320, 'px'),
           height=(None, None), color='black', profile=False, dataSrc=None):
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
    :rtype: html.HtmlMessaging.Alert
    """
    if not getattr(self.context.rptObj, "alerts", True):
      return

    ui_prop = self.context.rptObj._props.setdefault("ui", {})
    ui_prop.setdefault("notifications", {})["count"] = ui_prop.get("notifications", {}).get("count", 0) + 1
    return self.context.register(html.HtmlMessaging.Alert(self.context.rptObj, title, value, 'info', width,
                  height, close_button, self.context.rptObj.getColor('info', 0), color, htmlCode, dataSrc, profile))

  def success(self, title, value, htmlCode=None, close_button=True, width=(320, 'px'), height=(None, 'black'),
              color='black', profile=False, dataSrc=None):
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

    :param title:
    :param value:
    :param htmlCode:
    :param close_button:
    :param width:
    :param height:
    :param color:
    :param profile:
    :param dataSrc:
    """
    if not getattr(self.context.rptObj, "alerts", True):
      return

    ui_prop = self.context.rptObj._props.setdefault("ui", {})
    ui_prop.setdefault("notifications", {})["count"] = ui_prop.get("notifications", {}).get("count", 0) + 1
    return self.context.register(html.HtmlMessaging.Alert(self.context.rptObj, title, value, 'success', width,
                                                          height, close_button,
                                                          self.context.rptObj.getColor('success', 0), color, htmlCode,
                                                          dataSrc, profile))

  def warning(self, title, value, htmlCode=None, close_button=True, width=(320, 'px'), height=(None, None),
              color='black', profile=False, dataSrc=None):
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

    :param title:
    :param value:
    :param htmlCode:
    :param close_button:
    :param width:
    :param height:
    :param color:
    :param profile:
    :param dataSrc:

    """
    if not getattr(self.context.rptObj, "alerts", True):
      return

    ui_prop = self.context.rptObj._props.setdefault("ui", {})
    ui_prop.setdefault("notifications", {})["count"] = ui_prop.get("notifications", {}).get("count", 0) + 1
    return self.context.register(html.HtmlMessaging.Alert(self.context.rptObj, title, value, 'warning', width,
                  height, close_button, self.context.rptObj.getColor('warning', 0), color, htmlCode, dataSrc, profile))

  def news(self, title, value, label=None, link_script=None, icon=None, htmlCode=None, width=(320, 'px'), height=(None, None),
           profile=False):
    """
    Description:
    ------------

    Usage::

      b = rptObj.ui.button("Display")
      n = rptObj.ui.messaging.news("This is a title", "This is the content", link_script="TestSlider")
      b.click(n.jsGenerate("Updated content", isPyData=True))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.News`

    Attributes:
    ----------
    :param title:
    :param value:
    :param label:
    :param link_script:
    :param icon:
    :param htmlCode:
    :param width:
    :param height:
    :param profile:
    """
    return self.context.register(html.HtmlMessaging.News(self.context.rptObj, title, value, label, link_script, icon, width,
                                                          height, htmlCode, profile))
