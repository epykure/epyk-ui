
import json
from typing import Optional, Union

from epyk.core import html
from epyk.core.py import types
from epyk.fwk.mdc.html import HtmlMdcForms
from epyk.interfaces import Arguments


class Components:
  def __init__(self, ui):
    self.page = ui.page

  def discrete(self, number: float = 0, minimum: float = 0, maximum: float = 100, width: types.SIZE_TYPE = (100, '%'),
               height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, helper: str = None,
               options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-fab

    Attributes:
    ----------
    :param number: Optional. The initial value
    :param minimum: Optional. The min value. Default 0
    :param maximum: Optional. The max value. Default 100
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    return
