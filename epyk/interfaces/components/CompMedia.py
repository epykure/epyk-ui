#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union

from epyk.core import html
from epyk.interfaces import Arguments


class Media:

  def __init__(self, ui):
    self.page = ui.page

  def video(self, value: str = "", align: str = "center", path: str = None, width: Union[tuple, int] = (100, '%'),
            height: Union[tuple, int] = (None, 'px'), html_code: str = None,
            profile: Union[bool, dict] = None, options: dict = None):
    """
    Description:
    -----------
    Add a video from the server to the page.
    The format for the video must be MP4.

    Usage::

      page.ui.media.video("CWWB3673.MP4")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMedia.Media`

    Related Pages:

      https://www.w3schools.com/html/html5_video.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/

    Attributes:
    ----------
    :param value: String. Optional. The name of the video.
    :param path: String. Optional. THe path to the video.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple | Integer. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Integer. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. The component identifier code (for both Python and Javascript).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"autoplay": True}
    if options is not None:
      dft_options.update(options)
    html_media = html.HtmlMedia.Media(self.page, value, path, width, height, html_code, profile, dft_options)
    if align == "center":
      html_media.style.css.margin = "auto"
      html_media.style.css.display = "block"
    html.Html.set_component_skin(html_media)
    return html_media

  def audio(self, value: str = "", path: str = None, width: Union[tuple, int] = (100, '%'),
            height: Union[tuple, int] = (None, 'px'),
            html_code: str = None, profile: Union[bool, dict] = None, options: dict = None):
    """
    Description:
    -----------
    Add a audio track from the server to the page.
    The format for the video must be mpeg.

    Usage::

      page.ui.media.video("CWWB3673.mpeg")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMedia.Audio`

    Related Pages

      https://www.w3schools.com/html/html5_video.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/

    Attributes:
    ----------
    :param value: String. Optional. The name of the audio object.
    :param path: String. Optional. THe path to the audio object.
    :param width: Tuple | Integer. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Integer. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"autoplay": True}
    if options is not None:
      dft_options.update(options)
    html_audio = html.HtmlMedia.Audio(self.page, value, path, width, height, html_code, profile, dft_options)
    html.Html.set_component_skin(html_audio)
    return html_audio

  def youtube(self, link: str, align: str = "center", width: Union[tuple, int] = (100, '%'),
              height: Union[tuple, int] = (None, 'px'), html_code: str = None,
              profile: Union[bool, dict] = None, options: dict = None):
    """
    Description:
    -----------
    This will add a youtube video using the shared line to embedded to a website.

    Usage::

      page.ui.media.youtube("https://www.youtube.com/embed/dfiHMtih5Ac")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMedia.Youtube`

    Related Pages

      https://www.w3schools.com/html/html5_video.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/

    Attributes:
    ----------
    :param link: String. The youtube link.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple | Integer. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Integer. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. The component identifier code (for both Python and Javascript).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. A dictionary with the components properties.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"width": "420", "height": "315", "type": "text/html"}
    if '/embed/' not in link:
      link = html.HtmlMedia.Youtube.get_embed_link(link)
    if options is not None:
      dflt_options.update(options)
    html_youtube = html.HtmlMedia.Youtube(self.page, link, width, height, html_code, profile, dflt_options)
    html_youtube.style.css.text_align = align
    html.Html.set_component_skin(html_youtube)
    return html_youtube

  def camera(self, align: str = "center", width: Union[tuple, int] = (100, '%'),
             height: Union[tuple, int] = (None, 'px'), html_code: str = None,
             profile: Union[bool, dict] = None, options: dict = None):
    """
    Description:
    -----------
    Add a video from the server to the page.
    The format for the video must be MP4.

    Usage::

      page.ui.media.camera()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlMedia.Camera`

    Related Pages:

      https://www.w3schools.com/html/html5_video.asp
      https://www.kirupa.com/html5/accessing_your_webcam_in_html5.htm

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/

    Attributes:
    ----------
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple | Integer. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Integer. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. The component identifier code (for both Python and Javascript).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"autoplay": True}
    if options is not None:
      dft_options.update(options)
    html_media = html.HtmlMedia.Camera(self.page, width, height, html_code, profile, dft_options)
    if align == "center":
      html_media.style.css.margin = "auto"
      html_media.style.css.display = "block"
    html.Html.set_component_skin(html_media)
    return html_media
