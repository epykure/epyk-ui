
import time
import datetime
from typing import Optional

from epyk.core.py import primitives


DFL_DATE_FORMAT = '%Y-%m-%d'


class PyDates:
  """ Common module for managing dates.

  This module is a light wrapper on top of datetime in order to perform basic operations on dates.
  This will also standardise the date format to YYYY-MM-DD in the Python layer to simplify the
  conversion to the Javascript

  All the tests in this module are using doctest.
  """

  def __init__(self, src: primitives.PageModel = None):
    self.page = src

  @property
  def today(self):
    """ Return a String date in a format YYYY-MM-DD.

    Even if within the property python date object are used, this function will
    always return a string date in a specific format to guarantee and simplify the compatibility between languages
    within the components.

    Usage::

      PyDates().today

    Related Pages:

      https://docs.python.org/2/library/datetime.html

    :return: A string date in the format YYYY-MM-DD
    """
    return datetime.datetime.today().strftime(DFL_DATE_FORMAT)

  @property
  def now(self):
    """ Return the current timestamp in a format YYYY-MM-DD HH:mm:dd.

    Usage::

      PyDates().now

    Related Pages:

      https://docs.python.org/2/library/datetime.html

    :return: Return a string timestamp
    """
    return datetime.datetime.fromtimestamp(time.time()).strftime(DFL_DATE_FORMAT + ' %H:%M:%S')

  @staticmethod
  def path(with_time: bool = False):
    """ Return a predefined format for date in a file path.
    Using this method will ensure a consistency in the naming convention of the various files in the project.

    :param bool with_time: Optional. Specify if the time should be added to the path.
    """
    if with_time:
      return datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')

    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d')

  @property
  def cob(self):
    """ Returns the last close of business date.

    In this property the parameter weekdays is forced to True.

    Usage::

      page.py.dates.cob

    :return: A string date
    """
    return self.date_from_alias("T")

  @property
  def month_end(self):
    """ Returns the last month end date.

    In this property the parameter weekdays is forced to True.

    UUsage::

      page.py.dates.month_end

    :return: A string date
    """
    return self.date_from_alias("M")

  @property
  def months(self):
    """ Returns the list of month end dates from the beginning of the year.

    In this property the parameter weekdays is forced to True.

    Usage::

      page.py.dates.months

    :return: A list of String dates
    """
    date_split = list(map(lambda x: int(x), self.today.split("-")))
    return self.month_ends(datetime.datetime(date_split[0], 1, 1).strftime(DFL_DATE_FORMAT), self.today)

  @property
  def quarters(self):
    """ Return the list of quarter dates since the beginning of the year.

    In this property the parameter weekdays is forced to True.

    Usage::

      page.py.dates.quarters

    :return: A list of String dates
    """
    results = []
    for i, v in enumerate(self.months):
      if i % 3 == 2:
        results.append(v)
    return results

  def date_from_alias(self, alias: str, from_date: Optional[str] = None):
    """ Return the date corresponding to an alias code like T, T-N, M...

    Usage::

      >>> PyDates().date_from_alias("T", "2019-08-08")
      '2019-08-07'

    :param alias: The alias of the operation (T-3, M-2....)
    :param from_date: Optional. The start date from which the time operation is applied. Today by default

    :return: The converted date or a list of dates.
    """
    if from_date is None:
      cob_date = datetime.datetime.today()
    else:
      cob_date = datetime.datetime(*map(lambda x: int(x), from_date.split("-")))
    if len(alias) > 1:
      f_type, f_count = alias[0], "".join(alias[2:])
    else:
      f_type, f_count = alias, 0
    if f_type == 'T':
      for _ in range(0, int(f_count) + 1):
        if len(alias) > 1:
          if alias[1] == '+':
            cob_date = cob_date + datetime.timedelta(days=1)
            while cob_date.weekday() in [5, 6]:
              cob_date = cob_date + datetime.timedelta(days=1)
          else:
            cob_date = cob_date - datetime.timedelta(days=1)
            while cob_date.weekday() in [5, 6]:
              cob_date = cob_date - datetime.timedelta(days=1)
        else:
          cob_date = cob_date - datetime.timedelta(days=1)
          while cob_date.weekday() in [5, 6]:
            cob_date = cob_date - datetime.timedelta(days=1)
      return cob_date.strftime(DFL_DATE_FORMAT)

    if f_type == 'M':
      month = cob_date.month - int(f_count)
      year = cob_date.year
      if month <= 0:
        month = 12 - month
        year -= 1
      end_month_date = datetime.datetime(year, month, 1)
      end_month_date = end_month_date - datetime.timedelta(days=1)
      while end_month_date.weekday() in [5, 6]:
        end_month_date = end_month_date - datetime.timedelta(days=1)
      return end_month_date.strftime(DFL_DATE_FORMAT)

    if f_type == 'W':
      cob_date = cob_date - datetime.timedelta(days=1)
      while cob_date.weekday() != 4:
        cob_date = cob_date - datetime.timedelta(days=1)
      cob_date = cob_date - datetime.timedelta(days=(int(f_count) * 7))
      return cob_date.strftime(DFL_DATE_FORMAT)

    if f_type == 'Y':
      end_year_date = datetime.datetime(cob_date.year - int(f_count), 1, 1)
      end_year_date = end_year_date - datetime.timedelta(days=1)
      while end_year_date.weekday() in [5, 6]:
        end_year_date = end_year_date - datetime.timedelta(days=1)
      return end_year_date.strftime(DFL_DATE_FORMAT)

    return alias

  @staticmethod
  def date_from_excel(xl_date: int):
    """ Convert an Excel date to a standard date format YYYY-MM-DD.

    Usage::

      >>> PyDates().date_from_excel(39448)
      '2008-01-01'

    Related Pages:

      https://support.office.com/en-gb/article/date-function-e36c0c8c-4104-49da-ab83-82328b832349?ui=en-US&rs=en-GB&ad=GB

    :param xl_date: A date in the Excel format.

    :return: The date as a String in the common format YYYY-MM-DD
    """
    dt = datetime.datetime.fromordinal(datetime.datetime(1900, 1, 1).toordinal() + xl_date - 2)
    return dt.strftime(DFL_DATE_FORMAT)

  def month_ends(self, from_dt: str, to_dt: str, weekdays: bool = True):
    """ Return the list of end of month dates between two dates.

    UUsage::

      >>> PyDates().month_ends("2019-01-01", "2019-06-05", False)
      ['2019-01-31', '2019-02-28', '2019-03-31', '2019-04-30', '2019-05-31']

    :param from_dt: The start date in format YYYY-MM-DD.
    :param to_dt: The end date in format YYYY-MM-DD.
    :param weekdays: Optional. remove the weekends from the potential dates (take the day before). Default True.

    :return: A list of dates.
    """
    if to_dt < from_dt:
      tmp = from_dt
      from_dt = to_dt
      to_dt = tmp
    results = []
    date_split = list(map(lambda x: int(x), from_dt.split("-")))
    end_dt = datetime.datetime(*map(lambda x: int(x), to_dt.split("-")))
    dt = datetime.datetime(date_split[0], date_split[1]+1, 1) - datetime.timedelta(days=1)
    while dt < end_dt:
      results.append(dt.strftime(DFL_DATE_FORMAT))
      dt = datetime.datetime(dt.year + int((dt.month + 1) / 12), (dt.month + 1) % 12 + 1, 1)
      dt = dt - datetime.timedelta(days=1)
      if weekdays:
        while dt.weekday() in [5, 6]:
          dt = dt - datetime.timedelta(days=1)
    return results

  def range_dates(self, to_dt: str, from_dt: Optional[str] = None, weekdays: bool = True):
    """ Get the list of dates between two dates.

    The date should be two string dates in the format YYYY-MM-DD.
    The resulting range of date will always be increasing

    Usage::

      >>> PyDates().range_dates("2019-01-01", "2019-01-11")
      ['2019-01-11', '2019-01-10', '2019-01-09', '2019-01-08', '2019-01-07', '2019-01-04', '2019-01-03', '2019-01-02', '2019-01-01']

    :param from_dt: The start date in format YYYY-MM-DD.
    :param to_dt: Optional. The end date in format YYYY-MM-DD.
    :param weekdays: Optional. Remove the weekends from the potential dates (take the day before). Default True

    :return: A list of dates.
    """
    if from_dt is None:
      from_dt = datetime.datetime.today().strftime(DFL_DATE_FORMAT)
    start_date = self.date_from_alias(from_dt)
    end_date = self.date_from_alias(to_dt, from_date=start_date)
    if start_date < end_date:
      start_date = self.date_from_alias(to_dt, from_date=start_date)
      end_date = self.date_from_alias(from_dt)
    dt = datetime.datetime(*map(lambda x: int(x), start_date.split('-')))
    target_date = datetime.datetime(*map(lambda x: int(x), end_date.split('-')))
    dates = [start_date]
    while dt > target_date:
      dt = dt - datetime.timedelta(days=1)
      if not dt.weekday() in [5, 6] or not weekdays:
        dates.append(dt.strftime(DFL_DATE_FORMAT))
    return dates

  @staticmethod
  def from_timestamp(timestamp: int, offset: int = 0, reference: int = 60, factor: int = 1000):
    """ The default value will be given considering the GMT time.

    Usage::

      timestamp_s = page.py.dates.from_timestamp(1573074335010, 0)

    :param timestamp: The timestamp in milliseconds.
    :param offset: Optional. The time zone.
    :param reference: Optional. The reference shift in minutes.
    :param factor:

    :return: The server timestamp string
    """
    date = datetime.datetime.fromtimestamp(timestamp / factor)
    date = date + datetime.timedelta(minutes=(int(offset) + reference))
    return date.strftime(DFL_DATE_FORMAT + ' %H:%M:%S')

  @staticmethod
  def to_server_time(timestamp: str, offset: int = 0, reference: int = 60):
    """ Return the converted timestamp to be stored in the database.
    This conversion will be based on the offset coming from the UI to convert to common time.

    Usage::

      >>> PyDates().to_server_time("2019-08-20 20:04:10", 2)
      '2019-08-20 21:06:10'

    :param timestamp: The client timestamp.
    :param offset: Optional. The client offset time to be applied before storage in hour.
    :param reference: Optional. The reference time used on the server side.

    :return: The server timestamp string
    """
    date = datetime.datetime.strptime(timestamp, DFL_DATE_FORMAT + ' %H:%M:%S')
    date = date + datetime.timedelta(minutes=(int(offset) + reference))
    return date.strftime(DFL_DATE_FORMAT + ' %H:%M:%S')

  @staticmethod
  def to_user_time(timestamp: str, offset: int, reference: int = 60):
    """ Return the converted timestamp to be returned to the user.
    This is converting a stored timestamp to a user one.

    Usage::

      >>> PyDates().to_user_time('2019-08-20 21:06:10', 2)
      '2019-08-20 20:04:10'

    :param timestamp: The server timestamp.
    :param offset: The client offset time to be applied before storage.
    :param reference: Optional. The reference time used on the server side (default 20).

    :return: The client timestamp string
    """
    date = datetime.datetime.strptime(timestamp, DFL_DATE_FORMAT + ' %H:%M:%S')
    date = date + datetime.timedelta(minutes=-1 * (int(offset) + reference))
    return date.strftime(DFL_DATE_FORMAT + ' %H:%M:%S')

  @staticmethod
  def delta(from_dt: str, to_dt: str, format_dt: str = "%Y-%m-%d"):
    """

    :param from_dt:
    :param to_dt:
    :param format_dt:
    """
    from_dt = datetime.datetime.strptime(from_dt, format_dt)
    to_dt = datetime.datetime.strptime(to_dt, format_dt)
    return to_dt - from_dt

  @staticmethod
  def elapsed(delta_time, with_time: bool = False):
    """ Get the time between two dates.
    This function will only format the result of a delta time object.

    # TODO: Fix this method

    :param delta_time: delta_time. The delta time between two python dates.
    :param bool with_time: Optional. A flag to mention if the time should be computed.
    """
    year = delta_time.days // 365
    months = (delta_time.days - year * 365) // 30
    days = delta_time.days - year * 365 - months * 30
    if not with_time:
      return {"year": year, 'months': months, 'days': days}

    hours = int(delta_time.seconds / 3600)
    minutes = int((delta_time.seconds - hours * 3600) / 60)
    seconds = delta_time.seconds - hours * 3600 - minutes * 60
    return {"years": year, 'months': months, 'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}
