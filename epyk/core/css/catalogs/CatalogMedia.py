#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesMedia


class CatalogMedia(Catalog.CatalogGroup):

  def no_phone(self):
    """

    """
    return self._set_class(CssStylesMedia.CssStyleNoSmartphone)

  def font(self):
    """

    """
    return self._set_class(CssStylesMedia.CssStyleFont)
