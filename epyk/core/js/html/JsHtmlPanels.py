"""

"""


from epyk.core.js.html import JsHtml


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

