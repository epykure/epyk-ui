
from epyk.fwk.bs.html import BsDatePicker


class Dates:

  def __init__(self, ui):
    self.page = ui.page

  def datetime(self, value=None, label="", icon="", html_code=None, profile=False, options=None, helper=""):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/#using-locales

    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param html_code:
    :param profile:
    :param options:
    :param helper:
    """
    date = BsDatePicker.BsDate(self.page, value, label, icon, html_code, profile, options, helper)
    date.options.format = 'YYYY-MM-DD HH:mm:ss'
    return date

  def date(self, value=None, label="", icon="", html_code=None, profile=False, options=None, helper=""):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/#using-locales

    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param html_code:
    :param profile:
    :param options:
    :param helper:
    """
    date = BsDatePicker.BsDate(self.page, value, label, icon, html_code, profile, options, helper)
    date.options.format = 'YYYY-MM-DD'
    return date

  def today(self, label="", icon="", html_code=None, profile=False, options=None, helper=""):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/#using-locales

    Attributes:
    ----------
    :param label:
    :param icon:
    :param html_code:
    :param profile:
    :param options:
    :param helper:
    """
    value = self.page.py.dates.today
    date = BsDatePicker.BsDate(self.page, value, label, icon, html_code, profile, options, helper)
    date.options.format = 'YYYY-MM-DD'
    return date

  def cob(self, label="", icon="", html_code=None, profile=False, options=None, helper=""):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/#using-locales

    Attributes:
    ----------
    :param label:
    :param icon:
    :param html_code:
    :param profile:
    :param options:
    :param helper:
    """
    value = self.page.py.dates.cob
    date = BsDatePicker.BsDate(self.page, value, label, icon, html_code, profile, options, helper)
    date.options.format = 'YYYY-MM-DD'
    return date

  def time(self, value=None, label="", icon="", html_code=None, profile=False, options=None, helper=""):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/#using-locales

    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param html_code:
    :param profile:
    :param options:
    :param helper:
    """
    date = BsDatePicker.BsDate(self.page, value, label, icon, html_code, profile, options, helper)
    date.options.format = 'LT'
    return date
