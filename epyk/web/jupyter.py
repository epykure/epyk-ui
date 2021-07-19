
import os
from epyk.core.js import JsUtils
from epyk.core.py import PyNpm
from epyk.web.components import widgets


class NotebookJs:

  def set_python_from_component(self, name, component):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param component:
    """
    if hasattr(component, "dom"):
      return "window.Jupyter.notebook.kernel.execute(\"%s = '\" + %s  + \"'\")" % (name, component.dom.content.toStr())

    return "window.Jupyter.notebook.kernel.execute(\"%s = '\" + %s  + \"'\")" % (
      name, JsUtils.jsConvertData(component, None))

  def run_cell(self, i):
    """
    Description:
    ------------
    Run the cell based on indices in the notebook.

    Attributes:
    ----------
    :param i: List | Integer. The cells indices.
    """
    if isinstance(i, int):
      i = [i]
    return "window.Jupyter.notebook.execute_cells(%s)" % i

  def run_next_cell(self):
    """
    Description:
    ------------
    Run the next cell.
    """
    return JsUtils.jsWrap("window.Jupyter.notebook.execute_cells([window.Jupyter.notebook.get_cell_elements().index($(event.target).parents('.cell'))+1])")

  def run_next_cells(self, n, start=0):
    """
    Description:
    ------------
    Run a list of cells located after the running one.

    Attributes:
    ----------
    :param n: Integer. The number of cells to run.
    :param start: Integer. Optional. The index for the first table
    """
    return JsUtils.jsWrap('''
(function(n, start){
  var currentCell = window.Jupyter.notebook.get_cell_elements().index($(event.target).parents('.cell'))+ 1 + start;
  var compCells = []; for (i=0; i < n; i++){compCells.push(currentCell+i)}
  window.Jupyter.notebook.execute_cells(compCells)
})(%s, %s)''' % (n, start))

  def current_cell_id(self):
    """
    Description:
    ------------
    Get the id of the current cell.
    """
    return JsUtils.jsWrap("window.Jupyter.notebook.get_cell_elements().index($(event.target).parents('.cell'))")


class NotebookDisplay:

  def __init__(self):
    self._html, self._js, self._css = [], {"start": [], "end": []}, []

  def clear_toolbar(self):
    """
    Description:
    ------------

    :return:
    """
    return self.javascript('''
$('#maintoolbar-container').find('div.btn-group:not([id])').remove();
''')

  def add_toolbar_button(self, name, icon='fa-terminal', callback=""):
    """
    Description:
    ------------

    https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/JavaScript%20Notebook%20Extensions.html

    Attributes:
    ----------
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

  def css(self, text):
    """
    Description:
    ------------
    Add CSS Style to the rendered cell.

    Usage::

      pk.jupyter.Notebook.display.css("button {color:green}")

    Attributes:
    ----------
    :param text: String. The CSS style.
    """
    self._css.append(text)
    return self

  def javascript(self, text, start=True):
    """
    Description:
    ------------
    Add JavaScript string fragments to the rendered cell.

    Usage::

      pk.jupyter.Notebook.display.javascript('''
        document.getElementById('myButton').addEventListener('click', function(e){
          alert('ok')
        });
        ''', start=False)

    Attributes:
    ----------
    :param text: String. The JavaScript string.
    :param start: Boolean. Optional. Specify the location on the page.
    """
    if start:
      self._js["start"].append(text)
    else:
      self._js["end"].append(text)
    return self

  def html(self, text):
    """
    Description:
    ------------
    Add HTML component to the page.

    Usage::

      pk.jupyter.Notebook.display.html("<button id='but'>click</button>")

    Attributes:
    ----------
    :param text: String. The HTML component definition
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
    """
    Description:
    ------------
    Define the route for the external packages sources.

    TODO: Fix this to integrate it properly to Jupyter.
    """
    return self.page.imports.online

  @online.setter
  def online(self, flag):
    self.page.imports.online = flag
    if not flag:
      self.page.imports.static_url = "/static/components"# self.components_path

  def requireJs(self, jsFncs=None, verbose=False, excluded_packages=None):
    """
    Description:
    ------------
    Get the requirements generated by the page using requireJs package.
    This object can then be passed to the outs.jupyter() method in order to override the cell definition.

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param verbose: Boolean. Optional. Display version details (default False).
    :param excluded_packages: Optional.
    """
    results = self.page.outs._to_html_obj()
    importMng = self.page.imports
    if jsFncs is not None:
      results["jsFrgs"] = "%s;%s" % (JsUtils.jsConvertFncs(jsFncs, toStr=True), results["jsFrgs"])
    require_js = importMng.to_requireJs(
      results, excluded_packages or ['bootstrap', 'jquery', 'moment', 'jqueryui', 'mathjax'])
    if verbose:
      print(require_js)
    results['paths'] = "{%s}" % ", ".join(["%s: '%s'" % (k, p) for k, p in require_js['paths'].items()])
    results['jsFrgs_in_req'] = require_js['jsFrgs']
    return results

  def requirejs_path(self, jsFncs=None, verbose=False, excluded_packages=None):
    """
    Description:
    ------------
    Return the requirejs path dictionary.

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param verbose: Boolean. Optional. Display version details (default False).
    :param excluded_packages: Optional.
    """
    return self.requireJs(jsFncs, verbose, excluded_packages)["paths"]

  def requirejs_func(self, jsFncs=None, verbose=False, excluded_packages=None):
    """
    Description:
    ------------
    Return the requirejs path functions as a string.

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param verbose: Boolean. Optional. Display version details (default False).
    :param excluded_packages: Optional.
    """
    return self.requireJs(jsFncs, verbose, excluded_packages)["jsFrgs_in_req"]

  def add_cell(self, html_code):
    pass

  def cut_cell(self, html_code):
    pass

  @property
  def built_in(self):
    """
    Description:
    ------------
    Get the list of external packages installed to the Jupyter instance.
    """
    return os.listdir(self.components_path)

  @property
  def components_path(self):
    """
    Description:
    ------------
    Get the path of the Jupyter external packages.
    """
    import notebook

    nb_path = os.path.split(notebook.__file__)[0]
    return os.path.join(nb_path, 'static', 'components')

  def update(self, package, version=None):
    pass

  def add(self, package, update=False, verbose=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param package: List. Optional. A list of packages to download.
    :param update: Boolean, Optional. Flag to specify if the files need to be uploaded again.
    :param verbose: Boolean. Optional. Display version details (default True).
    """
    PyNpm.download(self.components_path, update=update, verbose=verbose, packages=[package])

  def install_packages(self, update=False, verbose=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param update: Boolean, Optional. Flag to specify if the files need to be uploaded again.
    :param verbose: Boolean. Optional. Display version details (default True).
    """
    PyNpm.download(self.components_path, update=update, verbose=verbose, page=self.page)
