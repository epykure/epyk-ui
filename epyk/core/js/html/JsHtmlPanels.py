"""

"""


from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.fncs import JsFncs
from epyk.core.js.statements import JsFor


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
      p = self.panel(i)
      yield self.panel(i)
      print(p)
    return ""

  def togglePanel(self, i):
    """

    :param i:
    :return:
    """
    return '''
      %(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display = 'none'
      ''' % {'compId': self.varId, 'i': i}

    # return '''
    #    var nextColDim = panel_dims_%(htmlId)s[1];
    #    var nextColDimTotal = panel_dims_%(htmlId)s[1] + panel_dims_%(htmlId)s[0];
    #    $(%(jqId)s.find('div')[1]).toggle();
    #    const panelDisplay = $(%(jqId)s.find('div')[1]).css('display');
    #    if (panelDisplay == 'block') {var cls = $(%(jqId)s.find('div')[1]).next().attr('class').replace("col-md-" + nextColDimTotal, "col-md-" + panel_dims_%(htmlId)s[1])}
    #    else {var cls = $(%(jqId)s.find('div')[1]).next().attr('class').replace("col-md-" + panel_dims_%(htmlId)s[1], "col-md-" + nextColDimTotal)}
    #    $(%(jqId)s.find('div')[1]).next().attr('class', cls)
    #    ''' % {'jqId': self.varId, 'htmlId': self.htmlId}
    #
    # # TODO: Fix this part
    #return "$(%(jqId)s.find('div:nth-child(%(index)s)')).toggle()" % {'jqId': self.jqId, 'index': i}


class JsHtmlTabs(JsHtml.JsHtml):

  @property
  def selected_index(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get("%s.querySelector('div[data-selected=true').getAttribute('data-index')" % self.varId)

  @property
  def selected_name(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get("%s.querySelector('div[data-selected=true').innerHTML" % self.varId)

  @property
  def reset_tabs(self):
    """

    :return:
    """
    return JsFncs.JsFunctions([
      self._report.js.getElementsByName(self._src.tabs_name).all([
        self._report.js.data.all.element.setAttribute("data-selected", False)
      ])
    ])
