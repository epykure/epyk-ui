"""
Core modules in charge of providing links services
"""

import json
import re

from epyk.core.html import Html
from epyk.core.js.Imports import requires

# The list of CSS classes
# from epyk.core.css.styles import GrpCls
# from epyk.core.css.styles import CssGrpClsText


class ExternalLink(Html.Html):
  name, category, callFnc = 'External link', 'Links', 'externallink'

  def __init__(self, report, text, url, icon, helper, height, decoration, options, profile):
    super(ExternalLink, self).__init__(report, {"text": text, "url": url}, css_attrs={'height': height}, profile=profile)
    # Add the internal components icon and helper
    self.add_icon(icon)
    self.add_helper(helper)
    if not 'url' in self.val:
      self.val['url'] = self.val['text']
    if 'target' in options:
      self.set_attrs(name="target", value=options['target'])
    self.decoration, self.options, self.__url = decoration, options, {}

  @property
  def _js__builder__(self):
    return 'htmlObj.innerHTML = data.text; htmlObj.href = data.url'

  @property
  def no_decoration(self):
    """
    Property to remove the list default style
    """
    self.style.css.text_decoration = None
    self.style.list_style_type = None
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

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val):
    result = re.findall("\[([a-zA-Z 0-9]*)\]\(http([:a-zA-Z\/\.\ 0-9]*)\)", val)
    if not result:
      result = re.findall('\[([a-zA-Z 0-9]*)\]\(<a href\=\"http://([:a-zA-Z/.0-9]*)\">', val)
    return result

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report):
    for name, url in regExpResult:
      val = val.replace("[%s](http%s)" % (name, url), "report.externallink('%s', 'http%s')" % (name, url))
      if report is not None:
        getattr(report, 'link')({'url': url, 'text': name})
    return [val]

  @classmethod
  def jsMarkDown(cls, vals): return "[%s](%s)" % (vals['text'], vals['url'])

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    """

    :param document:
    :return:
    """
    pkg_docx = requires("docx", reason='Missing Package', install='python-docx', source_script=__file__)

    p = document.add_paragraph()
    hyperlink = pkg_docx.oxml.shared.OxmlElement('w:hyperlink')
    r_id = p.part.relate_to(self.vals['url'], pkg_docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    hyperlink.set(pkg_docx.oxml.shared.qn('r:id'), r_id, )
    new_run = pkg_docx.oxml.shared.OxmlElement('w:r')
    new_run.append(pkg_docx.oxml.shared.OxmlElement('w:rPr'))
    new_run.text = self.vals['text']
    hyperlink.append(new_run)
    p._p.append(hyperlink)

  def to_xls(self, workbook, worksheet, cursor):
    worksheet.write_url(cursor['row'], 0, self.vals['url'], string=self.vals['text'])
    cursor['row'] += 2


class DataLink(Html.Html):
  name, category, callFnc = 'Data link', 'Links', 'linkdata'
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
  reqCss, reqJs = [], ['jquery']
  name, category, callFnc = 'Node Bridge', 'Links', 'bridge'
  # _grpCls = GrpCls.CssGrpClassBase

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
            htmlObj = self.itemFromCode(htmlObj)
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
