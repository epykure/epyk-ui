from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

# Add a text component (use markup in the text + some external HTML symbols
text = rptObj.ui.texts.text("**Test** text %s " % rptObj.symbols.SQUARE_ROOT).css({"color": 'red'})
# Add a number component
rptObj.ui.texts.number(188448228, label="test")
# Add a table to the page
title = rptObj.ui.texts.title("This is a *title*", options={"markdown": True})#.css({"color": 'green'})
# Add a predefined CSS class
title.style.commons.not_selectable()
title.style.div.mouse_hover_border_bottom().mouse_pointer()

# Add a preformatted text with a markup code with an HTML entity
rptObj.ui.texts.preformat("This is a __preformatted__ text %s" % rptObj.entities.EURO)

#
rptObj.ui.texts.text("This is a text with a max lenght")
rptObj.ui.texts.code("This is a code block")

# Add a bootstrap highlight text component
rptObj.ui.texts.highlights("This is a news", title="Important news")

# Add a context menu to the title
menu = rptObj.ui.context_menu([{"text": 'text', 'event': 'alert("ok")'}])
title.attach_menu(menu)

# Add a button with an alert when clicked
button = rptObj.ui.button("click me")
button.click([rptObj.js.window.alert("ok"), text.jsGenerate("Youpi", isPyData=True)])

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)