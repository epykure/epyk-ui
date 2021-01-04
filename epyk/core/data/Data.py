#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module in charge of monitoring the internal data sources in the framework.

This module will mainly monitor
  - The temp files: Cached files
  - The downloaded or saved files

For the cached the format will be using object whereas files will be stored without
any specific conversion. The module in charge of reading the file will be in
charge of parsing the data.

"""

import os
import sys
import json
import pickle
import importlib


from epyk.core.data import DataPy
from epyk.core.data import DataGrpc

from epyk.core.js.Imports import requires
from epyk.core.js.packages import JsQuery
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects


class DataJs(object):
  def __init__(self, report):
    self._report = report

  def record(self, varName=None, data=None):
    """
    Description:
    ------------
    Interface to transform Python records to Javascript objects.
    This will allow interactivity of the various HTML components

    Attributes:
    ----------
    :param varName: String. The Javascript variable name
    :param data: Dictionary of lists. Object passed to the Javascript layer
    """
    from epyk.core.data import DataCore

    return DataCore.DataGlobal(varName, data, self._report)

  def list(self, varName, data):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param varName: String. The Javascript variable name
    :param data: List. Object passed to the Javascript layer
    """
    JsUtils.getJsValid(varName, fail=True)
    return JsObjects.JsObjects().array(data, varName=varName, setVar=True, report=self._report)

  def number(self, varName, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param varName: String. The Javascript variable name
    :param value: Float or Integer. Object passed to the Javascript layer
    """
    JsUtils.getJsValid(varName, fail=True)
    return JsObjects.JsObjects().number(value, varName=varName, setVar=True, report=self._report)

  def object(self, varName, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param varName: String. The Javascript variable name
    :param value: Float or Integer. Object passed to the Javascript layer
    """
    JsUtils.getJsValid(varName, fail=True)
    return JsObjects.JsObjects().new(value, varName=varName, report=self._report)

  def server(self, hostname, port=8080):
    """
    Description:
    ------------
    Configuration data for server interaction.
    This will only help on centralising the configuration in the final page.

    Attributes:
    ----------
    :param hostname: String. The server hostname
    :param port: Integer. The server port
    """
    from epyk.core.data import DataCore

    return DataCore.ServerConfig(hostname, port, self._report)


class DataSrc(object):
  class __internal(object):
    _props = {}

  def __init__(self, report=None):
    self._report = report if report is not None else self.__internal()

  @property
  def vis(self):
    return DataPy.Vis()

  @property
  def chartJs(self):
    return DataPy.ChartJs()

  @property
  def plotly(self):
    return DataPy.Plotly()

  @property
  def c3(self):
    return DataPy.C3()

  @property
  def bb(self):
    return DataPy.C3()

  @property
  def nvd3(self):
    return DataPy.NVD3()

  @property
  def google(self):
    return DataPy.Google()

  @property
  def js(self):
    """
    Description:
    ------------
    Interface to the Javascript world
    """
    return DataJs(self._report)

  @property
  def db(self):
    from epyk.core.data import DataDb

    return DataDb.DataDb(self._report)

  def from_cache(self, code, is_secured=False, report_name=None):
    """
    Description:
    -----------
    Loads data from a cached files

    Attributes:
    ----------
    :param code: The code for the data
    :param is_secured: Optional, boolean to set if the file should be secured. Default False
    :param report_name: Optional, the environment in which cache are stored. Default current one

    :return: Return the data
    """
    if getattr(self._report, "run", None) is not None:
      report_name = report_name or self._report.run.report_name
      path = self._report.run.local_path
      if report_name != self._report.run.report_name:
        path = self._report.run.local_path.replace(self._report.run.report_name, report_name)
      cache_path = os.path.join(path, "tmp")
      if not os.path.exists(cache_path):
        os.mkdir(cache_path) # Create the path to store the temp files
      file_path = os.path.join(path, "tmp", code)
      if os.path.exists(file_path):
        file_obj = open(file_path, 'rb')
        return pickle.load(file_obj)

      return None

  def save_cache(self, data, code, is_secured=False, if_missing=True):
    """
    Description:
    -----------
    Temporary files are saved in a pickle manner in order to avoid having to parse those files again.

    Attributes:
    ----------
    :param data: The data to be saved
    :param code: The code for the data
    :param is_secured: Optional, boolean to set if the file should be secured. Default False
    :param if_missing: Optional, boolean to set the fact that caches are only saved if missing
    """
    if getattr(self._report, "run", None) is not None:
      cache_path = os.path.join(self._report.run.local_path, "tmp")
      if not os.path.exists(cache_path):
        os.mkdir(cache_path)  # Create the path to store the temp files
      if if_missing and not os.path.exists(os.path.join(cache_path, code)):
        file_obj = open(os.path.join(cache_path, code), 'wb')
        pickle.dump(data, file_obj)

  def from_file(self, filename, isSecured=False, report_name=None):
    """
    Description:
    -----------
    Return the file

    Attributes:
    ----------
    :param filename: The filename
    :param isSecured: Optional, Check if the file is secured or not
    :param report_name: The environment with the file

    :return: The file object
    """
    if getattr(self._report, "run", None) is not None:
      report_name = report_name or self._report.run.report_name
      path = self._report.run.local_path
      if report_name != self._report.run.report_name:
        path = self._report.run.local_path.replace(self._report.run.report_name, report_name)
      cachePath = os.path.join(path, "data")
      if not os.path.exists(cachePath):
        os.mkdir(cachePath) # Create the path to store the temp files
      filePath = os.path.join(path, "data", "%s.csv" % filename)
      return open(filePath)

  def from_source(self, http_data, fileName, fncName="getData", report_name=None, folder="sources", path=None):
    """
    Description:
    ------------
    Returns data from a internal data service defined in the sources folder

    Attributes:
    ----------
    :param http_data: The input data for the service
    :param fileName: The service file name
    :param fncName: Optional, the function name in the service. Default getData
    :param report_name: Optional, the report name. Default the current one
    :param folder: Optional, the folder with the services. Default sources
    :param path: Optional, the path to be added to the python system path
    """
    fileName = fileName.replace(".py", "")
    if path is not None:
      if path not in sys.path:
        sys.path.append(path)
      if folder is not None:
        mod = importlib.import_module("%s.%s" % (folder, fileName))
      else:
        mod = importlib.import_module(fileName)
    else:
      if report_name is None:
        report_name = self._report.run.report_name
      mod = importlib.import_module("%s.%s.%s" % (report_name, folder, fileName))
    return getattr(mod, fncName)(self._report, http_data)

  def from_post_source(self, script, data=None, successFncs=None, udpate_freq=None, interval_name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param script:
    :param data:
    :param successFncs:
    :param udpate_freq: Optional, Set the data update frequency in second
    """
    if udpate_freq is not None:
      return self._report.js.window.setInterval(JsQuery.JQuery(self._report).getPyScript(script, data, successFncs=successFncs), milliseconds=udpate_freq * 1000).setVar(interval_name)

    return JsQuery.JQuery(self._report).getPyScript(script, data, successFncs=successFncs)

  def from_get(self, url, data=None, code=None):
    """

    """
    return JsQuery.JQuery(self._report).get(url, data)

  def pdf(self, filename, path=None):
    """
    Description:
    -----------
    Read a pdf file

    This will require an external module PyPDF2
    Example
    data = rptObj.data.pdf("document.pdf", r"")
    data.getPage(0)

    Related Pages:

      https://www.geeksforgeeks.org/working-with-pdf-files-in-python/

    Attributes:
    ----------
    :param filename: The pdf file name
    :param path: The file path
    :return: A pdf object from PyPDF2
    """
    pyPDF2 = requires("PyPDF2", reason='Missing Package', install='PyPDF2', sourceScript=__file__, raiseExcept=True)
    pdf_data = pyPDF2.PdfFileReader(os.path.join(path, filename))
    return pdf_data

  # --------------------------------------------------------------------------------
  # generic system entry point
  #

  def soap(self, wsdl):
    """
    Description:
    -----------
    Interface to a SOAP server.

    This function will require an external python package zeep to use SOAP

    Example
    soap = rptObj.data.soap("http://www.soapclient.com/xml/soapresponder.wsdl")
    soap.Method1('Zeep', 'is cool')

    Related Pages:

      https://en.wikipedia.org/wiki/SOAP
    https://python-zeep.readthedocs.io/en/master/

    Attributes:
    ----------
    :param wsdl: The wsdl service url
    :rtype: zeep.service

    :return: The SOAP services
    """
    soap = requires("zeep", reason='Missing Package', install="zeep", sourceScript=__file__, raiseExcept=True)
    return soap.Client(wsdl).service

  def rest(self, url, data=None, method=None, encoding='utf-8', headers=None, unverifiable=False, proxy=None):
    """
    Description:
    -----------
    Interface to a REST server.

    Test with a online server can be done here https://jsonplaceholder.typicode.com/

    Example
    rptObj.data.rest("https://jsonplaceholder.typicode.com/posts/1", method="PUT")

    Related Pages:

      https://jsonrpcclient.readthedocs.io/en/latest/api.html

    Attributes:
    ----------
    :param url: The REST service url
    :param data: The input data for the service
    """
    return json.loads(self._report.py.request(url, data, method, encoding, headers, unverifiable, proxy=proxy))

  def socket(self, data, host='localhost', port=5000, encoding='utf-8'):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data: The input data for the service
    :param host: The service host name (e.g localhost)
    :param port: The service port
    :param encoding:
    """
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(json.dumps(data).encode(encoding=encoding))
    result = s.recv(1024)
    s.close()
    return result

  def websocket(self):
    pass

  def rss(self, url, proxy=None, method="GET"):
    """
    Description:
    -----------
    Entry point to retrieve RSS feeds.

    This module will require beautifulsoup4 as external package

    Example
    xml_soup = rptObj.data.rss("http://feeds.reuters.com/reuters/businessNews")
    for title in xml_soup.findAll('title'):
      print(title)

    Related Pages:

      https://pypi.org/project/beautifulsoup4/

    Attributes:
    ----------
    :param url: The url of the html page
    :param method: Optional, The request method. Default method GET

    :return: A xml object
    """
    bs4 = requires("bs4", reason='Missing Package', install='beautifulsoup4', sourceScript=__file__, raiseExcept=True)
    headers = {'User-Agent': 'Mozilla/5.0', 'accept': 'application/xml;q=0.9, */*;q=0.8'}
    response = self._report.py.requests.get(url, headers=headers, proxy=proxy)
    xml_soup = bs4.BeautifulSoup(response,)
    return xml_soup

  def webscrapping(self, url, parser="html.parser", proxy=None, method=None):
    """
    Description:
    -----------
    Entry point to retrieve data from any website.

    This module will require beautifulsoup4 as external package

    Example
    rptObj.data.webscrapping("https://www.w3schools.com/colors/default.asp")
    xml_soup.findAll('title')

    Related Pages:

      https://pypi.org/project/beautifulsoup4/

    Attributes:
    ----------
    :param url: The url of the html page
    :param parser: The output data parser

    :return: A xml object
    """
    bs4 = requires("bs4", reason='Missing Package', install='beautifulsoup4', sourceScript=__file__, raiseExcept=True)
    headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    response = self._report.py.request(url, headers=headers, method=method, proxy=proxy)
    xml_soup = bs4.BeautifulSoup(response, parser)
    return xml_soup



  def rpc(self, url, data=None, headers=None, is_secured=False):
    """
    Description:
    -----------
    Interface to a RPC server.

    This is using the external python package jsonrpcclient (https://jsonrpcclient.readthedocs.io/en/latest/)

    Example

    Related Pages:

      https://en.wikipedia.org/wiki/Rapid_control_prototyping
    https://gurujsonrpc.appspot.com/
    https://jsonrpcclient.readthedocs.io/en/latest/

    Attributes:
    ----------
    :param url: The RPC service url
    :param data: The input data for the service
    """
    http_client = requires("jsonrpcclient.clients.http_client", reason='Missing Package', install="jsonrpcclient[requests]", sourceScript=__file__, raiseExcept=True)
    client = http_client.HTTPClient(url)
    if headers is not None:
      client.session.headers.update(headers)
    if is_secured:
      client.session.auth = ("user", "pass")
    if data is None or "method" not in data:
      raise Exception("data must of a method defined")

    return client.send(json.dumps(data))

  def grpc(self, serviceName, path, module, host="localhost", port=50051):
    """
    Description:
    -----------
    Interface to a GRPC server.

    Example
    grpc = rptObj.data.grpc(serviceName="GreeterStub", module="helloworld_pb2_grpc", path="")
    data = grpc.imp("helloworld_pb2").HelloRequest(name="Test")
    print(grpc.request("SayHello", data))

    Related Pages:

      https://grpc.io/docs/tutorials/basic/python/
    https://grpc.io/docs/quickstart/python.html

    Attributes:
    ----------
    :param serviceName: The Service name (the class name in the python module)
    :param path: The path with the GRPC features
    :param module: The python module name for the service
    :param host: The service host name (e.g localhost)
    :param port: The service port

    :return: A GRPC wrapped object
    """
    requires("grpc", reason='Missing Package', install='grpcio', sourceScript=__file__, raiseExcept=True)
    return DataGrpc.DataGrpc(serviceName, path, module, host, port)
