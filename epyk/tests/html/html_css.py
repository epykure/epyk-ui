
from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()

# Create a text component on the page
text = rptObj.ui.text("test")

# Change the CSS Style
# Add the no_border style (ctrl + q) for the style documentation
text.style.defined.div.no_border()

text.style.defined.div.no_border()
