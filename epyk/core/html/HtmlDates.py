import time

from epyk.core.html import Html

from epyk.core.html.options import OptInputs


class DatePicker(Html.Html):
  requirements = ('jqueryui', )
  name = 'Date Picker'

  def __init__(self, report, value, label, icon, color, htmlCode, profile, options, helper):
    dfltOptions = {'dateFormat': 'yy-mm-dd'}
    dfltOptions.update(options)
    super(DatePicker, self).__init__(report, value, htmlCode=htmlCode, profile=profile)
    # Add all the internal components input, label, icon and helper
    self.input = self._report.ui.inputs.d_date(self.val, options=dfltOptions).css({"padding": 0})
    self.prepend_child(self.input)
    self.add_icon(icon, css={"margin-left": '5px', 'color': self._report.theme.success[1]}, position="after")
    if self.icon is not None:
      self.icon.click(self.input.dom.events.trigger("click").toStr())
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle", "display": "block", "width": 'auto',
              'margin-top': '2px'})

  @property
  def options(self):
    """
    Description:
    -----------
    The progress bar is designed to display the current percent complete for a process.
    The bar is coded to be flexibly sized through CSS and will scale to fit inside its parent container by default.

    Related Pages:

			https://api.jqueryui.com/menu

    :rtype: OptInputs.OptionsDatePicker
    """
    return self.input.options

  def excluded_dates(self, dts=None, jsFncs=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param dts:
    :param jsFncs:
    """
    return self.input.excluded_dates(dts, jsFncs)

  def included_dates(self, dts=None, jsFncs=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param dts:
    :param jsFncs:
    """
    return self.input.included_dates(dts, jsFncs)

  def add_options(self, options=None, name=None, value=None):
    """
    Add TimePicker options

    Related Pages:

			https://timepicker.co/options/

    Attributes:
    ----------
    :param key: A string or a Python dictionary with the options to set
    :param val: Optional.
    """
    if options is None and name is None:
      raise Exception("Either the attrs or the name should be specified")

    if options is None:
      options = {name: value}
    for k, v in options.items():
      self.vals['options'][k] = v
    return self

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class TimePicker(Html.Html):
  requirements = ('timepicker', )
  name = 'Time Picker'

  def __init__(self, report, value, label, icon, color, htmlCode, profile, options, helper):
    super(TimePicker, self).__init__(report, None, htmlCode=htmlCode, profile=profile)
    # Add the internal components (label, icon)
    self.input = self._report.ui.inputs.d_time(value, options=options)
    self.input.set_attrs(name="class", value='time').css({"padding": 0})
    self.prepend_child(self.input)
    self.add_icon(icon, css={"margin-left": '5px', 'color': self._report.theme.success[1]}, position="after")
    if self.icon is not None:
      self.icon.click(self.input.dom.events.trigger("click").toStr())
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_helper(helper, css={"float": "none", "margin-left": "5px"})
    self.css({"color": color or 'inherit', "vertical-align": "middle", 'margin-top': '2px'})

  @property
  def options(self):
    """
    Description:
    -----------
    The progress bar is designed to display the current percent complete for a process.
    The bar is coded to be flexibly sized through CSS and will scale to fit inside its parent container by default.

    Related Pages:

			https://api.jqueryui.com/menu

    :rtype: OptInputs.OptionsTimePicker
    """
    return self.input.options

  def change(self, jsFnc):
    """
    Description:
    -----------
    Event triggerd when the value of the input field changes. A Date object containing the selected time is passed as the first argument of the callback.
    Note: the variable time is a function parameter received in the Javascript side

    Usage::

      morning = rptObj.ui.fields.time("8:13:00", label="Time field")
    morning.change([
      rptObj.js.alert("time", skip_data_convert=True)
    ])

    Related Pages:

			https://timepicker.co/options/

    :param jsFnc:
    """
    self.input.change(jsFnc)
    return self

  def __str__(self):
    return '<div %(attr)s>%(helper)s</div>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'helper': self.helper}


class CountDownDate(Html.Html):
  name = 'Countdown'

  def __init__(self, report, yyyy_mm_dd, label, icon, timeInMilliSeconds, width, height, htmlCode, helper, profile):
    super(CountDownDate, self).__init__(report, yyyy_mm_dd, htmlCode=htmlCode, profile=profile,
                                        css_attrs={"width": width, "height": height})
    self._jsStyles = {"delete": True}
    self.timeInMilliSeconds = timeInMilliSeconds
    # Add the underlying components
    self.add_label(label, css={"padding": '2px 0', 'height': 'auto'})
    self.add_icon(icon)
    self.add_helper(helper)

  @property
  def jqId(self):
    return "$('#%s span')" % self.htmlId

  @property
  def _js__builder__(self):
    return ''' 
      var splitDt = data.split("-"); var endDate = new Date(splitDt[0], parseInt(splitDt[1])-1, splitDt[2]);
      var now = new Date().getTime(); var distance = endDate.getTime() - now;

      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance %% (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance %% (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance %% (1000 * 60)) / 1000);

      htmlObj.innerHTML = "<b>"+ days +"d "+ hours +"h "+ minutes + "m "+ seconds +"s </b>"; 
      if ((distance < 0) && (options.delete)){clearInterval(htmlObj.id +"_interval")
      }'''

  def __str__(self):
    self.jsUpdateDataFnc = '''var %(htmlId)s_interval = setInterval(function(){%(refresh)s}, %(timeInMilliSeconds)s)
              ''' % {'htmlId': self.htmlId, 'refresh': self.refresh(), 'timeInMilliSeconds': self.timeInMilliSeconds}
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.jsUpdateDataFnc)
    return '<div %s><span></span>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class LastUpdated(Html.Html):
  name = 'Last Update'

  def __init__(self, report, label, color, width, height, htmlCode, profile):
    super(LastUpdated, self).__init__(report, "%s %s" % (label or "Last update", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())),
                                      htmlCode, css_attrs={"width": width, "height": height, "color": color}, profile=profile)

  def __str__(self):
    return '<div %(strAttr)s>%(content)s</div>' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'content': self.val}
