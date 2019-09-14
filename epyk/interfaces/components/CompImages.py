"""

"""

from epyk.core import html


class Images(object):
  def __init__(self, context):
    self.context = context

  def img(self, text=None, path=None, width=(100, "%"), height=(None, "px"), align="center", htmlCode=None,
          serverSettings=None, profile=None):
    """

    Example

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_ref_css_images.asp
    https://www.w3schools.com/cssref/css3_pr_border-radius.asp

    :param text:
    :param path:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param serverSettings:
    :param profile:

    :rtype: html.HtmlImage.Image

    :return:
    """
    return self.context.register(html.HtmlImage.Image(self.context.rptObj, text, path, align, htmlCode, width,
                                                      height, serverSettings, profile))

  def img_animated(self, image=None, text="", title="", url=None, path=None, width=(200, "px"), height=(200, "px"),
                   serverSettings=None, profile=None):
    """

    Example

    Documentation
    https://tympanus.net/Tutorials/OriginalHoverEffects/

    :param image:
    :param text:
    :param title:
    :param url:
    :param path:
    :param width:
    :param height:
    :param serverSettings:
    :param profile:

    :rtype: html.HtmlImage.AnimatedImage

    :return:
    """
    return self.context.register(html.HtmlImage.AnimatedImage(self.context.rptObj, image, text, title, url, path, width,
                                                              height, serverSettings, profile))

  def carrousel(self, images, path=None, width=(100, "%"), height=(None, "px"), serverSettings=None, profile=None):
    """

    Example

    Documentation
    https://www.cssscript.com/basic-pure-css-slideshow-carousel/

    :param images:
    :param path:
    :param width:
    :param height:
    :param serverSettings:
    :param profile:

    :rtype: html.HtmlImage.ImgCarrousel

    :return:
    """
    return self.context.register(html.HtmlImage.ImgCarrousel(self.context.rptObj, images, path, width, height,
                                                             serverSettings, profile))

  def emoji(self, text=None, top=(20, 'px'), profile=None):
    """

    Example

    Documentation
    https://github.com/wedgies/jquery-emoji-picker

    :param text:
    :param top:
    :param profile:

    :rtype: html.HtmlImage.Emoji

    :return:
    """
    return self.context.register(html.HtmlImage.Emoji(self.context.rptObj, text, top, profile))

  def icon(self, text=None, size=(None, "px"), width=(None, 'px'), height=(None, "px"), tooltip=None, profile=None):
    """

    Documentation
    https://fontawesome.com/icons?m=free

    :param text:
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param tooltip:
    :param profile:

    :rtype: html.HtmlImage.Icon

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlImage.Icon(self.context.rptObj, text, size=size, width=width,
                                                     height=height, tooltip=tooltip, profile=profile))

  def badge(self, text=None, label=None, size=None, icon=None, background_color=None, color=None, tooltip=None, profile=None):
    """
    Display a badge component using Bootstrap

    Example
    rptObj.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")

    Documentation
    https://getbootstrap.com/docs/4.0/components/badge/

    :param text: The content of the badge
    :param label: Optional, The label to display close to the badge
    :param size: Optional, A tuple with a integer for the size and its unit
    :param icon: Optional, A String with the icon to display from font-awesome
    :param background_color: Optional, The background color of the badge
    :param color: Optional, The text color of the badge
    :param tooltip: Optional, The text to display in the tooltip
    :param profile: Optional, A boolean to store the performances for each components

    :rtype: html.HtmlImage.Badge

    :return:
    """
    return self.context.register(html.HtmlImage.Badge(self.context.rptObj, text, label, icon, size, background_color,
                                                      color, tooltip, profile))
