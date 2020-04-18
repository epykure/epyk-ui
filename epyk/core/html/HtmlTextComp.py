
import re

from epyk.core.html import Html
from epyk.core.css import Colors

from epyk.core.html.options import OptText
from epyk.core.js.html import JsHtml

# The list of CSS classes
from epyk.core.css.styles import GrpCls
from epyk.core.css import Defaults_css

# The list of CSS classes
from epyk.core.css.styles import GrpClsText


class UpDown(Html.Html):
  name, category, callFnc = 'Up and Down', 'Texts', 'updown'
  __reqCss, __reqJs = ['font-awesome'], ['accounting', 'font-awesome']

  def __init__(self, report, rec, color, label, options, helper, profile):
    if rec is None:
      rec = {'value': 0, 'previous': 0}
    if label is not None:
      rec["label"] = label
    super(UpDown, self).__init__(report, rec, profile=profile)
    self.add_helper(helper)
    self.val['color'] = self._report.theme.colors[9] if color is None else color
    self.__options = OptText.OptionsNumber(self, options)

  @property
  def options(self):
    """
    Property to set all the possible object for a button

    :rtype: OptText.OptionsNumber
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
      var delta = data.value - data.previous; 
      if(data.previous == 0) {var relMove = 'N/A'} else{var relMove = 100 * ((data.value - data.previous) / data.previous)};
      if(data.digits == undefined){data.digits = 0};
      if(data.label != undefined){htmlObj.append("<span style='padding:5px;font-size:"+ options.font_size+"'>"+ data.label +"</span>")};
      var valueElt = document.createElement('span'); valueElt.setAttribute('style', 'padding:5px'); 
      valueElt.innerHTML = accounting.formatNumber(data.value, options.digits, options.thousand_sep, options.decimal_sep); 
      htmlObj.appendChild(valueElt); var deltaElt = document.createElement('span');
      var relMoveElt = document.createElement('span'); var icon = document.createElement('i');
      if (delta < 0){
        deltaElt.setAttribute('style', 'padding:5px;color:'+ options.red +';font-size:'+ options.font_size);
        deltaElt.innerHTML = "(+"+ accounting.formatNumber(delta, options.digits, options.thousand_sep, options.decimal_sep) +")";
        relMoveElt.setAttribute('style', 'padding:5px;color:'+ options.red +';font-size:'+ options.font_size)
        relMoveElt.innerHTML = "("+ accounting.formatNumber(relMove, 2, options.thousand_sep, options.decimal_sep) +"%)";
        icon.className = 'fas fa-arrow-down';
        icon.setAttribute('style', 'color:'+ options.red +';font-size:'+ options.font_size)}
      else{  
        deltaElt.setAttribute('style', 'padding:5px;color:'+ options.green +';font-size:'+ options.font_size);
        deltaElt.innerHTML = "(+"+ accounting.formatNumber(delta, options.digits, options.thousand_sep, options.decimal_sep) +")";
        relMoveElt.setAttribute('style', 'padding:5px;color:'+ options.green +';font-size:'+ options.font_size)
        relMoveElt.innerHTML = "("+ accounting.formatNumber(relMove, 2, options.thousand_sep, options.decimal_sep) +"%)";
        icon.className = 'fas fa-arrow-up';
        icon.setAttribute('style', 'color:'+ options.green +';font-size:'+ options.font_size)};
      htmlObj.appendChild(deltaElt); htmlObj.appendChild(relMoveElt); htmlObj.appendChild(icon);
      '''

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class BlockText(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Block text', 'Rich', 'blocktext'
  # _grpCls = CssGrpClsText.CssClassTextBlock

  def __init__(self, report, recordSet, color, border, width, height, helper, options, profile):
    super(BlockText, self).__init__(report, recordSet, css_attrs={'color': color, "width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self.__options = OptText.OptionsText(self, options)
    self.css({'padding': '5px'})
    if border != 'auto':
      self.css('border', str(border))

  @property
  def options(self):
    """
    Property to set all the possible object for a button

    :rtype: OptText.OptionsText
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
      htmlObj.find('div').first().html(data.title); htmlObj.find('div').last().empty(); var content;
      if (typeof data.text === 'string' || data.text instanceof String) {content = data.text.split("\\n")}
      else {content = data.text}
      content.forEach(function(line){htmlObj.find('div').last().append('<p class="py_csstext">'+ line +'</a>')});
      if(options.showdown){var converter = new showdown.Converter(options.showdown); data.text = converter.makeHtml(data.text)} 
      htmlObj.find('div').last().html(data.text);
      if (data.color != undefined) {htmlObj.find('div').last().css('color', data.color)};
      if(typeof data.button != 'undefined'){
        htmlObj.find("a").html(data.button.text); htmlObj.find("a").attr('href', data.button.url)}
      '''

  def __str__(self):
    items = ['<div %s>' % self.get_attrs(pyClassNames=self.style.get_classes())]
    items.append('<div id="%s_title" style="font-size:%spx;text-align:left"><a></a></div>' % (self.htmlId, Defaults_css.font(3)))
    items.append('<div id="%s_p" style="width:100%%;text-justify:inter-word;text-align:justify;"></div>' % self.htmlId)
    #if self.val.get('button') is not None:
    #  items.append('<a href="#" %s><i></i></a>' % (self._report.style.getClsTag(['CssHrefNoDecoration', 'CssButtonBasic'])))
    items.append('</div>')
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return ''.join(items)


class TextWithBorder(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Text with Border and Icon', 'Rich', 'textborder'

  def __init__(self, report, recordSet, width, height, align, helper, options, profile):
    super(TextWithBorder, self).__init__(report, recordSet, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self.__options = OptText.OptionsText(self, options)
    self.align = align
    if not 'colorTitle' in self.val:
      self.val['colorTitle'] = self._report.theme.colors[9]
    if not 'color' in self.val:
      self.val['color'] = self._report.theme.colors[9]
    self.css({"border-color": self.val['colorTitle'], 'margin-top': '20px'})

  @property
  def options(self):
    """
    Property to set all the possible object for a button

    :rtype: OptText.OptionsText
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
      if(options.showdown){var converter = new showdown.Converter(options.showdown); 
        data.title = converter.makeHtml(data.title); data.value = converter.makeHtml(data.value)} 
      htmlObj.querySelector('legend').innerHTML = data.title; htmlObj.querySelector('span').innerHTML = data.value'''

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
  __reqCss, __reqJs = ['jqueryui'], ['accounting', 'jqueryui']
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
    self.__options = OptText.OptionsNumber(self, options)

  @property
  def options(self):
    """
    Property to set all the possible object for a button

    :rtype: OptText.OptionsNumber
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
       jHtmlObj = jQuery(htmlObj);
       var variation = 100 * (data.number - data.prevNumber) / data.prevNumber; var warning = ''; 
       var currVal = accounting.formatNumber(data.number, options.digits, options.thousand_sep, options.decimal_sep); 
       if(variation > data.thresold1){warning = '<i style="color:'+ options.red +';" title="'+ variation +' increase" class="fas fa-exclamation-triangle"></i>&nbsp;&nbsp;'};
       if(data.url != null){currVal = '<a style="text-decoration:none;color:'+ data.color +'" href="' + data.url+ '">'+ currVal +'</a>'}
       if(data.label != undefined){currVal = data.label +" "+ currVal};
       var progressElt = jHtmlObj.find('#progress');
       progressElt.progressbar({value: variation});
       if(variation > data.thresold1){progressElt.children().css({'background': options.red})} 
       else if(variation > data.thresold2){progressElt.children().css({'background': options.orange})} 
       else{progressElt.children().css({'background': options.green})}
       jHtmlObj.find('div').first().html(warning + currVal);
       jHtmlObj.find('div').last().html('Previous number: '+ accounting.formatNumber(data.prevNumber, options.digits, options.thousand_sep, options.decimal_sep));
      '''

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


class Formula(Html.Html):
  __reqJs = ['mathjs']
  name, category, callFnc = 'Latex Formula', 'Texts', 'formula'

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

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlBackground(self, report=self._report)
    return self._dom

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
      else {htmlObj.style.backgroundColor = data}'''

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

  def __init__(self, report, title, width, height, options, profile):
    self.indices, self.first_level, self.entries_count, self.ext_links = [], None, 0, {}
    super(ContentsTable, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.style.css.position = "fixed"
    self.title = self._report.ui.div()
    self.title += self._report.ui.text(title).css({"width": 'auto', 'display': 'inline-block'})
    self.title += self._report.ui.text("[hide]").css({"width": '30px', 'display': 'inline-block', 'margin-left': '5px'})
    self.title[0].style.css.font_size = Defaults_css.font(6)
    self.title[0].style.css.font_weight = "bold"
    self.title.inReport = False

  def __getitem__(self, i):
    """
    Description:
    ------------
    Return the internal column in the row for the given index

    :param i: the column index
    :rtype: Col
    """
    return self.val[i]

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component

    :rtype: GrpClsText.ContentTable
    """
    if self._styleObj is None:
      self._styleObj = GrpClsText.ContentTable(self)
    return self._styleObj

  def add(self, text, level, anchor):
    """
    Description:
    ------------

    :param text:
    :param level:
    """
    href = self._report.ui.link(text, url=anchor)
    href.style.css.font_size = Defaults_css.font(2)
    href.style.add_classes.link.no_decoration()
    self.val.append(href)
    href.style.css.display = 'block'
    href.style.css.width = '100%'
    if level is not None:
      href.style.css.padding_left = (level - 1) * 5
    return self

  def move(self):
    super(ContentsTable, self).move()
    self.style.css.position = None
    self.style.css.margin = 5

  def __str__(self):
    div_link = self._report.ui.div(self.val)
    div_link.inReport = False
    self.title[-1].click([div_link.dom.toggle(), self.title[-1].dom.toggleText('[show]', '[hide]')])
    return '''<div %(attr)s>%(title)s%(links)s</div> ''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()),
                                                            'title': self.title.html(), 'htmlId': self.htmlId, 'links': div_link.html()}


class SearchResult(Html.Html):
  name, category, callFnc = 'Search Result', 'Text', 'searchr'
  __reqJs = ['jquery']

  def __init__(self, report, recordSet, pageNumber, width, height, options, profile):
    super(SearchResult, self).__init__(report, recordSet, css_attrs={"width": width, "height": height})
    self._jsStyles = {'title': {'color': self._report.theme.colors[7], 'font-size': '18px'}, 'dsc': {'color': self._report.theme.greys[6]},
                      'url': {'color': self._report.theme.success[1], 'font-size': '14px'}, 'visited': {'color': self._report.theme.greys[5]},
                      'link': {'color': self._report.theme.colors[7], 'cursor': 'pointer'}, 'pageNumber': pageNumber,
                      'currPage': 0, "greyColor": self._report.theme.colors[9], "whiteColor": self._report.theme.greys[0]}

  # self.addGlobalFnc("%s(htmlObj, data, jsStyles, currPage)" % self.__class__.__name__, ''' htmlObj.empty() ;
  @property
  def _js__builder__(self):
    return '''
      jHtmlObj = jQuery(htmlObj);
      if (typeof options.currPage == 'undefined'){options.currPage = 0}; var pageNumber = options.pageNumber;
      data.slice(options.currPage * pageNumber).forEach( function(rec){
        var newItem = $('<div style="margin:5px 10px 5px 10px;"></div>') ; 
        var title = $('<div>'+ rec['title'] + '</div>').css( options.title );
        if (rec['urlTitle'] != undefined){
          title.css({'cursor': 'pointer'}); title.click(function(e){window.open(rec['urlTitle'], '_blank')})}
        newItem.append(title);
        if (rec.icon != undefined){
          var item = $('<div></div>').css(options.url);
          item.append( $('<i class="'+ rec['icon'] +'" style="margin-right:5px"></i>')).append(rec['url']);
          newItem.append(item)} 
        else if(rec.url != undefined) {newItem.append($('<div>'+ rec['url'] +'</div>').css(options.url))}
        newItem.append( $('<div>'+ rec['dsc'] +'</div>').css(options.dsc));
        if(rec.visited != undefined){newItem.append($('<div>'+ rec.visited +'</div>').css(options.visited))}
        if(rec.links != undefined){
          rec.links.forEach(function(link){ 
            if (link.url == undefined) {link.url = link.val};
            newItem.append($('<a href='+ link.url +' target="_blank">'+ link.val +'</a><br>').css(options.link))})};
        jHtmlObj.append(newItem);
      }); 
      if(data.length > 0) {
        var reste = data.length/ pageNumber; var currIndex = options.currPage+1; var roundRest = Math.trunc(reste);
        if (roundRest > reste) {reste ++};
        var paginate = $('<div style="display:inline-block;height:35px;padding:0;width:100%%;text-align:center;margin-top:10px" class="py_cssdivpagination"></div>');
        if (currIndex > 1){
          var href = $('<a href="#">&laquo;</a>');
          href.click({page: options.currPage-1, rec: data}, function(e){%(class)s(htmlObj, e.data.rec, options, e.data.page)});
          paginate.append(href)};
        for (var i = 0; i < reste; i++){
          var indexPage = i + 1;
          if (options.currPage == i) { 
            var href = $('<a href="#" style="background-color:'+ options.greyColor +';color:'+ options.whiteColor +'">'+ indexPage +'</a>');
            href.click({page: i, rec: data}, function(e) { %(class)s(htmlObj, e.data.rec, options, e.data.page)});
            paginate.append(href)}
          else{
            var href = $('<a href="#">'+ indexPage +'</a>') ;
            href.click({page: i, rec: data}, function(e){%(class)s(htmlObj, e.data.rec, options, e.data.page)});
            paginate.append(href)}}
        if(currIndex < reste){
          var href = $('<a href="#">&raquo;</a>');
          href.click({page: options.currPage+1, rec: data}, function(e){%(class)s(htmlObj, e.data.rec, options, e.data.page)});
          paginate.append(href)};
        jHtmlObj.append(paginate)
      } ''' % {"class": self.__class__.__name__}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    #self._report.style.cssCls('CssDivPagination')
    return '<div %s style="margin:5px 10px 5px 10px;"></div> ' % self.get_attrs(pyClassNames=self.style.get_classes())


class Composite(Html.Html):
  name, category, callFnc = 'Composite', 'Rich', 'composite'

  def __init__(self, report, schema, width, height, htmlCode, options, profile, helper):
    super(Composite, self).__init__(report, None, css_attrs={"width": width, "height": height})
    self.__builders = set()
    self.add_helper(helper)
    self._set_comp(None, schema, self.__builders)
    self.attr = self.val.attr
    self._js = self.val._js

  @property
  def dom(self):
    """
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtml(self.val, report=self._report)
    return self._dom

  @property
  def style(self):
    """
    Description:
    ------------

    :rtype: GrpCls.ClassHtmlEmpty
    """
    if self._styleObj is None:
      self._styleObj = GrpCls.ClassHtmlEmpty(self)
    return self._styleObj

  def __getitem__(self, i):
    return self.val[i]

  @property
  def _get_comp_map(self):
    """
    Description:
    ------------

    """
    return {
      'div': self._report.ui.div,
      'textarea': self._report.ui.textarea,
      'button': self._report.ui.section,
      'label': self._report.ui.label,
      'header': self._report.ui.header,
      'section': self._report.ui.section,
      'icon': self._report.ui.icon,
      'span': self._report.ui.texts.span,
      'input': self._report.ui.inputs.d_text}

  def _set_comp(self, comp, schema_child, builders):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param comp:
    :param schema_child:
    :param builders:
    """
    new_comp = self._get_comp_map[schema_child['type']](**schema_child.get('args', {}))
    if 'builder' in schema_child:
      builders.add(schema_child['builder'])
    if 'class' in schema_child:
      new_comp.set_attrs({'class': schema_child['class']})
    if 'arias' in schema_child:
      new_comp.aria.set(schema_child['arias'])
    if 'css' in schema_child:
      new_comp.css(schema_child['css'], reset=True)
    if 'attrs' in schema_child:
      new_comp.set_attrs(schema_child['attrs'])
    for child in schema_child.get('children', []):
      self._set_comp(new_comp, child, builders)

    if comp is not None:
      comp += new_comp
    else:
      new_comp.inReport = False
      # delegate the htmlID to the main component
      new_comp.htmlCode = self.htmlId
      self._vals = new_comp

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).extend(list(self.__builders))
    return self.val.html()
