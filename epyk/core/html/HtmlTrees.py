
from epyk.core.html import HtmlList
from epyk.core.html import Html
from epyk.core.html import Defaults

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery

from epyk.core.html.options import OptTrees

from epyk.core.css.styles import GrpClsList


class Tree(HtmlList.List):
  name, category, callFnc = 'List Expandable', 'Lists', 'tree'

  def __init__(self, report, data, color, width, height, htmlCode, helper, option, profile):
    super(Tree, self).__init__(report, [], color, width, height, htmlCode, helper, {}, profile)
    self._vals = data # Attach the original data anyway to the object
    self.__options = OptTrees.OptionsTree(self, option)
    self.set(self, self.val)

  @property
  def options(self):
    """

    :rtype: OptTrees.OptionsTree
    """
    return self.__options

  def empty(self):
    """

    :return:
    """
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
        ul[-1].add_label(l.get('label', l.get('value', '')), css={"color": l.get('color', 'none')})
        ul[-1].add_icon(self.options.icon_open if self.options.expanded else self.options.icon_close)
        if not self.options.expanded:
          sub_l.css({"display": 'none'})
        ul[-1].icon.click([
          ul[-1].val.dom.toggle(),
          ul[-1].icon.dom.switchClass(self.options.icon_close.split(" ")[-1], self.options.icon_open.split(" ")[-1])])
        self.set(sub_l, l.get('items'))
      else:
        ul.add_item(l.get('label', l.get('value', '')))[-1].no_decoration
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


class DropDown(Html.Html):
  __reqCss, __reqJs = ['bootstrap'], ['bootstrap', 'jquery']
  name, category, callFnc = 'DropDown Select', 'Lists', 'dropdown'

  def __init__(self, report, data, text, width, height, htmlCode, helper, options, profile):
    self.__options = {}
    super(DropDown, self).__init__(report, text, code=htmlCode, profile=profile, css_attrs={"width": width, "height": height})
    self._vals, self.text = data, text
    self.css({'padding': 0, 'margin': "1px", "display": "block", "z-index": 10, 'cursor': 'pointer', 'position': 'relative'})
    self._jsStyles = {"a": {'text-decoration': 'none', 'line-height': '%spx' % Defaults.LINE_HEIGHT, 'padding': '0 10px', "width": '%spx' % options.get("width")},
                      "ul": {"left": "%spx" % options.get("width")}}
    self.__options = OptTrees.OptDropDown(self, options)

  @property
  def style(self):
    """
    Description:
    -----------

    :rtype: GrpClsList.ClassDropDown
    """
    if self._styleObj is None:
      self._styleObj = GrpClsList.ClassDropDown(self)
    return self._styleObj

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for a dropdown

    :rtype: OptTrees.OptDropDown
    """
    return self.__options

  def click(self, jsFncs, profile=False):
    if not isinstance(jsFncs, list):
      jsFncs = []
    self._jsStyles['click'] = "function(event, value){%s} " % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  @property
  def _js__builder__(self):
    return ''' 
      var jqHtmlObj = %(jqId)s; if(options.clearDropDown){jqHtmlObj.empty()};
      data.forEach(function(rec){
        if (rec.items != undefined) {
          var li = $('<li class="dropdown" style="list-style-type:none;display:list-item;text-align:-webkit-match-parent"></li>'); var a = $('<a tabindex=-1>'+ rec.value +'<span class="caret"></span></a>');
          li.append(a); var ul = $('<ul class="submenu"></ul>'); ul.css(options.ul); options.clearDropDown = false; a.css(options.a);
          %(pyCls)s(ul, rec.items, options); li.append(ul); jqHtmlObj.append(li);
        } else {
          if (rec.url == undefined){var a = $('<a href="#">'+ rec.value +'</a>')}
          else {var a = $('<a href="'+ rec.url +'">'+ rec.value +'</a>')}; a.css(options.a);
          a.click(function(event){const value = a.html(); options.click(event, value)} );
          var li = $('<li style="list-style-type:none;display:list-item;text-align:-webkit-match-parent"></li>'); li.append(a); jqHtmlObj.append(li)}
      })''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False), "pyCls": self.__class__.__name__}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<ul %s></ul>" % (self.get_attrs(pyClassNames=self.style.get_classes()))

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
