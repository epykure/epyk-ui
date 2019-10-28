"""
Wrapper to the different complex text HTML components
"""

import re
import json

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls
from epyk.core.css.groups import CssGrpClsText
from epyk.core.css.groups import CssGrpClsTable


class UpDown(Html.Html):
  name, category, callFnc = 'Up and Down', 'Texts', 'updown'
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, rec, size, color, label, options, helper, profile):
    if rec is None:
      rec = {'value': 0, 'previous': 0}
    if label is not None:
      rec["label"] = label
    super(UpDown, self).__init__(report, rec, profile=profile)
    self.add_helper(helper)
    self.vals['color'] = self.getColor('colors', 9) if color is None else color
    self.size, self._jsStyles = size[0], options
    self.css({'font-size': "%s%s" % (size[0], size[1])})

  @property
  def val(self): return '$("#%s span").html()' % self.jqId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''htmlObj.empty();
      var delta = data.value - data.previous; 
      if(data.previous == 0) {var relMove = 'N/A'} else{var relMove = 100 * ((data.value - data.previous) / data.previous)};
      if(data.digits == undefined){data.digits = 0};
      if(data.label != undefined){htmlObj.append("<span style='padding:5px;font-size:%(size)spx'>"+ data.label +"</span>")};
      if (delta < 0){
        htmlObj.append("<span style='padding:5px'>"+ %(value)s +"</span>");
        htmlObj.append("<span style='padding:5px;color:%(redColor)s;font-size:%(size)spx'>("+ %(delta)s +")</span>");
        htmlObj.append("<span style='padding:5px;color:%(redColor)s;font-size:%(size)spx'>("+ %(relMove)s +"%%)</span>");
        htmlObj.append("<i class='fas fa-arrow-down' aria-hidden='true' style='color:%(redColor)s;font-size:%(size)spx'></i>")}
      else{
        htmlObj.append("<span style='padding:5px'>"+ %(value)s +"</span>");
        htmlObj.append("<span style='padding:5px;color:%(greenColor)s;font-size:%(size)spx'>(+"+ %(delta)s +")</span>");
        htmlObj.append("<span style='padding:5px;color:%(greenColor)s;font-size:%(size)spx'>("+ %(relMove)s +"%%)</span>");
        htmlObj.append("<i class='fas fa-arrow-up' aria-hidden='true' style='color:%(greenColor)s;font-size:%(size)spx'></i>")}
      ''' % {"greenColor": self.getColor("success", 1), "redColor": self.getColor("danger", 1), "size": self.size - 2,
             'value': self._report.js.number("data.value", isPyData=False).toFormattedNumber(
              decPlaces=self._report.js.number("jsStyles.decPlaces", isPyData=False),
              thouSeparator=self._report.js.number("jsStyles.thouSeparator", isPyData=False),
              decSeparator=self._report.js.number("jsStyles.decSeparator", isPyData=False)),
             'delta': self._report.js.number("delta", isPyData=False).toFormattedNumber(
               decPlaces=self._report.js.number("jsStyles.decPlaces", isPyData=False),
               thouSeparator=self._report.js.number("jsStyles.thouSeparator", isPyData=False),
               decSeparator=self._report.js.number("jsStyles.decSeparator", isPyData=False)),
             'relMove': self._report.js.number("relMove", isPyData=False).toFormattedNumber(decPlaces=2)})

  def __str__(self):
    return '<div %s></div>%s' % (self.strAttr(pyClassNames=self.defined), self.helper)


class TextBubble(Html.Html):
  name, category, callFnc = 'Bubble text', 'Rich', 'textbubble'
  _grpCls = CssGrpClsText.CssClassTextBubble

  def __init__(self, report, recordSet, width, height, color, size, background_color, helper, profile):
    super(TextBubble, self).__init__(report, recordSet, width=width[0], widthUnit=width[1], height=height[0],
                                     heightUnit=height[1], profile=profile)
    self.add_helper(helper)
    self.color = self.getColor('greys', 0) if color is None else color
    self.background_color = self.getColor('success', 1) if background_color is None else background_color
    self.size = size
    self.css({'text-align': 'center', 'background-color': self.getColor('greys', 0)})

  @property
  def val(self):
    if 'url' in self.vals is None:
      return '$("#%s > div").first().find("div").html()' % self.htmlId

    return '$("#%s > div").first().find("a").html()' % self.htmlId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      htmlObj.find('div').first().empty(); htmlObj.find('div').first().append(data.value); 
      if (data.url != undefined){htmlObj.find('div').last().find('a').attr('href', data.url)} 
      else {htmlObj.find('div').last().find('a').attr('href', '#')};
      if (data.color != undefined) {htmlObj.find('div').last().find('a').css('color', data.color)}
      else {htmlObj.find('div').last().find('a').css('color', '%(color)s')}
      htmlObj.find('div').last().find('a').html(data.title)''' % {"color": self.getColor("colors", -1)})

  def __str__(self):
    return '''
      <div %(strAttr)s>
        <div %(clsTag)s style="vertical-align:middle;background-color:%(bgcolor)s;font-size:%(size)s;color:%(color)s"></div>
        <div class="py_csstitle"><a style="text-decoration:none"></a></div>%(helper)s
      </div>''' % {"strAttr": self.strAttr(pyClassNames=self.defined), "clsTag": self._report.style.getClsTag(self.defined.clsAltMap),
                   'bgcolor': self.background_color, 'size': "%s%s" % (self.size[0], self.size[1]), 'color': self.color,
                   'helper': self.helper}


class BlockText(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Block text', 'Rich', 'blocktext'
  _grpCls = CssGrpClsText.CssClassTextBlock

  def __init__(self, report, recordSet, color, size, border, width, height, helper, profile):
    super(BlockText, self).__init__(report, recordSet, width=width[0], widthUnit=width[1], height=height[0],
                                     heightUnit=height[1], profile=profile)
    self.size = size[0]
    self.add_helper(helper)
    self.color = color if color is not None else self.getColor('colors', 9)
    self._jsStyles = {"reset": True, 'markdown': True}
    self.css({'color': self.color, 'padding': '5px'})
    if border != 'auto':
      self.css('border', str(border))

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      htmlObj.find('div').first().html(data.title); htmlObj.find('div').last().empty(); var content;
      if (typeof data.text === 'string' || data.text instanceof String) {content = data.text.split("\\n")}
      else {content = data.text}
      content.forEach(function(line){htmlObj.find('div').last().append('<p class="py_csstext">'+ line +'</a>')});
      htmlObj.find('div').last().html(%(markUp)s(data.text));
      if (data.color != undefined) {htmlObj.find('div').last().css('color', data.color)};
      if(typeof data.button != 'undefined'){
        htmlObj.find("a").html(data.button.text); htmlObj.find("a").attr('href', data.button.url)}
      ''' % {"markUp": self._report.js.fncs.markUp})

  def __str__(self):
    items = ['<div %s>' % self.strAttr(pyClassNames=self.defined)]
    items.append('<div id="%s_title" %s style="font-size:%spx;text-align:left"><a class="anchorjs-link"></a></div>' % (self.htmlId, self._report.style.getClsTag(['CssTitle']), self.size+3))
    items.append('<div id="%s_p" %s style="color:%s:font-size:%spx;width:100%%;text-justify:inter-word;text-align:justify;"></div>' % (self.htmlId, self._report.style.getClsTag(['CssText']), self.color, self.size))
    if self.vals.get('button') is not None:
      items.append('<a href="#" %s><i></i></a>' % (self._report.style.getClsTag(['CssHrefNoDecoration', 'CssButtonBasic'])))
    items.append('</div>')
    return ''.join(items)


class TextWithBorder(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Text with Border and Icon', 'Rich', 'textborder'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, recordSet, width, height, size, align, helper, profile):
    super(TextWithBorder, self).__init__(report, recordSet, width=width[0], widthUnit=width[1], height=height[0],
                                   heightUnit=height[1], profile=profile)
    self.size = size[0]
    self.add_helper(helper)
    self.align = align
    if not 'colorTitle' in self.vals:
      self.vals['colorTitle'] = self.getColor('colors', 9)
    if not 'color' in self.vals:
      self.vals['color'] = self.getColor('colors', 9)
    self.css({"border-color": self.vals['colorTitle'], 'margin-top': '20px', 'font-size': '%s%s' % (size[0], size[1])})

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      htmlObj.find('legend').html(data.title); htmlObj.find('span').html(data.value)''')

  @property
  def jqId(self): return "$('#%s fieldset')" % self.htmlId

  def __str__(self):
    item = ['<div %s>' % self.strAttr(pyClassNames=self.defined)]
    item.append('<fieldset style="color:%s">' % self.vals['color'])
    if 'icon' in self.vals:
      self.vals['align'] = self.align
      item.append('<i class="%(icon)s fa-5x" style="width:100%%;text-align:%(align)s;margin:2px 0 10px 0;color:%(color)s"></i>' % self.vals)
    if 'url' in self.vals:
      item.append('<legend style="font-size:%spx;color:%s"></legend><span></span><br><a style="float:right" href="%s">+ more details</a></fieldset>' % (self.size + 10, self.vals['colorTitle'], self.vals['url']) )
    else:
      item.append('<legend style="font-size:%spx;color:%s"></legend><span></span></fieldset>' % (self.size + 10, self.vals['colorTitle']))
    item.append('%s</div>' % self.helper)
    return "".join(item)


class Vignet(Html.Html):
  name, category, callFnc = 'Vignet', 'Rich', 'vignet'
  _grpCls = CssGrpClsText.CssClassTextVignet
  __reqCss, __reqJs = ['font-awesome', 'jqueryui'], ['font-awesome', 'jquery']

  def __init__(self, report, records, width, height, size, colorTitle, options, helper, profile):
    super(Vignet, self).__init__(report, records, width=width[0], widthUnit=width[1], height=height[0],
                                 heightUnit=height[1], profile=profile)
    self.add_helper(helper)
    if not 'color' in self.vals:
      self.vals['color'] = 'inherit'
    self.size, self._jsStyles = size, options
    self.css({"padding-left": "5px", "color": colorTitle if colorTitle is not None else 'inherit', "margin-top": "20px"})

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      if (data.urlTitle != undefined || data.urlTitle != null){htmlObj.find('div').find('p').first().html('<a href="'+ data.urlTitle +'" style="text-decoration:none;color:%(blackColor)s">'+ %(title)s +'</a>')}
      else{htmlObj.find('div').find('p').first().html(%(title)s)};
      htmlObj.find('div').find('p').eq(2).html(data.value);
      if(data.url != undefined || data.url != null){htmlObj.find('div').find('p').last().html('<a href="'+ data.url +'" style="text-decoration:none;color:%(blackColor)s">'+ %(number)s +'</a>')}
      else{htmlObj.find('div').find('p').last().html(%(number)s)};
      if(data.tooltip != undefined){htmlObj.find('div').find('p').last().tooltip()};
      if(data.text != undefined){htmlObj.find('p').last().html(%(content)s)}
      ''' % {"blackColor": self.getColor('greys', 9), 'number': self._report.js.number("data.number", isPyData=False).toFormattedNumber(
        decPlaces=self._report.js.number("jsStyles.decPlaces", isPyData=False),
        thouSeparator=self._report.js.number("jsStyles.thouSeparator", isPyData=False),
        decSeparator=self._report.js.number("jsStyles.decSeparator", isPyData=False)),
      'content': self._report.js.number("data.text", isPyData=False).toStringMarkup(),
      'title': self._report.js.number("data.title", isPyData=False).toStringMarkup()})

  def figureClick(self, jsData='data'):
    """
    Add on click function to update the number variable if need be

    :return:
    """
    self._report.jsOnLoadFnc.add("""
      $('#%(htmlId)s').find('div').find('p').last().on('click', function (event){
        var data = %(htmlId)s_data;
        if (data.url != undefined) {data.number++; $(this).html('<a href="'+ data.url +'">'+ data.number +'</a>')}              
      })""" % {"htmlId": self.htmlId, 'data': jsData})

  def __str__(self):
    items = ["<div %s>" % (self.strAttr(pyClassNames=self.defined))]
    tooltip = ' title="%s"' % self.tooltip if self.tooltip is not None else ' '
    if 'icon' in self.vals:
      items.append('<div style="position:relative;float:left;font-size:3em"><i class="%(icon)s"></i></div>' % self.vals)
      items.append('<div ><p style="font-size:%spx;margin-left:50px;font-weight:bold"></p>' % (self.size[0] + 6))
      items.append('<p %s %s data-placement="bottom" style="color:%s;font-size:%spx;margin-left:50px;text-align:center;margin-top:-20px;"></p></div>' % (self._report.style.getClsTag(['CssText']), self.vals.get('tooltip', ''),
                                                                                                     self.vals['color'], self.size[0] + 30))
    else:
      items.append('<div ><p %s style="font-size:%spx;margin-left:50px;font-weight:bold"></p>' % (self._report.style.getClsTag(['CssSubTitle']), self.size + 6))
      items.append('<p %s style="color:%s;font-size:%spx;margin-left:50px;text-align:center;margin-top:-20px;"></p></div>' % (self._report.style.getClsTag(['CssText']), self.vals['color'], self.size[0] + 30))
    items.append('<p %s style="font-size:%spx;margin-top:-10px;"></p>%s</div>' % (tooltip, "%s%s" % (self.size[0], self.size[1]), self.helper))
    return "".join(items)


class Delta(Html.Html):
  _grpCls = CssGrpCls.CssGrpClassBase
  __reqCss, __reqJs = ['font-awesome', 'bootstrap'], ['font-awesome', 'jqueryui', 'bootstrap'] # bootstrap for progressbar
  name, category, callFnc = 'Delta Figures', 'Rich', 'delta'

  def __init__(self, report, records, width, height, size, options, helper, profile):
    super(Delta, self).__init__(report, records, width=width[0], widthUnit=width[1], height=height[0],
                                heightUnit=height[1], profile=profile)
    self.add_helper(helper)
    self.size = int(self._report.pyStyleDfl['fontSize'][:-2]) if size is None else size
    if not 'color' in self.vals:
      self.vals['color'] = self.getColor('colors', 9)
    if not 'thresold1' in self.vals:
      self.vals['thresold1'] = 100
    if not 'thresold2' in self.vals:
      self.vals['thresold2'] = 50
    self.css({"color": self.vals['color']})
    self._jsStyles = options

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
       var htmlId = htmlObj.attr('id');
       var variation = 100 * (data.number - data.prevNumber) / data.prevNumber;
       var warning = ''; var currVal = %(number)s; 
       if(variation > data.thresold1) { warning = '<i style="color:%(recColod)s;" title="'+ variation +' increase" class="fas fa-exclamation-triangle"></i>&nbsp;&nbsp;' ;};
       if(data.url != null) {currVal = '<a style="text-decoration:none;color:'+ data.color +'" href="' + data.url+ '">'+ currVal +'</a>'}
       if(data.label != undefined){currVal = data.label +" "+ currVal};
       $("#"+ htmlId +"_progress").progressbar({value: variation});
       if(variation > data.thresold1){$("#"+ htmlId +"_progress").children().css({'background': 'Red' })} 
       else if(variation > data.thresold2){ $("#"+ htmlId +"_progress").children().css({'background': 'Orange'})} 
       else{$("#"+ htmlId +"_progress").children().css({'background': 'LightGreen'})}
       htmlObj.find('div').first().html(warning + currVal);
       htmlObj.find('div').last().html('Previous number: '+ %(prev_number)s);
      ''' % {"recColod": self.getColor('danger', 1), 'number': self._report.js.number("data.number", isPyData=False).toFormattedNumber(
        decPlaces=self._report.js.number("jsStyles.decPlaces", isPyData=False),
        thouSeparator=self._report.js.number("jsStyles.thouSeparator", isPyData=False),
        decSeparator=self._report.js.number("jsStyles.decSeparator", isPyData=False)),
             'prev_number': self._report.js.number("data.prevNumber", isPyData=False).toFormattedNumber(
        decPlaces=self._report.js.number("jsStyles.decPlaces", isPyData=False),
        thouSeparator=self._report.js.number("jsStyles.thouSeparator", isPyData=False),
        decSeparator=self._report.js.number("jsStyles.decSeparator", isPyData=False))})

  def __str__(self):
    return '''<div %(strAttr)s>
      <div style="width:100%%;text-align:right;font-size:%(size)spx;"></div>
      <div id="%(htmlId)s_progress" style="height:10px;color:%(color)s"></div>
      <div style="font-size:10px;font-style:italic;color:%(greyColor)s;padding-bottom:5px;text-align:left"></div>
      %(helper)s
      </div>''' % {"strAttr": self.strAttr(pyClassNames=self.defined), "size": self.size+12, 'htmlId': self.htmlId, "color": self.vals['color'],
                   "greyColor": self.getColor("greys", 6), "helper": self.helper}

  @staticmethod
  def matchMarkDown(val):
    return True if val.startswith("@delta ") else None

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report=None):
    curr, prev = val[6:].split(':')
    if report is not None:
      getattr(report, cls.callFnc)({'number': float(curr), 'prevNumber': float(prev)})
    return ["report.%s( {'number': %s, 'prevNumber': %s} )" % (cls.callFnc, float(curr,), float(prev))]

  @classmethod
  def jsMarkDown(self, vals): return "@delta %s:%s" % (vals['number'], vals['prevNumber'])


class DocScript(Html.Html):
  """
  Python Wrapper for a Static view of the scripts

  This interface is a bit special in the way it is supposed to interact with the production code.
  Indeed it will:
    - In production read a text file and display the data that will be produced from the system (Python, R, ....)
    - In test mode try to get it from the code directly using a REST Service

  Security checks are done in the script to ensure they are TAGS as open
  """
  docTypes = set(['documentation', 'code'])
  _grpCls = CssGrpCls.CssGrpClassBase
  __reqCss, __reqJs = ['font-awesome', 'bootstrap'], ['font-awesome', 'jquery']
  name, category, callFnc = 'Script Documentation', 'Text', 'doc'

  def __init__(self, report, title, scriptName, clssName, functionName, docType, color, size):
    if not docType in self.docTypes:
      raise Exception('The docType %s does not exist' % docType)

    clssName = clssName if clssName is not None else 'NOT_SET'
    super(DocScript, self).__init__(report, {'title': title, 'clssName': clssName, 'functionName': functionName,
                                             'docType': docType, 'scriptName': scriptName.replace('.py', '')})
    self.size = self._report.pyStyleDfl['fontSize'] if size is None else "%spx" % size
    self.color = self.getColor('colors', -1) if color is None else color

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, '''
      var request = "/reports/doc/"+ data.docType +"/"+ data.scriptName +"/"+ data.clssName +"/"+ data.functionName;
      if(data.functionName == ''){request = "/reports/doc/"+ data.docType +"/"+ data.scriptName +"/"+ data.clssName};
      $.post(request, function(data){JSON.parse(data).forEach(function(rec){htmlObj.find('pre').append('<code>'+ rec +'</code><br />')})})''')

  def __str__(self):
    label = "from script <b>%s</b>" % self.vals['scriptName']
    if self.vals['clssName'] != 'NOT_SET':
      label = "%s, class <b>%s</b>" % (label, self.vals['clssName'])
    if self.vals['functionName'] != '':
      label = "%s, function <b>%s</b>" % (label, self.vals['functionName'])
    return '''
      <div %s>
        <div style="color:%s;font-size:%s;font-weight:bold;">%s</div>
        <pre style="padding:5px"></pre>
        <span style="font-style:italic;width:100%%;text-align:right;display:block;margin-top:-15px">%s</span>
      </div> ''' % (self.strAttr(pyClassNames=self.defined), self.color, self.size, self.vals['title'], label)


class Prism(Html.Html):
  __reqCss, __reqJs = ['prism'], ['prism', 'jqueryui']
  name, category, callFnc = 'Code Viewer', 'Rich', 'prism'

  def __init__(self, report, vals, language, size, width, height, isEditable, trimSpaces, align, helper, profile):
    super(Prism, self).__init__(report, vals, width=width[0], widthUnit=width[1], height=height[0],
                                heightUnit=height[1], profile=profile)
    self.isEditable = isEditable
    self.trimSpaces = trimSpaces
    self.css({'font-size': "%s%s" % (size[0], size[1])})
    self.addClass('language-%s' % language)
    if align == 'center':
      self.css('margin', 'auto')

  def __str__(self):
    copy = self._report.ui.icons.awesome("fas fa-clipboard", tooltip="Copy to clipboard")
    copy.click(
      '''if (window.clipboardData) { window.clipboardData.setData('Text', %(vals)s)} 
         else {
            var $temp = $("<textarea>"); $("body").append($temp); $temp.val(%(vals)s).select();
            document.execCommand("copy"); $temp.remove()};         
          $('body').append("<div id='info' style='position:fixed;left:50;bottom:10px;z-index:100;background:#293846;padding:10px;color:%(whiteColor)s'>Data copied to clipboard</div>"); 
          $('#info').fadeOut(6000, function() { $('#info').remove()}) 
          ''' % {"vals": json.dumps(self.vals), 'whiteColor': self.getColor("greys", 0)})
    copy.html()
    if self.trimSpaces:
      content = "".join(['<code style="width:100%%;">%s</code><br />' % line.strip() for line in self.vals.split("\n")])
    else:
      content = "".join(['<code style="width:100%%;">%s</code><br />' % line for line in self.vals.split("\n")])
    return '''
      <div %(strAttr)s> 
        <table style="table-layout: fixed;width:100%%" id="%(htmlId)s_code">
          <tr>
            <td style="width:100%%;overflow:auto;vertical-align:top">
              <div contenteditable="%(isEditable)s" style="width:100%%;overflow:auto;display:block;margin-top:0">
                <pre>%(content)s</pre>%(helper)s
              </div>
            </td>
          </tr>
        </table>
        <div style="display:inline-block;margin:0;padding:0;width:100%%;text-align:right"><p style="display:inline:block;float:right;width:80px;white-space:nowrap;cursor:pointer" onclick="$('#%(htmlId)s_code').toggle()">[hide / show]</p></div>
      </div>''' % {"strAttr": self.strAttr(), "copy": copy.html(), "isEditable": self.isEditable,
                   "content": content, "helper": self.helper, "htmlId": self.htmlId}

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDownBlock(data):
    return re.match("```", data[0])

  @staticmethod
  def matchEndBlock(data):
    return data.endswith("```")

  @classmethod
  def convertMarkDownBlock(cls, data, report=None):
    language = data[0].replace("```", "").strip()
    if report is not None:
      getattr(report, 'prism')("\n".join(data[1:-1]), language)
    return ["report.prism('%s', '%s')" % ("\n".join(data[1:-1]).replace("'", '"'), language)]

  @classmethod
  def jsMarkDown(self, vals):
    return ["```", vals, "```"]

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    from docx.oxml.ns import nsdecls
    from docx.oxml import parse_xml

    table = document.add_table(rows=1, cols=1)
    table.style = 'TableGrid'
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "\n%s\n" % self.vals
    shading_elm_1 = parse_xml(r'<w:shd %s w:fill="F4F4F4"/>' % (nsdecls('w')))
    hdr_cells[0]._tc.get_or_add_tcPr().append(shading_elm_1)


class Formula(Html.Html):
  __reqJs = ['mathjs']
  name, category, callFnc = 'Latex Formula', 'Texts', 'formula'
  _grpCls = CssGrpClsText.CssClassText

  def __init__(self, report, text, size, width, color, helper, profile):
    super(Formula, self).__init__(report, text, width=width[0], widthUnit=width[1], profile=profile)
    self.color = color if color is not None else self.getColor('greys', 9)
    self.css({'color': self.color, 'font-size': "%s%s" % (size[0], size[1])})
    self.add_helper(helper)
    #self._report.jsGlobal.addJs("MathJax.Hub.Config({tex2jax: {inlineMath: [['$', '$'], ['\\(', '\\)']]}})")

  @property
  def val(self):
    return '%s.html()' % self.jqId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, '''htmlObj.html(data)''')

  def __str__(self):
    return '<font %s></font>%s' % (self.strAttr(pyClassNames=self.defined), self.helper)

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val): return True if val.startswith("$$") and val.strip().endswith("$$") else None

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report):
    if report is not None:
      getattr(report, 'formula')(val.strip())
    return ["report.formula('%s')" % val.strip()]

  @classmethod
  def jsMarkDown(self, vals): return vals


class TrafficLight(Html.Html):
  name, category, callFnc = 'Light', 'Rich', 'light'
  _grpCls = CssGrpCls.CssGrpClassBox

  def __init__(self, report, color, label, height, tooltip, helper, profile):
    # Small change to allow the direct use of boolean and none to define the color
    # Those standards will simplify the creation of themes going forward
    super(TrafficLight, self).__init__(report, color, width=height[0], widthUnit=height[1], height=height[0],
                                       heightUnit=height[1], profile=profile)
    self.add_helper(helper)
    self.add_label(label, css={"width": 'auto', 'height': 'auto', "margin-left": "%s%s" % (height[0], height[1])})
    self.css({'border-radius': '50px', 'background-color': self.vals, 'display': 'block'})
    self.addAttr("title", tooltip)
    self._jsStyles = {'red': self.getColor('danger', 1), 'green': self.getColor('success', 1), 'orange': self.getColor('warning', 1)}
    if tooltip is not None:
      self.tooltip(tooltip)

  def jsColor(self, color):
    """
    Function to change the color of the component from an event

    This should be used in a Javascript event

    Example
    l = rptObj.ui.rich.light("red")
    button.click(l.jsColor("blue"))

    :param color: A color code

    :return: The javascript string corresponding to the action of changing the color
    """
    return "%s.css('background-color', '%s')" % (self.jqId, color)

  @property
  def val(self):
    """
    Function to return the value of the component

    Example
    myObj.val

    :return: The javascript string to get the component value
    """
    return "%s.css('background-color')" % self.jqId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      if (data === false){htmlObj.css('background-color', jsStyles.red)}
      else if (data === true){htmlObj.css('background-color', jsStyles.green)}
      else if (data === null){htmlObj.css('background-color', jsStyles.orange)}
      else {htmlObj.css('background-color', data)}''')

  def __str__(self):
    return '<div %s></div>%s' % (self.strAttr(pyClassNames=self.defined), self.helper)

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val): return re.match("-\(\((.*)\)\)-", val)

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report=None):
    if report is not None:
      getattr(report, cls.callFnc)(regExpResult.group(1))
    return ["report.%s('%s')" % (regExpResult.group(1), cls.callFnc)]

  @classmethod
  def jsMarkDown(self, val):
    return "-((%s))-" % val


class ContentsTable(Html.Html):
  name, category, callFnc = 'Contents Table', None, 'contents'
  _grpCls = CssGrpClsTable.CssClassTableContent

  def __init__(self, report, recordSet, width, height, profile):
    recordSet = [] if recordSet is None else recordSet
    self.indices, self.first_level, self.entries_count, self.ext_links = [], None, 0, {}
    super(ContentsTable, self).__init__(report, recordSet, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                                        profile=profile)

  def add(self, text, level, name=None):
    if self.first_level is None:
      self.first_level = level
    adjLevel = level - self.first_level + 1
    self.indices.append( adjLevel)
    if name is None:
      name = self.entries_count
    self.vals.append({'text': text, 'level': adjLevel, 'name': name})
    self.entries_count += 1
    return name

  def add_link(self, text, level, script_name, report_name=None, name=None):
    """
    Add an external link in the content table

    Example

    :param text: THe text of the line
    :param level: The level of the link in the contents table
    :param script_name: The underlying script to point to
    :param report_name: The name of the folder
    :param name:

    :return:
    """
    self.ext_links[self.entries_count] = {"scriptName": script_name, "folderName": report_name if report_name is not None else self._report.run.report_name}
    self.add(text, level, name)

  def __str__(self):
    entries = []
    for i, v in enumerate(self.vals):
      try:
        css_cls_name = 'CssHrefContentLevel%(level)s' % v
        self._report.style.cssCls(css_cls_name)
        v['classname'] = self._report.style.cssName(css_cls_name)
      except:
        raise Exception("Missing css class CssHrefContentLevel%(level)s" % v)

      if i in self.ext_links:
        v.update(self.ext_links[i])
        entries.append("<a href='/reports/run/%(folderName)s/%(scriptName)s' target='_blank' class='%(classname)s'>%(text)s</a>" % v)
      else:
        entries.append("<a href='#%(name)s' class='%(classname)s'>%(text)s</a>" % v)
    self.addGlobalFnc("ChangeContents(src, htmlId)", '''
        $("#contents_vals_"+ htmlId).toggle() ;
        if( $("#contents_vals_"+ htmlId).css('display') == 'none'){
          $(src).text("Show"); $("#contents_title_"+ htmlId).css( "text-align", 'left')}
        else{$(src).text("Hide") ;$("#contents_title_"+ htmlId).css( "text-align", 'center')}''')
    return '''
      <div %(attr)s>
        <div id='contents_title_%(htmlId)s' style="text-align:center;margin-bottom:10px;font-size:16px;font-weight:bold">Contents [<a href='#' onclick='ChangeContents(this, "%(htmlId)s")' >hide</a>] </div>
        <div id='contents_vals_%(htmlId)s'>%(contents)s</div>
      </div> ''' % {'attr': self.strAttr(pyClassNames=self.defined), 'contents': "<br />".join(entries), 'htmlId': self.htmlId}
