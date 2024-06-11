from typing import Union
from epyk.core.py import primitives, types
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class ECharts(JsPackage):
    lib_alias = {'js': 'echarts'}

    def on(self, event_type: Union[str, primitives.JsDataModel], js_funcs: types.JS_FUNCS_TYPES,
           profile: types.PROFILE_TYPE = False):
        """Binds event-handling function.

        `ECharts <https://echarts.apache.org/en/api.html#echartsInstance.on>`_

        :param event_type:
        :param js_funcs:
        :param profile:
        """
        event_type = JsUtils.jsConvertData(event_type, None)
        return JsUtils.jsWrap("%s.on(%s, function (params) {%s})" % (
            self.varName, event_type, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

    def off(self, event_type: Union[str, primitives.JsDataModel], js_funcs: types.JS_FUNCS_TYPES,
           profile: types.PROFILE_TYPE = False):
        """Unbind event-handler function.

        `ECharts <https://echarts.apache.org/en/api.html#echartsInstance.off>`_

        :param event_type:
        :param js_funcs:
        :param profile:
        """
        event_type = JsUtils.jsConvertData(event_type, None)
        return JsUtils.jsWrap("%s.on(%s, function (params) {%s})" % (
            self.varName, event_type, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

    def dispatchAction(self, type: Union[str, primitives.JsDataModel], **kwargs):
        """

        :param type:
        :param kwargs:
        """
        type = JsUtils.jsConvertData(type, None)
        if not kwargs:
            return JsUtils.jsWrap("%s.dispatchAction({type: %s}})" % (self.varName, type))

        lnames = ["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in kwargs.items()]
        return JsUtils.jsWrap("%s.dispatchAction({type: %s, %s}})" % (
            self.varName, type, ",".join(lnames)))

    def connect(self, charts: list):
        """Connects interaction of multiple chart series.

        `ECharts <https://echarts.apache.org/en/api.html#echarts.disconnect>`_

        :param charts: List of charts object.
        """
        chart_ids = [k.varName for k in charts]
        if not self.varName in chart_ids:
            chart_ids.append(self.varName)
        return JsUtils.jsWrap("echarts.connect([%s])" % ",".join(chart_ids))

    def disconnect(self, charts: list):
        """Disconnects interaction of multiple chart series. To have one single instance to be removed, you can set
        group of chart instance to be null.

        `ECharts <https://echarts.apache.org/en/api.html#echarts.disconnect>`_

        :param charts: List of charts object.
        """
        chart_ids = [k.varName for k in charts]
        if not self.varName in chart_ids:
            chart_ids.append(self.varName)
        return JsUtils.jsWrap("echarts.disconnect([%s])" % ",".join(chart_ids))

    def appendData(self, seriesIndex: int = None, data = None):
        """The method is used in rendering millions of data.

        `ECharts <https://echarts.apache.org/en/api.html#echartsInstance.appendData>`_

        :param seriesIndex:
        :param data:
        """
        return JsUtils.jsWrap("%s.appendData({seriesIndex: %s, data: %s}})" % (self.varName, seriesIndex, data))

    def dispose(self):
        """Destroys chart instance, after which the instance cannot be used any more.

        `ECharts <https://echarts.apache.org/en/api.html#echarts.dispose>`_
        """
        return JsUtils.jsWrap("echarts.dispose({target: %s}})" % (self.varName))

    def getOption(self):
        """Gets option object maintained in current instance, which contains configuration item and data merged from
        previous setOption operations by users, along with user interaction states. For example, switching of legend,
        zooming area of data zoom, and so on. Therefore, a new instance that is exactly the same can be recovered from
        this option.
        """
        return JsObjects.JsObject.JsObject.get("%s.getOption()" % self.varName)

    def setOption(self, options: Union[list, primitives.JsDataModel]):
        """Configuration item, data, universal interface, all parameters and data can all be modified through setOption.

        `ECharts <https://echarts.apache.org/en/api.html#echartsInstance.setOption>`_

        :param options: Echarts options
        """
        options = JsUtils.jsConvertData(options, None)
        return JsObjects.JsObject.JsObject.get("%s.setOption(%s)" % (self.varName, options))

    def clear(self):
        """Clears current instance; removes all components and series in current instance.

        `ECharts <https://echarts.apache.org/en/api.html#echartsInstance.clear>`_
        """
        return JsUtils.jsWrap("echarts.clear()" % self.varName)

    def isDisposed(self):
        """Returns whether current instance has been disposed.

        `ECharts <https://echarts.apache.org/en/api.html#echartsInstance.isDisposed>`_
        """
        return JsUtils.jsWrap("echarts.isDisposed()" % self.varName)

    def dispose(self):
        """Returns whether current instance has been disposed.

        `ECharts <https://echarts.apache.org/en/api.html#echartsInstance.dispose>`_
        """
        return JsUtils.jsWrap("echarts.dispose()" % self.varName)

    def resize(self):
        return JsUtils.jsWrap("%s.resize()" % self.varName)

    def showLoading(self):
        return JsUtils.jsWrap("%s.showLoading()" % self.varName)

    def hideLoading(self):
        return JsUtils.jsWrap("%s.hideLoading()" % self.varName)
