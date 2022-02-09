"""
The location object contains information about the current URL.

The location object is part of the window object and is accessed through the window.location property.

Related Pages:

      https//www.w3schools.com/jsref/obj_location.asp

"""

from typing import Any, Optional, List, Union
from epyk.core.py import primitives

from epyk.core.js import JsUtils

# All the predefined variable types
from epyk.core.js.fncs import JsFncs
from epyk.core.js.primitives import JsObjects
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString


class URLSearchParams:

  def __init__(self, query: str):
    self.query = query

  def get(self, key: str, default: Any = None):
    """
    Description:
    ------------
    Get the value of a request parameter in the url.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams

    Attributes:
    ----------
    :param str key: The url parameter.
    :param Any default: Optional. The default value.
    """
    key = JsUtils.jsConvertData(key, None)
    default = JsUtils.jsConvertData(default, None)
    return JsString.JsString.get(
      "(function(){var pmt = new URLSearchParams(%s).get(%s); if(pmt == null){ return %s } else { return pmt }})()" % (
        self.query, key, default))

  def getAll(self, key: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Get all the values of a request parameter in the url.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] key: The url parameter.
    """
    key = JsUtils.jsConvertData(key, None)
    return JsObject.JsObject.get("(function(){return new URLSearchParams(%s)})().getAll(%s)" % (self.query, key))

  def has(self, key: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Check if a given parameter is in the url.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] key: The url parameter.
    """
    key = JsUtils.jsConvertData(key, None)
    return JsObject.JsObject.get("(function(){return new URLSearchParams(%s)})().has(%s)" % (self.query, key))

  def append(self, key: Union[str, primitives.JsDataModel], value: Any):
    """
    Description:
    ------------
    Append a key, value to the url parameter object.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] key: The url parameter.
    :param Any value: The value to be appended to the URL.
    """
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    return JsObject.JsObject.get(
      "(function(){return new URLSearchParams(%s)})().append(%s, %s)" % (self.query, key, value))


class JsLocation:

  @property
  def hostname(self):
    """
    Description:
    ------------
    The hostname property sets or returns the hostname of a URL.

    Usage::

      page.location.hostname

    Related Pages:

      https//www.w3schools.com/jsref/obj_location.asp

    :return: Return the hostname property.
    """
    return JsString.JsString("location.hostname", is_py_data=False)

  @property
  def pathname(self):
    """
    Description:
    ------------
    The hostname property sets or returns the hostname of a URL.

    Usage::

      jsObj.location.pathname

    Related Pages:

      https//www.w3schools.com/jsref/obj_location.asp

    :return: Return the pathname property.
    """
    return JsString.JsString("location.pathname", is_py_data=False)

  @property
  def host(self):
    """
    Description:
    ------------
    The host property sets or returns the hostname and port of a URL.

    Usage::

      jsObj.location.host

    Related Pages:

      https//www.w3schools.com/jsref/prop_loc_host.asp

    :return: Return the hostname and port of the current URL.
    """
    return JsString.JsString("location.host", is_py_data=False)

  @property
  def hash(self):
    """
    Description:
    ------------
    The hash property sets or returns the anchor part of a URL, including the hash sign (#).

    Usage::

      jsObj.location.hash

    Related Pages:

      https//www.w3schools.com/jsref/prop_loc_hash.asp

    :return: A String, representing the anchor part of the URL, including the hash sign (#).
    """
    return JsObject.JsObject("location.hash", is_py_data=False)

  @property
  def search(self):
    """
    Description:
    ------------
    The search property sets or returns the querystring part of a URL, including the question mark (?).

    Related Pages:

      https//www.w3schools.com/jsref/prop_loc_search.asp

    :return: A String, representing the querystring part of a URL, including the question mark (?).
    """
    return JsString.JsString("location.search", is_py_data=False)

  @property
  def urlSearchParams(self):
    """
    Description:
    ------------
    The URLSearchParams() constructor creates and returns a new URLSearchParams object.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/URLSearchParams
    """
    return URLSearchParams("location.search")

  @property
  def port(self):
    """
    Description:
    ------------
    The port property sets or returns the port number the server uses for a URL.

    Related Pages:

      https//www.w3schools.com/jsref/prop_loc_port.asp

    :return: A String, representing the port number of a URL.
    """
    return JsString.JsString("location.port", is_py_data=False)

  @property
  def origin(self):
    """
    Description:
    ------------
    The origin property returns the protocol, hostname and port number of a URL.

    Usage::

      page.js.location.origin + rptObj.js.location.pathname

    Related Pages:

      https//www.w3schools.com/jsref/prop_loc_origin.asp

    :return: A String, representing the protocol (including ://), the domain name (or IP address) and port number
    (including the colon sign (:) of the URL. For URL's using the "file:" protocol, the return value differs
    between browser
    """
    return JsString.JsString("location.origin", is_py_data=False)

  def href(self, href: Union[str, primitives.JsDataModel] = None, secured: bool = False):
    """
    Description:
    ------------
    The href property sets or returns the entire URL of the current component.

    Usage::

      page.js.location.href("https://www.w3schools.com/howto/howto_js_fullscreen.asp")

    Related Pages:

      https://www.w3schools.com/jsref/prop_loc_href.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] href: Optional. Set the href property.
    :param bool secured: Optional.

    :return: A String, representing the entire URL of the page, including the protocol (like http://).
    """
    if href is None:
      return JsString.JsString("location.href", is_py_data=False)

    if not hasattr(href, 'toStr') and href.startswith("www."):
      href = r"http:\\%s" % href if not secured else r"https:\\%s" % href
    return JsObject.JsObject("location.href = %s" % JsUtils.jsConvertData(href, None))

  def open_new_tab(self, url: Union[str, primitives.JsDataModel], name: Union[str, primitives.JsDataModel] = "_blank",
                   specs: Union[str, primitives.JsDataModel] = None, replace: Union[str, primitives.JsDataModel] = None,
                   window_id: str = "window", secured: bool = False):
    """
    Description:
    ------------
    Opens a new browser window in a new tab (duplicated but part of the Window module).

    Usage::

      page.js.location.open_new_tab("www.google.fr")

    Related Pages:

      https://www.w3schools.com/Jsref/met_win_open.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] url: Optional. Specifies the URL of the page to open. If no URL is
    specified, a new window/tab with about:blank is opened
    :param Union[str, primitives.JsDataModel] name: Optional. Specifies the target attribute or the name of the window.
    Default _blank.
    :param Union[str, primitives.JsDataModel] specs: Optional. A comma-separated list of items, no whitespaces.
    :param Union[str, primitives.JsDataModel] replace: Optional. Specifies whether the URL creates a new entry or
    replaces the current entry in the history list
    :param str window_id: The JavaScript window object
    :param bool secured:
    """
    if not hasattr(url, 'toStr') and url.startswith("www."):
      url = r"http:\\%s" % url if not secured else r"https:\\%s" % url
    url = JsUtils.jsConvertData(url, None)
    name = JsUtils.jsConvertData(name, None)
    if specs is None:
      return JsFncs.JsFunction("%s.open(%s, %s)" % (window_id, url, name))

    specs = JsUtils.jsConvertData(specs, None)
    replace = JsUtils.jsConvertData(replace, None)
    return JsFncs.JsFunction("%s.open(%s, %s, %s, %s)" % (window_id, url, name, specs, replace))

  def download(self, url: Union[str, primitives.JsDataModel], name: Union[str, primitives.JsDataModel] = 'download'):
    """
    Description:
    ------------
    Download data from the url.

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] url: The url of the image.
    :param Union[str, primitives.JsDataModel] name: Optional. The name of the file.
    """
    url = JsUtils.jsConvertData(url, None)
    name = JsUtils.jsConvertData(name, None)
    return JsObjects.JsVoid('''
      var link = document.createElement('a'); document.body.appendChild(link);
      link.download = %(name)s; link.href = %(url)s; link.click(); link.remove()''' % {'name': name, 'url': url})

  def mail(self, mails: List[str], subject: str, body: str):
    """
    Description:
    ------------
    The mailto link when clicked opens users default email program or software.
    A new email page is created with "To" field containing the address of the name specified on the link by default.

    Usage::

      page.js.location.mail(["test@gmail.com"], "This is a test", "This is the email's content")

    Related Pages:

      http://www.tutorialspark.com/html5/HTML5_email_mailto.php

    Attributes:
    ----------
    :param list[str] mails: The email addresses.
    :param str subject: The email's subject.
    :param str body: The email's content.

    :return: THe Javascript string.
    """
    if isinstance(mails, list):
      mails = ";".join(mails)
    return self.href(JsString.JsString(
      "'mailto:%s?subject=%s&body='+ encodeURIComponent('%s')" % (mails, subject, body), is_py_data=False))

  def reload(self, force_get: bool = False):
    """
    Description:
    ------------
    The reload() method is used to reload the current document.

    The reload() method does the same as the reload button in your browser.

    Related Pages:

      https//www.w3schools.com/jsref/met_loc_reload.asp

    Attributes:
    ----------
    :param bool force_get: Optional. Specifies the type of reloading:
          false - Default. Reloads the current page from the cache.
          true - Reloads the current page from the server.
    """
    force_get = JsUtils.jsConvertData(force_get, None)
    return JsFncs.JsFunction("location.reload(%s)" % force_get)

  def assign(self, url: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    The assign() method loads a new document.

    Related Pages:

      https//www.w3schools.com/jsref/met_loc_assign.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] url: Specifies the URL of the page to navigate to.
    """
    data = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunction("location.assign(%s)" % data)

  def replace(self, url: Union[str, primitives.JsDataModel], secured: bool = False):
    """
    Description:
    ------------
    The replace() method replaces the current document with a new one.

    The difference between this method and assign(), is that replace() removes the URL of the current document
    from the document history, meaning that it is not possible to use the "back" button to navigate back to the
    original document.

    Related Pages:

      https//www.w3schools.com/jsref/met_loc_replace.asp

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] url: Specifies the URL of the page to navigate to.
    :param bool secured: Optional. If the http is missing. This will be used to fix the url.
    """
    if url.startswith("www."):
      url = r"http:\\%s" % url if not secured else r"https:\\%s" % url
    js_data = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunction("location.replace(%s)" % js_data)

  def postTo(self, url: str, data: dict, method: str = "POST", target: str = "_blank"):
    """
    Description:
    ------------
    This method will create an internal form and submit the response exactly like a post of a form to another page.

    Related Pages:

      https://www.w3schools.com/jsref/dom_obj_form.asp

    Attributes:
    ----------
    :param str url: The target url.
    :param dict data:
    :param str method: Optional. The method used to send the data. Default POST.
    :param str target: Optional.
    """
    inputs = []
    for k, v in data.items():
      js_val = JsUtils.jsConvertData(v, None)
      inputs.append('var input = document.createElement("input"); input.name = "%s"; input.type = "hidden"; input.value = %s; form.appendChild(input);' % (k, js_val))
    return ''' 
      var form = document.createElement("form"); form.method = "%s"; form.target = "%s"; form.action = "%s"; %s;
      document.body.appendChild(form); form.submit()''' % (method, target, url, "".join(inputs))

  def getUrlFromData(self, data: Union[dict, primitives.JsDataModel],
                     options: Optional[Union[dict, primitives.JsDataModel]] = None):
    """
    Description:
    ------------
    Convert data to a URL.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Blob

    Attributes:
    ----------
    :param Union[dict, primitives.JsDataModel] data: Input data to be converted.
    :param Optional[Union[dict, primitives.JsDataModel]] options: Optional. Blob definition properties.
    """
    data = JsUtils.jsConvertData(data, None)
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsObjects.JsObject.JsObject.get("window.URL.createObjectURL(new Blob([%s], %s))" % (data, options))

    return JsObjects.JsObject.JsObject.get("window.URL.createObjectURL(new Blob([%s]))" % data)

  def getUrlFromArrays(self, data: Union[list, primitives.JsDataModel],
                       options: Optional[Union[dict, primitives.JsDataModel]] = None):
    """
    Description:
    ------------
    Convert data to a URL.

    Attributes:
    ----------
    :param Union[list, primitives.JsDataModel] data: A JavaScript array.
    :param Optional[Union[dict, primitives.JsDataModel]] options: Optional. Blob definition properties.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObject.JsObject.get(r'''
      (function(data){let csvContent = "";
        data.forEach(function(rowArray){let row = rowArray.join(","); csvContent += row + "\r\n"});
        return 'data:text/csv;charset=utf-8,'+escape(csvContent)})(%s)''' % data)

