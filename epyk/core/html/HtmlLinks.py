"""
Core modules in charge of providing links services
"""

import json
import re

from epyk.core.html import Html
from epyk.core.js.Imports import requires
from epyk.core.js import JsUtils


# The list of CSS classes
from epyk.core.css.groups import CssGrpCls
from epyk.core.css.groups import CssGrpClsText


class ExternalLink(Html.Html):
  name, category, callFnc = 'External link', 'Links', 'externallink'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, text, url, icon, helper, height, decoration, options, profile):
    super(ExternalLink, self).__init__(report, {"text": text, "url": url}, height=height[0], heightUnit=height[1], profile=profile)
    # Add the internal components icon and helper
    self.add_icon(icon)
    self.add_helper(helper)
    if not 'url' in self.vals:
      self.vals['url'] = self.vals['text']
    if 'target' in options:
      self.addAttr("target", options['target'])
    self.decoration, self.options, self.__url = decoration, options, {}

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, ''' 
      htmlObj.append(data.text); htmlObj.attr('href', data.url)''', 'Javascript Object builder')

  def __str__(self):
    return '<a %s></a>%s' % (self.strAttr(pyClassNames=self.defined), self.helper)

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
  _grpCls = CssGrpClsText.CssClassHref

  def __init__(self, report, recordSet, value, width, height, format, profile):
    super(DataLink, self).__init__(report, recordSet, width=width[0], widthUnit=width[1], height=height[0],
                                   heightUnit=height[1], profile=profile)
    self.format = format
    self.click(value)

  @property
  def jsQueryData(self): return "{}"

  def click(self, data):
    """
    Override the click event in order to download some Javascript data instead

    :param data: The data (Python or JsPy Objects

    :return: The link object
    """
    data = JsUtils.jsConvertData(data, None)
    return super(DataLink, self).click(self.dom.onclick('var csv = %s; var data = new Blob([csv]); this.href = URL.createObjectURL(data)' % data).toStr())

  def __str__(self):
    return '<a %(attr)s href="#" download="Download.%(format)s" type="text/%(format)s">%(val)s</a>' % {'attr': self.strAttr(pyClassNames=self.defined), 'val': self.vals, 'format': self.format}


class Bridge(Html.Html):
  reqCss, reqJs = [], ['jquery']
  name, category, callFnc = 'Node Bridge', 'Links', 'bridge'
  _grpCls = CssGrpCls.CssGrpClassBase

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
        'attr': self.strAttr(pyClassNames=self.defined), 'scriptName': self.scriptName, 'reportName': self.reportName,
        'url': self.url, 'pmts': ",".join(self.pmts), 'vals': self.vals}

    return ""
