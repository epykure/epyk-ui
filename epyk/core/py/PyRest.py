"""
Internal wrapper to the REST module.

This module will wrapped urllib and ensure a common interface to run REST calls.
This is not using any external Python module.

Modules wrapped as part of this script
  - https://docs.python.org/3/howto/urllib2.html
  - https://docs.python.org/2/library/urllib2.html

# TODO add pandas to this module when it is available
"""

from epyk.core.py import primitives

import csv
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


class PyRest:

  def __init__(self, page: primitives.PageModel = None):
    self.page = page

  def proxy(self, username: str, password: str, proxy_host: str, proxy_port: int, protocols: list = None):
    """ Set the proxy connexions for the Python requests.

    :param username: The username.
    :param password: The user password.
    :param proxy_host: The proxy server hostname.
    :param proxy_port: The proxy server port.
    :param protocols: Protocols for the proxy. Default [('http', 'http://'), ('https', 'https://')]
    """
    if protocols is None:
      protocols = [('http', 'http://'), ('https', 'https://')]
    proxies = {k: '%s%s:%s@%s:%s' % (v, username, password, proxy_host, proxy_port) for k, v in protocols}
    proxy = ProxyHandler(proxies)
    opener = build_opener(proxy)
    install_opener(opener)

  def http_server(self, port: int = 5000, service_name: str = ""):
    """ Start a local server for all the services.
    This should be at the end of the script in order to allow the services debug.

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

    handler = GetHandler
    httpd = socketserver.TCPServer(("", port), handler)
    httpd.serve_forever()

  def post(self, url: str, data=None, encoding: str = 'utf-8', headers: dict = None, proxy: dict = None):
    """ Run a external REST call using the POST method.

    This should be used to retrieve data from external services. If data should be extracted using
    an existing internal service the method query is better as it will embedded the security aspects

    Usage::

      page.py.requests.post("https://jsonplaceholder.typicode.com/todos/1")

    Related Pages:

      https://docs.python.org/2/howto/urllib2.html

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

  def get(self, url: str, data=None, encoding: str = 'utf-8', headers: dict = None, proxy: dict = None):
    """ Run an external REST call using the GET method.

    This should be used to retrieve data from external services. If data should be extracted using
    an existing internal service the method query is better as it will embedded the security aspects

    Usage::

      page.py.requests.get("https://api.cdnjs.com/libraries")
      pyrest.get(r"https://jsonplaceholder.typicode.com/todos/1")

    Related Pages:

      https://docs.python.org/2/howto/urllib2.html

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

  @staticmethod
  def request(url: str, data=None, method: str = None, encoding: str = 'utf-8', headers: dict = None,
              unverifiable: bool = False, proxy: dict = None):
    """ Run a external REST call using a specific method (PUT, DELETE, OPTIONS, HEAD, PUT, PATCH...).

    This should be used to retrieve data from external services. If data should be extracted using
    an existing internal service the method query is better as it will embedded the security aspects

    Usage::

      json.loads(PyRest().request(r"https://jsonplaceholder.typicode.com/todos/1", method="GET"))

    Related Pages:

      https://2.python-requests.org/en/master/api/
      https://docs.python.org/3/library/urllib.request.html

    :param url: Should be a string containing a valid URL
    :param method: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param data: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param encoding: String. Optional. the encoding of this request (defaults to 'utf-8'). This encoding will be used to percent-encode the URL and to convert the body to str (if given as unicode)
    :param headers: Optional. Should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments
    :param unverifiable: Optional. Should indicate whether the request is unverifiable, as defined by RFC 2965
    :param proxy: Optional.

    :return: The content of the REST call as a String
    """
    if data:
      data = json.dumps(data).encode(encoding=encoding)
    request = Request(url, data, method=method, headers={} if headers is None else headers, unverifiable=unverifiable)
    return urlopen(request).read()

  @staticmethod
  def webscrapping(url: str, data=None, encoding: str = 'utf-8', headers: dict = None,
                   unverifiable: bool = False, proxy: dict = None):
    """ Create a REST request with the appropriate header to mimic a browser GET request.

    Usage::

      PyRest().webscrapping(r"https://doc.scrapy.org/en/latest/topics/request-response.html")

    :param url: Should be a string containing a valid URL
    :param data: Optional. Must be an object specifying additional data to send to the server, or None if no such
      data is needed
    :param encoding: Optional. the encoding of this request (defaults to 'utf-8'). This encoding will be used to
      percent-encode the URL and to convert the body to str (if given as unicode)
    :param headers: Optional. Should be a dictionary, and will be treated as if add_header() was called with
      each key and value as arguments
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
      return PyRest.request(url, data, "GET", encoding, default_headers, unverifiable, proxy)

    except Exception as err:
      return err

  @staticmethod
  def csv(url: str, delimiter: str = ",", encoding: str = 'utf-8', with_header: bool = True,
          store_location: str = None, quotechar: str = '"'):
    """ Retrieve tabular data from an external REST service.

    :param url: The url with the data to request.
    :param delimiter: Optional. The line delimiter.
    :param encoding: Optional. The encoding format.
    :param with_header: Optional. A flag to mention if the header is available. (it will be used for the keys)
    :param store_location: Optional. The temp folder to cache the data locally. False will cancel the
      temps data retrieval
    :param quotechar: Optional.
    """
    has_file = str(hashlib.sha1(url.encode()).hexdigest())
    if store_location is None or store_location:
      # False will override the fact that we do not want to get stored data for this call
      store_location = store_location or TMP_PATH
    else:
      store_location = None
    if store_location is not None:
      file_path = os.path.join(store_location, has_file)
      if os.path.isfile(file_path):
        return json.load(open(file_path))

    if url.endswith(".tsv"):
      delimiter = "\t"
    raw_data = list(csv.reader(
      PyRest.webscrapping(url).decode(encoding).splitlines(), delimiter=delimiter, quotechar=quotechar))
    records = []
    if raw_data:
      header = raw_data[0]
      if not with_header:
        line = list(header)
        header = [i for i in range(len(header))]
        records.append(dict(zip(header, line)))
      for line in raw_data[1:]:
        records.append(dict(zip(header, line)))
    if store_location is not None:
      file_path = os.path.join(store_location, has_file)
      with open(file_path, "w") as f:
        json.dump(records, f)
    return records

  def json(self, url: str, encoding: str = 'utf-8', store_location: str = None):
    """ Retrieve Json data from an external REST service.

    :param url: The url with the data to request.
    :param encoding: Optional. The encoding format.
    :param store_location: Optional. String. The temp folder to cache the data locally.
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
