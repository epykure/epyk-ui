
from epyk.core import html
from epyk.core.js.packages import JsFontAwesome


class Icons(object):
  def __init__(self, context):
    self.context = context

  @property
  def get(self):
    return JsFontAwesome

  def awesome(self, icon, text=None, tooltip=None, position=None, width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.icons.awesome(icon="fas fa-align-center")

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    html_edit = html.HtmlButton.IconEdit(self.context.rptObj, position, icon, text, tooltip, width, height, htmlCode, profile)
    html_edit.style.css.float = position
    html_edit.style.css.display = "inline-block"
    self.context.register(html_edit)
    return html_edit

  def edit(self, text=None, position=None, tooltip="Edit", width=(None, 'px'), height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.icons.edit()
    rptObj.ui.icons.edit().color("red")

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-edit', text, position, tooltip, width, height, htmlCode, profile)

  def clock(self, text=None, position=None, tooltip="Last Updated Time", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-clock', text, position, tooltip, width, height, htmlCode, profile)

  def refresh(self, text=None, position=None, tooltip="Refresh Component", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-sync-alt', text, position, tooltip, width, height, htmlCode, profile)

  def pdf(self, text=None, position=None, tooltip="Convert to PDF", width=(None, 'px'), height=(None, 'px'),
          htmlCode=None,  profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.icons.pdf(tooltip="helper")

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-file-pdf', text, position, tooltip, width, height, htmlCode, profile)

  def plus(self, text=None, position=None, tooltip="Add line", width=(None, 'px'), height=(None, 'px'),
           htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-plus-square', text, position, tooltip, width, height, htmlCode, profile)

  def excel(self, text=None, position=None, tooltip="Convert to Excel", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-file-excel', text, position, tooltip, width, height, htmlCode, profile)

  def download(self, text=None, position=None, tooltip="Download", width=(None, 'px'), height=(None, 'px'),
               htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-download', text, position, tooltip, width, height, htmlCode, profile)

  def delete(self, text=None, position=None, tooltip="Delete Component on the page", width=(None, 'px'),
             height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-trash-alt', text, position, tooltip, width, height, htmlCode, profile)

  def zoom(self, text=None, position=None, tooltip="Zoom on Component", width=(None, 'px'), height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-search-plus', text, position, tooltip, width, height, htmlCode, profile)

  def capture(self, text=None, position=None, tooltip="Save to clipboard", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-clipboard', text, position, tooltip, width, height, htmlCode, profile)

  def remove(self, text=None, position=None, tooltip="Remove Item", width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-times-circle', text, position, tooltip, width, height, htmlCode, profile)

  def table(self, text=None, position=None, tooltip="Convert to Table", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.icons.table(tooltip="helper")

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-table', text, position, tooltip, width, height, htmlCode, profile)

  def wrench(self, text=None, position=None, tooltip="Processing Time", width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-wrench', text, position, tooltip, width, height, htmlCode, profile)

  def facebook(self, text=None, url="https://en-gb.facebook.com/", position=None, tooltip="Facebook", width=(25, 'px'),
               htmlCode=None, profile=None):
    icon = self.awesome('fab fa-facebook-f', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def twitter(self, text=None, url="https://twitter.com", position=None, tooltip="Twitter", width=(25, 'px'),
              htmlCode=None, profile=None):
    icon = self.awesome('fab fa-twitter', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def linkedIn(self, text=None, url="https://www.linkedin.com/home/?originalSubdomain=uk", position=None, tooltip="linkedIn",
               width=(25, 'px'), htmlCode=None, profile=None):
    icon = self.awesome('fab fa-linkedin-in', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def youtube(self, text=None, url="https://www.youtube.com/", position=None, tooltip="Follow us on Youtube",
              width=(25, 'px'), htmlCode=None, profile=None):
    icon = self.awesome('fab fa-youtube', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()# addCls("CssDivOnHoverBackgroundLight")
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def github(self, text=None, url="https://github.com/", position=False, tooltip="Go the the Github project",
             width=(25, 'px'), htmlCode=None, profile=None):
    icon = self.awesome('fab fa-github', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def python(self, text=None, url="https://pypi.org/", position=None, tooltip="Like or package",
             width=(25, 'px'), htmlCode=None, profile=None):
    icon = self.awesome("fab fa-python", text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def stackoverflow(self, text=None, url="https://stackoverflow.com/", position=None, tooltip="Share your comments",
                    width=(25, 'px'), htmlCode=None, profile=None):
    icon = self.awesome("fab fa-stack-overflow", text, position, tooltip, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def epyk(self, align="center", format='logo'):
    """
    Description:
    ------------
    Add the Epyk Icon

    Usage:
    ------
    rptObj.ui.icons.epyk()

    Attributes:
    ----------
    :param align:
    :param format:
    :rtype: html.HtmlImage.Image
    """
    if format == 'logo':
      img, width, height = "epyklogo.ico", (32, 'px'), (32, 'px')
    elif format == 'small':
      img, width, height = "epyklogo_whole_small.png", (45, 'px'), (32, 'px')
    else:
      img, width, height = "epyklogo_whole_big.png", ("auto", ''), ('auto', '')
    icon = self.context.rptObj.ui.img(img, path="https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images",
                                      align=align, width=width, height=height)
    icon.css({"text-align": "center", "padding": "auto", "vertical-align": "middle"})
    icon.style.add_classes.div.background_hover()
    return icon

  def signin(self, text, width=(40, "px"), icon=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.icons.signin("test")

    Attributes:
    ----------
    :return:
    """
    bar = html.HtmlEvent.SignIn(self.context.rptObj, text, width, icon)
    self.context.register(bar)
    return bar
