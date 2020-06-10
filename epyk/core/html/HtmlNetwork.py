"""
All those components are a bit special as they would require to work properly:
  - A server in order to interact dynamically
  - A database source

This can definition be configured but by default it is using the ones of the server.
"""

from epyk.core.html import Html
from epyk.core.html.options import OptNet

from epyk.core.js.objects import JsComponents
from epyk.core.js import JsUtils

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


class DropFile(Html.Html):
  requirements = ('font-awesome',)
  name, inputType = 'Drop File Area', "file"

  def __init__(self, report, vals, tooltip, options, profile):
    super(DropFile, self).__init__(report, vals, profile=profile)
    self.__options = OptNet.OptionFiles(self, options)
    self.tooltip(tooltip, location='bottom')
    self.css({"display": "inline-block", "width": '100%', 'text-align': 'center', 'margin': '0 5px',
              'border': "1px dashed %s" % report.theme.colors[-1]})

  @property
  def options(self):
    """
    Description:
    ------------
    Specific options for the files components

    :rtype: OptNet.OptionFiles
    """
    return self.__options

  def transfert(self, url, jsFncs, preventDefault=True, profile=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param url:
    :param jsFncs:
    :param preventDefault:
    :param profile:
    """

  def drop(self, jsFncs, preventDefault=True, profile=False):
    """
    Description:
    -----------
    Add a drag and drop property to the element

    Usage::

    Attributes:
    ----------
    :param jsFncs:
    :param preventDefault: Boolean.
    :param profile:

    :return: Return self to allow the chaining
    """
    dft_fnc = ""
    if preventDefault:
      dft_fnc = self._report.js.objects.event.preventDefault()
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    str_fncs = JsUtils.jsConvertFncs(["var data = %s" % self._report.js.objects.event.dataTransfer.files] + jsFncs, toStr=True)
    self.attr["ondragover"] = "(function(event){%s})(event)" % dft_fnc
    self.on("drop", ["%s; %s; return false" % (dft_fnc, str_fncs)])
    return self

  def drop2(self, url=None, jsData=None, jsFncs=None, httpCodes=None, isPyData=True, refresh=True, extensions=None):
    data = []
    if jsFncs is None:
      jsFncs = [self._report.jsReloadPage()]
    elif not isinstance(jsFncs, list):
      jsFncs = [jsFncs]

    if jsData is not None:
      for rec in jsData:
        if isinstance(rec, tuple):
          if isPyData:
            data.append("data.append('%s', %s)" % (rec[0], json.dumps(rec[1])))
          else:
            data.append("data.append('%s', %s)" % (rec[0], rec[1]))
        else:
          data.append("data.append('%s', %s)" % (rec.htmlCode, rec.val))
    super(DropFile, self).drop('''
      event.originalEvent.preventDefault(); event.originalEvent.stopPropagation();
      var files = event.originalEvent.dataTransfer.files; var data = new FormData();
      $.each(event.originalEvent.dataTransfer.files, function(i, file) { 
        var fileExt = '.' + file.name.split('.').pop();
        if(%(extensions)s == null) {data.append(file.name, file)} else {
          if(%(extensions)s.indexOf(fileExt) >= 0) { data.append(file.name, file)}}});
      %(jsData)s; %(ajax)s''' % {"jsData": ";".join(data), "extensions": json.dumps(extensions),
                                 "ajax": self._report.jsAjax(url, success=";".join(jsFncs) if refresh else '' ) })
    return self

  def __str__(self):
    return '''
      <div %(strAttr)s>
        <b><i class="fas fa-cloud-upload-alt" style="font-size:20px"></i>&nbsp;&nbsp;</b>
      </div>
      <input id="%(htmlCode)s_report" style="display:none;"/>
      ''' % {'htmlCode': self.htmlCode, 'strAttr': self.get_attrs(pyClassNames=self.style.get_classes())}
