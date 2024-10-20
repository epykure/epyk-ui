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
from typing import List

from epyk.core.py import primitives

from epyk.core.data import DataCore
from epyk.core.data import DataPy
from epyk.core.data import DataGrpc

from epyk.core.js.Imports import requires
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsUnderscore
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects


class DataJs:
    def __init__(self, page: primitives.PageModel):
        self.page = page

    def record(self, js_code: str = None, data=None) -> DataCore.DataGlobal:
        """Interface to transform Python records to Javascript objects.

        This will allow interactivity of the various HTML components.

        Usage::

            js_data = page.data.js.record(js_code="myData", data=randoms.languages) # Create JavaScript data
            filter1 = js_data.filterGroup("filter1") # Add a filter object

            # Add a dropdown box to drive the data changes in the charts
            select = page.ui.select([
              {"value": 'name', 'name': 'name'}, {"value": 'type', 'name': 'code'}], options={"empty_selected": False})

            # Create HTML charts
            bar = page.ui.charts.chartJs.bar(randoms.languages, y_columns=["rating", 'change'], x_axis='name')
            pie = page.ui.charts.chartJs.pie(randoms.languages, y_columns=['change'], x_axis='name')

            select.change([
              bar.build(filter1.group().sumBy(['rating', 'change'], select.dom.content), options={"x_axis": select.dom.content}),
              pie.build(filter1.group().sumBy(['change'], select.dom.content), options={"x_axis": select.dom.content}),
            ])

        :param js_code: Optional. The Javascript variable name
        :param data: Object passed to the Javascript layer
        """
        return DataCore.DataGlobal(js_code, data, self.page)

    def list(self, js_code: str, data):
        """Transform a Python object to a JavaScript list.

        :param js_code: The Javascript variable name
        :param data: Object passed to the Javascript layer
        """
        JsUtils.getJsValid(js_code, fail=True)
        return JsObjects.JsObjects().array(data, js_code=js_code, set_var=True, page=self.page)

    def number(self, js_code: str, value):
        """Transform a Python number to a JavaScript one.

        :param js_code: The Javascript variable name
        :param value: Object passed to the Javascript layer
        """
        JsUtils.getJsValid(js_code, fail=True)
        return JsObjects.JsObjects().number(value, js_code=js_code, set_var=True, page=self.page)

    def object(self, js_code: str, value: float):
        """Transform a Python object to a JavaScript object.

        :param js_code: The Javascript variable name
        :param value: Object passed to the Javascript layer
        """
        JsUtils.getJsValid(js_code, fail=True)
        return JsObjects.JsObjects().new(value, js_code=js_code, page=self.page)

    def server(self, hostname: str, port: int = 8080) -> DataCore.ServerConfig:
        """
    Configuration data for server interaction.

    This will only help on centralising the configuration in the final page.

    :param hostname: The server hostname
    :param port: Optional. The server port
    """
        return DataCore.ServerConfig(hostname, port, self.page)

    @property
    def _(self):
        """ """
        return JsUnderscore.Underscore(page=self.page)


class DataSrc:

    def __init__(self, page: primitives.PageModel = None):
        self.page = page

    @property
    def vis(self) -> DataPy.Vis:
        """Interface to Vis data transformation.

        This will convert Python object to input data for Vis charts.
        """
        return DataPy.Vis()

    @property
    def chartJs(self) -> DataPy.ChartJs:
        """Interface to chartJs data transformation.

        This will convert Python object to input data for chartJs charts.
        """
        return DataPy.ChartJs()

    @property
    def plotly(self) -> DataPy.Plotly:
        """Interface to Plotly data transformation.

        This will convert Python object to input data for Plotly charts.
        """
        return DataPy.Plotly()

    @property
    def c3(self) -> DataPy.C3:
        """Interface to C3 data transformation.

        This will convert Python object to input data for C3 charts.
        """
        return DataPy.C3()

    @property
    def bb(self) -> DataPy.C3:
        """Interface to Billboard data transformation.

        This will convert Python object to input data for Billboard charts.
        """
        return DataPy.C3()

    @property
    def nvd3(self) -> DataPy.NVD3:
        """Interface to NVD3 data transformation.

        This will convert Python object to input data for NVD3 charts.
        """
        return DataPy.NVD3()

    @property
    def google(self) -> DataPy.Google:
        """Interface to Google data transformation.

        This will convert Python object to input data for Google charts.
        """
        return DataPy.Google()

    @property
    def js(self) -> DataJs:
        """ Interface to standard JavaScript transformation. """
        return DataJs(self.page)

    @property
    def db(self):
        """Interface to the internal database wrapper.

        :rtype: DataDb.DataDb
        """
        from epyk.core.data import DataDb

        return DataDb.DataDb(self.page)

    def from_cache(self, code: str, is_secured: bool = False, report_name: str = None):
        """Loads data from a cached files.

        :param code: The code for the data
        :param is_secured: Optional, boolean to set if the file should be secured. Default False
        :param report_name: Optional. the environment in which cache are stored. Default current one

        :return: Return the data
        """
        if getattr(self.page, "run", None) is not None:
            report_name = report_name or self.page.run.report_name
            path = self.page.run.local_path
            if report_name != self.page.run.report_name:
                path = self.page.run.local_path.replace(self.page.run.report_name, report_name)
            cache_path = os.path.join(path, "tmp")
            if not os.path.exists(cache_path):
                os.mkdir(cache_path)  # Create the path to store the temp files
            file_path = os.path.join(path, "tmp", code)
            if os.path.exists(file_path):
                file_obj = open(file_path, 'rb')
                return pickle.load(file_obj)

    def save_cache(self, data, code, is_secured: bool = False, if_missing: bool = True):
        """ Temporary files are saved in a pickle manner in order to avoid having to parse those files again.

        :param data: The data to be saved
        :param code: The code for the data
        :param is_secured: Optional. boolean to set if the file should be secured. Default False
        :param if_missing: Optional. boolean to set the fact that caches are only saved if missing
        """
        if getattr(self.page, "run", None) is not None:
            cache_path = os.path.join(self.page.run.local_path, "tmp")
            if not os.path.exists(cache_path):
                os.mkdir(cache_path)  # Create the path to store the temp files
            if if_missing and not os.path.exists(os.path.join(cache_path, code)):
                file_obj = open(os.path.join(cache_path, code), 'wb')
                pickle.dump(data, file_obj)

    def from_file(self, filename, isSecured=False, report_name=None):
        """ Return the file.

        :param filename: The filename.
        :param isSecured: Optional. Check if the file is secured or not.
        :param report_name: Optional. The environment with the file.

        :return: The file object
        """
        if getattr(self.page, "run", None) is not None:
            report_name = report_name or self.page.run.report_name
            path = self.page.run.local_path
            if report_name != self.page.run.report_name:
                path = self.page.run.local_path.replace(self.page.run.report_name, report_name)
            cache_path = os.path.join(path, "data")
            if not os.path.exists(cache_path):
                os.mkdir(cache_path)  # Create the path to store the temp files
            file_path = os.path.join(path, "data", "%s.csv" % filename)
            return open(file_path)

    def from_source(self, http_data, file_name, func_name="getData", report_name=None,
                    folder="sources", path=None):
        """ Returns data from a internal data service defined in the sources folder.

        :param http_data: The input data for the service
        :param file_name: The service file name
        :param func_ame: Optional, the function name in the service. Default getData
        :param report_name: Optional, the report name. Default the current one
        :param folder: Optional, the folder with the services. Default sources
        :param path: Optional, the path to be added to the python system path
        """
        file_name = file_name.replace(".py", "")
        if path is not None:
            if path not in sys.path:
                sys.path.append(path)
            if folder is not None:
                mod = importlib.import_module("%s.%s" % (folder, file_name))
            else:
                mod = importlib.import_module(file_name)
        else:
            if report_name is None:
                report_name = self.page.run.report_name
            mod = importlib.import_module("%s.%s.%s" % (report_name, folder, file_name))
        return getattr(mod, func_name)(self.page, http_data)

    def from_get(self, url, data=None, code=None):
        """ """
        return JsQuery.JQuery(self.page).get(url, data)

    def pdf(self, filename, path=None):
        """Read a pdf file

        This will require an external module PyPDF2.

        Usage::

          data = page.data.pdf("document.pdf", r"")
          data.getPage(0)

        `Doc <https://www.geeksforgeeks.org/working-with-pdf-files-in-python/>`_

        :param filename: The pdf file name
        :param path: The file path

        :return: A pdf object from PyPDF2
        """
        pyPDF2 = requires("PyPDF2", reason='Missing Package', install='PyPDF2', source_script=__file__,
                          raise_except=True)
        pdf_data = pyPDF2.PdfFileReader(os.path.join(path, filename))
        return pdf_data

    def soap(self, wsdl):
        """Interface to a SOAP server.

        This function will require an external python package zeep to use SOAP

        Usage::

          soap = page.data.soap("http://www.soapclient.com/xml/soapresponder.wsdl")
          soap.Method1('Zeep', 'is cool')

        `wikipedia <https://en.wikipedia.org/wiki/SOAP>`_
        `Zeep <https://python-zeep.readthedocs.io/en/master/>`_

        :param wsdl: The wsdl service url
        :rtype: zeep.service

        :return: The SOAP services
        """
        soap = requires("zeep", reason='Missing Package', install="zeep", source_script=__file__, raise_except=True)
        return soap.Client(wsdl).service

    def rest(self, url, data=None, method=None, encoding='utf-8', headers=None, unverifiable=False, proxy=None):
        """Interface to a REST server.

        Test with a online server can be done here https://jsonplaceholder.typicode.com/

        Usage::

          page.data.rest("https://jsonplaceholder.typicode.com/posts/1", method="PUT")

        `jsonrpc <https://jsonrpcclient.readthedocs.io/en/latest/api.html>`_

        :param url: The REST service url
        :param data: The input data for the service
        """
        return json.loads(self.page.py.request(url, data, method, encoding, headers, unverifiable, proxy=proxy))

    def socket(self, data, host: str = 'localhost', port: int = 5000, encoding: str = 'utf-8'):
        """

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
        """Entry point to retrieve RSS feeds.

        This module will require beautifulsoup4 as external package

        Usage::

          xml_soup = rptObj.data.rss("http://feeds.reuters.com/reuters/businessNews")
          for title in xml_soup.findAll('title'):
            print(title)

        `beautifulsoup4 <https://pypi.org/project/beautifulsoup4/>`_

        :param url: The url of the html page
        :param method: Optional, The request method. Default method GET

        :return: A xml object
        """
        bs4 = requires("bs4", reason='Missing Package', install='beautifulsoup4', source_script=__file__,
                       raise_except=True)
        headers = {'User-Agent': 'Mozilla/5.0', 'accept': 'application/xml;q=0.9, */*;q=0.8'}
        response = self.page.py.requests.get(url, headers=headers, proxy=proxy)
        xml_soup = bs4.BeautifulSoup(response, )
        return xml_soup

    def webscrapping(self, url, parser="html.parser", proxy=None, method=None):
        """Entry point to retrieve data from any website.

        This module will require beautifulsoup4 as external package

        Usage::

          page.data.webscrapping("https://www.w3schools.com/colors/default.asp")
          xml_soup.findAll('title')

        `beautifulsoup4 <https://pypi.org/project/beautifulsoup4/>`_

        :param url: The url of the html page
        :param parser: The output data parser
        :param proxy:
        :param method:

        :return: A xml object
        """
        bs4 = requires("bs4", reason='Missing Package', install='beautifulsoup4', source_script=__file__,
                       raise_except=True)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        response = self.page.py.request(url, headers=headers, method=method, proxy=proxy)
        xml_soup = bs4.BeautifulSoup(response, parser)
        return xml_soup

    def rpc(self, url, data=None, headers=None, is_secured=False):
        """Interface to a RPC server.

        This is using the external python package jsonrpcclient (https://jsonrpcclient.readthedocs.io/en/latest/)

        `wikipedia <https://en.wikipedia.org/wiki/Rapid_control_prototyping>`_
        `gurujsonrpc <https://gurujsonrpc.appspot.com/>`_
        `jsonrpcclient <https://jsonrpcclient.readthedocs.io/en/latest/>`_

        :param url: The RPC service url
        :param data: The input data for the service
        """
        http_client = requires("jsonrpcclient.clients.http_client", reason='Missing Package',
                               install="jsonrpcclient[requests]", source_script=__file__, raise_except=True)
        client = http_client.HTTPClient(url)
        if headers is not None:
            client.session.headers.update(headers)
        if is_secured:
            client.session.auth = ("user", "pass")
        if data is None or "method" not in data:
            raise ValueError("data must of a method defined")

        return client.send(json.dumps(data))

    def grpc(self, service_name, path, module, host: str = "localhost", port: int = 50051):
        """Interface to a GRPC server.

        Usage::

          grpc = page.data.grpc(serviceName="GreeterStub", module="helloworld_pb2_grpc", path="")
          data = grpc.imp("helloworld_pb2").HelloRequest(name="Test")
          print(grpc.request("SayHello", data))

        `grpc <https://grpc.io/docs/tutorials/basic/python/>`_
        `grpc quickstart <https://grpc.io/docs/quickstart/python.html>`_

        :param service_name: The Service name (the class name in the python module)
        :param path: The path with the GRPC features
        :param module: The python module name for the service
        :param host: The service host name (e.g localhost)
        :param port: The service port

        :return: A GRPC wrapped object

        :rtype: DataGrpc.DataGrpc
        """
        requires("grpc", reason='Missing Package', install='grpcio', source_script=__file__, raise_except=True)
        return DataGrpc.DataGrpc(service_name, path, module, host, port)

    def to_hyr(self, data: List[dict], depth: List[str], values: List[str]) -> list:
        """Creates a hierarchy structure from a dataset

        :param data: A traditional dataset
        :param depth: hierarchy structure
        :param values: values retrieved in leaf nodes
        """
        tree, active_branch = {}, {}
        for rec in data:
            active_branch = tree
            for d in depth:
                if d not in rec:
                    break

                active_branch.setdefault(rec[d], {})
                active_branch = active_branch[rec[d]]
            for value in values:
                if value in rec:
                    active_branch[value] = rec.get(value, 0) + active_branch.get(value, 0)

        def process_node(branch: dict, hyr: list, path: list):
            for k, v in branch.items():
                if isinstance(v, dict):
                    path.append(k)
                    hyr.append({"name": k, "children": [], "path": "/".join(path)})
                    process_node(v, hyr[-1]["children"], path)
                else:
                    path.append(k)
                    hyr.append({"name": k, "value": v, "path": "/".join(path)})

        results = []
        process_node(tree, results, [])
        return results
