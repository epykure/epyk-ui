from epyk.core.html import graph


class CompChartFrappe:

  def __init__(self, ui):
    self.page = ui.page

  def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Related Pages:

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
    ------------
    Create a line chart from Frappe Chart libraries.

    Usage::

      c = page.ui.charts.frappe.line(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      text = page.ui.input("Italy")
      slider = page.ui.sliders.range(minimum=1990, maximum=2020)
      page.ui.button("Click").click([
      page.js.d3.csv(data_urls.DEMO_COUNTRY).filterCol("Country Name", text.dom.content).cast(["Year", "Value"]).
         filterCol("Year", slider.dom.min_select, ">").filterCol("Year", slider.dom.max_select, "<").get(
           [#"data = data.slice(1)",
          c.build(pk.events.data)])
      ])

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
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.Frappe(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    ------------
    Create a bar chart from Frappe Chart libraries.

    Usage::

      c = page.ui.charts.frappe.bar(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      text = page.ui.input("Italy")
      slider = page.ui.sliders.range(minimum=1990, maximum=2020)
      page.ui.button("Click").click([
      page.js.d3.csv(data_urls.DEMO_COUNTRY).filterCol("Country Name", text.dom.content).cast(["Year", "Value"]).
         filterCol("Year", slider.dom.min_select, ">").filterCol("Year", slider.dom.max_select, "<").get(
           [#"data = data.slice(1)",
          c.build(pk.events.data)])
      ])

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
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappeBar(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i], kind='bar')
    return line_chart

  def percentage(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
                 options=None, html_code=None):
    """
    Description:
    ------------

    Usage::

      c = page.ui.charts.frappe.percentage(y_columns=["Value"], x_axis="Year", height=(500, "px"))
      text = page.ui.input("Italy")
      slider = page.ui.sliders.range(minimum=1990, maximum=2020)
      page.ui.button("Click").click([
        page.js.fetch(data_urls.DEMO_COUNTRY).csvtoRecords().filterCol("Country Name", text.dom.content).cast(["Year", "Value"]).
          filterCol("Year", slider.dom.min_select, ">").filterCol("Year", slider.dom.max_select, "<").
          get([
            c.build(pk.events.data),
        ])
      ])

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
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappePercentage(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def donut(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappeDonut(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def pie(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappePie(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart

  def heatmap(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    options = options or {}
    options.update({'y_columns': y_columns or [], 'x_column': x_axis})
    line_chart = graph.GraphFrappe.FrappeHeatmap(self.page, width, height, html_code, options, profile)
    line_chart.options.height = height[0]
    line_chart.colors(self.page.theme.charts)
    data = self.page.data.c3.y(record or [], y_columns, x_axis)
    line_chart.labels(data["labels"])
    for i, dataset in enumerate(data["datasets"]):
      line_chart.add_dataset(dataset, data["series"][i])
    return line_chart
