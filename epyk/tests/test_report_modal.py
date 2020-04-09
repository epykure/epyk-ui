"""

"""

from epyk.core.Page import Report
from epyk.tests import data_urls
from epyk.core.css.themes import ThemeBlue
from epyk.core.css.themes import ThemeDark
from epyk.core.css.themes import ThemeRed
from epyk.core.css.themes import ThemeGreen
rptObj = Report()
# rptObj.ui.layouts.

privacy_title = rptObj.ui.texts.title('A privacy reminder from Google', 2)
p1 = rptObj.ui.texts.paragraph('''Scroll down and click “%s” when you’re ready to continue to Maps, or explore other options on this page.''' % rptObj.ui.tags.strong('''I agree''', options={'managed': False}))
stroke = rptObj.ui.layouts.hr()
p2 = rptObj.ui.texts.paragraph('''To be consistent with data protection laws, we’re asking you to take a moment to review key points of Google’s Privacy Policy. This isn’t about a change we’ve made — it’s just a chance to review some key points.''')
data_protect = rptObj.ui.texts.title('''Data we process when you use Google''')
l1 = rptObj.ui.texts.paragraph('''When you search for a restaurant on Google Maps or watch a video on YouTube, for example, we process information about that activity - including information like the video you watched, device IDs, IP addresses, cookie data, and location.''')
l2 = rptObj.ui.texts.paragraph('''We also process the kinds of information described above when you use apps or sites that use Google services like ads, Analytics, and the YouTube video player.''')
list_1 = rptObj.ui.lists.list([l1, l2])
process = rptObj.ui.texts.title('''Why we process it''')
p3 = rptObj.ui.texts.paragraph('''We process this data for the purposes described in our %s, including to:''' % rptObj.ui.tags.strong('policy', options={'managed': False}))
l3 = rptObj.ui.texts.paragraph('''Help our services deliver more useful, customized content such as more relevant search results;''')
l4 = rptObj.ui.texts.paragraph('''Improve the quality of our services and develop new ones;''')
l5 = rptObj.ui.texts.paragraph('''Deliver ads based on your interests, including things like searches you've done or videos you've watched on YouTube;''')
l6 = rptObj.ui.texts.paragraph('''Improve security by protecting against fraud and abuse; and''')
l7 = rptObj.ui.texts.paragraph('''Conduct analytics and measurement to understand how our services are used. We also have partners that measure how our services are used. Learn more about these specific advertising and measurement partners.''')
list_2 = rptObj.ui.lists.list([l3, l4, l5, l6, l7])
combining = rptObj.ui.texts.title('''Combining data''')
p4 = rptObj.ui.texts.paragraph('''We also combine data among our services and across your devices for these purposes. For example, we use data from trillions of search queries to build spell-correction models that we use across all of our services, and we combine data to alert you and other users to potential security risks.''')
control = rptObj.ui.texts.title('''Privacy Controls''')
p5 = rptObj.ui.texts.paragraph('''There are many privacy controls you can use, even when you're signed out, to get the Google experience you want.''')
disc = rptObj.ui.modal.disclaimer([privacy_title, p1, stroke, p2, data_protect,
                            list_1, process, p3, list_2, combining, p4, control, p5])
button_show = rptObj.ui.buttons.button('Disclaimer')
button_show.click(disc.show())

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
# button = rptObj.ui.buttons.button('Contact Sales')
# imp = rptObj.ui.buttons.important('Get Started for Free')
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

# div = rptObj.ui.div("toto")
# div.style.css.background_color = 'yellow'
# div.style.css.height = '50px'

# div.style.css_class.media({div: {"background-color": "red"}}, 'only', 'screen', {"and": [{'max-width': '600px'}]})
# print(div.style.css_class.get_ref())

# data_rest = rptObj.py.requests.csv(data_urls.COVID_ECDC_URL)
# print(data_rest)
# print(time.time() - start)


# rptObj.ui.texts.para

print(rptObj.outs.html_file(name='test'))

