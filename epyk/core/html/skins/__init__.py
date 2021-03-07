#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.skins import Winter


class Skins:

  def __init__(self, page):
    self.page = page

  def winter(self, width=(100, '%'), height=(100, '%'), options=None, profile=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    """
    component = Winter.WinterSnow(self.page, width, height, "snow_skin", options, profile)
    component.style.css.z_index = -1
    component.style.css.position = "absolute"
    return component

