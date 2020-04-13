
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.fncs import JsFncs


class JsHtmlPanel(JsHtml.JsHtml):
  pass


class JsHtmlTr(JsHtml.JsHtml):
  display_value = "table-row"


class JsHtmlRow(JsHtml.JsHtml):
  display_value = "flex"


class JsHtmlGrid(JsHtml.JsHtml):

  @property
  def val(self):
    """

    :return:
    """
    return self._src.input.dom.val

  @property
  def content(self):
    return self._src.input.dom.content

  def panel(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i:
    """
    panel = JsHtmlPanel(self._src, report=self._report)
    panel.varName = "%s.querySelector('.row').querySelector('div:nth-child(%s)')" % (self.varId, i+1)
    return panel

  @property
  def panels(self):
    for i, _ in enumerate(self._src.colsDim):
      yield self.panel(i)

    return ""

  def togglePanel(self, i):
    """
    Description:
    ------------
    Toggle the display of the column in a grid component.
    Teh other columns will be resized accordingly

    Attributes:
    ----------
    :param i: Integer. The column number (start at 0)

    :return:
    """
    return '''
      if(%(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display == 'none'){
        %(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display = 'block'
      } else {%(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display = 'none'}
      ''' % {'compId': self.varId, 'i': i+1}


class JsHtmlTabs(JsHtml.JsHtml):

  def add_tab(self, name):
    return JsFncs.JsFunctions([
      JsObjects.JsNodeDom.JsDoms.new("div", varName="new_table"),
      JsObjects.JsNodeDom.JsDoms.new("div", varName="new_table_content"),
      JsObjects.JsNodeDom.JsDoms.get("new_table").css({"width": "100px", "display": 'inline-block', "vertical-align": "middle", "box-sizing": 'border-box',
                                                       'text-align': 'left'}),
      JsObjects.JsNodeDom.JsDoms.get("new_table_content").innerText(name),
      JsObjects.JsNodeDom.JsDoms.get("new_table_content").setAttribute("name", self._src.tabs_name),
      JsObjects.JsNodeDom.JsDoms.get("new_table_content").css({"width": "100px"}),
      JsObjects.JsNodeDom.JsDoms.get("new_table_content").css(self._src.options.css_tab),
      JsObjects.JsNodeDom.JsDoms.get("new_table_content").css({"padding": '5px 0'}),
      JsObjects.JsNodeDom.JsDoms.get("new_table").appendChild(JsObjects.JsObjects.get("new_table_content")),
      JsObjects.JsNodeDom.JsDoms.new("div", varName="tab_container"),
      self.querySelector("div").appendChild(JsObjects.JsObjects.get("new_table")),
     ])

  def tab(self, i):
    """
    Description:
    ------------
    Return the Javascript tab object

    Example
    tab.dom.tab(3).firstChild.css({"color": 'red'})

    :param i: Integer. Starting from 0 as we keep the Python indexing as reference
    :return:
    """
    return JsObjects.JsNodeDom.JsDoms.get("%s.firstChild.querySelector('div:nth-child(%s)')" % (self.varId, i+1))

  @property
  def selected_index(self):
    """
    Description:
    ------------
    Return the index of the selected tab

    :return: The index or -1
    """
    return JsObjects.JsObjects.get('''
      (function(node){ var selectedTab = node.querySelector('div[data-selected=true'); 
        if(selectedTab == null){ return -1; }
        else{ return selectedTab.getAttribute('data-index')}
      })(%s)''' % self.varId)

  @property
  def selected_name(self):
    """
    Description:
    ------------
    Return the name of the selected tab

    :return: The HTML content or an emtpy string
    """
    return JsObjects.JsObjects.get('''
          (function(node){ var selectedTab = node.querySelector('div[data-selected=true'); 
            if(selectedTab == null){ return ""; }
            else{ return selectedTab.innerHTML}
          })(%s)''' % self.varId)

  def deselect_tabs(self):
    """
    Description:
    ------------
    Deselect all the tabs in the component

    :return:
    """
    return JsFncs.JsFunctions([
      self._report.js.getElementsByName(self._src.tabs_name).all([
        self._report.js.data.all.element.setAttribute("data-selected", False),
        self._report.js.getElementsByName(self._src.tabs_name).all([
          self._report.js.data.all.element.css(self._src.options.tab_not_clicked_style())])
      ])
    ])
