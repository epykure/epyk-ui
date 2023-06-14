from epyk.core.css.themes import Theme
from epyk.core.css import Icons


def scss_colors(out_file_path: str = "COLORS.SCSS", theme: Theme.Theme = None):
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
            theme = Theme.ThemeDefault()
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
