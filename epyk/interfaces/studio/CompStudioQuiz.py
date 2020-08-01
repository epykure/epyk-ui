#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeRed


class Quiz(object):

  def __init__(self, context):
    self.parent = context
