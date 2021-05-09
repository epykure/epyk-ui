import json

from epyk.core import Page as Rpt
from epyk.core.data import events
from epyk.core.data import components as inputs
from epyk.core.html import Defaults as settings

from epyk.core.css.styles.attributes import CssInline

# Add JavaScript shortcuts
from epyk.core.js import std
from epyk.core.js import expr
from epyk.core.js.JsUtils import jsWrap

Page = Rpt.Report

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
