#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os

from epyk.core.html import Html
from epyk.core.html import Defaults
from epyk.core.html.options import OptButton

# The list of JSS modules
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml


class Source(Html.Html):
  name = 'Source'

  def __init__(self, report, path, video):
    super(Source, self).__init__(report, "")
    self.path = path
    self.video = video

  def __str__(self):
    self.attr["src"] = os.path.join(self.path, self.video)
    attrs = " ".join(['%s="%s"' % (k, v) for k, v in self.attr.items() if k not in ("class", 'css', 'id')])
    return "<source %s></source>" % attrs


class Media(Html.Html):
  name = 'Video'
  _option_cls = OptButton.OptMedia
  mime_mapping = {
    ".avi": "video/x-msvideo",
    ".mpeg": "video/mpeg",
    ".ogv": "video/ogg",
    ".webm": "video/webm",
    ".3gp": "video/3gpp",
    ".3g2": "video/3gpp2",
    ".mp4": "video/mp4",
  }

  def __init__(self, report, video, path, width, height, html_code, profile, options):
    if path is None:
      path = Defaults.SERVER_PATH or os.path.split(video)[0]
    super(Media, self).__init__(report, {'path': path, 'video': video}, html_code=html_code, options=options,
                                css_attrs={"width": width, 'height': height}, profile=profile)
    extension = video.split(".")[-1].lower()
    self._vals = Source(report, path, video)
    if ".%s" % extension in self.mime_mapping:
      self.add_options(name="type", value=self.mime_mapping[".%s" % extension])
      self._vals.attr["type"] = self.mime_mapping[".%s" % extension]
    else:
      if options.get("verbose", False):
        logging.warning("Missing MIME Type extension %s" % extension)
      self.add_options(name="type", value='%s/%s' % (self.name.lower(), extension))
      self._vals.attr["type"] = extension
    self.options.controls = True

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for a Media (video and audio).

    Usage::

    :rtype: OptButton.OptMedia
    """
    return super().options

  _js__builder__ = '''
    var source = document.createElement("source"); htmlObj.innerHTML = "";
    source.setAttribute('src', data.path +"/"+ data.video);
    for(var key in options){
      if(key === 'autoplay'){htmlObj.autoplay = options.autoplay}
      else{source.setAttribute(key, options[key])}};
    htmlObj.appendChild(source)'''

  def __str__(self):
    if 'autoplay' in self._jsStyles:
      self.set_attrs(name="autoplay", value=JsUtils.jsConvertData(self._jsStyles["autoplay"], None))
    self.set_attrs(name="src", value=os.path.join(self.val.path, self.val.video))
    if self.options.controls:
      self.attr["controls"] = True
    return '<video %s>%s</video>' % (self.get_attrs(pyClassNames=self.style.get_classes()), str(self._vals))


class Audio(Media):
  name = 'Audio'

  mime_mapping = {
    ".aac": "audio/aac",
    ".midi": "audio/midi",
    ".mp3": "audio/mp3",
    ".mid": "audio/midi",
    ".oga": "audio/ogg",
    ".weba": "audio/webm",
    ".wav": "audio/x-wav",
    ".3gp": "audio/3gpp",
    ".3g2": "audio/3gpp2",
  }

  _js__builder__ = '''
    var source = document.createElement("source"); htmlObj.innerHTML = "";
    source.setAttribute('src', data.path +"/"+ data.audio);
    for(var key in options){
      if(key === 'autoplay'){htmlObj.autoplay = options.autoplay}
      else{source.setAttribute(key, options[key])}}; 
    htmlObj.appendChild(source)'''

  def __str__(self):
    if 'autoplay' in self._jsStyles:
      self.set_attrs(name="autoplay", value=JsUtils.jsConvertData(self._jsStyles["autoplay"], None))
    self.set_attrs(name="src", value=os.path.join(self.val.path, self.val.video))
    return '<audio %(attrs)s>%(source)s</audio>' % {'attrs': self.get_attrs(pyClassNames=self.style.get_classes()),
                                                    "source": self.val}


class Youtube(Html.Html):
  name = 'Youtube Video'

  def __init__(self, report, link, width, height, html_code, profile, options):
    super(Youtube, self).__init__(report, link, css_attrs={"width": width, 'height': height}, html_code=html_code,
                                  profile=profile)
    self._jsStyles = options
    self._jsStyles['src'] = link

  def __str__(self):
    opts = " ".join(["%s='%s'" % (k, v) for k, v in self._jsStyles.items()])
    return '''
      <div %(attrs)s><iframe %(options)s></iframe></div>
      ''' % {'attrs': self.get_attrs(pyClassNames=self.style.get_classes()), 'link': self.val, 'options': opts}

  @staticmethod
  def get_embed_link(youtube_link):
    """
    Description:
    -------------
    simple function to convert a youtube link to the embedded version.

    Usage::-

      html.HtmlMedia.Youtube.get_embed_link('https://www.youtube.com/watch?v=iPGgnzc34tY')

    Attributes:
    ----------
    :param youtube_link: String. The youtube link of the online video.
    """
    return 'http://www.youtube.com/embed/%s' % youtube_link.split('=')[-1]


class Camera(Html.Html):
  name = 'Camera'
  _option_cls = OptButton.OptMedia

  def __init__(self, report, width, height, html_code, profile, options):
    super(Camera, self).__init__(report, "", html_code=html_code, css_attrs={"width": width, 'height': height},
                                 profile=profile, options=options)
    self.options.controls = True
    self.options.autoplay = True

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for a Media (video and audio).

    Usage::

    :rtype: OptButton.OptMedia
    """
    return super().options

  @property
  def dom(self):
    """
    Description:
    -----------
    The Javascript Dom object.

    Usage::

    :rtype: JsHtml.JsMedia
    """
    if self._dom is None:
      self._dom = JsHtml.JsMedia(self, report=self._report)
    return self._dom

  def __str__(self):
    if 'autoplay' in self._jsStyles:
      self.set_attrs(name="autoplay", value=JsUtils.jsConvertData(self._jsStyles["autoplay"], None))
    return '<video %s></video><img src="">' % self.get_attrs(pyClassNames=self.style.get_classes())
