"""
Internal wrapper for all the exports

"""

import os
import time

from epyk.core.js import Imports
from epyk.core.js.Imports import requires


class PyOuts(object):
  class __internal(object):
    _props, _context, jsOnLoadEvtsFnc = {}, {}, []

  def __init__(self, report=None):
    self._report = report

  def __to_html_obj(self, content_only=False):
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
      'cssImports': importMng.cssResolve(self._report.cssImport, self._report.cssLocalImports),
      'jsImports': importMng.jsResolve(self._report.jsImports, self._report.jsLocalImports)
    }
    return results

  def jupyterlab(self):
    """

    :return:
    """

  def jupyter(self):
    """

    :return:
    """

  def jsfiddle(self, path=None, name=None):
    """
    Produce files which can be copied directly to https://jsfiddle.net in order to test the results and perform changes.

    Example

    Documentation
    https://jsfiddle.net/

    :param path: The path in which the output files will be created
    :param name: The filename without the extension
    """
    if path is None:
      path = os.path.join(os.getcwd(), "outs", "jsfiddle")
      os.makedirs(path, exist_ok=True)
    if os.path.exists(path):
      if name is None:
        name = int(time.time())
      results = self.__to_html_obj(content_only=True)
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

  def html_file(self):
    """

    :return:
    """

  def markdown_file(self):
    """

    :return:
    """

  def str(self):
    """

    :return:
    """

  def pdf(self):
    """

    :return:
    """

  def word(self):
    """

    :return:
    """
    from docx import Document
    from docx.shared import RGBColor

    timestamp = time.strftime("%Y%m%d_%H%M%S", time.gmtime())
    docName = '%s_%s.docx' % (self._report.run.script_name, timestamp)
    document = Document()
    for objId in self.content:
      if self.htmlItems[objId].inReport:
        try:
          self.htmlItems[objId].to_word(document)
        except Exception as err:
          errotTitle = document.add_heading().add_run("Error")
          errotTitle.font.color.rgb = RGBColor(255, 0, 0)
          errotTitle.font.italic = True
          errorParagraph = document.add_paragraph().add_run((str(err)))
          errorParagraph.font.color.rgb = RGBColor(255, 0, 0)
          errorParagraph.font.italic = True
    savedPath = os.path.join(self._report.run.local_path, "saved")
    if not os.path.exists(savedPath):
      os.mkdir(savedPath)
    document.save(os.path.join(self._report.run.local_path, "saved", docName))
    return docName

  def excel(self):
    """

    :return:
    """
    xls = requires("xlsxwriter", reason='Missing Package', install='xlsxwriter', source_script=__file__)

    timestamp = time.strftime("%Y%m%d_%H%M%S", time.gmtime())
    docName = '%s_%s.xlsx' % (self._report.run.script_name, timestamp)
    xlsDocument = os.path.join(self._report.run.local_path, "saved", docName)
    workbook = xls.Workbook(xlsDocument)
    worksheet = workbook.add_worksheet()
    cursor = {'row': 0, 'col': 0}
    for objId in self.content:
      if self.htmlItems[objId].inReport:
        try:
          self.htmlItems[objId].to_xls(workbook, worksheet, cursor)
        except Exception as err:
          cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
          worksheet.write(cursor['row'], 0, str(err), cell_format)
          cursor['row'] += 2
    workbook.close()
    return docName

  def power_point(self):
    """

    :return:
    """

