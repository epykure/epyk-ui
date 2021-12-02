import json

from epyk.core import Page as Rpt
from epyk.core.data import events
from epyk.core.data import configs
from epyk.core.data import datamap as js_datamap
from epyk.core.data import components as inputs
from epyk.core.html import Defaults as settings

from epyk.core.css import themes
from epyk.core.css import Defaults as settings_css
from epyk.core.css import Colors as colors
from epyk.core.css.themes import palettes
from epyk.core.css.styles.attributes import CssInline

# Add JavaScript shortcuts
from epyk.core.js import std as js_std
from epyk.core.js import expr as js_expr
from epyk.core.js import libs as js_libs
from epyk.core.js.JsUtils import jsWrap as js_callback

from epyk.core.js.Imports import Package as package
from epyk.core.js.Imports import PACKAGE_STATUS, JS_IMPORTS, CSS_IMPORTS

from epyk.web import jupyter

Page = Rpt.Report

LOG_SERVICE = None


def rename_css_cls(mappings):
  """
  Description:
  ------------
  Change the name of the CSS classes in the framework.
  This function need to be used before the creation of any component in the page.

  This will not change the content. it will only rename them.
  To remove a CSS classe or to change it in a component type have a look at components_skin

  Attributes:
  ----------
  :param mappings: Dictionary. The CSS class names to be renamed.
  """
  from epyk.core.css import Classes

  Classes.OVERRIDES = mappings


def packages_black_list(pkgs_alias, raise_exception=True):
  """
  All packages in this list will be considered as forbidden.
  The other packages will be authorised.

  Attributes:
  ----------
  :param pkgs_alias: List<String>. A list of packages reference.
  :param raise_exception: Boolean. Optional. The kind of error triggered.
  """
  global PACKAGE_STATUS

  for pkg in pkgs_alias:
    if raise_exception:
      PACKAGE_STATUS[pkg] = {"allowed": False}
    else:
      PACKAGE_STATUS[pkg] = {"allowed": True, "info": "Package in Black list"}


def packages_white_list(pkgs_alias, raise_exception=True):
  """
  Description:
  -----------
  All packages not in this lists will be considered as forbidden.

  Attributes:
  ----------
  :param pkgs_alias: List<String>. A list of packages reference.
  :param raise_exception: Boolean. Optional. The kind of error triggered.
  """
  global PACKAGE_STATUS

  for js_pkg in JS_IMPORTS:
    if js_pkg in pkgs_alias:
      PACKAGE_STATUS[js_pkg] = {"allowed": True}
    else:
      if raise_exception:
        PACKAGE_STATUS[js_pkg] = {"allowed": False}
      else:
        PACKAGE_STATUS[js_pkg] = {"allowed": True, "info": "Missing from white list"}
  for css_pkg in CSS_IMPORTS:
    if css_pkg in pkgs_alias:
      PACKAGE_STATUS[css_pkg] = {"allowed": True}
    else:
      if raise_exception:
        PACKAGE_STATUS[css_pkg] = {"allowed": False}
      else:
        PACKAGE_STATUS[css_pkg] = {"allowed": True, "info": "Missing from white list"}


#
# def from_ipynb(filename, page=None):
#   page = page or Page()
#   page.imports.extend(["requirejs", 'bootstrap', 'jquery', 'moment', 'jqueryui', 'mathjax'])
#   # Add Jupyter internal packages
#   with open(filename) as fp:
#     nb = json.load(fp)
#     for cell in nb["cells"]:
#       if cell['cell_type'] == "code":
#         for output in cell["outputs"]:
#           if output['output_type'] == "stream":
#             editor = page.ui.codes.markdown(output["text"], height="auto")
#           elif output['output_type'] == "execute_result":
#             div = page.ui.div()
#             page.body.onReady([
#               page.js.get("/frg", {"source": cell["source"]}).onSuccess([
#                 "var htmlObj = $(data)",
#                 "console.log(htmlObj)",
#                 "var scripts = []",
#                 "htmlObj.each(function(){if (this.nodeName == 'SCRIPT'){scripts.push(this.text)} })",
#                 "var script = document.createElement('script')",
#                 "script.type = 'text/javascript'",
#                 "var inlineScript = document.createTextNode(scripts.join(';'));",
#                 "script.appendChild(inlineScript); ",
#                 "%s.appendChild(script)" % div.dom.varName,
#                 div.dom.innerHTML(events.data),
#               ]),
#             ])
#
#       elif cell['cell_type'] == "markdown":
#         if isinstance(cell["source"], list):
#           cell["source"] = "".join(cell["source"])
#         editor = page.ui.text(cell["source"], height="auto", options={"markdown": True})
#         editor.style.css.inline()
#         editor.style.css.margin_h = "5%"
#         div = page.ui.div(editor)
#         div.style.css.padding = "auto"
#         div.style.css.margin_h = 20
#         div.style.css.margin_v = 20
#       else:
#         if isinstance(cell["source"], list):
#           cell["source"] = "".join(cell["source"])
#         editor = page.ui.codes.python(cell["source"], height="auto")
#         editor.style.css.inline()
#         editor.style.css.margin_h = "5%"
#         div = page.ui.div(editor)
#         div.style.css.padding = "auto"
#         div.style.css.margin_h = 20
#         div.style.css.margin_v = 20
#   return page
