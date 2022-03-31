#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles.classes import CssStyle


class CssLoadingLine(CssStyle.Style):
  _attrs = {
    'overflow': 'hidden',
    'margin': '100px auto',
    'position': 'relative'
  }

  _before = {
    "content": '""',
    "position": 'absolute',
    "left": '-50%',
    "height": '3px',
    "width": '40%',
    "background-color": 'coral',
    "-webkit-animation": 'lineAnim 1s linear infinite',
    "-moz-animation": 'lineAnim 1s linear infinite',
    "animation": 'lineAnim 1s linear infinite',
  }

  def customize(self):
    self.before.css({"background-color": self.page.theme.success.base})
    self.keyframes("lineAnim", {
        "0%": {"left": "-40%"},
        "50%": {"left": "20%", "width": "80%"},
        "100%": {"left": "100%", "width": "100%"}
    })
