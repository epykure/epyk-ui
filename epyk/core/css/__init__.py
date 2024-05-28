from . import themes
from .styles import effects
from . import styles, Icons
from . import Defaults as Defaults_css
from ...conf import global_settings

import logging
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
    """Get the CSS content from CSS component files.

    :param file_path: The list of CSS styles
    :param selector: Optional. The container selector definition
    :param style_vars: Optional. The value to replace in the CSS template file (SCSS file)
    :param minify: Optional. Flag to minify or not the CSS content
    """
    style_vars = style_vars or {}
    regex = re.compile(Defaults_css.REG_EXP_SECTOR)
    css_formatted = []
    if file_path is not None:
        for css_file in file_path:
            path_css_file = Path(css_file)
            if global_settings.NATIVE_CSS_PATH is not None:
                over_path = Path(global_settings.NATIVE_CSS_PATH) / path_css_file.name
                if over_path.exists():
                    logging.debug("NATIVE | CSS | file %s used from %s" % (
                        path_css_file.name, global_settings.NATIVE_CSS_PATH))
                    css_file = str(over_path)
                    path_css_file = over_path
            css_file = str(css_file)
            if path_css_file.exists():
                if css_file.endswith(".css"):
                    css_formatted.append("/* CSS From file %s */" % css_file)
                    with open(css_file) as fp:
                        css_data = " ".join([line.strip() for line in fp])
                        css_data = css_data.replace(":host", "")
                        for k in sorted(style_vars, key=lambda k: len(k), reverse=True):
                            # Important to replace by starting with the longest string to avoid issues
                            css_data = css_data.replace("$%s" % k, style_vars[k])
                        if "$" in css_data:
                            logging.warning("CSS | Loader | Issue when processing file: %s" % css_file)
                        for m in regex.findall(css_data):
                            if selector is not None:
                                container_ref = "div[name=%s]" % selector
                                if container_ref in m[0]:
                                    css_formatted.append("%s { %s }" % (m[0], m[1]))
                                else:
                                    css_formatted.append("%s %s { %s }" % (container_ref, m[0], m[1]))
                            else:
                                css_formatted.append("%s { %s }" % (m[0], m[1]))
                else:
                    raise ValueError("CSS file format not supported %s - only (.css and .scss)" % css_file)

            else:
                for k, v in style_vars.items():
                    css_file = css_file.replace("$%s" % k, v).replace(":host", "")
                for m in regex.findall(css_file):
                    if selector is not None:
                        css_formatted.append("div[name=%s] > %s { %s }" % (selector, m[0], m[1]))
                    else:
                        css_formatted.append("%s { %s }" % (m[0], m[1]))
    if minify:
        return " ".join(css_formatted)

    return "\n".join(css_formatted)


def export_scss_files(out_path: str = None):
    """This will export all SCSS files namely the colors and the Icons theme

    :param out_path: The export path. If None it will take the current directory
    """
    out_path = out_path or global_settings.THEME_SASS_PATH or Path.cwd()
    out_theme_path = Path(out_path, "%s.SCSS" % Defaults_css.THEME.upper())
    scss_colors(file_path=str(out_theme_path), theme=themes.get_theme(), override=True)

    out_icons_path = Path(out_path, "%s.SCSS" % Defaults_css.ICON_FAMILY.upper())
    scss_icons(file_path=str(out_icons_path), family=Defaults_css.ICON_FAMILY, override=True)


def scss_colors(file_path: str = "COLORS.SCSS", theme: themes.Theme.Theme = None, override: bool = False):
    """Create a SCSS template file for the definition of colors theme.
    It will generate a schema based on the default theme definition.

    Usages::

        import epyk as ek
        ek.helpers.scss_colors()

    :param file_path: Optional. The full scss file path
    :param theme: Optional. The theme to export
    :param override: Optional. Force the out_file to be updated
    """
    out_path = Path(file_path)
    if not out_path.exists() or override:
        with open(out_path, "w") as fp:
            fp.write("/* Auto generated SCSS files for colors definition */ \n")
            if theme is None:
                theme = themes.get_theme()
            mapped_groups = {"theme": "colors", "grey": "greys"}
            for group in theme.groups:
                fp.write("\n/* Colors codes for %s */ \n" % group)
                cat = mapped_groups.get(group, group)
                for i, color in enumerate(theme[cat][::-1]):
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
    else:
        dyn_theme = themes.Theme.Theme()
        dyn_theme.from_sass(file_path)
        themes.add_themes([dyn_theme])
        themes.set_theme(dyn_theme.name)


def scss_icons(file_path: str = "ICONS.SCSS", family: str = None, override: bool = False):
    """Create a SCSS template file for the definition of Icons.
    It will generate a schema based on the default definition using font-awesome icons.

    Usages::

        import epyk as ek
        ek.helpers.scss_icons()

    :param file_path: Optional. In / Out full scss file path
    :param family: Optional. Icon's family
    :param override: Optional. Force the file_path to be updated
    """
    fpath = Path(file_path)
    if fpath.exists() and not override:
        family = family or fpath.stem.lower()
        with open(file_path) as fp:
            Defaults_css.ICON_MAPPINGS[family] = {}
            for line in fp:
                l = line.strip()
                match = re.search("^\$(.*):(.*);", l)
                if match:
                    Defaults_css.ICON_MAPPINGS[family][match.group(1).strip()] = match.group(2).strip()
                    Defaults_css.ICON_FAMILY = family
    else:
        family = family or Defaults_css.ICON_FAMILY
        with open(file_path, "w") as fp:
            fp.write("/* Auto generated SCSS files for icons definition */ \n\n")
            for k, v in Defaults_css.ICON_MAPPINGS[family].items():
                fp.write("$%s: %s;\n" % (k, v))


def inline_to_dict(value: str, no_hyphen: bool = True) -> Dict[str, str]:
    """Convert an inline CSS String to a dictionary.

    :param value: Inline CSS content
    :param no_hyphen: Optional. Flag to remove the - from the CSS keys
    """
    results = {}
    for props in value.split(";"):
        if props.strip():
            k, val = props.split(":", 1)
            if no_hyphen:
                if "-" in k:
                    ks = k.split("-")
                    cks = [v.capitalize() for v in ks[1:]]
                    k = "".join([ks[0]] + cks)
            results[k.strip()] = val.strip()
    return results
