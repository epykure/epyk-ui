"""
Internal wrapper to the REST module.

This module will wrapped urllib and ensure a common interface to run REST calls.
This is not using any external Python module.

Modules wrapped as part of this script
  - https://docs.python.org/3/howto/urllib2.html
  - https://docs.python.org/2/library/urllib2.html
"""

import hashlib
import os
import json

TMP_PATH = None  # path for all the temporary files

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request, ProxyHandler, build_opener, install_opener
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError, ProxyHandler, build_opener, install_opener


class PyRest(object):
  class __internal(object):
    _props, _context = {}, {}

  def __init__(self, src=None):
    self.__src = src if src else self.__internal()

  def proxy(self, username, password, proxy_host, proxy_port, protocols=None):
    """
    Description:
    ------------
    Set the proxy connexions for the Python requests.

    Attributes:
    ----------
    :param username: String. The username
    :param password: String. The user password
    :param proxy_host: String. The proxy server hostname
    :param proxy_port: Integer. The proxy server port
    :param protocols: List. Protocoles for the proxy. Default [('http', 'http://'), ('https', 'https://')]
    """
    if protocols is None:
      protocols = [('http', 'http://'), ('https', 'https://')]
    proxies = {k: '%s%s:%s@%s:%s' % (v, username, password, proxy_host, proxy_port) for k, v in protocols}
    proxy = ProxyHandler(proxies)
    opener = build_opener(proxy)
    install_opener(opener)

  def http_server(self, port=5000, service_name=""):
    """
    Description:
    ------------
    Start a local server for all the services.
    This should be at the end of the script in order to allow the services debug

    Attributes:
    ----------
    :param port:
    :param service_name:
    """
    import http.server
    import socketserver
    import io

    class GetHandler(http.server.SimpleHTTPRequestHandler):

      def do_GET(self):
        self.send_response(200)
        self.end_headers()
        http.server.SimpleHTTPRequestHandler.do_GET(self)

      def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = io.BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

    Handler = GetHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    httpd.serve_forever()

  def post(self, url, data=None, encoding='utf-8', headers=None, proxy=None):
    """
    Description:
    ------------
    Run a external REST call using the POST method.

    This should be used to retrieve data from external services. If data should be extracted using
    an existing internal service the method query is better as it will embedded the security aspects

    Usage::

      rptObj.py.requests.post("https://jsonplaceholder.typicode.com/todos/1")

    Related Pages:

      https://docs.python.org/2/howto/urllib2.html

    Attributes:
    ----------
    :param url: The external URL to the REST service
    :param data: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param encoding: Optional. The encoding of this request (defaults to 'utf-8'). This encoding will be used to percent-encode the URL and to convert the body to str (if given as unicode)
    :param headers: Optional. Should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments
    :param proxy: Optional.

    :return: The content of the REST call as a String
    """
    if headers is None:
      headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
    request = Request(url, json.dumps(data or {}).encode(encoding=encoding), headers=headers)
    if headers.get("Content-Type") == "application/json":
      return json.loads(urlopen(request).read())

    return urlopen(request).read()

  def get(self, url, data=None, encoding='utf-8', headers=None, proxy=None):
    """
    Description:
    ------------
    Run a external REST call using the GET method.

    This should be used to retrieve data from external services. If data should be extracted using
    an existing internal service the method query is better as it will embedded the security aspects

    Usage::

      rptObj.py.requests.get("https://api.cdnjs.com/libraries")
    pyrest.get(r"https://jsonplaceholder.typicode.com/todos/1")

    Related Pages:

      https://docs.python.org/2/howto/urllib2.html

    Attributes:
    ----------
    :param url: Should be a string containing a valid URL
    :param data: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param encoding: Optional. The encoding of this request (defaults to 'utf-8'). This encoding will be used to percent-encode the URL and to convert the body to str (if given as unicode)
    :param headers: Optional. Should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments
    :param proxy: Optional.

    :return: Return a Python object by default
    """
    if headers is None:
      headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
    if data is None:
      request = Request(url, method="GET", headers=headers)
    else:
      request = Request(url, json.dumps(data).encode(encoding=encoding), method="GET", headers=headers)
    if headers.get("Content-Type") == "application/json":
      return json.loads(urlopen(request).read())

    return urlopen(request).read()

  def request(self, url, data=None, method=None, encoding='utf-8', headers=None, unverifiable=False, proxy=None):
    """
    Description:
    ------------
    Run a external REST call using a specific method (PUT, DELETE, OPTIONS, HEAD, PUT, PATCH...).

    This should be used to retrieve data from external services. If data should be extracted using
    an existing internal service the method query is better as it will embedded the security aspects

    Usage::

      json.loads(PyRest().request(r"https://jsonplaceholder.typicode.com/todos/1", method="GET"))

    Related Pages:

      https://2.python-requests.org/en/master/api/
    https://docs.python.org/3/library/urllib.request.html

    Attributes:
    ----------
    :param url: Should be a string containing a valid URL
    :param method: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param data: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param encoding: Optional. the encoding of this request (defaults to 'utf-8'). This encoding will be used to percent-encode the URL and to convert the body to str (if given as unicode)
    :param headers: Optional. Should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments
    :param unverifiable: Optional. Should indicate whether the request is unverifiable, as defined by RFC 2965
    :param proxy: Optional.

    :return: The content of the REST call as a String
    """
    if data:
      data = json.dumps(data).encode(encoding=encoding)
    request = Request(url, data, method=method, headers={} if headers is None else headers, unverifiable=unverifiable)
    return urlopen(request).read()

  def webscrapping(self, url, data=None, encoding='utf-8', headers=None, unverifiable=False, proxy=None):
    """
    Description:
    ------------
    Create a REST request with the appropriate header to mimic a browser GET request

    Usage::

      PyRest().webscrapping(r"https://doc.scrapy.org/en/latest/topics/request-response.html")

    Attributes:
    ----------
    :param url: Should be a string containing a valid URL
    :param data: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param encoding: Optional. the encoding of this request (defaults to 'utf-8'). This encoding will be used to percent-encode the URL and to convert the body to str (if given as unicode)
    :param headers: Optional. Should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments
    :param unverifiable: Optional. Should indicate whether the request is unverifiable, as defined by RFC 2965
    :param proxy: Optional.

    :return: The HTML content of the REST call as a String
    """
    default_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
      'referrer': 'https://google.com',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
      #'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'en-US,en;q=0.9',
      'Pragma': 'no-cache'
    }
    if headers is not None:
      default_headers.update(headers)
    try:
      return self.request(url, data, "GET", encoding, default_headers, unverifiable, proxy)

    except Exception as err:
      return err

  def csv(self, url, delimiter=",", encoding='utf-8', with_header=True, store_location=None):
    """
    Description:
    ------------
    Retrieve tabular data from an external REST service

    Attributes:
    ----------
    :param url: String. The url with the data to request
    :param delimiter: String. The line delimiter
    :param encoding: String. The encoding format
    :param with_header: Boolean. A flag to mention if the header is available. (it will be used for the keys)
    :param store_location: Optional. String. The temp folder to cache the data locally. False will cancel the temps data retrievall
    """
    has_file = str(hashlib.sha1(url.encode()).hexdigest())
    if store_location is not False:
      # False will override the fact that we do not want to get stored data for this call
      store_location = store_location or TMP_PATH
    else:
      store_location = None
    if store_location is not None:
      file_path = os.path.join(store_location, has_file)
      if os.path.isfile(file_path):
        return json.load(open(file_path))

    raw_data = self.webscrapping(url).decode(encoding).splitlines()
    if url.endswith(".tsv"):
      delimiter = "\t"
    records = []
    if raw_data:
      header = raw_data[0].split(delimiter)
      if not with_header:
        line = list(header)
        header = [i for i in range(len(header))]
        records.append(dict(zip(header, line)))
      for line in raw_data[1:]:
        records.append(dict(zip(header, line.split(delimiter))))

    if store_location is not None:
      with open(file_path, "w") as f:
        json.dump(records, f)
    return records

  def json(self, url, encoding='utf-8', store_location=None):
    """
    Description:
    ------------
    Retrieve Json data from an external REST service

    Attributes:
    ----------
    :param url: String. The url with the data to request
    :param encoding: String. The encoding format
    :param store_location: Optional. String. The temp folder to cache the data locally
    """
    has_file = str(hashlib.sha1(url.encode()).hexdigest())
    if store_location is not False:
      store_location = store_location or TMP_PATH
    else:
      store_location = None
    if store_location is not None:
      file_path = os.path.join(store_location, has_file)
      if os.path.isfile(file_path):
        return json.load(open(file_path))

    raw_data = json.loads(self.webscrapping(url).decode(encoding))
    if store_location is not None:
      with open(file_path, "w") as f:
        json.dump(raw_data, f)
    return raw_data

  def query(self, service_name, function_name="getData", report_name=None, data=None, encoding='utf-8'):
    """

    Usage::

      rptObj.py.requests.query("SrcTest", "textbubble")

    Attributes:
    ----------
    :param service_name: The service Name in the sources folder
    :param function_name: Optional, Optional, the function name in the service. Default getData()
    :param report_name: Optional, The folder name
    :param data: Optional, The input data for the service
    :param encoding: Optional, The encoding for the input data. Default utf-8

    :return:
    """
    if data is None:
      data = {}
    if not "data" in data:
      data = {"data": data}
    data["_function"] = function_name
    if report_name is None:
      report_name = self.__src.run.report_name
    try:
      headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
    except Exception as err:
      headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
    url = "%sdata/%s/%s" % ("http://192.168.0.34:5000/reports/", report_name, service_name)
    request = Request(url, json.dumps(data).encode(encoding=encoding), headers)
    return json.loads(urlopen(request).read())
