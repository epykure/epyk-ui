from epyk.core.html import Html
from epyk.fwk.toast.options import OptToastCalendar
from epyk.fwk.toast.options import OptToastTime
from epyk.fwk.toast.js import JsToastDates
from epyk.fwk.toast.css import GrpClsToastDates
from epyk.fwk.toast.dom import DomToastDatePicker


class DatePicker(Html.Html):
  name = 'ToastDate'
  requirements = ('tui-date-picker', )
  _option_cls = OptToastCalendar.OptionDate

  def __init__(self, report, width, height, html_code, options, profile):
    super(DatePicker, self).__init__(
      report, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.options.timePicker = False
    self.options.usageStatistics = False
    self.options.input.format = 'yyyy-MM-dd'
    self.options.input.element = '#%s_input' % self.htmlCode
    self.options.dates.current()

  _js__builder__ = '''window[htmlObj.id] = new tui.DatePicker('#'+ htmlObj.id, options); 
htmlObj.querySelector(".tui-datepicker").style["z-index"] = 500'''

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    :rtype: GrpClsToastDates.ClassDatePicker
    """
    if self._styleObj is None:
      self._styleObj = GrpClsToastDates.ClassDatePicker(self)
    return self._styleObj

  @property
  def dom(self):
    """
    Description:
    -----------
    The common DOM properties.

    :rtype: DomToastDatePicker.DomDate
    """
    if self._dom is None:
      self._dom = DomToastDatePicker.DomDate(self, report=self.page)
    return self._dom

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
    The component options.

    :rtype: OptToastCalendar.OptionDate
    """
    return super().options

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript module of the items in the menu.

    :rtype: JsToastDates.DatePicker
    """
    if self._js is None:
      self._js = JsToastDates.DatePicker(self, varName=self.var, report=self.page)
    return self._js

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '''
<div>
  <div class="tui-datepicker-input tui-datetime-input tui-has-focus">
      <input type="text" id="%s_input" aria-label="Date-Time">
      <span class="tui-ico-date"></span>
  </div>
  <div %s></div>
</div>''' % (self.htmlCode, self.get_attrs(pyClassNames=self.style.get_classes()))


class DateCalendar(Html.Html):
  name = 'ToastDateCalendar'
  requirements = ('tui-date-picker', )
  _option_cls = OptToastCalendar.OptionCalendar

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
    The component options.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

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

      https://nhn.github.io/tui.date-picker/latest/

    :rtype: JsToastDates.Calendar
    """
    if self._js is None:
      self._js = JsToastDates.Calendar(self, varName=self.var, report=self.page)
    return self._js


class DatePickerRange(Html.Html):
  name = 'ToastDateRange'
  requirements = ('tui-date-picker', )
  _option_cls = OptToastCalendar.OptionDateRange

  def __init__(self, report, vals, html_code=None, options=None, profile=None, css_attrs=None):
    super(DatePickerRange, self).__init__(report, vals, html_code, options, profile, css_attrs)
    self.options.startpicker.input = ""
    self.options.startpicker.container = ""
    self.options.startpicker.dates.today()
    self.options.endpicker.input = ""
    self.options.endpicker.container = ""
    self.options.endpicker.dates.today()

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
    The component options.

    :rtype: OptToastCalendar.OptionDateRange
    """
    return super().options

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript module of the items in the menu.

    :rtype: JsToastDates.DatePickerRange
    """
    if self._js is None:
      self._js = JsToastDates.DatePickerRange(self, varName=self.var, report=self.page)
    return self._js

  _js__builder__ = '''window[htmlObj.id] = new tui.DatePicker.createRangePicker(options)'''

  def __str__(self):
    return '''
<div class="tui-datepicker-input tui-datetime-input tui-has-focus">
    <input id="startpicker-input" type="text" aria-label="Date">
    <span class="tui-ico-date"></span>
    <div id="startpicker-container" style="margin-left: -1px;"></div>
</div>
<span>to</span>
<div class="tui-datepicker-input tui-datetime-input tui-has-focus">
    <input id="endpicker-input" type="text" aria-label="Date">
    <span class="tui-ico-date"></span>
    <div id="endpicker-container" style="margin-left: -1px;"></div>
</div>
''' % self.get_attrs(pyClassNames=self.style.get_classes())


class TimePicker(Html.Html):
  name = 'ToastTime'
  requirements = ('tui-time-picker', )
  _option_cls = OptToastTime.OptionTime

  def __init__(self, report, width, height, html_code, options, profile):
    super(TimePicker, self).__init__(
      report, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.options.usageStatistics = False
    self.style.css.margin_top = 2
    self.style.css.padding = "0 !IMPORTANT"

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    :rtype: GrpClsToastDates.ClassTimePicker
    """
    if self._styleObj is None:
      self._styleObj = GrpClsToastDates.ClassTimePicker(self)
    return self._styleObj

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
    TimePicker static properties.

    :rtype: OptToastTime.OptionTime
    """
    return super().options

  @property
  def dom(self):
    """
    Description:
    -----------
    The common DOM properties.

    :rtype: DomToastDatePicker.DomTime
    """
    if self._dom is None:
      self._dom = DomToastDatePicker.DomTime(self, report=self.page)
    return self._dom

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript module of the items in the menu.

    :rtype: JsToastDates.TimePicker
    """
    if self._js is None:
      self._js = JsToastDates.TimePicker(self, varName=self.var, report=self.page)
    return self._js

  _js__builder__ = '''window[htmlObj.id] = new tui.TimePicker('#'+ htmlObj.id, options)'''

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '''
<div %(attrs)s>ghjg
  <div id="%(htmlCode)s"></div>
  <div id="%(htmlCode)s-meridiem"></div>
</div>''' % {
      "attrs": self.get_attrs(pyClassNames=self.style.get_classes()),
      "htmlCode": self.htmlCode}
