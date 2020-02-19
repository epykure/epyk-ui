"""

https://www.w3schools.com/html/html_head.asp
"""

from epyk.core.html import Defaults


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
    self._favicon_url = Defaults.FAVICON_URL
    if report is not None:
      self._report = report
      self._report._props["header"] = self._headers

  @property
  def meta(self):
    """
    Property to the Meta data dictionary for the HTML page

    https://www.w3schools.com/tags/tag_meta.asp

    :rtype: Meta
    """
    if self.__meta is None:
      self.__meta = Meta()
    return self.__meta

  def title(self, value):
    """
    The <title> tag is required in all HTML documents and it defines the title of the document.

    https://www.w3schools.com/tags/tag_title.asp

    :param value:
    """
    self._headers['title'] = value
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
    self._base = url
    return self

  def favicon(self, url):
    """
    The <link> tag defines a link between a document and an external resource.

    The <link> tag is used to link to external style sheets.

    https://www.w3schools.com/tags/tag_link.asp
    """
    self._favicon_url = url
    return self

  def __str__(self):
    """

    :return:
    """
    if self._headers.get("title") is not None:
      print("<title>%s</title>" % self._headers.get("title"))
    print("<link rel='icon' href='%s' type='image/x-icon'/ >" % self._favicon_url)
    return str(self.meta)


if __name__ == "__main__":
  header = Header()
  header.title("test")
  print(header)

