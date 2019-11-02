"""
Wrapper to the different basic text HTML components
"""

import re
import os
import json

from epyk.core.html import Html
from epyk.core.js.objects import JsNodeDom
from epyk.core.js import JsUtils

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls
from epyk.core.css.groups import CssGrpClsText


class Label(Html.Html):
  name, category, callFnc = 'Label', 'Text', 'label'

  def __init__(self, report, text, size, color, align, width, height, htmlCode, tooltip, profile):
    super(Label, self).__init__(report, text, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                                code=htmlCode, profile=profile)
    self.color = color if color is not None else 'inherit'
    self.css({'color': self.color, 'font-size': "%s%s" % (size[0], size[1]) if size[0] is not None else 'inherit', 'text-align': align})
    self.css({'margin': '0 5px', 'float': 'left', 'display': 'inline-block'})
    if tooltip:
      self.addAttr('title', tooltip)

  @property
  def id_container(self):
    return self.htmlId

  @property
  def id_jquery(self):
    return JsNodeDom.JsDoms.get("$('#%s')" % self.htmlId)

  @property
  def id_html(self):
    """

    Documentation
    https://developer.mozilla.org/fr/docs/Web/API/Element/getElementsByTagName

    :return:
    """
    return JsNodeDom.JsDoms.get("document.getElementById('%s')" % self.htmlId)

  def click(self, jsFncs):
    """
    Add a click event for a component

    The event will be automatically added to the onload section to be activated once the component
    has been build

    Example
    select.label.click(str(rptObj.js.console.log("test")))

    Documentation
    https://www.w3schools.com/js/js_htmldom_eventlistener.asp
    https://www.w3schools.com/jsref/event_onload.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js
    :return: The htmlObj
    """
    self.css({"cursor": "pointer"})
    self._report.js.addOnLoad([self.dom.onclick(jsFncs)])
    return self

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, "htmlObj.html(data)")
    
  def __str__(self):
    return '<label %s>%s</label>%s' % (self.strAttr(pyClassNames=self.pyStyle), self.vals, self.helper)


class Span(Html.Html):
  name, category, callFnc = 'Label', 'Text', 'label'

  def __init__(self, report, text, size, color, align, width, height, htmlCode, tooltip, profile):
    super(Span, self).__init__(report, text, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                               code=htmlCode, profile=profile)
    self.color = color if color is not None else 'inherit'
    self.css({'color': self.color, 'font-size': "%s%s" % (size[0], size[1]) if size is not None else 'inherit', 'text-align': align})
    self.css({'margin': '0 5px', 'display': 'inline-block'})
    if tooltip is not None:
      self.tooltip(tooltip)

  @property
  def id_container(self):
    return self.htmlId

  @property
  def id_jquery(self):
    return JsNodeDom.JsDoms.get("$('#%s')" % self.htmlId)

  @property
  def id_html(self):
    """

    Documentation
    https://developer.mozilla.org/fr/docs/Web/API/Element/getElementsByTagName

    :return:
    """
    return JsNodeDom.JsDoms.get("document.getElementById('%s')" % self.htmlId)

  def click(self, jsFncs):
    """
    Add a click event for a component

    The event will be automatically added to the onload section to be activated once the component
    has been build

    Example
    select.label.click(str(rptObj.js.console.log("test")))

    Documentation
    https://www.w3schools.com/js/js_htmldom_eventlistener.asp
    https://www.w3schools.com/jsref/event_onload.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js
    :return: The htmlObj
    """
    self.css({"cursor": "pointer"})
    self._report.js.addOnLoad([self.dom.onclick(jsFncs)])
    return self

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, "htmlObj.html(data)")

  def __str__(self):
    return '<span %s>%s</span>%s' % (self.strAttr(pyClassNames=self.pyStyle), self.vals, self.helper)


class Text(Html.Html):
  _grpCls = CssGrpClsText.CssClassText
  name, category, callFnc = 'Text', 'Texts', 'text'

  def __init__(self, report, text, size, color, align, width, height, htmlCode, tooltip, options, helper, profile):
    super(Text, self).__init__(report, text, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                               code=htmlCode, profile=profile)
    self.color = color if color is not None else 'inherit'
    self.add_helper(helper)
    self._jsStyles = options
    self.css({'color': self.color, 'font-size': "%s%s" % (size[0], size[1]), 'text-align': align})
    if tooltip is not None:
      self.tooltip(tooltip)

  @property
  def val(self):
    """
    Property to get the jquery value of the HTML object in a python HTML object.
    This method can be used in any jsFunction to get the value of a component in the browser.
    This method will only be used on the javascript side, so please do not consider it in your algorithm in Python

    Example
    myObj.val

    :return: Javascript string with the function to get the current value of the component
    """
    return '%s.html()' % self.jqId

  def addStyles(self, reset=None, maxlength=None):
    """
    Add style properties to be used in the definition of the component in the Javascript layer

    :return: The object itself
    """
    if reset is not None:
      self._jsStyles['reset'] = reset
    if maxlength is not None:
      self._jsStyles['maxlength'] = maxlength
    return self

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      var content = data;
      if(jsStyles.reset){htmlObj.html("")}; 
      if(data != ''){ 
        if((jsStyles.maxlength != undefined) && (data.length > jsStyles.maxlength)){
          content = data.slice(0, jsStyles.maxlength); 
          var div = $("<div title='"+ data +"' data-html='true'>"+ %(markUp)s +"...</div>");
          htmlObj.append(div)} 
        else{
          var div = $("<div>"+ %(markUp)s +"</div>"); 
          htmlObj.append(div)}}''' % {"markUp": self._report.js.string("content", isPyData=False).toStringMarkup()})

  def toHtml(self):
    """
    Mandatory function for any child class of Html.
    Return the String representation of a Text HTML tag

    :returns: A String representing the HTML object
    """
    return str(self)

  def __str__(self):
    return '<div %s></div>%s' % (self.strAttr(pyClassNames=self.defined), self.helper)

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    """
    Add to the internal document object a word text section
    """
    document.add_paragraph(self.vals)


class Code(Html.Html):
  _grpCls = CssGrpCls.CssGrpClassBase
  name, category, callFnc = 'Code', 'Text', 'code'
  editable, scriptTitle = None, ''

  def __init__(self, report, vals, size, color, width, height, htmlCode, options, helper, profile):
    super(Code, self).__init__(report, vals, code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                               heightUnit=height[1], profile=profile)
    self.add_helper(helper)
    self._jsStyles = options
    self.color = color if color is not None else self.getColor("greys", 9)
    self.css({'color': self.color, 'display': 'block', 'font-size': "%s%s" % (size[0], size[1]), 'margin': '5px 0'})

  @property
  def val(self):
    return '%s.html()' % self.jqId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' htmlObj.empty();
      if(jsStyles.edit){
        htmlObj.append('<div style="position:relative;float:right;padding:2px 5px 2px 5px;cursor:pointer;background-color:%(blackColor)s;color:%(whiteColor)s">Edit</div>')}
      data.forEach(function(rec){htmlObj.append('<code>'+ rec +'</code><br />')})
      ''' % {"blackColor": self.getColor("greys", 9), "whiteColor": self.getColor("greys", 0)})

  def editable(self, urlPost, title=None):
    self.editable = urlPost
    self.scriptTitle = title

  def __str__(self):
    if self.editable is not None:
      self._report.jsOnLoadFnc.add(
        '''
        $('#%(htmlId)s div').on('click', function(event){
          %(jqId)s.empty();
          %(jqId)s.append('<span style="position:relative;float:right;padding:2px 5px 2px 5px;cursor:pointer;background-color:%(backGroundColor)s;color:%(whiteColor)s">Save</span>');
          %(jqId)s.attr('contenteditable','true'); %(jqId)s.css('padding', '0 0 0 5px');
          recordSet_%(htmlId)s.forEach(function(rec) { %(jqId)s.append(rec + "\\n")});
          %(jqId)s.append( "<br />");
          $('#%(htmlId)s span').on('click', function(event){
            var content = %(jqId)s.text();
            $.post("/%(url)s", {content: content.slice(4, content.length), title: '%(title)s'}, function(data){location.reload()})});   
          })''' % {'jqId': self.jqId, "url": self.editable, 'htmlId': self.htmlId, 'backGroundColor': self.getColor('colors', 5),
                   'whiteColor': self.getColor('greys', 0), 'title': self.scriptTitle})
    return '<div %s></div>%s' % (self.strAttr(pyClassNames=self.defined), self.helper)


class Pre(Html.Html):
  name, category, callFnc = 'Pre formatted text', 'Texts', 'preformat'

  def __init__(self, report, vals, size, color, width, height, htmlCode, dataSrc, options, helper, profile):
    super(Pre, self).__init__(report, vals, code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                              heightUnit=height[1], profile=profile, dataSrc=dataSrc)
    color = color if color is not None else self.getColor("greys", 9)
    self._jsStyles = options
    self.css({'color': color, 'font-size': "%s%s" % (size[0], size[1]), "text-align": 'left', "margin": "auto"})
    self.add_helper(helper)

    def append(text):
      return ";".join(JsUtils.jsConvertFncs("%s.append(%s)" % (self.jqId, JsUtils.jsConvertData(text, None))))

    self.js.append = append

  @property
  def val(self):
    return '%s.html()' % self.jqId

  def onDocumentLoadFnc(self):
    markdown = self._report.js.string("data", isPyData=False).toStringMarkup()
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
        htmlObj.empty(); if(jsStyles.markdown){htmlObj.html(%(markdown)s)} else{htmlObj.html(data)}''' % {"markdown": markdown})

  def __str__(self):
    return '<pre %s></pre>%s' % (self.strAttr(pyClassNames=self.defined), self.helper)


class Paragraph(Html.Html):
  _grpCls = CssGrpClsText.CssClassTextNoBorder
  name, category, callFnc = 'Paragraph', 'Texts', 'paragraph'

  def __init__(self, report, text, size, color, background_color, border, width, height, htmlCode, encoding, dataSrc,
               helper, profile):
    jsStyles, tmpText = {"reset": True, 'markdown': True, "style": []}, []
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
      jsStyles["style"].append(jsAttr)
    super(Paragraph, self).__init__(report, tmpText, code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                    heightUnit=height[1], dataSrc=dataSrc, profile=profile)
    self.add_helper(helper)
    self._jsStyles = jsStyles
    if border:
      self.css('border', '1px solid %s' % self.getColor("greys", 9))
    color = color if color is not None else 'inherit'
    background_color = background_color if background_color is not None else 'inherit'
    self.size = size[0]
    self.css({"background-color": background_color, 'text-align': 'justify', 'color': color,
              'font-size': '%s%s' % (size[0], size[1]), 'margin-top': '3px', "text-justify": 'distribute'})

  @property
  def val(self):
    self._report.jsOnLoadFnc.add('''
      function paraGrapVal(htmlId){
        var result = []; $('#'+ htmlId).find('p').each(function(){result.push($(this).html())});
        return result.join('\\n');}''')
    return "paraGrapVal('%s') " % self.htmlId

  def onDocumentLoadFnc(self):
    self._report.js.registerFunction('toMarkUp') # Add the toMarkUp predefined function
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      if (typeof jsStyles.reset === 'undefined' || jsStyles.reset){htmlObj.empty()};
      if (typeof data === 'string' || data instanceof String){data = data.split("\n")}; 
      data.forEach(function(line, i){
        var p = $("<p></p>").css(jsStyles.style[i]).html(JsMarkUp(line)); htmlObj.append(p)})''')

  def __str__(self):
    return '<div %s></div>%s' % (self.strAttr(pyClassNames=self.defined), self.helper)

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    p = document.add_paragraph(self.vals)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

  def to_xls(self, workbook, worksheet, cursor):
    """

    :param workbook:
    :param worksheet:
    :param cursor:
    :return:
    :link xlxWritter Documentation: https://xlsxwriter.readthedocs.io/format.html
    """
    worksheet.write(cursor['row'], 0, "\n".join(self.vals))
    cursor['row'] += 2


class BlockQuote(Html.Html):
  _grpCls = CssGrpCls.CssGrpClassBase
  name, category, callFnc = 'Block quotation', 'Texts', 'blockquote'

  def __init__(self, report, text, author, size, color, width, height, htmlCode, helper, profile):
    super(BlockQuote, self).__init__(report, {'text': text, 'author': author}, code=htmlCode, width=width[0],
                                     widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    self.css({'color': color if color is not None else self.getColor("greys", 9),
              'font-size': "%s%s" % (size[0], size[1]) if size[0] is not None else 'inherit',
              'display': 'inline-block', 'white-space': 'nowrap'})
    self.add_helper(helper)
    self._jsStyles = {"reset": True, 'markdown': True}

  @property
  def val(self):
    return "$('#%s > p').html() +' by '+ $('#%s cite').html()" % (self.htmlId, self.htmlId)

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      var div = htmlObj.find('div').first(); div.empty();
      data.text.split("\\n").forEach(function(rec) {div.append('<p style="margin:0;padding:0">'+ rec +'</p>')});
      if(data.author != null){htmlObj.find('div').last().html('<small>by '+ data.author +'<cite></cite></small>')}''')

  def __str__(self):
    return '''
      <blockquote %s>
          <div style="padding:5px;border-left:4px solid %s"></div>
          <div style="text-align:right"></div>
      </blockquote>%s''' % (self.strAttr(pyClassNames=self.defined), self.getColor('colors', 9), self.helper)

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDownBlock(data): return re.match(">>>Quote:(.*)", data[0])

  @staticmethod
  def matchEndBlock(data): return data.endswith("<<<")

  @classmethod
  def convertMarkDownBlock(cls, data, report):
    author = data[0].split(':')[-1]
    getattr(report, 'blockquote')("\n".join([val for val in data[1:-1]]), author)
    return ["report.blockquote(%s, '%s')" % (json.dumps([val for val in data[1:-1]]), author)]

  @classmethod
  def jsMarkDown(self, vals): return [">>>Quote:%s" % self.vals['author'], [rec for rec in vals['text']], "<<<"]


class Title(Html.Html):
  name, category, callFnc = 'Title', 'texts', 'title'
  _grpCls = CssGrpClsText.CssClassTitle

  def __init__(self, report, text, size, level, name, contents, color, picture, icon, marginTop, htmlCode, width,
               height, align, dflt_options, profile):
    cssStyles, jsStyles = re.search(" css\{(.*)\}", text), dflt_options
    if cssStyles is not None:
      text = text.replace(cssStyles.group(0), '')
      for cssAttr in cssStyles.group(1).split(","):
        cssKey, cssVal = cssAttr.split(":")
        jsStyles[cssKey.strip()] = cssVal.strip()
    super(Title, self).__init__(report, text, code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                heightUnit=width[1], profile=profile)
    self._jsStyles = jsStyles
    self._name, self.level, self.picture = name, level, picture
    self.add_icon(icon)
    if contents is not None:
      self._name = contents.add(text, level or 1, name)

    if level is not None:
      self.style.cssCls("CssTitle%s" % level)
      self.css({'color': color, 'margin': '%spx 0 5px 0' % marginTop})
    else:
      self.style.cssCls('CssTitle')
      self.css({'margin': '%spx 0 5px 0' % marginTop, 'font-size': "%s%s" % (size[0], size[1])})
      if size[0] > 21 and color is None:
        self.css('color', self.getColor('colors', 9))
      else:
        self.css('color', self.getColor('colors', -1) if color is None else color)
    if align == 'center':
      self.css({'margin': '5px auto 10px auto', 'display': 'block', 'text-align': 'center'})
    elif align is not None:
      self.css({'margin': '5px auto 10px auto', 'display': 'block', 'text-align': align})
    else:
      self.css({'display': 'inline-block'})

  @property
  def jqId(self):
    return "$('#%s a')" % self.htmlId

  @property
  def id_container(self):
    return self.htmlId

  @property
  def val(self):
    return "%s.html()" % self.jqId

  def onDocumentLoadFnc(self):
    markdown = self._report.js.string("data", isPyData=False).toStringMarkup()
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      if(jsStyles.markdown){htmlObj.html(%(markdown)s)} else{htmlObj.html(data)};
      if(typeof jsStyles.css !== 'undefined'){htmlObj.parent().css(jsStyles.css)}''' % {"markdown": markdown})

  def __str__(self):
    anchor_name = ' name="%s"' % self._name if self._name is not None else ''
    if self.picture is not None:
      path = "/img/%s" % self._report.run.report_name
      # Check if the file is available in the default directory
      # Otherwise raise an exception
      filePath = os.path.join(self._report.run.local_path, "static", self.picture)
      if not os.path.exists(filePath):
        raise Exception("Missing file %s in %s" % (self.picture, os.path.join(self._report.run.local_path, "static")))

      return '<div %s><img src="%s/%s" />&nbsp;<a%s></a>%s</div>' % (self.strAttr(pyClassNames=self.pyStyle), path, self.picture, anchor_name, self.helper)

    return '<div %s><a%s>%s</a></div>' % (self.strAttr(pyClassNames=self.defined), anchor_name, self.helper)

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val): return val.startswith("# ") or val.startswith("## ") or val.startswith("### ") or val.startswith("#### ")

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report=None):
    helper, infoData = re.search("epyk:info<(.*)>", val), None
    if helper is not None:
      infoData = helper.group(1)
      val = val.replace("epyk:info<%s>" % infoData, "")
    for i in range(1, 5):
      startIndex = i+1
      if val.startswith("%s " % "".join(["#"] * i)):
        if report is not None:
          title = getattr(report.ui.texts, cls.callFnc)(val[startIndex:], level=i)
          if infoData is not None:
            title.info(infoData)
        return ["report.ui.%s.title('%s', level=%s)" % (cls.category, val[startIndex:], i)]

    if report is not None:
      getattr(report.ui.texts, cls.callFnc)(val[2:])
    return ["report.ui.%s.%s('%s')" % (val[2:], cls.category, cls.callFnc)]

  @classmethod
  def jsMarkDown(cls, vals, level=None):
    if level == 1: return "# %s" % vals
    if level == 2: return "## %s" % vals
    if level == 3: return "### %s" % vals
    return "#### %s" % vals

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_ppt(self, document, currentSlide, newSlide=False):
    if newSlide:
      blankSlide = document.slide_layouts[6]
      currentSlide = document.slides.add_slide(blankSlide)
    textbox = currentSlide.shapes.add_textbox(0, 0, 100, 100)
    textbox.text_frame.text = self.vals
    return currentSlide

  def to_word(self, document):
    if self.level is not None:
      document.add_heading(self.vals, self.level)
    else:
      document.add_heading(self.vals)

  def to_xls(self, workbook, worksheet, cursor):
    """

    Documentation
    https://xlsxwriter.readthedocs.io/format.html

    :param workbook:
    :param worksheet:
    :param cursor:

    :return:
    """
    cell_format = workbook.add_format({'bold': True, 'font_color': self.color, 'font_size': self.size})
    worksheet.write(cursor['row'], 0, self.vals, cell_format)
    cursor['row'] += 2


class Numeric(Html.Html):
  name, category, callFnc = 'Number', 'Number', 'number'

  def __init__(self, report, number, label, icon, size, color, tooltip, htmlCode, options, helper, profile):
    super(Numeric, self).__init__(report, number, code=htmlCode, profile=profile)
    # Add the components label and icon
    self.add_label(label, css={"float": None, "width": 'none'})
    self.add_icon(icon)
    self.add_helper(helper)

    # Update the CSS Style of the component
    color = self.getColor('colors', -1) if color is None else color
    self.css({"color": color, 'font-size': "%s%s" % (size[0], size[1]) if size is not None else 'inherit'})
    self.tooltip(tooltip)
    self._jsStyles = options

  @property
  def jqId(self):
    return "$('#%s font')" % self.htmlId

  @property
  def id_container(self):
    return self.htmlId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__,
                      "%s.html(%s)" % (self.jqId, self.js.string("data", isPyData=False).toFormattedNumber(
                        decPlaces=self._report.js.number("jsStyles.decPlaces", isPyData=False),
                        thouSeparator=self._report.js.number("jsStyles.thouSeparator", isPyData=False),
                        decSeparator=self._report.js.number("jsStyles.decSeparator", isPyData=False))))

  def __str__(self):
    return "<div %s><font></font>%s</div>" % (self.strAttr(pyClassNames=self.defined), self.helper)


class Highlights(Html.Html):
  name, category, callFnc = 'Highlights', 'Texts', 'highlights'
  __reqCss, __reqJs = ['bootstrap'], ['bootstrap']

  def __init__(self, report, text, title, icon, type, size, color, width, height, htmlCode, helper, profile):
    super(Highlights, self).__init__(report, text, width=width[0], widthUnit=width[1], height=height[0],
                                     heightUnit=height[1], code=htmlCode, profile=profile)
    self.add_helper(helper)
    self.color = color if color is not None else self.getColor("greys", 9)
    # Add the components title and icon
    self.add_title(title, css={"width": "none", "font-weight": 'bold'})
    self.add_icon(icon, {"float": "left"})
    # Change the style of the component
    self.css({'font-size': "%s%s" % (size[0], size[1]) if size is not None else 'inherit', "margin": "5px"})
    self.addClass('alert alert-%s' % type)
    self.addAttr('role', "alert")

  @property
  def container(self):
    return self.dom

  def __str__(self):
    return "<div %s><div>%s</div></div>%s" % (self.strAttr(), self.vals, self.helper)


class SearchResult(Html.Html):
  name, category, callFnc = 'Search Result', 'Text', 'searchr'

  def __init__(self, report, recordSet, pageNumber, width, width_unit, height, height_unit):
    super(SearchResult, self).__init__(report, recordSet, width=width, widthUnit=width_unit, height=height, heightUnit=height_unit)
    self._jsStyles = {'title': {'color': self.getColor("colors", 7), 'font-size': '18px'}, 'dsc': {'color': self.getColor('greys', 6)},
                      'url': {'color': self.getColor("success", 1), 'font-size': '14px'}, 'visited': {'color': self.getColor('greys', 5)},
                      'link': {'color': self.getColor("colors", 7), 'cursor': 'pointer'}, 'pageNumber': pageNumber}

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles, currPage)" % self.__class__.__name__, ''' htmlObj.empty() ; 
      if (typeof currPage == 'undefined'){currPage = 0};
      var pageNumber = jsStyles.pageNumber;
      data.slice(currPage * pageNumber).forEach( function(rec){
        var newItem = $('<div style="margin:5px 10px 5px 10px;"></div>') ; 
        var title = $('<div>'+ rec['title'] + '</div>').css( jsStyles.title );
        if (rec['urlTitle'] != undefined){
          title.css({'cursor': 'pointer'});
          title.click(function(e){GoToReport(rec['urlTitle'], true, false)})}
        newItem.append(title);
        if (rec.icon != undefined){
          var item = $('<div></div>').css( jsStyles.url);
          item.append( $('<i class="'+ rec['icon'] +'" style="margin-right:5px"></i>')).append(rec['url']);
          newItem.append(item)} 
        else {newItem.append($('<div>'+ rec['url'] +'</div>').css(jsStyles.url))}
        newItem.append( $('<div>'+ rec['dsc'] +'</div>').css(jsStyles.dsc));
        if(rec.visited != undefined){newItem.append($('<div>'+ rec.visited +'</div>').css(jsStyles.visited))}
        if(rec.links != undefined){
          rec.links.forEach(function(link){ 
            if (link.url == undefined) {link.url = link.val};
            newItem.append($('<a href='+ link.url +' target="_blank">'+ link.val +'</a><br>').css(jsStyles.link))})};
        htmlObj.append(newItem);
      }); 
      if( data.length > 0) {
        var reste = data.length/ pageNumber; var currIndex = currPage+1;
        var roundRest = Math.trunc(reste);
        if (roundRest > reste) {reste ++};
        var paginate = $('<div style="display:inline-block;height:35px;padding:0;width:100%%;text-align:center;margin-top:10px" class="py_cssdivpagination"></div>');
        if (currIndex > 1){
          var href = $('<a href="#">&laquo;</a>');
          href.click({page: currPage-1, rec: data}, function(e){%(class)s(htmlObj, e.data.rec, jsStyles, e.data.page)});
          paginate.append(href)};
        for (var i = 0; i < reste; i++){
          var indexPage = i + 1;
          if (currPage == i) { 
            var href = $('<a href="#" style="background-color:%(greyColor)s;color:%(whiteColor)s">'+ indexPage +'</a>');
            href.click({page: i, rec: data}, function(e) { %(class)s(htmlObj, e.data.rec, jsStyles, e.data.page)});
            paginate.append(href)}
          else{
            var href = $('<a href="#">'+ indexPage +'</a>') ;
            href.click({page: i, rec: data}, function(e){%(class)s(htmlObj, e.data.rec, jsStyles, e.data.page)});
            paginate.append(href)}}
        if(currIndex < reste){
          var href = $('<a href="#">&raquo;</a>');
          href.click({page: currPage+1, rec: data}, function(e){%(class)s(htmlObj, e.data.rec, jsStyles, e.data.page)});
          paginate.append(href)};
        htmlObj.append(paginate)
      } ''' % {"breadCrumb": self._report.jsGlobal.breadCrumVar, "class": self.__class__.__name__,
               "greyColor": self.getColor("colors", 9), "whiteColor": self.getColor("greys", 0)})

  def __str__(self):
    self._report.style.cssCls('CssDivPagination')
    return '<div %s style="margin:5px 10px 5px 10px;"></div> ' % self.strAttr(pyClassNames=self.defined)


class Fieldset(Html.Html):
  name, category, callFnc = 'Fieldset', 'Texts', 'fieldset'

  def __init__(self, report, text, size, width, height, helper, profile):
    super(Fieldset, self).__init__(report, text, width=width[0], widthUnit=width[1], height=height[0],
                                   heightUnit=height[1], profile=profile)
    self.add_helper(helper)
    self.css({'padding': '5px', 'border': '1px groove %s' % self.getColor("greys", 3), 'display': 'block',
              'margin': '5px 0', 'font-size': "%s%s" % (size[0], size[1]) if size is not None else 'inherit'})

  def __str__(self):
    return '<fieldset %s><legend style="font-size:inherit">%s</legend>%s</fieldset>' % (self.strAttr(pyClassNames=self.defined), self.vals, self.helper)
