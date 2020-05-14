
import os

from epyk.core.html.graph import GraphD3


class D3(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "D3"

  def script(self, name, scripts, data=None, d3_version=None, dependencies=None, profile=None, options=None, width=(300, "px"),
             height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param name:
    :param scripts:
    :param d3_version:
    :param dependencies:
    """
    scripts = [os.path.split(script) for script in scripts]

    dependencies = dependencies or []
    self.parent.context.rptObj.ext_packages = self.parent.context.rptObj.ext_packages or {}
    dependencies.append({'alias': 'd3', 'version': d3_version} if d3_version is not None else "d3")

    self.parent.context.rptObj.ext_packages[name] = {
        'version': '', 'req': [{'alias': d} if not isinstance(d, dict) else d for d in dependencies],
        'register': {'alias': name, 'module': scripts[0][1][:-3]},
        'modules': [{'script': split_url[1], 'path': '', 'cdnjs': split_url[0]} for split_url in scripts]}
    self.parent.context.rptObj.jsImports.add(name)
    d3_chart = GraphD3.Script(self.parent.context.rptObj, data or [], width, height, htmlCode, options or {}, profile)
    self.parent.context.register(d3_chart)
    return d3_chart
