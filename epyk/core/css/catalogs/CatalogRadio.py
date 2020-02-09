"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesRadio


class CatalogRadio(Catalog.CatalogGroup):
  def button(self):
    """  """
    return self._set_class(CssStylesRadio.CssRadioButton)

  def selected(self):
    """  """
    return self._set_class(CssStylesRadio.CssRadioButtonSelected)

  def switch(self):
    """  """
    return self._set_class(CssStylesRadio.CssRadioSwitch)

  def switch_label(self):
    """  """
    return self._set_class(CssStylesRadio.CssRadioSwitchLabel)

  def switch_checked(self):
    """  """
    return self._set_class(CssStylesRadio.CssRadioSwitchChecked)
