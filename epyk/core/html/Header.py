"""

https://www.w3schools.com/html/html_head.asp
"""


class Meta(object):
  """
  Metadata is data (information) about data.

  The <meta> tag provides metadata about the HTML document.
  Metadata will not be displayed on the page, but will be machine parsable.
  """
  def __init__(self):
    self._metas = {}
    self.__cols = ['charset', 'viewport']
    self.viewport().charset()
    self.http_equiv("X-UA-Compatible", "IE=EDGE").http_equiv("Content-Type", "text/html; charset=utf-8")
    self.http_equiv("Cache-control", "no-cache")

  def viewport(self, value="width=device-width,height=device-height,initial-scale=1.0"):
    """
    Setting the viewport to make your website look good on all devices

    Documentation
    https://www.w3schools.com/html/html_head.asp

    :param value: Optional
    """
    self._metas["viewport"] = '<meta name="viewport" content="%s">' % value
    return self

  def charset(self, value="UTF-8"):
    """

    Documentation
    https://www.w3schools.com/tags/tag_meta.asp

    :param value: Optional

    """
    self._metas["charset"] = '<meta charset="%s">' % value
    return self

  def refresh(self, time):
    """
    Refresh document every X seconds

    Documentation
    https://www.w3schools.com/tags/tag_meta.asp

    :param time: A time in second
    """
    self._metas["refresh"] = '<meta http-equiv="refresh" content="%s">' % time
    return self

  def author(self, name):
    """

    :param:
    """
    self._metas["author"] = '<meta name="author" content="%s">' % name
    if not "author" in self.__cols:
      self.__cols.append("author")
    return self

  def description(self, value):
    """
    Define a description of your web page

    :param value:
    """
    self._metas["description"] = '<meta name="description" content="%s">' % value
    if not "description" in self.__cols:
      self.__cols.append("description")
    return self

  def keywords(self, content):
    """
    Define keywords for search engine

    Documentation
    https://www.w3schools.com/tags/tag_meta.asp

    :param content:
    """
    self._metas["keywords"] = '<meta name="keywords" content="%s">' % content
    if not "keywords" in self.__cols:
      self.__cols.append("keywords")
    return self

  def custom(self, name, content):
    """

    :param name:
    :param content:
    """
    self._metas[name] = '<meta name="%s" content="%s">' % (name, content)
    if not name in self.__cols:
      self.__cols.append(name)
    return self

  def http_equiv(self, name, content):
    """

    :param name:
    :param content:
    :return:
    """
    self._metas[name] = '<meta http-equiv="%s" content="%s">' % (name, content)
    if not name in self.__cols:
      self.__cols.append(name)
    return self

  def __str__(self):
    h = []
    for col in self.__cols:
      if self._metas.get(col) is not None:
        h.append(self._metas.get(col))
    return "\n".join(h)


class Header(object):
  def __init__(self, report=None):
    self._headers, self._links, self._styles, self._scripts, self._base, self.__meta = {}, [], [], [], None, None
    if report is not None:
      self._report = report
      self._report._props["header"] = self._headers

  @property
  def meta(self):
    if self.__meta is None:
      self.__meta = Meta()
    return self.__meta

  @property
  def title(self):
    return self._headers.get('title')

  @title.setter
  def title(self, title):
    self._headers['title'] = title

  def base(self, url):
    """
    Specify a dedicated path for the relative paths in the page.
    Basically the images will use this path as base if present in the page

    Documentation
    https://www.w3schools.com/tags/tag_base.asp

    :param url:

    :return:
    """
    self._base = url
    return self

  def favicon(self):
    """

    <link rel="shortcut icon" href="http://example.com/myicon.ico" />
    <link rel="icon" type="image/png" href="http://example.com/image.png" />

    <link rel='shortcut icon' type='image/vnd.microsoft.icon' href='/favicon.ico'> <!-- IE -->
    <link rel='apple-touch-icon' type='image/png' href='/icon.57.png'> <!-- iPhone -->
    <link rel='apple-touch-icon' type='image/png' sizes='72x72' href='/icon.72.png'> <!-- iPad -->
    <link rel='apple-touch-icon' type='image/png' sizes='114x114' href='/icon.114.png'> <!-- iPhone4 -->
    <link rel='icon' type='image/png' href='/icon.114.png'> <!-- Opera Speed Dial, at least 144×114 px -->
    :return:
    """

  def __str__(self):
    """

    :return:
    """
    return str(self.meta)


if __name__ == "__main__":
  header = Header()
  header.title = "test"
  print(header)

