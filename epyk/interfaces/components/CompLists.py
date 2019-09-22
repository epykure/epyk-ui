"""

"""

# Check if pandas is available in the current environment
# if it is the case this module can handle Dataframe directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False

from epyk.core import html


class Lists(object):
  """

  """

  def __init__(self, context):
    self.context = context

  def _size(self, size):
    """

    :param size:
    :return:
    """
    if size[0] is None and size[1] == "px" and hasattr(self.context.rptObj, "style"):
      size = (self.context.rptObj.style.defaults.font.size, self.context.rptObj.style.defaults.font.unit)
    return size

  def _filter(self, recordSet, column, options=None):
    """

    :param recordSet:
    :param column:
    :param options: A dictionary with specific filtering options e.g {'allSelected': True, 'operation': 'in'}
    :return:
    """
    dataId = id(recordSet)
    dataCode = "df_code_%s" % dataId
    globalFilter = {'jsId': dataCode, 'colName': column}
    globalFilter.update({options})
    if not dataCode in self.context.rptObj.jsSources:
      self.context.rptObj.jsSources[dataCode] = {'dataId': dataId, 'containers': [], 'data': recordSet}
      self.context.rptObj.jsSources[dataCode]['containers'].append(self)
    return globalFilter

  def _recordSet(self, recordSet, column):
    """

    :param recordSet:
    :param column:
    :return:
    """
    data = None
    is_converted = False
    if has_pandas:
      if isinstance(recordSet, pd.DataFrame):
        data = [{'name': r, 'value': r} for r in recordSet[column].unique().tolist()]
        is_converted = True

    if not is_converted:
      result = set([])
      for rec in recordSet:
        result.add({'name': rec[column], 'value': rec[column]})
      data = list(result)
    return data

  def select(self, records, htmlCode=None, label=None, selected=None, width=(100, "%"), height=(None, "%"),
             column=None, filter=None, profile=None, multiple=False, options=None):
    """
    HTML Select component

    Example
    rptObj.ui.select(["A", "B", "C"], label="label", selected="C", multiple=True,
                     options={"title": "ttle", 'showTick': True, 'maxOptions': 2})

    Documentation
    https://silviomoreto.github.io/bootstrap-select/examples/
    https://www.npmjs.com/package/bootstrap-select-v4
    https://www.jqueryscript.net/form/Bootstrap-4-Dropdown-Select-Plugin-jQuery.html

    :param records: The input data. Can be a list or a dataFrame
    :param htmlCode: Optional. The component identifier code (for bot
    :param label: Optional. The HTML label attached to the component
    :param selected: The selected values
    :param width: Optional. Integer for the component width
    :param width_unit: Optional. The unit for the with. Default %
    :param height: Optional. Integer for the component height
    :param height_unit: Optional. The unit for the height. Default px
    :param column:
    :param filter:
    :param profile: Optional. A flag to set the component performance storage
    :param multiple: Boolean. To set if the component can handle multiple selections
    :param options: The select options as defined https://developer.snapappointments.com/bootstrap-select/options/
    :rtype: html.HtmlSelect.Select
    :return:
    """
    if options is None:
      options = {}
    all_selected = options.get("allSelected", False)
    if column is not None:
      if filter is not None:
        if filter == True:
          self._filter(records, column, {'allSelected': all_selected, 'operation': options.get("operation", "in")})
      records = self._recordSet(records, column)
    elif isinstance(records, (list, tuple)) and len(records) > 0 and not isinstance(records[0], dict):
      records = [{'name': rec, 'value': rec} for rec in records]
    if all_selected:
      records = [{'name': 'All', 'value': ''}] + records

    if multiple:
      if not isinstance(multiple, dict):
        multiple = {"max": 2}
      if selected is not None:
        for rec in records:
          if rec["value"] in selected:
            rec["selected"] = True
      return self.context.register(
        html.HtmlSelect.Select(self.context.rptObj, records, htmlCode, label, width, height, filter, profile, multiple, options))

    if selected is not None:
      for rec in records:
        if rec["value"] == selected:
          rec["selected"] = True
    return self.context.register(html.HtmlSelect.Select(self.context.rptObj, records, htmlCode, label, width, height,
                                                        filter, profile, multiple, options))

  def list(self, categories=None, icon=None, title='', width=(100, "%"), height=(None, 'px'),
           draggable=False, draggableGroupId=None, draggableMax=None, dfColumn=None, dataSrc=None, htmlCode=None,
           searchable=False, selectable=True, showGrid=True, template=None, globalFilter=None, profile=None):
    """

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
    http://astronautweb.co/snippet/font-awesome/

    :param categories:
    :param icon:
    :param title:
    :param width:
    :param height:
    :param draggable:
    :param draggableGroupId:
    :param draggableMax:
    :param dfColumn:
    :param dataSrc:
    :param htmlCode:
    :param searchable:
    :param selectable:
    :param showGrid:
    :param template:
    :param globalFilter:
    :param profile:
    :return:
    """
    return self.context.register(html.HtmlList.List(self.context.rptObj, categories, icon, title, width,
                                                    height, draggable, draggableGroupId, draggableMax,
                                                    dfColumn, dataSrc, htmlCode, searchable, selectable, showGrid,
                                                    template, globalFilter, profile))

  def tree(self, recordSet=None, width=(100, "%"), height=(None, 'px'), title='', htmlCode=None,
           draggable=False, dataSrc=None, expanded=False, profile=None):
    """

    Example
    data = [{"label": 'test', 'items': [{"label": 'child 1', 'color': 'red'}]}]
    rptObj.ui.lists.tree(data)

    :param recordSet:
    :param width:
    :param height:
    :param title:
    :param htmlCode:
    :param draggable:
    :param dataSrc:
    :param expanded:
    :param profile:
    :rtype: html.HtmlList.ListTree
    :return:
    """
    return self.context.register(html.HtmlTrees.Tree(self.context.rptObj, recordSet, width, height, title, htmlCode,
                                                        draggable, dataSrc, expanded, profile))

  def listnumbers(self, recordSet=None, level=None, top=(10, 'px'), width=(100, '%'), height=(None, 'px'),
                  selectable=None, multiselectable=None, htmlCode=None, dfColumn=None,
                  globalFilter=None, dataSrc=None, profile=None):
    return self.context.register(html.HtmlList.NumberList(self.context.rptObj, recordSet, top, level, width,
                                                          height, selectable=selectable,
                                                          multiselectable=multiselectable, htmlCode=htmlCode,
                                                          dfColumn=dfColumn, globalFilter=globalFilter,
                                                          dataSrc=dataSrc, profile=profile))

  def listletter(self, recordSet=None, level=None, top=(10, 'px'), width=(100, "%"), height=(None, 'px'), selectable=None, multiselectable=None, htmlCode=None, dfColumn=None, globalFilter=None, dataSrc=None, profile=None):
    return self.context.register(html.HtmlList.LetterList(self.context.rptObj, recordSet, top, level, width, height,
            selectable=selectable, multiselectable=multiselectable, htmlCode=htmlCode, dfColumn=dfColumn, globalFilter=globalFilter, dataSrc=dataSrc, profile=profile))

  def checklist(self, recordSet=None, width=(100, "%"), height=(None, 'px'), dfColumn=None, globalFilter=None,
                dataSrc=None, profile=None):
    return self.context.register(html.HtmlList.CheckList(self.context.rptObj, recordSet, width, height, dfColumn,
                                                         globalFilter, dataSrc, profile))

  def points(self, recordSet=None, marginTop=10, level=None, width=(100, "%"), height=(None, 'px'), selectable=None,
             multiselectable=None, htmlCode=None, dfColumn=None, globalFilter=None, dataSrc=None, profile=None):
    return self.context.register(html.HtmlList.Bullets(self.context.rptObj, recordSet, marginTop, level, width, height,
        selectable=selectable, multiselectable=multiselectable, htmlCode=htmlCode, dfColumn=dfColumn, globalFilter=globalFilter, dataSrc=dataSrc, profile=profile))

  def squares(self, recordSet=None, marginTop=10, level=None, width=(100, "%"), height=(None, 'px'), selectable=None, multiselectable=None, htmlCode=None, dfColumn=None, globalFilter=None, dataSrc=None, profile=None):
    return self.context.register(html.HtmlList.Squares(self.context.rptObj, recordSet, marginTop, level, width, height,
        selectable=selectable, multiselectable=multiselectable, htmlCode=htmlCode, dfColumn=dfColumn, globalFilter=globalFilter, dataSrc=dataSrc, profile=profile))

  def dropdown(self, recordSet=None, size=(None, 'px'), title='', width=(100, "%"), height=(32, 'px'), htmlCode=None, dataSrc=None, globalFilter=None, profile=None):
    size = self._size(size)
    return self.context.register(html.HtmlSelect.SelectDropDown(self.context.rptObj, title, recordSet, size, width,
        height, htmlCode, dataSrc, globalFilter, profile))

  def listbadge(self, recordSet=None, color=None, size=(None, 'px'), width=(100, "%"), height=(None, 'px'), draggable=False, draggableGroupId=None, draggableMax=None, dfColumn=None, dataSrc=None, profile=None):
    size = self._size(size)
    return self.context.register(html.HtmlList.ListBadge(self.context.rptObj, recordSet, color, size, width, height,
       draggable, draggableGroupId, draggableMax, dfColumn, dataSrc, profile))

  def brackets(self, recordSet=None, width=(100, "%"), height=(550, 'px'), options=None, profile=None):
    return self.context.register(html.HtmlList.ListTournaments(self.context.rptObj, recordSet, width, height, options, profile))

  def accordeon(self, categories=None, color=None, width=(150, 'px'), size=(None, "px"), dataSrc=None, profile=None):
    """

    :param categories:
    :param color:
    :param width:
    :param width_unit:
    :param size:
    :param dataSrc:
    :param profile:
    :return:
    """
    size = self._size(size)
    return self.context.register(html.HtmlList.HtmlListAccordeon(self.context.rptObj, categories, color, width,
                                                                 size, dataSrc, profile))