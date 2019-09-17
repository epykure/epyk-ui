"""
Entry point for all the Media components.
"""

from epyk.core import html


class Media(object):
  def __init__(self, context):
    self.context = context

  def video(self, value, path=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, profile=None):
    """
    Add a video from the server to the page.
    The format for the video must be MP4

    Example
    rptObj.ui.media.video("CWWB3673.MP4")

    Documentation
    https://www.w3schools.com/html/html5_video.asp

    :param value: The name of the video
    :param path: Optional. THe path to the video
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlMedia.Media
    :return:
    """
    return self.context.register(html.HtmlMedia.Media(self.context.rptObj, value, path, width, height, htmlCode, profile))

  def audio(self, value, path=None, autoplay=True, width=(100, '%'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Add a audio track from the server to the page.
    The format for the video must be mpeg

    Example
    rptObj.ui.media.video("CWWB3673.mpeg")

    Documentation
    https://www.w3schools.com/html/html5_video.asp

    :param value: The name of the audio object
    :param path: Optional. THe path to the audio object
    :param autoplay: Optional. Start the audio when the page is loaded
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlMedia.Audio
    :return:
    """
    return self.context.register(html.HtmlMedia.Audio(self.context.rptObj, value, path, autoplay, width,
                                                      height, htmlCode, profile))

  def youtube(self, link, width=(100, '%'), height=(None, 'px'), htmlCode=None, profile=None):
    """
    This will add a youtube video using the shared line to embedded to a website.

    Example
    rptObj.ui.media.youtube("https://www.youtube.com/embed/dfiHMtih5Ac")

    Documentation
    https://www.w3schools.com/html/html5_video.asp

    :param link: The youtube link
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlMedia.Youtube
    :return:
    """
    return self.context.register(html.HtmlMedia.Youtube(self.context.rptObj, link, width, height, htmlCode, profile))

