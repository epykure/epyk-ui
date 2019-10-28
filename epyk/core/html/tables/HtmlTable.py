"""
Base module for the tables
"""

import json

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpClsTable


class Row(Html.Html):

  @staticmethod
  def to_html(row, css=None, css_cols=None, header=False):
    _row = []
    css_cols = css_cols or {}
    for i, _cell in enumerate(row):
      css_cell = dict(css)
      if i in css_cols:
        css_cell.update(css_cols[i])
      _row.append(Cell.to_html(_cell, css=css_cell, header=header))
    if css is not None:
      style = ["%s:%s" % (k, v) for k, v in css.items()]
      return "<tr style='%s'>%s</tr>" % (";".join(style), "".join(_row))

    return "<tr>%s</tr>" % "".join(_row)

  def __str__(self):
    return "<tr %s></tr>" % (self.strAttr(pyClassNames=self.pyStyle))


class Cell(Html.Html):

  @staticmethod
  def to_html(cell, css=None, header=False):
    style = ["%s:%s" % (k, v) for k, v in css.items()] if css is not None else []
    if header:
      return "<th style='%s'>%s</th>" % (";".join(style), cell)

    return "<td style='%s'>%s</td>" % (";".join(style), cell)

  def __str__(self):
    return "<td %s></td>" % (self.strAttr(pyClassNames=self.pyStyle))


class Bespoke(Html.Html):
  name, category, callFnc = 'Basic', 'Tables', 'basic'
  _grpCls = CssGrpClsTable.CssClassTableBespoke

  def __init__(self, report, recordSet, cols, rows, width, height, htmlCode, options, profile):
    data = []
    self.header = rows + cols
    for rec in recordSet:
      data.append([rec[c] for c in self.header])
    super(Bespoke, self).__init__(report, data, code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                  heightUnit=height[1], profile=profile)
    self.css({"text-align": 'center', 'border-collapse': 'collapse'})
    self._style = {"rows": {"padding": '5px 0'}, "header": {"padding": '5px 0'}}

  @property
  def tableId(self):
    """
    Return the Javascript variable of the bespoke
    """
    return self.dom.varId

  def row_style(self, css, row_id=None):
    """
    Change the style of a particular row in the table

    Example
    simple_table.row_style({"color": 'red'}, row_id=3)

    :param css: A dictionary with the CSS Style
    :param row_id: Optional. The row id

    :return: The python table object
    """
    if row_id is None:
      self._style["rows"] = css
    else:
      self._style.setdefault("row", {})[row_id] = css
    return self

  def column_style(self, css, column_name=None):
    """
    Change the style of a particular column in the table

    Example
    simple_table.column_style({"color": 'pink'}, column_name="A")

    :param css: A dictionary with the CSS styles
    :param column_name: Optional. The column name

    :return: The python table object
    """
    if column_name is None:
      self._style["cols"] = css
    else:
      col_index = self.header.index(column_name)
      self._style.setdefault("cols", {})[col_index] = css
    return self

  def column_format(self, fnc, column_name):
    """

    :param fnc:
    :param column_name:
    :return:
    """
    return self

  def row_add(self, data, missing=""):
    """
    Add a row to the table

    Example
    simple_table.row_add({"column": "value"})

    :param data: The row to be added to the table
    :param missing: The data to put when a cell is missing

    :return: The python table
    """
    if isinstance(data, dict):
      self.vals.append([data.get(h, missing) for h in self.header])
    else:
      self.vals.append(data)
    return self

  def __str__(self):
    _data = ["<thead>%s</thead><tbody>" % Row.to_html(self.header, css=self._style["header"], header=True)]
    for i, _row in enumerate(self.vals):
      css_row = dict(self._style["rows"])
      if i in self._style.get('row', []):
        css_row.update(self._style['row'][i])
      _data.append(Row.to_html(_row, css=css_row, css_cols=self._style.get('cols', {})))
    _data.append("</tbody>")
    return "<table %s>%s</table>" % (self.strAttr(pyClassNames=self.defined), "".join(_data))


class Excel(Html.Html):
  name, category, callFnc = 'Excel', 'Tables', 'excel'
  _grpCls = CssGrpClsTable.CssClassTableExcel

  def __init__(self, report, recordSet, cols, rows, title, width, height, cellwidth, delimiter, htmlCode):
    self.recordSet, self.delimiter = recordSet, delimiter
    super(Excel, self).__init__(report, [], code=htmlCode, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1])
    self._jsStyles = {'header': rows + cols, 'cellwidth': cellwidth}
    self.css({'display': 'inline-block', 'overflow': 'auto', 'padding': 0, 'vertical-align': 'top'})
    self.add_title(title)

  @property
  def tableId(self):
    """
    Return the Javascript variable of the bespoke
    """
    return self.dom.varId

  @property
  def val(self):
    return "JSON.stringify(tableData(%s))" % self.jqId

  @property
  def records(self):
    return "listToRec(tableData(%s), %s)" % (self.jqId, json.dumps(self._jsStyles['header']))

  @property
  def jqId(self):
    return "$('#%s table')" % self.htmlId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' htmlObj.empty();
      var tr = $('<tr></tr>');
      jsStyles.header.forEach(function(rec){tr.append("<th>"+ rec +"</th>")});
      htmlObj.append(tr); var tr = $('<tr></tr>'); var tbody = $('<tbody></tbody>');
      jsStyles.header.forEach(function(rec){tr.append("<td><input type='text' style='"+ jsStyles.cellwidth +"'/></td>")});
      tbody.append(tr);htmlObj.append(tbody)''')

  def __str__(self):
    self._report.jsOnLoadFnc.add('''
      function tableData(tableObj){
        res = [];
        tableObj.find('tbody').find('tr').each(function(key, val){
          var row = [];
          $(this).find('td').each(function(key, cell) {row.push($(cell).find('input').val())});
          res.push(row)}); return res};

      function listToRec(data, header){
          var res = [];
          data.forEach(function(row){
            rec = {};
            header.forEach(function(h, i){rec[h] = row[i]}); res.push(rec);
          }); return res}''')

    self.paste('''
      var tbody = $(this).find('tbody'); tbody.empty();
      var tableId = $(this).parent().attr('id');
      var lineDelimiter = $('#'+ tableId +'_delimiter').val();
      if (lineDelimiter == 'TAB'){lineDelimiter = '\\t'};
      data.split("\\n").forEach(function(line){
        if (line !== ''){
          var tr = $('<tr></tr>');
          line.split(lineDelimiter).forEach(function(rec){tr.append("<td><input type='text'  value='"+ rec +"'/></td>")
        }); tbody.append(tr)}}) ''')
    if self.delimiter is None:
      delimiter = '<input id="%s_delimiter" type="text" value="%s" placeholder="Line delimiter"/>' % (self.htmlId, self.delimiter)
    else:
      delimiter = '<input id="%s_delimiter" type="text" value="%s" style="display:none" placeholder="Line delimiter"/>' % (
          self.htmlId, self.delimiter)
    return '<div %(strAttr)s>%(delimiter)s<table style="width:100%%"></table></div>' % {
      'strAttr': self.strAttr(pyClassNames=self.defined), 'delimiter': delimiter}
