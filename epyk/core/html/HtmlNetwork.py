#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptNet

from epyk.core.data import events

from epyk.core.js.objects import JsComponents
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlNetwork

# The list of CSS classes
from epyk.core.css.styles import GrpClsNetwork


class Comments(Html.Html):
  name = 'Comment'

  def __init__(self, report, recordSet, width, height, htmlCode, options, profile):
    super(Comments, self).__init__(report, recordSet, css_attrs={"width": width, 'height': height}, htmlCode=htmlCode, profile=profile)
    self.__options = OptNet.OptionsChat(self, options)
    self.css({'padding': '5px'})
    self.input = None
    self.counter = report.ui.texts.span("0", width=(None, 'px'))
    self.counter.options.managed = False
    self.counter.attr["name"] = "count"
    self.counter.css({"display": "inline-block", "margin": 0, "padding": 0, "cursor": "pointer"})
    if not self.options.readonly:
      self.input = report.ui.input()
      self.input.options.managed = False
      self.input.style.css.text_align = 'left'

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptNet.OptionsChat
    """
    return self.__options

  @property
  def js(self):
    """
    Description:
    -----------

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsComponents.Chat
    """
    if self._js is None:
      self._js = JsComponents.Chat(self, report=self._report)
    return self._js

  @property
  def _js__builder__(self):
    return '''
        if (data != null){
          var comments;
          if(!Array.isArray(data)){ var now = new Date();
            comments = [{text: data, time: moment(now).format('YYYY-MM-DD HH:mm:ss')}]; 
          } else {comments = data}
          comments.forEach(function(comment){
            var feed = document.createElement("p"); feed.style.margin = "0 0 5px 0";
            if(options.showdown){var converter = new showdown.Converter(options.showdown); comment.text = converter.makeHtml(comment.text.trim())};
            feed.innerHTML = comment.text; htmlObj.querySelector("div").prepend(feed);
    
            var dateNews = document.createElement("p");
            dateNews.style.margin = 0;
            dateNews.style.fontWeight = 'bold';
            dateNews.innerHTML = comment.time;
            htmlObj.querySelector("div").prepend(dateNews);
          })
        }'''

  def add(self, text, time):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param time:
    """
    self.val.append({"text": text, "time": time})
    return self

  def enter(self, jsFncs=None, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: String or List. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if self.options.readonly:
      self.options.readonly = False
      self.input = self._report.ui.input()
      self.input.options.managed = False
      self.input.style.css.text_align = 'left'
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs] if jsFncs is not None else []
    self.input.enter(jsFncs + [
      self.js.add(self.input.dom.content),
      self.input.dom.empty()], profile, source_event, onReady)
    return self

  def send(self, socket, channel=None, jsFncs=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param socket:
    :param channel:
    :param jsFncs:
    :param profile:
    """
    if self.options.readonly:
      self.options.readonly = False
      self.input = self._report.ui.input()
      self.input.options.managed = False
      self.input.style.css.text_align = 'left'
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.input.enter(jsFncs + [
      socket.emit(channel or 'message', self.input.dom.content),
      self.input.dom.empty()])
    return self

  def subscribe(self, socket, channel, data=None, options=None, jsFncs=None, profile=False):
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
    :param channel: String. The channel on which events will be received
    """
    if data is None:
      data = socket.message
    jsFncs = jsFncs if jsFncs is not None else []
    socket.on(channel, [self.js.add(data)] + jsFncs)
    return self

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '''
      <div %(attr)s>
        <span>%(counter)s Comments <i style="margin:0 5px 0 20px;cursor:pointer;display:inline-block" class="fas fa-sort-amount-up"></i>Sort by</span>
        %(inputTag)s
        <div class='scroll_content' style="height:%(height)spx;margin:0;padding:5px 0;overflow:auto">
          <div name="comms"></div>
        </div>
      </div>
      ''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), "counter": self.counter.html(),
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

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Bot, self).__init__(report, [], css_attrs={"width": width}, htmlCode=htmlCode, profile=profile)
    self.css({"text-align": 'right', "position": 'fixed', "bottom": 0, 'margin': '10px', "height": "80px",
              "padding": "5px",  "z-index": 200})

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component

    :rtype: GrpClsNetwork.ClassNetworkBot
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
  """
  """
  name = 'Assistant'

  def __init__(self, component, title, report, htmlCode, options, profile):
    super(Assistant, self).__init__(report, component, htmlCode=htmlCode, profile=profile)
    self.css({'margin': '0 10px', "padding": "0 5px", 'text-align': 'center'})
    self.name = report.ui.text(title, align="center")
    self.name.options.managed = False
    self.name.style.css.bold()
    self.mail = report.ui.icon("fas fa-at")
    self.mail.options.managed = False
    self.mail.style.add_classes.div.color_hover()
    self.mail.style.css.margin_right = 2
    self.mail.style.css.background = 'white'
    self.mail.style.css.padding = "2px 2px"
    self.mail.style.css.border_radius = 20
    self.mail.style.css.margin_top = -20
    self.chat = report.ui.icon("far fa-comments")
    self.chat.options.managed = False
    self.chat.style.add_classes.div.color_hover()
    self.chat.style.css.margin_left = 2
    self.chat.style.css.background = 'white'
    self.chat.style.css.padding = "2px 2px"
    self.chat.style.css.border_radius = 20
    self.chat.style.css.margin_top = -20

  def __str__(self):
    return '''<div %(attr)s>%(name)s%(avatar)s%(mail)s%(chat)s</div>''' % {'attr': self.get_attrs(),
               'avatar': self.val.html(), 'mail': self.mail.html(), 'chat': self.chat.html(), 'name': self.name.html()}


class Chat(Html.Html):
  name = 'Chat'

  def __init__(self, report, recordSet, width, height, htmlCode, options, profile):
    super(Chat, self).__init__(report, recordSet, css_attrs={"width": width, 'height': height}, htmlCode=htmlCode, profile=profile)
    self.__options = OptNet.OptionsChat(self, options)
    self.css({'padding': '5px'})
    self.input = None
    self.counter = report.ui.texts.span("0", width=(None, 'px'))
    self.counter.options.managed = False
    self.counter.attr["name"] = "count"
    self.counter.css({"display": "none", "margin": 0, "padding": 0, "cursor": "pointer"})
    if not self.options.readonly:
      self.input = report.ui.input()
      self.input.options.managed = False
      self.input.style.css.text_align = 'left'

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptNet.OptionsChat
    """
    return self.__options

  @property
  def js(self):
    """
    Description:
    -----------

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsComponents.Chat
    """
    if self._js is None:
      self._js = JsComponents.Chat(self, report=self._report)
    return self._js

  @property
  def _js__builder__(self):
    return '''
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

  def enter(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: String or List. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.input.enter(jsFncs + [
      self.js.add(self.input.dom.content),
      self.input.dom.empty()], profile, source_event, onReady)
    return self

  def send(self, socket, channel=None, jsFncs=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param socket:
    :param channel:
    :param jsFncs:
    :param profile:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.input.enter(jsFncs + [
      socket.emit(channel or 'message', self.input.dom.content),
      self.input.dom.empty()])
    return self

  def subscribe(self, socket, channel, data=None, options=None, jsFncs=None, profile=False):
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
    :param channel: String. The channel on which events will be received
    """
    if data is None:
      data = socket.message
    jsFncs = jsFncs if jsFncs is not None else []
    socket.on(channel, [self.js.add(data)] + jsFncs)
    return self

  def __str__(self):
    return '''
      <div %(attr)s>
        %(inputTag)s
        <div style="margin:0;padding:5px 0;height:%(height)spx;overflow:auto"></div>
        %(counter)s
      </div>
      ''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'htmlCode': self.htmlCode, 'height': int(self.css("height")[:-2]) - 70,
             'inputTag': '' if self.input is None else self.input.html(), "counter": self.counter.html()}


class Alert(Html.Html):
  requirements = ('bootstrap', )
  name = 'Alert'

  def __init__(self, report, value, width, height, htmlCode, options, profile):
    super(Alert, self).__init__(report, value, css_attrs={"width": width, 'height': height}, htmlCode=htmlCode, profile=profile)
    self.__options = OptNet.OptionsAlert(self, options)
    self.css({"padding": '5px', 'position': 'fixed', 'top': '20px', 'right': '20px'})

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptNet.OptionsAlert
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
      var feed = document.createElement("p");
      options.classes.forEach(function(cls){ feed.classList.add(cls) });
      if(options.showdown){var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data.trim())};
      if (htmlObj.style.display != 'block'){htmlObj.innerHTML = ""; };
      feed.innerHTML = data; htmlObj.appendChild(feed);
      var s = htmlObj.style; s.opacity = 1; htmlObj.style.display = 'block';
      (function fade(){(s.opacity-=.1)<0?s.display="none": setTimeout(fade, options.time)})();
      '''

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.style.get_classes())


class News(Html.Html):
  name = 'News'

  def __init__(self, report, value, width, height, htmlCode, options, profile):
    super(News, self).__init__(report, value, css_attrs={"width": width, 'height': height}, htmlCode=htmlCode, profile=profile)
    #self.css({"padding": '5px', 'position': 'fixed', 'border': '1px solid %s' % self._report.theme.success[1],
    #          "background": self._report.theme.greys[0], 'bottom': '20px', 'right': '20px'})
    self.__options = OptNet.OptionsNews(self, options)
    self._report.jsImports.add('moment')

  @property
  def _js__builder__(self):
    return '''
    var feed = document.createElement("p");
    feed.style.margin = "0 0 5px 0";
    if(options.showdown){var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data.trim())};
    feed.innerHTML = data; htmlObj.prepend(feed);
    
    if (options.dated){
      var now = new Date();
      var dateStringWithTime = moment(now).format('YYYY-MM-DD HH:mm:ss');
      var dateNews = document.createElement("p");
      dateNews.style.margin = 0;
      dateNews.style.fontWeight = 'bold';
      dateNews.innerHTML = dateStringWithTime;
      htmlObj.prepend(dateNews); }
    '''

  @property
  def js(self):
    """
    Description:
    -----------

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsComponents.News
    """
    if self._js is None:
      self._js = JsComponents.News(self, report=self._report)
    return self._js

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptNet.OptionsNews
    """
    return self.__options

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.style.get_classes())


class Room(Html.Html):
  name = 'room'

  def __init__(self, report, img, width, height, htmlCode, options, profile):
    super(Room, self).__init__(report, "", css_attrs={"width": width, 'height': height}, htmlCode=htmlCode, profile=profile)
    self.__options = OptNet.OptionsNews(self, options)
    color = 'green'
    self.css({"padding": '5px', 'position': 'fixed', 'bottom': '10px', 'right': '20px', 'border-radius': '30px',
              'border': '1px solid %s' % color, 'background-repeat': 'no-repeat', 'z-index': 100,
              'background-position': 'center', 'background-size': 'cover', 'cursor': 'pointer',
              'background-image': 'url(%s)' % img})
    self.status = self._report.ui.div()
    self.status.options.managed = False
    self.status.attr['name'] = "status"
    self.status.css({"width": "15px", "height": "15px", "background": color, "border-radius": "20px",
                     "border": "1px solid %s" % color, "bottom": "0px", "position": "absolute", "right": 0})
    self.dots = self._report.ui.div(".")
    self.dots.attr['name'] = "dots"
    self.dots.options.managed = False
    self.dots.css({"bottom": "-5px", "position": "absolute", "left": "-25px", 'font-size': '30px', 'display': 'none'})

    keyframe_name = "dots"
    self.dots.style.css.animation = "%s 1s infinite" % keyframe_name
    attrs = {"0%, 20%": {"color": "rgba(0,0,0,0)", "text-shadow": ".25em 0 0 rgba(0,0,0,0),.5em 0 0 rgba(0,0,0,0)"},
             "40%": {"text-shadow": ".25em 0 0 rgba(0,0,0,0),.5em 0 0 rgba(0,0,0,0)"},
             "60%": {"text-shadow": ".25em 0 0 %s,.5em 0 0 rgba(0,0,0,0)" % report.theme.greys[-1]},
             "80%, 100%": {"text-shadow": ".25em 0 0 %s,.5em 0 0 %s" % (report.theme.greys[-1], report.theme.greys[-1])}}
    self.dots.style.css_class.keyframes(keyframe_name, attrs)

  @property
  def js(self):
    """
    Description:
    -----------

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsComponents.Room
    """
    if self._js is None:
      self._js = JsComponents.Room(self, report=self._report)
    return self._js

  def __str__(self):
    return "<div %s>%s%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.dots.html(), self.status.html())


class DropFile(Html.Html):
  requirements = ('font-awesome',)
  name, inputType = 'Drop File Area', "file"

  def __init__(self, report, vals, delimiter, tooltip, width, height, htmlCode, options, profile):
    super(DropFile, self).__init__(report, vals, profile=profile, htmlCode=htmlCode, css_attrs={"width": width, "height": height})
    self.__options = OptNet.OptionFiles(self, options)
    self.tooltip(tooltip, location='bottom')
    self.container = self._report.ui.div()
    self.container.css({"display": "inline-block", 'text-align': 'center', "color": self._report.theme.success[0],
                        'border': "1px dashed %s" % report.theme.colors[-1]})
    self.container.style.css.bold()
    self.container.add(self._report.ui.icon("fas fa-cloud-upload-alt", color=report.theme.colors[-1]))
    self.container.options.managed = False
    self.text = self._report.ui.text()
    self.text.style.css.italic()
    self.text.style.css.font_factor(-2)
    self.text.style.css.color = self._report.theme.greys[5]
    self.text.options.managed = False
    self.text.style.css.margin_bottom = 5
    self.delimiter = self._report.ui.text(delimiter, width=(25, 'px'), htmlCode="%s_delimiter" % self.htmlCode, options={"editable": True})
    self.delimiter.options.managed = False
    self.delimiter.style.css.bold()
    self.delimiter.style.css.display = 'inline-block'
    self.delimiter.style.css.text_align = 'center'
    self.delimiter.style.css.border = "1px solid %s" % report.theme.colors[3]
    self.delimiter.style.css.font_factor(2)
    self.delimiter.style.css.margin_top = 5
    self.delimiter.style.css.margin_left = 5
    self.delimiter.style.css.margin_right = 5
    self.delimiter.style.css.cursor = 'pointer'
    self.options.delimiter = self.delimiter.dom.content
    if self.options.format != 'json':
      self.icon = self._report.ui.icon("fas fa-paste")
      self.icon.options.managed = False
      self.icon.style.css.margin_left = 5
      self.icon.click(self.dom.events.trigger("paste"))

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsHtmlNetwork.JsHtmlDropFiles
    """
    if self._dom is None:
      self._dom = JsHtmlNetwork.JsHtmlDropFiles(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Specific options for the files components

    :rtype: OptNet.OptionFiles
    """
    return self.__options

  def transfer(self, url):
    """
    Description:
    -----------
    Create a Ajax transfer to a distant server

    Attributes:
    ----------
    :param url: String. The transfer end point on the server
    """
    # TODO add if else statement for the allowed and forbidden extensions
    post = self._report.js.post(url, self._report.js.objects.get("form_data"), is_json=False)
    return post

  def drop(self, jsFncs, jsData=None, preventDefault=True, profile=False):
    """
    Description:
    -----------
    Add a drag and drop property to the element

    Usage::

    Attributes:
    ----------
    :param jsFncs: List. The Javascript series of functions
    :param jsData: Data. A datamap objection of a dictionary
    :param preventDefault: Boolean. Prevent default on the JavaScript event
    :param profile: Boolean. Profiling

    :return: Return self to allow the chaining
    """
    dft_fnc = ""
    if preventDefault:
      dft_fnc = self._report.js.objects.event.preventDefault()
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    form_data = self._report.js.data.formdata()
    newJsFncs = [form_data.new("form_data"),  form_data.append("file", self._report.js.objects.event.dataTransfer.files[0])]
    if jsData is not None:
      newJsFncs.extend(form_data.update(jsData))
    newJsFncs.extend(jsFncs)
    str_fncs = JsUtils.jsConvertFncs(["var data = %s" % self._report.js.objects.event.dataTransfer.files] + newJsFncs, toStr=True)
    self.attr["ondragover"] = "(function(event){%s})(event)" % dft_fnc
    self.on("drop", ["%s; %s; return false" % (dft_fnc, str_fncs)])
    return self

  def loading(self, label="Processing data"):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param label:
    """
    return self.text.build('<i style="margin-right:5px" class="fas fa-spinner fa-spin"></i>%s' % label)

  def load(self, jsFncs, jsData=None, preventDefault=True, profile=False):
    """
    Description:
    -----------
    Load the content of the file.

    This function will first use as underlying the drop method to get the file dropped.

    Attributes:
    ----------
    :param jsFncs: List. The Javascript series of functions
    :param jsData: A datamap objection of a dictionary
    :param preventDefault: Boolean. Prevent default on the JavaScript event
    :param profile: Boolean. Profiling
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return self.drop(['''
      var reader = new FileReader(); var f = data[data.length - 1];
       reader.onloadstart = function() {%s};
       reader.onload = (function(value) {
          return function(e){data = atob(e.target.result.replace(/^data:.+;base64,/, '')); %s}})(f);
       reader.readAsDataURL(f);
      ''' % (JsUtils.jsConvertFncs([self.loading()], toStr=True), JsUtils.jsConvertFncs(jsFncs + [self.text.build(events.file.description)], toStr=True),
             )], jsData=jsData, preventDefault=preventDefault, profile=profile)

  def paste(self, jsFncs, profile=False, source_event=None):

    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return super(DropFile, self).paste([self.loading()]+jsFncs+[self.text.build("Bespoke data Loaded")], profile, source_event)

  def __str__(self):
    if self.options.format == 'json':
      return '''
        <div %(strAttr)s>
          %(container)s
          %(text)s
          <input id="%(htmlCode)s_report" style="display:none;"/>
        </div>
        ''' % {'htmlCode': self.htmlCode, 'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()),
               'container': self.container.html(), 'text': self.text.html()}

    return '''
      <div %(strAttr)s>
        <div style='display:inline-block'>using %(delimiter)s delimiter (<i>TAB for tabulation</i>)%(paste)s</div>
        %(container)s
        %(text)s
        <input id="%(htmlCode)s_report" style="display:none;"/>
      </div>
      ''' % {'htmlCode': self.htmlCode, 'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()),
             'paste': self.icon.html(),
             'container': self.container.html(), 'text': self.text.html(), 'delimiter': self.delimiter.html()}
