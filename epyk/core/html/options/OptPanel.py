
from epyk.core.html.options import Options


class OptionsPanelPoints(object):

  def __init__(self, src, options):
    self.src = src
    self.__background_color = options.get("background-color", src.theme.success[1])
    self.__div_css = options.get("div_css", {})
    self.__selected = options.get("selected", 0)

  @property
  def background_color(self):
    return self.__background_color

  @background_color.setter
  def background_color(self, val):
    self.__background_color = val

  @property
  def div_css(self):
    return self.__div_css

  @div_css.setter
  def div_css(self, css):
    self.__div_css = css

  @property
  def selected(self):
    return self.__selected

  @selected.setter
  def selected(self, num):
    self.__selected = num


class OptionPanelSliding(Options):

  @property
  def expanded(self):
    """
    Description:
    ------------

    :return:
    """
    return self.get(True)

  @expanded.setter
  def expanded(self, boool):
    self.set(boool)

  @property
  def icon_expanded(self):
    """
    Description:
    ------------

    :return:
    """
    return self.get("fas fa-caret-down")

  @icon_expanded.setter
  def icon_expanded(self, icon):
    self.set(icon)

  @property
  def icon_closed(self):
    """
    Description:
    ------------

    :return:
    """
    return self.get("fas fa-caret-up")

  @icon_closed.setter
  def icon_closed(self, icon):
    self.set(icon)


class OptionPanelTabs(Options):

  @property
  def css_tab(self):
    """
    Description:
    ------------
    The default CSS style for the tabs.
    This must be changed before adding components
    """
    dflt = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 5px 0', "border-bottom": "1px solid white"}
    return self.get(dflt)

  @css_tab.setter
  def css_tab(self, attrs):
    self.set(attrs)

  @property
  def css_tab_clicked(self):
    """
    Description:
    ------------
    The default CSS style for the clicked tab.
    This must be changed before adding components
    """
    dflt = {"border-bottom": "1px solid %s" % self._report.theme.success[1]}
    return self.get(dflt)

  @css_tab_clicked.setter
  def css_tab_clicked(self, attrs):
    self.set(attrs)

  def tab_style(self, name, css_style=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param css_style:
    """
    if not 'tab_style' in self._attrs:
      self._attrs['tab_style'] = {}
    css = dict(self.css_tab)
    if css_style is not None:
      css.update(css_style)
      self._attrs['tab_style'][name] = css
    return self._attrs['tab_style'].get(name, css)

  def tab_clicked_style(self, name, css_style=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param css_style:
    """
    if not 'tab_style_clicked' in self._attrs:
      self._attrs['tab_style_clicked'] = {}
    css = dict(self.css_tab_clicked)
    if css_style is not None:
      css.update(css_style)
      self._attrs['tab_style_clicked'][name] = css
    return self._attrs['tab_style_clicked'].get(name, css)

  def tab_not_clicked_style(self, name=None, css_style=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param css_style:
    """
    tab_clicked_style = self.tab_clicked_style(name)
    tab_style = self.tab_style(name)
    tab_not_clicked = {k: tab_style[k] if k in tab_style else 'none' for k, v in tab_clicked_style.items()}
    if css_style is not None:
     tab_not_clicked.update(css_style)
    return tab_not_clicked


class OptionPanelTable(Options):

  @property
  def header(self):
    """
    Description:
    ------------
    """
    return self.get(True)

  @header.setter
  def header(self, bool):
    self.set(bool)

  @property
  def cell_align(self):
    """
    Description:
    ------------
    """
    return self.get()

  @cell_align.setter
  def cell_align(self, value):
    self.set(value)


class OptionsDiv(Options):

  @property
  def inline(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @inline.setter
  def inline(self, bool):
    self.set(bool)


class OptionDrawer(Options):

  @property
  def side(self):
    """
    Description:
    ------------
    """
    return self.get("left")

  @side.setter
  def side(self, value):
    self.set(value)

  @property
  def width(self):
    """
    Description:
    ------------
    """
    return self.get("200px")

  @width.setter
  def width(self, integer):
    if isinstance(integer, int):
      integer = "%spx" % integer
    self.set(integer)


class OptionsStepper(Options):

  def __add_colors(self, type, colors):
    """
    Description:
    ------------
    Set the colors for a step state

    Attributes:
    ----------
    :param type: String. The state
    :param colors: List or Dictionary. The color definition
    """
    if not 'colors' in self._report._jsStyles:
      self._report._jsStyles['colors'] = {}
    if not isinstance(colors[0], dict):
      s = 100 / (len(colors) - 1)
      tmp_colors = []
      for i, c in enumerate(colors):
        tmp_colors.append({"color": c, 'offset': "%s%%" % int(i * s)})
      colors = tmp_colors
    self._report._jsStyles['colors'][type] = colors

  @property
  def success(self):
    """
    Description:
    ------------
    Add the success colors
    """
    return self._report._jsStyles.get('colors', {}).get('success', [])

  @success.setter
  def success(self, colors):
    self.__add_colors('success', colors)

  @property
  def error(self):
    """
    Description:
    ------------

    """
    return self._report._jsStyles['colors'].get('error', [])

  @error.setter
  def error(self, colors):
    self.__add_colors('error', colors)

  @property
  def pending(self):
    """
    Description:
    ------------

    """
    return self._report._jsStyles['colors'].get('pending', [])

  @pending.setter
  def pending(self, colors):
    self.__add_colors('pending', colors)

  @property
  def waiting(self):
    """
    Description:
    ------------
    The list of
    """
    return self._report._jsStyles['colors'].get('waiting', [])

  @waiting.setter
  def waiting(self, colors):
    self.__add_colors('waiting', colors)

  @property
  def blink(self):
    """
    Description:
    ------------

    """
    return self._report._jsStyles.get('colors', {}).get('blink')

  @blink.setter
  def blink(self, colors):
    self.__add_colors('blink', colors)

  @property
  def circle_factor(self):
    """
    Description:
    ------------

    """
    return self._config_get(False)

  @circle_factor.setter
  def circle_factor(self, bool):
    self._config(bool)

  @property
  def width(self):
    """
    Description:
    ------------

    """
    return self._config_get(100)

  @width.setter
  def width(self, num):
    self._config(num)

  @property
  def shape(self):
    """
    Description:
    ------------

    """
    return self._config_get('arrow')

  @shape.setter
  def shape(self, value):
    self._config(value)

  @property
  def opacities(self):
    """
    Description:
    ------------

    """
    return self._config_get([])

  @opacities.setter
  def opacities(self, values):
    self._config(values)

  @property
  def height(self):
    """
    Description:
    ------------

    """
    return self._config_get(50)

  @height.setter
  def height(self, num):
    self._config(num)

  @property
  def line(self):
    """
    Description:
    ------------

    """
    return self._config_get(False)

  @line.setter
  def line(self, attrs):
    if attrs is True:
      attrs = {"stroke": 'grey', 'stroke-width': 2}
    self._config(attrs)

  @property
  def backgrounds(self):
    """
    Description:
    ------------

    """
    return self._config_get({})

  @backgrounds.setter
  def backgrounds(self, color):
    self._config(color)

  @property
  def svg_style(self):
    """
    Description:
    ------------

    """
    return self._config_get({})

  @svg_style.setter
  def svg_style(self, css):
    if not 'svg_style' in self._report._jsStyles:
      self._report._jsStyles['svg_style'] = {}
    self._report._jsStyles['svg_style'].update(css)

  @property
  def text_color(self):
    """
    Description:
    ------------

    """
    return self._config_get('white')

  @text_color.setter
  def text_color(self, colors):
    self._config(colors)

  @property
  def text_style(self):
    """
    Description:
    ------------

    """
    return self._config_get({})

  @text_style.setter
  def text_style(self, css):
    if not 'title_style' in self._report._jsStyles:
      self._report._jsStyles['text_style'] = {}
    self._report._jsStyles['text_style'].update(css)


class OptionGrid(Options):

  @property
  def autoSize(self):
    """
    Description:
    ------------
    """
    return self.get(True)

  @autoSize.setter
  def autoSize(self, bool):
    self.set(bool)

  @property
  def noGutters(self):
    """
    Description:
    ------------

    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    return self.get(False)

  @noGutters.setter
  def noGutters(self, bool):
    self.set(bool)
