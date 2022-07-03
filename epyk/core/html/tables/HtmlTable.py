#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Union
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.js.html import JsHtml
from epyk.core.html.options import OptTable

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsTable


class Row(Html.Html):
  name = 'Row'
  _option_cls = OptTable.OptionsTableRow

  def __init__(self, page: primitives.PageModel, cells, options=None):
    super(Row, self).__init__(page, cells,  options=options)
    self.attr["class"].clear()

  @property
  def dom(self) -> JsHtml.JsHtmlRich:
    """
    Description:
    ------------
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, page=self.page)
    return self._dom

  @property
  def options(self) -> OptTable.OptionsTableRow:
    """
    Description:
    ------------
    All table options.
    """
    return super().options

  def __getitem__(self, i: int):
    return self.val[i]

  def cell(self, i: int):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param i:
    """
    return self[i]

  def __str__(self):
    data = [v.html() for v in self.val]
    return "<tr %s>%s</tr>" % (self.get_attrs(css_class_names=self.style.get_classes()), "".join(data))


class Cell(Html.Html):
  name = 'Cell'
  _option_cls = OptTable.OptionsTableCell

  def __init__(self, page: primitives.PageModel, text, is_header, options=None):
    super(Cell, self).__init__(page, text, options=options)
    self.attr["class"].clear()
    self.is_header = is_header

  @property
  def dom(self) -> JsHtml.JsHtmlRich:
    """
    Description:
    ------------

    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, page=self.page)
    return self._dom

  @property
  def options(self) -> OptTable.OptionsTableCell:
    """
    Description:
    ------------
    All table options.
    """
    return super().options

  def set_html_content(self, component: primitives.HtmlModel):
    """
    Description:
    ------------
    Set the cell content to be an HTML object.

    Attributes:
    ----------
    :param component: Python HTML object

    :return: self, the cell object to allow the chaining
    """
    component.options.managed = False
    self.innerPyHTML = component
    return self

  def __str__(self):
    if self.is_header:
      return "<th %s>%s</th>" % (self.get_attrs(css_class_names=self.style.get_classes()), self.content)

    return "<td %s>%s</td>" % (self.get_attrs(css_class_names=self.style.get_classes()), self.content)


class Bespoke(Html.Html):
  name = 'Basic Table'
  _option_cls = OptTable.OptionsBasic

  def __init__(self, page: primitives.PageModel, records, cols, rows, width, height, html_code, options, profile):
    data = []
    self._fields = rows + cols
    for rec in records:
      data.append([rec[c] for c in self._fields])
    super(Bespoke, self).__init__(
      page, data, html_code=html_code, profile=profile, css_attrs={"width": width, "height": height}, options=options)
    self.items = None
    self.style.add_classes.table.table()
    self.css({"text-align": 'center', 'border-collapse': 'collapse'})
    self.set_items()

  @property
  def options(self) -> OptTable.OptionsBasic:
    """
    Description:
    ------------
    All table options.
    """
    return super().options

  @property
  def tableId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the bespoke.
    """
    return self.dom.varId

  @property
  def header(self):
    """
    Description:
    -----------
    Get the header row. Returns none if missing.
    """
    return self._header

  def set_header(self, values: list, css: dict = None):
    """
    Description:
    -----------
    Set the table header.

    Attributes:
    ----------
    :param values: A list of headers
    :param css: Specific CSS attributes
    """
    for i, col in enumerate(self._header):
      col._vals = values[i]
      if css is not None:
        col.css(css)
    return self

  def set_items(self):
    """
    Description:
    -----------

    """
    if self.items is None:
      self.items = []
    if self._fields is not None and self.options.with_header:
      self._header = Row(self.page, [
        Cell(self.page, d, is_header=True, options={
          "cssClasses": self.options.colCssClasses, "managed": False}) for d in self._fields])
      self.items.append(self._header)
      self.items[-1].options.managed = False
    for rec in self.val:
      self.items.append(Row(self.page, [
        Cell(self.page, r, is_header=False, options={
          "cssClasses": self.options.rowCssClasses, "managed": False}) for r in rec]))
      self.items[-1].options.managed = False
      if self.options.with_hover:
        self.items[-1].style.add_classes.table.row_hover()
    return self

  def __getitem__(self, i: int) -> Html.Html:
    """
    Description:
    -----------
    Get the table rows.

    Usage::

    Attributes:
    ----------
    :param i: The column number
    """
    return self.items[i]

  def row(self, i: int, inc_header: bool = False):
    """
    Description:
    -----------
    Get the table rows.

    Usage::

    Attributes:
    ----------
    :param i: The column number.
    :param inc_header: Optional. Default False
    """
    if not inc_header and self._fields is not None:
      return self[i+1]

    return self[i]

  def col(self, header: Union[str, bool] = None, i: int = None):
    """
    Description:
    -----------
    Get the table column cells as a generator.

    Usage::

        for cell in t.col(i=1, header=False):
          cell

    Attributes:
    ----------
    :param header: Optional. Consider or not the header.
    :param i: Optional. The column index.
    """
    start = 1 if header is False else 0
    for v in self.items[start:]:
      if header is not None and header:
        i = self._fields.index(header)
      yield v[i]

    return self

  def set_editable_cols(self, col_indices: List[int]):
    """
    Description:
    ------------
    Define columns as editable.

    Attributes:
    ----------
    :param col_indices: Column indices to be changed.
    """
    for row in self.items:
      for i in col_indices:
        row[i].attr["contenteditable"] = "true"

  @property
  def dom(self) -> JsHtml.JsHtmlTable:
    """
    Description:
    ------------
    Dom properties for a table.
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlTable(self, page=self.page)
    return self._dom

  def add(self, row: Union[dict, list], missing: str = "", is_header: bool = False):
    """
    Description:
    -----------
    Add a row to the table.

    Usage::

      simple_table.row_add({"column": "value"})

    Attributes:
    ----------
    :param row: The row to be added to the table
    :param missing: The data to put when a cell is missing
    :param is_header: Boolean. Optional.

    :return: The python table
    """
    if isinstance(row, dict):
      data = [row.get(h, missing) for h in self._fields]
    else:
      data = row
    self.val.append(data)
    self.items.append(Row(self.page, [Cell(
      self.page, d, is_header=is_header, options={"managed": False}) for d in data]))
    self.items[-1].options.managed = False
    self.items[-1].style.add_classes.table.row_hover()
    return self

  def __str__(self):
    str_rows = [r.html() for r in self.items]
    return "<table %s>%s</table>" % (self.get_attrs(css_class_names=self.style.get_classes()), "".join(str_rows))


class Excel(Html.Html):
  name = 'Excel'
  # _grpCls = CssGrpClsTable.CssClassTableExcel

  def __init__(self, page: primitives.PageModel, records, cols, rows, title,
               width, height, cell_width, delimiter, html_code):
    self.recordSet, self.delimiter = records, delimiter
    super(Excel, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height})
    self._jsStyles = {'header': rows + cols, 'cellwidth': cell_width}
    self.css({'display': 'inline-block', 'overflow': 'auto', 'padding': 0, 'vertical-align': 'top'})
    self.add_title(title, options={'content_table': False})

  _js__builder__ = '''
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
      delimiter = '<input id="%s_delimiter" type="text" value="%s" placeholder="Line delimiter"/>' % (
        self.htmlCode, self.delimiter)
    else:
      delimiter = '<input id="%s_delimiter" type="text" value="%s" style="display:none" placeholder="Line delimiter"/>' % (
          self.htmlCode, self.delimiter)
    return '<div %(strAttr)s>%(delimiter)s<table style="width:100%%"></table></div>' % {
      'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), 'delimiter': delimiter}
