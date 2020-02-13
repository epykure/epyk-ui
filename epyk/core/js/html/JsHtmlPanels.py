"""

"""


from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.fncs import JsFncs


class JsHtmlPanel(JsHtml.JsHtml):
  pass


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
    panel = JsHtmlPanel(self._src, report=self._report)
    panel.varName = "%s.querySelector('.row').querySelector('div:nth-child(%s)')" % (self.varId, i)
    return panel

  @property
  def panels(self):
    for i, _ in enumerate(self._src.colsDim):
      yield self.panel(i)

    return ""

  def togglePanel(self, i):
    """

    :param i:
    :return:
    """
    return '''
      %(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display = 'none'
      ''' % {'compId': self.varId, 'i': i}


class JsHtmlTabs(JsHtml.JsHtml):

  def add_tab(self, name):
    return JsFncs.JsFunctions([
      JsObjects.JsNodeDom.JsDoms.new("div", varName="new_table"),
      JsObjects.JsNodeDom.JsDoms.new("div", varName="new_table_content"),
      JsObjects.JsNodeDom.JsDoms.get("new_table").css({"width": "100px", "display": 'inline-block'}),
      JsObjects.JsNodeDom.JsDoms.get("new_table_content").innerText(name),
      JsObjects.JsNodeDom.JsDoms.get("new_table_content").css(self._src.css_tab),
      JsObjects.JsNodeDom.JsDoms.get("new_table_content").css({"padding": '5px 0'}),
      JsObjects.JsNodeDom.JsDoms.get("new_table").appendChild(JsObjects.JsObjects.get("new_table_content")),
      self.querySelector("div").appendChild(JsObjects.JsObjects.get("new_table")),
     ])
    #return self._report.js.console.log( self._report.js.getElementsByName(self._src.tabs_name).length )

  def tab(self, i):
    """
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
    Return the index of the selected tab

    :return:
    """
    return JsObjects.JsObjects.get("%s.querySelector('div[data-selected=true').getAttribute('data-index')" % self.varId)

  @property
  def selected_name(self):
    """
    Return the name of the selected tab
    :return:
    """
    return JsObjects.JsObjects.get("%s.querySelector('div[data-selected=true').innerHTML" % self.varId)

  @property
  def deselect_tabs(self):
    """
    Deselect all the tabs in the component

    :return:
    """
    return JsFncs.JsFunctions([
      self._report.js.getElementsByName(self._src.tabs_name).all([
        self._report.js.data.all.element.setAttribute("data-selected", False)
      ])
    ])
