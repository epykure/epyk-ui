

class Style:

  def __init__(self, component_cls):
    self.cls = component_cls

  def clearfix(self):
    """
    Description:
    ------------
    Easily clear floats by adding .clearfix to the parent element. Can also be used as a mixin.

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/clearfix/
    """
    self.cls.add("clearfix")

  def link(self, category):
    """
    Description:
    ------------
    You can use the .link-* classes to colorize links. Unlike the .text-* classes, these classes have a :hover
    and :focus state.

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/colored-links/

    Attributes:
    ----------
    :param category:
    """
    self.cls.add("link-%s" % category)

  def ratio(self, x, y):
    """
    Description:
    ------------
    Aspect ratios can be customized with modifier classes. By default the following ratio classes are provided:

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/ratio/

    Attributes:
    ----------
    :param x:
    :param y:
    """
    self.cls.add("ratio")
    self.cls.add("ratio-%sx%s" % (x, y))

  def sticky(self, position, breakpoint=None):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/position/

    Attributes:
    ----------
    :param position:
    :param breakpoint: String. Optional. Grid system category, with
      - xs (for phones - screens less than 768px wide)
      - sm (for tablets - screens equal to or greater than 768px wide)
      - md (for small laptops - screens equal to or greater than 992px wide)
      - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
    """
    if breakpoint is not None:
      self.cls.add("sticky-%s-%s" % (breakpoint, position))
    else:
      self.cls.add("sticky-%s" % position)

  def fixed(self, position, breakpoint=None):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/position/

    Attributes:
    ----------
    :param position:
    :param breakpoint: String. Optional. Grid system category, with
      - xs (for phones - screens less than 768px wide)
      - sm (for tablets - screens equal to or greater than 768px wide)
      - md (for small laptops - screens equal to or greater than 992px wide)
      - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
    """
    if breakpoint is not None:
      self.cls.add("fixed-%s-%s" % (breakpoint, position))
    else:
      self.cls.add("fixed-%s" % position)

  def visually_hidden(self, focusable=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/visually-hidden/

    Attributes:
    ----------
    :param focusable:
    """
    if not focusable:
      self.cls.add("visually-hidden")
    else:
      self.cls.add("visually-hidden-focusable")

  def text_truncate(self):
    """
    Description:
    ------------
    For longer content, you can add a .text-truncate class to truncate the text with an ellipsis.

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/text-truncation/
    """
    self.cls.add("text-truncate")

  def font_size(self, n):
    """
    Description:
    ------------
    Quickly change the font-size of text. While our heading classes (e.g., .h1–.h6) apply font-size, font-weight,
    and line-height, these utilities only apply font-size.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/text/

    Attributes:
    ----------
    :param n:
    """
    self.cls.add("fs-%s" % n)

  def text_break(self):
    """
    Description:
    ------------
    Prevent long strings of text from breaking your components' layout by using .text-break to set word-wrap:
    break-word and word-break: break-word

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/text/
    """
    self.cls.add("text-break")

  def text(self, category):
    """
    Description:
    ------------
    Colorize text with color utilities.
    If you want to colorize links, you can use the .link-* helper classes which have :hover and :focus states.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/colors/

    Attributes:
    ----------
    :param category:
    """
    self.cls.add("text-%s" % category)

  def border(self, category, position=None):
    """
    Description:
    ------------
    Change the border color using utilities built on our theme colors.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/borders/

    Attributes:
    ----------
    :param category:
    :param position:
    """
    self.cls.add("bg-%s" % category)

  def bg(self, category):
    """
    Description:
    ------------
    Similar to the contextual text color classes, set the background of an element to any contextual class.
    Background utilities do not set color, so in some cases you’ll want to use .text-* color utilities.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/background/

    Attributes:
    ----------
    :param category:
    """
    self.cls.add("bg-%s" % category)

  def shadow(self, kind=None):
    """
    Description:
    ------------
    While shadows on components are disabled by default in Bootstrap and can be enabled via $enable-shadows,
    you can also quickly add or remove a shadow with our box-shadow utility classes

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/shadows/

    Attributes:
    ----------
    :param kind:
    """
    if kind is None:
      return

    if kind not in ("sm", "lg", "inset"):
      pass

  def float(self, position):
    """
    Description:
    ------------
    These utility classes float an element to the left or right, or disable floating, based on the current viewport
    size using the CSS float property.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/float/

    :param position:
    """

  def user_select_all(self):
    """
    Description:
    ------------
    Change the way in which the content is selected when the user interacts with it.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/interactions/
    """
    self.cls.add("user-select-all")

  def user_select_auto(self):
    """
    Description:
    ------------
    Change the way in which the content is selected when the user interacts with it.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/interactions/
    """
    self.cls.add("user-select-auto")

  def user_select_none(self):
    """
    Description:
    ------------
    Change the way in which the content is selected when the user interacts with it.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/interactions/
    """
    self.cls.add("user-select-none")

  def glutters(self, n, vertical=False, horizontal=True, breakpoint=None):
    """
    Description:
    ------------
    Gutters are the gaps between column content, created by horizontal padding.
    We set padding-right and padding-left on each column, and use negative margin to offset that at the start and end
    of each row to align content.

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/gutters/

    Attributes:
    ----------
    :param n:
    :param vertical:
    :param horizontal:
    :param breakpoint: String. Optional. Grid system category, with
      - xs (for phones - screens less than 768px wide)
      - sm (for tablets - screens equal to or greater than 768px wide)
      - md (for small laptops - screens equal to or greater than 992px wide)
      - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
    """
    pos = ""
    if horizontal:
      pos = "x"
      if vertical:
        pos = ""
    elif vertical:
      pos = "y"
    if breakpoint is not None:
      self.cls.add("g%s-%s-%s" % (pos, breakpoint, n))
    else:
      self.cls.add("g%s-%s" % (pos, n))

  def no_glutter(self):
    """
    Description:
    ------------
    The gutters between columns in our predefined grid classes can be removed with .g-0

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/gutters/
    """
    self.cls.add("g-0")

  def order(self, val):
    """
    Description:
    ------------
    Use .order- classes for controlling the visual order of your content.

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/columns/

    Attributes:
    ----------
    :param val:
    """
    self.cls.add("order-%s" % val)

  def offset(self, val, breakpoint=None):
    """
    Description:
    ------------
    Move columns to the right using .offset-md-* classes.
    These classes increase the left margin of a column by * columns.
    For example, .offset-md-4 moves .col-md-4 over four columns.

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/columns/

    Attributes:
    ----------
    :param val:
    :param breakpoint: String. Optional. Grid system category, with
      - xs (for phones - screens less than 768px wide)
      - sm (for tablets - screens equal to or greater than 768px wide)
      - md (for small laptops - screens equal to or greater than 992px wide)
      - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
    """
    if breakpoint is not None:
      self.cls.add("offset-%s-%s" % (breakpoint, val))
    else:
      self.cls.add("offset-%s" % val)

  def margin(self, val, breakpoint=None):
    """
    Description:
    ------------
    With the move to flexbox in v4, you can use margin utilities like .me-auto to force sibling columns away from
    one another.

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/columns/

    Attributes:
    ----------
    :param val:
    :param breakpoint: String. Optional. Grid system category, with
      - xs (for phones - screens less than 768px wide)
      - sm (for tablets - screens equal to or greater than 768px wide)
      - md (for small laptops - screens equal to or greater than 992px wide)
      - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
    """
    if breakpoint is not None:
      self.cls.add("ms-%s-%s" % (breakpoint, val))
    else:
      self.cls.add("ms-%s" % val)

  def width(self, percent, from_viewport=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/sizing/

    Attributes:
    ----------
    :param percent:
    :param from_viewport:
    """
    if from_viewport:
      self.cls.add("vw-%s" % percent)
    else:
      self.cls.add("w-%s" % percent)

  def height(self, percent, from_viewport=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/sizing/

    Attributes:
    ----------
    :param percent:
    :param from_viewport:
    """
    if from_viewport:
      self.cls.add("vh-%s" % percent)
    else:
      self.cls.add("h-%s" % percent)

  def visible(self):
    """
    Description:
    ------------
    Set the visibility of elements with our visibility utilities.
    These utility classes do not modify the display value at all and do not affect layout – .invisible elements still
    take up space in the page.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/visibility/
    """
    self.cls.add("visible")

  def invisible(self):
    """
    Description:
    ------------
    Set the visibility of elements with our visibility utilities.
    These utility classes do not modify the display value at all and do not affect layout – .invisible elements still
    take up space in the page.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/visibility/
    """
    self.cls.add("invisible")
