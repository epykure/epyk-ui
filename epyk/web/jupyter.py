
import os
from epyk.core.js import JsUtils


class Jupyter:

  def __init__(self, page):
    self.page = page

  def requireJs(self, jsFncs=None, verbose=False, excluded_packages=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param verbose: Boolean. Optional. Display version details (default False).

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
    import notebook

    nb_path = os.path.split(notebook.__file__)[0]
    return os.listdir(os.path.join(nb_path, 'static', 'components'))

