from . import HtmlButton
from . import HtmlContainer
from . import HtmlEvent
from . import HtmlLinks
from . import HtmlImage
from . import HtmlInput
from . import HtmlList
from . import HtmlMenu
from . import HtmlOthers
from . import HtmlRadio
from . import HtmlSelect
from . import HtmlText
from . import HtmlTextComp
from . import HtmlTextEditor
from . import HtmlMedia
from . import Html
from . import HtmlPopup
from . import HtmlNetwork
from . import HtmlDates
from . import templates
from . import HtmlTrees
from . import HtmlTags
from . import HtmlStepper
from . import HtmlDrawer
from . import Header

from . import tables
from . import graph
from . import Defaults as Defaults_html
from ...conf.global_settings import DEBUG

import re
from pathlib import Path
from typing import Optional
import logging


def html_formatter(
        html_content: str,
        values: Optional[dict] = None,
        new_var_format: Optional[str] = None,
        ref_expr: Optional[str] = None,
        directives: Optional[dict] = None,
        verbose: bool = None
) -> dict:
    """Format a string to provide a valid HTML string for a target web framework.

    :param html_content: HTML content as a string
    :param values: Optional. Values to be replaced by the Python
    :param new_var_format: Optional. Variable format for the target web framework (default {{ }})
    :param ref_expr: Optional. Special string for the component DOM identifier
    :param directives: Optional. The directive expression for the framework
    :param verbose: Show extra log messages
    """
    if values is not None and new_var_format is not None:
        raise ValueError("Both values and var_format cannot be defined")

    js_variables, inputs, css = [], [], []
    regex_tmpl = re.compile(r"{{([a-zA-Z_\.\ 0-9]*)}}")
    if directives:
        for ref, content in directives.items():
            directive_def = "[%s]" % ref
            if directive_def not in html_content:
                if verbose or (verbose is None and DEBUG):
                    logging.warning("-- Directive [%s] missing, in template\n %s" % (ref, html_content))
            html_content = html_content.replace(directive_def, content.strip())
            if ref in ["class", "style"]:
                # special template directives
                # slice to remove the quotes
                if content:
                    css.append('%s:string = ""' % content.split("=")[-1].strip()[1:-1])
    for m in regex_tmpl.findall(html_content):
        var_name = m.strip()
        if var_name == "id" and ref_expr is not None:
            for r in regex_tmpl.findall(ref_expr):
                var_name = r.strip()
                js_variables.append(var_name)
                inputs.append(var_name)
                if new_var_format is not None:
                    ref_expr = ref_expr.replace("{{%s}}" % r, new_var_format % var_name)
                elif values is not None:
                    ref_expr = ref_expr.replace("{{%s}}" % r, str(values[m.strip()]))
                else:
                    ref_expr = ref_expr.replace("{{%s}}" % r, var_name)
            html_content = html_content.replace("{{%s}}" % m, ref_expr)
        elif new_var_format is not None:
            js_variables.append(var_name)
            inputs.append(var_name)
            html_content = html_content.replace("{{%s}}" % m, new_var_format % var_name)
        elif values is not None:
            js_variables.append(var_name)
            inputs.append(var_name)
            html_content = html_content.replace("{{%s}}" % m, str(values[m.strip()]))
        else:
            js_variables.append(var_name)
            inputs.append(var_name)
    return {"vars": set(js_variables), "template": html_content.strip(), "inputs": set(inputs), "css": css}


def html_template_loader(
        file_path: str,
        values: Optional[dict] = None,
        new_var_format: Optional[str] = None,
        ref_expr: Optional[str] = None,
        directives: Optional[dict] = None
) -> dict:
    """
    Python loader for an HTML template.

    :param file_path: HTML file path
    :param values: Optional. Values to be replaced by the Python
    :param new_var_format: Optional. Variable format for the target web framework (default {{ }})
    :param ref_expr: Optional. Special string for the component DOM identifier
    :param directives: Optional. The directive expression for the framework
    """
    if values is not None and new_var_format is not None:
        raise ValueError("Both values and var_format cannot be defined")

    html_path = Path(file_path)
    if html_path.exists():
        with open(html_path) as hf:
            return html_formatter(
                hf.read(), values=values, new_var_format=new_var_format, ref_expr=ref_expr, directives=directives)
