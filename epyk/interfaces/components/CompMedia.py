"""
Entry point for all the Media components.
"""

from epyk.core import html


class Media(object):
  def __init__(self, context):
    self.context = context

  def video(self, value, path=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, profile=None, options=None):
    """
    Add a video from the server to the page.
    The format for the video must be MP4

    Usage::

      rptObj.ui.media.video("CWWB3673.MP4")

    Documentation
    https://www.w3schools.com/html/html5_video.asp

    Attributes:
    ----------
    :param value: The name of the video
    :param path: Optional. THe path to the video
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. A dictionary with the components properties
    """
    dft_options = {"autoplay": True}
    if options is not None:
      dft_options.update(options)
    html_media = html.HtmlMedia.Media(self.context.rptObj, value, path, width, height, htmlCode, profile, dft_options)
    self.context.register(html_media)
    return html_media

  def audio(self, value, path=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, profile=None, options=None):
    """
    Add a audio track from the server to the page.
    The format for the video must be mpeg

    Usage::

      rptObj.ui.media.video("CWWB3673.mpeg")

    Documentation
    https://www.w3schools.com/html/html5_video.asp

    Attributes:
    ----------
    :param value: The name of the audio object
    :param path: Optional. THe path to the audio object
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. A dictionary with the components properties
    """
    dft_options = {"autoplay": True}
    if options is not None:
      dft_options.update(options)
    html_audio = html.HtmlMedia.Audio(self.context.rptObj, value, path, width, height, htmlCode, profile, dft_options)
    self.context.register(html_audio)
    return html_audio

  def youtube(self, link, width=(100, '%'), height=(None, 'px'), htmlCode=None, profile=None, options=None):
    """
    This will add a youtube video using the shared line to embedded to a website.

    Usage::

      rptObj.ui.media.youtube("https://www.youtube.com/embed/dfiHMtih5Ac")

    Documentation
    https://www.w3schools.com/html/html5_video.asp

    Attributes:
    ----------
    :param link: The youtube link
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. A dictionary with the components properties
    """
    dflt_options = {"width": "420", "height": "315", "type": "text/html"}
    if options is not None:
      dflt_options.update(options)
    html_youtube = html.HtmlMedia.Youtube(self.context.rptObj, link, width, height, htmlCode, profile, dflt_options)
    self.context.register(html_youtube)
    return html_youtube

  def camera(self):
    """

    Documentation
    https://www.html5rocks.com/en/tutorials/getusermedia/intro/

    Attributes:
    ----------
    :return:
    """
