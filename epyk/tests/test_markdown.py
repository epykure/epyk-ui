from epyk.core.py import PyMarkdown
from epyk.core.js import Js
from epyk.core import Ares


md = PyMarkdown.MarkDown(report=Ares.Report()).parse_module(Js)
print(md)



report = Ares.Report()

PyMarkdown.MarkDown.MarkDown(report=report)
#MarkDown.parse_restructured_text(MarkDown.parse_restructured_text.__doc__)
