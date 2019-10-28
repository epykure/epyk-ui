"""
Module for the HTML Media (audio and video) components
"""

import os

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls


class Media(Html.Html):
  name, category, callFnc = 'Video', 'Media', 'video'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, video, path, width, height, htmlCode, profile):
    if path is None:
      path = "/img/%s" % report.run.report_name
      # Check if the file is available in the default directory
      # Otherwise raise an exception
      file_path = os.path.join(report.run.local_path, "static", video)
      if not os.path.exists(file_path):
        raise Exception("Missing file %s in %s" % (video, os.path.join(report.run.local_path, "static")))

    if not video.upper().endswith("MP4"):
      raise Exception("Only MP4 format supported by this HTML container")

    super(Media, self).__init__(report, {'path': path, 'video': video}, code=htmlCode, width=width[0], widthUnit=width[1],
                                height=height[0], heightUnit=height[1], profile=profile)

  @property
  def jqId(self): return "$('#%s video')" % self.htmlId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, '''
      htmlObj.empty(); htmlObj.append("<source src=\'" + data.path + "/" + data.video + "\' type='video/mp4'/>")''',
                      'Javascript Object builder')

  def __str__(self):
    return '''<div %s><video style="width:100%%" controls></video></div>''' % self.strAttr(pyClassNames=self.defined)


class Audio(Html.Html):
  name, category, callFnc = 'Video', 'Media', 'audio'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, audio, path, autoplay, width, height, htmlCode, profile):
    if path is None:
      path = "/img/%s" % report.run.report_name
      # Check if the file is available in the default directory
      # Otherwise raise an exception
      file_path = os.path.join(report.run.local_path, "static", audio)
      if not os.path.exists(file_path):
        raise Exception("Missing file %s in %s" % (audio, os.path.join(report.run.local_path, "static")))

    super(Audio, self).__init__(report, {'path': path, 'audio': audio}, width=width[0], widthUnit=width[1], height=height[0],
                                heightUnit=height[1], code=htmlCode, profile=profile)
    self.autoplay = autoplay

  @property
  def jqId(self): return "$('#%s audio')" % self.htmlId

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, '''
      htmlObj.empty(); htmlObj.append("<source src='" + data.path + "/" + data.audio + "' type='audio/mpeg'>")''', 'Javascript Object builder')

  def __str__(self):
    options = ["controls"]
    if self.autoplay:
      options.append("autoplay")
    return '''<div %(attrs)s><audio style="width:100%%" %(options)s></audio></div>''' % {'attrs': self.strAttr(pyClassNames=self.defined), "options": " ".join(options)}


class Youtube(Html.Html):
  name, category, callFnc = 'Youtube Video', 'Media', 'youtube'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, link, width, height, htmlCode, profile):
    super(Youtube, self).__init__(report, link, width=width[0], widthUnit=width[1], height=height[0],
                                  heightUnit=height[1], code=htmlCode, profile=profile)

  def __str__(self):
    return '''
      <div %(attrs)s><iframe width="420" height="315" type="text/html" src="%(link)s"> </iframe></div>
      ''' % {'attrs': self.strAttr(pyClassNames=self.defined), 'link': self.vals}
