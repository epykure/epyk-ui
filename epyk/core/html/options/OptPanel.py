#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.html.options import Options
from epyk.core.html.options import OptionsWithTemplates
from epyk.core.js.packages import packageImport


class OptionsPanelPoints(Options):

  @property
  def background_color(self):
    return self.get(self.page.theme.success[1])

  @background_color.setter
  def background_color(self, val):
    self.set(val)

  @property
  def div_css(self):
    return self.get({})

  @div_css.setter
  def div_css(self, css):
    self.set(css)

  @property
  def selected(self):
    return self.get(0)

  @selected.setter
  def selected(self, num):
    self.set(num)


class OptionPanelSliding(Options):
  component_properties = ("title_align", )

  @property
  def expanded(self):
    """  

    :return:
    """
    return self.get(True)

  @expanded.setter
  def expanded(self, flag: bool):
    self.set(flag)

  @property
  def icon_expanded(self):
    """  
    Add the open icon item.
    """
    if "material-design-icons" in self.component.requirements:
      return self.get("material-icons")

    if "office-ui-fabric-core" in self.component.requirements:
      return self.get("ms-Icon ms-Icon--CaretSolidDown")

    return self.get("fas fa-caret-down")

  @icon_expanded.setter
  def icon_expanded(self, icon: str):
    self.set(icon)

  @property
  def icon_closed(self):
    """  
    Add the close icon item.
    """
    if "material-design-icons" in self.component.requirements:
      return self.get("material-icons")

    if "office-ui-fabric-core" in self.component.requirements:
      return self.get("ms-Icon ms-Icon--CaretSolidUp")

    return self.get("fas fa-caret-up")

  @icon_closed.setter
  def icon_closed(self, icon: str):
    self.set(icon)

  @property
  def icon_position(self):
    """  
    Define the position for the arrow icon in the title.
    """
    return self.get("left")

  @icon_position.setter
  def icon_position(self, value: str):
    self.set(value)

  @property
  def title_align(self):
    """  
    Define the title position.
    """
    return self.get("left")

  @title_align.setter
  def title_align(self, value: str):
    self.set(value)

  @property
  def click_type(self):
    return self.get("title")

  @click_type.setter
  def click_type(self, value: str):
    self.set(value)


class OptionPanelTabs(Options):

  @property
  def display(self):
    return self.get("inline-block")

  @display.setter
  def display(self, value: str):
    self.set(value)

  @property
  def width(self):
    """  
    Set the with in pixel for the tabs.
    This will be applied to all the tabs in the container. It is possible to override the values for each tab.
    """
    return self.get(dfl=100)

  @width.setter
  def width(self, value: int):
    self.set(value)

  @property
  def css_tab(self):
    """  
    The default CSS style for the tabs.
    This must be changed before adding components
    """
    dfl = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 5px 0',
           "border-bottom": "2px solid %s" % self.component.page.theme.greys[0]}
    return self.get(dfl)

  @css_tab.setter
  def css_tab(self, attrs: dict):
    self.set(attrs)

  @property
  def css_tab_clicked(self):
    """  
    The default CSS style for the clicked tab.
    This must be changed before adding components
    """
    return self.get({"border-bottom": "2px solid %s" % self.component.page.theme.colors[-1]})

  @css_tab_clicked.setter
  def css_tab_clicked(self, attrs: dict):
    self.set(attrs)

  def tab_style(self, name: str, css_style: dict = None):
    """  

    :param name:
    :param css_style:
    """
    if 'tab_style' not in self._attrs:
      self._attrs['tab_style'] = {}
    css = dict(self.css_tab)
    if css_style is not None:
      css.update(css_style)
      self._attrs['tab_style'][name] = css
    return self._attrs['tab_style'].get(name, css)

  def tab_clicked_style(self, name, css_style=None):
    """  

    :param name:
    :param css_style:
    """
    if 'tab_style_clicked' not in self._attrs:
      self._attrs['tab_style_clicked'] = {}
    css = dict(self.css_tab_clicked)
    if css_style is not None:
      css.update(css_style)
      self._attrs['tab_style_clicked'][name] = css
    return self._attrs['tab_style_clicked'].get(name, css)

  def tab_not_clicked_style(self, name: str = None, css_style: dict = None):
    """  

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
    """
    return self.get(True)

  @header.setter
  def header(self, flag):
    self.set(flag)

  @property
  def cell_align(self):
    """  
    """
    return self.get()

  @cell_align.setter
  def cell_align(self, value):
    self.set(value)


class OptionsDiv(Options):

  @property
  def inline(self):
    """  
    """
    return self.get(False)

  @inline.setter
  def inline(self, flag: bool):
    self.set(flag)

  @property
  def html_encode(self):
    """  
    Encode Python content to HTML format.
    """
    return self._config_get(False)

  @html_encode.setter
  def html_encode(self, flag: bool):
    self._config(flag)

  @property
  def multiline(self):
    """  
    Replace the Python \n to the HTML tag <br/>.
    """
    return self._config_get(False)

  @multiline.setter
  def multiline(self, flag: bool):
    self._config(flag)


class OptionDrawer(Options):

  @property
  def side(self):
    """  
    """
    return self.get("left")

  @side.setter
  def side(self, value: str):
    self.set(value)

  @property
  def width(self):
    """  
    """
    return self.get("200px")

  @width.setter
  def width(self, num: int):
    if isinstance(num, int):
      num = "%spx" % num
    self.set(num)


class OptionsStepper(Options):
  component_properties = ("column_title", "column_text", "column_label", "column_tooltip")

  def __add_colors(self, type: str, colors: Union[list, dict]):
    """ Set the colors for a step state

    :param type: The state
    :param colors: The color definition
    """
    if not isinstance(colors[0], dict):
      s = 100 / (len(colors) - 1)
      colors = [{"color": c, 'offset': "%s%%" % int(i * s)} for i, c in enumerate(colors)]
    self._config_group('colors', colors, name=type)

  @property
  def success(self):
    """  
    Add the success colors
    """
    return self._config_group_get('colors', {})

  @success.setter
  def success(self, colors: Union[list, dict]):
    self.__add_colors('success', colors)

  @property
  def error(self):
    """  

    """
    return self._config_group_get('colors', {})

  @error.setter
  def error(self, colors: Union[list, dict]):
    self.__add_colors('error', colors)

  @property
  def pending(self):
    """

    """
    return self._config_group_get('colors', {})

  @pending.setter
  def pending(self, colors: Union[list, dict]):
    self.__add_colors('pending', colors)

  @property
  def waiting(self):
    """  
    The list of
    """
    return self._config_group_get('colors', {})

  @waiting.setter
  def waiting(self, colors: Union[list, dict]):
    self.__add_colors('waiting', colors)

  @property
  def blink(self):
    """  

    """
    return self._config_group_get('colors', {})

  @blink.setter
  def blink(self, colors: Union[list, dict]):
    self.__add_colors('blink', colors)

  @property
  def circle_factor(self):
    """  

    """
    return self._config_get(False)

  @circle_factor.setter
  def circle_factor(self, flag: bool):
    self._config(flag)

  @property
  def width(self):
    """  

    """
    return self.svg_style['width']

  @width.setter
  def width(self, num: int):
    self.svg_style['width'] = num

  @property
  def shape(self):
    """  

    """
    return self._config_get('arrow')

  @shape.setter
  def shape(self, value: str):
    self._config(value)

  @property
  def opacities(self):
    """  

    """
    return self._config_get([])

  @opacities.setter
  def opacities(self, values):
    self._config(values)

  @property
  def height(self):
    """  

    """
    return self._config_get(50)

  @height.setter
  def height(self, num: int):
    self._config(num)

  @property
  def line(self):
    """  

    """
    return self._config_get(False)

  @line.setter
  def line(self, attrs: Union[dict, bool]):
    if attrs is True:
      attrs = {"stroke": 'grey', 'stroke-width': 2}
    self._config(attrs)

  @property
  def backgrounds(self):
    """  

    """
    return self._config_get({})

  @backgrounds.setter
  def backgrounds(self, color: str):
    self._config(color)

  @property
  def svg_style(self):
    """  

    """
    return self._config_get({})

  @svg_style.setter
  def svg_style(self, css: dict):
    attrs = self._config_get({})
    attrs.update(css)
    self._config(attrs)

  @property
  def text_color(self):
    """  

    """
    return self._config_get('white')

  @text_color.setter
  def text_color(self, colors):
    self._config(colors)

  @property
  def text_style(self):
    """  

    """
    return self._config_get({})

  @text_style.setter
  def text_style(self, css: dict):
    attrs = self._config_get({})
    attrs.update(css)
    self._config(attrs)

  @property
  def column_title(self):
    """ Column name for the title in the recordset.
    """
    return self._config_get("title")

  @column_title.setter
  def column_title(self, value: str):
    self._config(value)

  @property
  def column_text(self):
    """ Column name for the text in the recordset.
    """
    return self._config_get("text")

  @column_text.setter
  def column_text(self, value: str):
    self._config(value)

  @property
  def column_label(self):
    """ Column name for the label in the recordset.
    """
    return self._config_get("label")

  @column_label.setter
  def column_label(self, value: str):
    self._config(value)

  @property
  def column_tooltip(self):
    """ Column name for the tootlip in the recordset.
    """
    return self._config_get("tooltip")

  @column_tooltip.setter
  def column_tooltip(self, value: str):
    self._config(value)


class OptionGrid(OptionsWithTemplates):
  component_properties = ('columns', 'class_col', 'class_row', 'class_title', 'title_tag', 'sortable')

  @property
  def autoSize(self):
    """  
    """
    return self.get(True)

  @autoSize.setter
  def autoSize(self, flag: bool):
    self.set(flag)

  @property
  def columns(self):
    """ Fix number of columns in the grid builder """
    return self._config_get(4)

  @columns.setter
  def columns(self, num: int):
    self.class_col = "col col-%s" % round(12 / num)
    self._config(num)

  @property
  def pivot(self):
    """ Column name for pivoting the records and building the grid """
    return self._config_get(None)

  @pivot.setter
  def pivot(self, value: str):
    self._config(value)

  @property
  def class_title(self):
    """ CSS class definition for the cell title """
    return self._config_get("text-center")

  @class_title.setter
  def class_title(self, value: str):
    self._config(value)

  @property
  def title_tag(self):
    """ Title HTML tag - default H4 """
    return self._config_get("h4")

  @title_tag.setter
  def title_tag(self, value: str):
    self._config(value)

  @property
  def responsive(self):
    """  
    """
    return self.get(True)

  @responsive.setter
  def responsive(self, flag: bool):
    self.set(flag)

  @property
  def template(self):
    """ Component used as template to build the grid """
    return self.get(True)

  @template.setter
  def template(self, component):
    self.set(component)

  @property
  def classe(self):
    """  
    """
    return self.get("container-fluid")

  @classe.setter
  def classe(self, cls):
    self.set(cls)

  @property
  def class_col(self):
    """ Col / Cell CSS class  """
    return self._config_get("col")

  @class_col.setter
  def class_col(self, cls: str):
    self._config(cls)

  @property
  def class_row(self):
    """ Row CSS Class"""
    return self._config_get("row")

  @class_row.setter
  def class_row(self, cls: str):
    self._config(cls)

  @property
  def noGutters(self):
    """  

    `Related Pages <https://getbootstrap.com/docs/4.0/layout/grid/>`_
    """
    return self.get(False)

  @noGutters.setter
  def noGutters(self, flag: bool):
    self.set(flag)

  @property
  def sortable(self):
    """
    """
    return self._config_get(False)

  @sortable.setter
  @packageImport('sortablejs')
  def sortable(self, values: Union[dict, bool]):
    if values is True:
      self.page.theme.notch()
      self.page.properties.css.add_text(
        '''.sortable-shadow-class {box-shadow: 5px 10px %s;}''' % self.page.theme.colors[0],
        map_id="sortable-shadow-class")
      values = {"animation": 150, "fallbackOnBody": True, "swapThreshold": 0.65,
                "ghostClass": "sortable-shadow-class"}
    if isinstance(values, dict) and "group" not in values:
      values["group"] = self.component.html_code

    self._config(values)


class OptionPopup(Options):

  component_properties = ("z_index", "draggable", "background", "escape")

  @property
  def background(self):
    """Boolean to mention if the popup should have a grey background."""
    return self.get(True)

  @background.setter
  def background(self, flag: bool):
    self.set(flag)

  @property
  def draggable(self):
    """Specify if the popup window is draggable.
    If True this will set the background flag to False.
    """
    return self.get(False)

  @draggable.setter
  def draggable(self, flag: bool):
    if flag:
      self.background = False
    self.set(flag)

  @property
  def closure(self):
    """ """
    return self.get(False)

  @closure.setter
  def closure(self, icon: str):
    if icon:
      self.component.close = self.page.ui.icon(icon)
    else:
      if getattr(self.component, "close", None) is not None:
        del self.page.components[self.component.close.htmlCode]

    self.set(icon)

  @property
  def top(self):
    """ """
    return self.get(100)

  @top.setter
  def top(self, value: int):
    self.set(value)

  @property
  def escape(self):
    """ """
    return self.get(True)

  @escape.setter
  def escape(self, flag: bool):
    if flag:
      self.component.keyup.escape(self.component.dom.hide().r, source_event="document")
    self.set(flag)

  @property
  def margin(self):
    """ Set the margin. By default the value will be in percentage but the unit can be supplied"""
    return self.get(10)

  @margin.setter
  def margin(self, num):
    if isinstance(num, int):
      self.set("%s%%" % num)
    else:
      self.set(num)

  @property
  def z_index(self):
    """ """
    return self.get(800)

  @z_index.setter
  def z_index(self, value: int):
    self.set(value)
