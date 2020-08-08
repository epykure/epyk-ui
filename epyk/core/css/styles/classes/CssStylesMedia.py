#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.styles.classes import CssStyle


class CssStyleNoSmartphone(CssStyle.Style):

  def customize(self):
    self.media({"display": "none"}, "only", "screen", {'and': [{'max-width': '600px'}]}, change=False, thisClass=True)


class CssStyleFont(CssStyle.Style):

  def customize(self):
    self.media({"font-size": "20px"}, "only", "screen", {'and': [{'max-width': '600px'}]}, change=False, thisClass=True)
