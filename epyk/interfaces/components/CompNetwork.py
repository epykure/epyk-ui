#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging

from typing import Union, List
from epyk.core.py import types
from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.css import Defaults as Defaults_css


class Network:

    def __init__(self, ui):
        self.page = ui.page

    def comments(self, html_code: str = None, record: List[dict] = None, width: types.SIZE_TYPE = (100, '%'),
                 height: types.SIZE_TYPE = (200, 'px'), profile: types.PROFILE_TYPE = None,
                 options: dict = None) -> html.HtmlNetwork.Comments:
        """Python wrapper to a div item composed to several sub html items to display message

        Usage::

          db = page.db(database="test.db")
          page.comments('Test', dbService={'db': db, 'com_table': 'comments', 'reply_table': 'replyComments',
            'reply_service': 'post_reply/url', 'user_coms': 'user_comments', 'privacy': 'public', 'service': your/url})

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlMessaging.Comments`

        Related Pages:

          https://leaverou.github.io/bubbly/
          http://manos.malihu.gr/jquery-custom-content-scroller/

        :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
        :param record: Optional. The Python list of dictionaries.
        :param width: Optional. A tuple with the integer for the component width and its unit.
        :param height: Optional. A tuple with the integer for the component height and its unit.
        :param profile: Optional. A flag to set the component performance storage.
        :param options: Optional. Specific Python options available for this component.
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dflt_options = {'readonly': True, 'markdown': True, 'dated': True}
        if options is not None:
            dflt_options.update(options)
        component = html.HtmlNetwork.Comments(self.page, record, width, height, html_code, dflt_options, profile)
        html.Html.set_component_skin(component)
        return component

    def chat(self, html_code: str = None, record: List[dict] = None, width: types.SIZE_TYPE = (100, '%'),
             height: types.SIZE_TYPE = (200, 'px'), profile: types.PROFILE_TYPE = None,
             options: dict = None) -> html.HtmlNetwork.Chat:
        """

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlMessaging.Chat`

        Templates:

            https://github.com/epykure/epyk-templates/blob/master/locals/components/chat.py

        :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
        :param record: Optional. The Python list of dictionaries.
        :param width: Optional. A tuple with the integer for the component width and its unit.
        :param height: Optional. A tuple with the integer for the component height and its unit.
        :param profile: Optional. A flag to set the component performance storage.
        :param options: Optional. Specific Python options available for this component.
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {'readonly': False, 'markdown': True, 'dated': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlNetwork.Chat(self.page, record, width, height, html_code, dfl_options, profile)
        html.Html.set_component_skin(component)
        return component

    def bot(self, html_code: str, width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (200, 'px'),
            profile: types.PROFILE_TYPE = None, options: dict = None) -> html.HtmlNetwork.Bot:
        """

        Usage::

          container = page.ui.network.bot(html_code='bot_service')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlMessaging.Bot`

        Templates:

          https://github.com/epykure/epyk-templates/blob/master/locals/components/bot.py

        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param profile: Optional. A flag to set the component performance storage
        :param options: Optional. Specific Python options available for this component
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {'readonly': False, 'markdown': True, 'dated': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlNetwork.Bot(self.page, width, height, html_code, dfl_options, profile)
        html.Html.set_component_skin(component)
        return component

    def alert(self, category: str, value: str = "", width: types.SIZE_TYPE = (320, 'px'),
              height: types.SIZE_TYPE = (None, None), html_code: str = None, options: dict = None,
              profile: types.PROFILE_TYPE = False) -> html.HtmlNetwork.Alert:
        """Function to add when the python run some tags to put on the top of your report messages.

        The type of the messages can be different according to its criticality.
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

        :param category: The warning level
        :param value: Optional. The content of the notification
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        dflt_options = {"time": 1000, 'delay': 1000, 'type': category, 'close': True, 'markdown': True,
                        'classes': ['alert', 'alert-%s' % category]}
        if options is not None:
            dflt_options.update(options)
        alert_types = ("danger", "info", "success", "warning")
        if self.page.verbose or dflt_options.get("verbose"):
            if category not in alert_types:
                logging.warning("Alert type not recognized: %s, %s " % (category, alert_types))
        component = html.HtmlNetwork.Alert(self.page, value, width, height, html_code, dflt_options, profile)
        html.Html.set_component_skin(component)
        return component

    def danger(self, value: str = "", html_code: str = None, width: types.SIZE_TYPE = (320, 'px'),
               height: types.SIZE_TYPE = (None, None), options: dict = None,
               profile: types.PROFILE_TYPE = False) -> html.HtmlNetwork.Alert:
        """Function to add when the python run some tags to put on the top of your report messages.

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
 
    :param value: Optional. The content of the notification
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
        component = self.alert('danger', value, width, height, html_code, options, profile)
        html.Html.set_component_skin(component)
        return component

    def info(self, value: str = "", html_code: str = None, width: types.SIZE_TYPE = (320, 'px'),
             height: types.SIZE_TYPE = (None, None), options: dict = None,
             profile: types.PROFILE_TYPE = False) -> html.HtmlNetwork.Alert:
        """Function to add when the python run some tags to put on the top of your report messages.
    The type of the messages can be different according to its criticallity.
    This is fully defined and #driven in the Python and visible in the browser when the page is ready

    Usage::

      page.ui.messaging.alert('info', 'Server URL not recognized', 'Please check')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMessaging.Alert`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/alerts/
 
    :param value: Optional. The content of the notification.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
        component = self.alert('info', value, width, height, html_code, options, profile)
        html.Html.set_component_skin(component)
        return component

    def success(self, value: str = "", html_code: str = None, width: types.SIZE_TYPE = (320, 'px'),
                height: types.SIZE_TYPE = (None, None), options: dict = None,
                profile: types.PROFILE_TYPE = False) -> html.HtmlNetwork.Alert:
        """Function to add when the python run some tags to put on the top of your report messages
        The type of the messages can be different according to its criticality
        This is fully defined and #driven in the Python and visible in the browser when the page is ready

        Usage::

          page.ui.messaging.alert('success', 'Server URL not recognized', 'Please check')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlMessaging.Alert`

        Related Pages:

          https://getbootstrap.com/docs/4.0/components/alerts/

        :param value: Optional. The content of the notification
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        component = self.alert('success', value, width, height, html_code, options, profile)
        html.Html.set_component_skin(component)
        return component

    def warning(self, value: str = "", html_code: str = None, width: types.SIZE_TYPE = (320, 'px'),
                height: types.SIZE_TYPE = (None, None), options: dict = None,
                profile: types.PROFILE_TYPE = False) -> html.HtmlNetwork.Alert:
        """Function to add when the python run some tags to put on the top of your report messages.
        The type of the messages can be different according to its criticality.
        This is fully defined and #driven in the Python and visible in the browser when the page is ready

        Usage::

          page.ui.messaging.alert('warning', 'Server URL not recognized', 'Please check')

          danger = page.ui.network.warning()
          danger.options.time = None
          danger.options.close = True

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlMessaging.Alert`

        Related Pages:

          https://getbootstrap.com/docs/4.0/components/alerts/

        :param value: Optional. The content of the notification
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        component = self.alert('warning', value, width, height, html_code, options, profile)
        html.Html.set_component_skin(component)
        return component

    def news(self, value: str = "", html_code: str = None, width: types.SIZE_TYPE = (320, 'px'),
             height: types.SIZE_TYPE = (None, None), options: dict = None,
             profile: types.PROFILE_TYPE = False) -> html.HtmlNetwork.News:
        """

        Usage::

          b = page.ui.button("Display")
          n = page.ui.messaging.news("This is a title", "This is the content", link_script="TestSlider")
          b.click(n.jsGenerate("Updated content", isPyData=True))

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlMessaging.News`

        Templates:

          https://github.com/epykure/epyk-templates/blob/master/locals/components/st_news.py

        :param value: Optional.
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        dfl_options = {"dated": True, 'markdown': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlNetwork.News(self.page, value, width, height, html_code, dfl_options, profile)
        html.Html.set_component_skin(component)
        return component

    def room(self, img: str, html_code: str = None, width: types.SIZE_TYPE = (60, 'px'),
             height: types.SIZE_TYPE = (60, 'px'), options: dict = None,
             profile: types.PROFILE_TYPE = False) -> html.HtmlNetwork.Room:
        """

        Usage::


        :param img: Optional. The image path on the server or locally to be used
        :param html_code: Optional. The id for this component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        dfl_options = {"dated": True, 'markdown': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlNetwork.Room(self.page, img, width, height, html_code, dfl_options, profile)
        html.Html.set_component_skin(component)
        return component

    def dropfile(self, placeholder: str = '', delimiter: str = "TAB", width: types.SIZE_TYPE = (100, '%'),
                 height: types.SIZE_TYPE = ('auto', ''), tooltip: str = None,
                 html_code: str = None, options: dict = None,
                 profile: types.PROFILE_TYPE = None) -> html.HtmlNetwork.DropFile:
        """Add an HTML component to drop files. The files will be dropped by default to the OUTPUT folder of the
        defined environment.

        Files will also be recorded in the database in order to ensure that those data will not be shared.
        The data sharing is and should be defined only by the user from the UI.

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlFiles.DropFile`

        Usage::

          page.ui.network.dropfile()

        :param placeholder: Optional. The placeholder text when input empty
        :param delimiter: Optional. The column delimiter
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param tooltip: Optional. A string with the value of the tooltip
        :param html_code: Optional. The id for this component
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        component = html.HtmlNetwork.DropFile(
            self.page, placeholder, delimiter, tooltip, width, height, html_code, options, profile)
        html.Html.set_component_skin(component)
        return component

    def upload(self, icon: str = None, width: types.SIZE_TYPE = (25, 'px'), height: types.SIZE_TYPE = (25, 'px'),
               html_code: str = None, options: dict = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlButton.IconEdit:
        """

        :param icon: Optional. The component icon content from font-awesome references
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. The id for this component
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        file = self.page.ui.icons.awesome(
            icon, width=width, height=height, html_code=html_code, options=options, profile=profile)
        html.Html.set_component_skin(file)
        return file

    def download(self, name: str, icon: str = None, path: str = None, width: types.SIZE_TYPE = (25, 'px'),
                 height: types.SIZE_TYPE = (25, 'px'), html_code: str = None, options: dict = None,
                 profile: types.PROFILE_TYPE = None) -> html.HtmlButton.IconEdit:
        """

        :param name: Optional.
        :param icon: Optional. The component icon content from font-awesome references
        :param path: Optional. String. The image file path
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. The id for this component
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        options = options or {}
        mapped_file = {
            "excel": self.page.icons.get("excel"), 'pdf': self.page.icons.get("pdf"), 'code':
                self.page.icons.get("code"), 'csv': self.page.icons.get("csv"), 'word': self.page.icons.get("word")}
        extension = name.split(".")[-1]
        if extension in mapped_file:
            icon = mapped_file[extension]["icon"]
            options["icon_family"] = mapped_file[extension]["icon_family"]
        if icon is None:
            icon = self.page.icons.get("upload")["icon"]
            options["icon_family"] = self.page.icons.get("upload")["icon_family"]
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
                  size: types.SIZE_TYPE = (50, 'px'), profile: types.PROFILE_TYPE = None,
                  options: dict = None) -> html.HtmlNetwork.Assistant:
        """


        :param image:
        :param name:
        :param path:
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param size: Optional. A tuple with the integer for the component width and its unit
        :param profile: Optional. A flag to set the component performance storage
        :param options: Optional. Specific Python options available for this component
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

    def logs(self, records: List[dict] = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = ("auto", ""), options: dict = None, html_code: str = None,
             profile: types.PROFILE_TYPE = None, helper: str = None) -> html.HtmlList.Items:
        component = self.page.ui.lists.items(records, width, height, options, html_code, profile, helper)
        component.options.items_type = "logs"
        html.Html.set_component_skin(component)
        return component

    def timeline(self, records: List[dict] = None, width: types.SIZE_TYPE = (100, "%"),
                 height: types.SIZE_TYPE = ("auto", ""), options: dict = None, html_code: str = None,
                 profile: types.PROFILE_TYPE = None, helper: str = None) -> html.HtmlList.Items:
        component = self.page.ui.lists.items(records, width, height, options, html_code, profile, helper)
        component.options.items_type = "timeline"
        html.Html.set_component_skin(component)
        return component

    def impression(self, number: int = 0, icon: str = "fas fa-chart-bar", options: dict = None, html_code: str = None,
                   profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
        """Add an impression component. This is designed to use the viewport function to increment the value,

        Usage::

          page.ui.network.impression()

        :param number: Optional. The initial value
        :param icon: Optional. The icon text
        :param options: Optional. The number component options
        :param html_code: Optional. The code used on the JavaScript side
        :param profile: Optional. The profiling options
        """
        component_icon = self.page.ui.icons.awesome(
            icon, html_code="%s_icon" % html_code if html_code is not None else html_code, options=options,
            profile=profile)
        component_icon.icon.style.css.font_factor(2)
        text = self.page.ui.numbers.number(
            number, width="auto", html_code=html_code, options=options, profile=profile)
        text.style.css.inline()
        text.style.css.user_select = "None"
        text.style.css.font_factor(0)
        container = self.page.ui.div([component_icon, text])
        container.viewport([text.dom.add(1)])
        container.icon = component_icon.icon
        container.number = text
        return container

    def votes(self, number: int = 0, options: dict = None, html_code: str = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
        """Add a vote component with two arrows and a number.

        Usage::

          vote = page.ui.network.votes()
          vote.up.style.css.cursor = "pointer"
          vote.up.click(vote.number.dom.add(1))
          vote.down.click(vote.number.dom.add(-1))

        :param number: Optional. The initial value
        :param options: Optional. The number component options
        :param html_code: Optional. The code used on the JavaScript side
        :param profile: Optional. The profiling options
        """
        icon_up = self.page.ui.div("&#8679;", width="auto")
        icon_up.style.css.user_select = "None"
        icon_up.style.css.inline()
        icon_up.style.css.font_factor(6)
        icon_down = self.page.ui.div("&#8681;", width="auto")
        icon_down.style.css.user_select = "None"
        icon_down.style.css.inline()
        icon_down.style.css.font_factor(6)
        text = self.page.ui.numbers.number(
            number, width=(20, "px"), align="center", html_code=html_code, options=options, profile=profile)
        text.style.css.inline()
        text.style.css.user_select = "None"
        text.style.css.font_factor(0)
        container = self.page.ui.div([icon_up, text, icon_down])
        container.up = icon_up
        container.down = icon_down
        container.number = text
        return container
