"""
Wrapper to the HTML tree components
"""

from epyk.core.html import HtmlList

# The list of CSS classes
from epyk.core.css.groups import CssGrpClsList


class OptionsTree(object):

  def __init__(self, src):
    self._icon_open, self._icon_close, self._expanded = "fas fa-folder-open", "fas fa-folder", True
    self.src = src

  @property
  def icon_open(self):
    """

    :return:
    """
    return self._icon_open

  @property
  def icon_close(self):
    """

    :return:
    """
    return self._icon_close

  @property
  def expanded(self):
    """

    :return:
    """
    return self._expanded

  @expanded.setter
  def expanded(self, bool):
    self._expanded = bool
    self.src.items = None
    self.src.set(self.src, self.src.val)

  @icon_open.setter
  def icon_open(self, icon):
    self._icon_open = icon
    self.src.items = []
    self.src.set(self.src, self.src.val)

  @icon_close.setter
  def icon_close(self, icon):
    self._icon_close = icon
    self.src.items = []
    self.src.set(self.src, self.src.val)


class Tree(HtmlList.List):
  name, category, callFnc = 'List Expandable', 'Lists', 'tree'

  def __init__(self, report, data, size, color, width, height, htmlCode, helper, profile):
    super(Tree, self).__init__(report, [], size, color, width, height, htmlCode, helper, profile)
    self._vals = data # Attach the original data anyway to the object
    self.options = OptionsTree(self)
    self.set(self, self.val)

  def empty(self):
    """"""
    return self

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
        ul[-1].add_icon(self.options.icon_open if self.options.expanded else self.options.icon_close)
        if not self.options.expanded:
          sub_l.css({"display": 'none'})
        ul[-1].icon.click([
          ul[-1].val.dom.toggle(),
          ul[-1].icon.dom.switchClass(self.options.icon_close.split(" ")[-1], self.options.icon_open.split(" ")[-1])])
        self.set(sub_l, l.get('items'))
      else:
        ul.add_item(l['label'])[-1].no_decoration
        ul[-1].css({"color": l.get('color', 'none')})
    return self

  def find(self, value):
    pass

  def nodes(self, level):
    """

    :param level:
    :return:
    """
    for i in self.items:
      print(i.items)

  def leafs(self):
    """

    :return:
    """
    pass


class TreeInput(Tree):
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
        ul[-1].add_icon(self.options.icon_open if self.options.expanded else self.options.icon_close)
        if not self.options.expanded:
          sub_l.css({"display": 'none'})
        ul[-1].icon.click([
          ul[-1].val.dom.toggle(),
          ul[-1].icon.dom.switchClass(self.options.icon_close.split(" ")[-1], self.options.icon_open.split(" ")[-1])])
        self.set(sub_l, l.get('items'))
      else:
        ul.add_item(self._report.ui.text(l['label']).editable().css({"width": 'none', 'min-width': 'none'}))[-1].no_decoration
        ul[-1].css({"color": l.get('color', 'none')})
    return self


class DropDown(HtmlList.List):
  alias, cssCls = 'dropdown', ['btn', 'dropdown-toggle']
  __reqCss, __reqJs = ['bootstrap'], ['bootstrap', 'jquery']
  _grpCls = CssGrpClsList.CssClassListDropDown
  name, category, callFnc = 'DropDown Select', 'Lists', 'dropdown'

  def __init__(self, report, data, size, color, width, height, htmlCode, helper, profile):
    super(DropDown, self).__init__(report, [], size, color, width, height, htmlCode, helper, profile)
    self.allowTableFilter, self._jsStyles = [], {"clearDropDown": True, 'dropdown_submenu': {},
      'a_dropdown_item': {'text-decoration': 'none', "color": 'inherit', 'font-size': self._report.pyStyleDfl['fontSize']}, # {"width": "100%", 'font-size': '12px', 'text-decoration': 'none', 'padding-left': "10px"},
      "li_dropdown_item": {"text-align": "left", 'font-size': self._report.pyStyleDfl['fontSize']}}
    self._vals = data
    self.css({"margin-top": "5px", "display": "inline-block"})
    self.set(self, self.val)
    #self.set_attrs(attrs={"class": ["dropdown-menu"], 'id': self.htmlId, 'aria-labelledby': 'dropdownMenu'})

  def set(self, ul, data):
    """

    :param ul:
    :param data:
    """
    for v in data:
      if v.get('items') is not None:
        sub_l = self._report.ui.list([]).set_attrs(attrs={"class": ["dropdown-menu"]})
        sub_l.inReport = False
        ul.add_item(sub_l)[-1].no_decoration
        ul[-1].set_attrs({"class": "dropdown-submenu"})
        ul[-1].add_link(v['label'], url="#", css={"width": "none"})
        #for i in v['items']:
        #  sub_l.add_item(i["label"])
        #  sub_l[-1].set_attrs({"class": ["dropdown-submenu", 'dropdown-menu-right']})
        self.set(sub_l, v.get('items'))
        #children.append("<a class='dropdown-item' tabindex='-1' href='#'>%s</a> %s" % (v['value'], sub_l))
      else:
        a = self._report.ui.link(v['label'], url="#")
        a.no_decoration
        ul.add_item(a)[-1].no_decoration
    #l.set_items(data=children, attrs={"class": ['dropdown-submenu', 'dropdown-menu-right']})
    return self

  @property
  def _js__builder__(self):
    return ''' 
        var jqHtmlObj = jQuery(htmlObj);
        if (options.clearDropDown) {jqHtmlObj.empty()};
        data.forEach(function(rec){
          if (rec._children != undefined) {
            var li = $('<li class="dropdown-submenu dropdown-menu-right"></li>').css(options.dropdown_submenu);
            var a = $('<a class="dropdown-item" tabindex="-1" href="#" style="display:inline-block"><span style="display:inline-block;float:left">'+ rec.value +'</span></a>').css(options.a_dropdown_item);
            li.append(a); var ul = $('<ul class="dropdown-menu"></ul>'); li.append(ul); options.clearDropDown = false;
            jqHtmlObj.append(li); %(pyCls)s(ul, rec._children, options)
          } else {
            if (rec.disable == true){jqHtmlObj.append('<li class="disabled"><a href="#">'+ rec.value +'</a></li>')}
            else {
              if (rec.url == undefined){var a = $('<a href="#">'+ rec.value +'</a>')}
              else {var a = $('<a href="'+ rec.url +'">'+ rec.value +'</a>')}
              a.css(options.a_dropdown_item);
              var li = $('<li class="dropdown-item"></li>').css(options.dropdown_submenu);
              li.append(a); jqHtmlObj.append(li)}}
        })''' % {"pyCls": self.__class__.__name__}

  # def __str__(self):
  #   # [s for s in self.defined if not s.startswith("CssDropDown")]
  #   items, children = [], []
  #   l = self._report.ui.list([])
  #   l.inReport = False
  #   for v in self.val:
  #     if v.get('items') is not None:
  #       sub_l = self._report.ui.list([])
  #       sub_l.inReport = False
  #       a = self._report.ui.link("test 2", url="#").set_attrs({"class": ["dropdown-item"], 'tabindex': -1})
  #       a.inReport = False
  #       for i in v['items']:
  #         sub_l.add_item(i["label"], attrs={"class": ["dropdown-submenu", 'dropdown-menu-right']})
  #       sub_l.set_attrs(attrs={"class": ["dropdown-menu"]})
  #       children.append("<a class='dropdown-item' tabindex='-1' href='#'>%s</a> %s" % (v['value'], sub_l))
  #     else:
  #       children.append(v['label'])
  #   l.set_items(data=children, attrs={"class": ['dropdown-submenu', 'dropdown-menu-right']})
  #   l.set_attrs(attrs={"class": ["dropdown-menu"], 'id': self.htmlId, 'aria-labelledby': 'dropdownMenu'})
  #   items.append(l)
  #   return '''
  #     <div class="dropdown" %(cssAttr)s>
  #       <button id="%(htmlId)s_button" style="font-size:%(size)s;width:100%%;height:100%%;background-color:%(darkBlue)s;color:%(color)s" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">%(title)s<span class="caret"></span></button>
  #       %(val)s
  #     </div> ''' % {'cssAttr': self.get_attrs(withId=False, pyClassNames=self.defined), 'title': self.title, 'htmlId': self.htmlId,
  #                   'darkBlue': self.getColor('colors', 7), 'color': self.getColor('greys', 0), 'size': self.size,
  #                   'val': "".join([str(l) for l in items])}

  def to_word(self, document):
    p = document.add_paragraph()
    p.add_run("Selected: ")
    runner = p.add_run(self._report.http.get(self.htmlCode, self.vals))
    runner.bold = True

  def to_xls(self, workbook, worksheet, cursor):
    if self.htmlId in self._report.http:
      cellTitle = self.title if self.title != "" else 'Input'
      cell_format = workbook.add_format({'bold': True})
      worksheet.write(cursor['row'], 0, cellTitle, cell_format)
      cursor['row'] += 1
      worksheet.write(cursor['row'], 0, self._report.http[self.htmlId])
      cursor['row'] += 2
