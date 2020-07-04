#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.html import Html
from epyk.core.js.Imports import requires


class ConfigTable(Html.Html):
  requirements = ('tabulator', )
  name = 'Config Table'

  def __init__(self, report, htmlCode, visible, profile):
    pass

  def load(self):
    """

    :return:
    """

  def get(self):
    """

    :param htmlCode:
    :return:
    """
