from epyk.core.html import graph


class Vis2D:

    def __init__(self, ui):
        self.page = ui.page
        self.chartFamily = "Vis"

    def plot(self, record=None, y=None, x=None, kind="line", profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

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
        if not isinstance(y, list):
            y = [y]
        return getattr(self, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                                   options=options, html_code=html_code)

    def line(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
             options=None, html_code=None):
        """ Graph2d is an interactive visualization chart to draw data in a 2D graph. You can freely move and zoom in the graph
        by dragging and scrolling in the window.

        Graph2d uses HTML DOM and SVG for rendering. This allows for flexible customization using css styling.

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        Related Pages::

          https://visjs.github.io/vis-timeline/examples/graph2d/16_bothAxisTitles.html

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        data = self.page.data.vis.xy(record or [], y_columns, x_axis)
        line_chart = graph.GraphVis.ChartLine(self.page, width, height, html_code, options, profile)
        for d in data:
            line_chart.add_items(d)
        return line_chart

    def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
                options=None, html_code=None):
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        data = self.page.data.vis.xy(record, y_columns, x_axis)
        line_chart = graph.GraphVis.ChartScatter(self.page, width, height, html_code, options, profile)
        line_chart.options.height = height[0]
        for d in data:
            line_chart.add_items(d)
        return line_chart

    def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        data = self.page.data.vis.xy(record, y_columns, x_axis)
        line_chart = graph.GraphVis.ChartBar(self.page, width, height, html_code, options, profile)
        line_chart.options.height = height[0]
        for d in data:
            line_chart.add_items(d)
        return line_chart

    def timeline(self, record=None, start=None, content=None, end=None, type=None, group=None, profile=None,
                 width=(100, "%"), height=(330, "px"), options=None, html_code=None):
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record:
        :param start:
        :param content:
        :param end:
        :param type:
        :param group:
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        data = self.page.data.vis.timeline(record, start, content, end, type, group, options)
        line_chart = graph.GraphVis.ChartTimeline(self.page, width, height, html_code, options, profile)
        line_chart.options.height = height[0]
        line_chart.options.editable = True
        line_chart.options.showCurrentTime = True
        if data['datasets']:
            line_chart.add_items(data['datasets'])
        return line_chart

    def network(self, profile=None, width=(100, "%"), height=(330, "px"), options=None, html_code=None):
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        line_chart = graph.GraphVis.ChartNetwork(self.page, width, height, html_code, options, profile)
        line_chart.options.height = height[0]
        return line_chart


class Vis3D:

    def __init__(self, ui):
        self.page = ui.page
        self.chartFamily = "Vis"

    def line(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"),
             options=None, html_code=None) -> graph.GraphVis.Chart3DLine:
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        data = self.page.data.vis.xyz(record, y_columns, x_axis, z_axis)
        line_chart = graph.GraphVis.Chart3DLine(self.page, width, height, html_code, options, profile)
        for d in data:
            line_chart.add_items(d)
        return line_chart

    def bar(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"),
            options=None, html_code=None) -> graph.GraphVis.Chart3DBar:
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        data = self.page.data.vis.xyz(record, y_columns, x_axis, z_axis)
        line_chart = graph.GraphVis.Chart3DBar(self.page, width, height, html_code, options, profile)
        for d in data:
            line_chart.add_items(d)
        return line_chart

    def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
                height=(400, "px"), options=None, html_code=None) -> graph.GraphVis.Chart3D:
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        data = self.page.data.vis.xyz(record, y_columns, x_axis, z_axis)
        line_chart = graph.GraphVis.Chart3D(self.page, width, height, html_code, options, profile)
        for d in data:
            line_chart.add_items(d)
        return line_chart

    def scatter(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
                height=(400, "px"), options=None, html_code=None) -> graph.GraphVis.Chart3DScatter:
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param z_axis: The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        data = self.page.data.vis.xyz(record, y_columns, x_axis, z_axis)
        line_chart = graph.GraphVis.Chart3DScatter(self.page, width, height, html_code, options, profile)
        for d in data:
            line_chart.add_items(d)
        return line_chart


class Vis(Vis2D):

    def __init__(self, ui):
        super(Vis, self).__init__(ui)
        self._3d = Vis3D(ui)

    def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
                height=(400, "px"), options=None, html_code=None) -> graph.GraphVis.Chart3D:
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        return self._3d.surface(record, y_columns, x_axis, z_axis, profile, width, height, options, html_code)

    def bar3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
              height=(400, "px"),
              options=None, html_code=None) -> graph.GraphVis.Chart3DBar:
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        return self._3d.bar(record, y_columns, x_axis, z_axis, profile, width, height, options, html_code)

    def scatter3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
                  height=(400, "px"), options=None, html_code=None) -> graph.GraphVis.Chart3DScatter:
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        return self._3d.scatter(record, y_columns, x_axis, z_axis, profile, width, height, options, html_code)

    def line3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"),
               height=(400, "px"),
               options=None, html_code=None) -> graph.GraphVis.Chart3DLine:
        """

        :tags:
        :categories:

        `VisJs <https://visjs.org/>`_

        :param record: List of dict. The Python record.
        :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
        :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param z_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        """
        return self._3d.line(record, y_columns, x_axis, z_axis, profile, width, height, options, html_code)
