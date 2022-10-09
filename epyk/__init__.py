import json
import inspect

from typing import List, Union, Callable
from epyk.core import Page as Rpt
from epyk._version import __version__
from epyk.core.data import events
from epyk.core.data import configs
from epyk.core.data import datamap as js_datamap
from epyk.core.data import components as inputs
from epyk.core.html import Defaults as settings
from epyk.core.html.symboles import Symboles as symboles

from epyk.core.css import themes
from epyk.core.css import Defaults as settings_css
from epyk.core.css import Colors as colors
from epyk.core.css.themes import palettes
from epyk.core.css.styles.attributes import CssInline

# Add JavaScript shortcuts
from epyk.core.js import std as js_std
from epyk.core.js import expr as js_expr
from epyk.core.js import libs as js_libs
from epyk.core.js.JsUtils import jsWrap as js_callback

from epyk.core.js.Imports import Package as package
from epyk.core.js.Imports import PACKAGE_STATUS, JS_IMPORTS, CSS_IMPORTS

from epyk.web import jupyter

Page = Rpt.Report

LOG_SERVICE = None


def rename_css_cls(mappings: dict):
  """  Change the name of the CSS classes in the framework.
  This function need to be used before the creation of any component in the page.

  This will not change the content. it will only rename them.
  To remove a CSS class or to change it in a component type have a look at components_skin

  :param dict mappings: The CSS class names to be renamed
  """
  from epyk.core.css import Classes

  Classes.OVERRIDES = mappings


def packages_black_list(pkgs_alias: List[str], raise_exception: bool = True):
  """
  All packages in this list will be considered as forbidden.
  The other packages will be authorised.

  :param List[str] pkgs_alias: A list of packages reference
  :param bool raise_exception: Optional. The kind of error triggered
  """
  global PACKAGE_STATUS

  for pkg in pkgs_alias:
    if raise_exception:
      PACKAGE_STATUS[pkg] = {"allowed": False}
    else:
      PACKAGE_STATUS[pkg] = {"allowed": True, "info": "Package in Black list"}


def packages_white_list(pkgs_alias: List[str], raise_exception: bool = True):
  """
  Description:
  -----------
  All packages not in those lists will be considered as forbidden.

  :param List[str] pkgs_alias: A list of packages reference
  :param bool raise_exception: Optional. The kind of error triggered
  """
  global PACKAGE_STATUS

  for js_pkg in JS_IMPORTS:
    if js_pkg in pkgs_alias:
      PACKAGE_STATUS[js_pkg] = {"allowed": True}
    else:
      if raise_exception:
        PACKAGE_STATUS[js_pkg] = {"allowed": False}
      else:
        PACKAGE_STATUS[js_pkg] = {"allowed": True, "info": "Missing from white list"}
  for css_pkg in CSS_IMPORTS:
    if css_pkg in pkgs_alias:
      PACKAGE_STATUS[css_pkg] = {"allowed": True}
    else:
      if raise_exception:
        PACKAGE_STATUS[css_pkg] = {"allowed": False}
      else:
        PACKAGE_STATUS[css_pkg] = {"allowed": True, "info": "Missing from white list"}


class Interface:
  """ Quick interface for building dashboards.

  """
  def __init__(self, inputs: dict, outputs: dict = None, event: dict = None, verbose: bool = False):
    self.page = Page()
    out_components, in_components = [], []
    for i, inp in enumerate(inputs):
      component = self.__build_comp(inp, i, verbose=verbose)
      if component is not None:
        in_components.append(component)
      else:
        print("%s not defined" % inp)

    for j, out in enumerate(outputs, start=1):
      component = self.__build_comp(out, i+j)
      if component is not None:
        out_components.append(component)
      else:
        print("%s not defined" % out)

    if event is not None:
      btn = self.page.ui.buttons.large("Run", align="center", options={"colored": True})
      btn.style.css.margin_top = 10
      inputs_comps = []
      for comp in in_components:
        if hasattr(comp, 'input'):
          inputs_comps.append(getattr(comp, 'input'))
        else:
          inputs_comps.append(comp)
      btn.click(
        getattr(self.page.js, event.get("method", "get").lower())(event["url"], components=inputs_comps).onSuccess([
          out_components[0].build(events.data)
      ]))
      in_components.append(btn)
    self.page.ui.row([in_components, out_components], position="top")

  def __build_comp(self, inp: Union[str, dict], i: int = None, verbose: bool = False):
    comp = None
    if isinstance(inp, dict):
      pos = self.page.ui
      is_valid = True
      for frg in inp["type"].split("."):
        if hasattr(pos, frg):
          pos = getattr(pos, frg)
        else:
          is_valid = False
          break

      if is_valid:
        pmts = {}
        funcs_args = inspect.getfullargspec(pos)[0][1:]
        if verbose:
          print("%s got arguments %s" % (pos.__name__, funcs_args))
        for arg_name in funcs_args:
          if arg_name in inp:
            pmts[arg_name] = inp[arg_name]
        if "html_code" not in pmts:
          pmts["html_code"] = "comp_%s" % i
        comp = pos(**pmts)
        if 'css' in inp:
          comp.css(inp["css"])
        if 'class' in inp:
          comp["attr"]["class"].add(inp["class"])
    else:
      pos = self.page.ui
      is_valid = True
      for frg in inp.split("."):
        if hasattr(pos, frg):
          pos = getattr(pos, frg)
        else:
          is_valid = False
          break

      if is_valid:
        comp = pos(html_code="comp_%s" % i)
    return comp

  def launch(self):
    if jupyter.is_notebook():
      return self.page.outs.jupyter(closure=False)

    return self.page.outs.html()
