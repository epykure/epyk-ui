from epyk.core.html import Defaults


class Meta(object):
  def __init__(self):
    self._metas = {}
    self.__cols = ['charset', 'viewport']
    self.viewport().charset()
    self.http_equiv("X-UA-Compatible", "IE=EDGE").http_equiv("Content-Type", "text/html; charset=utf-8")
    self.http_equiv("Cache-control", "no-cache")

  def viewport(self, value="width=device-width,height=device-height,initial-scale=1.0"):
    """
    Description:
    ------------
    Setting the viewport to make your website look good on all devices

    Usage::

      rptObj.headers.meta.viewport("test")

    Related Pages:

      https://www.w3schools.com/html/html_head.asp

    Attributes:
    ----------
    :param value: Optional. A string with the view port content
    """
    self._metas["viewport"] = '<meta name="viewport" content="%s">' % value
    return self

  def charset(self, value="UTF-8"):
    """
    Description:
    ------------
    Define the character set used

    Usage::

      rptObj.headers.meta.charset("test")

    Related Pages:

			https://www.w3schools.com/tags/tag_meta.asp

    Attributes:
    ----------
    :param value: Optional. A String
    """
    self._metas["charset"] = '<meta charset="%s">' % value
    return self

  def refresh(self, time):
    """
    Description:
    ------------
    Refresh document every X seconds

    Usage::

      rptObj.headers.meta.refresh(10)

    Related Pages:

			https://www.w3schools.com/tags/tag_meta.asp

    Attributes:
    ----------
    :param time: A time in second
    """
    self._metas["refresh"] = '<meta http-equiv="refresh" content="%s">' % time
    if not "refresh" in self.__cols:
      self.__cols.append("refresh")
    return self

  def author(self, name):
    """
    Description:
    ------------
    Define the author of the page

    Usage::

      rptObj.headers.meta.author('epykure')

    Attributes:
    ----------
    :param name: String. The author name
    """
    self._metas["author"] = '<meta name="author" content="%s">' % name
    if not "author" in self.__cols:
      self.__cols.append("author")
    return self

  def description(self, value):
    """
    Description:
    ------------
    Define a description of your web page

    Usage::

      rptObj.headers.meta.description('This is a description')

    Related Pages:

			https://www.w3schools.com/html/html_head.asp

    Attributes:
    ----------
    :param value: String. The report description
    """
    self._metas["description"] = '<meta name="description" content="%s">' % value
    if not "description" in self.__cols:
      self.__cols.append("description")
    return self

  def keywords(self, content):
    """
    Description:
    ------------
    Define keywords for search engine

    Usage::

      rptObj.headers.meta.keywords(['python', 'javascript'])

    Related Pages:

			https://www.w3schools.com/html/html_head.asp

    Attributes:
    ----------
    :param content: String or list with the keyword data
    """
    if isinstance(content, list):
      content = ",".join(content)
    self._metas["keywords"] = '<meta name="keywords" content="%s">' % content
    if not "keywords" in self.__cols:
      self.__cols.append("keywords")
    return self

  def custom(self, name, content):
    """
    Description:
    ------------
    Bespoke function to add other meta tags

    Usage::

      rptObj.headers.meta.custom('language', 'python')

    Attributes:
    ----------
    :param name: String.
    :param content: String.
    """
    self._metas[name] = '<meta name="%s" content="%s">' % (name, content)
    if not name in self.__cols:
      self.__cols.append(name)
    return self

  def http_equiv(self, name, content):
    """
    Description:
    ------------
    Bespoke function to add other http-equiv tags to the meta section

    Usage::

      rptObj.headers.meta.http_equiv('language', 'python')

    Attributes:
    ----------
    :param name: String.
    :param content: String

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

  def dev(self, icon=None):
    """
    Description:
    ------------
    Change the tab icon to highlight this page is still in dev mode

    Attributes:
    ----------
    :param icon:
    """
    self._favicon_url = icon or Defaults.FAVICON_DEV_URL

  @property
  def meta(self):
    """
    Description:
    ------------
    Property to the Meta data dictionary for the HTML page

    Metadata is data (information) about data.

    The <meta> tag provides metadata about the HTML document.
    Metadata will not be displayed on the page, but will be machine parsable.

    Usage::

      rptObj.headers.meta

    Related Pages:

	  https://www.w3schools.com/tags/tag_meta.asp

    :rtype: Meta
    """
    if self.__meta is None:
      self.__meta = Meta()
    return self.__meta

  def title(self, value):
    """
    Description:
    ------------
    The <title> tag is required in all HTML documents and it defines the title of the document.

    Usage::

      rptObj.headers.title("title")

    Related Pages:

      https://www.w3schools.com/tags/tag_title.asp

    Attributes:
    ----------
    :param value: String.
    """
    self._headers['title'] = value
    return self

  def base(self, url):
    """
    Description:
    ------------
    Specify a dedicated path for the relative paths in the page.
    Basically the images will use this path as base if present in the page

    Related Pages:

      https://www.w3schools.com/tags/tag_base.asp

    Attributes:
    ----------
    :param url:

    :return:
    """
    self._base = url
    return self

  def favicon(self, url):
    """
    Description:
    ------------
    The <link> tag defines a link between a document and an external resource.

    The <link> tag is used to link to external style sheets.

    Usage::

      rptObj.headers.favicon('https://github.com/favicon.ico')

    Related Pages:

			https://www.w3schools.com/tags/tag_link.asp

    Attributes:
    ----------
    :param url:

    :return:
    """
    self._favicon_url = url
    return self

  def __str__(self):
    result = [str(self.meta)]
    if self._headers.get("title") is not None:
      result.append("<title>%s</title>" % self._headers.get("title"))
    result.append("<link rel='icon' href='%s' type='image/x-icon'/ >" % self._favicon_url)
    return "\n".join(result)

