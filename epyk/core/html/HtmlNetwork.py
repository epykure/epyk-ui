#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.html.options import OptNet

from epyk.core.js.objects import JsComponents
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlNetwork

# The list of CSS classes
from epyk.core.css.styles import GrpClsNetwork
from epyk.core.css import Defaults as cssDefaults


class Comments(Html.Html):
  name = 'Comment'
  _option_cls = OptNet.OptionsChat

  def __init__(self, page: primitives.PageModel, record, width, height, html_code, options, profile):
    super(Comments, self).__init__(page, record, css_attrs={"width": width, 'height': height}, html_code=html_code,
                                   profile=profile, options=options)
    self.css({'padding': '5px'})
    self.input = None
    self.counter = page.ui.texts.span("0", width=(None, 'px'))
    self.counter.options.managed = False
    self.counter.attr["name"] = "count"
    self.counter.css({"display": "inline-block", "margin": 0, "padding": 0, "cursor": "pointer"})
    if not self.options.readonly:
      self.input = page.ui.input(html_code="%s_input" % self.htmlCode)
      self.input.options.managed = False
      self.input.style.css.text_align = 'left'
      if "background" in options:
        self.input.style.css.background = options["background"]

  @property
  def options(self) -> OptNet.OptionsChat:
    """
    Description:
    ------------
    Property to the comments component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  @property
  def js(self) -> JsComponents.Chat:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    :return: A Javascript Dom object
    """
    if self._js is None:
      self._js = JsComponents.Chat(self, page=self.page)
    return self._js

  _js__builder__ = '''
        if (data != null){
          var comments;
          if(!Array.isArray(data)){ var now = new Date();
            comments = [{text: data, time: moment(now).format('YYYY-MM-DD HH:mm:ss')}]; 
          } else {comments = data}
          comments.forEach(function(comment){
            var feed = document.createElement("p"); feed.style.margin = "0 0 5px 0";
            if(options.showdown){var converter = new showdown.Converter(options.showdown); 
            comment.text = converter.makeHtml(comment.text.trim())};
            feed.innerHTML = comment.text; htmlObj.querySelector("div").prepend(feed);
    
            var dateNews = document.createElement("p");
            dateNews.style.margin = 0;
            dateNews.style.fontWeight = 'bold';
            dateNews.innerHTML = comment.time;
            htmlObj.querySelector("div").prepend(dateNews);
          })
        }'''

  def add(self, text: str, time: str):
    """
    Description:
    ------------
    Add a text message.

    Attributes:
    ----------
    :param text: The text message.
    :param time: the timestamp.
    """
    self.val.append({"text": text, "time": time})
    return self

  def enter(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    ------------
    Define the function when the user press enter.

    Attributes:
    ----------
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item).
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if self.options.readonly:
      self.options.readonly = False
      self.input = self.page.ui.input(html_code="%s_input" % self.htmlCode)
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
    Description:
    ------------

    Attributes:
    ----------
    :param socket:
    :param channel:
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
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

  def subscribe(self, socket, channel, data=None, options=None, js_funcs=None, profile=None):
    """
    Description:
    ------------
    Subscribe to a socket channel.
    Data received from the socket are defined as a dictionary with a field data.

    The content of data will be used by this component.

    Related Pages:

      https://timepicker.co/options/

    Attributes:
    ----------
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

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '''
      <div %(attr)s>
        <span>%(counter)s Comments <i style="margin:0 5px 0 20px;cursor:pointer;display:inline-block" class="fas fa-sort-amount-up"></i>Sort by</span>
        %(inputTag)s
        <div class='scroll_content' style="height:%(height)spx;margin:0;padding:5px 0;overflow:auto">
          <div name="comms"></div>
        </div>
      </div>
      ''' % {'attr': self.get_attrs(css_class_names=self.style.get_classes()), "counter": self.counter.html(),
             'height': int(self.css("height")[:-2]) - 70,
             'inputTag': '' if self.input is None else self.input.html()}


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
              "padding": "5px",  "z-index": 200})

  @property
  def style(self) -> GrpClsNetwork.ClassNetworkBot:
    """
    Description:
    ------------
    Property to the CSS Style of the component.
    """
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
       </div>   
    ''' % {'attr': self.get_attrs(), "name": 'Test'}


class Assistant(Html.Html):
  name = 'Assistant'

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
    return '''<div %(attr)s>%(name)s%(avatar)s%(mail)s%(chat)s</div>''' % {
      'attr': self.get_attrs(), 'avatar': self.val.html(), 'mail': self.mail.html(), 'chat': self.chat.html(),
      'name': self.name.html()}


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
    """
    Description:
    ------------
    Property to the comments component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  @property
  def js(self) -> JsComponents.Chat:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.
    """
    if self._js is None:
      self._js = JsComponents.Chat(self, page=self.page)
    return self._js

  _js__builder__ = '''
      var feed = document.createElement("p");
      feed.style.margin = "0 0 5px 0";
      if(options.showdown){var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data.trim())};
      feed.innerHTML = data; htmlObj.querySelector("div").prepend(feed);
      
      var now = new Date();
      var dateStringWithTime = moment(now).format('YYYY-MM-DD HH:mm:ss');
      var dateNews = document.createElement("p");
      dateNews.style.margin = 0;
      dateNews.style.fontWeight = 'bold';
      dateNews.innerHTML = dateStringWithTime;
      htmlObj.querySelector("div").prepend(dateNews);
      '''

  def enter(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item).
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.input.enter(js_funcs + [
      self.js.add(self.input.dom.content),
      self.input.dom.empty()], profile, source_event, on_ready)
    return self

  def send(self, socket, channel=None, js_funcs=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
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
    """
    Description:
    ------------
    Subscribe to a socket channel.
    Data received from the socket are defined as a dictionary with a field data.

    The content of data will be used by this component.

    Related Pages:

      https://timepicker.co/options/

    Attributes:
    ----------
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
      ''' % {'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'htmlCode': self.htmlCode,
             'height': int(self.css("height")[:-2]) - 70,
             'inputTag': '' if self.input is None else self.input.html(), "counter": self.counter.html()}


class Alert(Html.Html):
  requirements = ('bootstrap', )
  name = 'Alert'
  _option_cls = OptNet.OptionsAlert

  def __init__(self, page: primitives.PageModel, value, width, height, html_code, options, profile):
    super(Alert, self).__init__(page, value, css_attrs={"width": width, 'height': height},
                                html_code=html_code, profile=profile, options=options)
    self.css({"padding": '5px', 'position': 'fixed', 'top': '20px', 'right': '20px'})

  @property
  def options(self) -> OptNet.OptionsAlert:
    """
    Description:
    ------------
    Property to the component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    Usage::

      danger = page.ui.network.warning()
      danger.options.time = None
    """
    return super().options

  _js__builder__ = '''
      var feed = document.createElement("p");
      options.classes.forEach(function(cls){ feed.classList.add(cls) });
      if(options.showdown){
        var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data.trim())};
      if (htmlObj.style.display != 'block'){htmlObj.innerHTML = ""};
      if (options.close){
        var icon = document.createElement("i");  
        icon.className = "fas fa-times"; icon.style.float = "right"; icon.style.marginRight = "2px";
        icon.style.cursor = "pointer"; icon.style.zIndex = 50; icon.style.position = "relative";
        icon.addEventListener("click", function(){feed.remove(); this.remove()} )
        htmlObj.appendChild(icon)};
      feed.innerHTML = data; htmlObj.appendChild(feed);
      var s = htmlObj.style; s.opacity = 1; htmlObj.style.display = 'block';
      if(options.time != null){
        (function fade(){(s.opacity-=.1)<0?s.display="none": setTimeout(fade, options.time)})()}
      '''

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(css_class_names=self.style.get_classes())


class News(Html.Html):
  name = 'News'
  _option_cls = OptNet.OptionsNews

  def __init__(self, page: primitives.PageModel, value, width, height, html_code, options, profile):
    super(News, self).__init__(page, value, css_attrs={"width": width, 'height': height},
                               html_code=html_code, profile=profile, options=options)
    self.page.jsImports.add('moment')

  _js__builder__ = '''
    var feed = document.createElement("p");
    feed.style.margin = "0 0 5px 0";
    if(options.showdown){
      var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data.trim())};
    feed.innerHTML = data; htmlObj.prepend(feed);
    
    if (options.dated){
      var now = new Date();
      var dateStringWithTime = moment(now).format('YYYY-MM-DD HH:mm:ss');
      var dateNews = document.createElement("p");
      dateNews.style.margin = 0;
      dateNews.style.fontWeight = 'bold';
      dateNews.innerHTML = dateStringWithTime;
      htmlObj.prepend(dateNews)}
    '''

  @property
  def js(self) -> JsComponents.News:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.
    """
    if self._js is None:
      self._js = JsComponents.News(self, page=self.page)
    return self._js

  @property
  def options(self) -> OptNet.OptionsNews:
    """
    Description:
    ------------
    Property to the component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(css_class_names=self.style.get_classes())


class Room(Html.Html):
  name = 'room'
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
    self.dots.css({"bottom": "-5px", "position": "absolute", "left": "-25px", 'font-size': '30px', 'display': 'none'})

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
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.
    """
    if self._js is None:
      self._js = JsComponents.Room(self, page=self.page)
    return self._js

  def __str__(self):
    return "<div %s>%s%s</div>" % (self.get_attrs(css_class_names=self.style.get_classes()), self.dots.html(),
                                   self.status.html())


class DropFile(Html.Html):
  requirements = (cssDefaults.ICON_FAMILY,)
  name, inputType = 'Drop File Area', "file"
  _option_cls = OptNet.OptionFiles

  def __init__(self, page: primitives.PageModel, vals, delimiter, tooltip, width, height, html_code, options, profile):
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
    #self.delimiter.click(["document.execCommand('selectAll',false,null)"])
    #self.delimiter.keypress.enter(["event.preventDefault(); event.target.blur(); return"])
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

  @property
  def dom(self) -> JsHtmlNetwork.JsHtmlDropFiles:
    """
    Description:
    ------------

    """
    if self._dom is None:
      self._dom = JsHtmlNetwork.JsHtmlDropFiles(self, page=self.page)
    return self._dom

  @property
  def options(self) -> OptNet.OptionFiles:
    """
    Description:
    ------------
    Property to the component options.
    Optional can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  def transfer(self, url: str):
    """
    Description:
    -----------
    Create a Ajax transfer to a distant server.

    Attributes:
    ----------
    :param url: The transfer end point on the server.
    """
    # TODO add if else statement for the allowed and forbidden extensions
    form_data = self.page.js.data.formdata.get("form_data")
    post = self.page.js.post(url, form_data, is_json=False)
    return post

  def drop(self, js_funcs, js_data=None, components=None, prevent_default=True, profile=None):
    """
    Description:
    -----------
    Add a drag and drop property to the element.

    Usage::

      drop_area.drop([
        drop_area.transfer("<URL>")
      ], components=[])

    Attributes:
    ----------
    :param js_funcs: The Javascript series of functions.
    :param js_data: Optional. A datamap objection of a dictionary.
    :param components: The different HTML objects to be added to the component.
    :param prevent_default: Optional. Prevent default on the JavaScript event.
    :param profile: Optional. A flag to set the component performance storage.

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
      ["var data = %s" % self.page.js.objects.event.dataTransfer.files] + new_js_funcs, toStr=True, profile=profile)
    self.attr["ondragover"] = "(function(event){%s})(event)" % dft_fnc
    self.on("drop", ["%s; %s; return false" % (dft_fnc, str_fncs)])
    return self

  def loading(self, label="Processing data"):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param label: Optional.
    """
    return self.text.build('<i style="margin-right:5px" class="fas fa-spinner fa-spin"></i>%s' % label)

  def load(self, js_funcs, js_data=None, components=None, prevent_default=True, profile=None):
    """
    Description:
    -----------
    Load the content of the file.

    This function will first use as underlying the drop method to get the file dropped.

    Usage::

      drop_area.load([
        drop_area.transfer("<URL>")
      ], components=[])

    Attributes:
    ----------
    :param js_funcs: The Javascript series of functions.
    :param js_data: Optional. A datamap objection of a dictionary.
    :param components: Optional. The different HTML objects to be added to the component.
    :param prevent_default: Optional. Prevent default on the JavaScript event.
    :param profile: Optional. A flag to set the component performance storage.
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
       reader.readAsDataURL(f);
      ''' % (JsUtils.jsConvertFncs([self.loading()], toStr=True), JsUtils.jsConvertFncs(js_funcs + [
        self.text.dom.setAttribute("title", self.dom.content.length.toString().add(" rows")),
        self.text.build(events.file.description) if self.options.text else self.text.build("File Loaded"),
        self.delete.dom.show(display_value="block")], toStr=True),
       )], js_data=js_data, components=components, prevent_default=prevent_default, profile=profile)

  def paste(self, js_funcs, components=None, profile=None, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param components: The different HTML objects to be added to the component.
    :param profile: Optional. A flag to set the component performance storage.
    :param source_event: Optional. The source target for the event.
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
        "title", self.dom.content.length.toString().add(" rows"))], profile, source_event, components=components)

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
