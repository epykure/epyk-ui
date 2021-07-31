
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.fncs import JsFncs
from epyk.core.js import JsUtils


class JsHtmlPanel(JsHtml.JsHtml):

  def __init__(self, data, varName=None, setVar=False, isPyData=False, report=None, src=None):
    super(JsHtmlPanel, self).__init__(data, varName, setVar, isPyData, report)
    if varName is not None:
      self.varName = varName

  def select(self):
    return self.firstChild.events.trigger("click")


class JsHtmlSlidingPanel(JsHtml.JsHtml):

  def close(self):
    """
    Description:
    ------------
    Close the sliding panel.
    """
    return JsFncs.JsFunctions([
      self._report.js.if_(self._src.icon.dom.content.toString().indexOf(self._src.options.icon_expanded.split(" ")[-1]) >= 0, [
        self._report.js.getElementsByName("panel_%s" % self.htmlCode).first.toggle(),
        self._src.icon.dom.switchClass(self._src.options.icon_expanded, self._src.options.icon_closed)
      ])
    ])

  def open(self):
    """
    Description:
    ------------
    Open the sliding panel.
    """
    return JsFncs.JsFunctions([
      self._report.js.if_(self._src.icon.dom.content.toString().indexOf(self._src.options.icon_closed.split(" ")[-1]) >= 0, [
        self._report.js.getElementsByName("panel_%s" % self.htmlCode).first.toggle(),
        self._src.icon.dom.switchClass(self._src.options.icon_closed, self._src.options.icon_expanded)
      ])
    ])

  def set_title(self, jsData, options=None):
    """
    Description:
    ------------
    Set the component title.

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    return self._src.title[1].build(jsData, options=options)

  def set_icon(self, jsData, css=None, options=None):
    """
    Description:
    ------------
    Set the icon from Font-awesome options.

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    :param css: Dictionary. Optional. The CSS attributes to be added to the HTML component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    if css is not None:
      return self._src.title[0].build(jsData, options={"css": css})

    return self._src.title[0].build(jsData, options=options)


class JsHtmlTr(JsHtml.JsHtml):
  display_value = "table-row"


class JsHtmlRow(JsHtml.JsHtml):
  display_value = "flex"


class JsHtmlGrid(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------
    Return the underlying input values.
    """
    return self._src.input.dom.val

  @property
  def content(self):
    """
    Description:
    ------------
    Return the underlying input content.
    """
    return self._src.input.dom.content

  def panel(self, i):
    """
    Description:
    ------------
    Return the underlying panel object.

    Attributes:
    ----------
    :param i: Integer. The panel index.
    """
    panel = JsHtmlPanel(self._src, report=self._report)
    panel.varName = "%s.querySelector('.row').querySelector('div:nth-child(%s)')" % (self.varId, i+1)
    return panel

  @property
  def panels(self):
    """
    Description:
    ------------
    Iterator on the various available panels.
    """
    for i, _ in enumerate(self._src.colsDim):
      yield self.panel(i)

    return ""

  def togglePanel(self, i):
    """
    Description:
    ------------
    Toggle the display of the column in a grid component.
    Thw other columns will be resized accordingly.

    Attributes:
    ----------
    :param i: Integer. The column number (start at 0).
    """
    return '''
      if(%(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display == 'none'){
        %(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display = 'block'
      } else {%(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display = 'none'}
      ''' % {'compId': self.varId, 'i': i+1}


class JsHtmlTabs(JsHtml.JsHtml):

  def __getitem__(self, i):
    return JsHtmlPanel(
      self, src=self._src, varName="%s.firstChild.querySelector('div:nth-child('+ (parseInt(%s)+1) + ')')" % (
        self.varId, i), report=self._report)

  def add_tab(self, name):
    """
    Description:
    ------------
    Add a tab to the panel.

    Attributes:
    ----------
    :param name: String. The name of the new tab.
    """
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
    Return the Javascript tab object.

    Usage::

      tab.dom.tab(3).firstChild.css({"color": 'red'})

    Attributes:
    ----------
    :param i: Integer. Starting from 0 as we keep the Python indexing as reference.
    """
    return JsObjects.JsNodeDom.JsDoms.get("%s.firstChild.querySelector('div:nth-child(%s)')" % (self.varId, i+1))

  def set_tab_name(self, i, name):
    """
    Description:
    ------------
    Change the name for a specific panel.

    Attributes:
    ----------
    :param i: Integer. The panel index.
    :param name: String. The panel name.
    """
    name = JsUtils.jsConvertData(name, None)
    return JsObjects.JsNodeDom.JsDoms.get(
      "%s.firstChild.querySelector('div:nth-child(%s)').querySelectorAll('[name=%s]')[0].innerHTML = %s" % (self.varId, i+1, self._src.tabs_name, name))

  @property
  def selected_index(self):
    """
    Description:
    ------------
    Return the index of the selected tab.

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
    Return the name of the selected tab.

    :return: The HTML content or an emtpy string.
    """
    return JsObjects.JsObjects.get('''
          (function(node){ var selectedTab = node.querySelector('div[data-selected=true'); 
            if(selectedTab == null){ return ""; }
            else{ return selectedTab.innerHTML}
          })(%s)''' % self.varId)

  @property
  def content(self):
    """
    Description:
    -----------
    Standard property to get the component value.
    """
    return JsHtml.ContentFormatters(self._report, '''
          (function(node){ var selectedTab = node.querySelector('div[data-selected=true'); 
            if(selectedTab == null){ return ""; }
            else{ var attrVal = null;
              if(typeof selectedTab.firstChild.getAttribute !== 'undefined'){ 
                  attrVal = selectedTab.firstChild.getAttribute("data-value");} 
              if(attrVal != null){ return attrVal}
              else{return selectedTab.innerText}}
          })(%s)''' % self.varId)

  def deselect_tabs(self):
    """
    Description:
    ------------
    Deselect all the tabs in the component.
    """
    return JsFncs.JsFunctions([
      self._report.js.getElementsByName(self._src.tabs_name).all([
        self._report.js.data.all.element.setAttribute("data-selected", False),
        self._report.js.getElementsByName(self._src.tabs_name).all([
          self._report.js.data.all.element.css(self._src.options.tab_not_clicked_style())])
      ])
    ])


class JsHtmlIFrame(JsHtml.JsHtml):

  def src(self, src):
    src = JsUtils.jsConvertData(src, None)
    return self.setAttribute("src", src)

  def srcdoc(self, content):
    content = JsUtils.jsConvertData(content, None)
    return self.setAttribute("srcdoc", content)
