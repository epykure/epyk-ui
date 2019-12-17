"""
Wrapper to the HTML tree components
"""

import json

from epyk.core.html import Html
from epyk.core.html import HtmlList

# The list of CSS classes
from epyk.core.css.groups import CssGrpClsList


class Tree(HtmlList.List):
  name, category, callFnc = 'List Expandable', 'Lists', 'tree'
  #_grpCls = CssGrpClsList.CssClassListTree

  def __init__(self, report, data, size, color, width, height, htmlCode, helper, profile):
    super(Tree, self).__init__(report, [], size, color, width, height, htmlCode, helper, profile)
    self.options = {"expand": True, "icon_open": "fas fa-folder-open", "icon_close": "fas fa-folder"}
    self.set(self, data)

  def set(self, ul, data):
    """

    :param ul:
    :param data:
    """
    for l in data:
      if l.get('items') is not None:
        sub_l = self._report.ui.list()
        sub_l.inReport = False
        ul.add_item(sub_l)[-1].no_decoration
        ul[-1].add_label(l['label'], css={"color": l.get('color', 'none')})
        ul[-1].add_icon(self.options["icon_open"] if self.options.get("expand", True) else self.options["icon_close"])
        if not self.options.get("expand", True):
          sub_l.css({"display": 'none'})
        ul[-1].icon.click([
          ul[-1].val.dom.toggle(),
          ul[-1].icon.dom.switchClass(self.options["icon_close"].split(" ")[-1], self.options["icon_open"].split(" ")[-1])])
        self.set(sub_l, l.get('items'))
      else:
        ul.add_item(l['label'])[-1].no_decoration
        ul[-1].css({"color": l.get('color', 'none')})
    return self


class TreeOld(Html.Html):
  name, category, callFnc = 'List Expandable', 'Lists', 'tree'
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome', 'jquery']
  _grpCls = CssGrpClsList.CssClassListTree

  def __init__(self, report, recordSet, width, height, title, htmlCode, draggable, dataSrc, expand, profile):
    self.dataSrc, self.title, self.expand = None, title, expand
    self._jsActions, self._definedActions = {}, ['add', 'save', 'refresh', 'delete']
    if recordSet is None:
      if dataSrc is None:
        recordSet = []
      else:
        self.report, self.dataSrc = report, dataSrc
        if dataSrc.get('on_init', False):
          recordSet = self.onInit(None, dataSrc)
    super(TreeOld, self).__init__(report, recordSet, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                                   htmlCode=htmlCode, dataSrc=dataSrc, profile=profile)
    self.css({"padding-left": "5px"})
    self.cssSelected = self._report.style.cssName("CssBasicListItemsSelected")
    # The flag start in _jsStyles is only used in the javascript recursion
    self._jsStyles = {'style': {"text-decoration": "none", "padding": 0, "margin": 0, "list-style-position": 'inside'}, 'start': True,
                      'icons': {'close': 'fas fa-folder', 'open': 'fas fa-folder-open'}, 'reset': True, 'draggable': draggable}
    #self.jsFrg('click', ''' event.stopPropagation(); $('#%(htmlId)s li span[name=value],a').removeClass('%(cssSelected)s');
    #    $(event.currentTarget).addClass('%(cssSelected)s')
    #  ''' % {'htmlCode': self.htmlCode, 'htmlId': self.htmlId, 'cssSelected': self.cssSelected})
    if dataSrc is not None and dataSrc['type'] in ["script", 'url']:
      # TODO To extend to internal flask calls
      self.jsAction(action='refresh', icon='fas fa-sync-alt', pyCssCls="CssSmallIcon", tooltip="Refresh the tree", url=self.dataSrc.get('script', self.dataSrc.get('url', '')),
                    jsData=self.dataSrc.get('htmlObjs'), jsFncs=['var styles_%(htmlId)s = %(jsStyles)s; styles_%(htmlId)s.forceSelect = $("#%(htmlId)s").find(".%(cssSelected)s").first().text()' % {'cssSelected': self.cssSelected, "jsStyles": json.dumps(self._jsStyles), "htmlId": self.htmlId},
                                                                 self.jsGenerate(jsStyles="styles_%s" % self.htmlId)], httpCodes=self.dataSrc.get('httpCodes'))
    self._report.style.add('CssBasicListItemsSelected')

  @property
  def jsQueryData(self):
    return "{event_parent: $(event.currentTarget).parent('li').parent('ul').siblings('span[name=value]').text(), event_val: $(event.currentTarget).text(), event_dsc: $(event.currentTarget).next().text(), event_code: '%s'}" % self.htmlId

  @property
  def val(self):
    return '$("#%s").find(".%s").first().text()' % (self.htmlId, self.cssSelected)

  @property
  def eventId(self): return "$('#%s li span[name=value],a')" % self.htmlId

  def builder_options(self, attrs):
    """

    :param attrs:
    :return:
    """
    jsStyle = dict(self._jsStyles) if self._jsStyles is not None else {}
    jsStyle.update(attrs)
    return jsStyle

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' 
      if (jsStyles.start == true && !Array.isArray(data)) {
        tmpData = []; jsStyles.start = false;
        for (var key in data){
          var row = {'label': key, 'items': []}; data[key].forEach(function(val) {row['items'].push( {'label': val})});
          tmpData.push(row)}
        data = tmpData};
      if (jsStyles.reset) {htmlObj.empty()}; var ul = $("<ul style='margin:0 0 0 10px;padding:0'></u>"); var resetFlag = jsStyles.reset;
      if (jsStyles.draggable) {ul.addClass("list_draggable")};
      data.forEach(function(rec){ 
        var content = rec.label; 
        if (rec.color != undefined) {jsStyles.style.color = rec.color} else {jsStyles.style.color = "%(blackColor)s"}
        if (rec.icon != '' && rec.icon != undefined) {content = '<i style="margin-left:5px;margin-right:5px" class="'+ rec.icon +'"></i>'+ rec.label}
        var li = $('<li name="expandable"></li>').css(jsStyles.style); 
        if (rec.url != undefined) {li.append('<a style="display:inline-block;text-decoration:none" href="'+ rec.url +'" target="_blank">'+ content +'</a>')}
        else {
          var labelDom = $('<span name="value">'+ content +'</span>'); li.append(labelDom);
          if (rec.dsc !== undefined){li.append('<p style="cursor:default;font-style:italic;display:inline-block;margin:0 0 0 10px;padding:0;color:%(lightColor)s">'+ rec.dsc +'</p>')};
          if (rec.dblclick !== undefined){labelDom.dblclick(function(){var data = $(this).text(); eval(rec.dblclick)})}
        }; jsStyles.reset = false;
        if (rec.items != undefined) { 
          li.css({'list-style-type':'none', 'list-style-image':'none', 'cursor': 'pointer'});
          var span = $('<span data-close="'+ jsStyles.icons.close +'" data-open="'+ jsStyles.icons.open +'" class="'+ jsStyles.icons.open +'" style="margin-right:5px"></span>');
          span.attr('name', 'section'); li.prepend(span);
          ul.append(li); htmlObj.append(ul);
          %(jsFnc)s(li, rec.items, jsStyles)}
        else if(rec.selects != undefined) {
          li.css({'list-style-type':'none', 'list-style-image':'none', 'cursor': 'pointer'});
          var span = $('<span data-close="'+ jsStyles.icons.close +'" data-open="'+ jsStyles.icons.open +'" class="'+ jsStyles.icons.open +'" style="margin-right:5px"></span>' );
          span.attr('name', 'section'); li.prepend(span);
          var select = $('<select></select>').css({"margin-left": '5px'});
          rec.selects.forEach(function(s){select.append('<option value="'+ s +'">'+ s +'</option>')});
          if (typeof rec.event !== "undefined"){
            select.change(function() {var data = {'val': $(this).val()}; var li = $(this).parent().first()[0]; 
              while (li.childNodes.length > 3) {li.removeChild(li.lastChild)}; var result = eval(rec.event); 
              %(jsFnc)s($(this).parent(), result.new, jsStyles)})};
          li.append(select); ul.append(li); htmlObj.append(ul);
        } else{
          if (jsStyles.forceSelect != undefined) {
            if (jsStyles.forceSelect == rec.label) {li.find('span').addClass('%(cssSelected)s'); jsStyles.forceSelect = undefined}};
          li.css({'list-style-type':'none', 'list-style-image': 'none'});
          ul.append(li); htmlObj.append(ul)}}); 
      if (jsStyles.draggable){
        ul.sortable({placeholder: "ui-state-highlight", dropOnEmpty: true, start: function(event, ui) {},
                    stop: function(event, ui) {}, connectWith: '.list_draggable'}).disableSelection()}
      ''' % {'cssSelected': self.cssSelected, 'jsFnc': self.__class__.__name__, 'blackColor': self.getColor("greys", 9),
             'lightColor': self.getColor("colors", 5)}, 'Javascript Object builder' )

  def jsEvents(self):
    if hasattr(self, 'jsFncFrag'):
      for eventKey, fnc in self.jsFncFrag.items():
        if self.htmlCode is not None:
          fnc.insert(0, self.jsAddUrlParam(self.htmlCode, self.val, isPyData=False))
        self._report.jsOnLoadEvtsFnc.add('''
          $('body').on('%(eventKey)s', '#%(htmlId)s li span[name=value], #%(htmlId)s li a', function(event) {
            var useAsync = false; var data = %(data)s;
            %(jsInfo)s; %(jsFnc)s; 
            if (!useAsync) {
              var body_loading_count = parseInt($('#body_loading span').text()); $('#body_loading span').html(body_loading_count - 1);
              if ($('#body_loading span').html() == '0') {$('#body_loading').remove()}}
          })''' % {'htmlId': self.htmlId, 'eventKey': eventKey, 'data': self.jsQueryData, 'jsFnc': ";".join([f for f in fnc if f is not None]),
                   'jsInfo': self._report.jsInfo('process(es) running', 'body_loading')})

  def __str__(self):
    self._report.jsOnLoadFnc.add('''
      $(document).on('click', 'span[name=section]', function(event) {
        $(this).parent().children().not(":nth-child(0)").not("select").not(":nth-child(1)").not(":nth-child(2)").toggle('fast'); 
        if ($(this).attr('class') == $(this).data('open')){ $(this).attr('class', $(this).data('close'))} 
        else {$(this).attr('class', $(this).data('open'))}});
      $("span[name=section]").trigger("click")''')
    if self.expand:
      self._report.jsOnLoadFnc.add('$("#%s span[name=section]").trigger("click")' % self.htmlId)
    events = []
    for action in self._definedActions:
      if action in self._jsActions:
        events.append(self._jsActions[action])
    return '''
      <div style="width:100%%;margin:5px 0 0 5px">
        <span style='font-weight:bold;font-size:14px'>%(title)s</span>
        <div style="width:100%%">%(events)s</div>
      </div>
      <div %(strAttr)s></div>%(helper)s''' % {'title': self.title, 'strAttr': self.get_attrs(pyClassNames=self.defined), 'helper': self.helper, 'events': "".join(events)}

  def setSelected(self, value):
    self._jsStyles["forceSelect"] = value
    if self.htmlCode is not None:
      self._report.jsOnLoadEvtsFnc.add(self.jsAddUrlParam(self.htmlCode, value, isPyData=True))
    return self

  def dblclick(self, jsFncs="", childOnly=True):
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.jsFrg('dblclick', ''' 
      if($(event.currentTarget).prev().attr('name') != 'section'){
        var text = $(event.currentTarget).text(); $(event.currentTarget).text(''); input = $("<input type='text'>");
        input.val(text); input.appendTo($(event.currentTarget)).focus();
        input.focusout(function(){
          if($(this).val() == ''){$(event.currentTarget).text(text); data.event_val = $(this).val()} 
          else{$(event.currentTarget).text($(this).val()); data.event_val = $(this).val()}; 
          $(this).remove(); %(jsFncs)s; 
          if(%(htmlCode)s != null){%(breadCrumbVar)s['params'][%(htmlCode)s] = data.event_val}
        }); 
        input.keypress(function(e){
            if(e.which == 13) { $(this).trigger("focusout");}
            if(e.keyCode == 27) { $(this).val('') ;$(this).trigger("focusout")}
        })}
      ''' % {"jsFncs": ';'.join(jsFncs), 'breadCrumbVar': self._report.jsGlobal.breadCrumVar, 'htmlCode': json.dumps(self.htmlCode)})

  def jsAction(self, action, icon, pyCssCls, tooltip, url=None, jsData=None, jsFncs=None, httpCodes=None):
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs] if jsFncs is not None else []

    # Add this to an ajax POST call if an URL is defined
    self.css({"cursor": "pointer"})
    fnc = self._report.jsPost(url=url, jsData=jsData, jsFnc=jsFncs, httpCodes=httpCodes) if url is not None else ";".join(jsFncs)
    self._report.style.cssCls(pyCssCls)
    self._jsActions[action] = "<span id='%(htmlId)s_%(action)s' title='%(tooltip)s' class='%(cssStyle)s %(icon)s'></span>" % {
      "icon": icon, "cssStyle": self._report.style.cssName(pyCssCls), "htmlId": self.htmlId, 'tooltip': tooltip, 'action': action}
    self._report.jsOnLoadFnc.add("$('#%(htmlId)s_%(action)s').on('click', function(event) { %(jsFncs)s; })" % {"htmlId": self.htmlId, "jsFncs": fnc, 'action': action})
    if action not in self._definedActions:
      self._definedActions.append(action)
    return self

  def removeNode(self, jsFncs=None, url=None, jsData=None, httpCodes=None):
    """
    Set the function to add a new node to a tree object. This function needs to be defined in order to set the
    corresponding javascript function used in the browser

    :return: The python object itself
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs] if jsFncs is not None else []
    jsFncs.append(''' console.log($('#%(htmlId)s').find(".%(cssSelected)s").first().parent());
      var selectedItem = $('#%(htmlId)s').find(".%(cssSelected)s").first(); var selectedVal = selectedItem.text();
      var selectedParentVal = selectedItem.parent('li').parent('ul').siblings('span[name=value]').text();
      if (selectedVal != ''){
        var data = {event_parent: selectedParentVal, event_val: selectedVal, htmlId: '%(htmlId)s'}; selectedItem.parent().remove();
      }''' % {'breadCrumVar': self._report.jsGlobal.breadCrumVar, 'htmlId': self.htmlId, 'cssSelected': self.cssSelected})
    return self.jsAction(action='delete', icon='far fa-trash-alt', pyCssCls="CssSmallIconRed", tooltip="Remove selected node", url=url,
                         jsData=jsData, jsFncs=jsFncs, httpCodes=httpCodes)

  def addNode(self, jsFncs="", url=None, jsData="NewScript.py", httpCodes=None, nodeId=0, icon="far fa-file-alt"):
    """
    Set the function to add a new node to a tree object. This function needs to be defined in order to set the
    corresponding javascript function used in the browser

    :return: The python object itself
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs] if jsFncs is not None else []
    jsIcon = '' if icon is None else '<i style="margin-left:5px;margin-right:5px" class="far fa-file-alt"></i>'
    jsFncs.append('''var li = $('<li name="expandable"></li>').css(%(jsStyles)s.style);
      li.css({'list-style-type':'none', 'list-style-image':'none', 'cursor': 'pointer' });
      li.append('%(jsIcon)s<span name="value">%(jsData)s</span>');
      if($('#%(htmlId)s ul').get(0) == undefined){var ul = $("<ul style='margin:0 0 0 10px;padding:0'></u>"); $('#%(htmlId)s').append(ul) ;};
      $($('#%(htmlId)s ul').get(%(nodeId)s)).append(li);
      ''' % {'jsStyles': json.dumps(self._jsStyles), 'jsData': jsData, 'htmlId': self.htmlId, 'jsFncs': ';'.join(jsFncs), 'nodeId': nodeId, "jsIcon": jsIcon})
    return self.jsAction(action='add', icon='fas fa-plus', pyCssCls="CssSmallIcon", tooltip="Add new node to a Tree object", url=url, jsData=jsData, jsFncs=jsFncs, httpCodes=httpCodes)

  def save(self, jsFncs="", url=None, jsData="NewScript.py", httpCodes=None):
    """
    :return: The python object itself
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs] if jsFncs is not None else []
    return self.jsAction(action='save', icon='far fa-hdd', pyCssCls="CssSmallIcon",
                         tooltip="Save an empty file on the drive", url=url, jsData=jsData, jsFncs=jsFncs,
                         httpCodes=httpCodes)

  def refresh(self, jsFncs=None, url=None, jsData=None, httpCodes=None):
    """
    :return: The python object itself
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs] if jsFncs is not None else []
    jsFncs.append(self.jsGenerate(None))
    return self.jsAction(action='refresh_tree', icon='fas fa-sync-alt', pyCssCls="CssSmallIcon",
                         tooltip="Refresh the tree", url=url, jsData=jsData, jsFncs=jsFncs, httpCodes=httpCodes)

  def to_word(self, document):
    pass


