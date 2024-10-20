"""
The location object contains information about the current URL.

The location object is part of the window object and is accessed through the window.location property.

Related Pages:

      https//www.w3schools.com/jsref/obj_location.asp

"""

from typing import Any, Optional, List, Union
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js import JsGlobals

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
        Get the value of a request parameter in the url.

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams>`_

        :param key: The url parameter
        :param default: Optional. The default value
    """
        key = JsUtils.jsConvertData(key, None)
        default = JsUtils.jsConvertData(default, None)
        return JsString.JsString.get(
            "(function(){var pmt = new URLSearchParams(%s).get(%s); if(pmt == null){ return %s } else { return pmt }})()" % (
                self.query, key, default))

    def set(self, key: str, value: Any):
        """
        Set the value of a request parameter in the url.

        Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams>`_

        :param key: The url parameter
        :param value: The value to set
        """
        key = JsUtils.jsConvertData(key, None)
        value = JsUtils.jsConvertData(value, None)
        return JsString.JsString.get(
            "(function(){const urlParams = new URLSearchParams(%s); urlParams.set(%s, %s); window.location.search = urlParams})()" % (
                self.query, key, value))

    def add(self, component: primitives.HtmlModel):
        return self.set(component.html_code, component.dom.content)

    def getAll(self, key: Union[str, primitives.JsDataModel]):
        """
        Get all the values of a request parameter in the url.

        Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams>`_

        :param key: The url parameter
        """
        key = JsUtils.jsConvertData(key, None)
        return JsObject.JsObject.get("(function(){return new URLSearchParams(%s)})().getAll(%s)" % (self.query, key))

    def has(self, key: Union[str, primitives.JsDataModel]):
        """
        Check if a given parameter is in the url.

        Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams>`_

        :param key: The url parameter
        """
        key = JsUtils.jsConvertData(key, None)
        return JsObject.JsObject.get("(function(){return new URLSearchParams(%s)})().has(%s)" % (self.query, key))

    def append(self, key: Union[str, primitives.JsDataModel], value: Any):
        """
        Append a key, value to the url parameter object.

        Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams>`_

        :param key: The url parameter
        :param value: The value to be appended to the URL
        """
        key = JsUtils.jsConvertData(key, None)
        value = JsUtils.jsConvertData(value, None)
        return JsObject.JsObject.get(
            "(function(){return new URLSearchParams(%s)})().append(%s, %s)" % (self.query, key, value))

    def delete(self, key):
        """
        The delete() method of the URLSearchParams interface deletes the given search parameter and all its associated
        values, from the list of all search parameters.

        Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/delete>`_

        :param key:
        """
        key = JsUtils.jsConvertData(key, None)
        return JsString.JsString.get(
            "(function(){const urlParams = new URLSearchParams(%s); urlParams.delete(%s); window.location.search = urlParams})()" % (
                self.query, key))

    def all(self, stringify: bool = True) -> JsObject.JsObject:
        """Convert all url parameters to an object.

        :param stringify: For the object conversion to a String.
        """
        if stringify:
            return JsObject.JsObject.get("JSON.stringify(Object.fromEntries(new URLSearchParams(window.location.search)))")

        return JsObject.JsObject.get("Object.fromEntries(new URLSearchParams(window.location.search))")


class JsLocation:
    """  JavaScript Location module. """

    def __init__(self, page: primitives.PageModel = None):
        self.page = page

    def part(self, i: int, from_: str = None) -> JsString.JsString:
        """Extract a part of the current url.
        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/URL#Properties>`_

        Usage::
            ic = page.ui.icon("far fa-thumbs-up", text="0")
            ic.click(page.js.warnings([page.js.console.log(page.js.const("file"))])

        :param i: Position in the url to be extracted
        :param from_: Starting position in the url
        """
        if from_:
            from_ = JsUtils.jsConvertData(from_, None)
            return JsString.JsString.get("location.href.split('/' + %s + '/')[1].split('/')[%s]" % (from_, i))

        return JsString.JsString.get("(new URL(location.href).pathname).split( '/' )[%s]" % i)

    @property
    def hostname(self) -> JsString.JsString:
        """The hostname property sets or returns the hostname of a URL.
        `Related Pages <https//www.w3schools.com/jsref/obj_location.asp>`_

        Usage::
          page.location.hostname

        :return: Return the hostname property.
        """
        return JsString.JsString("location.hostname", is_py_data=False)

    @property
    def pathname(self) -> JsString.JsString:
        """The hostname property sets or returns the hostname of a URL.
        `Related Pages <https//www.w3schools.com/jsref/obj_location.asp>`_

        Usage::
          jsObj.location.pathname

        :return: Return the pathname property.
        """
        return JsString.JsString("location.pathname", is_py_data=False)

    @property
    def host(self) -> JsString.JsString:
        """The host property sets or returns the hostname and port of a URL.
        `Related Pages <https//www.w3schools.com/jsref/prop_loc_host.asp>`_

        Usage::
          jsObj.location.host

        :return: Return the hostname and port of the current URL.
        """
        return JsString.JsString("location.host", is_py_data=False)

    @property
    def hash(self) -> JsObject.JsObject:
        """The hash property sets or returns the anchor part of a URL, including the hash sign (#).
        `Related Pages <https//www.w3schools.com/jsref/prop_loc_hash.asp>`_

        Usage::
          jsObj.location.hash

        :return: A String, representing the anchor part of the URL, including the hash sign (#).
        """
        return JsObject.JsObject("location.hash", is_py_data=False)

    @property
    def search(self) -> JsString.JsString:
        """The search property sets or returns the querystring part of a URL, including the question mark (?).
        `Related Pages <https//www.w3schools.com/jsref/prop_loc_search.asp>`_

        :return: A String, representing the querystring part of a URL, including the question mark (?).
        """
        return JsString.JsString("location.search", is_py_data=False)

    @property
    def urlSearchParams(self) -> URLSearchParams:
        """The URLSearchParams() constructor creates and returns a new URLSearchParams object.
        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/URLSearchParams>`_
        """
        return URLSearchParams("location.search")

    @property
    def port(self) -> JsString.JsString:
        """The port property sets or returns the port number the server uses for a URL.
        `Related Pages <https//www.w3schools.com/jsref/prop_loc_port.asp>`_

        :return: A String, representing the port number of a URL.
        """
        return JsString.JsString("location.port", is_py_data=False)

    @property
    def origin(self) -> JsString.JsString:
        """The origin property returns the protocol, hostname and port number of a URL.
        `Related Pages <https//www.w3schools.com/jsref/prop_loc_origin.asp>`_

        Usage::
          page.js.location.origin + page.js.location.pathname

        :return: A String, representing the protocol (including ://), the domain name (or IP address) and port number
          (including the colon sign (:) of the URL. For URL's using the "file:" protocol, the return value differs
          between browser)
        """
        return JsString.JsString("location.origin", is_py_data=False)

    @classmethod
    def href(cls, href: Union[str, primitives.JsDataModel] = None, secured: bool = False) -> JsObject.JsObject:
        """The href property sets or returns the entire URL of the current component.
        `Related Pages <https://www.w3schools.com/jsref/prop_loc_href.asp>`_

        Usage::
          page.js.location.href("https://www.w3schools.com/howto/howto_js_fullscreen.asp")

        :param href: Optional. Set the href property
        :param secured: Optional. The secured flag

        :return: A String, representing the entire URL of the page, including the protocol (like http://).
        """
        if href is None:
            return JsString.JsString("location.href", is_py_data=False)

        if not hasattr(href, 'toStr') and href.startswith("www."):
            href = r"http:\\%s" % href if not secured else r"https:\\%s" % href
        return JsObject.JsObject("location.href = %s" % JsUtils.jsConvertData(href, None))

    @classmethod
    def open_new_tab(cls, url: Union[str, primitives.JsDataModel], name: Union[str, primitives.JsDataModel] = "_blank",
                     specs: Union[str, primitives.JsDataModel] = None,
                     replace: Union[str, primitives.JsDataModel] = None,
                     window_id: str = "window", data: dict = None, secured: bool = False, keep_state: bool = True
                     ) -> JsFncs.JsFunction:
        """Opens a new browser window in a new tab (duplicated but part of the Window module).
        `Related Pages <https://www.w3schools.com/Jsref/met_win_open.asp>`_

        Usage::
          page.js.location.open_new_tab("www.google.fr")

        :param url: Optional. Specifies the URL of the page to open.
          If no URL is specified, a new window/tab with about:blank is opened
        :param name: Optional. Specifies the target attribute or the name of the window. Default _blank
        :param specs: Optional. A comma-separated list of items, no whitespaces
        :param replace: Optional. Specifies whether the URL creates a new entry or replaces the current entry in the
          history list
        :param window_id: Optional. The JavaScript window object
        :param data: Optional. The url parameters
        :param secured: Optional. The secure flag
        :param keep_state: Optional. Keep url parameters
        """
        if not hasattr(url, 'toStr') and url.startswith("www."):
            url = r"http:\\%s" % url if not secured else r"https:\\%s" % url
        url = JsUtils.jsConvertData(url, None)
        name = JsUtils.jsConvertData(name, None)
        keepState = JsUtils.jsConvertData(keep_state, None)
        if data is not None:
            attrs = []
            for k, v in data.items():
                js_val = JsUtils.jsConvertData(v, None)
                attrs.append('"%s=" + %s' % (k, js_val))
            url = str(url) + '+ "?" + %s' % ' +"&"+ '.join(attrs)
        if specs is None:
            return JsFncs.JsFunction('''%s.open((function(url, keepState){
    if (!keepState) {return url};
    const urlTargets = new URL(url); const urlTargetParams = new URLSearchParams(urlTargets.search) ;
    const urlParams = new URLSearchParams(window.location.search) ;
    for(const entry of urlParams.entries()) { 
        if (!urlTargetParams.has(entry[0])){urlTargetParams.append(entry[0], entry[1])}};
    if (urlTargetParams.toString()){ return urlTargets.href + "?" + urlTargetParams.toString() }
    else {return urlTargets.href}
})(%s, %s), %s)
''' % (window_id, url, keepState, name))

        specs = JsUtils.jsConvertData(specs, None)
        replace = JsUtils.jsConvertData(replace, None)
        return JsFncs.JsFunction('''%s.open((function(url, keepState){
    if (!keepState) {return url};
    const urlTargets = new URL(url); const urlTargetParams = new URLSearchParams(urlTargets.search) ;
    const urlParams = new URLSearchParams(window.location.search) ;
    for(const entry of urlParams.entries()) { 
        if (!urlTargetParams.has(entry[0])){urlTargetParams.append(entry[0], entry[1])}};
    if (urlTargetParams.toString()){ return urlTargets.href + "?" + urlTargetParams.toString() }
    else {return urlTargets.href}
})(%s, %s), %s, %s, %s)''' % (window_id, url, keepState, name, specs, replace))

    @classmethod
    def download(cls, url: Union[str, primitives.JsDataModel],
                 name: Union[str, primitives.JsDataModel] = 'download') -> JsObjects.JsVoid:
        """Download data from the url.

        :param url: The url of the image
        :param name: Optional. The name of the file
        """
        url = JsUtils.jsConvertData(url, None)
        name = JsUtils.jsConvertData(name, None)
        return JsObjects.JsVoid('''var link = document.createElement('a'); document.body.appendChild(link);
link.download = %(name)s; link.href = %(url)s; link.click(); link.remove()''' % {'name': name, 'url': url})

    def mail(self, mails: List[str], subject: str, body: str):
        """The mailto link when clicked opens users default email program or software.
        A new email page is created with "To" field containing the address of the name specified on the link by default.
        `Related Pages <http://www.tutorialspark.com/html5/HTML5_email_mailto.php>`_

        Usage::
          page.js.location.mail(["test@gmail.com"], "This is a test", "This is the email's content")

        :param mails: The email addresses
        :param subject: The email's subject
        :param body: The email's content

        :return: THe Javascript string.
        """
        if isinstance(mails, list):
            mails = ";".join(mails)
        return self.href(JsString.JsString(
            "'mailto:%s?subject=%s&body='+ encodeURIComponent('%s')" % (mails, subject, body), is_py_data=False))

    @classmethod
    def reload(cls, force_get: bool = False):
        """The reload() method is used to reload the current document.
        The reload() method does the same as the reload button in your browser.
        `Related Pages <https//www.w3schools.com/jsref/met_loc_reload.asp>`_

        :param force_get: Optional. Specifies the type of reloading:
              false - Default. Reloads the current page from the cache
              true - Reloads the current page from the server
        """
        force_get = JsUtils.jsConvertData(force_get, None)
        return JsFncs.JsFunction("location.reload(%s)" % force_get)

    @classmethod
    def assign(cls, url: Union[str, primitives.JsDataModel]) -> JsFncs.JsFunction:
        """The assign() method loads a new document.
        `Related Pages <https//www.w3schools.com/jsref/met_loc_assign.asp>`_

        :param url: Specifies the URL of the page to navigate to
        """
        data = JsUtils.jsConvertData(url, None)
        return JsFncs.JsFunction("location.assign(%s)" % data)

    @classmethod
    def replace(cls, url: Union[str, primitives.JsDataModel], secured: bool = False) -> JsFncs.JsFunction:
        """The replace() method replaces the current document with a new one.

        The difference between this method and assign(), is that replace() removes the URL of the current document
        from the document history, meaning that it is not possible to use the "back" button to navigate back to the
        original document.

        `Related Pages <https//www.w3schools.com/jsref/met_loc_replace.asp>`_

        :param url: Specifies the URL of the page to navigate to
        :param secured: Optional. If the http is missing. This will be used to fix the url
        """
        if url.startswith("www."):
            url = r"http:\\%s" % url if not secured else r"https:\\%s" % url
        js_data = JsUtils.jsConvertData(url, None)
        return JsFncs.JsFunction("location.replace(%s)" % js_data)

    @classmethod
    def postTo(cls, url: str, data: dict, method: str = "POST", target: str = "_blank"):
        """This method will create an internal form and submit the response exactly like a post of a form to another page.
        `Related Pages <https://www.w3schools.com/jsref/dom_obj_form.asp>`_

        :param url: The target url
        :param data: The url parameters
        :param method: Optional. The method used to send the data. Default POST
        :param target: Optional. Target method to access the new page
        """
        inputs = []
        for k, v in data.items():
            js_val = JsUtils.jsConvertData(v, None)
            inputs.append('''var input = document.createElement("input"); input.name = "%s"; 
input.type = "hidden"; input.value = %s; form.appendChild(input)''' % (k, js_val))
        return ''' 
var form = document.createElement("form"); form.method = "%s"; form.target = "%s"; form.action = "%s"; %s;
document.body.appendChild(form); form.submit()''' % (method, target, url, "".join(inputs))

    @classmethod
    def getUrlFromData(cls, data: Union[dict, primitives.JsDataModel],
                       options: Optional[Union[dict, primitives.JsDataModel]] = None):
        """Convert data to a URL.
        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/Blob>`_

        :param data: Input data to be converted
        :param options: Optional. Blob definition properties
        """
        data = JsUtils.jsConvertData(data, None)
        if options is not None:
            options = JsUtils.jsConvertData(options, None)
            return JsObjects.JsObject.JsObject.get("window.URL.createObjectURL(new Blob([%s], %s))" % (data, options))

        return JsObjects.JsObject.JsObject.get("window.URL.createObjectURL(new Blob([%s]))" % data)

    @classmethod
    def getUrlFromArrays(cls, data: Union[list, primitives.JsDataModel],
                         delimiter: Union[str, primitives.JsDataModel] = ",",
                         charset: str = "utf-8",
                         end_line: Union[str, primitives.JsDataModel] = "\r\n",
                         ):
        """Convert data to a URL.

        :param data: A JavaScript array
        :param delimiter: Optional. The column delimiter
        :param charset: Optional.
        :param end_line: Optional.
        """
        data = JsUtils.jsConvertData(data, None)
        delimiter = JsUtils.jsConvertData(delimiter, None)
        end_line = JsUtils.jsConvertData(end_line, None)
        return JsObjects.JsObject.JsObject.get(r'''
(function(data){let csvContent = "";
  data.forEach(function(rowArray){let row = rowArray.join(%s); csvContent += row + %s});
  return 'data:text/csv;charset=%s,'+escape(csvContent)})(%s)''' % (delimiter, end_line, charset, data))

    def url(self, params: Union[dict, primitives.JsDataModel] = None,
            removed_params: List[str] = None) -> JsString.JsString:
        """Get the current url value. This function can also apply some filters on the existing parameters.

        :param params: Optional. Parameters to be changed / added
        :param removed_params: Optional. Parameters to be removed
        """
        params = params or {}
        removed_params = removed_params or []
        return JsString.JsString('''
(function(params, removedParams){
  var url = new URL(window.location.href); var newParams = [];
  for (k in params){newParams.push(k +"="+ params[k]) }
  for(const entry of url.searchParams.entries()) {
    if (!removedParams.includes(entry[0]) && params[entry[0]] === undefined){
      newParams.push(entry[0] +"="+ entry[1])
    }
  }
  return url.origin + url.pathname + "?"+ newParams.join("&")
})(%s, %s)
''' % (JsUtils.jsConvertData(params, None), JsUtils.jsConvertData(removed_params, None)), is_py_data=False)

    def url_from_object(self, obj, columns: List[str] = None, url: str = None):
        return JsString.JsString.get('''
(function(obj, columns, url){
  let urlParams = [];
  if (columns){columns.forEach(function(col){urlParams.push(col +"="+ obj[col]?.join(","))})} 
  else {for (const [col, colValues] of Object.entries(obj)) {urlParams.push(col +"="+ colValues.join(","))}}
  if (!url){let urlOrigin = new URL(window.location.href); url = urlOrigin.origin + urlOrigin.pathname;}
  return url + "?"+ urlParams.join("&")
})(%s, %s, %s)
''' % (JsUtils.jsConvertData(obj, None), JsUtils.jsConvertData(columns, None),
       JsUtils.jsConvertData(url, None)))

    def update_components(self) -> JsFncs.JsFunction:
        """ Update all components using the default / init configurations. """
        # This will require to add all builders to the resources in the page
        select_components = {}
        for component in self.page.components.values():
            if component.defined_code and hasattr(component.js, "set_value"):
                code = component.html_code
                if component.name == "Radio":
                    code = component.input.attr["name"]
                select_components[code] = "function(v){%s}" % component.js.set_value(JsUtils.jsWrap("v"))
            elif component.defined_code and component._js__builder__:
                component.build(None)
        return JsFncs.JsFunction('''
(function(){let params = new URLSearchParams(location.search); 
    let sComponents = %(sComponents)s;
    for (const [key, value] of params) {
      if (key in sComponents){
        sComponents[key](value)
      } else {
          let componentBuilder = document.getElementById(key);
          if (componentBuilder){
            let componentOptions = %(gOptions)s[key] || {}; 
            let compDataBuilder = componentBuilder?.dataset?.builder ;
            if (!compDataBuilder){compDataBuilder = componentBuilder.getAttribute('data-builder')};
            if (window[compDataBuilder]){
                window[compDataBuilder](componentBuilder, value, componentOptions);
            }
          }
      }
    }
 })()''' % {'gOptions': JsGlobals.EXPORT_INIT_OPTIONS,
            "sComponents": "{%s}" % ", ".join(["%s: %s" % (k, v)for k, v in select_components.items()])})

    def animate_anchor(self, class_name: str, time: int = 3000) -> JsFncs.JsFunction:
        """Animate the selected component when the page.

        :param class_name: The new class name
        :param time: Optional. The time the class will be using in (ms)
        """
        return JsFncs.JsFunction('''
(function(){        
    urlParts = document.URL.split('#');
    let anchor = (urlParts.length > 1) ? urlParts[1] : null;
    if (anchor){
        let anchorComponent = document.getElementById(anchor);
        if (anchorComponent){
            anchorComponent.classList.add("%(class)s");
            if ('scrollRestoration' in window.history) {window.history.scrollRestoration = 'manual'};
            anchorComponent.scrollIntoView();
            setTimeout(function(){anchorComponent.classList.remove("%(class)s");}, %(time)s);
      }
    }
})()''' % {"class": class_name, "time": time})
