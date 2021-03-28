

class ItemsLinkRec:

  @staticmethod
  def from_records(records, column, text=None, url=None, dsc=None, image=None, target=None, icon=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param records:
    :param column:
    :param text:
    """
    if text is None:
      text = column
    result = {}
    if callable(text):
      for rec in records:
        result[rec[column]] = {"value": text(rec), "text": rec[column]}
    else:
      for rec in records:
        result[rec[column]] = {"value": rec[text], "text": rec[column]}
    return [result[k] for k in sorted(result.keys())]


class ItemsIconRec:

  @staticmethod
  def from_records(records, column, icon=None):
    pass


class ItemsCheckRec:

  @staticmethod
  def from_records(records, column, text=None, checked=None):
    pass


class ItemsBoxRec:

  @staticmethod
  def from_records(records, column, title=None, color=None, icons=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param records:
    :param column:
    :param title:
    :param color:
    :param icons:
    """
    if title is None:
      title = column
    result = {}
    if callable(title):
      for rec in records:
        result[rec[column]] = {"title": title(rec), "text": rec[column]}
    else:
      for rec in records:
        result[rec[column]] = {"title": rec[title], "text": rec[column]}

    return [result[k] for k in sorted(result.keys())]


class ItemsTweetRec:

  @staticmethod
  def from_records(records, column, time=None, title=None, author=None):
    pass

