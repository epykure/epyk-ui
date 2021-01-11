
from epyk.fwk.bs.html import BsDatePicker


class Dates(object):

  def __init__(self, context):
    self.context = context

  def datetime(self, value=None, label="", icon="", htmlCode=None, profile=False, options=None, helper=""):
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
    :param htmlCode:
    :param profile:
    :param options:
    :param helper:
    """
    date = BsDatePicker.BsDate(self.context.rptObj, value, label, icon, htmlCode, profile, options, helper)
    date.options.format = 'YYYY-MM-DD HH:mm:ss'
    return date

  def date(self, value=None, label="", icon="", htmlCode=None, profile=False, options=None, helper=""):
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
    :param htmlCode:
    :param profile:
    :param options:
    :param helper:
    """
    date = BsDatePicker.BsDate(self.context.rptObj, value, label, icon, htmlCode, profile, options, helper)
    date.options.format = 'YYYY-MM-DD'
    return date

  def today(self, label="", icon="", htmlCode=None, profile=False, options=None, helper=""):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/#using-locales

    Attributes:
    ----------
    :param label:
    :param icon:
    :param htmlCode:
    :param profile:
    :param options:
    :param helper:
    """
    value = self.context.rptObj.py.dates.today
    date = BsDatePicker.BsDate(self.context.rptObj, value, label, icon, htmlCode, profile, options, helper)
    date.options.format = 'YYYY-MM-DD'
    return date

  def cob(self, label="", icon="", htmlCode=None, profile=False, options=None, helper=""):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/#using-locales

    Attributes:
    ----------
    :param label:
    :param icon:
    :param htmlCode:
    :param profile:
    :param options:
    :param helper:
    """
    value = self.context.rptObj.py.dates.cob
    date = BsDatePicker.BsDate(self.context.rptObj, value, label, icon, htmlCode, profile, options, helper)
    date.options.format = 'YYYY-MM-DD'
    return date

  def time(self, value=None, label="", icon="", htmlCode=None, profile=False, options=None, helper=""):
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
    :param htmlCode:
    :param profile:
    :param options:
    :param helper:
    """
    date = BsDatePicker.BsDate(self.context.rptObj, value, label, icon, htmlCode, profile, options, helper)
    date.options.format = 'LT'
    return date
