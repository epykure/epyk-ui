from epyk.core.Page import Report
from epyk.tests import test_statics

rptObj = Report()

sub_tree = [
    {"label": 'sub test 1', 'dblclick': 'alert("General")', 'items': [
        {"label": 'sub child 2', 'dblclick': 'alert("General !!!")', 'color': 'green'},
        {"label": 'sub child 3', 'color': 'green'},
        {"label": 'sub child 4', 'color': 'green'},
    ]}
]

data = [{"label": 'test', 'items': [
        {"label": 'child 1', 'color': 'red', 'selects': ["A", "B", "C"], 'event': '%s' % rptObj.js.fncs.anonymous('if(data.val == "A") {return {"new": %s}} else { return []}' % sub_tree)},
        {"label": 'child 2', 'color': 'red'},
    ]},
        {"label": 'test2'}
        ]

t = rptObj.ui.tree(data)
t.removeNode()

b = rptObj.ui.button("test")

b.click(t.jsGenerate(sub_tree, jsStyles=t.builder_options({"reset": False}), isPyData=True))

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS, target="_self")
