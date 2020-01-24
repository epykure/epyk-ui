"""
Wrapper to Bootstrap Nav Bar
"""


import json
import time
import logging


from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls


class HtmlNavBar(Html.Html):
  __reqCss, __reqJs = ['bootstrap', 'font-awesome'], ['bootstrap', 'font-awesome']
  lenght = 42
  name, category, docCategory = 'Nav Bar', 'System', 'System'
  searchEngine, stackOverFlow = None, None

  def __init__(self, report, value, color, selected, size, breadcrum, logo, backgroundColor):
    self.selected, self.extraLinks, self.breadcrum = selected, None, breadcrum
    report.marginTop, self.categories, self.definedOrder = self.lenght, {}, ['Report', 'Archives', 'Export', 'Notebook']
    super(HtmlNavBar, self).__init__(report, value)
    self.backgroundColor = 'inherit' if backgroundColor is None else backgroundColor
    self.size = int(self._report.pyStyleDfl['fontSize'][:-2]) + 2 if size is None else size
    self.color, self.stype = 'inherit' if color is None else color, 'standard'
    self._report.logo, self._logoUrl = logo, "%s/img/%s/%s" % (self._report._urlsApp['index'].replace("/index", ''),
                                                               self._report.run.report_name, logo)


  # --------------------------------------------------------------------------------------------------------------
  #                                     DROPDOWN SECTIONS
  #
  def dropDown(self, name, definition, style="dropdown-toggle"):
    self.categories[name] = {"content": definition, "style": style}
    if not name in self.definedOrder:
      self.definedOrder.append(name)
    return self

  def dropDownReport(self,  report_name, script_name):
    return self.dropDown('Report', [
      {"name": "Clear Parameters", 'url': '%s/run/%s/%s' % (self._report._urlsApp['report'], report_name, script_name)},
      {"diviser": True},
      {"name": "Documentation", 'url': '%s/dsc/%s/%s' % (self._report._urlsApp['report'], report_name, script_name)},
      {"name": "Quick Share", 'url': '#', 'action': "onclick=\"FormGoTo('%s/quick/%s/%s', 'POST')\"" % (self._report._urlsApp['transfer'], report_name, script_name)},
      {"diviser": True},
      {"name": "Activity Info", 'target': '_blank', 'url': '%s/logs/%s/%s' % (self._report._urlsApp['report'], report_name, script_name)},
      {"name": "System Info", 'target': '_blank', 'url': '%s/info/%s/%s' % (self._report._urlsApp['report'], report_name, script_name)},
      {"name": "Code Inspection", 'target': '_blank', 'url': '%s/code/%s/%s' % (self._report._urlsApp['report'], report_name, script_name)},
      #{"diviser": True},
      #{"name": "Download Env", 'url': '%s/download/report/%s' % (self._report._urlsApp['transfer'], report_name)},
      #{"name": "Download Page", 'url': ''},
    ])

  def dropDownExport(self, report_name, script_name):
    return []
    # return self.dropDown('Export', [
    #   {"name": "Copy URL", 'url': '#', 'action': "onclick='CopyToClipboard()'"},
    #   {"diviser": True},
    #   {"name": "HTML 5", 'url': '#', 'action': "onclick=\"FormGoTo('%s/html/%s/%s', 'POST')\"" % (self._report._urlsApp['transfer'], report_name, script_name)},
    #   {"name": "Excel", 'url': '#', 'action': "onclick=\"FormGoTo('%s/xls/%s/%s', 'POST')\"" % (self._report._urlsApp['transfer'], report_name, script_name)},
    #   {"name": "Word", 'url': '#', 'action': "onclick=\"FormGoTo('%s/doc/%s/%s', 'POST')\"" % (self._report._urlsApp['transfer'], report_name, script_name)},
    #   #{"name": "Power Point", 'url': '#', 'action': "onclick=\"FormGoTo('%s/ppt/%s/%s', 'POST')\"" % (self._report._urlsApp['transfer'], report_name, script_name)}
    # ])

  def dropDownThemes(self, size):
    themeLst = []
    for theme in self._report.getThemes():
      themeLst.append('''<a class="dropdown-item" href="#" onclick="SetTheme('%s')" style="font-size:%s;position:relative;padding-left:35px;display:inline-block"><i class="fas fa-fill-drip" style="margin-right:10px"></i>%s</a>''' % (theme, size, theme))
    return '\n'.join(themeLst)


  def signingType(self, stype):
    """
    """
    sTypes = ['controlled', 'standard', 'owner']
    if not stype.lower() in sTypes:
      raise Exception("Signing Type accepted %s" % sTypes)
    self.stype = stype.lower()

  def __str__(self):
    colorText = 7
    barTheme = 'navbar-dark' if self._report.theme.greys[-1] == '#FFFFFF' else 'navbar-light'
    items = ['<nav id="report_nav_bar" class="navbar navbar-expand-sm fixed-top %s" style="background:%s;margin:0;padding:0 5px 2px 5px;border-bottom:1px solid %s">' % (barTheme, self._report.theme.greys[1], self._report.theme.greys[6])]
    items.append('<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon" style="margin-top:-5px"></span></button>')
    # Common part with the logo and the link to the main page
    if self._report.run.report_name is None or self._report.run.title == "":
      breadcrumb = '<a class="navbar-brand" href="%(url)s" style="padding:0;margin:0 5px;color:%(color)s">%(title)s</a>' % {'url': self._report.run.url, 'title': self._report.run.title, 'color': self._report.theme.greys[colorText]}
    else:
      breadcrumb = '<a class="navbar-brand" href="/reports/run/%(env)s" style="padding:0;margin:0 5px;color:%(color)s">%(env)s</a> / <a class="navbar-brand" href="%(url)s" style="padding:0;margin:0 5px;color:%(color)s">%(title)s</a>' % {
        'env': self._report.run.report_name, 'title': self._report.run.title, 'color': self._report.theme.greys[colorText], 'url': self._report.run.url}
    if self._report.logo is not None and self._report.logo.lower().endswith(".ico"):
      items.append('<a href="%s" style="line-height:30px;margin:0;padding:0 10px 0 0" class="navbar-brand"><img height="25px" title="Environement Home page" style="margin:0;padding:0" src="%s" /></a>%s' % (self._report._urlsApp['index'], self._logoUrl, breadcrumb))
    else:
      awesomeIcon = self._report.logo if self._report.logo is not None else "fab fa-whmcs"
      items.append('<a href="%s" class="navbar-brand" style="display:inline-block;vertical-align:middle;line-height:20px;padding:0;margin:3px 5px 0 0"><i class="%s" style="color:%s;font-size:24px"></i></a>%s' % (self._report._urlsApp['index'], awesomeIcon, self._report.theme.greys[colorText], breadcrumb))
    if self._report.run.url_root is not None:
      items.append('<div class="collapse navbar-collapse" id="navbarTogglerDemo02">')
      items.append('<ul class="navbar-nav ml-auto">')
      for name in self.definedOrder:
        section = self.categories.get(name, {})
        if len(section.get("content", [])) > 0:
          items.append('<li class="nav-item dropdown">')
          items.append('<a class="nav-link %s" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="margin:0 5px;white-space:nowrap;padding-top:10px;display:inline-block;color:%s">%s</a>' % (section['style'], self._report.theme.greys[colorText], name))
          items.append('<div class="dropdown-menu scroll_content" aria-labelledby="navbarDropdownMenuLink" style="max-height:500px;overflow:auto">')
          for s in section["content"]:
            if 'diviser' in s:
              items.append('<div class="dropdown-divider"></div>')
            elif 'header' in s:
              items.append('<div class="dropdown-header" style="font-weight:bold">%s</div>' % s['header'])
            elif 'group' in s:
              subItems = []
              for sub in s['group']:
                if not 'action' in sub:
                  sub['action'] = ""
                if not 'dsc' in sub:
                  sub['dsc'] = ""
                if not 'target' in sub:
                  sub['target'] = '_self'
                sub['size'] = self._report.pyStyleDfl['fontSize']
                subItems.append('<a class="dropdown-item" title="%(dsc)s" target="%(target)s" href="%(url)s" %(action)s style="font-size:%(size)s;color:inherit">%(name)s</a>' % sub)
              items.append("<div style='max-height:200px;overflow:auto' class='scroll_content'>%s</div>" % "".join(subItems))
              self._report.jsOnLoadFnc.add("$('.scroll_content').mCustomScrollbar()")
              self._report.jsImports.add('jquery-scrollbar')
              self._report.cssImport.add('jquery-scrollbar')
            else:
              if not 'action' in s:
                s['action'] = ""
              if not 'dsc' in s:
                s['dsc'] = ""
              if not 'target' in s:
                s['target'] = '_self'
              s['size'] = self._report.pyStyleDfl['fontSize']
              items.append('<a class="dropdown-item" title="%(dsc)s" target="%(target)s" href="%(url)s" %(action)s style="font-size:%(size)s;color:inherit">%(name)s</a>' % s)
          items.append('</div></li>')
      questionReport = ''
      if self.stackOverFlow is not None:
        questionReport = '''
          <a class="dropdown-item" target="_blank" href="%(urlReport)s/run/%(stackOverFlow)s" style="font-size:%(size)s"><i class="fas fa-question-circle" style="margin-right:10px"></i>Help</a>
          <a class="dropdown-item" target="_blank" href="%(urlReport)s/run/%(stackOverFlow)s/ideas" style="font-size:%(size)s"><i class="fas fa-comment-alt" style="margin-right:10px"></i>Send Feedback</a>''' % {'stackOverFlow': self.stackOverFlow, 'urlReport': self._report._urlsApp['report']}

      # The different SIGN IN Options in the framework
      if self.stype == 'controlled':
        items.append('''
           <li class="nav-item">
              <i class="nav-link fas fa-lock" style="color:%(color)s;margin:0 5px;padding-top:12px;display:inline-block" title="Controlled Access"></i></li>
           '''% {'color': self._report.theme.greys[colorText], 'urlAdmin': self._report._urlsApp['admin']})
      elif self.stype == 'owner':
        items.append('''
           <li class="nav-item">
              <a class="nav-link fas fa-lock" href="%(urlAdmin)s/access/%(reportName)s" style="color:%(color)s;white-space:nowrap;font-weight:bold;margin:0 5px;padding-top:12px;display:inline-block" target="_BLANK"></a></li>
           ''' % {'color': self._report.theme.greys[colorText], 'urlAdmin': self._report._urlsApp['admin'],
                  'reportName': self._report.run.report_name})
      elif self._report.run.current_user == 'anonymous':
        items.append('''
          <li class="nav-item">
            <a class="nav-link" href="%(urlAdmin)s/login" style="border:1px solid %(color)s;color:%(color)s;white-space:nowrap;font-weight:bold;margin:5px;display:inline-block;padding:4px 5px">SIGN IN</a>
          </li>''' % {'color': self._report.theme.greys[colorText], 'urlAdmin': self._report._urlsApp['admin']})
      else:
        items.append('''
          <li class="nav-item">
            <a class="nav-link" href="%(urlAdmin)s/logout" style="border:1px solid %(color)s;color:%(color)s;white-space:nowrap;font-weight:bold;margin:5px;display:inline-block;padding:4px 5px">SIGN OUT</a>
          </li>''' % {'color': self._report.theme.danger[1], 'urlAdmin': self._report._urlsApp['admin']})

      items.append('''
        <li class="nav-item dropdown">
          <a class="nav-link" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="color:%(color)s;margin:0 5px;padding-top:10px;display:inline-block"><i class="fas fa-ellipsis-v"></i></a>
          <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownMenuLink">
            <a class="dropdown-item" target="_blank" href="%(urlAdmin)s/user" style="font-size:%(size)s"><i class="fas fa-cogs" style="margin-right:10px"></i>Settings</a>
            <a class="dropdown-item" target="_blank" href="%(urlAdmin)s/systems" style="font-size:%(size)s"><i class="fas fa-bezier-curve" style="margin-right:10px"></i>Add-Ons</a>
            <a class="dropdown-item" href="#" id="epyk-nav-themes" role="button" data-toggle="dropdown" aria-expanded="true" aria-haspopup="true" style="font-size:%(size)s"><i class="fas fa-palette" style="margin-right:10px"></i>Themes</a>
            <div class="dropdown-menu" onclick="OpenDropDownThemes()" style="position:relative;z-index:2" aria-labelledby="epyk-nav-themes">
                %(Themes)s
            </div>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" target="_blank" href="%(urlReport)s/framework" style="font-size:%(size)s"><i class="fab fa-python" style="margin-right:10px"></i>Framework</a>
            %(stackOverFlow)s
            <div class="dropdown-divider"></div>
            <div class="dropdown-item" style="font-size:12px;">Mode: %(mode)s</div>
            <div class="dropdown-item" style="font-size:12px;">User Mode: %(user)s</div>
            <div class="dropdown-item" style="font-size:12px;">User Name: %(userName)s</div>
            <div class="dropdown-item" style="font-size:12px;">Updated: %(updateDt)s</div>
          </div>
        </li>
        ''' % {'color': self._report.theme.greys[colorText], 'size': self._report.pyStyleDfl['headerFontSize'], 'Themes': self.dropDownThemes(self._report.pyStyleDfl['headerFontSize']),
               'urlReport': self._report._urlsApp['report'], 'urlAdmin': self._report._urlsApp['admin'], 'userName': self._report.run.current_user,
               'user': self._report.run.current_user, 'mode': '%s (Local)' % self._report.run.url_root if self._report.run.is_local else '%s (Server)' % self._report.run.url_root,
               'updateDt': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), 'stackOverFlow': questionReport})

      items.append('</ul>')
      if self.searchEngine is not None:
        items.append('''
          <form class="form-inline my-2 my-md-0" style="position:relative">
            <span onclick="GoToReport('%(urlReport)s/run/%(search)s/index?value='+ $('#search_input').val(), true, false)" class="fas fa-search my-2 my-sm-0" style="position:absolute;font-size:15px;left:7px;top:6px;cursor:pointer"></span>
            <input onkeydown="if (event.keyCode == 13) {GoToReport('%(urlReport)s/run/%(search)s/index?value=' + $(this).val(), true, false)}" class="form-control" type="search" id="search_input" placeholder="Search" aria-label="Search" style="font-size:%(size)s;color:%(color)s;text-indent:30px;height:30px;background-color:%(bgColor)s;margin-right:5px">
          </form> ''' % {"urlReport": self._report._urlsApp['report'], 'search': self.searchEngine, 'bgColor': self._report.theme.greys[0], 'color': self._report.theme.greys[-1], 'size': self._report.pyStyleDfl['fontSize']})
        items.append('</div>')
    items.append('</nav>')
    self._report.jsOnLoadFnc.add('$("body").css("padding-top", "%spx")' % (self.lenght + 3))
    self._report.jsOnLoadFnc.add('function OpenDropDownThemes(){}')
    return "".join(items)



  def to_word(self, document): pass


class HtmlParamsBar(Html.Html):
  __reqCss, __reqJs = ['bootstrap'], ['bootstrap']
  _grpCls = CssGrpCls.CssGrpClassBase
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
  _grpCls = CssGrpCls.CssClassSideBarFixed

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
    # Add some specific styles for the sidebar items
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
