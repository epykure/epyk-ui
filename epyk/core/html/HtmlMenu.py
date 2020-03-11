
import json
import logging


from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.styles import GrpClsMenu
from epyk.core.css import Defaults_css


class HtmlNavBar(Html.Html):
  name, category = 'Nav Bar', 'System'

  def __init__(self, report, components, width, height, options, profile):
    super(HtmlNavBar, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    if components is not None:
      if not isinstance(components, list):
        components = [components]
      for c in components:
        self.__add__(c)

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component

    :rtype: GrpClsMenu.ClassNav
    """
    if self._styleObj is None:
      self._styleObj = GrpClsMenu.ClassNav(self)
    return self._styleObj

  def __add__(self, htmlObj):
    """ Add items to the footer """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    htmlObj.style.css.display = 'inline-block'
    htmlObj.style.css.line_height = '100%'
    htmlObj.style.css.font_size = Defaults_css.font(5)
    if htmlObj.css('height') is None:
      htmlObj.style.css.vertical_align = 'middle'
    if htmlObj.css('width') == '100%':
      htmlObj.style.css.width = None
    self.val.append(htmlObj)
    return self

  def add_text(self, text):
    """

    :param text:
    :return:
    """
    val = self._report.ui.text(text)
    self.__add__(val)
    val.style.css.height = "100%"
    val.style.css.vertical_align = 'middle'
    return val

  def __str__(self):
    str_h = "".join([h.html() for h in self.val])
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_h)


class HtmlParamsBar(Html.Html):
  __reqCss, __reqJs = ['bootstrap'], ['bootstrap']
  # _grpCls = GrpCls.CssGrpClassBase
  allowedComponents = ['date', 'input', 'radio', 'button', 'select', 'title', 'slider', 'switch',
                       'selectmulti', 'delimiter', 'check', 'checkbox', 'inputRange', 'slider', 'inputInt']
  name, category = 'Parameters Bar', 'System'
  docCategory = 'System'

  def __init__(self, report, vals, top, logFiles, height):
    """ Instanciate a container object """
    self.__components, self.__order, self.logFiles = {}, [], logFiles
    self.jsUpdateFnc, self.inCookies = True, {}
    vals = list(vals)
    for component in vals:
      if component['htmlComponent'] not in self.allowedComponents:
        logging.error('%s is not allowed in the parameters bar' % component['htmlComponent'])
        raise Exception('%s is not allowed in the parameters bar' % component['htmlComponent'])

      fnc = getattr(report, component['htmlComponent'])
      parameters = dict(component)
      if 'inCookies' in parameters and report.withCookies:
        self.inCookies[component['htmlCode']] = parameters['inCookies']
        del parameters['inCookies']

      if parameters['htmlComponent'] in ['input', 'date', 'checkbox', 'switch', 'slider']:
        if "widthUnit" not in parameters:
          parameters['widthUnit'] = "px"
        if parameters['htmlComponent'] == 'input':
          parameters['align'] = None
      del parameters['htmlComponent']

      if 'on_init' in parameters:
        recordSet = parameters['on_init'](report)
        parameters['recordSet'] = recordSet
        del parameters['on_init']

      if not component['htmlComponent'] in ['delimiter']:
        htmlCode = component['htmlCode']
        if htmlCode in self.__order:
          raise Exception('code in the Parameters bar - %s - duplicated' % htmlCode)

      htmlObj = fnc(**parameters)
      if hasattr(htmlObj, 'initVal') and htmlCode in report.http:
        htmlObj.initVal(report.http[htmlCode])
      if component['htmlComponent'] in ['delimiter']:
        htmlObj.htmlCode = "component_%s" % id(self)
      self.__add__(htmlObj)
    self.height, self.top = height, top
    report.marginTop += height
    super(HtmlParamsBar, self).__init__(report, [])
    self.css({'margin': 0, "padding": '4px 0', 'display': 'inline-block'})

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    htmlObj.css({'display': 'inline-block', 'margin-right': '10px'})
    htmlObj.change(htmlObj.jsToUrl())
    # The component added must have a htmlCode class variable defined
    self.__order.append(htmlObj.htmlCode)
    self.__components[htmlObj.htmlCode] = htmlObj
    return self

  def getHtmlCodes(self):
    return self.__order

  def get(self, htmlCode):
    """ Return the Html component in the parameter bar """
    return self.__components[htmlCode]

  def toCookies(self, htmlCode):
    return self.inCookies.get(htmlCode, True)

  def onDocumentReady(self):
    """ Return the javascript calls to be returned to update the component """
    vals = [self.__components[comp].html() for comp in self.__order]
    self._report.jsOnLoadFnc.insert(0, 'NavBar(%s, %s)' % (self.jqId, json.dumps(vals)))

  def onDocumentLoadFnc(self):
    """ Pure Javascript onDocumentLoad Function """
    self.addGlobalFnc("NavBar(htmlObj, data)", ''' htmlObj.empty() ; data.forEach(function(rec){ htmlObj.append(rec) ; });  ''')

  def jsToUrl(self): return ''

  def __str__(self):
    """ Returns the HTML representation of the parameter bar """
    # Change the margin of the body as the Parameter bar will take some extra space on the top of the page
    self._report.jsOnLoadFnc.add('$("body").css("margin-bottom", "%spx")' % (self._report.marginTop - self.height))
    self._report.jsOnLoadFnc.add('''
      $('#nav_bar_reset').on('click', function(event) {%(jsPost)s});
      ''' % {'jsPost': self._report.jsPost("%s/locals/clean/%s" % (self._report._urlsApp['transfer'], self._report.run.report_name), None, self.jsGoTo(self.jsToUrlReset(), isPyData=False), isPyData=False)} )
    self._report.style.cssCls("CssParamsBar")
    self.addGlobalFnc("BreadCrumbClick(url)", '''
        $('#popup_loading').find("div").html("Loading "+ url +"...");
        $('#popup_loading_back').show(); $('#popup_loading').show();
        var params = []; console.log(%(breadCrumVar)s);
        for(var key in %(breadCrumVar)s['params']) {
          if (%(breadCrumVar)s['params'][key] != null){params.push(key +"="+ %(breadCrumVar)s['params'][key])}}
        if(params.length > 0) {breadCrumResult = url +"?"+ params.join("&")} else {breadCrumResult = url};
        window.location.href = breadCrumResult ''' % {'breadCrumVar': self._report.jsGlobal.breadCrumVar})
    return '''
      <div id="param_bar" class="%(clsParamBar)s" style="bottom:%(bottom)spx;border-bottom:1px solid %(border)s;z-index:30">
        <i class="fas fa-play" onclick="BreadCrumbClick(%(url)s)" style="margin-right:30px;cursor:pointer"></i><div %(strAttr)s></div>
      </div> ''' % {'bottom': 0, 'clsParamBar': self._report.style.cssName("CssParamsBar"),
                    'strAttr': self.get_attrs(pyClassNames=['CssBasicList']), "border": self._report.theme.greys[5], "url": self.jsToUrlReset()}


class HtmlSideBar(Html.Html):
  name, category, callFnc = 'Side bar', 'Others', 'sidebar'
  __reqCss, __reqJs = ['bootstrap', 'font-awesome', 'jquery-scrollbar'], ['bootstrap', 'font-awesome', 'jquery-scrollbar']
  onMouseOverColor = 'black'
  # _grpCls = GrpCls.CssClassSideBarFixed

  def __init__(self, report, links, color, size, servers):
    super(HtmlSideBar, self).__init__(report, links)
    self.color = self._report.theme.greys[0] if color is None else color
    self.size, self.servers = "%s%s" % (size[0], size[1]), servers
    self.css({'color': self.color, 'font-size': self.size, 'z-index': 5, 'margin': 0})
    self._actions = []

  @property
  def htmlId(self):
    return 'report_side_bar'

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, ''' $('#side_bar_explorer').empty();
      var group = $('<ul style="padding:0;margin:0;list-style:none"></ul>'); 
      var sidebarState = JSON.parse(window.sessionStorage.getItem('SIDEBAR_STATE'));
      if (sidebarState === null) {sidebarState = {}};
      data.folders.forEach(function(rec, index){
        var li = $('<li onclick="GetFolder(this);"></li>'); var display = 'none' ; var chevron = 'fas fa-folder';
        if ('env_' + index in sidebarState) { display = sidebarState['env_' + index] ; }
        if (display != 'none') { chevron = 'fas fa-folder-open'; }
        li.append('<a href="#" style="color:%(darkBlue)s;font-weight:bold;text-decoration:none;display:inline-block;padding-left:5px;margin-right:5px;font-size:14px;font-variant:small-caps;"><b><i id="chevron" class="fa ' + chevron + '"></i>&nbsp;'+ rec.name +'</a></b>') ;
        var sub = $('<ul id="env_' + index + '" style="padding:0 0 0 20px;margin:0;list-style:none;display:'+ display +'"></ul>') ;
        eventLi = $('<li onclick="event.stopPropagation();" style="margin-bottom:10px">') ;
        sub.append(eventLi);

        rec.items.forEach(function(data){
          var icons = '<i onclick=\\'GoToReport("%(urlReport)s/run/'+ rec.name +'/'+ data.script +'", true, false)\\' style="display:inline-block;margin-right:10px" title="Open in new tab" class="far fa-arrow-alt-circle-right"></i><i onclick=\\'GoToReport("%(urlReport)s/view/'+ rec.name +'/'+ data.script +'", true, false)\\' style="display:inline-block;font-size:14px;margin-right:10px" title="View Statistics" class="far fa-chart-bar"></i>' ;
          if (data.color == undefined) { data.color = '%(darkBlue)s' ; };
          if (data.doc) { icons = icons + '<i onclick=\\'GoToReport("%(urlReport)s/dsc/'+ rec.name +'/'+ data.script +'", true, false)\\' style="display:inline-block;margin-right:10px" title="Documentation" class="far fa-file-alt"></i>' ; }
          if (data.inFavorite) {sub.append('<li onclick="event.stopPropagation();"><a href="#" title="'+ data.script + '" style="display:inline-block;margin-right:10px;color:'+ data.color + '" onclick="BreadCrumbClick(this, \\''+ data.url.replace(/\\\\/g, '\\\\\\\\')  +'\\')">'+ data.name +'</a></li>') ; } 
          else { sub.append('<li style="white-space:nowrap; overflow-x: hidden;margin-right:10px" onclick="event.stopPropagation();"><a href="#" title="'+ data.script + '" style="display:inline-block;margin-right:10px;color:'+ data.color + '" onclick="BreadCrumbClick(this, \\''+ data.url.replace(/\\\\/g, '\\\\\\\\')  +'\\')">'+ data.name +'</a><i style="color:%(darkBlue)s;cursor:pointer;font-size:14px;margin-right:10px" onclick="Favorites(this, \\'' + rec.name + '\\', \\'' + data.script + '\\', \\'div\\', true)" title="Add to favorites" class="far fa-heart"></i></li>') ; }});
        li.append(sub); group.append(li); });

      $('#side_bar_explorer').append(group);
      $('#side_bar_explorer').css( {'height': parseInt($('#side_bar_envs').css('height'),10) - 250 + 'px'} ) ;
      if (data.favorites.length > 0){
        htmlObj.find('#side_bar_favorite').empty();
        var groupFav = $('<ul style="padding:0;margin:0;list-style:none"></ul>');
        data.favorites.forEach(function(rec, index){
          var li = $('<li onclick="GetFolder(this);"></li>'); var display = 'none' ; var chevron = 'fas fa-folder';
          if ('env_' + index in sidebarState) { display = sidebarState['env_' + index]}
          if (display != 'none') { chevron = 'fas fa-folder-open'}
          li.append('<a href="#" style="color:%(darkBlue)s;font-weight:bold;font-variant:small-caps;text-decoration:none;display:block;font-size:14px;padding-left:5px"><b><i id="chevron" class="fa ' + chevron + '"></i>&nbsp;'+ rec.name +'</a></b>') ;
          var sub = $('<ul id="env_' + index + '" style="padding:0 0 0 20px;margin:0;list-style:none;display:'+ display +'"></ul>') ;
          rec.items.forEach(function(data){
            if (data.color == undefined) { data.color = '%(darkBlue)s'};
            sub.append('<li onclick="event.stopPropagation();"><a href="#" title="'+ data.script + '" style="color:'+ data.color + '" onclick="BreadCrumbClick(this, \\''+ data.url.replace(/\\\\/g, '\\\\\\\\')  +'\\')">'+ data.name +'</a><div style="color:%(darkBlue)s;cursor:pointer;margin-left:5px;font-size:10px" onclick="Favorites(this, \\'' + rec.name + '\\', \\'' + data.script + '\\', \\'div\\', false)" title="Remove from favorites" class="fas fa-times"></div></li>') ; 
          });
          li.append(sub); groupFav.append(li)});
        $('#side_bar_favorite').append(groupFav)}
      $("#nav_link_title").tooltip()
      ''' % {'reportName': self._report.run.report_name, 'hoverColor': self.onMouseOverColor,
             'urlReport': "",
             'cssLinks': self._report.style.getClsTag(['CssSideBarLinks']), 'darkBlue': self._report.theme.colors[9]})

  def addAction(self, icon, url, tooltip='', color=None, isPyData=True):
    actionDef = ['<div style="position:relative;cursor:pointer;display:block;pointer-events:auto;margin-bottom:10px;">']
    if isPyData:
      actionDef.append(
        '<i onclick="GoToReport(\'%(url)s\')" class="%(icon)s" title="%(tooltip)s" style="color:%(color)s"></i>' % {
          "url": url, "icon": icon, "url": url, "color": color, "tooltip": tooltip})
    else:
      actionDef.append(
        '<i onclick="%(url)s" class="%(icon)s" title="%(tooltip)s" style="color:%(color)s"></i>' % {"url": url,
                                                                                                    "icon": icon,
                                                                                                    "url": url,
                                                                                                    "color": color,
                                                                                                    "tooltip": tooltip})
    actionDef.append('</div>')
    self._actions.append("".join(actionDef))
    return self

  def __str__(self):
    styleBarBulble, StyleBarMenu = "CssSideBarBubble", "CssSideBarMenu"
    # Add some specific classes for the sidebar items
    self._report.style.cssCls(styleBarBulble)
    self._report.style.cssCls(StyleBarMenu)
    return '''
      <div id="side_bar_envs" style='height:100%%;display:none;position:fixed;z-index:5;width:300px;top:0;background-color:%(lightBlue)s;left:0;padding:50px 5px 5px 45px;'>
        <span style="font-weight:bold;display:inline-block;text-transform:uppercase;margin-top:10px;width:100%%">Favorites</span>
        <div id="side_bar_favorite" style="width:100%%;display:inline-block"></div>

        <hr />
        <input type="text" style="width:100%%;display:inline-block" placeholder="search a report" />
        <span style="font-weight:bold;display:inline-block;text-transform:uppercase;margin-top:10px;width:100%%">Environments</span>
        <div id="side_bar_explorer" style="margin-right:20px;width:100%%;overflow-y:scroll"></div>
      </div>

      <div %(strAttr)s>                
        <div style="position:relative;cursor:pointer;display:inline-block;pointer-events:auto;" onclick="$('#side_bar_envs').toggle()">
          <i class="fas fa-users" title="Public folders"></i>
        </div>

        <hr style="background-color:white;margin:10px 5px 15px 5px" />
        %(actions)s

        <div style="position:fixed;bottom:5px;cursor:pointer;width:40px">
          <div style="position:relative;display:inline-block;pointer-events:auto;" title="Python Info" onmouseout="$(this).find('div').hide()" onmouseover="$(this).find('div').show();">
            <i onclick="GoToReport('%(urlReport)s/python', false, false)" style="margin-right:2px" class="fab fa-python"></i>
          </div>
          <div style="position:relative;display:inline-block;pointer-events:auto;" title="Settings" onmouseout="$(this).find('div').hide()" onmouseover="$(this).find('div').show();">
            <i onclick="GoToReport('%(urlAdmin)s/account', false, false)" style="margin-right:2px" class="fas fa-wrench"></i>
          </div>

          <br />
          <!--
          <div style="position:relative;display:inline-block;pointer-events:auto;" title="The Script scheduler" onmouseout="$(this).find('div').hide()" onmouseover="$(this).find('div').show();">
            <i onclick="GoToReport('%(urlReport)s/run/scheduler/index', false, false)"  class="far fa-clock"></i>
          </div> 
          <div style="position:relative;display:inline-block;pointer-events:auto;" title="The lab" onmouseout="$(this).find('div').hide()" onmouseover="$(this).find('div').show();">
            <i onclick="GoToReport('%(urlReport)s/run/lab/index', false, false)"  class="fas fa-flask"></i>
          </div> --!>
          <div style="position:relative;display:inline-block;pointer-events:auto;" title="Log off" onmouseout="$(this).find('div').hide()" onmouseover="$(this).find('div').show();">
            <i onclick="GoToReport('%(urlAdmin)s/logout', false, false)" style="margin-right:2px" class="fas fa-power-off"></i>
          </div>

        </div>
      </div>''' % {"strAttr": self.get_attrs(pyClassNames=self.defined),
                   'report_name': self._report.run.report_name, 'urlReport': "",
                   'cssDef': self._report.style.cssName(styleBarBulble),
                   'cssSideBarMenu': "",
                   'script_name': self._report.run.script_name,
                   'urlAdmin': "", 'lightBlue': self._report.theme.colors[1],
                   "actions": "".join(self._actions)}


class HtmlFooter(Html.Html):

  def __init__(self, report, components, width, height, options, profile):
    super(HtmlFooter, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    if components is not None:
      if not isinstance(components, list):
        components = [components]
      for c in components:
        self.__add__(c)

  def __add__(self, htmlObj):
    """ Add items to the footer """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    self.val.append(htmlObj)
    return self

  def __getitem__(self, i):
    """
    Return the internal column in the row for the given index

    :param i: the column index
    """
    return self.val[i]

  def add_menu(self):
    pass

  def __str__(self):
    return "<footer %s></footer>" % self.get_attrs(pyClassNames=self.style.get_classes())
