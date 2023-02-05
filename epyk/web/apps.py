
import sys
import os

from epyk.core.py import primitives
from epyk.web import angular
from epyk.web import svelte
from epyk.web import vue
from epyk.web import react
from epyk.web import jupyter


class AppRoute:

  def __init__(self, page: primitives.PageModel):
    self.page = page

  def angular(self, server, app, selector: str = None, name: str = None) -> angular.Angular:
    """ Entry point to a local Angular setup.
    This will allow the framework to convert modules and integrate them to an external Angular App.

    If selector or name is defined a page will be added to the app.

    :param server:
    :param app:
    :param str selector:
    :param str name:
    """
    name = name or os.path.split(sys.argv[0])[1][:-3]
    selector = selector or os.path.split(sys.argv[0])[1][:-3]
    ang_app = angular.Angular(server, app, page=self.page)
    if selector is not None or name is not None:
      ang_app.page(selector, name)
    return ang_app

  def react(self, server, app, selector: str = None, name: str = None) -> react.React:
    """ Entry point to a local React setup.
    This will allow the framework to convert modules and integrate them to an external React App.

    If selector or name is defined a page will be added to the app.

    :param server:
    :param app:
    :param selector:
    :param name:
    """
    name = name or os.path.split(sys.argv[0])[1][:-3]
    selector = selector or os.path.split(sys.argv[0])[1][:-3]
    react_app = react.React(app_path=server, name=app, page=self.page)
    if selector is not None or name is not None:
      react_app.page(selector, name)
    return react_app

  def vue(self, server, app, selector: str = None, name: str = None) -> vue.VueJs:
    """ Entry point to a local Vue setup.
    This will allow the framework to convert modules and integrate them to an external Vue App.

    If selector or name is defined a page will be added to the app.

    :param server:
    :param app:
    :param selector:
    :param name:
    """
    name = name or os.path.split(sys.argv[0])[1][:-3]
    selector = selector or os.path.split(sys.argv[0])[1][:-3]
    vue_app = vue.VueJs(app_path=server, name=app, page=self.page)
    if selector is not None or name is not None:
      vue_app.page(selector=selector, name=name)
    return vue_app

  def svelte(self, server, app, selector: str = None, name: str = None) -> svelte.Svelte:
    ...

  @property
  def jupyter(self):
    """ Entry point to a local Jupyter configuration.
    This will provide some information concerning the configuration of the local Jupyter instance.

    """
    return jupyter.Jupyter(self.page)

