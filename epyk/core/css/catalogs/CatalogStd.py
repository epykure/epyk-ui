
import logging


class CatalogStd:

  # spacing rules from bootstrap
  spaces = {0: "0", 1: "0.25", 2: "0.5", 3: "1", 4: "1.25", 5: "3"}
  alias = {
    "padding": 'p', "padding-left": 'pl', "padding-right": 'pr',
    "margin": 'm', "margin-left": 'ml', "margin-right": 'mr',
  }

  def __init__(self, page, class_lists):
    self._page = page
    self.class_lists = class_lists

  def _add_class(self, name, n):
    """   Create the CSS class and add it to the page object.
    This function is an internal one used by the other functions in this module.

    Usage::

    :param name: String. The CSS attribute.
    :param n: Integer. The number of spaces.
    """
    if "bootstrap" not in self._page.imports.requirements or n > 5:
      if n not in self.spaces:
        self.spaces[n] = 3 * (2^(n-6))
      self._page.css.customText('.%s-%s {%s: %srem !important;}' % (self.alias[name], n, name, self.spaces[n]))

  def margin(self, n):
    """   Add a CSS margin to the component.

    Related Pages:

      https://getbootstrap.com/docs/4.0/utilities/spacing/
      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

      t1 = page.ui.title("Templates structure")
      t1.style.add_classes.std.margin(7)

    :param n: Integer. The number of spaces to add.
    """
    self._add_class("margin", n)
    self.class_lists["main"].add("m-%s" % n)

  def margin_r(self, n):
    """   Add a CSS class for the CSS margin-right CSS attribute to the component.

    Usage::

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/spacing/

    :param n: Integer. The number of spaces.
    """
    self._add_class("margin-right", n)
    self.class_lists["main"].add("mr-%s" % n)

  def margin_l(self, n):
    """   Add a CSS class for the CSS margin-left CSS attribute to the component.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param n: Integer. The number of spaces.
    """
    self._add_class("margin-left", n)
    self.class_lists["main"].add("ml-%s" % n)

  def margin_x(self, n):
    """   Add a CSS class for the CSS margin-right and CSS margin-left CSS attributes to the component.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param n: Integer. The number of spaces.
    """
    self._add_class("margin-left", n)
    self._add_class("margin-right", n)
    self.class_lists["main"].add("mx-%s" % n)

  def margin_lr(self, n):
    """   Add a CSS class for the CSS margin-right and CSS margin-left CSS attributes to the component.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param n: Integer. The number of spaces.
    """
    self.margin_x(n)

  def margin_center(self, verbose=True):
    """   Add a CSS class to the component to center it using margin auto attribute.

    Related Pages:

      https://getbootstrap.com/docs/4.0/utilities/spacing/
      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param verbose: Boolean. Optional. Display a log message.
    """
    if verbose and "bootstrap" not in self._page.imports.requirements:
      # TODO replicate the logic
      logging.warning("Boostrap must be in the requirement to use this class")

    self.class_lists["main"].add("mx-auto")

  def padding(self, n):
    """   Add a CSS class for the CSS padding CSS attribute to the component.

    Related Pages:

      https://getbootstrap.com/docs/4.0/utilities/spacing/
      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param n: Integer. The number of spaces.
    """
    self._add_class("padding", n)
    self.class_lists["main"].add("p-%s" % n)

  def padding_r(self, n):
    """   Add a CSS class for the CSS padding-right CSS attribute to the component.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param n: Integer. The number of spaces.
    """
    self._add_class("padding-right", n)
    self.class_lists["main"].add("pr-%s" % n)

  def padding_l(self, n):
    """   Add a CSS class for the CSS padding-left CSS attribute to the component.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param n: Integer. The number of spaces.
    """
    self._add_class("padding-left", n)
    self.class_lists["main"].add("pl-%s" % n)

  def padding_x(self, n):
    """   Add a CSS class for the CSS padding-right and CSS padding-left CSS attributes to the component.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param n: Integer. The number of spaces.
    """
    self._add_class("padding-left", n)
    self._add_class("padding-right", n)
    self.class_lists["main"].add("px-%s" % n)

  def padding_lr(self, n):
    """   Add a CSS class for the CSS padding-right and CSS padding-left CSS attributes to the component.

    Related Pages:

      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param n: Integer. The number of spaces.
    """
    self.padding_x(n)

  def padding_center(self, verbose=True):
    """   Add a CSS class to the component to center it using padding auto attribute.

    Related Pages:

      https://getbootstrap.com/docs/4.0/utilities/spacing/
      https://getbootstrap.com/docs/5.0/utilities/spacing/

    Usage::

    :param verbose: Boolean. Optional. Display a log message.
    """
    if verbose and "bootstrap" not in self._page.imports.requirements:
      # TODO replicate the logic
      logging.warning("Boostrap must be in the requirement to use this class")

    self.class_lists["main"].add("px-auto")
