"""
Base module for the tables
"""

import json

from epyk.core.html import Html

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsTable


class Row(Html.Html):
  name, category, callFnc = 'Row', 'Tables', None

  def __init__(self, report, cells):
    super(Row, self).__init__(report, cells)

  def __getitem__(self, i):
    return self.val[i]

  def cell(self, i):
    return self[i]

  def __str__(self):
    data = [v.html() for v in self.val]
    return "<tr %s>%s</tr>" % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(data))


class Cell(Html.Html):
  name, category, callFnc = 'Cell', 'Tables', None

  def __init__(self, report, text, is_header):
    super(Cell, self).__init__(report, text)
    self.is_header = is_header

  def set_html_content(self, htmlObj):
    """
    Set the cell content to be an HTML object

    :param htmlObj: Python HTML object
    :return: self, the cell object to allow the chaining
    """
    htmlObj.options.managed = False
    self.innerPyHTML = htmlObj
    return self

  def __str__(self):
    if self.is_header:
      return "<th %s>%s</th>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.content)

    return "<td %s>%s</td>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.content)


class Bespoke(Html.Html):
  name = 'Basic Table'
  # _grpCls = CssGrpClsTable.CssClassTableBespoke

  def __init__(self, report, recordSet, cols, rows, width, height, htmlCode, options, profile):
    data = []
    self._fields = rows + cols
    for rec in recordSet:
      data.append([rec[c] for c in self._fields])
    super(Bespoke, self).__init__(report, data, htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.items = None
    self.css({"text-align": 'center', 'border-collapse': 'collapse'})
    self._style = {"rows": {"padding": '5px 0'}, "header": {"padding": '5px 0'}}
    self.set_items()

  @property
  def tableId(self):
    """
    Return the Javascript variable of the bespoke
    """
    return self.dom.varId

  @property
  def header(self):
    """
    Get the header row. Returns none if missing
    """
    return self._header

  def set_items(self):
    if self.items is None:
      self.items = []
    if self._fields is not None:
      self._header = Row(self._report, [Cell(self._report, d, is_header=True) for d in self._fields])
      self.items.append(self._header)
    for rec in self.val:
      self.items.append(Row(self._report, [Cell(self._report, r, is_header=False) for r in rec]))
    return self

  def __getitem__(self, i):
    """
    Get the table rows
    """
    return self.items[i]

  def row(self, i, inc_header=False):
    """
    Get the table rows

    :param i: Integer. The column number
    :param inc_header: Boolean. Default False

    :return:
    """
    if not inc_header and self._fields is not None:
      return self[i+1]

    return self[i]

  def col(self, header=None, i=None):
    """
    Get the table column cells as a generator

    :param header: String.
    :param i: Integer
    """
    for v in self.items:
      if header is not None:
        i = self._fields.index(header)
      yield v[i]

    return self

  def add(self, row, missing="", is_header=False):
    """
    Add a row to the table

    Example
    simple_table.row_add({"column": "value"})

    :param row: The row to be added to the table
    :param missing: The data to put when a cell is missing

    :return: The python table
    """

    if isinstance(row, dict):
      data = [row.get(h, missing) for h in self._fields]
    else:
      data = row
    self.val.append(data)
    self.items.append(Row(self._report, [Cell(self._report, d, is_header=is_header) for d in data]))
    return self

  def __str__(self):
    str_rows = [r.html() for r in self.items]
    return "<table %s>%s</table>" % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(str_rows))


class Excel(Html.Html):
  name = 'Excel'
  # _grpCls = CssGrpClsTable.CssClassTableExcel

  def __init__(self, report, recordSet, cols, rows, title, width, height, cellwidth, delimiter, htmlCode):
    self.recordSet, self.delimiter = recordSet, delimiter
    super(Excel, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height})
    self._jsStyles = {'header': rows + cols, 'cellwidth': cellwidth}
    self.css({'display': 'inline-block', 'overflow': 'auto', 'padding': 0, 'vertical-align': 'top'})
    self.add_title(title, options={'content_table': False})

  @property
  def _js__builder__(self):
    return '''
      var tr = $('<tr></tr>');
      jsStyles.header.forEach(function(rec){tr.append("<th>"+ rec +"</th>")});
      htmlObj.append(tr); var tr = $('<tr></tr>'); var tbody = $('<tbody></tbody>');
      jsStyles.header.forEach(function(rec){tr.append("<td><input type='text' style='"+ jsStyles.cellwidth +"'/></td>")});
      tbody.append(tr);htmlObj.append(tbody)
      '''

  def __str__(self):
    self._browser_data['component_ready'].append('''
      function tableData(tableObj){
        res = [];
        tableObj.find('tbody').find('tr').each(function(key, val){
          var row = [];
          $(this).find('td').each(function(key, cell) {row.push($(cell).find('input').val())});
          res.push(row)}); return res};

      function listToRec(data, header){
          var res = [];
          data.forEach(function(row){
            rec = {}; header.forEach(function(h, i){rec[h] = row[i]}); res.push(rec)
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
      delimiter = '<input id="%s_delimiter" type="text" value="%s" placeholder="Line delimiter"/>' % (self.htmlCode, self.delimiter)
    else:
      delimiter = '<input id="%s_delimiter" type="text" value="%s" style="display:none" placeholder="Line delimiter"/>' % (
          self.htmlCode, self.delimiter)
    return '<div %(strAttr)s>%(delimiter)s<table style="width:100%%"></table></div>' % {
      'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'delimiter': delimiter}
