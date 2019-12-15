"""
Module in charge of the testing of the trees
"""


from epyk.core.Page import Report
from epyk.tests import test_statics

# Create a basic report object
rptObj = Report()

rptObj.ui.text("this is a test")
rptObj.ui.texts.label("this is a test", color="red").css({"float": 'none'})
rptObj.ui.texts.span("Test").css({"border": "1px solid black"})
rptObj.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")
rptObj.ui.texts.formula("$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$", helper="This is a formula")
rptObj.ui.texts.paragraph("This is a paragraph", helper="Paragraph helper")
rptObj.ui.texts.up_down({'previous': 240885, 'value': 240985})
rptObj.ui.texts.number(289839898, label="test", helper="Ok", icon="fas fa-align-center")
rptObj.ui.title("Test")
rptObj.ui.title("Test", level=2)
rptObj.ui.texts.fieldset("legend")
rptObj.ui.layouts.hr(3)
rptObj.ui.images.badge("This is a badge", background_color="red", color="white")
rptObj.ui.layouts.new_line()
rptObj.ui.images.icon("fab fa-angellist")


#rptObj.ui.texts.blockquote("This is a code")
#rptObj.ui.texts.preformat("This is a pre formatted text")
#rptObj.ui.texts.code("This is a code")

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_text"))
