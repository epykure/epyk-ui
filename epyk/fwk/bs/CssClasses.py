

class Style:

  def __init__(self, component_cls):
    self.cls = component_cls

  def clearfix(self):
    """  
    Easily clear floats by adding .clearfix to the parent element. Can also be used as a mixin.

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/clearfix/
    """
    self.cls.add("clearfix")
    return self

  def link(self, category: str):
    """  
    You can use the .link-* classes to colorize links. Unlike the .text-* classes, these classes have a :hover
    and :focus state.

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/colored-links/

    :param category: The link CSS category
    """
    self.cls.add("link-%s" % category)
    return self

  def ratio(self, x: int, y: int):
    """  
    Aspect ratios can be customized with modifier classes. By default the following ratio classes are provided:

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/ratio/

    :param x:
    :param y:
    """
    self.cls.add("ratio")
    self.cls.add("ratio-%sx%s" % (x, y))
    return self

  def sticky(self, position, breakpoint: str = None):
    """  

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/position/

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
    return self

  def fixed(self, position, breakpoint: str = None):
    """  

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/position/

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

  def visually_hidden(self, focusable: bool = False):
    """  
    Use .visually-hidden-focusable to visually hide an element by default, but to display it when it’s focused.

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/visually-hidden/

    :param focusable: A boolean to activate the focusable property
    """
    if not focusable:
      self.cls.add("visually-hidden")
    else:
      self.cls.add("visually-hidden-focusable")

  def text_truncate(self):
    """  
    For longer content, you can add a .text-truncate class to truncate the text with an ellipsis.

    Related Pages:

      https://getbootstrap.com/docs/5.0/helpers/text-truncation/
    """
    self.cls.add("text-truncate")
    return self

  def font_size(self, n: int):
    """  
    Quickly change the font-size of text. While our heading classes (e.g., .h1–.h6) apply font-size, font-weight,
    and line-height, these utilities only apply font-size.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/text/

    :param n: The font-size number.
    """
    self.cls.add("fs-%s" % n)
    return self

  def text_break(self):
    """  
    Prevent long strings of text from breaking your components' layout by using .text-break to set word-wrap:
    break-word and word-break: break-word.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/text/
    """
    self.cls.add("text-break")
    return self

  def text(self, category: str):
    """  
    Colorize text with color utilities.
    If you want to colorize links, you can use the .link-* helper classes which have :hover and :focus states.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/colors/

    :param category:
    """
    self.cls.add("text-%s" % category)
    return self

  def border(self, category, position=None):
    """  
    Change the border color using utilities built on our theme colors.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/borders/

    :param category:
    :param position:
    """
    self.cls.add("bg-%s" % category)
    return self

  def bg(self, category):
    """  
    Similar to the contextual text color classes, set the background of an element to any contextual class.
    Background utilities do not set color, so in some cases you’ll want to use .text-* color utilities.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/background/

    :param category:
    """
    self.cls.add("bg-%s" % category)
    return self

  def shadow(self, kind: str = ""):
    """  
    While shadows on components are disabled by default in Bootstrap and can be enabled via $enable-shadows,
    you can also quickly add or remove a shadow with our box-shadow utility classes

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/shadows/

    :param kind: The CSS category
    """
    if kind is None:
      self.cls.add("shadow-none")
      return self

    if kind:
      self.cls.add("shadow-%s" % kind)
      return self

    self.cls.add("shadow")
    return self

  def float(self, position: str = None, breakpoint: str = None):
    """  
    These utility classes float an element to the left or right, or disable floating, based on the current viewport
    size using the CSS float property.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/float/

    :param position:
    :param breakpoint: Optional. Grid system category, with
      - xs (for phones - screens less than 768px wide)
      - sm (for tablets - screens equal to or greater than 768px wide)
      - md (for small laptops - screens equal to or greater than 992px wide)
      - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
    """
    if position is None:
      position = "none"
    if breakpoint is None:
      self.cls.add("float-%s" % position)
    else:
      self.cls.add("float-%s-%s" % (breakpoint, position))
    return self

  def user_select_all(self):
    """  
    Change the way in which the content is selected when the user interacts with it.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/interactions/
    """
    self.cls.add("user-select-all")
    return self

  def user_select_auto(self):
    """  
    Change the way in which the content is selected when the user interacts with it.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/interactions/
    """
    self.cls.add("user-select-auto")
    return self

  def user_select_none(self):
    """  
    Change the way in which the content is selected when the user interacts with it.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/interactions/
    """
    self.cls.add("user-select-none")
    return self

  def glutters(self, n: int, vertical: bool = False, horizontal: bool = True, breakpoint: str = None):
    """  
    Gutters are the gaps between column content, created by horizontal padding.
    We set padding-right and padding-left on each column, and use negative margin to offset that at the start and end
    of each row to align content.

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/gutters/

    :param n:
    :param vertical:
    :param horizontal:
    :param breakpoint: Optional. Grid system category, with
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
    return self

  def no_glutter(self):
    """  
    The gutters between columns in our predefined grid classes can be removed with .g-0

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/gutters/
    """
    self.cls.add("g-0")
    return self

  def order(self, val):
    """  
    Use .order- classes for controlling the visual order of your content.

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/columns/

    :param val:
    """
    self.cls.add("order-%s" % val)
    return self

  def offset(self, val, breakpoint: str = None):
    """  
    Move columns to the right using .offset-md-* classes.
    These classes increase the left margin of a column by * columns.
    For example, .offset-md-4 moves .col-md-4 over four columns.

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/columns/

    :param val:
    :param breakpoint: Optional. Grid system category, with
      - xs (for phones - screens less than 768px wide)
      - sm (for tablets - screens equal to or greater than 768px wide)
      - md (for small laptops - screens equal to or greater than 992px wide)
      - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
    """
    if breakpoint is not None:
      self.cls.add("offset-%s-%s" % (breakpoint, val))
    else:
      self.cls.add("offset-%s" % val)
    return self

  def margin(self, val, breakpoint: str = None):
    """  
    With the move to flexbox in v4, you can use margin utilities like .me-auto to force sibling columns away from
    one another.

    Related Pages:

      https://getbootstrap.com/docs/5.0/layout/columns/

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
    return self

  def width(self, percent, from_viewport: bool = False):
    """  

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/sizing/

    :param percent:
    :param from_viewport:
    """
    if from_viewport:
      self.cls.add("vw-%s" % percent)
    else:
      self.cls.add("w-%s" % percent)
    return self

  def height(self, percent, from_viewport: bool = False):
    """  

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/sizing/

    :param percent:
    :param from_viewport:
    """
    if from_viewport:
      self.cls.add("vh-%s" % percent)
    else:
      self.cls.add("h-%s" % percent)
    return self

  def visible(self):
    """  
    Set the visibility of elements with our visibility utilities.
    These utility classes do not modify the display value at all and do not affect layout – .invisible elements still
    take up space in the page.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/visibility/
    """
    self.cls.add("visible")
    return self

  def invisible(self):
    """  
    Set the visibility of elements with our visibility utilities.
    These utility classes do not modify the display value at all and do not affect layout – .invisible elements still
    take up space in the page.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/visibility/
    """
    self.cls.add("invisible")
    return self

  def sizing(self, breakpoint: str):
    """  
    Set the size of the component.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/buttons/

    :param breakpoint: Optional. Grid system category, with
      - xs (for phones - screens less than 768px wide)
      - sm (for tablets - screens equal to or greater than 768px wide)
      - md (for small laptops - screens equal to or greater than 992px wide)
      - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
    """
    self.cls.add("%s-%s" % (self.cls[0], breakpoint))
    return self

  def justify_content(self, position: str):
    """  
    Align component content (start, center, end)

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/navs-tabs/#horizontal-alignment

    :param position: The position.
    """
    self.cls.add("justify-content-%s" % position)
    return self
