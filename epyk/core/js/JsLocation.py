"""
The location object contains information about the current URL.

The location object is part of the window object and is accessed through the window.location property.

Documentation:
https://www.w3schools.com/jsref/obj_location.asp

"""

from epyk.core.js import JsUtils

# All the predefined variable types
from epyk.core.js.fncs import JsFncs
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString


class JsLocation(object):
  @property
  def hostname(self):
    """
    The hostname property sets or returns the hostname of a URL.

    Example
    rptObj.location.hostname

    Documentation:
    https://www.w3schools.com/jsref/obj_location.asp

    :return: Return the hostname property
    """
    return JsString.JsString("location.hostname", isPyData=False)

  @property
  def pathname(self):
    """
    The hostname property sets or returns the hostname of a URL.

    Example
    jsObj.location.pathname

    Documentation:
    https://www.w3schools.com/jsref/obj_location.asp

    :return: Return the pathname property
    """
    return JsString.JsString("location.pathname", isPyData=False)

  @property
  def host(self):
    """
    The host property sets or returns the hostname and port of a URL.

    Example
    jsObj.location.host

    Documentation:
    https://www.w3schools.com/jsref/prop_loc_host.asp

    :return: Return the hostname and port of the current URL
    """
    return JsString.JsString("location.host", isPyData=False)

  @property
  def hash(self):
    """
    The hash property sets or returns the anchor part of a URL, including the hash sign (#)

    Example
    jsObj.location.hash

    Documentation:
    https://www.w3schools.com/jsref/prop_loc_hash.asp

    :return: A String, representing the anchor part of the URL, including the hash sign (#)
    """
    return JsObject.JsObject("location.hash", isPyData=False)

  @property
  def search(self):
    """
    The search property sets or returns the querystring part of a URL, including the question mark (?).

    Documentation:
    https://www.w3schools.com/jsref/prop_loc_search.asp

    :return: A String, representing the querystring part of a URL, including the question mark (?)
    """
    return JsString.JsString("location.search", isPyData=False)

  @property
  def port(self):
    """
    The port property sets or returns the port number the server uses for a URL.

    Documentation:
    https://www.w3schools.com/jsref/prop_loc_port.asp

    :return: A String, representing the port number of a URL.
    """
    return JsString.JsString("location.port", isPyData=False)

  @property
  def origin(self):
    """
    The origin property returns the protocol, hostname and port number of a URL.

    Example
    rptObj.js.location.origin + rptObj.js.location.pathname

    Documentation:
    https://www.w3schools.com/jsref/prop_loc_origin.asp

    :return: A String, representing the protocol (including ://), the domain name (or IP address) and port number (including the colon sign (:) of the URL.
             For URL's using the "file:" protocol, the return value differs between browser
    """
    return JsString.JsString("location.origin", isPyData=False)

  def href(self, href=None, secured=False):
    """
    The href property sets or returns the entire URL of the current p

    Example
    rptObj.js.location.href("https://www.w3schools.com/howto/howto_js_fullscreen.asp")

    Documentation
    https://www.w3schools.com/jsref/prop_loc_href.asp

    :param href: Set the href property

    :return: A String, representing the entire URL of the page, including the protocol (like http://)
    """
    if href is None:
      return JsString.JsString("location.href", isPyData=False)

    if href.startswith("www."):
      href = r"http:\\%s" % href if not secured else r"https:\\%s" % href
    return JsObject.JsObject("location.href = %s" % JsUtils.jsConvertData(href, None))

  def open_new_tab(self, url, name="_blank", specs=None, replace=None, windowId="window", secured=False):
    """
    Opens a new browser window in a new tab (duplicated but part of the Window module)

    Example
    rptObj.js.location.open_new_tab("www.google.fr")

    Documentation
    https://www.w3schools.com/Jsref/met_win_open.asp

    :param url: Optional. Specifies the URL of the page to open. If no URL is specified, a new window/tab with about:blank is opened
    :param name: Optional. Specifies the target attribute or the name of the window. Default _blank
    :param specs: Optional. A comma-separated list of items, no whitespaces.
    :param replace: Optional. Specifies whether the URL creates a new entry or replaces the current entry in the history list
    :param windowId: The JavaScript window object

    :return:
    """
    if url.startswith("www."):
      url = r"http:\\%s" % url if not secured else r"https:\\%s" % url
    url = JsUtils.jsConvertData(url, None)
    name = JsUtils.jsConvertData(name, None)
    specs = JsUtils.jsConvertData(specs, None)
    replace = JsUtils.jsConvertData(replace, None)
    return JsFncs.JsFunction("%s.open(%s, %s, %s, %s)" % (windowId, url, name, specs, replace))

  def mail(self, mails, subject, body):
    """
    The mailto link when clicked opens users default email program or software. A new email page is created with "To" field containing the address of the name specified on the link by default.

    Example
    rptObj.js.location.mail(["test@gmail.com"], "This is a test", "This is the email's content")

    Documentation
    http://www.tutorialspark.com/html5/HTML5_email_mailto.php

    :param mails: A list of email addresses
    :param subject: The email's subject
    :param body: The email's content

    :return: THe Javascript string
    """
    if isinstance(mails, list):
      mails = ";".join(mails)
    return self.href(JsString.JsString("'mailto:%s?subject=%s&body='+ encodeURIComponent('%s')" % (mails, subject, body), isPyData=False))

  def reload(self, forceGet=False):
    """
    The reload() method is used to reload the current document.

    The reload() method does the same as the reload button in your browser.

    Documentation:
    https://www.w3schools.com/jsref/met_loc_reload.asp

    :param forceGet: Optional. Specifies the type of reloading:
          false - Default. Reloads the current page from the cache.
          true - Reloads the current page from the server

    :return: Void
    """
    forceGet = JsUtils.jsConvertData(forceGet, None)
    return JsFncs.JsFunction("location.reload(%s)" % forceGet)

  def assign(self, url):
    """
    The assign() method loads a new document.

    Documentation:
    https://www.w3schools.com/jsref/met_loc_assign.asp

    :param url: Required. Specifies the URL of the page to navigate to

    :return: Void
    """
    jsData = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunction("location.assign(%s)" % jsData)

  def replace(self, url, secured=False):
    """
    The replace() method replaces the current document with a new one.

    The difference between this method and assign(), is that replace() removes the URL of the current document from the document history, meaning that it is not possible to use the "back" button to navigate back to the original document.

    Documentation:
    https://www.w3schools.com/jsref/met_loc_replace.asp

    :param url: Required. Specifies the URL of the page to navigate to
    :param secured: Optional. If the http is missing. This will be used to fix the url

    :return: Void
    """
    if url.startswith("www."):
      url = r"http:\\%s" % url if not secured else r"https:\\%s" % url
    js_data = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunction("location.replace(%s)" % js_data)

  def postTo(self, url, data, method="POST", target="_blank"):
    """
    This method will create a internal form and submit the response exactly like a post of a form to another page

    Documentation
    https://www.w3schools.com/jsref/dom_obj_form.asp

    :param url: The target url
    :param data: A python dictionary
    :param method: Optional. The method used to send the data. Default POST

    """
    inputs = []
    for k, v in data.items():
      jsVal = JsUtils.jsConvertData(v, None)
      inputs.append('var input = document.createElement("input"); input.name = "%s"; input.type = "hidden"; input.value = %s; form.appendChild(input);' % (k, jsVal))
    return ''' 
      var form = document.createElement("form"); form.method = "%s"; form.target = "%s"; form.action = "%s"; %s;
      document.body.appendChild(form); form.submit()''' % (method, target, url, "".join(inputs))
