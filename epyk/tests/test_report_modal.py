"""

"""

from epyk.core.Page import Report
from epyk.tests import data_urls
from epyk.core.css.themes import ThemeBlue
from epyk.core.css.themes import ThemeDark
from epyk.core.css.themes import ThemeRed
from epyk.core.css.themes import ThemeGreen
rptObj = Report()

disc = '''This is not a production platform if you use this code in production
YOU NEED TO BE AWARE OF THE IT GOVERNANCE
Ciao bye'''
#########THEMES#########
# rptObj.theme = ThemeBlue.BlueGrey()
# rptObj.theme = ThemeBlue.Blue()
# rptObj.theme = ThemeBlue.LightBlue()
# rptObj.theme = ThemeRed.Red()
# rptObj.theme = ThemeDark.Dark()
# rptObj.theme = ThemeDark.Grey()
# rptObj.theme = ThemeGreen.Green()
# rptObj.theme = ThemeGreen.LightGreen()
# rptObj.theme = ThemeGreen.Teal()

# f = rptObj.ui.forms.inputs([
#   {"label": "name", "htmlCode": "input"},
#   {"label": "name 2", "htmlCode": "input2"},
# ], "http://127.0.0.1:5000", "POST")
# f + rptObj.ui.fields.today('test')
# print(rptObj.tags.bdi("test"))
# print(rptObj.entities.POUND)
# print(rptObj.symbols.ALMOST_EQUAL_TO)
# rptObj.ui.d
# d = rptObj.ui.fields.today('test')
# i = rptObj.ui.fields.input(placeholder='test2', label='test1')
# i.input.set_attrs(name='required')
# i.input.set_attrs({'name': 'input1'})
# i2 = rptObj.ui.fields.input('test3', label='test2')
# f + rptObj.ui.fields.today('test')
###########BUTTONS###########
button = rptObj.ui.buttons.button('Contact Sales')
imp = rptObj.ui.buttons.important('Get Started for Free')
# rptObj.ui.modal.forms([d, i, i2], "http://127.0.0.1:5000", "POST")
# rptObj.ui.modal.objects([d, i, i2], "POST", submit=False)
# disclaimer = rptObj.ui.texts.paragraph(disc)

# dis = rptObj.ui.modal.disclaimer(disc)
# button.click(rptObj.js.getElementById(dis.htmlId).css({'display': 'block'}))



#########FOOTER#########
nav = rptObj.ui.navigation.bar(title="test")
nav.add_text("This is a huge text that I don't know what to do with")
nav + button
nav + imp
# nav.add_text("Test text")
# nav + rptObj.ui.button("Click").css({"margin": '0 0 20px 5px'})
# rptObj.ui.navigation.banner("", "test", "google")
# footer = rptObj.ui.navigation.footer([button, imp])

# footer = rptObj.ui.navigation.complex_footer(4, {1: [button, imp], 2: [rptObj.ui.texts.text('toto')]})
# footer + button
# footer + imp
# footer + rptObj.ui.texts.paragraph('This is the end')
# import time
# start = time.time()
# data_rest = rptObj.py.requests.csv(data_urls.DATA_EARTHQUAKE)
# print(data_rest)
# print(time.time() - start)

print(rptObj.outs.html_file(name='test'))

