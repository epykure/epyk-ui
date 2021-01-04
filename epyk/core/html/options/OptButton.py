#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from epyk.core.html.options import Options


class OptionsButton(Options):

  @property
  def multiple(self):
    """
    Description:
    ------------
    Property to define if multiple buttons can be selected at the same time.
    Default value is false.

    Usage:
    -----


    Attributes:
    ----------
    :prop bool: Boolean. To be used if multiple buttons are grouped.
    """
    return self.get(False)

  @multiple.setter
  def multiple(self, bool):
    self.set(bool)

  @property
  def group(self):
    """
    Description:
    ------------
    Property to set the group name of a button.

    Usage:
    -----

    Attributes:
    ----------
    :prop val:
    """
    return self._report.attr.get('name')

  @group.setter
  def group(self, val):
    self._report.set_attrs(name='name', value=val)


class OptionsBadge(Options):

  @property
  def badge_css(self):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :prop css:
    """
    return self.get()

  @badge_css.setter
  def badge_css(self, css):
    if hasattr(self, '_report') and hasattr(self._report, 'link'):
      self._report.link.css(css)
    cssOpts = self.get({})
    cssOpts.update(css)
    self.set(cssOpts)

  @property
  def badge_position(self):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :prop position:
    """
    return self.get()

  @badge_position.setter
  def badge_position(self, position):
    if position == 'left':
      self.set({"position": 'relative'}, name='badge_css')
    else:
      self.set({"position": 'relative', "top": "-4px", "right": "11px"}, name='badge_css')
    self.set(position)


class OptMedia(Options):

  @property
  def controls(self):
    """
    Description:
    ------------
    Specifies that video controls should be displayed (such as a play/pause button etc).

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/tags/tag_video.asp
      https://www.w3schools.com/tags/att_video_controls.asp

    Attributes:
    ----------
    :param bool: Boolean. Optional. Default value is false.
    """
    return self.get(True)

  @controls.setter
  def controls(self, bool=True):
    self.set(bool)

  @property
  def loop(self):
    """
    Description:
    ------------
    Specifies that the video will start over again, every time it is finished.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/tags/tag_video.asp
      https://www.w3schools.com/tags/att_video_loop.asp

    Attributes:
    ----------
    :prop bool: Boolean. Optional. Default value is false.
    """
    return self.get(False)

  @loop.setter
  def loop(self, bool=False):
    self.set(bool)

  @property
  def preload(self):
    """
    Description:
    ------------
    Specifies if and how the author thinks the video should be loaded when the page loads.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/tags/tag_video.asp
      https://www.w3schools.com/tags/att_video_preload.asp

    Attributes:
    ----------
    :prop value: String. Optional. The preload attribute specifies if and how the author thinks that the video should be loaded when the page loads.
    """
    return self.get('none')

  @preload.setter
  def preload(self, value="auto"):
    value = value or "none"
    if self.options.verbose and value not in ("none", "auto", "metadata"):
      logging.warning("Not defined preload value %s" % value)
    self.set(value)

  @property
  def muted(self):
    """
    Description:
    ------------
    Specifies that the audio output of the video should be muted.

    The muted attribute is a boolean attribute.

    When present, it specifies that the audio output should be muted.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/tags/tag_video.asp
      https://www.w3schools.com/tags/att_audio_muted.asp

    Attributes:
    ----------
    :prop flag: Boolean. Optional. Default value is false.
    """
    return self.get(False)

  @muted.setter
  def muted(self, bool=False):
    self.set(bool)

  @property
  def poster(self):
    """
    Description:
    ------------
    Specifies an image to be shown while the video is downloading, or until the user hits the play button.

    The poster attribute specifies an image to be shown while the video is downloading,
    or until the user hits the play button.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/tags/tag_video.asp
      https://www.w3schools.com/tags/att_video_poster.asp

    Attributes:
    ----------
    :prop url: String. Url path for the image. Specifies the URL of the image file.
    """
    return self.get()

  @poster.setter
  def poster(self, url):
    self.set(url)

  @property
  def autoplay(self):
    """
    Description:
    ------------
    Set the autoplay flag.

    Specifies that the video will start playing as soon as it is ready.

    Usage:
    -----

    Attributes:
    ----------
    :prop flag: Boolean. Optional. Default value is true.
    """
    return self.get(True)

  @autoplay.setter
  def autoplay(self, bool=True):
    self.set(bool)
