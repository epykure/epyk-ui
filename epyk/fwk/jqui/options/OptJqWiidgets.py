
from epyk.core.html.options import Options
from epyk.core.html.options import Enums
from epyk.core.js import JsUtils


class EnumHeightStyles(Enums):

  def auto(self):
    """
    Description:
    ------------
    All panels will be set to the height of the tallest panel.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    self._set_value()

  def fill(self):
    """
    Description:
    ------------
    Expand to the available height based on the accordion's parent height.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    self._set_value()

  def content(self):
    """
    Description:
    ------------
    Each panel will be only as tall as its content.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    self._set_value()


class OptAccordion(Options):

  @property
  def active(self):
    """
    Description:
    -----------
    Which panel is currently open.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return self._config_get()

  @active.setter
  def active(self, num):
    self._config(num)

  @property
  def animate(self):
    """
    Description:
    -----------
    If and how to animate changing panels.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return self._config_get()

  @animate.setter
  def animate(self, num):
    self._config(num)

  @property
  def classes(self):
    """
    Description:
    -----------
    Specify additional classes to add to the widget's elements.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return self._config_get()

  @classes.setter
  def classes(self, values):
    self._config(values)

  @property
  def collapsible(self):
    """
    Description:
    -----------
    Whether all the sections can be closed at once. Allows collapsing the active section.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return self._config_get()

  @collapsible.setter
  def collapsible(self, flag):
    self._config(flag)

  @property
  def disabled(self):
    """
    Description:
    -----------
    Disables the accordion if set to true.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return self._config_get()

  @disabled.setter
  def disabled(self, flag):
    self._config(flag)

  @property
  def event(self):
    """
    Description:
    -----------
    The type of event that the tabs should react to in order to activate the tab. To activate on hover, use "mouseover".

    Usage::

        acc = page.web.jqui.accordion({"title": "paragraph"})
        acc.add_section("Test", page.ui.div(page.ui.text("oNew content")))
        acc.options.event = "mouseover"

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return self._config_get("click")

  @event.setter
  def event(self, indices):
    self._config(indices)

  @property
  def header(self):
    """
    Description:
    -----------
    Data identifying the header element.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return self._config_get("h3")

  @header.setter
  def header(self, text):
    self._config(text)

  @property
  def heightStyle(self):
    """
    Description:
    -----------
    Controls the height of the accordion and each panel.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return self._config_get("auto")

  @heightStyle.setter
  def heightStyle(self, text):
    self._config(text)

  @property
  def heightStyles(self):
    return EnumHeightStyles(self, "heightStyle")

  @property
  def icons(self):
    """
    Description:
    -----------
    Icons to use for headers, matching an icon provided by the jQuery UI CSS Framework.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return self._config_get()

  @icons.setter
  def icons(self, values):
    self._config(values)

  def activate(self, js_funcs, profile):
    """
    Description:
    ------------
    Triggered after a panel has been activated (after animation completes). If the accordion was previously collapsed,

    Related Pages:

      https://api.jqueryui.com/accordion/

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True)

  def beforeActivate(self, js_funcs, profile):
    """
    Description:
    ------------
    Triggered directly before a panel is activated. Can be canceled to prevent the panel from activating.

    Related Pages:

      https://api.jqueryui.com/accordion/

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True)

  def create(self, js_funcs, profile):
    """
    Description:
    ------------
    Triggered directly before a panel is activated. Can be canceled to prevent the panel from activating.

    Related Pages:

      https://api.jqueryui.com/accordion/

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True)


class OptTabs(Options):

  @property
  def active(self):
    """
    Description:
    -----------
    Which panel is currently open.

    Related Pages:

      https://api.jqueryui.com/tabs/
    """
    return self._config_get()

  @active.setter
  def active(self, num):
    self._config(num)

  @property
  def classes(self):
    """
    Description:
    -----------
    Specify additional classes to add to the widget's elements.
    Any of classes specified in the Theming section can be used as keys to override their value.

    Related Pages:

      https://api.jqueryui.com/tabs/
    """
    return self._config_get()

  @classes.setter
  def classes(self, values):
    self._config(values)

  @property
  def collapsible(self):
    """
    Description:
    -----------
    When set to true, the active panel can be closed.

    Related Pages:

      https://api.jqueryui.com/tabs/
    """
    return self._config_get()

  @collapsible.setter
  def collapsible(self, flag):
    self._config(flag)

  @property
  def disabled(self):
    """
    Description:
    -----------
    Which tabs are disabled.

    Related Pages:

      https://api.jqueryui.com/tabs/
    """
    return self._config_get()

  @disabled.setter
  def disabled(self, indices):
    self._config(indices)

  @property
  def event(self):
    """
    Description:
    -----------
    The type of event that the tabs should react to in order to activate the tab. To activate on hover, use "mouseover".

    Usage::

        acc = page.web.jqui.tabs({"title": "paragraph"})
        acc.add_panel("Test", page.ui.div(page.ui.text("oNew content")))
        acc.options.event = "mouseover"

    Related Pages:

      https://api.jqueryui.com/tabs/
    """
    return self._config_get("click")

  @event .setter
  def event(self, indices):
    self._config(indices)

  @property
  def heightStyle(self):
    """
    Description:
    -----------
    Controls the height of the tabs widget and each panel. Possible values:
      "auto": All panels will be set to the height of the tallest panel.
      "fill": Expand to the available height based on the tabs' parent height.
      "content": Each panel will be only as tall as its content.

    Related Pages:

      https://api.jqueryui.com/tabs/
    """
    return self._config_get()

  @heightStyle.setter
  def heightStyle(self, text):
    self._config(text)

  def hide(self, effect, duration=1000):
    """
    Description:
    -----------
    If and how to animate the hiding of the panel.

    Related Pages:

      https://api.jqueryui.com/tabs/

    Usage::

        acc.options.hide("explode")

    Attributes:
    ----------
    :param effect: String.
    :param duration: Number. Optional.  The panel will fade out with the specified duration and the default easing.
    """
    self._config({"effect": effect, "duration": duration})

  def show(self, effect, duration=800):
    """
    Description:
    -----------
    If and how to animate the showing of the panel.

    Related Pages:

      https://api.jqueryui.com/tabs/

    Attributes:
    ----------
    :param effect: String.
    :param duration: Number. Optional.  The panel will fade out with the specified duration and the default easing.
    """
    self._config({"effect": effect, "duration": duration})

  def activate(self, js_funcs, profile):
    """
    Description:
    ------------
    Triggered after a panel has been activated (after animation completes). If the accordion was previously collapsed,

    Related Pages:

      https://api.jqueryui.com/tabs/

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True)

  def beforeActivate(self, js_funcs, profile):
    """
    Description:
    ------------
    Triggered directly before a panel is activated. Can be canceled to prevent the panel from activating.

    Related Pages:

      https://api.jqueryui.com/tabs/

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True)

  def beforeLoad(self, js_funcs, profile):
    """
    Description:
    ------------
    Triggered when a remote tab is about to be loaded, after the beforeActivate event.

    Related Pages:

      https://api.jqueryui.com/tabs/

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True)

  def create(self, js_funcs, profile):
    """
    Description:
    ------------
    Triggered when the tabs are created.

    Related Pages:

      https://api.jqueryui.com/tabs/

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True)

  def load(self, js_funcs, profile):
    """
    Description:
    ------------
    Triggered after a remote tab has been loaded.

    Related Pages:

      https://api.jqueryui.com/tabs/

    Attributes:
    ----------
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config("function (event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True)
