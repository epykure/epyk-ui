#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from epyk.core.html import Defaults


class Meta:
  def __init__(self, page):
    self._report = page
    self._metas = {}
    self.__cols = ['charset', 'viewport']
    self.viewport().charset()
    self.http_equiv("X-UA-Compatible", "IE=EDGE").http_equiv("Content-Type", "text/html; charset=utf-8")
    self.http_equiv("Cache-control", "no-cache")

  def viewport(self, attrs=None):
    """
    Description:
    ------------
    Setting the viewport to make your website look good on all devices.

    Usage::

      page.headers.meta.viewport({"width": "device-width"})

    Related Pages:

      https://www.w3schools.com/html/html_head.asp
      https://www.w3schools.com/tags/tag_meta.asp

    Attributes:
    ----------
    :param attrs: Dictionary. Optional. The view port attributes.
    """
    dflt_attrs = {"width": "device-width", "height": "device-height", "initial-scale": "1.0"}
    if attrs is not None:
      dflt_attrs.update(attrs)
    self._metas["viewport"] = '<meta name="viewport" content="%s">' % ", ".join(
      ["%s=%s" % (k, v) for k, v in dflt_attrs.items()])
    return self

  def charset(self, value="utf-8"):
    """
    Description:
    ------------
    Define the character set used.

    Usage::

      page.headers.meta.charset("test")

    Related Pages:

      https://www.w3schools.com/tags/tag_meta.asp
      https://www.w3schools.com/tags/att_meta_charset.asp

    Attributes:
    ----------
    :param value: String. Optional. The charset encoding.
    """
    common_vals = ("UTF-8", "ISO-8859-1")
    if self._report.verbose and value.upper() not in common_vals:
      logging.warning("Charset value %s not in common ones %s" % (value, common_vals))

    self._metas["charset"] = '<meta charset="%s">' % value
    return self

  def refresh(self, time):
    """
    Description:
    ------------
    Refresh document every X seconds.

    Usage::

      page.headers.meta.refresh(10)

    Related Pages:

      https://www.w3schools.com/tags/tag_meta.asp

    Attributes:
    ----------
    :param time: Integer. A time in second.
    """
    self._metas["refresh"] = '<meta http-equiv="refresh" content="%s">' % time
    if "refresh" not in self.__cols:
      self.__cols.append("refresh")
    return self

  def author(self, name):
    """
    Description:
    ------------
    Define the author of the page.

    Usage::

      page.headers.meta.author('epykure')

    Related Pages:

      https://www.w3schools.com/tags/att_meta_name.asp

    Attributes:
    ----------
    :param name: String. The author name.
    """
    self._metas["author"] = '<meta name="author" content="%s">' % name
    if "author" not in self.__cols:
      self.__cols.append("author")
    return self

  def description(self, value):
    """
    Description:
    ------------
    Define a description of your web page.

    Usage::

      page.headers.meta.description('This is a description')

    Related Pages:

      https://www.w3schools.com/html/html_head.asp

    Attributes:
    ----------
    :param value: String. The report description.
    """
    self._metas["description"] = '<meta name="description" content="%s">' % value
    if "description" not in self.__cols:
      self.__cols.append("description")
    return self

  def keywords(self, content):
    """
    Description:
    ------------
    Define keywords for search engine.

    Usage::

      page.headers.meta.keywords(['python', 'javascript'])

    Related Pages:

      https://www.w3schools.com/html/html_head.asp

    Attributes:
    ----------
    :param content: String | list. The keyword data.
    """
    if isinstance(content, list):
      content = ",".join(content)
    self._metas["keywords"] = '<meta name="keywords" content="%s">' % content
    if "keywords" not in self.__cols:
      self.__cols.append("keywords")
    return self

  def custom(self, name, content):
    """
    Description:
    ------------
    Bespoke function to add other meta tags.

    Usage::

      page.headers.meta.custom('language', 'python')

    Related Pages:

      https://www.w3schools.com/tags/att_meta_name.asp

    Attributes:
    ----------
    :param name: String. The name for the meta tag.
    :param content: String. The value of the meta tag.
    """
    self._metas[name] = '<meta name="%s" content="%s">' % (name, content)
    if name not in self.__cols:
      self.__cols.append(name)
    return self

  def http_equiv(self, name, content):
    """
    Description:
    ------------
    Bespoke function to add other http-equiv tags to the meta section.

    Usage::

      rptObj.headers.meta.http_equiv('language', 'python')

    Related Pages:

      https://www.w3schools.com/tags/att_meta_http_equiv.asp

    Attributes:
    ----------
    :param name: String. The name for the meta tag.
    :param content: String. The value of the meta tag.
    """
    self._metas[name] = '<meta http-equiv="%s" content="%s">' % (name, content)
    if name not in self.__cols:
      self.__cols.append(name)
    return self

  def __str__(self):
    h = []
    for col in self.__cols:
      if self._metas.get(col) is not None:
        h.append(self._metas.get(col))
    return "\n".join(h)


class Links:

  def __init__(self, header):
    self.__header = header

  def icon(self, href, crossorigin=False):
    """
    Description:
    ------------
    Defines a resource for representing the page in the user interface, usually an icon (auditory or visual).
    In the browser, it is usually referred to as the favicon.

    If there are multiple <link rel="icon">s, the browser uses their media, type, and sizes attributes to select
    the most appropriate icon.
    If several icons are equally appropriate, the last one is used.
    If the most appropriate icon is later found to be inappropriate, for example because it uses an unsupported format,
    the browser proceeds to the next-most appropriate, and so on.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param crossorigin: Boolean. Optional. Specify to the browser to enable the cross origin to get resource from different website.
    """
    self.stylesheet(href=href, file_type="", media=None, rel="icon", crossorigin=crossorigin)

  def pingback(self, href, crossorigin=False):
    """
    Description:
    ------------
    Pingbacks (also known as trackbacks) are a form of automated comment for a page or post,
    created when another WordPress blog links to that page or post.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://wordpress.stackexchange.com/questions/116079/what-is-rel-pingback-and-what-is-the-use-of-this-in-my-website

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param crossorigin: Boolean. Optional. Specify to the browser to enable the cross origin to get resource from different website.
    """
    self.stylesheet(href=href, file_type="", media=None, rel="pingback", crossorigin=crossorigin)

  def shortlink(self, href):
    """
    Description:
    ------------
    Some websites create short links to make sharing links via instant messaging easier.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints

    Attributes:
    ----------
    :param href: String. The url path.
    """
    self.stylesheet(href=href, file_type="", media=None, rel="shortlink", crossorigin=False)

  def preload(self, href, file_type="", media=None, crossorigin=False):
    """
    Description:
    ------------
    The preload keyword for the rel attribute of the <link> element indicates the user is highly likely to require
    the target resource for the current navigation, and therefore the browser must preemptively fetch and cache
    the resource.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preload

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param file_type: String. Optional. The type of the href tag.
    :param media: String. Optional. This resource will then only be loaded if the media condition is true.
    :param crossorigin: Boolean. Optional. Specify to the browser to enable the cross origin to get resource from different website.
    """
    self.stylesheet(href=href, file_type=file_type, media=media, rel="preload", crossorigin=crossorigin)

  def prefetch(self, href, media=None, crossorigin=False):
    """
    Description:
    ------------
    The prefetch keyword for the rel attribute of the <link> element is a hint to browsers that the user is likely to
    need the target resource for future navigations, and therefore the browser can likely improve the user experience
    by preemptively fetching and caching the resource.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/prefetch


    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param media: String. Optional. This resource will then only be loaded if the media condition is true.
    :param crossorigin: Boolean. Optional. Specify to the browser to enable the cross origin to get resource from different website.
    """
    self.stylesheet(href=href, file_type=media, media=media, rel="prefetch", crossorigin=crossorigin)

  def dns_prefetch(self, href, media=None, crossorigin=False):
    """
    Description:
    ------------
    The dns-prefetch keyword for the rel attribute of the <link> element is a hint to browsers that the user is likely
    to need resources from the target resource's origin, and therefore the browser can likely improve the user
    experience by preemptively performing DNS resolution for that origin.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/dns-prefetch

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param media: String. Optional. This resource will then only be loaded if the media condition is true.
    :param crossorigin: Boolean. Optional. Specify to the browser to enable the cross origin to get resource from different website.
    """
    self.stylesheet(href=href, file_type="", media=media, rel="dns-prefetch", crossorigin=crossorigin)

  def prerender(self, href, media=None, crossorigin=False):
    """
    Description:
    ------------
    The prerender keyword for the rel attribute of the <link> element is a hint to browsers that the user might need
    the target resource for the next navigation, and therefore the browser can likely improve the user experience
    by preemptively fetching and processing the resource — for example, by fetching its subresources or performing
    some rendering in the background offscreen.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/prerender

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param media: String. Optional. This resource will then only be loaded if the media condition is true.
    :param crossorigin: Boolean. Optional. Specify to the browser to enable the cross origin to get resource from different website.
    """
    self.stylesheet(href=href, file_type="", media=media, rel="prerender", crossorigin=crossorigin)

  def preconnect(self, href, media=None, crossorigin=False):
    """
    Description:
    ------------
    The preconnect directive allows the browser to setup early connections before an HTTP request is actually sent
    to the server.
    This includes DNS lookups, TLS negotiations, TCP handshakes.
    This in turn eliminates roundtrip latency and saves time for users.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preconnect

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param media: String. Optional. This resource will then only be loaded if the media condition is true.
    :param crossorigin: Boolean. Optional. Specify to the browser to enable the cross origin to get resource from different website.
    """
    self.stylesheet(href=href, file_type="", media=media, rel="preconnect", crossorigin=crossorigin)

  def imports(self, href, file_type="", media=None, rel="import"):
    """
    Description:
    ------------
    HTML Imports is intended to be the packaging mechanism for web components, but you can also use HTML Imports by
    itself.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/Web_Components/HTML_Imports

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param file_type: String. Optional. The type of the href tag.
    :param media: String. Optional. This resource will then only be loaded if the media condition is true.
    :param rel: String. Optional. This attribute names a relationship of the linked document to the current document.
    """
    self.stylesheet(href, file_type, media, rel)

  def manifest(self, href, file_type="", media=None):
    """
    Description:
    ------------
    The manifest keyword for the rel attribute of the <link> element indicates that the target resource is a Web app
    manifest.

    Web app manifests are deployed in your HTML pages using a <link> element in the <head> of a document:

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/manifest
      https://developer.mozilla.org/en-US/docs/Web/Manifest

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param file_type: String. Optional. The type of the href tag.
    :param media: String. Optional. This resource will then only be loaded if the media condition is true.
    """
    if not href.endswith(".json"):
      raise Exception("Manifest file should be a json file")

    self.stylesheet(href, file_type, media, rel="manifest")

  def stylesheet(self, href, file_type="text/css", media=None, rel="stylesheet", crossorigin=False):
    """
    Description:
    ------------
    Link the page to a style sheet.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param file_type: String. Optional. The type of the href tag.
    :param media: String. Optional. This resource will then only be loaded if the media condition is true.
    :param rel: String. Optional. This attribute names a relationship of the linked document to the current document.
    :param crossorigin: Boolean. Optional. Specify to the browser to enable the cross origin to get resource from different website.
    """
    if isinstance(href, list):
      self.__header._links.append({"href": href[0], "rel": rel})
      for h in href[1:]:
        self.alternative(h, file_type=file_type, media=media)
    else:
      for header in self.__header._links:
        if header["href"] == href:
          return

      self.__header._links.append({"href": href, "rel": rel, "crossorigin": crossorigin})
    if file_type:
      self.__header._links[-1]["type"] = file_type
    if media is not None:
      self.__header._links[-1]["media"] = media

  def alternative(self, href, file_type="text/css", media=None):
    """
    Description:
    ------------
    Specifying alternative style sheets in a web page provides a way for users to see multiple versions of a page,
    based on their needs or preferences.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link

    Attributes:
    ----------
    :param href: String. The link path for the stylesheet page.
    :param file_type: String. Optional. The type of the href tag.
    :param media: String. Optional. This resource will then only be loaded if the media condition is true.
    """
    self.__header._links.append({"href": href, "rel": "alternate stylesheet"})
    if file_type is not None:
      self.__header._links["type"] = file_type
    if media is not None:
      self.__header._links["media"] = media


class Icons:

  def __init__(self, header):
    self.__header = header

  def icon(self, url, sizes=None, img_type=None):
    """
    Description:
    ------------
    Set the icon for the page.

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

    Attributes:
    ----------
    :param url: String. The url of the icon on the server.
    :param sizes: String. Optional. The size of the icon.
    :param img_type: String. Optional. The type of picture.
    """
    self.__header.favicon(url, rel="icon", sizes=sizes, img_type=img_type)
    return self.__header

  def gif(self, url, sizes=None):
    """
    Description:
    ------------


    Related Pages:

      https://www.w3schools.com/tags/att_link_sizes.asp

    Attributes:
    ----------
    :param url: String. The path for the gif.
    :param sizes: String. Optional. The size in a format 25x25.
    """
    self.__header.favicon(url, rel="icon", sizes=sizes, img_type="image/gif")
    return self.__header

  def svg(self, url, sizes=None):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/tags/att_link_sizes.asp

    Attributes:
    ----------
    :param url: String. The path for the svg file.
    :param sizes: String. Optional. The size for 25x25.
    """
    self.__header.favicon(url, rel="icon", sizes=sizes, img_type="image/svg+xml")
    return self.__header

  def apple_touch_icon(self, url, sizes=None):
    """
    Description:
    ------------


    Related Pages:

      https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html#//apple_ref/doc/uid/TP40002051-CH3-SW4

    Attributes:
    ----------
    :param url: String. The path for the svg file.
    :param sizes: String. Optional. The size for 25x25.
    """
    self.__header.favicon(url, rel="apple-touch-icon", sizes=sizes)
    return self.__header

  def apple_touch_startup_icon(self, url, sizes=None):
    """
    Description:
    ------------


    Related Pages:

      https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html#//apple_ref/doc/uid/TP40002051-CH3-SW4

    Attributes:
    ----------
    :param url: String. The path for the svg file.
    :param sizes: String. Optional. The size for 25x25.
    """
    self.__header.favicon(url, rel="apple-touch-startup-image", sizes=sizes)
    return self.__header


class Header:

  # Internal mapping to deduce the corresponding type mime for the item.
  mime_mapping = {
    ".ico": "image/x-icon",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".gif": "image/gif",
    ".bmp": "image/bmp",
    ".webp": "image/webp",
    ".tif": "image/tiff",
    ".tiff": "image/tiff",
    ".png": "image/png",
    ".svg": "image/svg+xml",
  }

  def __init__(self, report=None):
    self._headers, self._links, self._styles, self._scripts, self._base, self.__meta = {}, [], [], [], None, None
    self._favicon_url = {}
    self.favicon(Defaults.FAVICON_URL)
    self._report = report
    if report is not None:
      self._report._props["header"] = self._headers

  def dev(self, icon=None):
    """
    Description:
    ------------
    Change the tab icon to highlight this page is still in dev mode.

    Usage::

      page = Report()
      page.headers.dev()

    Attributes:
    ----------
    :param icon: String. Optional. The url path of the icon.
    """
    self.favicon(icon or Defaults.FAVICON_DEV_URL)

  @property
  def meta(self):
    """
    Description:
    ------------
    Property to the Meta data dictionary for the HTML page.

    Metadata is data (information) about data.

    The <meta> tag provides metadata about the HTML document.
    Metadata will not be displayed on the page, but will be machine parsable.

    Usage::

      page.headers.meta

    Related Pages:

      https://www.w3schools.com/tags/tag_meta.asp

    :rtype: Meta
    """
    if self.__meta is None:
      self.__meta = Meta(self._report)
    return self.__meta

  def addScripts(self, src, attrs=None):
    """
    Description:
    -----------
    Add a JavaScript tag to th eHTML page.

    The script will be added in a script tag.

    Attributes:
    ----------
    :param src: String. The script path added to the page.
    :param attrs: Dictionary. optional. The various attributes to be added to the script tag.
    """
    attr_list = []
    if attrs is not None:
      for k, v in attrs.items():
        attr_list.append('%s="%s"' % (k, v))
    self._scripts.append('<script src="%s" %s></script>' % (src, ' '.join(attr_list)))

  def title(self, value):
    """
    Description:
    ------------
    The <title> tag is required in all HTML documents and it defines the title of the document.

    You can NOT have more than one <title> element in an HTML document.

    Usage::

      page.headers.title("title")

    Related Pages:

      https://www.w3schools.com/tags/tag_title.asp

    Attributes:
    ----------
    :param value: String. The title value for the page.
    """
    self._headers['title'] = value
    return self

  def base(self, url):
    """
    Description:
    ------------
    Specify a dedicated path for the relative paths in the page.

    Basically the images will use this path as base if present in the page.

    Related Pages:

      https://www.w3schools.com/tags/tag_base.asp

    Attributes:
    ----------
    :param url: String. The url path.
    """
    self._base = url
    return self

  def favicon(self, url, rel="icon", sizes=None, img_type=None):
    """
    Description:
    ------------
    The <link> tag defines a link between a document and an external resource.

    The <link> tag is used to link to external style sheets.

    Usage::

      rptObj.headers.favicon('https://github.com/favicon.ico')

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/HTML/Element/link
      https://www.w3schools.com/tags/tag_link.asp

    Attributes:
    ----------
    :param url: String. The url full path.
    :param rel: String. Optional.
    :param sizes: String. Optional.
    :param img_type: String. Optional.
    """
    extension = url.split(".")[-1].lower()
    if ".%s" % extension in self.mime_mapping:
      img_type = self.mime_mapping[".%s" % extension]
    elif self._report is not None:
      if self._report.verbose:
        logging.warning("Favicon - Missing extension %s - No default used" % extension)
    else:
      logging.warning("Favicon - Missing extension %s - No default used" % extension)
    self._favicon_url[rel] = {"href": url, "rel": rel}
    if img_type is not None:
      self._favicon_url[rel]["type"] = img_type
    if sizes is not None:
      self._favicon_url[rel]["sizes"] = sizes
    return self

  @property
  def links(self):
    """
    Description:
    ------------
    The various HTML page header links.

    Related Pages:

      https://www.w3schools.com/jsref/dom_obj_link.asp
      https://developer.mozilla.org/fr/docs/Web/HTML/Element/link
    """
    return Links(self)

  @property
  def icons(self):
    """
    Description:
    ------------
    Property to defined / add more icons to the page header.
    Some browsers (like Safari or Opera) could require specify tags in the page.
    """
    return Icons(self)

  def __str__(self):
    result = [str(self.meta)]
    if self._headers.get("title") is not None:
      result.append("<title>%s</title>" % self._headers.get("title"))
    for rel, rel_attrs in self._favicon_url.items():
      result.append("<link %s>" % " ".join(["%s='%s'" % (k, v) for k, v in rel_attrs.items()]))
    for link in self._links:
      if "media" in link:
        result.append("<link rel='%(rel)s' type='%(type)s' href='%(href)s' media='%(media)s'>" % link)
      else:
        result.append("<link rel='%(rel)s' type='%(type)s' href='%(href)s'>" % link)
    result.extend(self._scripts)
    return "\n".join(result)
