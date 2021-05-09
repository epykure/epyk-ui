
import sys
import os

from epyk.web import angular
from epyk.web import vue
from epyk.web import react
from epyk.web import jupyter


class AppRoute:

  def __init__(self, page):
    self.page = page

  def angular(self, server, app, selector=None, name=None):
    """
    Description:
    ------------
    Entry point to a local Angular setup.
    This will allow the framework to convert modules and integrate them to an external Angular App.

    Attributes:
    ----------
    :param server:
    :param app:
    :param selector:
    :param name:
    """
    name = name or os.path.split(sys.argv[0])[1][:-3]
    selector = selector or os.path.split(sys.argv[0])[1][:-3]
    return angular.Angular(server, app).page(selector, name, report=self.page)

  def react(self, server, app, selector=None, name=None):
    """
    Description:
    ------------
    Entry point to a local React setup.
    This will allow the framework to convert modules and integrate them to an external React App.

    Attributes:
    ----------
    :param server:
    :param app:
    :param selector:
    :param name:
    """
    name = name or os.path.split(sys.argv[0])[1][:-3]
    selector = selector or os.path.split(sys.argv[0])[1][:-3]
    return react.React(app_path=server, name=app).page(report=self.page, selector=selector, name=name)

  def vue(self, server, app, selector=None, name=None):
    """
    Description:
    ------------
    Entry point to a local Vue setup.
    This will allow the framework to convert modules and integrate them to an external Vue App.

    Attributes:
    ----------
    :param server:
    :param app:
    :param selector:
    :param name:
    """
    name = name or os.path.split(sys.argv[0])[1][:-3]
    selector = selector or os.path.split(sys.argv[0])[1][:-3]
    return vue.VueJs(app_path=server, name=app).page(report=self.page, selector=selector, name=name)

  @property
  def jupyter(self):
    """
    Description:
    ------------
    Entry point to a local Jupyter configuration.
    This will provide some information concerning the configuration of the local Jupyter instance.

    """
    return jupyter.Jupyter()

