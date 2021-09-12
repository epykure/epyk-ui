
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
