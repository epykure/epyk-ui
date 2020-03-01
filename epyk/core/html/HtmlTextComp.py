import re
import json

from epyk.core.html import Html
from epyk.core.css import Colors

# The list of CSS classes
from epyk.core.css import Defaults_css


class UpDown(Html.Html):
  name, category, callFnc = 'Up and Down', 'Texts', 'updown'
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']

  def __init__(self, report, rec, color, label, options, helper, profile):
    if rec is None:
      rec = {'value': 0, 'previous': 0}
    if label is not None:
      rec["label"] = label
    super(UpDown, self).__init__(report, rec, profile=profile)
    self.add_helper(helper)
    self.val['color'] = self._report.theme.colors[9] if color is None else color
    self._jsStyles = options

  @property
  def _js__builder__(self):
    return '''
      var delta = data.value - data.previous; 
      if(data.previous == 0) {var relMove = 'N/A'} else{var relMove = 100 * ((data.value - data.previous) / data.previous)};
      if(data.digits == undefined){data.digits = 0};
      if(data.label != undefined){htmlObj.append("<span style='padding:5px;font-size:%(size)spx'>"+ data.label +"</span>")};
      var valueElt = document.createElement('span');
      valueElt.setAttribute('style', 'padding:5px')
      valueElt.innerHTML = %(value)s;
      htmlObj.appendChild(valueElt);
      var deltaElt = document.createElement('span');
      var relMoveElt = document.createElement('span');
      var icon = document.createElement('i');
      if (delta < 0){
        deltaElt.setAttribute('style', 'padding:5px;color:%(redColor)s;font-size:%(size)s');
        deltaElt.innerHTML = "(+"+ %(delta)s +")";
        relMoveElt.setAttribute('style', 'padding:5px;color:%(redColor)s;font-size:%(size)s')
        relMoveElt.innerHTML = "("+ %(relMove)s +"%%)";
        icon.className = 'fas fa-arrow-down';
        icon.setAttribute('style', 'color:%(redColor)s;font-size:%(size)s')}
      else{  
        deltaElt.setAttribute('style', 'padding:5px;color:%(greenColor)s;font-size:%(size)s');
        deltaElt.innerHTML = "(+"+ %(delta)s +")";
        relMoveElt.setAttribute('style', 'padding:5px;color:%(greenColor)s;font-size:%(size)s')
        relMoveElt.innerHTML = "("+ %(relMove)s +"%%)";
        icon.className = 'fas fa-arrow-up';
        icon.setAttribute('style', 'color:%(greenColor)s;font-size:%(size)spx')};
      htmlObj.appendChild(deltaElt); htmlObj.appendChild(relMoveElt); htmlObj.appendChild(icon);
      ''' % {"greenColor": self._report.theme.success[1], "redColor": self._report.theme.danger[1], "size": Defaults_css.font(-2),
             'value': self._report.js.number("data.value", isPyData=False).toFormattedNumber(
              decPlaces=self._report.js.number("options.decPlaces", isPyData=False),
              thouSeparator=self._report.js.number("options.thouSeparator", isPyData=False),
              decSeparator=self._report.js.number("options.decSeparator", isPyData=False)),
             'delta': self._report.js.number("delta", isPyData=False).toFormattedNumber(
               decPlaces=self._report.js.number("options.decPlaces", isPyData=False),
               thouSeparator=self._report.js.number("options.thouSeparator", isPyData=False),
               decSeparator=self._report.js.number("options.decSeparator", isPyData=False)),
             'relMove': self._report.js.number("relMove", isPyData=False).toFormattedNumber(decPlaces=2)}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class TextBubble(Html.Html):
  name, category, callFnc = 'Bubble text', 'Vignets', 'bubble'
  # _grpCls = CssGrpClsText.CssClassTextBubble

  def __init__(self, report, recordSet, width, height, color, background_color, helper, profile):
    super(TextBubble, self).__init__(report, recordSet, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self.color = self._report.theme.greys[0] if color is None else color
    self.background_color = self._report.theme.success[1] if background_color is None else background_color
    self.height = height[0]
    self.css({'text-align': 'center', 'background-color': self._report.theme.greys[0]})

  @property
  def _js__builder__(self):
    return '''
      htmlObj.querySelectorAll('div')[0].innerHTML = data.value;
      var div_elements = htmlObj.querySelectorAll('div');  
      if (data.url != undefined){div_elements[div_elements.length - 1].querySelectorAll('a')[0].href = data.url} 
      else {div_elements[div_elements.length - 1].querySelectorAll('a')[0].href = '#'};
      if (data.color != undefined) {div_elements[div_elements.length - 1].querySelectorAll('a')[0].style.color = data.color}
      else {div_elements[div_elements.length - 1].querySelectorAll('a')[0].style.color = '%(color)s'}
      div_elements[div_elements.length - 1].querySelectorAll('a')[0].innerHTML = data.title
      ''' % {"color": self._report.theme.colors[-1]}

  def __str__(self):
    bubble_height = self.height - 20
    bubble_width = self.height - 20
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '''
      <div %(strAttr)s>
        <div %(clsTag)s style="padding-top:10px;width:%(width)spx;height:%(height)spx;vertical-align:middle;background-color:%(bgcolor)s"></div>
        <div "%(clsTitle)s"><a style="text-decoration:none"></a></div>%(helper)s
      </div>''' % {"strAttr": self.get_attrs(pyClassNames=self.style.get_classes()), "clsTag": ''# self._report.style.getClsTag(['CssDivBubble'], loadCls=True)
      , 'clsTitle': '' #self._report.style.getClsTag(['CssTitle'], loadCls=True)
      , 'bgcolor': self.background_color,
                   'helper': self.helper, 'height': bubble_height, 'width': bubble_width}


class BlockText(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Block text', 'Rich', 'blocktext'
  # _grpCls = CssGrpClsText.CssClassTextBlock

  def __init__(self, report, recordSet, color, border, width, height, helper, profile):
    super(BlockText, self).__init__(report, recordSet, css_attrs={'color': color, "width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self._jsStyles = {"reset": True, 'markdown': True}
    self.css({'padding': '5px'})
    if border != 'auto':
      self.css('border', str(border))

  @property
  def _js__builder__(self):
    mark_up = self._report.js.string("data.text", isPyData=False).toStringMarkup()
    return '''
      htmlObj.find('div').first().html(data.title); htmlObj.find('div').last().empty(); var content;
      if (typeof data.text === 'string' || data.text instanceof String) {content = data.text.split("\\n")}
      else {content = data.text}
      content.forEach(function(line){htmlObj.find('div').last().append('<p class="py_csstext">'+ line +'</a>')});
      htmlObj.find('div').last().html(%(markUp)s);
      if (data.color != undefined) {htmlObj.find('div').last().css('color', data.color)};
      if(typeof data.button != 'undefined'){
        htmlObj.find("a").html(data.button.text); htmlObj.find("a").attr('href', data.button.url)}
      ''' % {"markUp": mark_up}

  def __str__(self):
    items = ['<div %s>' % self.get_attrs(pyClassNames=self.style.get_classes())]
    items.append('<div id="%s_title" %s style="font-size:%spx;text-align:left"><a></a></div>' % (self.htmlId, self._report.style.getClsTag(['CssTitle']), Defaults_css.font(3)))
    items.append('<div id="%s_p" %s style="width:100%%;text-justify:inter-word;text-align:justify;"></div>' % (self.htmlId, self._report.style.getClsTag(['CssText'])))
    if self.val.get('button') is not None:
      items.append('<a href="#" %s><i></i></a>' % (self._report.style.getClsTag(['CssHrefNoDecoration', 'CssButtonBasic'])))
    items.append('</div>')
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return ''.join(items)


class TextWithBorder(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Text with Border and Icon', 'Rich', 'textborder'

  def __init__(self, report, recordSet, width, height, align, helper, profile):
    super(TextWithBorder, self).__init__(report, recordSet, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self.align = align
    if not 'colorTitle' in self.val:
      self.val['colorTitle'] = self._report.theme.colors[9]
    if not 'color' in self.val:
      self.val['color'] = self._report.theme.colors[9]
    self.css({"border-color": self.val['colorTitle'], 'margin-top': '20px'})

  @property
  def _js__builder__(self):
    return '''
      var legendElt = htmlObj.querySelector('legend'); legendElt.innerHTML = data.title; 
      htmlObj.querySelector('span').innerHTML = data.value'''

  def __str__(self):
    item = ['<fieldset %s>' % self.get_attrs(pyClassNames=self.style.get_classes())]
    if 'icon' in self.val:
      self.val['align'] = self.align
      item.append('<i class="%(icon)s fa-5x" style="width:100%%;text-align:%(align)s;margin:2px 0 10px 0;color:%(color)s"></i>' % self.val)
    if 'url' in self.val:
      item.append('<legend style="font-size:%spx;color:%s"></legend><span></span><br><a style="float:right" href="%s">+ more details</a></fieldset>' % (Defaults_css.font(10), self.val['colorTitle'], self.val['url']))
    else:
      item.append('<legend style="font-size:%spx;color:%s"></legend><span></span></fieldset>' % (Defaults_css.font(10), self.val['colorTitle']))
    item.append(self.helper)
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "".join(item)


class Number(Html.Html):
  name, category, callFnc = 'Number', 'Rich', 'number'

  def __init__(self, report, number, label, width, height, profile, options):
    super(Number, self).__init__(report, number, css_attrs={"width": width, "height": height}, profile=profile)
    if options.get('url', None) is not None:
      self.add_link(number, url=options['url'], css={"font-size": Defaults_css.font(10),
                      "width": "100%", 'text-decoration': 'none', 'display': 'inline-block', "text-align": 'center',
                      'margin': 0, 'color': 'inherit', 'padding': 0})
      self.span = self.link
    else:
      self.add_link(number, url="#", css={"font-size": Defaults_css.font(10),
                     "width": "100%", 'text-decoration': 'none', 'cursor': 'default',
                     'display': 'inline-block', "text-align": 'center', 'margin': 0, 'color': 'inherit', 'padding': 0})
      self.link.attr['target'] = '_self'
      self.span = self.link

      # self.add_span(number, css={'height': 'auto', "font-size": "%s%s" % (size[0] + 10, size[1]), "width": "100%", 'margin': 0})
    self.add_label(label, css={'float': 'none', "width": "100%", "margin": 0})
    self.css({"display": "inline-block", 'padding': '2px 0', 'clear': 'both', 'margin': '2px'})

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.style.get_classes())


class Delta(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui'] # jquery ui for progressbar
  name, category, callFnc = 'Delta Figures', 'Rich', 'delta'

  def __init__(self, report, records, width, height, options, helper, profile):
    super(Delta, self).__init__(report, records, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    if not 'color' in self.val:
      self.val['color'] = self._report.theme.colors[9]
    if not 'thresold1' in self.val:
      self.val['thresold1'] = 100
    if not 'thresold2' in self.val:
      self.val['thresold2'] = 50
    self.css({"color": self.val['color']})
    self._jsStyles = options

  @property
  def _js__builder__(self):
    return '''
       jHtmlObj = jQuery(htmlObj);
       var variation = 100 * (data.number - data.prevNumber) / data.prevNumber; var warning = ''; var currVal = %(number)s; 
       if(variation > data.thresold1){warning = '<i style="color:%(recColod)s;" title="'+ variation +' increase" class="fas fa-exclamation-triangle"></i>&nbsp;&nbsp;'};
       if(data.url != null){currVal = '<a style="text-decoration:none;color:'+ data.color +'" href="' + data.url+ '">'+ currVal +'</a>'}
       if(data.label != undefined){currVal = data.label +" "+ currVal};
       var progressElt = jHtmlObj.find('#progress');
       progressElt.progressbar({value: variation});
       if(variation > data.thresold1){progressElt.children().css({'background': options.colors.red})} 
       else if(variation > data.thresold2){progressElt.children().css({'background': options.colors.orange})} 
       else{progressElt.children().css({'background': options.colors.green})}
       jHtmlObj.find('div').first().html(warning + currVal);
       jHtmlObj.find('div').last().html('Previous number: '+ %(prev_number)s);
      ''' % {"recColod": self._report.theme.danger[1], 'number': self._report.js.number("data.number", isPyData=False).toFormattedNumber(
        decPlaces=self._report.js.number("options.decPlaces", isPyData=False),
        thouSeparator=self._report.js.number("options.thouSeparator", isPyData=False),
        decSeparator=self._report.js.number("options.decSeparator", isPyData=False)),
             'prev_number': self._report.js.number("data.prevNumber", isPyData=False).toFormattedNumber(
        decPlaces=self._report.js.number("options.decPlaces", isPyData=False),
        thouSeparator=self._report.js.number("options.thouSeparator", isPyData=False),
        decSeparator=self._report.js.number("options.decSeparator", isPyData=False))}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '''<div %(strAttr)s>
      <div style="width:100%%;text-align:right;font-size:%(size)s"></div>
      <div id="progress" style="height:10px;color:%(color)s;border:1px solid %(greyColor)s"></div>
      <div style="font-size:10px;font-style:italic;color:%(greyColor)s;padding-bottom:5px;text-align:left"></div>
      %(helper)s
      </div>''' % {"strAttr": self.get_attrs(pyClassNames=self.style.get_classes()), "size": Defaults_css.font(12),
                   'htmlId': self.htmlId, "color": self.val['color'],
                   "greyColor": self._report.theme.greys[6], "helper": self.helper}

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
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
  __reqCss, __reqJs = ['font-awesome', 'bootstrap'], ['font-awesome', 'jquery']
  name, category, callFnc = 'Script Documentation', 'Text', 'doc'

  def __init__(self, report, title, scriptName, clssName, functionName, docType, width, height, color, profile):
    if not docType in self.docTypes:
      raise Exception('The docType %s does not exist' % docType)

    clssName = clssName if clssName is not None else 'NOT_SET'
    super(DocScript, self).__init__(report, {'title': title, 'clssName': clssName, 'functionName': functionName,
                                             'docType': docType, 'scriptName': scriptName.replace('.py', '')},
                                    css_attrs={"width": width, "height": height}, profile=profile)
    self.color = self._report.theme.colors[-1] if color is None else color

  @property
  def _js__builder__(self):
    return '''
      var request = "/reports/doc/"+ data.docType +"/"+ data.scriptName +"/"+ data.clssName +"/"+ data.functionName;
      if(data.functionName == ''){request = "/reports/doc/"+ data.docType +"/"+ data.scriptName +"/"+ data.clssName};
      $.post(request, function(data){JSON.parse(data).forEach(function(rec){htmlObj.querySelector('pre').append('<code>'+ rec +'</code><br />')})})'''

  def __str__(self):
    label = "from script <b>%s</b>" % self.val['scriptName']
    if self.val['clssName'] != 'NOT_SET':
      label = "%s, class <b>%s</b>" % (label, self.val['clssName'])
    if self.val['functionName'] != '':
      label = "%s, function <b>%s</b>" % (label, self.val['functionName'])
    return '''
      <div %s>
        <div style="color:%s;font-weight:bold;">%s</div>
        <pre style="padding:5px"></pre>
        <span style="font-style:italic;width:100%%;text-align:right;display:block;margin-top:-15px">%s</span>
      </div> ''' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.color, self.val['title'], label)


class Prism(Html.Html):
  __reqCss, __reqJs = ['prism'], ['prism', 'jqueryui']
  name, category, callFnc = 'Code Viewer', 'Rich', 'prism'

  def __init__(self, report, vals, language, width, height, isEditable, trimSpaces, align, helper, profile):
    super(Prism, self).__init__(report, vals, css_attrs={"width": width, "height": height}, profile=profile)
    self.isEditable = isEditable
    self.trimSpaces = trimSpaces
    self.attr['class'].add('language-%s' % language)
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
          ''' % {"vals": json.dumps(self.val), 'whiteColor': self._report.theme.greys[0]})
    copy.html()
    if self.trimSpaces:
      content = "".join(['<code style="width:100%%;">%s</code><br />' % line.strip() for line in self.val.split("\n")])
    else:
      content = "".join(['<code style="width:100%%;">%s</code><br />' % line for line in self.val.split("\n")])
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
      </div>''' % {"strAttr": self.get_attrs(self.get_attrs(pyClassNames=self.style.get_classes())), "copy": copy.html(),
                   "isEditable": self.isEditable, "content": content, "helper": self.helper, "htmlId": self.htmlId}

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
  # _grpCls = CssGrpClsText.CssClassFormulas

  def __init__(self, report, text, width, color, helper, profile):
    super(Formula, self).__init__(report, text, css_attrs={"color": color, "width": width}, profile=profile)
    self.add_helper(helper)
    #self._report.jsGlobal.addJs("MathJax.Hub.Config({tex2jax: {inlineMath: [['$', '$'], ['\\(', '\\)']]}})")

  @property
  def _js__builder__(self):
    return 'htmlObj.innerHTML = data'

  def __str__(self):
    return '<font %s>%s</font>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.content, self.helper)

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

  def __init__(self, report, color, label, height, tooltip, helper, profile):
    # Small change to allow the direct use of boolean and none to define the color
    # Those standards will simplify the creation of themes going forward
    super(TrafficLight, self).__init__(report, color, css_attrs={"width": height, "height": height}, profile=profile)
    self.add_helper(helper, css={"margin-top": "-17px"})
    self.add_label(label, css={"width": 'auto', 'float': 'none', 'vertical-align': 'middle', 'height': '100%',
                               "margin": '0 5px', 'display': 'inline-block', "min-width": '100px'})
    self.css({'border-radius': '60px', 'background-color': self.val, 'display': 'inline-block',
              'vertical-align': 'middle'})
    self.set_attrs(name="title", value=tooltip)
    self.set_attrs(name="data-status", value=color)
    self._jsStyles = {'red': self._report.theme.danger[1], 'green': self._report.theme.success[1], 'orange': self._report.theme.warning[1]}
    self.action = None
    if tooltip is not None:
      self.tooltip(tooltip)

  def colors(self, green=None, red=None, neutral=None):
    """
    Description:
    ------------
    Set the 3 colors of the traffic light

    Attributes:
    ----------
    :param green: The color used in case of result true
    :param red: The color used in case of result false
    :param neutral: The color used in case of null

    :return: self to allow the chains
    """
    if neutral is not None:
      self._jsStyles['orange'] = neutral
    if green is not None:
      self._jsStyles['green'] = green
    if red is not None:
      self._jsStyles['red'] = red
    return self

  def resolve(self, jsFncs, profile=False):
    """
    Description:
    ------------
    Turn a error warning to a green one

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    self.action = self._report.ui.icon("fas fa-wrench")
    self.action.inReport = False
    self.action.tooltip("Click to try to resolve the issue")
    self.action.style.css.font_size = 8
    self.action.style.css.margin_top = 8
    self.action.style.css.cursor = 'pointer'
    self.action.style.css.vertical_align = 'top'
    self.action.click(jsFncs, profile)
    return self

  def click(self, jsFncs, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    success = Colors.getHexToRgb(self._report.theme.success[1])
    self.style.css.cursor = "pointer"
    jsFncs = [self.dom.querySelector("div").toggle("background-color", "rgb(%s, %s, %s)" % (success[0], success[1], success[2]),
                                                   self._report.theme.danger[1])] + jsFncs
    return super(TrafficLight, self).click(jsFncs, profile)

  @property
  def _js__builder__(self):
    return '''
      if(data === false){htmlObj.querySelector('div').style.backgroundColor = options.red}
      else if (data === true){htmlObj.querySelector('div').style.backgroundColor = options.green}
      else if (data === null){htmlObj.querySelector('div').style.backgroundColor = options.orange}
      else {htmlObj.style.backgroundColor =data}'''

  def __str__(self):
    if self.action is not None:
      return '<div id="%s"><div %s></div>%s</div>%s' % (self.htmlId, self.get_attrs(pyClassNames=self.style.get_classes(), withId=False), self.action.html(), self.helper)

    return '<div id="%s"><div %s></div></div>%s' % (self.htmlId, self.get_attrs(pyClassNames=self.style.get_classes(), withId=False), self.helper)

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
  # _grpCls = CssGrpClsTable.CssClassTableContent

  def __init__(self, report, recordSet, width, height, profile):
    self.indices, self.first_level, self.entries_count, self.ext_links = [], None, 0, {}
    super(ContentsTable, self).__init__(report, recordSet, css_attrs={"width": width, "height": height}, profile=profile)

  def add(self, text, level, name=None, script_name=None, report_name=None):
    """

    :param text:
    :param level:
    :param name:
    :param script_name:
    :param report_name:
    """
    if script_name is not None:
      self.ext_links[self.entries_count] = {"scriptName": script_name,
                     "folderName": report_name if report_name is not None else self._report.run.report_name}
    if self.first_level is None:
      self.first_level = level
    adjLevel = level - self.first_level + 1
    self.indices.append(adjLevel)
    if name is None:
      name = self.entries_count
    self.val.append({'text': text, 'level': adjLevel, 'name': name})
    self.entries_count += 1
    return name

  def __str__(self):
    entries = []
    for i, v in enumerate(self.val):
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
    # self.addGlobalFnc("ChangeContents(src, htmlId)", '''
    #     $("#contents_vals_"+ htmlId).toggle() ;
    #     if( $("#contents_vals_"+ htmlId).css('display') == 'none'){
    #       $(src).text("Show"); $("#contents_title_"+ htmlId).css( "text-align", 'left')}
    #     else{$(src).text("Hide") ;$("#contents_title_"+ htmlId).css( "text-align", 'center')}''')
    return '''
      <div %(attr)s>
        <div id='contents_title_%(htmlId)s' style="text-align:center;font-size:%(size)spx;font-weight:bold">Contents [<a href='#' onclick='ChangeContents(this, "%(htmlId)s")' >hide</a>] </div>
        <div id='contents_vals_%(htmlId)s' style="margin:0;padding:0">%(contents)s</div>
      </div> ''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'contents': "<br />".join(entries),
                    'size': Defaults_css.font(4), 'htmlId': self.htmlId}


class SearchResult(Html.Html):
  name, category, callFnc = 'Search Result', 'Text', 'searchr'

  def __init__(self, report, recordSet, pageNumber, width, height):
    super(SearchResult, self).__init__(report, recordSet, css_attrs={"width": width, "height": height})
    self._jsStyles = {'title': {'color': self._report.theme.colors[7], 'font-size': '18px'}, 'dsc': {'color': self._report.theme.greys[6]},
                      'url': {'color': self._report.theme.success[1], 'font-size': '14px'}, 'visited': {'color': self._report.theme.greys[5]},
                      'link': {'color': self._report.theme.colors[7], 'cursor': 'pointer'}, 'pageNumber': pageNumber}

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
               "greyColor": self._report.theme.colors[9], "whiteColor": self._report.theme.greys[0]})

  def __str__(self):
    self._report.style.cssCls('CssDivPagination')
    return '<div %s style="margin:5px 10px 5px 10px;"></div> ' % self.get_attrs(pyClassNames=self.defined)
