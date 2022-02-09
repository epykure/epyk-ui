#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives
from epyk.core.html.skins import Winter
from epyk.core.html.skins import Movies
from epyk.core.html.skins import Parties
from epyk.core.html.skins import Summer

# TODO change loading animation with skins


class Skins:

  def __init__(self, page: primitives.PageModel):
    self.page = page

  def set(self, skin: str = "", options: dict = None, profile: Union[dict, bool] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param str skin: Optional. The skin name.
    :param dict options: Optional. Specific Python options available for this component.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.
    """
    if skin:
      getattr(self, skin.lower())(options=options, profile=profile)

  def rains(self, width: tuple = (100, '%'), height: tuple = (100, '%'), options: dict = None,
            profile: Union[dict, bool] = None):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:

      https://codepen.io/ruigewaard/pen/JHDdF

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param dict options: Optional. Specific Python options available for this component.
    :param Union[dict, bool] profile:. Optional. A flag to set the component performance storage.
    """
    component = Winter.Rains(self.page, width, height, "snow_skin", options, profile)
    component.style.css.z_index = -1
    component.style.css.position = "fixed"
    component.style.css.left = 0
    component.style.css.top = 0
    self.page.theme.dark = True
    self.page.body.style.css.background = self.page.theme.black
    self.page.body.style.css.color = self.page.theme.white
    return component

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
    component.style.css.position = "fixed"
    component.style.css.left = 0
    component.style.css.top = 0
    self.page.theme.dark = True
    self.page.body.style.css.background = self.page.theme.black
    self.page.body.style.css.color = self.page.theme.white
    return component

  def matrix(self, width=(100, '%'), height=(100, '%'), options=None, profile=None):
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
    component = Movies.Matrix(self.page, width, height, "snow_skin", options, profile)
    component.style.css.z_index = -1
    component.style.css.position = "fixed"
    component.style.css.left = 0
    component.style.css.top = 0
    self.page.theme.dark = True
    self.page.body.style.css.background = self.page.theme.black
    self.page.body.style.css.color = self.page.theme.white
    return component

  def doctor(self, width=(100, '%'), height=(100, '%'), options=None, profile=None):
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
    component = Movies.Doctor(self.page, width, height, "snow_skin", options, profile)
    component.style.css.z_index = -1
    component.style.css.position = "fixed"
    component.style.css.left = 0
    component.style.css.top = 0
    self.page.theme.dark = True
    self.page.body.style.css.background = self.page.theme.black
    self.page.body.style.css.color = self.page.theme.white
    return component

  def fireworks(self, width=(100, '%'), height=(100, '%'), options=None, profile=None):
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
    component = Parties.Fireworks(self.page, width, height, "snow_skin", options, profile)
    component.style.css.z_index = -1
    component.style.css.position = "fixed"
    component.style.css.left = 0
    component.style.css.top = 0
    self.page.theme.dark = True
    self.page.body.style.css.background = self.page.theme.black
    self.page.body.style.css.color = self.page.theme.white
    return component

  def birthday(self, width=(100, '%'), height=(100, '%'), options=None, profile=None):
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
    component = Parties.Birthday(self.page, width, height, "snow_skin", options, profile)
    component.style.css.z_index = -1
    component.style.css.position = "fixed"
    component.style.css.left = 0
    component.style.css.top = 0
    self.page.theme.dark = True
    self.page.body.style.css.background = self.page.theme.black
    self.page.body.style.css.color = self.page.theme.white
    return component

  def lights(self, width=(100, '%'), height=(100, '%'), options=None, profile=None):
    """
    Description:
    -----------
    Add fireflies to the background page.

    Usage:
    -----


    Related Pages:

      https://codepen.io/Mertl/pen/GexapP

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    """
    component = Summer.Lights(self.page, width, height, "snow_skin", options, profile)
    component.style.css.z_index = -1
    component.style.css.position = "fixed"
    component.style.css.left = 0
    component.style.css.top = 0
    self.page.theme.dark = True
    self.page.body.style.css.background = self.page.theme.black
    self.page.body.style.css.color = self.page.theme.white
    return component
