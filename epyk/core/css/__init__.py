from . import themes
from .styles import effects
from . import styles, Icons
from . import Defaults as Defaults_css

from typing import List
from pathlib import Path
import re
from typing import Optional, Dict


def css_files_loader(
        file_path: Optional[List[str]],
        selector: str = None,
        style_vars: Optional[Dict[str, str]] = None,
        minify: bool = True
) -> str:
    """
    Get the CSS content from CSS component files.

    :param file_path: The list of CSS styles
    :param selector: Optional. The container selector definition
    :param style_vars: Optional. The value to replace in the CSS template file (SCSS file)
    :param minify: Optional. Flag to minify or not the CSS content
    """
    style_vars = style_vars or {}
    regex = re.compile(r"([A-Za-z0-9\.,\-\=\"'\[\]]*) {([#A-Za-z0-9\ \:\;\-]*) }")
    css_formatted = []
    if file_path is not None:
        for css_file in file_path:
            if Path(css_file).exists():
                if css_file.endswith(".css"):
                    css_formatted.append("/* CSS From file %s */" % css_file)
                    with open(css_file) as fp:
                        css_data = " ".join([line.strip() for line in fp])
                        for k, v in style_vars.items():
                            css_data = css_data.replace("$%s" % k, v)
                        for m in regex.findall(css_data):
                            if selector is not None:
                                css_formatted.append("div[name=%s] %s { %s }" % (selector, m[0], m[1]))
                            else:
                                css_formatted.append("%s { %s }" % (m[0], m[1]))
                else:
                    raise ValueError("CSS file format not supported only (.css and .scss)" % css_file)

            else:
                for k, v in style_vars.items():
                    css_file = css_file.replace("$%s" % k, v)
                for m in regex.findall(css_data):
                    if selector is not None:
                        css_formatted.append("div[name=%s] > %s { %s }" % (selector, m[0], m[1]))
                    else:
                        css_formatted.append("%s { %s }" % (m[0], m[1]))
    if minify:
        return " ".join(css_formatted)

    return "\n".join(css_formatted)


def scss_colors(out_file_path: str = "COLORS.SCSS", theme: themes.Theme.Theme = None):
    """
    Create a SCSS template file for the definition of colors theme.
    It will generate a schema based on the default theme definition.

    Usages::

        import epyk as ek
        ek.helpers.scss_colors()

    :param out_file_path: Optional. The full scss file path
    :param theme: Optional. The theme to export
    """
    with open(out_file_path, "w") as fp:
        fp.write("/* Auto generated SCSS files for colors definition */ \n")
        if theme is None:
            theme = themes.Theme.ThemeDefault()
        mapped_groups = {"theme": "colors", "grey": "greys"}
        for group in theme.groups:
            fp.write("\n/* Colors codes for %s */ \n" % group)
            for i, color in enumerate(getattr(theme, mapped_groups.get(group, group))[::-1]):
                if i == 0:
                    fp.write("$color-%s-50: %s;\n" % (group, color))
                else:
                    fp.write("$color-%s-%s: %s;\n" % (group, i * 100, color))

        fp.write("\n\n/* Colors codes for charts */ \n")
        if not theme.chart_categories:
            fp.write("/*$charts: (green, blue, purple, yellow, orange, red, brown) ; */ \n")
            fp.write("$charts: default ; \n\n")
            for i, color in enumerate(theme.charts):
                if i == 0:
                    fp.write("$chart-default-50: %s;\n" % color)
                else:
                    fp.write("$chart-default-%s: %s;\n" % (i * 100, color))
        else:
            if len(theme.chart_categories) > 1:
                fp.write("/*$charts: (%s) ; */ \n" % ", ".join(theme.chart_categories))
            else:
                fp.write("/*$charts: (green, blue, purple, yellow, orange, red, brown) ; */ \n")
                fp.write("$charts: %s ; \n\n" % theme.chart_categories[0])
            for group in theme.chart_categories:
                for i, color in enumerate(theme.charts):
                    if i == 0:
                        fp.write("$chart-%s-50: %s;\n" % (group, color))
                    else:
                        fp.write("$chart-%s-%s: %s;\n" % (group, i * 100, color))


def scss_icons(out_file_path: str = "ICONS.SCSS"):
    """
    Create a SCSS template file for the definition of Icons.
    It will generate a schema based on the default definition using font-awesome icons.

    Usages::

        import epyk as ek
        ek.helpers.scss_icons()

    :param out_file_path: Optional. The full scss file path
    """
    with open(out_file_path, "w") as fp:
        fp.write("/* Auto generated SCSS files for icons definition */ \n\n")
        for k, v in Icons._ICON_MAPPINGS["font-awesome"].items():
            fp.write("$%s: %s;\n" % (k, v))
