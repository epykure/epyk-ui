from typing import Union
from epyk.core.py import primitives
from epyk.core.html.options import OptionsWithTemplates
from epyk.core.js import JsUtils
import abc


class OptionsChart(OptionsWithTemplates):
    component_properties = ("opacity", "get_width", "get_height")

    @property
    def get_width(self):
        """  Get the container available with in pixel (including the padding). """
        return self._config_get(JsUtils.jsWrap(
            "function(component){return component.clientWidth - (parseFloat(component.style.paddingLeft) + parseFloat(component.style.paddingRight)) }"))

    @get_width.setter
    def get_width(self, num: int):
        self._config(num)

    @property
    def get_height(self):
        """ Get the container available height in pixel (including the padding). """
        return self._config_get(JsUtils.jsWrap(
            "function(component){return component.clientHeight - (parseFloat(component.style.paddingTop) + parseFloat(component.style.paddingBottom))}"))

    @get_height.setter
    def get_height(self, num: int):
        self._config(num)

    @property
    def height(self):
        return self._config_get(None)

    @height.setter
    def height(self, num: int):
        self._config(num)

    @property
    def opacity(self):
        return self._config_get(0.5)

    @opacity.setter
    def opacity(self, num: float):
        self._config(num)

    @property
    def type(self):
        return self._config_get(None)

    @type.setter
    def type(self, value: str):
        self._config(value)

    @property
    def colors(self):
        return self._config_get(None)

    @colors.setter
    def colors(self, colors: list):
        self._config(colors)

    @property
    def background_colors(self):
        return self._config_get(None)

    @background_colors.setter
    def background_colors(self, colors: list):
        self._config(colors)

    @property
    def y_columns(self):
        return self._config_get(None)

    @y_columns.setter
    def y_columns(self, cols: list):
        self._config(cols)

    @property
    def x_axis(self):
        return self._config_get(None)

    @x_axis.setter
    def x_axis(self, col: str):
        self._config(col)

    @property
    def props(self):
        return self._config_get({})

    @props.setter
    def props(self, values: dict):
        self._config(values)

    @property
    def commons(self):
        return self._config_get({})

    @commons.setter
    def commons(self, values: dict):
        self._config(values)


class OptionsChartShared(abc.ABC):

    def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
        self.component, self.page = component, page
        if page is None:
            self.page = component.page

    @abc.abstractmethod
    def x_format(self, js_funcs, profile: Union[dict, bool] = None):
        """

        :param js_funcs:
        :param profile:
        """

    @abc.abstractmethod
    def x_format_money(self, symbol="", digit=0, thousand_sep=".", decimal_sep=",", fmt="%v %s", factor=None, alias=""):
        """

        :param symbol:
        :param digit:
        :param thousand_sep:
        :param decimal_sep:
        :param fmt:
        :param factor:
        :param alias:
        """

    @abc.abstractmethod
    def x_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
        """

        :param factor:
        :param alias:
        :param digits:
        :param thousand_sep:
        """

    @abc.abstractmethod
    def x_label(self, value: str):
        """
        Set the label of the x axis.

        :param value: The axis label.
        """

    @abc.abstractmethod
    def x_tick_count(self, num):
        """

        :param num:
        """

    @abc.abstractmethod
    def y_format(self, js_funcs, profile: Union[dict, bool] = None):
        """

        :param js_funcs:
        :param profile:
        """

    @abc.abstractmethod
    def y_format_money(self, symbol: str = "", digit: int = 0, thousand_sep: str = ".", decimal_sep: str = ",",
                       fmt: str = "%v %s", factor: int = None, alias: str = ""):
        """

        :param symbol:
        :param digit:
        :param thousand_sep:
        :param decimal_sep:
        :param fmt:
        :param factor:
        :param alias:
        """

    @abc.abstractmethod
    def y_format_number(self, factor=1000, alias=None, digits=0, thousand_sep="."):
        """

        :param factor:
        :param alias:
        :param digits:
        :param thousand_sep:
        """

    @abc.abstractmethod
    def y_label(self, value):
        """
        Set the label of the y axis.

        :param value: String. The axis label.
        """

    @abc.abstractmethod
    def y_tick_count(self, num):
        """

        :param num:
        """
