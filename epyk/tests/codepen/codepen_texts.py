from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

# Add a text component
text = rptObj.ui.texts.text("Test text").css({"color": 'red'})
# Add a number component
rptObj.ui.texts.number(188448228, label="test")
# Add a table to the page
title = rptObj.ui.texts.title("title").css({"color": 'green'})
# Add a predefined class
title.style.cssCls("CssNotSelect")

# Add a bootstrap highlight text component
rptObj.ui.texts.highlights("This is a news", title="Important news")

# Add a context menu to the title
menu = rptObj.ui.context_menu([{"text": 'text', 'event': 'alert("ok")'}])
title.attach_menu(menu)

# Add a button with an alert when clicked
button = rptObj.ui.button("click me")
button.click([rptObj.js.window.alert("ok"), text.jsGenerate("Youpi", isPyData=True)])

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)