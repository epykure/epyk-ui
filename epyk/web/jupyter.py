
import os
from typing import Any
from epyk.core.js import JsUtils
from epyk.core.py import PyNpm
from epyk.core.css import Defaults as Defaults_css
from epyk.web.components import widgets


def is_notebook() -> bool:
  """ Function to check if the code is running in a Jupyter notebook.
  """
  try:
    from IPython import get_ipython

    if "IPKernelApp" not in get_ipython().config:  # pragma: no cover
      raise ImportError("console")
      return False

    if "VSCODE_PID" in os.environ:  # pragma: no cover
      raise ImportError("vscode")
      return False

  except:
    return False
  else:  # pragma: no cover
    return True


def js_store_var(var_name: str, event_data: Any):
  """ Store JavaScript results to a Python variable.

  Usages::

    # In a cell in a Jupyter notebook
    btn = page.ui.button("Click")
    btn.click([
        page.js.get("http://127.0.0.1:5000/autocomplete").onSuccess([
            pk.jupyter.js_store_var('foo', pk.events.data)
        ])
    ])

  :param var_name: The Python variable name
  :param event_data: The JavaScript returned data
  :return: Nothing but store the result to a python variable
  """
  return JsUtils.jsWrap('IPython.notebook.kernel.execute("%s=" + JSON.stringify(%s))' % (var_name, event_data))


class NotebookJsCell:

  def __init__(self, cell_ref):
    self._cell_ref = cell_ref

  def run(self):
    """  

    :return:
    """
    return JsUtils.jsWrap("window.Jupyter.notebook.execute_cells([%s])" % self._cell_ref)

  def hide(self):
    """  

    :return:
    """
    return JsUtils.jsWrap("$(Jupyter.notebook.get_cell(%s).element).hide()" % self._cell_ref)

  def show(self):
    """  

    :return:
    """
    return JsUtils.jsWrap("$(Jupyter.notebook.get_cell(%s).element).show()" % self._cell_ref)


class NotebookJs:

  def set_python_from_component(self, name, component):
    """  

    :param name:
    :param component:
    """
    if hasattr(component, "dom"):
      return "window.Jupyter.notebook.kernel.execute(\"%s = \" + JSON.stringify(%s)  + \"\")" % (
        name, component.dom.content.toStr())

    return "window.Jupyter.notebook.kernel.execute(\"%s = '\" + %s  + \"'\")" % (
      name, JsUtils.jsConvertData(component, None))

  def run_cell(self, i, hide: bool = True):
    """ Run the cell based on indices in the notebook.

    :param i: The cells indices
    :param hide: Optional. hide the cell once run. Default True
    """
    if isinstance(i, int):
      i = [i]
    return "window.Jupyter.notebook.execute_cells(%s)" % i

  @property
  def next_cell(self):
    return NotebookJsCell(
      "window.Jupyter.notebook.get_cell_elements().index($(event.target).parents('.cell'))+1")

  def cell_below(self, index: int):
    return NotebookJsCell(
      "window.Jupyter.notebook.get_cell_elements().index($(event.target).parents('.cell'))+%s" % index)

  def run_next_cells(self, n, start: int = 0, hide: bool = True):
    """ Run a list of cells located after the running one.

    :param n: The number of cells to run
    :param start: Optional. The index for the first table
    :param hide: Optional. hide the cell once run. Default True
    """
    return JsUtils.jsWrap('''
(function(n, start){
  var currentCell = window.Jupyter.notebook.get_cell_elements().index($(event.target).parents('.cell'))+ 1 + start;
  var compCells = []; for (i=0; i < n; i++){compCells.push(currentCell+i)}
  window.Jupyter.notebook.execute_cells(compCells)
})(%s, %s)''' % (n, start))

  def current_cell_id(self):
    """ Get the id of the current cell.
    """
    return JsUtils.jsWrap("window.Jupyter.notebook.get_cell_elements().index($(event.target).parents('.cell'))")


class NotebookDisplay:

  def __init__(self):
    self._html, self._js, self._css = [], {"start": [], "end": []}, []
    self.page = None

  def full_width(self, page=None):
    """ Shortcut to set the width for a Jupyter page.

    :param page: Optional. The web page or cell in the Jupyter notebook
    """
    self.page = page or self.page
    return self.style_container({"width": "100%"})

  def full_page(self, page=None):
    """ Shortcut to set the width for a Jupyter page.

    :param page: Optional. The web page or cell in the Jupyter notebook
    """
    self.page = page or self.page
    self.style_container({"width": "100%"})
    self.style_prompt({"min-width": 0}, page=page)
    self.style_notebook({"padding-top": 0, "padding-bottom": 0}, page=page)
    if self.page is not None:
      self.page.properties.css.add_text(".end_space {min-height: 0}")
      return self

    else:
      return self.css(".end_space {min-height}")

  def style_notebook(self, attrs: dict, important: bool = True, page=None):
    """  

    :param attrs:
    :param important:
    :param page:
    :return:
    """
    self.page = page or self.page
    if self.page is not None:
      self.page.properties.css.add_text("#notebook {%s}" % Defaults_css.inline(attrs, important))
      return self

    else:
      return self.css("#notebook {%s}" % Defaults_css.inline(attrs, important))

  def style_prompt(self, attrs: dict, important: bool = True, page=None):
    """  

    :param attrs:
    :param important:
    :param page:
    :return:
    """
    self.page = page or self.page
    if self.page is not None:
      self.page.properties.css.add_text(".prompt {%s}" % Defaults_css.inline(attrs, important))
      return self

    else:
      return self.css(".prompt {%s}" % Defaults_css.inline(attrs, important))

  def style_container(self, attrs: dict, important: bool = True, page=None):
    """ Set the CSS style for the container page in a Jupyter Notebook.

    Usage::

      page = pk.Page()
      pk.jupyter.Notebook.display.full_width(page)

    :param attrs: The key, value pairs with the CSS attributes
    :param important: Optional. Set all the CSS attributes are important
    :param page: Optional. The web page or cell in the Jupyter notebook
    """
    self.page = page or self.page
    if self.page is not None:
      self.page.properties.css.add_text(".container {%s}" % Defaults_css.inline(attrs, important))
      return self

    else:
      return self.css(".container {%s}" % Defaults_css.inline(attrs, important))

  def clear_toolbar(self):
    """  
    """
    return self.javascript('''
$('#maintoolbar-container').find('div.btn-group:not([id])').remove();
''')

  def add_toolbar_button(self, name, icon='fa-terminal', callback=""):
    """  

    https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/JavaScript%20Notebook%20Extensions.html

    :param name:
    :param icon:
    :param callback:
    """
    return self.javascript('''
var toolbarItemValid = true;
$('#maintoolbar-container').find('div.btn-group:not([id])').each(function(item){
  if(this.innerText == '%(name)s'){toolbarItemValid = false}});
if (toolbarItemValid){
  window.Jupyter.toolbar.add_buttons_group([{'label': '%(name)s', 'icon': '%(icon)s', 'callback': function(){%(js)s}}])}
''' % {"name": name, "icon": icon, "js": callback})

  def css(self, text: str):
    """  
    Add CSS Style to the rendered cell.

    Usage::

      pk.jupyter.Notebook.display.css("button {color:green}")

    :param text: The CSS style.
    """
    self._css.append(text)
    return self

  def javascript(self, text: str, start: bool = True):
    """ Add JavaScript string fragments to the rendered cell.

    Usage::

      pk.jupyter.Notebook.display.javascript('''
        document.getElementById('myButton').addEventListener('click', function(e){
          alert('ok')
        });
        ''', start=False)

    :param text: String. The JavaScript string.
    :param start: Boolean. Optional. Specify the location on the page.
    """
    if start:
      self._js["start"].append(text)
    else:
      self._js["end"].append(text)
    return self

  def html(self, text: str):
    """ Add HTML component to the page.

    Usage::

      pk.jupyter.Notebook.display.html("<button id='but'>click</button>")

    :param text: The HTML component definition
    """
    self._html.append(text)
    return self

  def _repr_html_(self):
    frgs = []
    if self._css:
      frgs.append("<style>%s</style>" % "\n".join(self._css))
    if self._js["start"]:
      frgs.append("<script>%s</script>" % ";".join(self._js["start"]))
    if self._html:
      frgs.append("<HTML>%s</HTML>" % "".join(self._html))
    if self._js["end"]:
      frgs.append("<script>%s</script>" % ";".join(self._js["end"]))
    return "".join(frgs)


class Notebook:
  widgets = widgets
  js = NotebookJs()
  display = NotebookDisplay()


class Jupyter:

  def __init__(self, page):
    self.page = page

  @property
  def online(self):
    """ Define the route for the external packages sources.

    TODO: Fix this to integrate it properly to Jupyter.
    """
    return self.page.imports.online

  @online.setter
  def online(self, flag: bool):
    self.page.imports.online = flag
    if not flag:
      self.page.imports.static_url = "/static/components"# self.components_path

  def requireJs(self, js_funcs=None, verbose: bool = False, excluded_packages: list = None):
    """ Get the requirements generated by the page using requireJs package.
    This object can then be passed to the outs.jupyter() method in order to override the cell definition.

    :param js_funcs: Javascript functions
    :param verbose: Optional. Display version details (default False)
    :param excluded_packages: Optional.
    """
    results = self.page.outs._to_html_obj()
    import_mng = self.page.imports
    if js_funcs is not None:
      results["jsFrgs"] = "%s;%s" % (JsUtils.jsConvertFncs(js_funcs, toStr=True), results["jsFrgs"])
    require_js = import_mng.to_requireJs(
      results, excluded_packages or ['bootstrap', 'jquery', 'moment', 'jqueryui', 'mathjax'])
    if verbose:
      print(require_js)
    results['paths'] = "{%s}" % ", ".join(["%s: '%s'" % (k, p) for k, p in require_js['paths'].items()])
    results['jsFrgs_in_req'] = require_js['jsFrgs']
    return results

  def requirejs_path(self, js_funcs=None, verbose: bool = False, excluded_packages: list = None):
    """  
    Return the requirejs path dictionary.

    :param js_funcs: Javascript functions
    :param verbose: Optional. Display version details (default False)
    :param excluded_packages: Optional.
    """
    return self.requireJs(js_funcs, verbose, excluded_packages)["paths"]

  def requirejs_func(self, js_funcs=None, verbose: bool = False, excluded_packages: list = None):
    """ Return the requirejs path functions as a string.

    :param js_funcs: Javascript functions
    :param verbose: Boolean. Optional. Display version details (default False)
    :param excluded_packages: Optional.
    """
    return self.requireJs(js_funcs, verbose, excluded_packages)["jsFrgs_in_req"]

  def add_cell(self, html_code: str):
    pass

  def cut_cell(self, html_code: str):
    pass

  @property
  def built_in(self):
    """ Get the list of external packages installed to the Jupyter instance.
    """
    return os.listdir(self.components_path)

  @property
  def components_path(self):
    """ Get the path of the Jupyter external packages.
    """
    import notebook

    nb_path = os.path.split(notebook.__file__)[0]
    return os.path.join(nb_path, 'static', 'components')

  def update(self, package, version=None):
    pass

  def add(self, package, update: bool = False, verbose: bool = False):
    """  

    :param package: Optional. A list of packages to download
    :param update: Optional. Flag to specify if the files need to be uploaded again
    :param verbose: Optional. Display version details (default True)
    """
    PyNpm.download(self.components_path, update=update, verbose=verbose, packages=[package])

  def install_packages(self, update: bool = False, verbose: bool = False):
    """  

    :param update: Optional. Flag to specify if the files need to be uploaded again
    :param verbose: Optional. Display version details (default True)
    """
    PyNpm.download(self.components_path, update=update, verbose=verbose, page=self.page)
