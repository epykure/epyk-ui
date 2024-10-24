#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import Optional
from pathlib import Path
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.html.options import OptNet

from epyk.core.js.objects import JsComponents
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlNetwork

# The list of CSS classes
from epyk.core.css.styles import GrpClsNetwork


class Comments(Html.Html):
    name = 'Comments'
    tag = "div"
    _option_cls = OptNet.OptionsComments

    style_urls = [
        Path(__file__).parent.parent / "css" / "native" / "html-comments.css",
    ]

    style_refs = {
        "html-comments": "html-comments",
        "html-comments-counter": "html-comments-counter",
        "html-comments-input": "html-comments-input",
        "html-comments-icon": "html-comments-icon",
        "html-comments-content": "html-comments-content",
        "html-comments-timestamp": "html-comments-timestamp",
        "html-comments-feed": "html-comments-feed",
    }

    def __init__(self, page: primitives.PageModel, record, width, height, html_code, options, profile):
        super(Comments, self).__init__(page, record, css_attrs={"width": width, 'height': height}, html_code=html_code,
                                       profile=profile, options=options)
        self.classList.add(self.style_refs["html-comments"])
        self.input, self.icon = None, None
        self.counter = page.ui.texts.span("0", width=(None, 'px'), html_code=self.sub_html_code("counter"))
        self.counter.style.clear_all(no_default = True, keep_html_class = False)
        self.counter.options.managed = False
        self.counter.attr["name"] = "count"
        self.counter.classList.add(self.style_refs["html-comments-counter"])
        self.actions = []
        if not self.options.readonly:
            self.input = page.ui.input(html_code=self.sub_html_code("input"), width=None)
            self.input.options.managed = False
            self.input.classList.add(self.style_refs["html-comments-input"])
            if "background" in options:
                self.input.style.css.background = options["background"]

    @classmethod
    def get_requirements(cls, page: primitives.PageModel, options: types.OPTION_TYPE = None) -> tuple:
        """Update requirements with the defined Icons' family.

        :param page: Page context
        :param options: Component input options
        """
        if options and options.get('icon_family') is not None:
            return (options['icon_family'],)

        return (page.icons.family,)

    @property
    def options(self) -> OptNet.OptionsComments:
        """Property to the comments component options.
        Optional can either impact the Python side or the Javascript builder.

        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def js(self) -> JsComponents.Chat:
        """The Javascript functions defined for this component.
        Those can be specific ones for the module or generic ones from the language.

        :return: A Javascript Dom object
        """
        if self._js is None:
            self._js = JsComponents.Chat(self, page=self.page)
        return self._js

    def add(self, text: str, time: str = None, time_format: str = "%Y-%m-%d %H:%M:%S", **kwargs):
        """Add a text message.

        :param text: The text message
        :param time: Optional. the timestamp
        :param time_format: Optional. Time format. Default %Y-%m-%d %H:%M:%S
        """
        if time is None:
            time = datetime.now().strftime(time_format)
        self.val.append({"text": text, "time": time})
        return self

    def enter(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
              source_event: Optional[str] = None, on_ready: bool = False):
        """Define the function when the user press enter.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if self.options.readonly:
            self.options.readonly = False
            if not self.input:
                self.input = self.page.ui.input(html_code=self.sub_html_code("input"))
                self.input.options.managed = False
                self.input.style.css.text_align = 'left'
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs] if js_funcs is not None else []
        self.input.enter(js_funcs + [
            self.js.add(self.input.dom.content),
            self.input.dom.empty()], profile, source_event, on_ready)
        return self

    def send(self, socket, channel=None, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None):
        """

        :param socket:
        :param channel:
        :param js_funcs: Optional. The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if self.options.readonly:
            self.options.readonly = False
            self.input = self.page.ui.input()
            self.input.options.managed = False
            self.input.style.css.text_align = 'left'
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.input.enter(js_funcs + [
            socket.emit(channel or 'message', self.input.dom.content),
            self.input.dom.empty()], profile=profile)
        return self

    def subscribe(self, socket, channel, data=None, options=None, js_funcs: types.JS_FUNCS_TYPES = None,
                  profile: types.PROFILE_TYPE = None):
        """Subscribe to a socket channel. Data received from the socket are defined as a dictionary with a field data.
        The content of data will be used by this component.

        :param socket: Socket. A python socket object
        :param channel: The channel on which events will be received
        :param data:
        :param options:
        :param js_funcs:
        :param profile:
        """
        if data is None:
            data = socket.message
        js_funcs = js_funcs if js_funcs is not None else []
        socket.on(channel, [self.js.add(data)] + js_funcs, profile=profile)
        return self

    def sort(self, icon: str = "fas fa-sort-amount-up", title: str = "Sort by", options: dict = None):
        """Display a sorting feature for comment to the title.

        :param icon: Icon alias
        :param title: Label
        :param options: Settings for the component
        """
        if options and options.get('icon_family') is not None:
            family = options.get('icon_family')
        else:
            family = self.page.icons.family
        self.options.sort_label = title
        self.icon = self.page.ui.images.icon(icon, html_code=self.sub_html_code("icon"), family=family, options=options)
        return self.icon

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        comment_content = self.style_refs["html-comments-content"]
        comment_icon = self.style_refs["html-comments-icon"]
        try:
            height = "%spx" % (int(self.css("height")[:-2]) - 70)
        except:
            height = "auto"
        icon_content = ""
        if self.icon:
            icon_content = self.icon.html()
        actions_html = []
        for action in self.actions:
            if hasattr(action, "html"):
                action.options.managed = False
                actions_html.append(action.html())
            else:
                actions_html.append(action)
        return '''
<%(tag)s %(attr)s>
    <label class="html-comments-label">
        <span>%(counter)s %(title)s %(icon)s%(sort)s</span>
        %(actions)s
        %(inputTag)s
    </label>
<div class='%(content)s' style="height:%(height)s">
  <div name="comms"></div>
</div></%(tag)s>''' % {
            'attr': self.get_attrs(css_class_names=self.style.get_classes()), "counter": self.counter.html(),
            'height': height, 'inputTag': '' if self.input is None else self.input.html(),
            "tag": self.tag, "title": self.options.title, "icon": icon_content, "actions": "".join(actions_html),
            "sort": self.options.sort_label, "content": comment_content, "icon_style": comment_icon}


class Bot(Html.Html):
    """

    Three main states for the bot:
      - Message
      - Question
      - Advice / Information

    """
    name = 'Bot'

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        super(Bot, self).__init__(page, [], css_attrs={"width": width}, html_code=html_code, profile=profile)
        self.css({"text-align": 'right', "position": 'fixed', "bottom": 0, 'margin': '10px', "height": "80px",
                  "padding": "5px", "z-index": 200})

    @property
    def style(self) -> GrpClsNetwork.ClassNetworkBot:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsNetwork.ClassNetworkBot(self)
        return self._styleObj

    def __str__(self):
        return '''
       <div %(attr)s>
          <div class="speech-bubble-ds">
            <p>Hello, I am Roxanne. How can I help you!</p>
            <div class="speech-bubble-ds__arrow"></div>
          </div>
          <div style="background-repeat:no-repeat;height:80px;width:80px;display:inline-block;background-image:url('')">&nbsp;</div>
       </div>''' % {'attr': self.get_attrs(), "name": 'Test'}


class Assistant(Html.Html):
    name = 'Assistant'
    tag = "div"

    def __init__(self, component: Html.Html, title, page: primitives.PageModel, html_code, options, profile):
        super(Assistant, self).__init__(page, component, html_code=html_code, profile=profile)
        self.css({'margin': '0 10px', "padding": "0 5px", 'text-align': 'center'})
        self.name = page.ui.text(title, align="center")
        self.name.options.managed = False
        self.name.style.css.bold()
        self.mail = page.ui.icon("fas fa-at")
        self.mail.options.managed = False
        self.mail.style.add_classes.div.color_hover()
        self.mail.style.css.margin_right = 2
        self.mail.style.css.background = 'white'
        self.mail.style.css.padding = "2px 2px"
        self.mail.style.css.border_radius = 20
        self.mail.style.css.margin_top = -20
        self.chat = page.ui.icon("far fa-comments")
        self.chat.options.managed = False
        self.chat.style.add_classes.div.color_hover()
        self.chat.style.css.margin_left = 2
        self.chat.style.css.background = 'white'
        self.chat.style.css.padding = "2px 2px"
        self.chat.style.css.border_radius = 20
        self.chat.style.css.margin_top = -20

    def __str__(self):
        return '''<%(tag)s %(attr)s>%(name)s%(avatar)s%(mail)s%(chat)s</%(tag)s>''' % {
            'attr': self.get_attrs(), 'avatar': self.val.html(), 'mail': self.mail.html(), 'chat': self.chat.html(),
            'name': self.name.html(), "tag": self.tag}


class Chat(Html.Html):
    name = 'Chat'
    _option_cls = OptNet.OptionsChat

    def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
        super(Chat, self).__init__(page, records, css_attrs={"width": width, 'height': height},
                                   html_code=html_code, profile=profile, options=options)
        self.css({'padding': '5px'})
        self.input = None
        self.counter = page.ui.texts.span("0", width=(None, 'px'))
        self.counter.options.managed = False
        self.counter.attr["name"] = "count"
        self.counter.css({"display": "none", "margin": 0, "padding": 0, "cursor": "pointer"})
        if not self.options.readonly:
            self.input = page.ui.input()
            self.input.options.managed = False
            self.input.style.css.text_align = 'left'

    @property
    def options(self) -> OptNet.OptionsChat:
        """Property to the comments component options.
        Optional can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    @property
    def js(self) -> JsComponents.Chat:
        """The Javascript functions defined for this component.
        Those can be specific ones for the module or generic ones from the language.
        """
        if self._js is None:
            self._js = JsComponents.Chat(self, page=self.page)
        return self._js

    def enter(self, js_funcs, profile=None, source_event=None, on_ready=False):
        """

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.input.enter(js_funcs + [
            self.js.add(self.input.dom.content),
            self.input.dom.empty()], profile, source_event, on_ready)
        return self

    def send(self, socket, channel=None, js_funcs=None, profile=None):
        """

        :param socket:
        :param channel:
        :param js_funcs: The Javascript functions.
        :param profile: Optional. A flag to set the component performance storage.
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.input.enter(js_funcs + [
            socket.emit(channel or 'message', self.input.dom.content),
            self.input.dom.empty()], profile=profile)
        return self

    def subscribe(self, socket, channel, data=None, options=None, js_funcs=None, profile=None):
        """Subscribe to a socket channel.
        Data received from the socket are defined as a dictionary with a field data.

        The content of data will be used by this component.

        :param socket: Socket. A python socket object
        :param channel: The channel on which events will be received
        :param data:
        :param options:
        :param js_funcs: The Javascript functions.
        :param profile: Optional. A flag to set the component performance storage.
        """
        if data is None:
            data = socket.message
        js_funcs = js_funcs if js_funcs is not None else []
        socket.on(channel, [self.js.add(data)] + js_funcs, profile=profile)
        return self

    def __str__(self):
        return '''
      <div %(attr)s>
        %(inputTag)s
        <div style="margin:0;padding:5px 0;height:%(height)spx;overflow:auto"></div>
        %(counter)s
      </div>
      ''' % {'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'htmlCode': self.html_code,
             'height': int(self.css("height")[:-2]) - 70,
             'inputTag': '' if self.input is None else self.input.html(), "counter": self.counter.html()}


class Alert(Html.Html):
    requirements = ('bootstrap',)
    name = 'Alert'
    tag = "div"
    _option_cls = OptNet.OptionsAlert

    def __init__(self, page: primitives.PageModel, value, width, height, html_code, options, profile):
        super(Alert, self).__init__(page, value, css_attrs={"width": width, 'height': height},
                                    html_code=html_code, profile=profile, options=options)
        self.css({"padding": '5px', 'position': 'fixed', 'top': '20px', 'right': '20px'})

    @property
    def options(self) -> OptNet.OptionsAlert:
        """Property to the component options.
        Optional can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.

        Usage::

          danger = page.ui.network.warning()
          danger.options.time = None
        """
        return super().options

    def __str__(self):
        return "<%s %s></%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class News(Html.Html):
    name = 'News'
    tag = "div"
    _option_cls = OptNet.OptionsNews

    def __init__(self, page: primitives.PageModel, value, width, height, html_code, options, profile):
        super(News, self).__init__(page, value, css_attrs={"width": width, 'height': height},
                                   html_code=html_code, profile=profile, options=options)
        self.page.jsImports.add('moment')

    @property
    def js(self) -> JsComponents.News:
        """The Javascript functions defined for this component.
        Those can be specific ones for the module or generic ones from the language.
        """
        if self._js is None:
            self._js = JsComponents.News(self, page=self.page)
        return self._js

    @property
    def options(self) -> OptNet.OptionsNews:
        """Property to the component options.
        Optional can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def __str__(self):
        return "<%s %s></%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class Room(Html.Html):
    name = 'room'
    tag = "div"
    _option_cls = OptNet.OptionsNews

    def __init__(self, page: primitives.PageModel, img, width, height, html_code, options, profile):
        super(Room, self).__init__(page, "", css_attrs={"width": width, 'height': height},
                                   html_code=html_code, profile=profile, options=options)
        color = 'green'
        self.css({"padding": '5px', 'position': 'fixed', 'bottom': '10px', 'right': '20px', 'border-radius': '30px',
                  'border': '1px solid %s' % color, 'background-repeat': 'no-repeat', 'z-index': 100,
                  'background-position': 'center', 'background-size': 'cover', 'cursor': 'pointer',
                  'background-image': 'url(%s)' % img})
        self.status = self.page.ui.div()
        self.status.options.managed = False
        self.status.attr['name'] = "status"
        self.status.css({"width": "15px", "height": "15px", "background": color, "border-radius": "20px",
                         "border": "1px solid %s" % color, "bottom": "0px", "position": "absolute", "right": 0})
        self.dots = self.page.ui.div(".")
        self.dots.attr['name'] = "dots"
        self.dots.options.managed = False
        self.dots.css(
            {"bottom": "-5px", "position": "absolute", "left": "-25px", 'font-size': '30px', 'display': 'none'})

        keyframe_name = "dots"
        self.dots.style.css.animation = "%s 1s infinite" % keyframe_name
        attrs = {"0%, 20%": {"color": "rgba(0,0,0,0)", "text-shadow": ".25em 0 0 rgba(0,0,0,0),.5em 0 0 rgba(0,0,0,0)"},
                 "40%": {"text-shadow": ".25em 0 0 rgba(0,0,0,0),.5em 0 0 rgba(0,0,0,0)"},
                 "60%": {"text-shadow": ".25em 0 0 %s,.5em 0 0 rgba(0,0,0,0)" % page.theme.greys[-1]},
                 "80%, 100%": {"text-shadow": ".25em 0 0 %s,.5em 0 0 %s" % (
                     page.theme.greys[-1], page.theme.greys[-1])}}
        self.dots.style.css_class.keyframes(keyframe_name, attrs)

    @property
    def js(self) -> JsComponents.Room:
        """The Javascript functions defined for this component.
        Those can be specific ones for the module or generic ones from the language.
        """
        if self._js is None:
            self._js = JsComponents.Room(self, page=self.page)
        return self._js

    def __str__(self):
        return "<%s %s>%s%s</%s>" % (
          self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.dots.html(), self.status.html(),
          self.tag)


class DropFile(Html.Html):
    name, inputType = 'Drop File Area', "file"
    _option_cls = OptNet.OptionFiles

    def __init__(self, page: primitives.PageModel, vals, delimiter, tooltip, width, height, html_code, options,
                 profile):
        super(DropFile, self).__init__(page, vals, profile=profile, html_code=html_code, options=options,
                                       css_attrs={"width": width, "height": height})
        self.tooltip(tooltip, location='bottom')
        self.container = self.page.ui.div()
        self.container.css({"display": "inline-block", 'text-align': 'center', "color": self.page.theme.success.light,
                            'border': "1px dashed %s" % page.theme.colors[-1]})
        self.container.style.css.bold()
        self.container.style.css.margin = "0 5px"
        self.container.style.css.width = "calc(100% - 10px)"
        self.container.style.css.background = page.theme.greys[0]
        self.container.add(self.page.ui.icon("fas fa-cloud-upload-alt", color=page.theme.colors[-1]))
        self.container.options.managed = False
        self.text = self.page.ui.text()
        self.text.style.css.italic()
        self.text.style.css.font_factor(-2)
        self.text.style.css.color = self.page.theme.greys[5]
        self.text.options.managed = False
        self.text.style.css.margin_bottom = 5
        self.text.style.css.padding_left = 5
        self.delimiter = self.page.ui.text(
            delimiter, width=(25, 'px'), html_code="%s_delimiter" % self.htmlCode)
        self.delimiter.options.managed = False
        self.delimiter.style.css.bold()
        self.delimiter.style.css.display = 'inline-block'
        self.delimiter.style.css.text_align = 'center'
        self.delimiter.style.css.border = "1px solid %s" % page.theme.colors[3]
        self.delimiter.style.css.margin_top = 5
        self.delimiter.style.css.margin_left = 5
        self.delimiter.style.css.margin_right = 5
        self.delimiter.editable()
        self.delimiter.style.css.cursor = 'pointer'
        self.delete = self.page.ui.text("&#x274c;", width=(20, 'px'), html_code="%s_delete" % self.htmlCode)
        self.delete.options.managed = False
        self.delete.style.css.margin_top = -20
        self.delete.style.css.hide()
        self.delete.style.css.right = 0
        self.delete.style.css.position = "absolute"
        # self.delimiter.click(["document.execCommand('selectAll',false,null)"])
        # self.delimiter.keypress.enter(["event.preventDefault(); event.target.blur(); return"])
        self.options.delimiter = self.delimiter.dom.content
        self.style.css.border = "1px solid %s" % page.theme.colors[-1]
        self.style.css.position = "relative"
        if self.options.format != 'json':
            self.icon = self.page.ui.icon("fas fa-paste")
            self.icon.options.managed = False
            if "color" in self.icon.attr['css']:
                del self.icon.attr['css']["color"]
            self.icon.style.add_classes.icon.selected()
            self.icon.style.css.margin_left = 5
            self.icon.click(self.dom.events.trigger("paste"))
        self.sync = None
        if options is not None and options.get("sync"):
            self.sync = self.page.ui.icon("fas fa-sync-alt")
            self.sync.options.managed = False
            self.sync.style.css.margin_left = 5

    @classmethod
    def get_requirements(cls, page: primitives.PageModel, options: types.OPTION_TYPE = None) -> tuple:
        """Update requirements with the defined Icons' family.

        :param page: Page context
        :param options: Component input options
        """
        if options and options.get('icon_family') is not None:
            return (options['icon_family'],)

        return (page.icons.family,)

    @property
    def dom(self) -> JsHtmlNetwork.JsHtmlDropFiles:
        """ The dom component property """
        if self._dom is None:
            self._dom = JsHtmlNetwork.JsHtmlDropFiles(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptNet.OptionFiles:
        """Property to the component options.
        Optional can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.
        """
        return super().options

    def transfer(self, url: str):
        """Create a Ajax transfer to a distant server.

        :param url: The transfer end point on the server.
        """
        # TODO add if else statement for the allowed and forbidden extensions
        form_data = self.page.js.data.formdata.get("form_data")
        post = self.page.js.post(url, form_data, is_json=False)
        return post

    def drop(self, js_funcs, js_data=None, components=None, prevent_default=True, profile=None):
        """Add a drag and drop property to the element.

        Usage::

          drop_area.drop([drop_area.transfer("<URL>")], components=[])

        :param js_funcs: The Javascript series of functions
        :param js_data: Optional. A datamap objection of a dictionary
        :param components: The different HTML objects to be added to the component
        :param prevent_default: Optional. Prevent default on the JavaScript event
        :param profile: Optional. A flag to set the component performance storage

        :return: Return self to allow the chaining
        """
        dft_fnc = ""
        if prevent_default:
            dft_fnc = self.page.js.objects.event.preventDefault()
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        form_data = self.page.js.data.formdata
        new_js_funcs = [form_data.new("form_data"),
                        form_data.append("%s_file" % self.htmlCode, self.page.js.objects.event.dataTransfer.files[0])]
        if components is not None:
            for component in components:
                if isinstance(component, tuple):
                    new_js_funcs.append(form_data.add(component[0], component[1]))
                else:
                    new_js_funcs.append(form_data.add(component))
        if js_data is not None:
            new_js_funcs.extend(form_data.update(js_data))
        new_js_funcs.extend(js_funcs)
        str_fncs = JsUtils.jsConvertFncs(
            ["var data = %s" % self.page.js.objects.event.dataTransfer.files] + new_js_funcs, toStr=True,
            profile=profile)
        self.attr["ondragover"] = "(function(event){%s})(event)" % dft_fnc
        self.on("drop", ["%s; %s; return false" % (dft_fnc, str_fncs)])
        return self

    def loading(self, label: str = "Processing data", **kwargs):
        """
        :param label: Optional.
        """
        return self.text.build('<i style="margin-right:5px" class="fas fa-spinner fa-spin"></i>%s' % label)

    def load(self, js_funcs, js_data=None, components=None, prevent_default=True, profile=None):
        """Load the content of the file.
        This function will first use as underlying the drop method to get the file dropped.

        Usage::

          drop_area.load([drop_area.transfer("<URL>")], components=[])

        :param js_funcs: The Javascript series of functions
        :param js_data: Optional. A datamap objection of a dictionary
        :param components: Optional. The different HTML objects to be added to the component
        :param prevent_default: Optional. Prevent default on the JavaScript event
        :param profile: Optional. A flag to set the component performance storage
        """
        from epyk.core.data import events

        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        if components is None:
            components = []
        components.append(self.delimiter)
        return self.drop(['''
var reader = new FileReader(); var f = data[data.length - 1];
reader.onloadstart = function() {%s};
reader.onload = (function(value) {
  return function(e){data = atob(e.target.result.replace(/^data:.+;base64,/, '')); %s}})(f);
reader.readAsDataURL(f);''' % (
          JsUtils.jsConvertFncs([self.loading()], toStr=True), JsUtils.jsConvertFncs(js_funcs + [
            self.text.dom.setAttribute("title", self.dom.content.length.toString().add(" rows")),
            self.text.build(events.file.description) if self.options.text else self.text.build("File Loaded"),
            self.delete.dom.show(display_value="block")], toStr=True),
        )], js_data=js_data, components=components, prevent_default=prevent_default, profile=profile)

    def paste(self, js_funcs, components=None, profile=None, source_event=None):
        """

        :param js_funcs: Javascript functions
        :param components: The different HTML objects to be added to the component
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        if components is None:
            components = [self.delimiter]
        else:
            components.append(self.delimiter)
        return super(DropFile, self).paste([self.loading()] + js_funcs + [
            self.text.build(self.page.js.objects.get("'Bespoke data Loaded, '+ (new Date).toISOString()")),
            self.delete.dom.show(display_value="block"),
            self.text.dom.setAttribute(
                "title", self.dom.content.length.toString().add(" rows"))], profile, source_event,
                                           components=components)

    def __str__(self):
        if self.options.format == 'json':
            return '''
        <div %(strAttr)s>
          %(container)s
          %(text)s
          %(delete)s
          <input id="%(htmlCode)s_report" style="display:none;"/>
        </div>
        ''' % {'htmlCode': self.htmlCode, 'strAttr': self.get_attrs(css_class_names=self.style.get_classes()),
               'container': self.container.html(), 'text': self.text.html(), 'delete': self.delete.html()}

        return '''
      <div %(strAttr)s>
        <div style='display:inline-block;padding-left:5px'>using %(delimiter)s delimiter (<i>TAB for tabulation</i>)%(paste)s %(sync)s</div>
        %(container)s
        %(text)s
        %(delete)s
        <input id="%(htmlCode)s_report" style="display:none;"/>
      </div>
      ''' % {'htmlCode': self.htmlCode, 'strAttr': self.get_attrs(css_class_names=self.style.get_classes()),
             'paste': self.icon.html(), 'sync': self.sync.html() if self.sync is not None else "",
             'container': self.container.html(), 'text': self.text.html(), 'delete': self.delete.html(),
             'delimiter': self.delimiter.html()}
