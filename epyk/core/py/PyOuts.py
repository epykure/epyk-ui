import os
import time
import json

from epyk.core.js import Imports
from epyk.core.js import Js
from epyk.core.js import JsUtils

from epyk.core.html.templates import HtmlTmplBase


class OutBrowsers(object):
  def __init__(self, context):
    self._context = context

  def codepen(self, path=None, target="_blank", open_browser=True):
    """
    Description:
    ------------
    Update the Html launcher and send the data to codepen
    URL used: https://codepen.io/pen/define/

    Related Pages:

      https://www.debuggex.com/cheatsheet/regex/python

    Attributes:
    ----------
    :param path: String. Output path in which the static files will be generated
    :param target: String. Load the data in a new tab in the browser
    :param open_browser: Boolean. Flag to open the browser automatically

    :return: The output launcher full file name
    """
    import re
    import webbrowser

    results = self._context._to_html_obj()
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
    launcher_file = os.path.join(path, "RunnerCodepen.html")
    if open_browser:
      webbrowser.open(launcher_file)
    return launcher_file

  def stackblitz(self, path=None, target="_blank", open_browser=True):
    """
    Description:
    ------------

    Related Pages:

      https://stackblitz.com/docs

    Attributes:
    ----------
    :param path: String. Output path in which the static files will be generated
    :param target: String. Load the data in a new tab in the browser
    :param open_browser: Boolean. Flag to open the browser automatically
    """
    import webbrowser

    results = self._context._to_html_obj()
    results['jsFrgs'] = results['jsFrgs'].replace('"', "'")
    results['cssImports'] = results['cssImports'].replace('"', "'")
    results['content'] = results['content'].replace('"', "'")
    with open(os.path.join(path, "RunnerStackblitz.html"), "w") as f:
      f.write('''
<html lang="en">
<head></head>
<body>
<form id="mainForm" method="post" action="https://stackblitz.com/run" target="_self">
<input type="hidden" name="project[files][index.js]" value="
%(jsFrgs)s
">
<input type="hidden" name="project[files][index.html]" value="
%(cssImports)s
<style>
%(cssStyle)s
</style>
%(content)s
">
<input type="hidden" name="project[description]" value="Epyk Example">
<input type="hidden" name="project[dependencies]" value="{&quot;rxjs&quot;:&quot;5.5.6&quot;}">
<input type="hidden" name="project[template]" value="javascript">
<input type="hidden" name="project[settings]" value="{&quot;compile&quot;:{&quot;clearConsole&quot;:false}}">
</form>
<script>document.getElementById("mainForm").submit();</script>

</body></html>
''' % results)
    launcher_file = os.path.join(path, "RunnerStackblitz.html")
    if open_browser:
      webbrowser.open(launcher_file)
    return launcher_file


class PyOuts(object):
  def __init__(self, report=None, options=None):
    self._report, self._options = report, options
    self.excluded_packages, html_tmpl = None, HtmlTmplBase.JUPYTERLAB

  def _to_html_obj(self, htmlParts=None, cssParts=None, split_js=False):
    """
    Description:
    ------------
    Create the HTML result object from the report definition

    Attributes:
    ----------
    :param htmlParts: Optional. HTML Content of the page
    :param cssParts: Optional. CSS classes content of the page

    :return: A python dictionary with the HTML results
    """
    order_components = list(self._report.components.keys())
    if htmlParts is None:
      htmlParts, cssParts = [], {}
      for component_id in order_components:
        component = self._report.components[component_id]
        if component.name == 'Body':
          continue

        if component.options.managed:
          htmlParts.append(component.html())
        #
        cssParts.update(component.style.get_classes_css())
    onloadParts, onloadPartsCommon = list(self._report._jsText), {}
    for data_id, data in self._report._props.get("data", {}).get('sources', {}).items():
      onloadParts.append("var data_%s = %s" % (data_id, json.dumps(data)))

    for k, v in self._report._props.get('js', {}).get('functions', {}).items():
      sPmt = "(%s)" % ", ".join(list(v["pmt"])) if "pmt" in v else "{}"
      onloadParts.append("function %s%s{%s}" % (k, sPmt, v["content"].strip()))

    if split_js:
      onloadPartsCommon = self._report._props.get('js', {}).get("constructors", {})
    else:
      for c, d in self._report._props.get('js', {}).get("constructors", {}).items():
        onloadParts.append(d)
    for c, d in self._report._props.get('js', {}).get("configs", {}).items():
      onloadParts.append(str(d))

    for c, d in self._report._props.get('js', {}).get("datasets", {}).items():
      onloadParts.append(d)

    for b in self._report._props.get('js', {}).get("builders", []):
      onloadParts.append(b)

    for b in self._report._props.get('js', {}).get("builders_css", []):
      onloadParts.append(b)

    # Add the component on ready functions
    for component_id in order_components:
      component = self._report.components[component_id]
      if component.name == 'Body':
        continue

      onloadParts.extend(component._browser_data['component_ready'])

      for event, source_fncs in component._browser_data['mouse'].items():
        for source, event_fncs in source_fncs.items():
          str_fncs = JsUtils.jsConvertFncs(event_fncs['content'], toStr=True)
          onloadParts.append("%s.addEventListener('%s', function(event){%s})" % (source, event, str_fncs))

      for event, source_fncs in component._browser_data['keys'].items():
        for source, event_fncs in source_fncs.get_event().items():
          str_fncs = JsUtils.jsConvertFncs(event_fncs['content'], toStr=True)
          onloadParts.append("%s.addEventListener('%s', function(event){%s})" % (source, event, str_fncs))

    # Add the page on document ready functions
    for on_ready_frg in self._report._props.get('js', {}).get('onReady', []):
      onloadParts.append(on_ready_frg)
    # Add the document events functions
    for event, source_fncs in self._report._props.get('js', {}).get('events', []).items():
      for source, event_fncs in source_fncs.get_event().items():
        str_fncs = JsUtils.jsConvertFncs(event_fncs['content'], toStr=True)
        onloadParts.append("%s.addEventListener('%s', function(event){%s})" % (source, event, str_fncs))

    importMng = Imports.ImportManager(online=True, report=self._report)
    results = {
      'cssStyle': "%s\n%s" % ("\n".join([v for v in cssParts.values()]), "\n".join(self._report._cssText)),
      'cssContainer': ";".join(["%s:%s" % (k, v) for k, v in self._report._props.get('css', {}).get('container', {}).items()]),
      'content': "\n".join(htmlParts),
      'jsFrgsCommon': onloadPartsCommon, # This is only used in some specific web frameworks and it is better to keep the data as list
      'jsFrgs': ";".join(onloadParts),
      'cssImports': importMng.cssResolve(self._report.cssImport, self._report.cssLocalImports, excluded=self.excluded_packages),
      'jsImports': importMng.jsResolve(self._report.jsImports, self._report.jsLocalImports, excluded=self.excluded_packages)
    }
    return results

  def _repr_html_(self):
    """
    Description:
    ------------
    Standard output for Jupyter Notebooks.

    This is what will use IPython in order to display the results in cells.
    """
    results = self._to_html_obj()
    importMng = Imports.ImportManager(online=True, report=self._report)
    require_js = importMng.to_requireJs(results, self.excluded_packages)
    results['paths'] = "{%s}" % ", ".join(["%s: '%s'" % (k, p) for k, p in require_js['paths'].items()])
    results['jsFrgs_in_req'] = require_js['jsFrgs']
    return self.html_tmpl.strip() % results

  def jupyterlab(self):
    """
    Description:
    ------------
    For a display of the report in JupyterLab.
    Thanks to this function some packages will not be imported to not conflict with the existing ones

    Related Pages:

      https://jupyter.org/
    """
    self.html_tmpl = HtmlTmplBase.JUPYTERLAB
    self.excluded_packages = ['bootstrap']
    return self

  def jupyter(self):
    """
    Description:
    ------------
    For a display of the report in Jupyter.
    Thanks to this function some packages will not be imported to not conflict with the existing ones

    Related Pages:

      https://jupyter.org/

    :return: The ouput object with the function _repr_html_
    """
    self.html_tmpl = HtmlTmplBase.JUPYTER
    try:
      import notebook

      self.excluded_packages = []
      nb_path = os.path.split(notebook.__file__)[0]
      for f in os.listdir(os.path.join(nb_path, 'static', 'components')):
        self.excluded_packages.append(Imports.NOTEBOOK_MAPPING.get(f, f))
    except:
      self.excluded_packages = ['bootstrap', 'jquery', 'moment', 'jqueryui', 'mathjs']
    return self

  def w3cTryIt(self, path=None, name=None):
    """
    Description:
    ------------
    This will produce everything in a single page which can be directly copied to the try editor in w3C website

    Related Pages:

      https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic

    Attributes:
    ----------
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
    Description:
    ------------

    Usage::

      Related Pages:

      https://codepen.io/

    Attributes:
    ----------
    :param path: The path in which the output files will be created
    :param name: The filename without the extension

    TODO Try to add the prefill
    https://blog.codepen.io/documentation/api/prefill/

    :return: The file path
    """
    self.jsfiddle(path, name, framework="codepen")

  def jsfiddle(self, path=None, name=None, framework="jsfiddle"):
    """
    Description:
    ------------
    Produce files which can be copied directly to https://jsfiddle.net in order to test the results and perform changes.

    The output is always in a sub directory jsfiddle

    Usage::

      Related Pages:

      https://jsfiddle.net/

    Attributes:
    ----------
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
      results = self._to_html_obj()
      # For the JavaScript builders
      with open(os.path.join(path, "%s.js" % name), "w") as f:
        f.write(results["jsFrgs"])

      # For all the doms and imports
      with open(os.path.join(path, "%s.html" % name), "w") as f:
        f.write("%s\n" % results["cssImports"])
        f.write("%s\n" % results["jsImports"])
        f.write(results["content"])

      # For the CSS styles
      with open(os.path.join(path, "%s.css" % name), "w") as f:
        f.write(results["cssStyle"])
    return path

  def html_file(self, path=None, name=None, split_files=False):
    """
    Description:
    ------------
    Function used to generate a static HTML page for the report

    Usage::

      Attributes:
    ----------
    :param path: The path in which the output files will be created
    :param name: The filename without the extension

    :return: The file full path
    """
    if path is None:
      path = os.path.join(os.getcwd(), "outs")
    if not os.path.exists(path):
      os.makedirs(path, exist_ok=True)
    if name is None:
      name = int(time.time())
    html_file_path = os.path.join(path, "%s.html" % name)
    htmlParts = []
    cssParts = dict(self._report.body.style.get_classes_css())
    order_components = list(self._report.components.keys())
    for component_id in order_components:
      component = self._report.components[component_id]
      if component.name == 'Body':
        continue

      if component.options.managed:
        htmlParts.append(component.html())
      cssParts.update(component.style.get_classes_css())
    body = str(self._report.body.set_content(self._report, "\n".join(htmlParts)))
    results = self._to_html_obj(htmlParts, cssParts, split_js=split_files)
    if split_files:
      results['cssImports'] = '%s\n<link rel="stylesheet" href="./css/%s.css" type="text/css">\n\n' % (results['cssImports'], name)
      body = '%s\n\n<script language="javascript" type="text/javascript" src="./js/%s.js"></script>' % (body, name)
      if not os.path.exists(os.path.join(path, 'css')):
        os.makedirs(os.path.join(path, 'css'), exist_ok=True)
      with open(os.path.join(path, 'css', "%s.css" % name), "w") as f:
        f.write(results['cssStyle'])

      if not os.path.exists(os.path.join(path, 'js')):
        os.makedirs(os.path.join(path, 'js'), exist_ok=True)
      with open(os.path.join(path, 'js', "%s.js" % name), "w") as f:
        f.write(";".join(results['jsFrgsCommon'].values()))

    # Add the worker sections when no server available
    for js_id, wk_content in self._report._props.get('js', {}).get("workers", {}).items():
      body += '\n<script id="%s" type="javascript/worker">\n%s\n</script>' % (js_id, wk_content)
    with open(html_file_path, "w") as f:
      results['body'] = body
      results['header'] = self._report.headers
      f.write(HtmlTmplBase.STATIC_PAGE % results)
    return html_file_path

  def web(self):
    """
    Description:
    ------------
    Return the complete page structure to allow the various web framework to split the code accordingly.
    Fragments will then be used by the various framework to create the corresponding pages
    """
    htmlParts = []
    cssParts = dict(self._report.body.style.get_classes_css())
    order_components = list(self._report.components.keys())
    for component_id in order_components:
      component = self._report.components[component_id]
      if component.name == 'Body':
        continue

      if component.options.managed:
        htmlParts.append(component.html())
      cssParts.update(component.style.get_classes_css())
    body = str(self._report.body.set_content(self._report, "\n".join(htmlParts)))
    results = self._to_html_obj(htmlParts, cssParts, split_js=True)
    results['body'] = body.replace("<body", "<div").replace("</body>", "</div>")
    return results

  def publish(self, server, app_path, selector=None, name=None, module=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param server:
    :param app_path:
    :param name:
    """
    from epyk.web import angular, node, vue, react, deno

    app = None
    if server.upper() == 'NODE':
      app = node.Node(app_path=app_path, name=name or 'node')
      app.page(report=self._report, selector=selector or 'app-root', name=module)
    elif server.upper() == 'DENO':
      app = deno.Deno(app_path=app_path, name=name or 'deno')
      app.page(report=self._report, selector=selector or 'app-root', name=module)
    elif server.upper() == 'ANGULAR':
      app = angular.Angular(app_path=app_path, name=name or 'angular')
      app.page(report=self._report, selector=selector or 'app-root', name=module)
    elif server.upper() == 'VUE':
      app = vue.VueJs(app_path=app_path, name=name or 'vue')
      app.page(report=self._report, selector=selector or 'app-root', name=module)
    elif server.upper() == 'REACT':
      app = react.React(app_path=app_path, name=name or 'react')
      app.page(report=self._report, selector=selector or 'app-root', name=module)
    app.publish()

  def markdown_file(self, path=None, name=None):
    """
    Description:
    ------------
    Writes a Markdown file from the report object

    Attributes:
    ----------
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
        order_components = list(self._report.components.keys())
        for component_id in order_components:
          component = self._report.components[component_id]
          if component.name == 'Body':
            continue

          if hasattr(component, "to_markdown"):
            f.write("%s\n" % component.to_markdown(component.vals))
      return file_Path

  def html(self):
    """

    :return:
    """
    self.html_tmpl = HtmlTmplBase.STATIC_PAGE
    results = self._to_html_obj()
    importMng = Imports.ImportManager(online=True, report=self._report)
    require_js = importMng.to_requireJs(results, self.excluded_packages)
    results['paths'] = "{%s}" % ", ".join(["%s: '%s'" % (k, p) for k, p in require_js['paths'].items()])
    results['jsFrgs_in_req'] = require_js['jsFrgs']
    htmlParts = []
    cssParts = dict(self._report.body.style.get_classes_css())
    order_components = list(self._report.components.keys())
    for component_id in order_components:
      component = self._report.components[component_id]
      if component.name == 'Body':
        continue

      if component.options.managed:
        htmlParts.append(component.html())
      cssParts.update(component.style.get_classes_css())
    body = str(self._report.body.set_content(self._report, "\n".join(htmlParts)))
    results['body'] = body
    results['header'] = self._report.headers
    return self.html_tmpl.strip() % results

  @property
  def browser(self):
    """
    Description:
    ------------
    This module will require the package webbrowser.
    It will allow outputs to be created directly in the webpages (without using intermediary text files
    """
    return OutBrowsers(self)
