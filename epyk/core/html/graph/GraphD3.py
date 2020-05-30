
# https://bl.ocks.org/ctufts/f38ef0187f98c537d791d24fda4a6ef9

from epyk.core.html import Html
from epyk.core.js import JsUtils


class Script(Html.Html):
  name = 'D3 Script'

  def __init__(self, report, data, width, height, htmlCode, options, profile):
    super(Script, self).__init__(report, data, code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__loader = ""
    self._jsStyles.update(options)
    self._jsStyles.update({"wdith": width[0], "height": height[0]})

  def data(self, data):
    if not isinstance(data, list):
      data = data.split(" ")
    self._vals = data

  def loader(self, str_frg, pretty_format=False):
    #fgs = [l.lstrip() for l in str_frg.split()]
    self.__loader = str_frg

  def build(self, data=None, options=None, profile=False):
    if not self.builder_name:
      raise Exception("No builder defined for this HTML component %s" % self.__class__.__name__)

    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[self.builder_name] = "function %s(htmlObj, data, options){%s}" % (
    self.builder_name, self.__loader)
    if isinstance(data, dict):
      # check if there is no nested HTML components in the data
      tmp_data = ["%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)) for k, v in data.items()]
      js_data = "{%s}" % ",".join(tmp_data)
    else:
      js_data = JsUtils.jsConvertData(data, None)
    options, js_options = options or self._jsStyles, []
    for k, v in options.items():
      if isinstance(v, dict):
        row = ["'%s': %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
        js_options.append("'%s': {%s}" % (k, ", ".join(row)))
      else:
        if k in self.js_fncs_opts or str(v).strip().startswith("function"):
          js_options.append("%s: %s" % (k, v))
        else:
          js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
    return "%s(%s, %s, %s)" % (self.builder_name, self.dom.d3.varId, js_data, "{%s}" % ",".join(js_options))

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
