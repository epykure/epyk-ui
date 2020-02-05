"""
Module in charge of the testing of the trees
"""

from epyk.core.Page import Report
from epyk.tests import test_statics


from epyk.core.html import Defaults
from epyk.core.css.themes import ThemeDark

Defaults.TEXTS_SPAN_WIDTH = None

# Create a basic report object
rptObj = Report()
rptObj.theme = ThemeDark.Dark()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

data = [{"label": 'test', 'items': [
  {"label": 'child 1', 'color': 'red'},
  {"label": 'child 2', 'color': 'green', 'items': [
      {"label": 'sub child 1', 'color': 'red'},
  ]},
  {"label": 'child 3', 'color': 'red'},

]}]
# t1 = rptObj.ui.trees.inputs(data)
# t2 = rptObj.ui.trees.tree(data)
#
# rptObj.ui.grid([t1, t2])

#t = rptObj.ui.lists.dropdown(data)
#t.options.expanded = False
#t.level(1)

#
# table = rptObj.ui.layouts.table([
#   ["A", "B", "C"],
#   ["1", "2", "C3"],
#   ["A4", "5", "4C"],
# ], width=(50, 'px'))
#
# #for c in table.col(i=1):
# #  c.add_title(c.val)
#   #v[i] = self._report.ui.texts.span(v[i])
#   #v[i].inReport = False
# #  c.css({"background": 'red'})
#
# table.style.clear()
#
# #rptObj.ui.sliders.slider(40)
# d = rptObj.ui.fields.textarea()
# i = rptObj.ui.inputs.search(extensible=True)
# i.enter(
#   #rptObj.js.alert(i.dom.content),
#   rptObj.js.alert(d.dom.content),
# )
#
# i.attr['autocomplete'] = 'false'
#
s = rptObj.ui.fields.select(["A"], label="test")
s.input.attr["data-live-search"] = "true"


rptObj.js.addOnReady([
  s.input.dom.ajaxSelectPicker({"ajax": {
    #"beforeSend": "function(){console.log(%s)}()" % s.input.dom.content,
    #"url": 'function(element){return "https://jsonplaceholder.typicode.com/posts/"}(this)' % s.input.dom.search,
    'url': 'function(){return "https://jsonplaceholder.typicode.com/posts/" + this.plugin.query}',
    "type": "get", "dataType": "json", "data": "",
    #"data": {"q": "{{{q}}}"}
    },
        'preserveSelected': False, 'preprocessData':
        'function(data) {return [{text: "C", value: "C"}, {text: "D", value: "D"}]}', "locale": {
    "emptyTitle": "Select and Begin Typing"}})
])

rptObj.ui.button("test").click([
  rptObj.js.window.toggleInterval(rptObj.js.console.log('ok'), 'test', 400),
])


s = rptObj.ui.select(["A", "B", "C"], label="label", selected="C", multiple=True,
                      options={"title": "ttle", 'showTick': True, 'maxOptions': 2})
s.selected = "B"
s.change(c.write(s.dom.content))

#
# #rptObj.ui.charts.skillbars()
# rptObj.ui.layouts.hr(3)
#
# l = rptObj.ui.list(range(10))
# #l.set_items(in_span=True)
#
# l2 = rptObj.ui.list(range(10))
#
# l3 = rptObj.ui.list(range(10)).css({"color": "red"})
# #rptObj.ui.context_menu(["context"])
# #l3[1].add_menu()
#
# l2.add_item(l3)[-1].val.css({"margin": "2px 10px"})
# #l2[-1].set_html_content(rptObj.ui.texts.span(l2[-1].val))
# l2[-1].add_label("test")
# l2[-1].add_icon("fas fa-folder")
#
#
# l2[-1].label.tooltip("test")
# l2[-1].icon.click([
#   l2[-1].val.dom.toggle(),
#   l2[-1].icon.dom.switchClass("fa-folder", "fa-folder-open")
# ])
#
# l2.add_item(14)
#
# l.add_item(l2)[-1].val.css({"margin": "0px 10px"})
#
# #l2.set_items_format(icon="fas fa-folder")
# #l3.set_items_format(icon="fas fa-archive")
# #l.set_items_format(icon="fas fa-archive")
#
#
# l = rptObj.ui.lists.groups(["AWW", "B"])
# l.add_list(["D", "E"], category="Test")
# for i in l:
#   for u in i:
#     u.no_decoration
#
#
# data = [{"label": "python", "value": False}, {"label": "Java", "value": 5}]
# checks = rptObj.ui.lists.checklist(data)
#
# rptObj.ui.button("Test").click([
#   checks.items[1].dom.toggle()
# ])
#
#
# bs = rptObj.ui.lists.buttons(["Button", "Button 2", "Button 3"])
# bs = rptObj.ui.buttons.buttons(["Button", "Button 2", "Button 3"])
# print(bs[2].content)
# bs[2].click([
#   rptObj.js.alert(bs[2].dom.content)
# ])
#
# rptObj.ui.lists.badges([{'label': 'Python', 'value': 12}, {'label': 'R', 'value': 3}])
#

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_list"))
