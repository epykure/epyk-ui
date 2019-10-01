"""
Internal wrapper for all the exports

"""

import os
import time
import json

from epyk.core.js import Imports
from epyk.core.js import Js
from epyk.core.js.Imports import requires

from epyk.core.html.templates import HtmlTmplBase
from epyk.core.html.templates import HtmlTmplJupyter


class OutBrowsers(object):
  def __init__(self, context):
    self._context = context

  def codepen(self, path=None, target="_blank"):
    """
    Update the Html launcher and send the data to codepen

    Documentation
    https://www.debuggex.com/cheatsheet/regex/python

    :return:
    """
    import re
    import webbrowser

    results = self._context._to_html_obj(content_only=True)
    js_external = re.findall('<script language="javascript" type="text/javascript" src="(.*?)"></script>', results['jsImports'])
    css_external = re.findall('<link rel="stylesheet" href="(.*?)" type="text/css">', results['cssImports'])
    jsObj = Js.JsBase()
    result = {"js": results["jsFrgs"], "js_external": ";".join(js_external), "css_external": ";".join(css_external), "html": results['content'], "css": results["cssStyle"]}
    data = jsObj.location.postTo("https://codepen.io/pen/define/", {"data": json.dumps(result)}, target=target)
    if path is None:
      path = os.path.join(os.getcwd(), "outs")
    else:
      path = os.path.join(path)
    if not os.path.exists(path):
      os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "RunnerCodepen.html"), "w") as f:
      f.write('<html><body></body><script>%s</script></html>' % data.replace("\\\\n", ""))
    webbrowser.open(os.path.join(path, "RunnerCodepen.html"))


class PyOuts(object):
  class __internal(object):
    _props, _context, jsOnLoadEvtsFnc = {}, {}, []

  def __init__(self, report=None):
    self._report = report
    self.excluded_packages = None

  def _to_html_obj(self, content_only=False):
    """
    Create the HTML result object from the report definition

    :param content_only: Optional. Boolean to remove all the frame of the report

    :return: A python dictionary with the HTML results
    """
    if not content_only:
      self._report.style.add('CssBody', cssRef='body')
      self._report.style.add('CssBodyContent', htmlId='page_content')
      self._report.style.add('CssBodyLoadingBack', htmlId='popup_loading_back')
      self._report.style.add('CssBodyLoading', htmlId='popup_loading')
    self._report.style.add('CssStandardLinks')
    self._report.style.add('CssTextSelection', cssRef='::selection')
    self._report.style.add('CssTextSelection', cssRef='::-moz-selection')

    htmlParts = []
    for objId in self._report.content:
      if content_only and self._report.htmlItems[objId].name == "Nav Bar":
        continue

      if self._report.htmlItems[objId].inReport:
        htmlParts.append(self._report.htmlItems[objId].html())

    onloadParts = []
    for k, v in self._report._props.get('js', {}).get('functions', {}).items():
      sPmt = "(%s)" % ", ".join(list(v["pmt"])) if "pmt" in v else "{}"
      onloadParts.append("function %s%s{%s}" % (k, sPmt, v["content"].strip()))

    for c, d in self._report._props['js'].get("constructors", {}).items():
      onloadParts.append(d)

    for c, d in self._report._props['js'].get("datasets", {}).items():
      onloadParts.append(d)

    for b in self._report._props['js'].get("builders", []):
      onloadParts.append(b)

    #for jsFnc in self._report.jsOnLoadFnc:
    #  onloadParts.append(str(jsFnc))
    #for jsFnc in self._report.jsFnc:
    #  onloadParts.append(str(jsFnc))
    #onloadParts.append(str(self._report.jsGlobal))

    importMng = Imports.ImportManager(online=True, report=self._report)

    results = {
      'cssStyle': "%s%s" % (self._report._css.toCss(), self._report._cssText),
      'content': "\n".join(htmlParts),
      'jsFrgs': ";".join(onloadParts),
      'cssImports': importMng.cssResolve(self._report.cssImport, self._report.cssLocalImports, excluded=self.excluded_packages),
      'jsImports': importMng.jsResolve(self._report.jsImports, self._report.jsLocalImports, excluded=self.excluded_packages)
    }
    return results

  def _repr_html_(self):
    """
    Standard output for Jupyter Notebooks.

    This is what will use IPython in order to display the results in cells.

    Documentation

    :return:
    """

    results = self._to_html_obj(content_only=True)
    return HtmlTmplJupyter.DATA.strip() % results

  def jupyterlab(self):
    """

    Documentation
    https://jupyter.org/

    :return:
    """
    self.excluded_packages = ['bootstrap']
    return self

  def jupyter(self):
    """

    Documentation
    https://jupyter.org/

    :return: The ouput object with the function _repr_html_
    """
    self.excluded_packages = ['bootstrap', 'jquery']
    return self

  def w3cTryIt(self, path=None, name=None):
    """
    This will produce everything in a single page which can be directly copied to the try editor in w3C website

    Documentation
    https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic

    :param path: The path in which the output files will be created
    :param name: The filename without the extension

    """
    if path is None:
      path = os.path.join(os.getcwd(), "outs", "w3schools")
    else:
      path = os.path.join(path, "w3schools")
    if not os.path.exists(path):
      os.makedirs(path, exist_ok=True)
    if name is None:
      name = int(time.time())
    file_path = os.path.join(path, "%s.html" % name)
    with open(file_path, "w") as f:
      f.write(self._repr_html_())
    return file_path

  def codepen(self, path=None, name=None):
    """

    Example

    Documentation
    https://codepen.io/

    :param path: The path in which the output files will be created
    :param name: The filename without the extension

    TODO Try to add the prefill
    https://blog.codepen.io/documentation/api/prefill/

    :return: The file path
    """
    self.jsfiddle(path, name, framework="codepen")

  def jsfiddle(self, path=None, name=None, framework="jsfiddle"):
    """
    Produce files which can be copied directly to https://jsfiddle.net in order to test the results and perform changes.

    The output is always in a sub directory jsfiddle

    Example

    Documentation
    https://jsfiddle.net/

    :param path: The path in which the output files will be created
    :param name: The filename without the extension

    :return: The file path
    """
    if path is None:
      path = os.path.join(os.getcwd(), "outs", framework)
    else:
      path = os.path.join(path, framework)
    if not os.path.exists(path):
      os.makedirs(path, exist_ok=True)
    if os.path.exists(path):
      if name is None:
        name = int(time.time())
      results = self._to_html_obj(content_only=True)
      # For the JavaScript builders
      with open(os.path.join(path, "%s.js" % name), "w") as f:
        f.write(results["jsFrgs"])

      # FOr all the doms and imports
      with open(os.path.join(path, "%s.html" % name), "w") as f:
        f.write("%s\n" % results["cssImports"])
        f.write("%s\n" % results["jsImports"])
        f.write(results["content"])

      # For the CSS styles
      with open(os.path.join(path, "%s.css" % name), "w") as f:
        f.write(results["cssStyle"])
    return path

  def html_file(self, path=None, name=None):
    """

    :param path: The path in which the output files will be created
    :param name: The filename without the extension

    :return: The file full path
    """
    if path is None:
      path = os.path.join(os.getcwd(), "outs", "html")
    else:
      path = os.path.join(path, "html")
    if not os.path.exists(path):
      os.makedirs(path, exist_ok=True)
    if name is None:
      name = int(time.time())
    file_path = os.path.join(path, "%s.html" % name)
    with open(file_path, "w") as f:
      results = self._to_html_obj()
      f.write(HtmlTmplBase.DATA % results)
    return file_path

  def markdown_file(self, path=None, name=None):
    """
    Writes a Markdown file from the report object

    :param path: The path in which the output files will be created
    :param name: The filename without the extension

    :return: The file path
    """
    if path is None:
      path = os.path.join(os.getcwd(), "outs", "markdowns")
    else:
      path = os.path.join(path, "markdowns")
    if not os.path.exists(path):
      os.makedirs(path, exist_ok=True)
    if os.path.exists(path):
      if name is None:
        name = "md_%s.amd" % int(time.time())

      file_Path = os.path.join(path, name)
      with open(file_Path, "w") as f:
        for objId in self._report.content:
          html_obj = self._report.htmlItems[objId]
          if hasattr(html_obj, "to_markdown"):
            f.write("%s\n" % html_obj.to_markdown(html_obj.vals))
      return file_Path

  def str(self):
    """

    :return:
    """

  def pdf(self):
    """

    :return:
    """
    self.word()
    # Then save the file to pdf

  def word(self, path=None, name=None):
    """
    Writes the result to an Word document

    :param path: The path in which the output files will be created
    :param name: The filename without the extension

    :return:
    """
    from docx import Document
    from docx.shared import RGBColor

    if path is None:
      path = os.path.join(os.getcwd(), "outs", "office")
    else:
      path = os.path.join(path, "office")
    if not os.path.exists(path):
      os.makedirs(path, exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.gmtime())
    name = name or 'word_%s.docx' % timestamp
    document = Document()
    for objId in self._report.content:
      if self._report.htmlItems[objId].inReport:
        try:
          self._report.htmlItems[objId].to_word(document)
        except Exception as err:
          error_title = document.add_heading().add_run("Error")
          error_title.font.color.rgb = RGBColor(255, 0, 0)
          error_title.font.italic = True
          error_paragraph = document.add_paragraph().add_run((str(err)))
          error_paragraph.font.color.rgb = RGBColor(255, 0, 0)
          error_paragraph.font.italic = True
    document.save(os.path.join(path, name))
    return name

  def excel(self, path=None, name=None):
    """
    Writes the result to an Excel document

    :param path: The path in which the output files will be created
    :param name: The filename without the extension

    :return:
    """
    xls = requires("xlsxwriter", reason='Missing Package', install='xlsxwriter', source_script=__file__)

    if path is None:
      path = os.path.join(os.getcwd(), "outs", "office")
    else:
      path = os.path.join(path, "office")
    if not os.path.exists(path):
      os.makedirs(path, exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.gmtime())
    name = name or '%s_%s.xlsx' % (self._report.run.script_name, timestamp)
    workbook = xls.Workbook(os.path.join(path, name))
    worksheet = workbook.add_worksheet()
    cursor = {'row': 0, 'col': 0}
    for objId in self._report.content:
      if self._report.htmlItems[objId].inReport:
        try:
          self._report.htmlItems[objId].to_xls(workbook, worksheet, cursor)
        except Exception as err:
          cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
          worksheet.write(cursor['row'], 0, str(err), cell_format)
          cursor['row'] += 2
    workbook.close()
    return name

  def power_point(self):
    """

    :return:
    """

  @property
  def browser(self):
    """
    This module will require the package webbrowser.
    It will allow outputs to be created directly in the webpages (without using intermediary text files
    """
    return OutBrowsers(self)
