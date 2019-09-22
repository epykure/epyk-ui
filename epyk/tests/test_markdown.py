from epyk.core.py import PyMarkdown
from epyk.core.js import Js
from epyk.core import Page


md = PyMarkdown.MarkDown(report=Page.Report()).parse_module(Js)
print(md)



report = Page.Report()

PyMarkdown.MarkDown.MarkDown(report=report)
#MarkDown.parse_restructured_text(MarkDown.parse_restructured_text.__doc__)
