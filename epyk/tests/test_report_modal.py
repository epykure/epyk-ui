"""

"""

from epyk.core.Page import Report
from epyk.core.py import Pyk
from epyk.tests import data_urls
from epyk.core.css.themes import ThemeBlue
from epyk.core.css.themes import ThemeDark
from epyk.core.css.themes import ThemeRed
from epyk.core.css.themes import ThemeGreen
rptObj = Report()
# rptObj.ui.layouts.


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
# rptObj.ui.fields.today('test')
# rptObj.ui.images.icon()
###########BUTTONS###########
button = rptObj.ui.buttons.button('Contact Sales')
imp = rptObj.ui.buttons.important('Get Started for Free')
# rptObj.ui.modal.forms([d, i, i2], "http://127.0.0.1:5000", "POST")
# rptObj.ui.modal.objects([d, i, i2], "POST", submit=False)
# disclaimer = rptObj.ui.texts.paragraph(disc)

# dis = rptObj.ui.modal.disclaimer(disc)
# button.click(rptObj.js.getElementById(dis.htmlId).css({'display': 'block'}))
# print(rptObj.js.addOnReady(rptObj.js.window.events.addClickListener(rptObj.js.if_('event.target == %s' % button.htmlId, button.), subEvents=['event'])))

#########FOOTER#########
# nav = rptObj.ui.navigation.bar(title="test")
# nav.add_text("This is a huge text that I don't know what to do with")
# nav + button
# nav + imp
# nav.add_text("Test text")
# nav + rptObj.ui.button("Click").css({"margin": '0 0 20px 5px'})
# rptObj.ui.navigation.banner("", "test", "google")
# footer = rptObj.ui.navigation.footer([button, imp])
#
# footer = rptObj.ui.navigation.complex_footer(4, {1: [button, imp], 2: [rptObj.ui.texts.text('toto')]})
# footer + button
# footer + imp
# footer + rptObj.ui.texts.paragraph('This is the end')
# import time
# start = time.time()

div = rptObj.ui.div("toto")
div.style.css_class.media({'.topnav li': {"float": None, 'width': '100%'},
                           'topnav li line': {'stroke-width': 0},
                           'topnav li [name=label]': {'width': '100%!IMPORTANT'}}, 'only', 'screen', {"and": [{'max-width': '600px'}]})
# div.style.css.background_color = 'yellow'
# div.style.css.height = '50px'

# div.style.css_class.media({div: {"background-color": "red"}}, 'only', 'screen', {"and": [{'max-width': '2000px'}]})
# print(div.style.css_class.get_ref())
#
# rptObj.js.addOnLoad()

# data_rest = rptObj.py.requests.csv(data_urls.COVID_ECDC_URL)
# print(data_rest)
# print(time.time() - start)


# rptObj.ui.texts.para

print(rptObj.outs.html_file(name='test'))

