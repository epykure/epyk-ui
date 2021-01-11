#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import HtmlTextComp


class MdcComposite(HtmlTextComp.Composite):

  extended_map = None

  @property
  def _get_comp_map(self):
    """
    Description:
    ------------
    This list is specific for the Material components.

    Span are replaced by div as I did not want to use the span as a container object.
    I believe this component should remain a base one.

    """
    if self.extended_map is None:
      self.extended_map = dict(super(MdcComposite, self)._get_comp_map)
      self.extended_map.update({
        'icon': self._report.web.mt.icon,

        # Specific material shortcuts are prefixed with mdc_
        'mdc_icon': self._report.web.mt.icon,
        'mdc_floating': self._report.web.mt.texts.floating,
        'mdc_field': self._report.web.mt.texts.field,
        'mdc_line': self._report.web.mt.texts.line,
        'mdc_radio': self._report.web.mt.inputs.mdc_radio,
      })
    return self.extended_map
