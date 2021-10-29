

from epyk.customs.data.html import HtmlDashboard
from epyk.core.html import Defaults


class Components:

  def __init__(self, ui):
    self.page = ui.page

  def pivots(self, rows=None, columns=None, width=(100, "%"), height=('auto', ""), html_code=None, options=None,
             profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param columns: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    dflt_options = {"sub_chart": False, "max": {"rows": 1}, "columns": "", 'rows': ""}
    if options is not None:
      dflt_options.update(options)
    component = HtmlDashboard.Pivots(self.page, width, height, html_code, options, profile)
    if rows is None:
      row_options = dict(dflt_options)
      row_options["max"] = dflt_options.get("max", {}).get("rows")
      component.rows = self.page.ui.lists.drop(html_code="%s_rows" % component.htmlCode, options=row_options)
      if row_options["max"] == 1:
        component.rows.style.css.min_height = 20
      component.rows.style.css.margin_top = 0
    else:
      component.rows = rows

    if dflt_options.get("sub_chart"):
      component.sub_rows = self.page.ui.lists.drop(
        html_code="%s_sub_rows" % component.htmlCode, options={"max": 1})
      component.sub_rows.style.css.min_height = 20
      component.sub_rows.style.css.margin_top = 0
      component.sub_rows.options.managed = False
    else:
      component.sub_rows = None
    component.rows.options.managed = False
    if columns is None:
      columns_options = dict(dflt_options)
      columns_options["max"] = dflt_options.get("max", {}).get("columns")
      component.columns = self.page.ui.lists.drop(
        html_code="%s_columns" % component.htmlCode, options=columns_options)
      component.columns.style.css.margin_top = 0
    else:
      component.columns = columns
    component.columns.options.managed = False
    component.style.css.margin_top = 5
    component.style.css.margin_bottom = 5
    return component

  def filters(self, items=None, button=None, width=("auto", ""), height=(60, "px"), html_code=None, helper=None,
              options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param items:
    :param button:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    container = self.page.ui.div(width=width)
    if options.get("select", 'select') == 'input':
      container.select = self.page.ui.inputs.autocomplete(
        html_code="%s_select" % html_code if html_code is not None else html_code,
        width=(Defaults.TEXTS_SPAN_WIDTH, 'px'))
      container.select.style.css.text_align = "left"
      container.select.style.css.padding_left = 5
      container.select.options.liveSearch = True
    else:
      container.select = self.page.ui.select(
        html_code="%s_select" % html_code if html_code is not None else html_code)
      container.select.attr['data-width'] = '%spx' % options.get('width', Defaults.TEXTS_SPAN_WIDTH)
      container.select.options.liveSearch = True
    if options.get("autocomplete"):
      container.input = self.page.ui.inputs.autocomplete(
        html_code="%s_input" % html_code if html_code is not None else html_code,
        width=(Defaults.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
    else:
      container.input = self.page.ui.input(
        html_code="%s_input" % html_code if html_code is not None else html_code,
        width=(Defaults.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
    container.input.style.css.text_align = 'left'
    container.input.style.css.padding_left = 5
    container.input.style.css.margin_left = 10
    if button is None:
      button = self.page.ui.buttons.colored("add")
      button.style.css.margin_left = 10
    container.button = button
    container.clear = self.page.ui.icon("fas fa-times")
    container.clear.style.css.color = self.page.theme.danger[1]
    container.clear.style.css.margin_left = 20
    container.clear.tooltip("Clear all filters")
    container.add(self.page.ui.div([container.select, container.input, container.button, container.clear]))
    container.filters = self.page.ui.panels.filters(
      items, container.select.dom.content, (100, '%'), height, html_code, helper, options, profile)
    container.add(container.filters)
    container.clear.click([
      container.filters.dom.clear()
    ])
    container.button.click([
      container.filters.dom.add(container.input.dom.content, container.select.dom.content)
    ])
    container.input.enter(container.button.dom.events.trigger("click"))
    return container
