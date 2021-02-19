#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os

from epyk.core.html import Html
from epyk.core.html.options import OptText

from epyk.core.html import Defaults as Default_html
from epyk.core.css import Defaults as Default_css

# The list of Javascript classes
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.html import JsHtml
from epyk.core.css.styles import GrpCls


class Label(Html.Html):
  name = 'Label'

  def __init__(self, report, text=None, color=None, align=None, width=None, height=None, htmlCode=None, tooltip=None,
               profile=None, options=None):
    text = text or []
    if not isinstance(text, list):
      text = [text]
    for obj in text:
      if hasattr(obj, 'options'):
        obj.options.managed = False
    super(Label, self).__init__(report, text, css_attrs={"width": width, "height": height, 'color': color, 'text-align': align},
                                htmlCode=htmlCode, profile=profile)
    self.__options = OptText.OptionsText(self, options or {})
    self.css({'margin': '0 5px', 'float': 'left', 'display': 'inline-block', 'line-height': '23px',
              'vertical-align': 'middle', 'text-align': 'left'})
    if tooltip:
      self.set_attrs(name='title', value=tooltip)

  @property
  def id_html(self):
    """

    Usage:
    -----

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/API/Element/getElementsByTagName
    """
    return JsNodeDom.JsDoms.get("document.getElementById('%s')" % self.htmlCode)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    Usage:
    -----

    :rtype: OptText.OptionsText
    """
    return self.__options

  def click(self, js_funcs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------
    Add a click event for a component.

    The event will be automatically added to the onload section to be activated once the component
    has been build.

    Usage:
    -----

      select.label.click(str(page.js.console.log("test")))

    Related Pages:

      https://www.w3schools.com/js/js_htmldom_eventlistener.asp
      https://www.w3schools.com/jsref/event_onload.asp

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded

    :return: The htmlObj
    """
    self.css({"cursor": "pointer"})
    self.on("click", js_funcs, profile, source_event=source_event, onReady=onReady)
    return self

  def selectable(self, flag=False):
    """
    Description:
    ------------
    Make the label component not selectable.

    This will be done by adding the class CssTextNotSelectable to the component

    Usage:
    -----

    Attributes:
    ----------
    :param flag: Boolean.

    :return: self to allow the chains
    """
    if not flag:
      self.style.add_classes.text.no_selection()
    return self

  _js__builder__ = ''' 
      if (typeof data !== "undefined"){
        if(options.showdown){var converter = new showdown.Converter(options.showdown); 
        var content = converter.makeHtml(data).replace(/<\/?p[^>]*>/ig, '')}  else {var content = data}
        if(options._children > 0){htmlObj.insertAdjacentHTML('beforeend', '<div style="display:inline-block;vertical-align:middle">'+ content +'</div>')}
        else{htmlObj.innerHTML = content};
        if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}}'''
    
  def __str__(self):
    res = []
    for v in self.val:
      if hasattr(v, 'html'):
        res.append(v.html())
      else:
        if self.options.showdown:
          res.append(self._report.py.markdown.all(self.val))
        else:
          res.append(str(v))
    return '<label %s>%s</label>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(res), self.helper)


class Span(Html.Html):
  name = 'Span'

  def __init__(self, report, text="", color=None, align=None, width=None, height=None, htmlCode=None, tooltip=None,
               options=None, profile=None):
    super(Span, self).__init__(report, text, css_attrs={"width": width, "height": height, "color": color, 'text-align': align},
                               htmlCode=htmlCode, profile=profile)
    self.css({'line-height': '%spx' % Default_html.LINE_HEIGHT, 'margin': '0 5px', 'display': 'inline-block', 'vertical-align': 'middle'})
    self.__options = OptText.OptionsText(self, options)
    if tooltip is not None:
      self.tooltip(tooltip)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    Usage:
    -----

    :rtype: OptText.OptionsText
    """
    return self.__options

  @property
  def id_container(self):
    return self.htmlCode

  @property
  def id_jquery(self):
    return JsNodeDom.JsDoms.get("$('#%s')" % self.htmlCode)

  @property
  def id_html(self):
    """
    Description:
    ------------

    Usage:
    -----

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/API/Element/getElementsByTagName

    """
    return JsNodeDom.JsDoms.get("document.getElementById('%s')" % self.htmlCode)

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, report=self._report)
    return self._dom

  def click(self, js_funcs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------
    Add a click event for a component

    The event will be automatically added to the onload section to be activated once the component
    has been build

    Usage:
    -----

      select.label.click(str(page.js.console.log("test")))

    Related Pages:

      https://www.w3schools.com/js/js_htmldom_eventlistener.asp
      https://www.w3schools.com/jsref/event_onload.asp

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item).
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.

    :return: The htmlObj
    """
    self.css({"cursor": "pointer"})
    self.on("click", js_funcs, profile, source_event, onReady)
    return self

  _js__builder__ = ''' 
      if(options.showdown){var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data)} 
      if(options._children > 0){htmlObj.appendChild(document.createTextNode(data))}
      else{htmlObj.innerHTML = data}'''

  def __str__(self):
    val = self._report.py.markdown.all(self.val) if self.options.showdown else self.val
    return '<span %s>%s</span>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), val, self.helper)


class Position(Span):

  def digits(self, flag):
    """
    Description:
    ------------
    Specify if the count should be done from the commas

    Usage:
    -----

    Attributes:
    ----------
    :param flag: Boolean (default false)
    """
    self._jsStyles["digits"] = flag
    return self

  def position(self, index, style):
    """
    Description:
    ------------
    Set the CSS format for a specific character at a given position

    Usage:
    -----

    Attributes:
    ----------
    :param index: Integer. A number
    :param style: Dictionary. The CSS Style to be used
    """
    self._jsStyles.setdefault("positions", {})[index] = style
    return self

  _js__builder__ = ''' htmlObj.innerHTML = ""; 
        var prevCursor = 0; var content = ""+ data; var shift = 0;
        if (options.digits === true){ shift = content.indexOf(".") + 1; }
        if (typeof options.positions !== 'undefined'){
          const keys = Object.keys(options.positions).sort();
          keys.forEach(function(k){
            var cursor = parseInt(k) + shift;
            var span = document.createElement("span");
            span.innerHTML = content.slice(prevCursor, cursor);
            span.style.display = "inline-block";
            htmlObj.appendChild(span);
            
            var span2 = document.createElement("span");
            span2.innerHTML = content.slice(cursor, cursor+1);
            span2.style.display = "inline-block";
            Object.keys(options.positions[k]).forEach(function(key){
                span2.style[key] = options.positions[k][key]});
            htmlObj.appendChild(span2);
            prevCursor = cursor+1;
          });
          if (content.length > prevCursor){
            var span = document.createElement("span");
            span.innerHTML = content.slice(prevCursor, content.length);
            span.style.display = "inline-block";
            htmlObj.appendChild(span);
          }
        }
        '''

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<span %s>%s</span>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val, self.helper)


class Text(Html.Html):
  name = 'Text'

  def __init__(self, report, text, color, align, width, height, htmlCode, tooltip, options, helper, profile):
    super(Text, self).__init__(report, text, css_attrs={"color": color, "width": width, "height": height},
                               htmlCode=htmlCode, profile=profile)
    self.add_helper(helper)
    self.__options = OptText.OptionsText(self, options)
    #self._jsStyles = {"reset": self.options.reset, "markdown": self.options.markdown, "maxlength": self.options.limit_char}
    self.css({'text-align': align})
    if tooltip is not None:
      self.tooltip(tooltip)

  def click(self, js_funcs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------
    Add a click event on the text component.
    The style of the mouse on the component will be changed to make the event more visible

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item).
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.style.css.cursor = 'pointer'
    if "data-group" in self.attr:
      return super(Text, self).click(js_funcs + ["document.querySelectorAll('[data-group=%s]').forEach(function(dom){dom.classList.remove('%s')})" % (self.attr["data-group"], self.dom.classList.style_select), self.dom.classList.select()], profile, source_event, onReady)

    return super(Text, self).click(js_funcs, profile, source_event, onReady)

  def goto(self, url, js_funcs=None, profile=False, name="_blank", source_event=None, onReady=False):
    """
    Description:
    -----------
    Click event which redirect to another page.

    Usage:
    -----

    Attributes:
    ----------
    :param url:
    :param js_funcs: List | String. The Javascript Events triggered before the redirection.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param name: String. Optional.
    :param source_event: String. Optional. The event source.
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.js.location.open_new_tab(url, name))
    return self.click(js_funcs, profile, source_event, onReady)

  @property
  def val(self):
    """
    Description:
    ------------
    Property to get the jquery value of the HTML object in a python HTML object.
    This method can be used in any jsFunction to get the value of a component in the browser.
    This method will only be used on the javascript side, so please do not consider it in your algorithm in Python

    Usage:
    -----

    :returns: Javascript string with the function to get the current value of the component
    """
    return self._vals

  @val.setter
  def val(self, val):
    self._vals = val

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button.

    Usage:
    -----

    :rtype: OptText.OptionsText
    """
    return self.__options

  def editable(self):
    """
    Description:
    ------------
    Change the component properties to be editable if double clicked

    Usage:
    -----

      page.ui.text("This is a text").editable()

    :return: Self to allow the chaining
    """
    self.style.add_classes.text.content_editable()
    self.set_attrs({"contenteditable": "false", "ondblclick": "this.contentEditable=true;this.className='inEdit'",
                    "onblur": "this.contentEditable=false;this.className=''"})
    return self

  def write(self, timer=50):
    """
    Description:
    ------------
    Add a typing effect on this text

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/howto/howto_js_typewriter.asp

    Attributes:
    ----------
    :param timer: Integer. The speed for the typing effect
    """
    value = self.val
    self.val = ""
    self._report.body.onReady([
      self._report.js.objects.string(value, varName="%s_writer" % self.htmlCode, setVar=True),
      self._report.js.objects.number(0, varName="%s_pos" % self.htmlCode, setVar=True),
      self.build(""),
      self._report.js.window.setInterval([
        self._report.js.if_(self._report.js.objects.number.get("window.%s_pos" % self.htmlCode) < self._report.js.objects.string.get("window.%s_writer" % self.htmlCode).length, [
            self._report.js.objects.number(self._report.js.objects.number.get("window.%s_pos" % self.htmlCode) + 1, varName="window.%s_pos" % self.htmlCode, setVar=True),
            self.dom.append(self._report.js.objects.string.get("window.%s_writer" % self.htmlCode).charAt(self._report.js.objects.number.get("window.%s_pos" % self.htmlCode)), new_line=False)
          ]).else_(self._report.js.window.clearInterval("%s_interval" % self.htmlCode))
      ], "%s_interval" % self.htmlCode, timer)
    ])
    return self

  _js__builder__ = '''
      var content = data;
      if(options.reset){htmlObj.innerHTML = ""}; 
      if(data != ''){ 
        if(options.showdown){var converter = new showdown.Converter(options.showdown); content = converter.makeHtml(data)} 
        if((options.maxlength != undefined) && (data.length > options.maxlength)){
          content = data.slice(0, options.maxlength); 
          if(options.markdown){htmlObj.innerHTML = content +"..."} else {htmlObj.innerHTML = content +"..."}; 
          htmlObj.title = data} 
        else{
          if(options.markdown){htmlObj.innerHTML = content} else {htmlObj.innerHTML = content}}};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}};
      '''

  def __str__(self):
    if self.options.markdown:
      # Delegate to the JavaScript builder
      self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
      return '<div %s></div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)

    return '<div %s>%s</div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.content, self.helper)


class Pre(Html.Html):
  name = 'Pre formatted text'

  def __init__(self, report, vals, color, width, height, htmlCode, dataSrc, options, helper, profile):
    super(Pre, self).__init__(report, vals, htmlCode=htmlCode, css_attrs={"width": width, 'height': height, 'color': color},
                              profile=profile)
    self.__options = OptText.OptionsText(self, options)
    self.css({"text-align": 'left'})
    self.add_helper(helper)

  @property
  def dom(self):
    """
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, report=self._report)
    return self._dom

  def selectable(self, flag=False):
    """
    Description:
    ------------
    Make the label component not selectable.

    This will be done by adding the class CssTextNotSelectable to the component

    Usage:
    -----

    Attributes:
    ----------
    :param flag: Boolean.

    :return: self to allow the chains
    """
    if not flag:
      self.style.add_classes.text.no_selection()
    return self

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    Usage:
    -----

    :rtype: OptText.OptionsText
    """
    return self.__options

  _js__builder__ = '''
        if(options.showdown){var converter = new showdown.Converter(options.showdown); htmlObj.innerHTML = converter.makeHtml(data)} 
        else{htmlObj.innerHTML = data}'''

  def __str__(self):
    val = self._report.py.markdown.all(self.val) if self.options.showdown else self.val
    return '<pre %s>%s</pre>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), val, self.helper)


class Paragraph(Html.Html):
  name = 'Paragraph'

  def __init__(self, report, text, color, background_color, border, width, height, htmlCode, encoding, dataSrc, helper, options, profile):
    tmpText = []
    if not isinstance(text, list):
      content = []
      for line in text.strip().split("\n"):
        content.append(line.strip())
      text = [" ".join(content)]
    for t in text:
      cssStyles = re.search(" css\{(.*)\}", t)
      jsAttr = {}
      if cssStyles is not None:
        content = t.replace(cssStyles.group(0), '').decode(encoding) if hasattr(t, 'decode') else t.replace(cssStyles.group(0), '')
        tmpText.append(content)
        for cssAttr in cssStyles.group(1).split(","):
          cssKey, cssVal = cssAttr.split(":")
          jsAttr[cssKey.strip()] = cssVal.strip()
      else:
        if hasattr(t, 'decode'):
          tmpText.append(t.decode(encoding))
        else:
          tmpText.append(t)
      options["classes"].append(jsAttr)
    super(Paragraph, self).__init__(report, tmpText, htmlCode=htmlCode, css_attrs={'color': color, "width": width,
           "height": height, "background-color": background_color}, profile=profile)
    self.add_helper(helper)
    self.__options = OptText.OptionsText(self, options)
    if border:
      self.css('border', '1px solid %s' % self._report.theme.greys[9])
    self.css({'text-align': 'justify', 'margin-top': '3px', "text-justify": 'distribute'})

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for a button

    Usage:
    -----

    :rtype: Options
    """
    return self.__options

  _js__builder__ = '''
      if (typeof options.reset === 'undefined' || options.reset){htmlObj.innerHTML = ''};
      if (typeof data === 'string' || data instanceof String){data = data.split('\\n')}; 
      if(typeof data !== 'undefined'){
      data.forEach(function(line, i){
        if(options.showdown){var converter = new showdown.Converter(options.showdown); line = converter.makeHtml(line)} 
        var p = document.createElement('p'); p.innerHTML = line;
        htmlObj.appendChild(p)})}
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}
      '''

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, report=self._report)
    return self._dom

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class BlockQuote(Html.Html):
  name = 'Block quotation'

  def __init__(self, report, text, author, color, width, height, htmlCode, helper, options, profile):
    super(BlockQuote, self).__init__(report, {'text': text, 'author': author}, htmlCode=htmlCode, profile=profile,
                                     css_attrs={"width": width, "height": height, 'color': color, "white-space": 'nowrap'})
    self.add_helper(helper)
    self.__options = OptText.OptionsText(self, options)

  _js__builder__ = '''var div = htmlObj.querySelector('div'); div.innerHTML = '';
        data.text.split("\\n").forEach(function(rec) {
          if(options.showdown){var converter = new showdown.Converter(options.showdown); rec = converter.makeHtml(rec)} 
          var p = document.createElement("p"); p.style.margin = 0; p.style.padding = 0; p.innerHTML = rec; div.appendChild(p) });
        if(data.author != null){htmlObj.querySelector('div:last-child').innerHTML = '<small>by '+ data.author +'<cite></cite></small>'}'''

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '''
      <blockquote %s>
          <div style="padding:5px;border-left:2px solid %s"></div>
          <div style="text-align:right"></div>
      </blockquote>%s''' % (self.get_attrs(pyClassNames=self.style.get_classes()), self._report.theme.colors[3], self.helper)


class Title(Html.Html):
  name = 'Title'

  def __init__(self, report, text, level, name, contents, color, picture, icon, marginTop, htmlCode, width,
               height, align, options, profile):

    css_styles = re.search(" css\{(.*)\}", text)
    if css_styles is not None:
      text = text.replace(css_styles.group(0), '')
      for cssAttr in css_styles.group(1).split(","):
        css_key, css_val = cssAttr.split(":")
        options[css_key.strip()] = css_val.strip()
    super(Title, self).__init__(report, text, htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptText.OptionsTitle(self, options)
    self._name, self.level, self.picture = name, level, picture
    self.add_icon(icon, htmlCode=self.htmlCode, family=options.get("icon_family"))
    if contents is not None:
      self._name = contents.add(text, level or 1, name)
    if level is not None and level < 5:
      getattr(self.style.add_classes.text, "title_%s" % level)()
      self.css({'color': color, 'margin': '%spx 0 5px 0' % marginTop, 'font-size': Default_css.font({1: 8, 2: 6, 3: 4, 4: 2}[level])})
    else:
      self.style.add_classes.text.title()
      self.css({'margin': '%spx 0 5px 0' % marginTop, 'font-size': Default_css.font(5)})
    if align == 'center':
      self.css({'margin': '5px auto 10px auto', 'display': 'block', 'text-align': 'center'})
    elif align is not None:
      self.css({'margin': '5px auto 10px auto', 'display': 'block', 'text-align': align})
    else:
      self.css({'display': 'block', "margin-right": "10px"})
    if hasattr(report, '_content_table') and not report._content_table.options.manual and self.__options.content_table:
      report._content_table.add_title(self, level=level)

  @property
  def style(self):
    """
    Description:
    ------------

    Usage:
    -----

    :rtype: GrpCls.ClassHtmlEmpty
    """
    if self._styleObj is None:
      self._styleObj = GrpCls.ClassHtmlEmpty(self)
    return self._styleObj

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    Usage:
    -----

    :rtype: OptText.OptionsTitle
    """
    return self.__options

  _js__builder__ = '''
      if(options.showdown){var converter = new showdown.Converter(options.showdown); htmlObj.innerHTML = converter.makeHtml(data)} else{htmlObj.innerHTML = data}
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def click(self, js_funcs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------
    Add a click event for a component

    The event will be automatically added to the onload section to be activated once the component
    has been build


    Usage:
    -----

      select.label.click(str(page.js.console.log("test")))

    Related Pages:

      https://www.w3schools.com/js/js_htmldom_eventlistener.asp
      https://www.w3schools.com/jsref/event_onload.asp

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item).
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.

    :return: The htmlObj
    """
    self.css({"cursor": "pointer"})
    return super(Title, self).click(js_funcs, profile, source_event, onReady)

  def __str__(self):
    anchor_name = ' name="%s"' % self._name if self._name is not None else ''
    val = self._report.py.markdown.all(self.val) if self.options.showdown else self.val
    if self.picture is not None:
      path = Default_html.SERVER_PATH or os.path.split(self.picture)[0]
      return '<div %s><img src="%s/%s" />&nbsp;<a%s></a>%s%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), path, self.picture, anchor_name, val, self.helper)

    return '<div %s><a%s></a>%s%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), anchor_name, val, self.helper)


class Numeric(Html.Html):
  name = 'Number'
  requirements = ('accounting', )

  def __init__(self, report, number, title, label, icon, color, tooltip, htmlCode, options, helper, width, profile):
    super(Numeric, self).__init__(report, number, htmlCode=htmlCode, profile=profile, css_attrs={"width": width, "color": color})
    # Add the components label and icon
    self.add_label(label, css={"float": "none", "width": 'auto', 'margin-right': '10px'}, htmlCode=self.htmlCode)
    self.add_icon(icon, htmlCode=self.htmlCode, family=options.get("icon_family"))
    self.add_helper(helper, css={"line-height": '20px'})
    self.add_title(title, level=4, css={"margin-bottom": 0, "margin-right": 0, "padding": 0}, options={'content_table': False})

    # Update the CSS Style of the component
    self.css({'text-align': 'center', 'display': 'inline-block'})
    self.tooltip(tooltip)
    self.__options = OptText.OptionsNumber(self, options)

  def money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", format="%s%v"):
    """
    Description:
    -----------
    Format any number into currency

    Usage:
    -----

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param symbol: String. custom symbol
    :param digit: Integer. Number of digit
    :param thousand_sep: String. The thousand separator
    :param decimal_sep: String. The decimal separator
    """
    self.options.symbol = symbol
    self.options.format = format
    self.options.digit = digit
    self.options.thousand_sep = thousand_sep
    self.options.decimal_sep = decimal_sep
    return self

  def number(self, digits=0, thousand_sep=',', decimal_sep=","):
    """
    Description:
    -----------
    Format a number with custom precision and localisation

    Usage:
    -----

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digits: Integer. Number of digit
    :param thousand_sep: String. The thousand separator
    :param decimal_sep:
    """
    self._jsStyles["type_number"] = "number"
    self.options.digits = digits
    self.options.thousand_sep = thousand_sep
    self.options.decimal_sep = decimal_sep
    return self

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlNumeric
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlNumeric(self, report=self._report)
    return self._dom

  def to(self, number, timer=1):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param number:
    :param timer: Integer. the spped of the increase in millisecond
    """
    self._report.body.onReady([
      self._report.js.objects.number(self.val, varName="%s_counter" % self.htmlCode, setVar=True),
      self._report.js.window.setInterval([
        self._report.js.if_(
          self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) < number, [
            self._report.js.objects.number(
              self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) + 1,
              varName="window.%s_counter" % self.htmlCode, setVar=True),
            self.build(self._report.js.objects.number.get("window.%s_counter" % self.htmlCode))
          ]).else_(self._report.js.window.clearInterval("%s_interval" % self.htmlCode))
      ], "%s_interval" % self.htmlCode, timer)
    ])
    return self

  def click(self, js_funcs, profile=False, source_event=None, onReady=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event:
    :param onReady:
    """
    self.style.css.cursor = "pointer"
    self.style.add_classes.div.border_hover()
    return super(Numeric, self).click(js_funcs, profile, source_event, onReady)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    Usage:
    -----

    :rtype: OptText.OptionsNumber
    """
    return self.__options

  _js__builder__ = '''
      if (options.type_number == 'money'){ htmlObj.querySelector('font').innerHTML = accounting.formatMoney(data, options.symbol, options.digits, options.thousand_sep, options.decimal_sep, options.format) }
      else { htmlObj.querySelector('font').innerHTML = accounting.formatNumber(data, options.digits, options.thousand_sep, options.decimal_sep) }      
      '''

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<div %s><font style='vertical-align:middle;height:100%%;padding:0;margin:0;display:inline-block'>%s</font>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val, self.helper)


class Highlights(Html.Html):
  name = 'Highlights'
  requirements = ('bootstrap', )

  def __init__(self, report, text, title, icon, type, color, width, height, htmlCode, helper, options, profile):
    super(Highlights, self).__init__(report, text, css_attrs={"width": width, "height": height}, htmlCode=htmlCode, profile=profile)
    self.add_helper(helper)
    self.color = color if color is not None else self._report.theme.greys[-1]
    # Add the components title and icon
    self.add_title(title, css={"width": "none", "font-weight": 'bold', 'margin-top': 0}, options={'content_table': False})
    self.add_icon(icon, {"float": "left", 'padding-top': '3px', "color": 'inherit'}, htmlCode=self.htmlCode, family=options.get("icon_family"))
    if self.icon is not None and self.icon != "" and self.title:
      self.icon.style.css.font_factor(10)
    # Change the style of the component
    self.css({"margin": "5px 0", 'padding': "5px"})
    self.style.css.font_factor(5)
    self.attr['class'].add('alert alert-%s' % type)
    self.set_attrs(name='role', value="alert")
    self.dom.display_value = "block"

  _js__builder__ = '''
      if(typeof data === 'undefined'){htmlObj.remove()}
      else {htmlObj.querySelector('div[name=content]').innerHTML = data} '''

  def __str__(self):
    return '''
      <div %s>
        <span aria-hidden='true' style='float:right;font-size:25px;cursor:pointer' onclick='this.parentNode.remove()'>&times;</span>
        <div name='content'>%s</div></div>%s
    ''' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val, self.helper)


class Fieldset(Html.Html):
  name = 'Fieldset'

  def __init__(self, report, legend, width, height, helper, options, profile):
    super(Fieldset, self).__init__(report, legend, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self.css({'padding': '5px', 'border': '1px groove %s' % self._report.theme.greys[3], 'display': 'block', 'margin': '5px 0'})
    self.__options = OptText.OptionsText(self, options)

  _js__builder__ = '''htmlObj.firstChild.innerHTML = data; 
      if(typeof options.css !== 'undefined'){Object.keys(options.css).forEach(function(key){htmlObj.firstChild.style[key] = options.css[key]})}'''

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    Usage:
    -----

    :rtype: OptText.OptionsText
    """
    return self.__options

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.options.managed = False  # Has to be defined here otherwise it is set to late
    self.components[htmlObj.htmlCode] = htmlObj
    return self

  def __getitem__(self, id):
    if isinstance(id, int) and id not in self.components:
      return list(self.components.items())[id][1]

    return self.components[id]

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.components.values()])
    val = self._report.py.markdown.all(self.val) if self.options.showdown else self.val
    return '<fieldset %s><legend style="width:auto">%s</legend>%s</fieldset>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), val, str_div, self.helper)
