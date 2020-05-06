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
from epyk.core.css.themes import Theme
from epyk.core.css import Classes

from epyk.core import html
from epyk.core import js
from epyk.core import py
from epyk.core import data

from epyk.core.html import symboles
from epyk.core.html import entities
from epyk.core.py import OrderedSet


class ContextRun(object):
  __slots__ = ['mac_address', 'host_name', 'current_user', 'report_name', 'script_name', 'local_path', 'url_root', 'title', 'is_local', 'url', 'username']
  __internals_attrs = ['mac_address', 'local_path', 'is_local', 'url', 'username']

  def __init__(self, report_name=None, script_name=None, current_user="local", host_name="script",
               url_root='http://127.0.0.1', title=None, urlMaps=None):
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
  ext_packages = None # For extension modules

  def __init__(self, run_options=None):
    #
    self._css, self._ui, self._js, self._py, self._theme, self.__body = {}, None, None, None, None, None
    self._props, self._tags, self._header_obj, self.__import_manage = {'js': {'onReady': OrderedSet()}}, None, None, None
    self.run = self.run_context(run_options if run_options is not None else {})

    self.timestamp, self.runTime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), time.time() * 100
    self.content, self.shortcuts, self.exportCsv, self.jsSources = [], {}, {}, {}
    self._dbBindings, self._dbErrors = {}, collections.defaultdict(int)
    self.currentTitleObj, self.navBarContent, self.sideBarActions = {}, {'content': []}, []
    self.htmlItems, self.jsOnLoad, self.http, self.htmlCodes, self.htmlRefs = {}, [], {}, {}, {}
    self.notifications = collections.defaultdict(list)
    self.interruptReport, self._propagate = (False, None), []

    self.sourceDef, self.localFiles, self.libDef, self._run, self._scroll, self._contextMenu = {}, {}, {}, {}, set(), {}
    self.logo, self._dbSettings, self.dbsDef, self._cssText, self._jsText = None, None, {}, [], []

    #
    self.jsOnLoadFnc, self.jsWindowLoadFnc = OrderedSet(), OrderedSet()
    self.jsOnLoadEvtsFnc = OrderedSet()

    self.jsImports, self.cssImport = set(), set()
    self.jsLocalImports, self.cssLocalImports = set(), set()

  def run_context(self, run_options):
    """

    :return:
    """
    return ContextRun(**run_options)

  @property
  def body(self):
    """
    Property that returns the Body element of the HTML page
    """
    if self.__body is None:
      self.__body = html.Html.Body(self, None)
    return self.__body

  @body.setter
  def body(self, calc):
    self.__body = calc(self, None)

  @property
  def theme(self):
    """
    Return the currently used :doc:`report/theme` for the report
    """
    if self._theme is None:
      self._theme = Theme.ThemeDefault()
    return self._theme

  @theme.setter
  def theme(self, theme):
    if isinstance(theme, dict):
      self._theme = Theme.ThemeCustome()
      self._theme = theme
    else:
      self._theme = theme

  def imports(self, online=False):
    """
    Return the :doc:`report/import_manager`, which allows to import automatically packages for certain components to run.
    """
    if self.__import_manage is None:
      self.__import_manage = Imports.ImportManager(online, report=self)
    return self.__import_manage

  @property
  def symbols(self):
    """
    Description:
    ------------
    Shortcut to the HTML symbols

    Related Pages:

      https://www.w3schools.com/html/html_symbols.asp
      https://www.w3schools.com/charsets/ref_utf_math.asp

    Those can be added in string in order to improve the render of a text.
    """
    return symboles.Symboles()

  @property
  def entities(self):
    """
    Description:
    ------------
    Shortcut to the HTML Entities

    Related Pages:

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

    All the :doc:`components <report/ui>` which can be used in the dashboard to display the data.
    Within this object different categories of items can be used like (list, simple text, charts...)

    Related Pages:

	    https://www.w3schools.com/html/default.asp

    :rtype: :doc:`Components.Components <report/ui>`

    :return: Python HTML object
    """
    if self._ui is None:
      self._ui = Components.Components(self)
    return self._ui

  @property
  def css(self):
    """
    Returns the set of :doc:`CSS Classes <css>` for the HTML report
    """
    return Classes.Catalog(self, {'other': set()})._class_type('other')

  @property
  def js(self):
    """
    Description:
    ------------
    Go to the Javascript section. Property to get all the JavaScript features.
    Most of the standard modules will be available in order to add event and interaction to the Js transpiled

    Usage::

      js.console.log("test")

    Related Pages:

      https://www.w3schools.com/js/default.asp

    :return: Python HTML object
    """
    if self._js is None:
      self._js = js.Js.JsBase(self)
    return self._js

  @property
  def py(self):
    """
    Description:
    ------------
    Python external module section.

    Related Pages:

      https://www.w3schools.com/js/default.asp

    :return: Python HTML object
    """
    if self._py is None:
      self._py = py.PyExt.PyExt(self)
    return self._py

  @property
  def data(self):
    """
    Description:
    ------------
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
    """
    Property to the HTML page header
    """
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

    Example::

      report.dumps(result)

    Related Pages:

			https://docs.python.org/2/library/json.html

    :param data: The python dictionary or data structure
    :return: The serialised data
    """
    return json.dumps(data, cls=js.JsEncoder.Encoder, allow_nan=False)
