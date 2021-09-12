
from epyk.fwk.toast import html
from epyk.fwk.toast.js import JsToast
from epyk.core.js import JsUtils
from epyk.interfaces import Arguments
from epyk.fwk.toast import PkgImports


class ToastGrids:
  def __init__(self, ui):
    self.page = ui.page

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(300, 'px'), html_code=None,
            options=None, profile=None):

    cols = cols or []
    rows = rows or []
    if not cols and not rows:
      if records is not None and records:
        cols = list(records[0].keys())

    table_options_dfls = {}
    if options is not None:
      table_options_dfls.update(options)
    table = html.HtmlToastGrid.Grid(self.page, records, width, height, html_code, table_options_dfls, profile)
    for c in cols + rows:
      table.add_column(c)
    return table


class ToastTimes:

  def __init__(self, ui):
    self.page = ui.page

  def selectbox(self, hour=None, minute=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None,
                options=None):
    """
    Description:
    ------------
    Component that selects specific time.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/

    Attributes:
    ----------
    :param hour: Number. optional. The initial hour.
    :param minute: Number. optional. The initial minute.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"inputType": "selectbox"}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlToastDates.TimePicker(self.page, width, height, html_code, dfl_options, profile)
    if hour is not None:
      component.options.initialHour = hour
    if minute is not None:
      component.options.initialMinute = minute
    return component

  def spinbox(self, hour=None, minute=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None,
              options=None):
    """
    Description:
    ------------
    Component that selects specific time.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/

    Attributes:
    ----------
    :param hour: Number. optional. The initial hour.
    :param minute: Number. optional. The initial minute.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"inputType": "spinbox"}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlToastDates.TimePicker(self.page, width, height, html_code, dfl_options, profile)
    if hour is not None:
      component.options.initialHour = hour
    if minute is not None:
      component.options.initialMinute = minute
    return component


class ToastFields:

  def __init__(self, ui):
    self.page = ui.page

  def date(self, value=None, label="", width=(None, "px"), height=(None, "px"), html_code=None, profile=None,
           options=None, helper=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param label:
    :param width:
    :param height:
    :param html_code:
    :param profile:
    :param options:
    :param helper:
    """
    component = self.page.ui.div(html_code=html_code, profile=profile, helper=helper, width=width, height=height)
    component.input = self.page.web.tui.dates.date(value, html_code="%s_input" % component.htmlCode, profile=profile)
    component.label = self.page.ui.label(label, html_code="%s_label" % component.htmlCode, profile=profile)
    if options and options.get("format") == "column":
      component.label.style.css.float = None
      component.label.style.css.display = "block"
      component.label.style.css.color = self.page.theme.notch()
      component.label.style.css.bold()
      component.input.style.css.remove("width")
    else:
      component.style.css.remove("display")
    component.extend([component.label, component.input])
    return component

  def time(self, hour=None, minute=None, label=None, width=(None, "px"), height=(None, "px"), html_code=None,
           profile=None, options=None, helper=None):
    """
    Description:
    ------------
    Component that selects specific time.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/

    Attributes:
    ----------
    :param hour: Number. optional. The initial hour.
    :param minute: Number. optional. The initial minute.
    :param label: String. Optional. The text of label to be added to the component.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    """
    component = self.page.ui.div(html_code=html_code, profile=profile, helper=helper, width=width, height=height)
    component.input = self.page.web.tui.time(hour, minute, html_code="%s_input" % component.htmlCode, profile=profile)
    component.label = self.page.ui.label(label, html_code="%s_label" % component.htmlCode, profile=profile)
    if options and options.get("format") == "column":
      component.label.style.css.float = None
      component.label.style.css.display = "block"
      component.label.style.css.color = self.page.theme.notch()
      component.label.style.css.bold()
      component.input.style.css.remove("width")
    else:
      component.style.css.remove("display")
    component.extend([component.label, component.input])
    return component

  def today(self, value=None, label="", width=(None, "px"), height=(None, "px"), html_code=None, profile=None,
            options=None, helper=None):
    """
    Description:
    ------------
    Component that selects specific time.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/

    Attributes:
    ----------
    :param value:
    :param label: String. Optional. The text of label to be added to the component.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    """
    component = self.page.ui.div(html_code=html_code, profile=profile, helper=helper, width=width, height=height)
    component.input = self.page.web.tui.dates.date(None, html_code="%s_input" % component.htmlCode, profile=profile)
    component.label = self.page.ui.label(label, html_code="%s_label" % component.htmlCode, profile=profile)
    if options and options.get("format") == "column":
      component.label.style.css.float = None
      component.label.style.css.display = "block"
      component.label.style.css.color = self.page.theme.notch()
      component.label.style.css.bold()
      component.input.style.css.remove("width")
    else:
      component.style.css.remove("display")
    component.extend([component.label, component.input])
    return component

  def cob(self, value=None, label="", width=(None, "px"), height=(None, "px"), html_code=None, profile=None,
          options=None, helper=None):
    """
    Description:
    ------------
    Component that selects specific time.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/

    Attributes:
    ----------
    :param value:
    :param label: String. Optional. The text of label to be added to the component.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    """
    component = self.page.ui.div(html_code=html_code, profile=profile, helper=helper, width=width, height=height)
    component.input = self.page.web.tui.dates.date(value, html_code="%s_input" % component.htmlCode, profile=profile)
    component.label = self.page.ui.label(label, html_code="%s_label" % component.htmlCode, profile=profile)
    if options and options.get("format") == "column":
      component.label.style.css.float = None
      component.label.style.css.display = "block"
      component.label.style.css.color = self.page.theme.notch()
      component.label.style.css.bold()
      component.input.style.css.remove("width")
    else:
      component.style.css.remove("display")
    component.extend([component.label, component.input])
    return component


class ToastDates:

  def __init__(self, ui):
    self.page = ui.page

  def date(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    Create a date picker.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlToastDates.DatePicker(self.page, width, height, html_code, dfl_options, profile)
    if value is not None:
      component.options.date = value
    return component

  def range(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    Create a date-range picker by DatePicker.createRangePicker().

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/DateRangePicker
      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlToastDates.DatePickerRange(self.page, width, height, html_code, dfl_options, profile)
    if value is not None:
      component.options.date = value
    return component

  def calendar(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    Create a calendar by DatePicker.createCalendar().

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/Calendar
      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlToastDates.DateCalendar(self.page, width, height, html_code, dfl_options, profile)
    if value is not None:
      component.options.date = value
    return component


class ToastCalendars:

  def __init__(self, ui):
    self.page = ui.page

  def monthly(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlToastCalendar.Calendar(self.page, width, height, html_code, dfl_options, profile)
    component.options.defaultViews.month()
    return component

  def weekly(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlToastCalendar.Calendar(self.page, width, height, html_code, dfl_options, profile)
    component.options.defaultViews.week()
    return component

  def daily(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlToastCalendar.Calendar(self.page, width, height, html_code, dfl_options, profile)
    component.options.defaultViews.day()
    return component


class ToastCharts:

  def __init__(self, ui):
    self.page = ui.page

  def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------
    Generic entry point for charts.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://nhn.github.io/tui.chart/latest

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y: List | String. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param kind: String. Optional. The chart type.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    if y is not None and not isinstance(y, list):
      y = [y]
    return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                               options=options, html_code=html_code)

  def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    -----------

    Usage::

      https://nhn.github.io/tui.chart/latest/LineChart
      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-line.md

    Attributes:
    ----------
    :param record: Array<dict>. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.c3.y(record or [], y_columns, x_axis, options)
    chart = html.HtmlToastCharts.Chart(self.page, width, height, html_code, dfl_options, profile)
    if data["series"]:
      for i, s in enumerate(data["series"]):
        chart.options.data.add_series(s, data["datasets"][i])
      chart.options.data.categories = data["labels"]
    chart.config.theme.series.colors = list(self.page.theme.charts)
    chart.config.series.eventDetectType = "grouped"
    return chart

  def area(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    -----------

    Usage::

      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-area.md

    Attributes:
    ----------
    :param record: Array<dict>. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    chart = html.HtmlToastCharts.ChartArea(self.page, width, height, html_code, dfl_options, profile)
    if data["series"]:
      for i, s in enumerate(data["series"]):
        chart.options.data.add_series(s, data["datasets"][i])
      chart.options.data.categories = data["labels"]
    chart.config.theme.series.colors = list(self.page.theme.charts)
    return chart

  def bullet(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    pass

  def bubble(self, record=None, y_columns=None, x_axis=None, r_columns=None, profile=None, width=(100, "%"),
             height=(330, "px"), options=None, html_code=None):
    """
    Description:
    -----------

    Usage::

      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-bubble.md

    Attributes:
    ----------
    :param record: Array<dict>. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param r_columns: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.chartJs.xyz(record or [], y_columns, x_axis, z_axis=r_columns, options=options)
    chart = html.HtmlToastCharts.ChartBubble(self.page, width, height, html_code, dfl_options, profile)
    if data["series"]:
      for i, s in enumerate(data["series"]):
        chart.options.data.add_series(s, data["datasets"][i]['data'])
      chart.options.data.categories = data["labels"]
    chart.config.theme.series.colors = list(self.page.theme.charts)
    return chart

  def box(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    pass

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    -----------

    Usage::


    Attributes:
    ----------
    :param record: Array<dict>. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.c3.y(record or [], y_columns, x_axis, options=options)
    chart = html.HtmlToastCharts.ChartColumn(self.page, width, height, html_code, dfl_options, profile)
    #chart.config.chart.width = JsUtils.jsWrap(
    #  "function(component){return component.clientWidth - (parseFloat(component.style.paddingLeft) + parseFloat(component.style.paddingRight)) }")
    if data["series"]:
      for i, s in enumerate(data["series"]):
        chart.options.data.add_series(s, data["datasets"][i])
      chart.options.data.categories = data["labels"]
    chart.config.theme.series.colors = list(self.page.theme.charts)
    return chart

  def hbar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    -----------

    Usage::


    Attributes:
    ----------
    :param record: Array<dict>. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.c3.y(record or [], y_columns, x_axis, options=options)
    chart = html.HtmlToastCharts.ChartBar(self.page, width, height, html_code, dfl_options, profile)
    if data["series"]:
      for i, s in enumerate(data["series"]):
        chart.options.data.add_series(s, data["datasets"][i])
      chart.options.data.categories = data["labels"]
    chart.config.theme.series.colors = list(self.page.theme.charts)
    return chart

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    """
    Description:
    -----------

    Usage::


    Attributes:
    ----------
    :param record: Array<dict>. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis)
    chart = html.HtmlToastCharts.ChartScatter(self.page, width, height, html_code, dfl_options, profile)
    if data["series"]:
      for i, s in enumerate(data["series"]):
        chart.options.data.add_series(s, data["datasets"][i])
      chart.options.data.categories = data["labels"]
    chart.config.theme.series.colors = list(self.page.theme.charts)
    return chart

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param record: Array<dict>. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    chart = html.HtmlToastCharts.ChartPie(self.page, width, height, html_code, dfl_options, profile)
    if data["series"]:
      for i, s in enumerate(data["series"]):
        chart.options.data.add_series(s, data["datasets"][i][0])
      chart.options.data.categories = data["labels"]
    chart.config.theme.series.colors = list(self.page.theme.charts)
    return chart

  def radar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    -----------

    Usage::


    Attributes:
    ----------
    :param record: Array<dict>. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    chart = html.HtmlToastCharts.ChartRadar(self.page, width, height, html_code, dfl_options, profile)
    if data["series"]:
      for i, s in enumerate(data["series"]):
        chart.options.data.add_series(s, data["datasets"][i])
      chart.options.data.categories = data["labels"]
    chart.config.theme.series.colors = list(self.page.theme.charts)
    return chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    -----------

    Usage::


    Attributes:
    ----------
    :param record: Array<dict>. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    pie_chart = self.pie(record, y_columns, x_axis, profile, width, height, options, html_code)
    pie_chart.config.series.radiusRange.inner = "40%"
    pie_chart.config.series.radiusRange.outer = "100%"
    return pie_chart

  def radial(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
    """
    Description:
    -----------

    Usage::

      https://github.com/nhn/tui.chart/blob/main/docs/en/chart-radialBar.md

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param width:
    :param height:
    :param options:
    :param html_code:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"series": []}
    dfl_options.update({'y_columns': y_columns or [], 'x_axis': x_axis, 'commons': {'fill': None}})
    if options is not None:
      dfl_options.update(options)
    data = self.page.data.c3.y(record or [], y_columns, x_axis, options=options)
    chart = html.HtmlToastCharts.ChartRadialBar(self.page, width, height, html_code, dfl_options, profile)
    chart.config.chart.width = JsUtils.jsWrap(
      "function(component){return component.clientWidth - (parseFloat(component.style.paddingLeft) + parseFloat(component.style.paddingRight)) }")
    if data["series"]:
      for i, s in enumerate(data["series"]):
        chart.options.data.add_series(s, data["datasets"][i])
      chart.options.data.categories = data["labels"]
    chart.config.theme.series.colors = list(self.page.theme.charts)
    chart.style.css.text_align = "center"
    return chart

  def gauge(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    pass

  def heatmap(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    pass

  def treemap(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    pass


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.TOAST)
    self.page.imports.reload()

  def time(self, hour=None, minute=None, width=(170, "px"), height=(None, "px"), html_code=None, profile=None,
           options=None):
    """
    Description:
    ------------
    Component that selects specific time.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/

    Attributes:
    ----------
    :param hour: Number. optional. The initial hour.
    :param minute: Number. optional. The initial minute.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    return self.times.selectbox(hour, minute, width, height, html_code, profile, options)

  @property
  def fields(self):
    """
    Description:
    ------------
    Toast predefined form input fields.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/
      https://nhn.github.io/tui.time-picker/latest/
    """
    return ToastFields(self)

  @property
  def times(self):
    """
    Description:
    ------------
    Toast times components and configurations.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/
      https://nhn.github.io/tui.time-picker/latest/tutorial-example01-basic
    """
    self.page.cssImport.add("tui-time-picker")
    self.page.jsImports.add("tui-time-picker")
    return ToastTimes(self)

  def date(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    Toast default date component.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value:
    :param width:
    :param height:
    :param html_code:
    :param profile:
    :param options:
    """
    return self.dates.date(value, width, height, html_code, profile, options)

  def calendar(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    A JavaScript schedule calendar that is full featured. Now your service just got the customizable calendar.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/

    Attributes:
    ----------
    :param value:
    :param width:
    :param height:
    :param profile:
    :param options:
    :param html_code:
    """
    return self.calendars.monthly(value, width, height, html_code, profile, options)

  @property
  def dates(self):
    """
    Description:
    ------------
    Toast Date components and configurations.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/
    """
    self.page.cssImport.add("tui-date-picker")
    self.page.jsImports.add("tui-date-picker")
    return ToastDates(self)

  @property
  def calendars(self):
    """
    Description:
    ------------
    The Calendar supports monthly, weekly, daily views and more, and you can create or edit your schedule with a
    simple dragging motion.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/
    """
    self.page.cssImport.add("tui-calendar")
    self.page.jsImports.add("tui-calendar")
    return ToastCalendars(self)

  @property
  def grids(self):
    """
    Description:
    ------------
    The Grid is a powerful library with features like data editing, filtering, sorting, and more, and can be used to
    customize the editor or the renderer to your desired format.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/tutorial-example05-relation-columns
    """
    self.page.cssImport.add("tui-grid")
    self.page.jsImports.add("tui-grid")
    return ToastGrids(self)

  @property
  def charts(self):
    """
    Description:
    ------------
    The Chart makes your data pop, and it is easy to use. It provides you with multiple charts like Bar, Column, Line,
    and more.

    Related Pages:

      https://nhn.github.io/tui.chart/latest/
    """
    return ToastCharts(self)

  def editor(self, value=None, profile=None, width=(100, "%"), height=(330, "px"), options=None, html_code=None):
    """
    Description:
    ------------
    The Editor allows you to edit your Markdown documents using text or WYSIWYG and comes with Syntax Highlighting,
    Scroll-Sync, Live Preview, and Chart features.

    Related Pages:

      https://ui.toast.com/tui-editor

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to the component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {}
    if options is not None:
      dfl_options.update(options)
    editor = html.HtmlToastEditor.Editor(self.page, width, height, html_code, dfl_options, profile)
    if value is not None:
      editor.options.initialValue = value
    return editor

  @property
  def js(self):
    """
    Description:
    ------------
    The Grid is a powerful library with features like data editing, filtering, sorting, and more, and can be used to
    customize the editor or the renderer to your desired format.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/tutorial-example05-relation-columns
    """
    self.page.jsImports.add("tui-code-snippet")
    return JsToast.Js(self)
