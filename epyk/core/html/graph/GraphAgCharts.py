
from typing import List

from epyk.core.py import primitives, types
from epyk.core.html.options import OptAgCharts
from epyk.core.html.tables import HtmlTableAgGrid


class Chart(HtmlTableAgGrid.Table):
    name = 'AgCharts'
    tag = "div"
    requirements = ('ag-charts-community',)
    _type = None
    _option_cls = OptAgCharts.AgChartsConfig

    def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
        data, columns, self.__config, self.q_filter = [], [], None, None
        super(Chart, self).__init__(page, records, width, height, html_code, options, profile)
        self.options.data = records or []
        self.options.container = self.dom.varId

    @property
    def options(self) -> OptAgCharts.AgChartsConfig:
        """Ag Charts options. """
        return super().options

    def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """Common JavaScript function to add series to the chart.

        :param data: Optional.
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The object reference ID
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        self.js_code = component_id
        if data is not None:
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(self.html_code)
            return "%s;if(!%s){%s};%s" % (
                self.js.setRowData(data, dataflows=dataflows).toStr(), self.js.getDisplayedRowCount().toStr(),
                self.js.showNoRowsOverlay().toStr(), state_expr)

        return 'var %(tableId)s = agCharts.AgCharts.create(%(config)s);' % {
            'tableId': self.js_code, 'config': self.options.config_js(options, incl_settings=False),
            'htmlCode': self.dom.varName}
