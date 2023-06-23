from . import themes
from epyk.core.css.styles import effects
from . import styles

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
