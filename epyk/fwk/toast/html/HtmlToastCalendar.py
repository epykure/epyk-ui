
from epyk.core.html import Html
from epyk.fwk.toast.options import OptToastCalendar
from epyk.fwk.toast.js import JsToastCalendar


class Calendar(Html.Html):
  name = 'ToastCalendar'
  requirements = ('tui-calendar', )
  _option_cls = OptToastCalendar.OptionCalendar

  def __init__(self, report, width, height, html_code, options, profile):
    self.height = height[0]
    super(Calendar, self).__init__(
      report, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.options.height = height[0]

  @property
  def var(self):
    """
    Description:
    -----------
    Return the calendar javaScript object reference after the builder.
    """
    return "window['%s']" % self.htmlCode

  @property
  def options(self):
    """
    Description:
    -----------
    The Toast UI Calendar options.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/tutorial-example01-monthly

    :rtype: OptToastCalendar.OptionCalendar
    """
    return super().options

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript module of the items in the menu.

    Related Pages:

      https://nhn.github.io/tui.calendar/latest/Calendar

    :rtype: JsToastCalendar.Calendar
    """
    if self._js is None:
      self._js = JsToastCalendar.Calendar(self, varName=self.var, report=self.page)
    return self._js

  _js__builder__ = '''window[htmlObj.id] = new tui.Calendar(htmlObj, options)'''

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '''<div %(attrs)s></div>''' % {"attrs": self.get_attrs(pyClassNames=self.style.get_classes())}
