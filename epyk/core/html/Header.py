#!/usr/bin/python
# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Union, Optional
from epyk.core.py import primitives
from epyk.core.py import PyRest
import base64
import logging
import os

from epyk.core.html import Defaults


class Meta:
  def __init__(self, page: primitives.PageModel):
    self.page = page
    self._metas = {}
    self.__cols = ['charset', 'viewport']
    self.viewport().charset()
    self.http_equiv("X-UA-Compatible", "IE=EDGE").http_equiv("Content-Type", "text/html; charset=utf-8")
    self.http_equiv("Cache-control", "no-cache")

  def viewport(self, attrs: Optional[dict] = None):
    """
    Setting the viewport to make your website look good on all devices.

    Usage::

      page.headers.meta.viewport({"width": "device-width"})

    Related Pages:

      https://www.w3schools.com/html/html_head.asp
      https://www.w3schools.com/tags/tag_meta.asp

    :param attrs: Optional. The view port attributes
    """
    dfl_attrs = {"width": "device-width", "height": "device-height", "initial-scale": "1.0"}
    if attrs is not None:
      dfl_attrs.update(attrs)
    self._metas["viewport"] = '<meta name="viewport" content="%s">' % ", ".join(
      ["%s=%s" % (k, v) for k, v in dfl_attrs.items()])
    return self

  def charset(self, value: str = "utf-8"):
    """
    Define the character set used.

    Usage::

      page.headers.meta.charset("test")

    Related Pages:

      https://www.w3schools.com/tags/tag_meta.asp
      https://www.w3schools.com/tags/att_meta_charset.asp

    :param value: Optional. The charset encoding
    """
    common_vals = ("UTF-8", "ISO-8859-1")
    if self.page.verbose and value.upper() not in common_vals:
      logging.warning("Charset value %s not in common ones %s" % (value, common_vals))

    self._metas["charset"] = '<meta charset="%s">' % value
    return self

  def refresh(self, time: int):
    """
    Refresh document every X seconds.

    Usage::

      page.headers.meta.refresh(10)

    Related Pages:

      https://www.w3schools.com/tags/tag_meta.asp

    :param time: A time in second
    """
    self._metas["refresh"] = '<meta http-equiv="refresh" content="%s">' % time
    if "refresh" not in self.__cols:
      self.__cols.append("refresh")
    return self

  def author(self, name: str):
    """
    Define the author of the page.

    Usage::

      page.headers.meta.author('epykure')

    Related Pages:

      https://www.w3schools.com/tags/att_meta_name.asp

    :param name: The author name
    """
    self._metas["author"] = '<meta name="author" content="%s">' % name
    if "author" not in self.__cols:
      self.__cols.append("author")
    return self

  def description(self, value: str):
    """
    Define a description of your web page.

    Usage::

      page.headers.meta.description('This is a description')

    Related Pages:

      https://www.w3schools.com/html/html_head.asp

    :param value: The report description
    """
    self._metas["description"] = '<meta name="description" content="%s">' % value
    if "description" not in self.__cols:
      self.__cols.append("description")
    return self

  def keywords(self, content: Union[list, str]):
    """
    Define keywords for search engine.

    Usage::

      page.headers.meta.keywords(['python', 'javascript'])

    Related Pages:

      https://www.w3schools.com/html/html_head.asp

    :param content: The keyword data
    """
    if isinstance(content, list):
      content = ",".join(content)
    self._metas["keywords"] = '<meta name="keywords" content="%s">' % content
    if "keywords" not in self.__cols:
      self.__cols.append("keywords")
    return self

  def custom(self, name: str, content: str):
    """
    Bespoke function to add other meta tags.

    Usage::

      page.headers.meta.custom('language', 'python')

    Related Pages:

      https://www.w3schools.com/tags/att_meta_name.asp

    :param name: The name for the meta tag
    :param content: The value of the meta tag
    """
    self._metas[name] = '<meta name="%s" content="%s">' % (name, content)
    if name not in self.__cols:
      self.__cols.append(name)
    return self

  def add(self, **kwargs):
    """Add a bespoke meta HTML tag to the page.

    Usage::
      page.headers.meta.add(http_equiv="Page-Enter", content="RevealTrans(Duration=2.0,Transition=2)")
      page.headers.meta.add(data_rh="true", name="twitter:site", content="@Epyk")

    `Documentation <https://gist.github.com/lancejpollard/1978404>`_

    :param kwargs: The value of the attribute you want to add
    """
    attrs = " ".join(['%s="%s"' % (k.replace("_", "-"), v) for k, v in kwargs.items()])
    self._metas[attrs] = '<meta %s>' % attrs
    if attrs not in self.__cols:
      self.__cols.append(attrs)
    return self

  def http_equiv(self, name: str, content: str):
    """
    Bespoke function to add other http-equiv tags to the meta section.

    Usage::

      rptObj.headers.meta.http_equiv('language', 'python')

    Related Pages:

      https://www.w3schools.com/tags/att_meta_http_equiv.asp

    :param name: The name for the meta tag
    :param content: The value of the meta tag
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

  def icon(self, href: str, cross_origin: bool = False):
    """
    Defines a resource for representing the page in the user interface, usually an icon (auditory or visual).
    In the browser, it is usually referred to as the favicon.

    If there are multiple <link rel="icon">s, the browser uses their media, type, and sizes attributes to select
    the most appropriate icon.
    If several icons are equally appropriate, the last one is used.
    If the most appropriate icon is later found to be inappropriate, for example because it uses an unsupported format,
    the browser proceeds to the next-most appropriate, and so on.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types

    :param href: The link path for the stylesheet page
    :param cross_origin: Optional. Specify to the browser to enable the cross origin to get resource from different
    website.
    """
    self.stylesheet(href=href, file_type="", media=None, rel="icon", cross_origin=cross_origin)

  def pingback(self, href: str, cross_origin: bool = False):
    """
    Pingbacks (also known as trackbacks) are a form of automated comment for a page or post,
    created when another WordPress blog links to that page or post.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://wordpress.stackexchange.com/questions/116079/what-is-rel-pingback-and-what-is-the-use-of-this-in-my-website

    :param href: The link path for the stylesheet page
    :param cross_origin: Optional. Specify to the browser to enable the cross origin to get resource from
    different website.
    """
    self.stylesheet(href=href, file_type="", media=None, rel="pingback", cross_origin=cross_origin)

  def shortlink(self, href: str):
    """
    Some websites create short links to make sharing links via instant messaging easier.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints

    :param href: The url path
    """
    self.stylesheet(href=href, file_type="", media=None, rel="shortlink", cross_origin=False)

  def preload(self, href: str, file_type: str = "", media: Optional[str] = None, cross_origin: bool = False):
    """
    The preload keyword for the rel attribute of the <link> element indicates the user is highly likely to require
    the target resource for the current navigation, and therefore the browser must preemptively fetch and cache
    the resource.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preload

    :param href: The link path for the stylesheet page
    :param file_type: Optional. The type of the href tag
    :param media: Optional. This resource will then only be loaded if the media condition is true
    :param cross_origin: Optional. Specify to the browser to enable the cross origin to get resource from
      different website.
    """
    self.stylesheet(href=href, file_type=file_type, media=media, rel="preload", cross_origin=cross_origin)

  def prefetch(self, href: str, media: Optional[str] = None, cross_origin: bool = False):
    """
    The prefetch keyword for the rel attribute of the <link> element is a hint to browsers that the user is likely to
    need the target resource for future navigations, and therefore the browser can likely improve the user experience
    by preemptively fetching and caching the resource.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/prefetch

    :param href: The link path for the stylesheet page
    :param media: Optional. This resource will then only be loaded if the media condition is true
    :param cross_origin: Optional. Specify to the browser to enable the cross origin to get resource from
      different website.
    """
    self.stylesheet(href=href, file_type=media, media=media, rel="prefetch", cross_origin=cross_origin)

  def dns_prefetch(self, href: str, media: Optional[str] = None, cross_origin: bool = False):
    """
    The dns-prefetch keyword for the rel attribute of the <link> element is a hint to browsers that the user is likely
    to need resources from the target resource's origin, and therefore the browser can likely improve the user
    experience by preemptively performing DNS resolution for that origin.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/dns-prefetch

    :param href: The link path for the stylesheet page
    :param media: Optional. This resource will then only be loaded if the media condition is true
    :param cross_origin: Optional. Specify to the browser to enable the cross origin to get resource from
      different website.
    """
    self.stylesheet(href=href, file_type="", media=media, rel="dns-prefetch", cross_origin=cross_origin)

  def prerender(self, href: str, media: Optional[str] = None, cross_origin: bool = False):
    """
    The prerender keyword for the rel attribute of the <link> element is a hint to browsers that the user might need
    the target resource for the next navigation, and therefore the browser can likely improve the user experience
    by preemptively fetching and processing the resource — for example, by fetching its subresources or performing
    some rendering in the background offscreen.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/prerender

    :param href: The link path for the stylesheet page
    :param media: Optional. This resource will then only be loaded if the media condition is true
    :param cross_origin: Optional. Specify to the browser to enable the cross origin to get resource from
      different website.
    """
    self.stylesheet(href=href, file_type="", media=media, rel="prerender", cross_origin=cross_origin)

  def preconnect(self, href: str, media: Optional[str] = None, cross_origin: bool = False):
    """
    The preconnect directive allows the browser to setup early connections before an HTTP request is actually sent
    to the server.
    This includes DNS lookups, TLS negotiations, TCP handshakes.
    This in turn eliminates roundtrip latency and saves time for users.

    Related Pages:

      https://www.keycdn.com/blog/resource-hints
      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preconnect

    :param href: The link path for the stylesheet page
    :param media: Optional. This resource will then only be loaded if the media condition is true
    :param cross_origin: Optional. Specify to the browser to enable the cross origin to get resource from
      different website.
    """
    self.stylesheet(href=href, file_type="", media=media, rel="preconnect", cross_origin=cross_origin)

  def imports(self, href: str, file_type: str = "", media: Optional[str] = None, rel: str = "import"):
    """
    HTML Imports is intended to be the packaging mechanism for web components, but you can also use HTML Imports by
    itself.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/Web_Components/HTML_Imports

    :param href: The link path for the stylesheet page
    :param file_type: Optional. The type of the href tag
    :param media: Optional. This resource will then only be loaded if the media condition is true
    :param rel: Optional. This attribute names a relationship of the linked document to the current document
    """
    self.stylesheet(href, file_type, media, rel)

  def manifest(self, href: str, file_type: str = "", media: Optional[str] = None):
    """
    The manifest keyword for the rel attribute of the <link> element indicates that the target resource is a Web app
    manifest.

    Web app manifests are deployed in your HTML pages using a <link> element in the <head> of a document:

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/manifest
      https://developer.mozilla.org/en-US/docs/Web/Manifest

    :param href: The link path for the stylesheet page
    :param file_type: Optional. The type of the href tag
    :param media: Optional. This resource will then only be loaded if the media condition is true
    """
    if not href.endswith(".json"):
      raise ValueError("Manifest file should be a json file")

    self.stylesheet(href, file_type, media, rel="manifest")

  def stylesheet(self, href: str, file_type: str = "text/css", media: Optional[str] = None, rel: str = "stylesheet",
                 cross_origin: bool = False, title: str = ""):
    """
    Link the page to a style sheet.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link

    :param href: The link path for the stylesheet page
    :param file_type: Optional. The type of the href tag
    :param media: Optional. This resource will then only be loaded if the media condition is true
    :param rel: Optional. This attribute names a relationship of the linked document to the current document
    :param cross_origin: Optional. Specify to the browser to enable the cross-origin to get resource from
      different website.
    :param title: File description
    """
    if isinstance(href, list):
      self.__header._links.append({"href": href[0], "rel": rel, "title": title})
      for h in href[1:]:
        self.alternative(h, file_type=file_type, media=media)
    else:
      for header in self.__header._links:
        if header["href"] == href:
          return

      self.__header._links.append({"href": href, "rel": rel, "crossorigin": cross_origin, "title": title})
    if file_type:
      self.__header._links[-1]["type"] = file_type
    if media is not None:
      self.__header._links[-1]["media"] = media

  def alternative(
          self, href: str, file_type: str = "text/css", media: Optional[str] = None, title: str = "alternate stylesheet"):
    """
    Specifying alternative style sheets in a web page provides a way for users to see multiple versions of a page,
    based on their needs or preferences.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link

    :param href: The link path for the stylesheet page
    :param file_type: Optional. The type of the href tag
    :param media: Optional. This resource will then only be loaded if the media condition is true
    :param dsc: Optional. File metadata description
    :param title: File description
    """
    self.__header._links.append({"href": href, "rel": "alternate stylesheet", "title": title})
    if file_type is not None:
      self.__header._links[-1]["type"] = file_type
    if media is not None:
      self.__header._links[-1]["media"] = media


class Icons:

  def __init__(self, header):
    self.__header = header

  def icon(self, url: str, sizes: Optional[str] = None, img_type: Optional[str] = None):
    """
    Set the icon for the page.

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

    :param url: The url of the icon on the server
    :param sizes: Optional. The size of the icon
    :param img_type: Optional. The type of picture
    """
    self.__header.favicon(url, rel="icon", sizes=sizes, img_type=img_type)
    return self.__header

  def gif(self, url: str, sizes: Optional[str] = None):
    """


    Related Pages:

      https://www.w3schools.com/tags/att_link_sizes.asp

    :param url: The path for the gif
    :param sizes: Optional. The size in a format 25x25
    """
    self.__header.favicon(url, rel="icon", sizes=sizes, img_type="image/gif")
    return self.__header

  def svg(self, url: str, sizes: Optional[str] = None):
    """

    Related Pages:

      https://www.w3schools.com/tags/att_link_sizes.asp

    :param url: The path for the svg file
    :param sizes: Optional. The size for 25x25
    """
    self.__header.favicon(url, rel="icon", sizes=sizes, img_type="image/svg+xml")
    return self.__header

  def apple_touch_icon(self, url: str, sizes: Optional[str] = None):
    """


    Related Pages:

      https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html#//apple_ref/doc/uid/TP40002051-CH3-SW4

    :param url: The path for the svg file
    :param sizes: Optional. The size for 25x25
    """
    self.__header.favicon(url, rel="apple-touch-icon", sizes=sizes)
    return self.__header

  def apple_touch_startup_icon(self, url: str, sizes: Optional[str] = None):
    """


    Related Pages:

      https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html#//apple_ref/doc/uid/TP40002051-CH3-SW4

    :param url: The path for the svg file
    :param sizes: Optional. The size for 25x25
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

  def __init__(self, page: Optional[primitives.PageModel] = None):
    self._headers, self._links, self._styles, self._scripts, self._base, self.__meta = {}, [], [], [], None, None
    self._favicon_url = {}
    self.page = page
    self.favicon(Defaults.FAVICON_URL)
    if page is not None:
      self.page._props["header"] = self._headers

  def dev(self, icon: Optional[str] = None):
    """
    Change the tab icon to highlight this page is still in dev mode.

    Usage::

      page = Report()
      page.headers.dev()

    :param icon: Optional. The url path of the icon
    """
    self.favicon(icon or Defaults.FAVICON_DEV_URL)

  @property
  def meta(self) -> Meta:
    """
    Property to the Meta data dictionary for the HTML page.

    Metadata is data (information) about data.

    The <meta> tag provides metadata about the HTML document.
    Metadata will not be displayed on the page, but will be machine parsable.

    Usage::

      page.headers.meta

    Related Pages:

      https://www.w3schools.com/tags/tag_meta.asp
    """
    if self.__meta is None:
      self.__meta = Meta(self.page)
    return self.__meta

  def add_script(self, src: str, attrs: Optional[dict] = None):
    """   Add a JavaScript tag to the HTML page.

    The script will be added in a script tag.

    :param src: The script path added to the page
    :param attrs: optional. The various attributes to be added to the script tag
    """
    attr_list = []
    if attrs is not None:
      for k, v in attrs.items():
        attr_list.append('%s="%s"' % (k, v))
    self._scripts.append('<script src="%s" %s></script>' % (src, ' '.join(attr_list)))

  def add_code(self, code: str, attrs: Optional[dict] = None):
    """   Add a JavaScript tag to the HTML page.

    The code will be added in a script tag.

    :param code: The JavaScript code to be added to the page
    :param attrs: optional. The various attributes to be added to the script tag
    """
    base64_bytes = base64.b64encode(code.encode('ascii'))
    base64_message = base64_bytes.decode('ascii')
    self.add_script("data:text/css;base64,%s" % base64_message, attrs)

  def title(self, value: str):
    """
    The <title> tag is required in all HTML documents and it defines the title of the document.

    You can NOT have more than one <title> element in an HTML document.

    Usage::

      page.headers.title("title")

    Related Pages:

      https://www.w3schools.com/tags/tag_title.asp

    :param value: The title value for the page
    """
    self._headers['title'] = value
    return self

  def base(self, url: str):
    """
    Specify a dedicated path for the relative paths in the page.

    Basically the images will use this path as base if present in the page.

    Related Pages:

      https://www.w3schools.com/tags/tag_base.asp

    :param url: The url path
    """
    self._base = url
    return self

  def favicon(self, url: str, rel: str = "icon", sizes: Optional[str] = None, img_type: Optional[str] = None):
    """
    The <link> tag defines a link between a document and an external resource.

    The <link> tag is used to link to external style sheets.

    Usage::

      rptObj.headers.favicon('https://github.com/favicon.ico')

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/HTML/Element/link
      https://www.w3schools.com/tags/tag_link.asp

    :param url: The url full path
    :param rel: Optional
    :param sizes: Optional
    :param img_type: Optional
    """
    from epyk.conf.global_settings import (ASSETS_SPLIT, ASSETS_STATIC_ROUTE, ASSETS_STATIC_PATH, ASSETS_STATIC_PUBLIC)

    if url in [
      'https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo.ico',
      'https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo_dev.ico',
    ]:
      icon_name = url.split("/")
      with open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "..", "..", "static", "images", icon_name[-1]), "rb") as fp:
        if ASSETS_SPLIT:
          public_file_path = Path(ASSETS_STATIC_PATH) / ASSETS_STATIC_PUBLIC
          if not public_file_path.exists():
            public_file_path.mkdir(parents=True, exist_ok=True)
          with open(public_file_path / icon_name[-1], "wb") as fw:
            fw.write(fp.read())
          url = "%s/%s/%s" % (ASSETS_STATIC_ROUTE, ASSETS_STATIC_PUBLIC, icon_name[-1])
        else:
          base64_bytes = base64.b64encode(fp.read())
          base64_message = base64_bytes.decode('ascii')
          url = "data:image/x-icon;base64,%s" % base64_message
    extension = url.split(".")[-1].lower()
    if ".%s" % extension in self.mime_mapping:
      img_type = self.mime_mapping[".%s" % extension]
    elif self.page is not None:
      if self.page.verbose:
        logging.warning("Favicon - Missing extension %s - No default used" % extension)
    else:
      logging.warning("Favicon - Missing extension %s - No default used" % extension)
    if self.page is not None and self.page.imports.self_contained:
      r = PyRest.PyRest(self.page)
      base64_bytes = base64.b64encode(r.request(url, encoding="ascii"))
      base64_message = base64_bytes.decode('ascii')
      url = "data:image/x-icon;base64,%s" % base64_message
    self._favicon_url[rel] = {"href": url, "rel": rel}
    if img_type is not None:
      self._favicon_url[rel]["type"] = img_type
    if sizes is not None:
      self._favicon_url[rel]["sizes"] = sizes
    return self

  @property
  def links(self):
    """
    The various HTML page header links.

    Related Pages:

      https://www.w3schools.com/jsref/dom_obj_link.asp
      https://developer.mozilla.org/fr/docs/Web/HTML/Element/link
    """
    return Links(self)

  @property
  def icons(self):
    """
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
      elif "title" in link:
        result.append("<link rel='%(rel)s' title='%(title)s' type='%(type)s' href='%(href)s'>" % link)
      else:
        result.append("<link rel='%(rel)s' type='%(type)s' href='%(href)s'>" % link)
    result.extend(self._scripts)
    return "\n".join(result)
