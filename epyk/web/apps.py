
import sys
import os

from epyk.web import angular
from epyk.web import vue
from epyk.web import react


class AppRoute(object):

  def __init__(self, page):
    self.page = page

  def angular(self, server, app, selector=None, name=None):
    """
    Description:
    ------------

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
