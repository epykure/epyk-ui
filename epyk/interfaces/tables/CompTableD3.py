

class D3(object):

  def __init__(self, context):
    self.parent = context

  def table(self, records=None, header=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None,
            profile=None):
    """

    :param records:
    :param header:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    table = self.parent.context.rptObj.ui.div(width=width, height=height, htmlCode=htmlCode, options=options,
                                              profile=profile)
    d3_table = table.js.d3.select("#%s" % table.htmlId, varName='d3Table').rappend('table')
    if header is None and records is not None:
      header = list(records[0].keys())
    table.onReady(
      [d3_table.toStr(),
       d3_table.rappend('thead').rappend('tr')
         .selectAll('th').data(header).enter().rappend('th').text("ƒ('head')").toStr(),
       d3_table.rappend('tbody').selectAll('tr').data(records).enter()
         .rappend('tr').selectAll('td').dataRecord(header).enter().rappend('td').html().toStr()
       ]
    )
    return table
