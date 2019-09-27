"""

https://www.w3schools.com/html/html_head.asp
"""


class Meta(object):
  """

  """

  def charset(self):
    """

    :return:
    """
    return self

  def author(self):
    """

    :return:
    """
    return self



  def description(self):
    """

    :return:
    """
    return self

  def keywords(self):
    """

    :return:
    """
    return self



  def viewport(self):
    """

    :return:
    """
    return self


class Header(object):

  def __init__(self, report):
    self._report = report
    self._report._props["header"] = {}

  @property
  def title(self, title):
    """
    Report title

    :param title:

    :return:
    """
    self._report._props["header"]['title'] = title
    return self

  def base(self, url):
    """
    Specify a dedicated path for the relative paths in the page.
    Basically the images will use this path as base if present in the page

    Documentation
    https://www.w3schools.com/tags/tag_base.asp

    :param url:

    :return:
    """

