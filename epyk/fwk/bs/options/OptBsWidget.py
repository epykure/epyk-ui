import json

from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class Carousel(Options):

  @property
  def interval(self):
    """
    Description:
    -----------
    The amount of time to delay between automatically cycling an item. If false, carousel will not automatically cycle.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/carousel/#options
    """
    return self._config_get(5000)

  @interval.setter
  def interval(self, num):
    self._config(num)

  @property
  def keyboard(self):
    """
    Description:
    -----------
    Whether the carousel should react to keyboard events.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/carousel/#options
    """
    return self._config_get(True)

  @keyboard.setter
  def keyboard(self, flag):
    self._config(flag)

  @property
  def pause(self):
    """
    Description:
    -----------
    If set to 'hover', pauses the cycling of the carousel on mouseenter and resumes the cycling of the carousel on
    mouseleave. If set to false, hovering over the carousel won't pause it..

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/carousel/#options
    """
    return self._config_get("hover")

  @pause.setter
  def pause(self, value):
    self._config(value)

  @property
  def ride(self):
    """
    Description:
    -----------
    Autoplays the carousel after the user manually cycles the first item. If set to 'carousel',
    autoplays the carousel on load.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/carousel/#options
    """
    return self._config_get(False)

  @ride.setter
  def ride(self, flag):
    self._config(flag)

  @property
  def wrap(self):
    """
    Description:
    -----------
    Whether the carousel should cycle continuously or have hard stops.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/carousel/#options
    """
    return self._config_get(True)

  @wrap.setter
  def wrap(self, flag):
    self._config(flag)

  @property
  def touch(self):
    """
    Description:
    -----------
    Whether the carousel should support left/right swipe interactions on touchscreen devices..

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/carousel/#options
    """
    return self._config_get(True)

  @touch.setter
  def touch(self, flag):
    self._config(flag)


class OffCanvas(Options):

  @property
  def show(self):
    """
    Description:
    -----------

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/
    """
    return self._config_get(False)

  @show.setter
  def show(self, flag):
    if flag:
      self.component.attr["class"].add("show")
    self._config(flag)

  @property
  def backdrop(self):
    """
    Description:
    -----------
    Apply a backdrop on body while offcanvas is open.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/
    """
    return self.component.attr.get("data-bs-backdrop")

  @backdrop.setter
  def backdrop(self, flag):
    self.component.attr["data-bs-backdrop"] = json.dumps(flag)

  @property
  def scroll(self):
    """
    Description:
    -----------
    Allow body scrolling while offcanvas is open.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/
    """
    return self.component.attr.get("data-bs-scroll")

  @scroll.setter
  def scroll(self, flag):
    self.component.attr["data-bs-scroll"] = json.dumps(flag)

  @property
  def keyboard(self):
    """
    Description:
    -----------
    Closes the offcanvas when escape key is pressed.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/
    """
    return self.component.attr.get("data-bs-keyboard")

  @keyboard.setter
  def keyboard(self, flag):
    self.component.attr["data-bs-keyboard"] = json.dumps(flag)


class Modal(Options):

  @property
  def fade(self):
    """
    Description:
    -----------

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/
    """
    return self._config_get(False)

  @fade.setter
  def fade(self, flag):
    if flag:
      self.component.attr["class"].add("fade")
      self.component.attr["aria-hidden"] = True
    self._config(flag)

  @property
  def focus(self):
    """
    Description:
    -----------
    Puts the focus on the modal when initialized.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/
    """
    return self.component.attr.get("data-bs-focus")

  @focus.setter
  def focus(self, flag):
    self.component.attr["data-bs-focus"] = json.dumps(flag)

  @property
  def keyboard(self):
    """
    Description:
    -----------
    Closes the modal when escape key is pressed.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/
    """
    return self.component.attr.get("data-bs-keyboard")

  @keyboard.setter
  def keyboard(self, flag):
    self.component.attr["data-bs-keyboard"] = json.dumps(flag)

  @property
  def backdrop(self):
    """
    Description:
    -----------
    Includes a modal-backdrop element. Alternatively, specify static for a backdrop which doesn't close the modal
    on click.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/#options
    """
    return self.component.attr.get("data-bs-backdrop")

  @backdrop.setter
  def backdrop(self, flag):
    self.component.attr["data-bs-backdrop"] = json.dumps(flag)

  @property
  def scroll(self):
    """
    Description:
    -----------
    Allow the scrolling for long content.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/#scrolling-long-content
    """
    return self._config_get(False)

  @scroll.setter
  def scroll(self, flag):
    if flag:
      self.component.attr["class"].add("modal-dialog-scrollable")
    self._config(flag)

  @property
  def centered(self):
    """
    Description:
    -----------
    Vertically center the modal.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/
    """
    return self._config_get(False)

  @centered.setter
  def centered(self, flag):
    if flag:
      self.component.attr["class"].add("modal-dialog-centered")
    self._config(flag)

  def size(self, breakpoint):
    """
    Description:
    -----------
    Set the size for the modal.

    Attributes:
    ----------
    :param breakpoint: String. The alias for the bootstrap breakpoint.
    """
    self.component.attr["class"].add("modal-%s" % breakpoint)

  def full_screen(self, breakpoint):
    """
    Description:
    -----------
    Set the size for the modal in full screen mode.

    Attributes:
    ----------
    :param breakpoint: String. The alias for the bootstrap breakpoint.
    """
    self.component.attr["class"].add("modal-fullscreen-%s-down" % breakpoint)


class Toast(Options):

  @property
  def show(self):
    """
    Description:
    -----------

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/toasts/
    """
    return self._config_get(False)

  @show.setter
  def show(self, flag):
    if flag:
      self.component.attr["class"].add("show")
    self._config(flag)

  @property
  def hide(self):
    """
    Description:
    -----------

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/toasts/
    """
    return self._config_get(False)

  @hide.setter
  def hide(self, flag):
    if flag:
      self.component.attr["class"].add("hide")
    self._config(flag)
