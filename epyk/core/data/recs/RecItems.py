
from typing import Callable, Dict, Any


class ItemsLinkRec:

  @staticmethod
  def from_records(records, column, text: Callable = None, other_fields: Dict[str, Any] = None):
    """

    Usage::

    :param records:
    :param column:
    :param text: A Python function to transform the text displayed.
    :param other_fields:
    """
    if text is None:
      text = column
    result = {}
    if callable(text):
      for rec in records:
        result[rec[column]] = {"value": text(rec), "text": rec[column]}
        if other_fields is not None:
          for f, v in other_fields.items():
            if callable(v):
              result[rec[column]][f] = v(rec)
            else:
              result[rec[column]][f] = rec[v]
    else:
      for rec in records:
        result[rec[column]] = {"value": rec[text], "text": rec[column]}
        if other_fields is not None:
          for f, v in other_fields.items():
            if callable(v):
              result[rec[column]][f] = v(rec)
            else:
              result[rec[column]][f] = rec[v]
    return [result[k] for k in sorted(result.keys())]


class ItemsIconRec:

  @staticmethod
  def from_records(records, column, icon=None, other_fields: Dict[str, Any] = None):
    other_fields = other_fields or {}
    other_fields["icon"] = icon
    return ItemsLinkRec.from_records(records, column, other_fields=other_fields)


class ItemsCheckRec:

  @staticmethod
  def from_records(records, column, text=None, checked=None, other_fields: Dict[str, Any] = None):
    other_fields = other_fields or {}
    other_fields["checked"] = checked
    return ItemsLinkRec.from_records(records, column, text=text, other_fields=other_fields)


class ItemsBoxRec:

  @staticmethod
  def from_records(records, column, title=None, color=None, icons=None):
    """

    Usage::

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

