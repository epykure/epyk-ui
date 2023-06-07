#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from typing import List
from epyk.core.css.themes import palettes


class ColorRange:

    def __init__(self, colors: list, index: int = None):
        self.__colors = colors
        self.index = index or round(len(colors) / 2)

    def __iter__(self):
        """ Make the object iterable """
        yield from self.__colors

    def __getitem__(self, item: int):
        """ Make the object subscriptable """
        return self.__colors[item]

    def reverse(self):
        self.__colors = self.__colors[::-1]

    @property
    def light(self):
        return self.__colors[0]

    @property
    def dark(self):
        return self.__colors[-1]

    @property
    def base(self):
        return self.__colors[self.index]


class Theme:
    dark = False
    _greys = ['#FFFFFF', '#f5f5f5', '#eeeeee', '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242',
              '#212121', '#000000']
    _info = ["#e3f2fd", "#2196f3", "#0d47a1"]

    def __init__(self, ovr_attrs: dict = None, index: int = 5, step: int = 1):
        self.__colors = {
            "charts": list(self._charts),
            "colors": list(self._colors),
            "greys": list(self._greys),
            "warning": ColorRange(self._warning),
            "danger": ColorRange(self._danger),
            "success": ColorRange(self._success),
            "info": ColorRange(self._info),
            "all": {}
        }
        self.chart_categories = []
        self.index = index
        self.step = step
        if ovr_attrs is not None:
            self.__colors.update(ovr_attrs)

    def notch(self, value: int = None, step: int = None):
        """
        Get the base color from the theme.
        The base color can change and it is defined by the variable self.index.

        Usage::

          base_color = page.theme.notch()

        :param value: Optional. The number of notch from the centered index.
        :param step: Optional The value of a move (default 1).
        """
        step = step or self.step
        if value is not None:
            return self.colors[max(0, min(self.index + value * step, len(self.colors) - 1))]

        return self.colors[self.index]

    @property
    def white(self):
        """
        Get the white color from the theme.

        Usage::

          color = page.theme.white
        """
        return self.__colors["greys"][0]

    def dark_or_white(self, light=True) -> str:
        """
        Get the appropriate light or dark color according to the theme.
        Setting the Light flag to true will point to white in light mode otherwise it will point to black.
        """
        if light:
            return self.black if self.dark else self.white

        return self.white if self.dark else self.black

    @property
    def black(self):
        """
        Get the black color from the theme.

        Usage::

          color = page.theme.black
        """
        return self.__colors["greys"][-1]

    @property
    def charts(self):
        """
        Get the chart colors from the theme.

        Usage::

          colors = page.theme.charts
        """
        return self.__colors["charts"]

    @charts.setter
    def charts(self, colors: list):
        self.__colors["charts"] = colors

    @property
    def colors(self):
        """
        Get the theme colors scale.

        Usage::

          colors = page.theme.colors
        """
        if self.dark:
            return self.__colors["colors"][::-1]

        return self.__colors["colors"]

    @colors.setter
    def colors(self, colors: list):
        self.__colors["colors"] = colors

    @property
    def greys(self):
        """
        Get the theme grey colors scale.

        Usage::

          colors = page.theme.greys
        """
        if self.dark:
            return self.__colors["greys"][::-1]

        return self.__colors["greys"]

    @greys.setter
    def greys(self, colors: list):
        self.__colors["greys"] = colors

    @property
    def warning(self) -> ColorRange:
        """
        Get the warning colors. It is a tuple (light, dark).

        Usage::

          light, dark = page.theme.warning
        """
        return self.__colors["warning"]

    @warning.setter
    def warning(self, colors: list):
        self.__colors["warning"] = ColorRange(colors)

    @property
    def danger(self) -> ColorRange:
        """
        Get the danger colors. It is a tuple (light, dark).

        Usage::

          light, dark = page.theme.danger
        """
        return self.__colors["danger"]

    @danger.setter
    def danger(self, colors: list):
        self.__colors["danger"] = ColorRange(colors)

    @property
    def info(self) -> ColorRange:
        """
        Get the info colors. It is a tuple (light, dark).

        Usage::

          light, dark = page.theme.danger
        """
        return self.__colors["info"]

    @info.setter
    def info(self, colors: list):
        self.__colors["info"] = ColorRange(colors)

    @property
    def success(self) -> ColorRange:
        """
        Get the success colors. It is a tuple (light, dark).

        Usage::

          light, dark = page.theme.success
        """
        return self.__colors["success"]

    @success.setter
    def success(self, colors: list):
        self.__colors["success"] = ColorRange(colors)

    def color_palette(self, palette: str = None, n_colors: int = None, desat: float = None):
        """
        Change the chart color codes using standard palettes used in JavaScript and Python libraries.

        Related Pages:

          https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html

        :param palette: Optional. Name of palette or None to set for charts colors
        :param n_colors: Optional. Number of colors in the palette
        :param desat: Optional. Proportion to desaturate each color by
        """
        if palette is not None and palette.startswith("brewer."):
            self.__colors["charts"] = getattr(palettes.brewer, palette.split(".")[1])
        elif palette is not None and palette.startswith("office."):
            self.__colors["charts"] = getattr(palettes.office, palette.split(".")[1])
        elif palette is not None and palette.startswith("tableau."):
            self.__colors["charts"] = getattr(palettes.tableau, palette.split(".")[1])

    def from_sass(self, file_path: str):
        """
        Load the SASS file to set the colors codes.

        Usage::

            page = pk.Page()
            page.theme.dark = True
            page.theme.from_sass("../components/assets/theme.scss")

        :param file_path: The full file path
        """
        regex = re.compile("\$(.*): (.*);")
        with open(file_path) as fp:
            content = fp.read()
            for m in regex.findall(content):
                tag, color = m
                if tag.startswith("color") or tag.startswith("chart-"):
                    _, category, level = tag.split("-")
                    self.__colors["all"].setdefault(category, {})[tag] = color.strip()
                if tag.startswith("charts"):
                    self.chart_categories = [s.strip() for s in color.strip()[1:-1].split(",")]
        if self.chart_categories:
            chart_colors = []
            tmp_chart_map = {self.chart_categories[0]: self.category(self.chart_categories[0])[::-1]}
            for i in range(0, len(tmp_chart_map[self.chart_categories[0]])):
                for cat in self.chart_categories:
                    if cat not in tmp_chart_map:
                        tmp_chart_map[cat] = self.category(cat)[::-1]
                    chart_colors.append(tmp_chart_map[cat][i])
            self.charts = chart_colors
        self.update()

    def monochrome(self, name: str, reverse: bool = None):
        """
        Change the chart definition to use a unique category.
        This must be defined from a CSS file (no default category available).

        :param name: The category name
        :param reverse: Set the color order (default from dark to light)
        """
        colors = self.category(name)
        reverse = reverse or not self.dark
        if reverse:
            colors = colors[::-1]
        self.charts = colors

    def update(self):
        """ Sync the colors with the ones stored from the static file. """
        for category, colors in self.__colors["all"].items():
            if category == "theme":
                #self._colors = self.category("theme")
                self.colors = self.category("theme")
            elif category == "greys":
                #self._greys = self.category("grey")
                self.greys = self.category("grey")
            elif category == "warning":
                #self._warning = self.category("warning")
                self.warning =self.category("warning")
            elif category == "danger":
                #self._danger = self.category("danger")
                self.danger = self.category("danger")
            elif category == "success":
                #self._success = self.category("success")
                self.success = self.category("success")
            elif category == "info":
                #self._info = self.category("info")
                self.info = self.category("info")

    def category(self, name: str, reverse: bool = None) -> List[str]:
        """
        Get the colors for a given category.

        :param name: The color category
        :param reverse: Set the color order (default from light to dark)
        """
        reverse = reverse or self.dark
        colors = {int(k.split("-")[-1]): v for k, v in self.__colors["all"][name].items()}
        return [colors[k] for k in sorted(colors, reverse=reverse)]

    def all(self) -> dict:
        colors_code = {}
        for v in self.__colors["all"].values():
            colors_code.update(v)
        return colors_code


class ThemeCustom(Theme):
    _charts, _colors, _greys = [], [], []
    _warning, _danger, _success = set(), set(), set()


class ThemeDefault(Theme):
    _charts = [
        '#009999', '#336699', '#ffdcb9',
        '#cc99ff', '#b3d9ff', '#ffff99',
        '#000066', '#b2dfdb', '#80cbc4',
        '#e0f2f1', '#b2dfdb', '#80cbc4',  # teal
        '#ffebee', '#ffcdd2', '#ef9a9a',  # red
        '#f3e5f5', '#e1bee7', '#ce93d8',  # purple
        '#ede7f6', '#d1c4e9', '#b39ddb',  # deep purple
        '#e8eaf6', '#c5cae9', '#9fa8da',  # indigo
        '#fffde7', '#fff9c4', '#fff59d',  # yellow
        '#fff3e0', '#ffe0b2', '#ffcc80',  # orange
        '#efebe9', '#d7ccc8', '#bcaaa4',  # brown
    ]
    _colors = ['#f4f9fc', '#cfd8dc', '#b0bec5', '#90a4ae', '#78909c', '#607d8b', '#546e7a', '#455a64',
               '#37474f', '#263238']
    _warning, _danger, _success = ['#FFF3CD', '#e2ac00'], ["#F8D7DA", "#C00000"], ['#e8f2ef', '#5DDEAD']
