"""
Module dedicated to produce Images components
"""

from epyk.core import html


class Images(object):
  def __init__(self, context):
    self.context = context

  def img(self, image=None, path=None, width=(100, "%"), height=(None, "px"), align="center", htmlCode=None,
          profile=None, options=None):
    """

    Example


    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_ref_css_images.asp
    https://www.w3schools.com/cssref/css3_pr_border-radius.asp

    :param image:
    :param path:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param profile:
    :param options:
    """
    html_image = html.HtmlImage.Image(self.context.rptObj, image, path, align, htmlCode, width, height, profile, options or {})
    self.context.register(html_image)
    return html_image

  def animated(self, image=None, text="", title="", url=None, path=None, width=(200, "px"), height=(200, "px"),
               profile=None):
    """

    Example
    rptObj.ui.images.animated("philo.PNG")

    Documentation
    https://tympanus.net/Tutorials/OriginalHoverEffects/

    :param image:
    :param text:
    :param title:
    :param url:
    :param path:
    :param width:
    :param height:
    :param profile:
    """
    html_id = html.HtmlImage.AnimatedImage(self.context.rptObj, image, text, title, url, path, width, height, profile)
    self.context.register(html_id)
    return html_id

  def carrousel(self, images, path=None, width=(100, "%"), height=('auto', ""), profile=None):
    """

    Example
    Defaults.SERVER_PATH = r"XXXXX"
    rptObj.ui.images.carrousel(["Capture.PNG", "philo.PNG"])

    Documentation
    https://www.cssscript.com/basic-pure-css-slideshow-carousel/

    :param images:
    :param path:
    :param width:
    :param height:
    :param profile:
    """
    html_i = html.HtmlImage.ImgCarrousel(self.context.rptObj, images, path, width, height, profile)
    self.context.register(html_i)
    return html_i

  def emoji(self, symbole=None, top=(20, 'px'), profile=None):
    """

    Example
    rptObj.ui.images.emoji(rptObj.symbols.smileys.DISAPPOINTED_FACE)

    Documentation
    https://github.com/wedgies/jquery-emoji-picker

    :param symbole:
    :param top:
    :param profile:
    """
    html_emoji = html.HtmlImage.Emoji(self.context.rptObj, symbole, top, profile)
    self.context.register(html_emoji)
    return html_emoji

  def icon(self, text=None, width=(None, 'px'), height=(None, "px"), color=None, tooltip=None, profile=None):
    """

    Example
    rptObj.ui.images.icon("fab fa-angellist")
    
    Documentation
    https://fontawesome.com/icons?m=free

    :param text:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color:
    :param tooltip:
    :param profile:
    """
    html_icon = html.HtmlImage.Icon(self.context.rptObj, text, width=width, height=height, color=color, tooltip=tooltip,
                                    profile=profile)
    self.context.register(html_icon)
    return html_icon

  def badge(self, text=None, label=None, icon=None, background_color=None, color=None, url=None,
            tooltip=None, options=None, profile=None):
    """
    Display a badge component using Bootstrap

    Example
    rptObj.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")
    rptObj.ui.images.badge("This is a badge", background_color="red", color="white")
    rptObj.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'right'})

    b = rptObj.ui.images.badge(7688, icon="fab fa-python", options={'badge_css': {'color': 'white', "background": 'red'}})
    b.options.badge_css = {"background": 'green'}

    Documentation
    https://getbootstrap.com/docs/4.0/components/badge/

    :param text: The content of the badge
    :param label: Optional, The label to display close to the badge
    :param icon: Optional, A String with the icon to display from font-awesome
    :param background_color: Optional, The background color of the badge
    :param color: Optional, The text color of the badge
    :param url:
    :param tooltip: Optional, The text to display in the tooltip
    :param options:
    :param profile: Optional, A boolean to store the performances for each components
    """
    html_badge = html.HtmlImage.Badge(self.context.rptObj, text, label, icon, background_color, color, url,
                                      tooltip, options or {}, profile)
    self.context.register(html_badge)
    return html_badge
