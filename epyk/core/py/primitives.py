"""
Module dedicated to help on the type hinting
"""

from typing import Optional, Union, Any
from abc import ABC, abstractmethod


class JsDataModel(ABC):

  @abstractmethod
  def toStr(self) -> str:
    pass


class DomModel:
  content = None
  varId = None
  events = None
  isInViewPort = None
  classList = None
  jquery = None

  def getAttribute(self, value):
    ...

  def setAttribute(self, name, value):
    ...

  def css(self, type: Union[dict, str], data: Union[str, JsDataModel] = None, duration: int = None):
    ...

  def hide(self):
    ...

  def show(self):
    ...


class OptionModel:
  verbose = False
  config_default = None


class HtmlModel:
  htmlCode = None
  style = None
  name = None
  options = None
  _browser_data = None
  var = None
  is_range = None # For slider component

  @property
  @abstractmethod
  def dom(self) -> DomModel:
    ...

  @property
  @abstractmethod
  def options(self) -> OptionModel:
    ...

  @abstractmethod
  def css(self, attrs: dict):
    ...

  @abstractmethod
  def html(self):
    ...

  def set_attrs(self, attrs: Optional[dict] = None, name: Optional[str] = None, value: Optional[Any] = None):
    ...

  jsImports = None
  cssImport = None
  _browser_data = None
  attr = None
  page = None

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    ...


class PageModel:
  _props = None
  _contextMenu = None
  imports = None
  jsImports = None
  cssImport = None
  ext_packages = None
  verbose = False
  components = None
  properties = None
  json_config_file = None
  body = None
  headers = None
  profile = False
  js = None
  css = None
  ui = None
  theme = None
  web = None
  inputs = None
  py = None
  user = None
  entities = None

  @property
  @abstractmethod
  def style(self):
    ...


class CssClsModel:
   classname = None
