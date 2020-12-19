#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module for the HTML Media (audio and video) components
"""

import os

from epyk.core.html import Html
from epyk.core.html import Defaults

# The list of JSS modules
from epyk.core.js import JsUtils


class Media(Html.Html):
  name = 'Video'

  def __init__(self, report, video, path, width, height, htmlCode, profile, options):
    if path is None:
      path = Defaults.SERVER_PATH or os.path.split(video)[0]
    super(Media, self).__init__(report, {'path': path, 'video': video}, htmlCode=htmlCode,
                                css_attrs={"width": width, 'height': height}, profile=profile)
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
    Description:
    ------------
    Set the autoplay flag.

    Attributes:
    ----------
    :param flag: Boolean. Optional. Default value is true.
    """
    if flag:
      self.set_attrs(name="autoplay", value=flag)
    return self

  def __str__(self):
    if 'autoplay' in self._jsStyles:
      self.set_attrs(name="autoplay", value=JsUtils.jsConvertData(self._jsStyles["autoplay"], None))
    self.set_attrs(name="src", value=os.path.join(self.val['path'], self.val['video']))
    return '<video %s></video>' % self.get_attrs(pyClassNames=self.style.get_classes())


class Audio(Html.Html):
  name = 'Video'

  def __init__(self, report, audio, path, width, height, htmlCode, profile, options):
    if path is None:
      path = Defaults.SERVER_PATH or os.path.split(audio)[0]
    super(Audio, self).__init__(report, {'path': path, 'audio': audio}, css_attrs={"width": width, 'height': height}, htmlCode=htmlCode, profile=profile)
    self._jsStyles = options
    self.add_options(name="type", value='audio/%s' % {'mp3': 'mpeg'}.get(audio.split(".")[-1].lower(), audio.split(".")[-1]))
    self.set_attrs(name="controls", value="controls")

  def autoplay(self, flag=True):
    """
    Description:
    ------------
    Set the autoplay flag.

    Attributes:
    ----------
    :param flag: Boolean. Optional. Default value is true
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
    self.set_attrs(name="src", value=os.path.join(self.val['path'], self.val['audio']))
    return '<audio %(attrs)s></audio>' % {'attrs': self.get_attrs(pyClassNames=self.style.get_classes())}


class Youtube(Html.Html):
  name = 'Youtube Video'

  def __init__(self, report, link, width, height, htmlCode, profile, options):
    super(Youtube, self).__init__(report, link, css_attrs={"width": width, 'height': height}, htmlCode=htmlCode, profile=profile)
    self._jsStyles = options
    self._jsStyles['src'] = link

  def __str__(self):
    opts = ["%s='%s'" % (k, v) for k, v in self._jsStyles.items()]
    return '''
      <div %(attrs)s><iframe %(options)s></iframe></div>
      ''' % {'attrs': self.get_attrs(pyClassNames=self.style.get_classes()), 'link': self.val, 'options': " ".join(opts)}

  @staticmethod
  def get_embed_link(youtube_link):
    """
    Description:
    -------------
    simple function to convert a youtube link to the embedded version

    Usage:
    ------

      html.HtmlMedia.Youtube.get_embed_link('https://www.youtube.com/watch?v=iPGgnzc34tY')

    Attributes:
    ----------
    :param youtube_link: String. The youtube link of the online video.
    """
    return 'http://www.youtube.com/embed/%s' % youtube_link.split('=')[-1]
