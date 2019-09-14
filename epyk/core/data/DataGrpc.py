"""
This module will propose an implementation of a GPRC call.

THis module has been designed based on the examples available here: https://github.com/grpc/grpc/tree/v1.23.0
"""

import sys
import importlib


class DataGrpc(object):
  def __init__(self, service_name, path, module, host, port):
    """
    The path will be added to the python path

    :param service_name: The Service name (the class name in the python module)
    :param path: The path with the GRPC features
    :param module: The python module name for the service
    :param host: The service host name (e.g localhost)
    :param port: The service port
    """
    if not path in sys.path:
      sys.path.append(path)
    self.host, self.port, self.module = host, port, module.replace(".py", "")
    self.service_name, self._libs = service_name, {}
    if not module.endswith("_grpc"):
      raise Exception("Service module should ends with _grpc")

  @property
  def py(self):
    """
    Return the main module in the GRPC service for the data.
    Namely is return the module without the _grpc

    Example
    grpc.py.HelloRequest(name="Test 3")

    :return: A python module
    """
    return self.imp(self.module.replace("_grpc", ""))

  def imp(self, module):
    """
    Return any module from the GRPC service based on its module name

    Example
    grpc.imp(self.module)

    :param module: The python module name

    :return: A python module
    """
    module = module.replace(".py", "")
    if not module in self._libs:
      self._libs[module] = importlib.import_module(module)
    return self._libs[module]

  def request(self, method, data=None, options=None):
    """
    Run the GRPC call from the service definition in the init

    Example
    grpc.request("SayHello", data)

    :param method: The function name to be called for the request
    :param data: The data to be passed during the call
    :param options: The GRPC service call options

    :return:
    """
    import grpc

    with grpc.insecure_channel(target="%s:%s" % (self.host, self.port), options=options) as channel:
      stub = getattr(self.imp(self.module), self.service_name)(channel)
      if data is None:
        results = getattr(stub, method)()
      else:
        results = getattr(stub, method)(data)
      return results
