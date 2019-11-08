"""
Module for the HTML Media (audio and video) components
"""

import os

from epyk.core.html import Html

# The list of JSS modules
from epyk.core.js import JsUtils

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls


class Media(Html.Html):
  name, category, callFnc = 'Video', 'Media', 'video'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, video, path, width, height, htmlCode, profile, options):
    if path is None:
      path = "/img/%s" % report.run.report_name
      # Check if the file is available in the default directory
      # Otherwise raise an exception
      file_path = os.path.join(report.run.local_path, "static", video)
      if not os.path.exists(file_path):
        raise Exception("Missing file %s in %s" % (video, os.path.join(report.run.local_path, "static")))

    super(Media, self).__init__(report, {'path': path, 'video': video}, code=htmlCode, width=width[0], widthUnit=width[1],
                                height=height[0], heightUnit=height[1], profile=profile)
    self._jsStyles = options
    self.add_options(name="type", value='video/%s' % video.split(".")[-1])
    self.set_attrs(name="controls", value="controls")

  @property
  def _js__builder__(self):
    return '''
      var source = document.createElement("source");
      source.setAttribute('src', data.path +"/"+ data.video);
      for(var key in options){
        if(key === 'autoplay'){htmlObj.autoplay = options.autoplay}
        else{source.setAttribute(key, options[key])}};
      htmlObj.appendChild(source)'''

  def autoplay(self, flag=True):
    """
    Set the autoplay flag

    :param flag: Boolean. Default value is true
    """
    if flag:
      self.set_attrs(name="autoplay", value=flag)
    return self

  def __str__(self):
    if 'autoplay' in self._jsStyles:
      self.set_attrs(name="autoplay", value=JsUtils.jsConvertData(self._jsStyles["autoplay"], None))
    return '<video %s></video>' % self.get_attrs(pyClassNames=self.defined)


class Audio(Html.Html):
  name, category, callFnc = 'Video', 'Media', 'audio'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, audio, path, width, height, htmlCode, profile, options):
    if path is None:
      path = "/img/%s" % report.run.report_name
      # Check if the file is available in the default directory
      # Otherwise raise an exception
      file_path = os.path.join(report.run.local_path, "static", audio)
      if not os.path.exists(file_path):
        raise Exception("Missing file %s in %s" % (audio, os.path.join(report.run.local_path, "static")))

    super(Audio, self).__init__(report, {'path': path, 'audio': audio}, width=width[0], widthUnit=width[1], height=height[0],
                                heightUnit=height[1], code=htmlCode, profile=profile)
    self._jsStyles = options
    self.add_options(name="type", value='audio/%s' % {'mp3': 'mpeg'}.get(audio.split(".")[-1].lower(), audio.split(".")[-1]))
    self.set_attrs(name="controls", value="controls")

  def autoplay(self, flag=True):
    """
    Set the autoplay flag

    :param flag: Boolean. Default value is true
    """
    if flag:
      self.set_attrs(name="autoplay", value=flag)
    return self

  @property
  def _js__builder__(self):
    return '''
      var source = document.createElement("source");
      source.setAttribute('src', data.path +"/"+ data.audio);
      for(var key in options){
        if(key === 'autoplay'){htmlObj.autoplay = options.autoplay}
        else{source.setAttribute(key, options[key])}}; 
      htmlObj.appendChild(source)'''

  def __str__(self):
    if 'autoplay' in self._jsStyles:
      self.set_attrs(name="autoplay", value=JsUtils.jsConvertData(self._jsStyles["autoplay"], None))
    return '<audio %(attrs)s></audio>' % {'attrs': self.get_attrs(pyClassNames=self.defined)}


class Youtube(Html.Html):
  name, category, callFnc = 'Youtube Video', 'Media', 'youtube'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, link, width, height, htmlCode, profile):
    super(Youtube, self).__init__(report, link, width=width[0], widthUnit=width[1], height=height[0],
                                  heightUnit=height[1], code=htmlCode, profile=profile)

  def __str__(self):
    return '''
      <div %(attrs)s><iframe width="420" height="315" type="text/html" src="%(link)s"></iframe></div>
      ''' % {'attrs': self.get_attrs(pyClassNames=self.defined), 'link': self.vals}
