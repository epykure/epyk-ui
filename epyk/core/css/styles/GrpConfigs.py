
from epyk.core.py import primitives
from epyk.core.css import Colors
from epyk.interfaces import Arguments


class ClsConfigs:

  def __init__(self, component: primitives.HtmlModel):
    self.component = component
    self.page = component.page

  def margins(self, h: tuple = (10, '%'), v: tuple = (0, 'px')):
    """
    Description:
    ------------
    Add a vertical and horizontal margin to the underlying template added to the body component.

    Usage::

      page = pk.Page()
      page.body.template.style.configs.margins(h=5)
      page.body.template.style.css.background = "white"

    Attributes:
    ----------
    :param tuple h: Optional. The horizontal (left and right) margin.
    :param tuple v: Optional. The vertical (top, bottom) margin.
    """
    h = Arguments.size(h, unit="%")
    v = Arguments.size(v, unit="px")
    self.component.style.css.margin = "%s%s %s%s" % (v[0], v[1], h[0], h[1])
    return self

  def box(self, hexa_color: str = None, opacity: float = 0.6, size: int = 5, margin_v: tuple = (10, 'px'),
          margin_h: tuple = (10, 'px'), background: str = "white"):
    """
    Description:
    ------------
    Add a box shadow layout to the component.

    Usage::

        page = pk.Page()
        page.body.template.style.configs.box()

    Attributes:
    ----------
    :param str hexa_color: Optional. The color code in hexadecimal format.
    :param float opacity: Optional. The opacity value between 0 and 1.
    :param int size: Optional. The border size.
    :param int margin_h: Optional. The left and right margin in pixel.
    :param int margin_v: Optional. The top and bottom margin in pixel.
    :param str background: Optional. The background color.
    """
    if self.component.style.css.padding is None:
      self.component.style.css.padding = 5
    self.component.style.css.width = "calc(100%% - %s%s)" % (2*margin_h[0], margin_h[1])
    self.component.style.css.margin_v = "%s%s" % (margin_v[0], margin_v[1])
    self.component.style.css.margin_h = "%s%s" % (margin_h[0], margin_h[1])
    if background is not None:
      self.component.style.css.background = background
    rgb = Colors.getHexToRgb(self.component.page.theme.greys[5] if hexa_color is None else hexa_color)
    self.component.style.css.box_shadow = "0 0 %(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
      "r": rgb[0], "g": rgb[1], "b": rgb[2], 'opac': opacity, 'size': size}
    return self

  def parallax(self, url: str):
    """
    Description:
    -----------
    Parallax scrolling is a website trend where the background content (i.e. an image) is moved at a different
    speed than the foreground content while scrolling.

    Usage::

      div = page.ui.div()
      div.style.css.parallax("https://www.w3schools.com/howto/img_parallax.jpg")

    Related Pages:

      https://www.w3schools.com/howto/howto_css_parallax.asp

    Attributes:
    ----------
    :param str url: The path of the picture visible in the background.
    """
    self.component.style.css.background_image = 'url("%s")' % url
    self.component.style.css.background_attachment = "fixed"
    self.component.style.css.background_position = "center"
    self.component.style.css.background_repeat = "no-repeat"
    self.component.style.css.background_size = "cover"
    return self

  def shadow(self, hexa_color: str = None, opacity: float = 0.5, size: int = 10, position: str = None,
             radius: int = 10):
    """
    Description:
    ------------
    Set the box shadow color.

    Related Pages:

      https://www.w3schools.com/css/css3_shadows.asp
      https://gist.github.com/ocean90/1268328

    Attributes:
    ----------
    :param str hexa_color: Optional. A hexadecimal color code.
    :param str opacity: Optional. The shadow opacity. Default 0.5.
    :param int size: Optional. The size of the shadow effect.
    :param str position: Optional. The position for the shadow.
    :param int radius: Optional. The size for the angle rounding.

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

  def rounded_icons(self, padding: int = 8):
    """
    Description:
    ------------
    Add rounded border to the component.

    Attributes:
    ----------
    :param int padding: Optional. The padding (top, right, bottom and left) in pixel.
    """
    self.component.style.add_classes.div.border_hover()
    self.component.style.css.border_radius = self.component.page.body.style.globals.font.size
    self.component.style.css.padding = padding
    return self

  def doc(self, percent: int = 5, max_width: int = 650, padding: bool = True, background: str = None,
          header: str = None, header_path: str = "/static", top: int = 60):
    """
    Description:
    ------------

    TODO: Find way to set the container to the middle of the page.

    Usage::

       page = pk.Page()
       page.body.template.style.configs.doc(background="white")

    Attributes:
    ----------
    :param int percent: Optional. The percentage of space on the left and right.
    :param int max_width: Optional. The max size of the page in pixel.
    :param bool padding: Optional. The top and bottom padding in the doc.
    :param str background: Optional. The background color.
    :param str header: Optional. The header picture.
    :param str header_path: Optional. The header path.
    :param int top: Optional. The body top position in the page.
    """
    if header is not None:
      self.component.page.body.header.add(self.component.page.ui.img(header, path=header_path))
      self.component.page.body.header.style.css.left = 0
      self.component.page.body.header.style.css.right = 0
      self.component.page.body.header.style.css.top = 0
      self.component.page.body.header.style.css.z_index = -1
      self.component.page.body.header.style.css.position = "absolute"
    self.component.style.css.max_width = max_width
    self.component.style.css.min_height = 150
    if padding:
      self.component.style.css.padding = "20px 10px"
    self.component.style.configs.shadow(radius=0)
    if background is not None:
      self.component.style.css.background = background
    self.component.style.css.margin = "20px auto"
    self.component.page.body.style.css.margin_top = top
    self.component.page.body.style.css.padding_bottom = 5
    self.component.page.body.style.css.padding_left = "%s%%" % percent
    self.component.page.body.style.css.padding_right = "%s%%" % percent
    self.component.page.body.style.css.background = self.component.page.theme.greys[2]
    return self
