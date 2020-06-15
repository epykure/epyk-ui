
from epyk.core import html
from epyk.core.js.packages import JsFontAwesome


class Icons(object):
  def __init__(self, context):
    self.context = context

  @property
  def get(self):
    return JsFontAwesome

  def awesome(self, icon, text=None, tooltip=None, position=None, width=(25, 'px'), height=(25, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.icons.awesome(icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

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
    return html_edit

  def edit(self, text=None, position=None, tooltip="Edit", width=(None, 'px'), height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-edit <https://fontawesome.com/icons/edit>`_ icon

    Usage::

      rptObj.ui.icons.edit()
      rptObj.ui.icons.edit().color("red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-edit', text, tooltip, position, width, height, htmlCode, profile)

  def clock(self, text=None, position=None, tooltip="Last Updated Time", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-clock <https://fontawesome.com/icons/clock>`_ icon

    Usage::

      rptObj.ui.icons.clock()
      rptObj.ui.icons.clock().color("red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-clock', text, tooltip, position, width, height, htmlCode, profile)

  def refresh(self, text=None, position=None, tooltip="Refresh Component", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-sync-alt <https://fontawesome.com/icons/sync-alt>`_ icon

    Usage::

      rptObj.ui.icons.refresh()
      rptObj.ui.icons.refresh().color("red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-sync-alt', text, tooltip, position, width, height, htmlCode, profile)

  def pdf(self, text=None, position=None, tooltip="Convert to PDF", width=(None, 'px'), height=(None, 'px'),
          htmlCode=None,  profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-file-pdf <https://fontawesome.com/icons/file-pdf>`_ icon

    Usage::

      rptObj.ui.icons.pdf(tooltip="helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-file-pdf', text, tooltip, position, width, height, htmlCode, profile)

  def plus(self, text=None, position=None, tooltip="Add line", width=(None, 'px'), height=(None, 'px'),
           htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-file-pdf <https://fontawesome.com/icons/plus-square>`_ icon

    Usage::

      rptObj.ui.icons.plus()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-plus-square', text, tooltip, position, width, height, htmlCode, profile)

  def excel(self, text=None, position=None, tooltip="Convert to Excel", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-file-excel <https://fontawesome.com/icons/file-excel>`_ icon

    Usage::

      rptObj.ui.icons.excel()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-file-excel', text, tooltip, position, width, height, htmlCode, profile)

  def download(self, text=None, position=None, tooltip="Download", width=(None, 'px'), height=(None, 'px'),
               htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-download <https://fontawesome.com/icons/download>`_ icon

    Usage::

      rptObj.ui.icons.download()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-download', text, tooltip, position, width, height, htmlCode, profile)

  def delete(self, text=None, position=None, tooltip="Delete Component on the page", width=(None, 'px'),
             height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-trash-alt <https://fontawesome.com/icons/trash-alt>`_ icon

    Usage::

      rptObj.ui.icons.delete()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-trash-alt', text, tooltip, position, width, height, htmlCode, profile)

  def zoom(self, text=None, position=None, tooltip="Zoom on Component", width=(None, 'px'), height=(None, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-search-plus <https://fontawesome.com/icons/search-plus>`_ icon

    Usage::

      rptObj.ui.icons.zoom()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-search-plus', text, tooltip, position, width, height, htmlCode, profile)

  def capture(self, text=None, position=None, tooltip="Save to clipboard", width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `far fa-clipboard <https://fontawesome.com/icons/clipboard>`_ icon

    Usage::

      rptObj.ui.icons.capture()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-clipboard', text, tooltip, position, width, height, htmlCode, profile)

  def remove(self, text=None, position=None, tooltip="Remove Item", width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-times-circle <https://fontawesome.com/icons/times-circle>`_ icon

    Usage::

      rptObj.ui.icons.remove()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-times-circle', text, tooltip, position, width, height, htmlCode, profile)

  def table(self, text=None, position=None, tooltip="Convert to Table", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-table <https://fontawesome.com/icons/table>`_ icon

    Usage::

      rptObj.ui.icons.table(tooltip="helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-table', text, tooltip, position, width, height, htmlCode, profile)

  def wrench(self, text=None, position=None, tooltip="Processing Time", width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fas fa-wrench <https://fontawesome.com/icons/wrench>`_ icon

    Usage::

      rptObj.ui.icons.wrench()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-wrench', text, tooltip, position, width, height, htmlCode, profile)

  def facebook(self, text=None, url="https://en-gb.facebook.com/", position=None, tooltip="Facebook", width=(25, 'px'),
               htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-facebook-f <https://fontawesome.com/icons/facebook-f>`_ icon

    Usage::

      rptObj.ui.icons.facebook()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width:
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-facebook-f', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def twitter(self, text=None, url="https://twitter.com", position=None, tooltip="Twitter", width=(25, 'px'),
              htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-twitter <https://fontawesome.com/icons/twitter>`_ icon

    Usage::

      rptObj.ui.icons.twitter()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width:
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-twitter', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def linkedIn(self, text=None, url="https://www.linkedin.com/home/?originalSubdomain=uk", position=None, tooltip="linkedIn",
               width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-linkedin-in <https://fontawesome.com/icons/linkedin-in>`_ icon

    Usage::

      rptObj.ui.icons.linkedIn()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width:
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-linkedin-in', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def youtube(self, text=None, url="https://www.youtube.com/", position=None, tooltip="Follow us on Youtube",
              width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-youtube <https://fontawesome.com/icons/youtube>`_ icon

    Usage::

      rptObj.ui.icons.youtube()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width:
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-youtube', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()# addCls("CssDivOnHoverBackgroundLight")
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def github(self, text=None, url="https://github.com/", position=False, tooltip="Go the the Github project",
             width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-github <https://fontawesome.com/icons/github>`_ icon

    Usage::

      rptObj.ui.icons.github()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width:
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome('fab fa-github', text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def python(self, text=None, url="https://pypi.org/", position=None, tooltip="Like or package",
             width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-python <https://fontawesome.com/icons/python>`_ icon

    Usage::

      rptObj.ui.icons.python()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width:
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome("fab fa-python", text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def stackoverflow(self, text=None, url="https://stackoverflow.com/", position=None, tooltip="Share your comments",
                    width=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Same as :func:`epyk.interfaces.components.CompIcons.Icons.awesome` with a `fab fa-stack-overflow <https://fontawesome.com/icons/stack-overflow>`_ icon

    Usage::

      rptObj.ui.icons.stackoverflow()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.IconEdit`

    Attributes:
    ----------
    :param text:
    :param url:
    :param position:
    :param tooltip:
    :param width:
    :param htmlCode:
    :param profile:
    """
    icon = self.awesome("fab fa-stack-overflow", text, tooltip, position, width, width, htmlCode, profile)
    icon.css({"border-radius": "%spx" % width[0], "text-align": "center", "line-height": '%s%s' % (width[0], width[1])})
    icon.icon.css({"margin-right": "auto", "margin": "auto", "color": 'blue'})
    icon.style.add_classes.div.background_hover()
    icon.click([self.context.rptObj.js.navigateTo(url)])
    return icon

  def tick(self, flag=True, text=None, icons=(JsFontAwesome.ICON_CHECK, JsFontAwesome.ICON_TIMES), position=None,
           tooltip="", width=(None, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.icons.tick()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlRadio.Tick`

    Attributes:
    ----------
    :param text:
    :param icons:
    :param position:
    :param tooltip:
    :param width:
    :param htmlCode:
    :param profile:
    """
    dftl_options = {"true": icons[0], "false": icons[1]}
    dftl_options.update(options or {})
    # report, position, icon, text, tooltip, width, height, htmlCode, profile
    icon = html.HtmlRadio.Tick(self.context.rptObj, position, icons[0] if flag else icons[1], text, tooltip, width, width,
                               htmlCode, dftl_options, profile)
    icon.click([
      icon.icon.dom.switchClass(icons[0] if flag else icons[1], icons[1] if flag else icons[0]),
      icon.icon.dom.transition('background', self.context.rptObj.theme.success[0], duration=.2, reverse=True)
    ])
    return icon

  def epyk(self, align="center", format='logo'):
    """
    Description:
    ------------
    Add the Epyk Icon

    Usage::

      rptObj.ui.icons.epyk()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

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

    Usage::

      rptObj.ui.icons.signin("test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.SignIn

    Attributes:
    ----------

    """
    bar = html.HtmlEvent.SignIn(self.context.rptObj, text, width, icon)
    return bar

  def bar(self, records=None, color=None, width=(70, 'px'), height=(None, 'px'), options=None):
    """
    Description:
    ------------
    Add a bespoke options / actions bar with icons

    Usage::

      Related Pages:
Attributes:
    ----------
    :param records:
    :param color:
    :param width:
    :param height:
    :param options:
    """
    records = records or []
    options = options or {}
    html_opts = html.HtmlEvent.OptionsBar(self.context.rptObj, records, width, height, color, options)
    return html_opts

  def avatar(self, img, name=None, width=(30, 'px'), height=(None, ''), options=None, profile=None):
    """
    Description:
    ------------

Attributes:
    ----------
    :param img:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    img = img.replace("\\", "/")
    if height[0] is None:
      height = width
    avatar = self.context.rptObj.ui.div("&nbsp;", width=width, height=height, options=options, profile=profile)
    avatar.css({"padding": '5px', 'border-radius': '30px',
              'background-repeat': 'no-repeat',
              'background-position': 'center', 'background-size': 'cover', 'cursor': 'pointer',
              'background-image': 'url(%s)' % img})
    if name is not None:
      avatar.tooltip(name)
    return avatar

  def badge(self, text="", icon=None, width=(25, "px"), height=(25, "px"), background_color=None, color=None, url=None,
            tooltip=None, options=None, profile=None):
    """
    Description:
    ------------
    Display a badge component using Bootstrap

    Usage::

      rptObj.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")
      rptObj.ui.images.badge("This is a badge", background_color="red", color="white")
      rptObj.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'right'})

      b = rptObj.ui.images.badge(7688, icon="fab fa-python", options={'badge_css': {'color': 'white', "background": 'red'}})
      b.options.badge_css = {"background": 'green'}

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Badge`

    Related Pages:

        https://getbootstrap.com/docs/4.0/components/badge/

    Attributes:
    ----------
    :param text: The content of the badge
    :param icon: Optional, A String with the icon to display from font-awesome
    :param background_color: Optional, The background color of the badge
    :param color: Optional, The text color of the badge
    :param url:
    :param tooltip: Optional, The text to display in the tooltip
    :param options:
    :param profile: Optional, A boolean to store the performances for each components
    """
    if background_color is None:
      background_color = self.context.rptObj.theme.greys[0]
    if color is None:
      color = self.context.rptObj.theme.success[1]
    html_badge = html.HtmlImage.Badge(self.context.rptObj, text, width, height, None, icon, background_color, color, url,
                                      tooltip, options or {}, profile)
    return html_badge

  def date(self, value, label=None, icon="far fa-calendar-alt", color=None, width=(None, "px"), height=(None, "px"),
           htmlCode=None, profile=None, options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    Usage::

      rptObj.ui.fields.date('2020-04-08', label="Date").included_dates(["2020-04-08", "2019-09-06"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

      https://jqueryui.com/datepicker/

    Attributes:
    ----------
    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    dftl_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dftl_options.update(options)
    html_dt = html.HtmlDates.DatePicker(self.context.rptObj, value, label, icon, width, height, color, htmlCode, profile, dftl_options, helper)
    html_dt.input.style.css.width = 0
    return html_dt
