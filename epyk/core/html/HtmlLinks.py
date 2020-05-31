
import json

from epyk.core.html import Html

# The list of CSS classes
# from epyk.core.css.styles import GrpCls
# from epyk.core.css.styles import CssGrpClsText


class ExternalLink(Html.Html):
  name = 'External link'

  def __init__(self, report, text, url, icon, helper, height, decoration, options, profile):
    super(ExternalLink, self).__init__(report, {"text": text, "url": url}, css_attrs={'height': height}, profile=profile)
    # Add the internal components icon and helper
    self.add_icon(icon)
    self.add_helper(helper)
    if not 'url' in self.val:
      self.val['url'] = self.val['text']
    if 'target' in options:
      self.set_attrs(name="target", value=options['target'])
    self.decoration, self.__url = decoration, {}

  @property
  def _js__builder__(self):
    return 'htmlObj.innerHTML = data.text; htmlObj.href = data.url'

  def no_decoration(self, color=None):
    """
    Property to remove the list default style
    """
    self.style.css.text_decoration = None
    self.style.list_style_type = None
    if color is None:
      color = self._report.theme.greys[-1]
    self.style.css.color = color
    return self

  def build(self, data=None, options=None, profile=False):
    if not isinstance(data, dict):
      data = {"text": data}
    if "url" not in data:
      data["url"] = self.val["url"]
    return super(ExternalLink, self).build(data, options, profile)

  def __str__(self):
    self.set_attrs(name="href", value=self.val['url'])
    return '<a %s>%s</a>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val['text'], self.helper)


class DataLink(Html.Html):
  name = 'Data link'
  # _grpCls = CssGrpClsText.CssClassHref

  def __init__(self, report, text, value, width, height, format, profile):
    super(DataLink, self).__init__(report, {"text": text, 'value': value}, profile=profile,
                                   css_attrs={"width": width, 'height': height})
    self.format = format

  @property
  def no_decoration(self):
    """
    Property to remove the list default style
    """
    self.style.css.text_decoration = None
    self.style.css.list_style_type = None
    return self

  @property
  def _js__builder__(self):
    return '''
      var b = new Blob([data.value]); htmlObj.href = URL.createObjectURL(b);
      htmlObj.innerHTML = data.text'''

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<a %(attr)s href="#" download="Download.%(format)s" type="text/%(format)s">%(val)s</a>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'val': self.val['text'], 'format': self.format}


class Bridge(Html.Html):
  requirements = ('jquery', )
  name = 'Node Bridge'

  def __init__(self, report, text, script_name, report_name, url, jsData, context):
    super(Bridge, self).__init__(report, text)
    self.scriptName, self.reportName, self.url = script_name, report_name, url
    if context is not None:
      self.pmts = ["%s: %s" % (k, json.dumps(v))for k, v in context.items()]
    else:
      self.pmts = []
    if jsData is not None:
      for htmlObj in jsData:
        if isinstance(htmlObj, str):
          try:
            htmlObj = report.component(htmlObj.htmlCode)
            self.pmts.append("%s: %s" % (htmlObj.htmlCode, htmlObj.val))
          except:
            # hook to assume the user is directly passing a key: value as a string
            self.pmts.append(htmlObj)
        else:
          self.pmts.append("%s: %s" % (htmlObj.htmlCode, htmlObj.val))
    self.addGlobalFnc('NodeBridge(script, report, url, pmts)', '''
      $.post("%s/node/route/" + report + "/" + script, {"url": url}, function(data){
        res = JSON.parse(data);
        if (res.valid){
          var pmt = []; for (k in pmts){pmt.push(k +"="+ pmts[k])};
          if (pmt.length > 0){var url = res['url'] +"?"+ pmt.join("&"); window.open(url, '_blank')}
          else{window.open(res['url'], '_blank')}}}) ''' % self._report._urlsApp['epyk-admin'])

  def __str__(self):
    if self._report.user != "anonymous":
      return "<a %(attr)s onclick='NodeBridge(\"%(scriptName)s\", \"%(reportName)s\", \"%(url)s\", {%(pmts)s})' href='#'>%(vals)s</a>" % {
        'attr': self.get_attrs(pyClassNames=self.defined), 'scriptName': self.scriptName, 'reportName': self.reportName,
        'url': self.url, 'pmts': ",".join(self.pmts), 'vals': self.vals}

    return ""
