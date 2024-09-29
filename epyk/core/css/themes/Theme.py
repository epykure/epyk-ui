#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
from typing import List, Optional, Dict
from epyk.core.css.themes import palettes
from epyk.core.css.Colors import THEME_REFERENCE


class ColorRange:

    def __init__(self, colors: List[str], index: int = None):
        self.__colors = colors
        self.index = index or round(len(colors) / 2)

    def __iter__(self):
        """Make the object iterable"""
        yield from self.__colors

    def __getitem__(self, item: int) -> str:
        """Make the object subscriptable"""
        return self.__colors[item]

    def reverse(self):
        """Reverse the color range (when DARK_MODE is switched on / off)"""
        self.__colors = self.__colors[::-1]

    @property
    def light(self) -> str:
        """Lightest color from the internal colors range"""
        return self.__colors[0]

    @property
    def dark(self) -> str:
        """Darkest color from the internal colors range"""
        return self.__colors[-1]

    @property
    def base(self) -> str:
        return self.__colors[self.index]


class Theme:
    dark = False
    name: Optional[str] = None
    _greys = ['#FFFFFF', '#f5f5f5', '#eeeeee', '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242',
              '#212121', '#000000']
    _info = ["#e3f2fd", "#2196f3", "#0d47a1"]
    # Add extra groups to a theme
    other_groups: Optional[Dict[str, List[str]]] = None

    def __init__(self, ovr_attrs: dict = None, index: int = 5, step: int = 1):
        sys_categories = ["charts", "colors", "greys"]
        sys_color_ranges = ["warning", "danger", "success", "info"]
        self.__colors = {"all": {}}
        for c in sys_categories:
            if not hasattr(self, "_%s" % c):
                #TODO - To be reviewed
                ...
            else:
                self.__colors[c] = getattr(self, "_%s" % c, [])
        for c in sys_color_ranges:
            self.__colors[c] = ColorRange(getattr(self, "_%s" % c, []))
        self.chart_categories = []
        self.index = index
        self.step = step
        if ovr_attrs is not None:
            self.__colors.update(ovr_attrs)
        if self.other_groups:
            for k, c in self.other_groups.items():
                self.__colors["all"][k] = {}
                for i, v in enumerate(c, start=1):
                    self.__colors["all"][k]["%s-%s" % (k, i)] = v

    def notch(self, value: int = None, step: int = None) -> str:
        """Get the base color from the theme.
        The base color can change and it is defined by the variable self.index.

        Usage::

          base_color = page.theme.notch()

        :param value: Optional. The number of notch from the centered index
        :param step: Optional The value of a move (default 1)
        """
        step = step or self.step
        if value is not None:
            return self.colors[max(0, min(self.index + value * step, len(self.colors) - 1))]

        return self.colors[self.index]

    def __getitem__(self, item: str):
      """

      This will raise an exception if the group does not exist for the theme.
      """
      if item in self.__colors:
        return self.__colors[item]

      return self.other_groups[item]

    @property
    def white(self) -> str:
        """Get the white color from the theme.

        Usage::

          color = page.theme.white
        """
        return self["greys"][0]

    def dark_or_white(self, light: bool = True) -> str:
        """Get the appropriate light or dark color according to the theme.
        Setting the Light flag to true will point to white in light mode otherwise it will point to black.

        :param light:
        """
        if light:
            return self.black if self.dark else self.white

        return self.white if self.dark else self.black

    @property
    def black(self) -> str:
        """Get the black color from the theme.

        Usage::

          color = page.theme.black
        """
        return self["greys"][-1]

    @property
    def charts(self) -> List[str]:
        """Get the chart colors from the theme.

        Usage::

          colors = page.theme.charts
        """
        return self["charts"]

    @charts.setter
    def charts(self, colors: list):
        self.__colors["charts"] = colors

    @property
    def colors(self) -> List[str]:
        """Get the theme colors scale.

        Usage::

          colors = page.theme.colors
        """
        if self.dark:
            return self["colors"][::-1]

        return self["colors"]

    @colors.setter
    def colors(self, colors: list):
        self.__colors["colors"] = colors

    @property
    def greys(self) -> List[str]:
        """Get the theme grey colors scale.

        Usage::

          colors = page.theme.greys
        """
        if self.dark:
            return self["greys"][::-1]

        return self["greys"]

    @greys.setter
    def greys(self, colors: list):
        self.__colors["greys"] = colors

    @property
    def warning(self) -> ColorRange:
        """Get the warning colors. It is a tuple (light, dark).

        Usage::

          light, dark = page.theme.warning
        """
        return self["warning"]

    @warning.setter
    def warning(self, colors: list):
        self.__colors["warning"] = ColorRange(colors)

    @property
    def danger(self) -> ColorRange:
        """Get the danger colors. It is a tuple (light, dark).

        Usage::

          light, dark = page.theme.danger
        """
        return self["danger"]

    @danger.setter
    def danger(self, colors: list):
        self.__colors["danger"] = ColorRange(colors)

    @property
    def info(self) -> ColorRange:
        """Get the info colors. It is a tuple (light, dark).

        Usage::

          light, dark = page.theme.danger
        """
        return self["info"]

    @info.setter
    def info(self, colors: list):
        self.__colors["info"] = ColorRange(colors)

    @property
    def success(self) -> ColorRange:
        """Get the success colors. It is a tuple (light, dark).

        Usage::

          light, dark = page.theme.success
        """
        return self["success"]

    @success.setter
    def success(self, colors: list):
        self.__colors["success"] = ColorRange(colors)

    def color_palette(self, palette: str = None, n_colors: int = None, desat: float = None):
        """Change the chart color codes using standard palettes used in JavaScript and Python libraries.

        `Color Chart <https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html>`_

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

    def from_sass(self, file_path: str = "COLORS.SCSS"):
        """Load the SASS file to set the colors codes.

        Usage::

            page = pk.Page()
            page.theme.dark = True
            page.theme.from_sass("../components/assets/theme.scss")

        :param file_path: The full file path
        """
        regex = re.compile("\$(.*): (.*);")
        if os.path.isfile(file_path):
            head, tail = os.path.split(file_path)
            self.name = tail[:-5]
            with open(file_path) as fp:
                content = fp.read()
                for m in regex.findall(content):
                    tag, color = m
                    if tag.startswith("color") or tag.startswith("chart-"):
                        _, category, _ = tag.split("-")
                        self.__colors["all"].setdefault(category, {})[tag] = color.strip()
                    if tag.startswith("charts"):
                        if color.strip().startswith("("):
                            self.chart_categories = [s.strip() for s in color.strip()[1:-1].split(",")]
                        else:
                            self.chart_categories = ["default"]
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
        """Change the chart definition to use a unique category.
        This must be defined from a CSS file (no default category available).

        :param name: The category name
        :param reverse: Set the color order (default from dark to light)
        """
        colors = self.category(name)
        reverse = reverse or not self.dark
        if reverse:
            colors = colors[::-1]
        self.charts = colors

    @property
    def groups(self) -> List[str]:
        """Get all the technical / extra colors categories defined for a selected theme"""
        if self.other_groups is not None:
          return ["theme", "grey", "warning", "danger", "success", "info"] + list(self.other_groups.keys())

        return ["theme", "grey", "warning", "danger", "success", "info"]

    def update(self):
        """ Sync the colors with the ones stored from the static file. """
        for category in self.__colors["all"].keys():
            if category == "theme":
                self.colors = self.category("theme")
            elif category == "greys":
                self.greys = self.category("grey")
            elif category == "warning":
                self.warning = self.category("warning")
            elif category == "danger":
                self.danger = self.category("danger")
            elif category == "success":
                self.success = self.category("success")
            elif category == "info":
                self.info = self.category("info")
            else:
                # Add the extra category to the internal mapping anyway
                if self.other_groups is None:
                  self.other_groups = {}
                self.other_groups[category] = self.category(category)

    def category(self, name: str, reverse: bool = None) -> List[str]:
        """Get the colors for a given category.

        Usages::

            import epyk as ek

            ek.helpers.scss_colors()
            page.theme.from_sass()
            print(page.theme.category("default"))

        :param name: The color category
        :param reverse: Optional. Set the color order (default from light to dark)
        """
        reverse = reverse or self.dark
        if name not in self.__colors["all"]:
            return []

        colors = {int(k.split("-")[-1]): v for k, v in self.__colors["all"][name].items()}
        return [colors[k] for k in sorted(colors, reverse=reverse)]

    def all(self) -> dict:
        colors_code = {}
        # Add main colors theme
        for k in self.groups:
            v = "%s-%%s" % k
            if k == "theme":
                colors = getattr(self, "_colors", None)
                v = "theme-%s"
            elif hasattr(self, "_%s" % k):
                colors = getattr(self, "_%s" % k)
                if self.dark:
                    colors = colors[::-1]
            elif hasattr(self, "_%ss" % k):
                colors = getattr(self, "_%ss" % k)
                if self.dark:
                    colors = colors[::-1]
                v = "%ss-%%s" % k
            else:
                colors = self.category(k)
            if colors:
                for i, c in enumerate(colors):
                    colors_code[v % i] = c
                colors_code[v % "dark"] = c
                if v % self.index in colors_code:
                    colors_code[v[:-3]] = colors_code[v % self.index]
                    colors_code[v % "light"] = colors_code[v % (self.index - self.step)]
                else:
                    colors_code[v[:-3]] = colors_code[v % int(len(colors) / 2)]
                    colors_code[v % "light"] = colors_code[v % (int(len(colors) / 2) - self.step)]
        return colors_code


class ThemeCustom(Theme):
    _charts, _colors, _greys = [], [], []
    _warning, _danger, _success = set(), set(), set()


class ThemeDefault(Theme):
    name = "default"
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
    _colors = [
        '#f4f9fc', '#cfd8dc', '#b0bec5', '#90a4ae', '#78909c', '#607d8b', '#546e7a', '#455a64', '#37474f', '#263238']
    _warning, _danger, _success = ['#FFF3CD', '#e2ac00'], ["#F8D7DA", "#C00000"], ['#e8f2ef', '#5DDEAD']
