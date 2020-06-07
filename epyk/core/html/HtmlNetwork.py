"""
All those components are a bit special as they would require to work properly:
  - A server in order to interact dynamically
  - A database source

This can definition be configured but by default it is using the ones of the server.
"""

from epyk.core.html import Html
from epyk.core.html.options import OptNet

from epyk.core.js.objects import JsComponents

# The list of CSS classes
from epyk.core.css.styles import GrpClsNetwork


class Comments(Html.Html):
  name = 'Comment'

  def __init__(self, report, recordSet, width, height, htmlCode, options, profile):
    super(Comments, self).__init__(report, recordSet, css_attrs={"width": width, 'height': height}, htmlCode=htmlCode, profile=profile)
    self.__options = OptNet.OptionsChat(self, options)
    self.css({'padding': '5px'})
    self.input = None
    if not self.options.readonly:
      self.input = report.ui.input()
      self.input.options.managed = False
      self.input.style.css.text_align = 'left'
      self.input.enter([self.js.add(self.input.dom.content)])

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

  def __str__(self):
    return '''
      <div %(attr)s>
        <span><p style="display:inline-block;margin:0;padding:0;cursor:pointer" id="%(htmlCode)s_comms_count">0</p> Comments <i style="margin:0 5px 0 20px;cursor:pointer;display:inline-block" class="fas fa-sort-amount-up"></i>Sort by</span>
        %(inputTag)s
        <div class='scroll_content' style="margin:0;padding:5px 0;overflow:auto">
          <div id="%(htmlCode)s_comms"></div>
        </div>
      </div>
      ''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'htmlCode': self.htmlCode,
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


class Chat(Html.Html):
  name = 'Chat'

  def __init__(self, report, recordSet, width, height, htmlCode, options, profile):
    super(Chat, self).__init__(report, recordSet, css_attrs={"width": width, 'height': height}, htmlCode=htmlCode, profile=profile)
    self.__options = OptNet.OptionsChat(self, options)
    self.css({'padding': '5px'})
    self.input = None
    if not self.options.readonly:
      self.input = report.ui.input()
      self.input.options.managed = False
      self.input.style.css.text_align = 'left'
      self.input.enter([self.js.add(self.input.dom.content)])

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

  def __str__(self):
    return '''
      <div %(attr)s>
        %(inputTag)s
        <div style="margin:0;padding:5px 0;height:%(height)spx;overflow:auto"></div>
      </div>
      ''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'htmlCode': self.htmlCode, 'height': int(self.css("height")[:-2]) - 70,
             'inputTag': '' if self.input is None else self.input.html()}


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

  def subscribe(self, socket, channel, jsFncs=None):
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
    :param jsFncs: List. Optional. The other Javascript functions to be triggered
    """
    jsFncs = jsFncs if jsFncs is not None else []
    self.onReady([socket.on(channel, [self.build(socket.message['data'])] + jsFncs)])
    return self

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

  def subscribe(self, socket, channel, jsFncs=None):
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
    :param jsFncs: List. Optional. The other Javascript functions to be triggered
    """
    jsFncs = jsFncs if jsFncs is not None else []
    self.onReady([socket.on(channel, [self.build(socket.message['data'])] + jsFncs)])
    return self

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.style.get_classes())
