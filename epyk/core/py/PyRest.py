"""
Internal wrapper to the REST module.

This module will wrapped urllib and ensure a common interface to run REST calls.
This is not using any external Python module.

Modules wrapped as part of this script
  - https://docs.python.org/3/howto/urllib2.html
  - https://docs.python.org/2/library/urllib2.html
"""

import json
import socket

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
    _props, _context, jsOnLoadEvtsFnc = {}, {}, []

  def __init__(self, src=None):
    self.__src = src if src else self.__internal()

  def server(self, port=5000, service_name=""):
    """
    Start a local server for all the services.
    This should be at the end of the script in order to allow the services debug

    :param port:
    :param service_name:
    :return:
    """
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', port)
    sock.bind(server_address)
    sock.listen(1)
    while True:
      print("Server started")
      connection, client_address = sock.accept()
      try:
        while True:
          data = connection.recv(4096)
      finally:
        connection.close()

  def post(self, url, data=None, encoding='utf-8', headers=None, proxy=None):
    """
    Run a external REST call using the POST method.

    This should be used to retrieve data from external services. If data should be extracted using
    an existing internal service the method query is better as it will embedded the security aspects

    Example
    rptObj.py.requests.post("https://jsonplaceholder.typicode.com/todos/1")

    Documentation
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

  def get(self, url, data=None, encoding='utf-8', headers=None, proxy=None):
    """
    Run a external REST call using the GET method.

    This should be used to retrieve data from external services. If data should be extracted using
    an existing internal service the method query is better as it will embedded the security aspects

    Example
    rptObj.py.requests.get("https://api.cdnjs.com/libraries")
    pyrest.get(r"https://jsonplaceholder.typicode.com/todos/1")

    Documentation
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

  def request(self, url, data=None, method=None, encoding='utf-8', headers=None, unverifiable=False, proxy=None):
    """
    Run a external REST call using a specific method (PUT, DELETE, OPTIONS, HEAD, PUT, PATCH...).

    This should be used to retrieve data from external services. If data should be extracted using
    an existing internal service the method query is better as it will embedded the security aspects

    Example
    json.loads(PyRest().request(r"https://jsonplaceholder.typicode.com/todos/1", method="GET"))

    Documentation
    https://2.python-requests.org/en/master/api/
    https://docs.python.org/3/library/urllib.request.html

    :param url: Should be a string containing a valid URL
    :param method: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param data: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param encoding: Optional. the encoding of this request (defaults to 'utf-8'). This encoding will be used to percent-encode the URL and to convert the body to str (if given as unicode)
    :param headers: Optional. Should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments
    :param unverifiable: Optional. Should indicate whether the request is unverifiable, as defined by RFC 2965
    :param proxy: Optional.

    :return: The content of the REST call as a String
    """
    request = Request(url, json.dumps(data or {}).encode(encoding=encoding), method=method, headers={} if headers is None else headers,
                      unverifiable=unverifiable)
    return urlopen(request).read()

  def webscrapping(self, url, data=None, encoding='utf-8', headers=None, unverifiable=False, proxy=None):
    """
    Create a REST request with the appropriate header to mimic a browser GET request

    Example
    PyRest().webscrapping(r"https://doc.scrapy.org/en/latest/topics/request-response.html")

    :param url: Should be a string containing a valid URL
    :param data: Optional. Must be an object specifying additional data to send to the server, or None if no such data is needed
    :param encoding: Optional. the encoding of this request (defaults to 'utf-8'). This encoding will be used to percent-encode the URL and to convert the body to str (if given as unicode)
    :param headers: Optional. Should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments
    :param unverifiable: Optional. Should indicate whether the request is unverifiable, as defined by RFC 2965
    :param proxy: Optional.

    :return: The HTML content of the REST call as a String
    """
    default_headers = {'User-Agent': 'Mozilla/5.0'}
    if headers is not None:
      default_headers.update(headers)
    try:
      return self.request(url, data, "GET", encoding, default_headers, unverifiable, proxy)

    except Exception as err:
      return err

  def query(self, service_name, function_name="getData", report_name=None, data=None, encoding='utf-8'):
    """

    Example
    rptObj.py.requests.query("SrcTest", "textbubble")

    Documentation

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
