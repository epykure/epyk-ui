
from epyk.core.css import Colors
from epyk.interfaces import Arguments


class ClsConfigs:

  def __init__(self, component):
    self.component = component

  def margins(self, h=(10, '%'), v=(0, 'px')):
    """
    Description:
    ------------
    Add a vertical and horizontal margin to the underlying template added to the body component.

    Usage:
    -----

      page = pk.Page()
      page.body.template.style.configs.margins(h=5)
      page.body.template.style.css.background = "white"

    Attributes:
    ----------
    :param h: Tuple. optional. The horizontal (left and right) margin.
    :param v: Tuple. optional. The vertical (top, bottom) margin.
    """
    h = Arguments.size(h, unit="%")
    v = Arguments.size(v, unit="px")
    self.component.style.css.margin = "%s%s %s%s" % (v[0], v[1], h[0], h[1])

  def box(self, hexa_color=None, opacity=0.6, size=5, margin=5):
    """
    Description:
    ------------
    Add a box shadow layout to the component.

    Usage:
    -----


    Attributes:
    ----------
    :param hexa_color: String. Optional. The color code in hexadecimal format.
    :param opacity: Float. Optional. The opacity value between 0 and 1.
    :param size: Integer. Optional. The border size.
    :param margin: Integer. Optional. The left and right margin in pixel.
    """
    self.component.style.css.background_color = "white"
    if self.component.style.css.padding is None:
      self.component.style.css.padding = 5
    self.component.style.css.width = "calc(100%% - %spx)" % (2*margin)
    self.component.style.css.margin = margin
    rgb = Colors.getHexToRgb(self.component.page.theme.greys[5] if hexa_color is None else hexa_color)
    self.component.style.css.box_shadow = "0 0 %(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
      "r": rgb[0], "g": rgb[1], "b": rgb[2], 'opac': opacity, 'size': size}

  def parallax(self, url):
    """
    Description:
    -----------
    Parallax scrolling is a web site trend where the background content (i.e. an image) is moved at a different
    speed than the foreground content while scrolling.

    Usage:
    -----

      div = page.ui.div()
      div.style.css.parallax("https://www.w3schools.com/howto/img_parallax.jpg")

    Related Pages:

      https://www.w3schools.com/howto/howto_css_parallax.asp

    Attributes:
    ----------
    :param url: String. The path of the picture visible in the background.
    """
    self.component.style.css.background_image = 'url("%s")' % url
    self.component.style.css.background_attachment = "fixed"
    self.component.style.css.background_position = "center"
    self.component.style.css.background_repeat = "no-repeat"
    self.component.style.css.background_size = "cover"
    return self

  def shadow(self, hexa_color=None, opacity=0.5, size=10, position=None, radius=10):
    """
    Description:
    ------------
    Set the box shadow color.

    Usage:
    -----



    Related Pages:

      https://www.w3schools.com/css/css3_shadows.asp
      https://gist.github.com/ocean90/1268328

    Attributes:
    ----------
    :param hexa_color: String. Optional. An hexadecimal color code.
    :param opacity: Integer. Optional. The shadow opacity. Default 0.5.
    :param size: Integer. Optional. The size of the shadow effect.
    :param position: String. Optional. The position for the shadow.
    :param radius: Integer. Optional. The size for the angle rounding.

    :return: The CSS object to allow the functions chaining.
    """
    rgb = Colors.getHexToRgb(self.component.page.theme.greys[-1] if hexa_color is None else hexa_color)
    if position == 'right':
      self.component.style.css.box_shadow = "%(size)spx 0 %(size)spx -%(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
        "r": rgb[0], "g": rgb[1], "b": rgb[2], 'opac': opacity, 'size': size}
    elif position == 'left':
      self.component.style.css.box_shadow = "-%(size)spx 0 5px -%(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
        "r": rgb[0], "g": rgb[1], "b": rgb[2], 'opac': opacity, 'size': size}
    else:
      self.component.style.css.box_shadow = "0 0 %(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
        "r": rgb[0], "g": rgb[1], "b": rgb[2], 'opac': opacity, 'size': size}
    self.component.style.css.border_radius = radius
    return self

  def rounded_icons(self, padding=8):
    """
    Description:
    ------------
    Add rounded border to the component.

    Usage:
    -----


    Attributes:
    ----------
    :param padding: Integer. Optional. The padding (top, right, bottom and left) in pixel.
    """
    self.component.style.add_classes.div.border_hover()
    self.component.style.css.border_radius = self.component.page.body.style.globals.font.size
    self.component.style.css.padding = padding

  def doc(self, percent=5, max_width=650, padding=True, background=None):
    """
    Description:
    ------------

    TODO: Find way to set the container to the middle of the page.

    Usage:
    -----

    Attributes:
    ----------
    :param percent: Integer. Optional. The percentage of space on the left and right.
    :param max_width: Integer. Optional. The max size of the page in pixel.
    :param padding: Boolean. Optional. The top and bottom padding in the doc.
    :param background: String. Optional. The background color.
    """
    self.component.style.css.max_width = max_width
    self.component.style.css.min_height = 150
    if padding:
      self.component.style.css.padding = "20px 10px"
    self.component.style.configs.shadow(radius=0)
    if background is not None:
      self.component.style.css.background = background
    self.component.style.css.margin = "20px auto"
    self.component.page.body.style.css.padding_bottom = 5
    self.component.page.body.style.css.padding_left = "%s%%" % percent
    self.component.page.body.style.css.padding_right = "%s%%" % percent
    self.component.page.body.style.css.background = self.component.page.theme.greys[2]
