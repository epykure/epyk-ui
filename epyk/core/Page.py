"""

"""

import os
import json
import importlib
import collections
import datetime
import time
import re
import logging

try:
  basestring
except NameError:
  basestring = str

from epyk.core.js import Imports
from epyk.interfaces import Components
from epyk.core.css.styles import GrpCls
from epyk.core.css.themes import Theme

from epyk.core import html
from epyk.core import js
from epyk.core import py
from epyk.core import data

from epyk.core.html import symboles
from epyk.core.html import entities


class OrderedSet(list):
  def __init__(self):
    super(OrderedSet, self).__init__()

  def add(self, key):
    if key not in self:
      self.append(key)


class ContextRun(object):
  __slots__ = ['mac_address', 'host_name', 'current_user', 'report_name', 'script_name', 'local_path', 'url_root', 'title', 'is_local', 'url', 'username']
  __internals_attrs = ['mac_address', 'local_path', 'is_local', 'url', 'username']

  def __init__(self, report_name=None, script_name=None, current_user="local", host_name="script", url_root='http://127.0.0.1', title=None, urlMaps=None):
    self.report_name, self.script_name = report_name, script_name
    self.current_user, self.host_name, self.mac_address, self.url_root = current_user, host_name, "", None
    self.url = "#"
    if report_name is not None:
      mod = importlib.import_module('%s.__init__' % report_name)
      self.local_path, _ = os.path.split(os.path.abspath(mod.__file__))
    else:
      self.local_path = os.getcwd()
    self.title = self.script_name if title is None else title
    self.is_local = True

  def to_dict(self, inputs_scope=True):
    """

    :param inputs_scope: Boolean
    :return:
    """
    if inputs_scope:
      return dict([(s, getattr(self, s)) for s in self.__slots__ if s not in self.__internals_attrs])

    return dict([(s, getattr(self, s)) for s in self.__slots__])

  def __str__(self):
    return str(self.to_dict())


class Report(object):
  showNavMenu, withContainer = False, False

  def __init__(self, run_options=None, appCache=None, sideBar=True, urlsApp=None, theme=None, context=None):
    #
    self._css, self._ui, self._js, self._py, self._theme, self.__style = {}, None, None, None, None, None
    self._props, self._tags, self._header_obj, self.__import_manage = {}, None, None, None
    self.run = self.run_context(run_options if run_options is not None else {})
    self.useSideBar, self.preferredTheme = sideBar, None
    self.cache, self._urlsApp = appCache, {'incidents': '/incidents', 'index': '/', 'questions': '/questions',
                                           'admin': '/admin', 'report': '/reports', 'transfer': '/transfer', 'search': '/search'} if urlsApp is None else dict(urlsApp)
    self._system = dict(context) if context is not None else {}
    if urlsApp is not None:
      self._urlsApp.update(urlsApp)
    self.timestamp, self.runTime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), time.time() * 100
    self.countItems, self.countNotif, self.userGroups = 0, 0, {}
    self.content, self.shortcuts, self.exportCsv, self.jsSources = [], {}, {}, {}
    self._dbBindings, self._dbErrors = {}, collections.defaultdict(int)
    self.currentTitleObj, self.navBarContent, self.sideBarActions = {}, {'content': []}, []
    self.htmlItems, self.jsOnLoad, self.http, self.htmlCodes, self.htmlRefs = {}, [], {}, {}, {}
    self.notifications = collections.defaultdict(list)
    self.interruptReport, self._propagate = (False, None), []
    self.dataSourceMonitor = {}
    self.sourceDef, self.localFiles, self.libDef, self._run, self._scroll, self._contextMenu = {}, {}, {}, {}, set(), {}
    self.logo, self._dbSettings, self._cssText, self.dbsDef = None, None, "", {}

    #
    self.jsOnLoadFnc, self.jsWindowLoadFnc = OrderedSet(), OrderedSet()
    self.jsOnLoadEvtsFnc = OrderedSet()
    self.jsFnc = OrderedSet()

    self.jsImports, self.cssImport = set(['jquery', 'font-awesome']), set(['font-awesome'])
    self.jsLocalImports, self.cssLocalImports = set(), set()
    self.workers, self.fileMap, self.files = {}, {}, {}

    # Add Style default and Standard values in a given report
    self.ageReference, self.colorBase = 'red', 'green'
    if theme is not None:
      self.style.colors.setTheme(theme)

  def run_context(self, run_options):
    """

    :return:
    """
    return ContextRun(**run_options)

  @property
  def style(self):
    """
    Interface to the CSS framework.

    This module will allow you to change the different style of the components by creating bespoke one.
    It will be also possible to override colors of the themes in order to quickly get framework changes.

    Documentation
    https://www.w3schools.com/css/default.asp

    :rtype: GrpCls.ClassPage
    :return: A Python CSS Object
    """
    if self.__style is None:
      self.__style = GrpCls.ClassPage(self)
    return self.__style

  @property
  def theme(self):
    """ """
    if self._theme is None:
      self._theme = Theme.ThemeDefault()
    return self._theme

  @theme.setter
  def theme(self, theme):
    """

    :param theme:
    :return:
    """
    if isinstance(theme, dict):
      self._theme = Theme.ThemeCustome()
      self._theme = theme
    else:
      self._theme = theme

  def imports(self, online=False):
    """

    :param online:
    """
    if self.__import_manage is None:
      self.__import_manage = Imports.ImportManager(online, report=self)
    return self.__import_manage

  @property
  def symbols(self):
    """
    Shortcut to the HTML symbols

    Documentation
    https://www.w3schools.com/html/html_symbols.asp
    https://www.w3schools.com/charsets/ref_utf_math.asp

    Those can be added in string in order to improve the render of a text.
    """
    return symboles.Symboles()

  @property
  def entities(self):
    """
    Shortcut to the HTML Entities

    Documentation
    https://www.w3schools.com/html/html_entities.asp

    Those can be added in string in order to improve the render of a text.
    """
    return entities.Entities()

  @property
  def ui(self):
    """
    Description:
    ------------
    User Interface section.

    All the components which can be used in the dashboard to display the data.
    Within this object different categories of items can be used like (list, simple text, charts...)

    Related Pages:
    --------------
    https://www.w3schools.com/html/default.asp

    :rtype: Components.Components

    :return: Python HTML object
    """
    if self._ui is None:
      self._ui = Components.Components(self)
    return self._ui

  @property
  def js(self):
    """
    Description:
    ------------
    Go to the Javascript section. Property to get all the JavaScript features.
    Most of the standard modules will be available in order to add event and interaction to the Js transpiled

    Usage:
    ------
    js.console.log("test")

    Related Pages:
    --------------
    https://www.w3schools.com/js/default.asp

    :return: Python HTML object
    """
    if self._js is None:
      self._js = js.Js.JsBase(self)
    return self._js

  @property
  def py(self):
    """
    Python external module section.


    Documentation:
    https://www.w3schools.com/js/default.asp

    :return: Python HTML object
    """
    if self._py is None:
      self._py = py.PyExt.PyExt(self)
    return self._py

  @property
  def data(self):
    """
    Python internal data source management

    This can be extended by inheriting from this epyk.core.data.DataSrc.DataSrc
    and adding extra entry points

    :return: The framework available data source
    """
    return data.Data.DataSrc(self)

  def itemFromCode(self, htmlCode):
    """

    :param htmlCode:

    :rtype: html.Html.Html
    :return:
    """
    return self.htmlCodes[htmlCode]

  def item(self, itemId):
    """

    :param itemId:
    :return:
    """
    return self.htmlItems[itemId]

  def socketSend(self, htmlCode, data, report_name=None, script_name=None):
    try:
      from urllib.parse import urlparse, urlencode
      from urllib.request import urlopen, Request
      from urllib.error import HTTPError
    except ImportError:
      from urlparse import urlparse
      from urllib import urlencode
      from urllib2 import urlopen, Request, HTTPError

    urls = [htmlCode]
    if report_name or report_name is None:
      urls.append(self.run.report_name if report_name is None else report_name)
      if script_name or script_name is None:
        urls.append(self.run.script_name if script_name is None else script_name)
    response = urlopen(Request("%s%smessage/%s" % (self.run.url_root, self._urlsApp["index"].replace("/index", "/"), "/".join(urls)),
                    data=urlencode({'data': json.dumps(data)}).encode('utf-8')))
    response.read()

  # def getCss(self, clsName, ovrData=None):
  #   """
  #   Retrieve the CSS Class definition from the Python framework.
  #   This will also allow the definition update by defining some overrides.
  #   Overrides might be temporary changes in the class but the right practice will be to get them push to the core style framework
  #   """
  #   return self.style.cssCls(clsName, ovrData)

  # #
  # def addCss(self, filename):
  #   """
  #   This will load your local CSS file when the report will be built. Then you will be able to use the new Styles in the different HTML Components
  #   """
  #   self.cssLocalImports.add("%s/css/%s" % (self.run.report_name, filename))
  #   return self

  def addCssText(self, cssText):
    self._cssText = cssText
    return self

  def addJs(self, filename):
    """
    This will load your local javascript file when the report will be built. Then you will be able to use the new features in the different Javascript wrappers
    """
    self.jsLocalImports.add("%s/js/%s" % (self.run.report_name, filename))
    return self


  # -----------------------------------------------------------------------------------------
  #                                    LOGGING AND DEBUGGING FUNCTIONS
  # -----------------------------------------------------------------------------------------
  def log(self, text, type='DEBUG'):
    """
    This will write some logs to your local user.log file in \system\logs.
    """
    log = logging.getLogger('user')
    if type.upper() == 'INFO':
      log.info("| %s [ %s ] >> %s" % (self.run.report_name, self.run.script_name, text))
    elif type.upper() == 'WARNING':
      log.warning("| %s [ %s ] >> %s" % (self.run.report_name, self.run.script_name, text))
    else:
      log.debug("| %s [ %s ] >> %s" % (self.run.report_name, self.run.script_name, text))

  @property
  def outs(self):
    """

    :return:
    """
    return py.PyOuts.PyOuts(self)

  @property
  def headers(self):
    """ Property to the HTML page header """
    if self._header_obj is None:
      self._header_obj = html.Header.Header(self)
    return self._header_obj

  def to_html(self, online=False, mode=None, html_template=None, fnc=None):
    """

    :param online:
    :param mode:
    :param html_template:
    :param fnc:

    :return:
    """
    if html_template is None:
      html_template = html.templates.HtmlTmplBase.DATA

    if fnc is not None:
      return fnc(html_template, **self.html(online, mode))

    return html_template % self.html(online, mode)

  def to_html_error(self, tracebackStr, server_owner, title="Script Error Details", icon="fas fa-exclamation-triangle",
                    pyModule=None, online=False, mode=None, html_template=None, fnc=None):
    """

    :param tracebackStr:
    :param server_owner:
    :param title:
    :param icon:
    :param pyModule:

    :return:
    """
    report_error = Report(self.run.to_dict())
    report_error._urlsApp.update(self._urlsApp)
    report_error.nav(selected='Reports', breadcrum=True)
    for notification in self._propagate:
      report_error.add(notification)
    report_error.ui.text("<i class='fas fa-cog'></i>&nbsp;To open the report again click [here](/reports/run/%s/%s)" % (
      report_error.run.report_name, report_error.run.script_name)).css('margin', '5px')
    owners = ";".join(pyModule.OWNERS) if pyModule is not None and hasattr(pyModule, 'OWNERS') else server_owner
    report_error.ui.text("<i class='fas fa-envelope'></i>&nbsp;To raise this issue to the report owner <a onclick='window.NO_UNLOAD = true;' href='mailto:%(owners)s?subject=Report error&body=%(error)s'>contact us</a>" % {
      'owners': owners, 'error': tracebackStr.replace("'", "").replace('"', "")}).css('margin', '5px')
    report_error.ui.rich.textborder({'title': title, 'icon': icon, 'value': "<pre style='padding:5px;white-space:pre-wrap; '>%s</pre>" % '<br>'.join([re.sub(r'^ +', lambda m: ' ' * len(m.group()), i) for i in tracebackStr.split('\n')]),
                                     'color': self.getColor('danger', 1), 'colorTitle': self.getColor('danger', 1)})
    return report_error.to_html(online, mode, html_template, fnc)

  def dumps(self, data):
    """
    Function used to dump the data before being sent to the Javascript layer
    This function relies on json.dumps with a special encoder in order to work with Numpy array and Pandas data structures.

    As NaN is not valid on the Json side those object are not allowed during the dump.
    It is advised to use fillna() in your script before returning the data to the framework to avoid this issue.

    Example
    report.dumps(result)

    Documentation
    https://docs.python.org/2/library/json.html

    :param data: The python dictionary or data structure
    :return: The serialised data
    """
    return json.dumps(data, cls=js.JsEncoder.Encoder, allow_nan=False)

  def html(self, online=False, mode=None):
    """
    Special output function used by the framework to export the report to a isoldated HTML document
    This function cannot be used directly as it will write the report on the server but some buttons are available on the top to trigger it
    """
    if mode is None:
      self.style.add('CssBody', cssRef='body')
      self.style.add('CssBodyContent', htmlId='page_content')
    self.style.add('CssBodyLoadingBack', htmlId='popup_loading_back')
    self.style.add('CssBodyLoading', htmlId='popup_loading')
    self.style.add('CssStandardLinks')
    self.style.add('CssTextSelection', cssRef='::selection')
    self.style.add('CssTextSelection', cssRef='::-moz-selection')

    if getattr(self, 'DEBUG', False):
      print("Debug mode activated, please press F12 in your browser to get Javascript details")

    # Add directly to the main page only components that are attached to the report
    # All the components added to a container are not considered here.
    # The framework assume that the containers should take care of them
    if len(self.localFiles) > 0:
      self.jsGlobal.fnc('RemoveFile(src, fileName)', '$(src).parent().empty();%s' % self.jsPost("%s/remove/file/OUTPUTS/%s" % (self._urlsApp['transfer'], self.run.report_name), "filename: fileName", isPyData=False))
      self.jsGlobal.fnc("RemoveLocalFiles(src, fileNames)", '$(src).parent().remove();%s' % self.jsPost('%s/locals/clean/%s' % (self._urlsApp['transfer'], self.run.report_name), "filenames: fileNames", isPyData=False))
      self.jsGlobal.fnc("DownloadCachedFiles(filePath)", "NO_UNLOAD = true; %s " % self.jsSubmitForm('"%s/download/OUTPUTS/%s"' % (self._urlsApp['transfer'], self.run.report_name), isPyData=False, method='POST'))
      filesUsed, maxLenght, usedFileNames = [], 18, []
      for fileInfo in self.localFiles.values():
        fileInfo['full_path'] = "%(subFolder)s/%(filename)s" % fileInfo
        fileInfo['full_path_red'] = "%(subFolder)s/%(filename)s" % fileInfo
        usedFileNames.append(fileInfo['full_path'])
        if len(fileInfo['full_path']) > maxLenght:
          fileInfo['full_path_short'] = fileInfo['full_path'][-maxLenght:]
          fileInfo['full_path_red'] = "<div style='cursor:pointer;display:inline-block' title='%(full_path)s'>...%(full_path_short)s</div>" % fileInfo
        if self.user == 'anonymous':
          filesUsed.append(
            "<div>&nbsp;&nbsp;&bull; %(full_path_red)s - <b>%(timestamp)s</b> </div>" % fileInfo)
        else:
          filesUsed.append( "<div>&nbsp;&nbsp;&bull; %(full_path_red)s - <b>%(timestamp)s</b>&nbsp;&nbsp;<i style='color:#C00000;cursor:pointer;margin-right:5px' class='fas fa-times' onclick='RemoveFile(this, \"%(full_path)s\")'></i> <i onclick='DownloadCachedFiles(\"%(full_path)s\")' style='cursor:pointer;' class='fas fa-file-download'></i> </div>" % fileInfo)
      self.notification('WARNING', "<b>%s</b> Cached Data Source Used" % len(self.localFiles),
                        '''
                        <br>Remove folder outputs/ to update your data <a href="%(urlTransfer)s/viewer/files/%(reportName)s" class="far fa-copy" style="color:#293846;margin-left:5px" target="_blank" title="Files management"></a>
                        <br>%(filesUsed)s<br>
                        <div style='color:#C00000;cursor:pointer' onclick='RemoveLocalFiles(this, %(usedFileNames)s)' ><b>&times;</b> Remove all temporary local files</div>''' % {"urlTransfer": self._urlsApp['transfer'], "reportName": self.run.report_name, "filesUsed": "".join(filesUsed), "usedFileNames": json.dumps(usedFileNames) } )

    if len(self._dbErrors) > 0:
      errors = []
      for dbType, dbVals in self._dbErrors.items():
        errors.append("<div><strong>%s</strong>&nbsp;&nbsp;%s</div>" % (dbVals, dbType))
      self.notification('DANGER', 'Database errors', "".join(errors))

    onloadParts, windowLoadParts, htmlParts, result = [], [], [], {}
    for htmlCode, src in self.jsSources.items():
      # TODO add a check regarding the volume of data
      if len(src['containers']) > 0:
        self.jsGlobal.add(htmlCode, json.dumps(src['data'], cls=js.JsEncoder.Encoder))
        #htmlParts.append(src['data'].html())

    # Add the extra function defined in the Javascript framework
    for fnc, details in self._props.get('js', {}).get('functions', {}).items():
      self.jsGlobal.fnc("%s(%s)" % (fnc, ",".join(details.get('pmt', []))), details["content"])

    for fnc, details in self._props.get('js', {}).get('prototypes', {}).items():
      self.jsGlobal.addJs("%s = function(%s){%s};" % (fnc, ",".join(details.get('pmts', [])), details["content"]))

    # 'functions'
    for objId in self.content:
      if self.htmlItems[objId].inReport:
        htmlParts.append(self.htmlItems[objId].html())

    for jsFnc in self.jsOnLoadFnc:
      onloadParts.append(str(jsFnc))

    for jsFnc in self.jsFnc:
      onloadParts.append(str(jsFnc))

    for jsFnc in self.jsOnLoadEvtsFnc:
      onloadParts.append(str(jsFnc))

    if len(self._scroll) > 0:
      onloadParts.append('''
        $(window).scroll(function(event) {var screenPos = $(window).scrollTop() + $(window).height();%s})''' % ";".join(self._scroll))

    for jsFnc in self.jsWindowLoadFnc:
      windowLoadParts.append(str(jsFnc))

    #
    if self.shortcuts:
      onloadParts.append("$(document).on('keydown', 'body', function(e){var code = e.keyCode || e.which")
      for key, action in self.shortcuts.items():
        onloadParts.append("if(%s) {%s}" % (key, action))
      onloadParts.append("});")

    # Add imports
    self.jsImports |= self._props.get("js", {}).get('imports', set([]))
    self.cssImport |= self._props.get("css", {}).get('imports', set([]))

    # Section dedicated to the javascript for all the charts
    importMng = self.imports(online=online)
    result['cssImports'] = importMng.cssResolve(self.cssImport, self.cssLocalImports)
    result['jsImports'] = importMng.jsResolve(self.jsImports, self.jsLocalImports)
    result['jsDocumentReady'] = ";".join(onloadParts)
    result['jsWindowLoad'] = "\n".join(windowLoadParts)
    result['content'] = "\n".join(htmlParts)
    result['title'] = self.run.title
    result['mailTo'] = ""
    result['exportData'] = self.exportCsv
    result['cssStyle'] = "%s%s" % (self._css.toCss(), self._cssText)
    result['favicon'] = "" if self.logo is None else '<link rel="shortcut icon" type="image/vnd.microsoft.icon" href="../../../img/%s/%s" />' % (self.run.report_name, self.logo)
    return result
