"""
This module will propose an implementation of a GPRC call.

THis module has been designed based on the examples available here: https://github.com/grpc/grpc/tree/v1.23.0
"""

import sys
import importlib


class DataGrpc:

  def __init__(self, service_name: str, path: str, module: str, host: str, port: int):
    """
    Description:
    ------------
    The path will be added to the python path.

    Attributes:
    ----------
    :param str service_name: The Service name (the class name in the python module).
    :param str path: The path with the GRPC features.
    :param str module: The python module name for the service.
    :param str host: The service host name (e.g localhost).
    :param int port: The service port.
    """
    if path not in sys.path:
      sys.path.append(path)
    self.host, self.port, self.module = host, port, module.replace(".py", "")
    self.service_name, self._libs = service_name, {}
    if not module.endswith("_grpc"):
      raise ValueError("Service module should ends with _grpc")

  @property
  def py(self):
    """
    Description:
    -----------
    Return the main module in the GRPC service for the data.
    Namely is return the module without the _grpc.

    Usage:
    -----

      grpc.py.HelloRequest(name="Test 3")

    :return: A python module
    """
    return self.imp(self.module.replace("_grpc", ""))

  def imp(self, module: str):
    """
    Description:
    -----------
    Return any module from the GRPC service based on its module name.

    Usage:
    -----

      grpc.imp(self.module)

    Attributes:
    ----------
    :param str module: The python module name.

    :return: A python module
    """
    module = module.replace(".py", "")
    if module not in self._libs:
      self._libs[module] = importlib.import_module(module)
    return self._libs[module]

  def request(self, method: str, data: dict = None, options: dict = None):
    """
    Description:
    -----------
    Run the GRPC call from the service definition in the init.

    Usage:
    -----

      grpc.request("SayHello", data)

    Attributes:
    ----------
    :param str method: The function name to be called for the request.
    :param dict data: Optional. The data to be passed during the call.
    :param dict options: Optional. The GRPC service call options.
    """
    import grpc

    with grpc.insecure_channel(target="%s:%s" % (self.host, self.port), options=options) as channel:
      stub = getattr(self.imp(self.module), self.service_name)(channel)
      return getattr(stub, method)() if data is None else getattr(stub, method)(data)
