#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.js.objects import JsCanvas


class Canvas(Html.Html):
    name = 'Canvas'
    tag = "canvas"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        super(Canvas, self).__init__(page, "", html_code=html_code, css_attrs={"width": width, "height": height},
                                     options=options, profile=profile)
        self.__ctx = None

    @property
    def dom(self) -> JsCanvas.Canvas:
        """Property to the DOM object.
        This will return the Canvas properties.
        """
        if self._dom is None:
            self._dom = JsCanvas.Canvas(page=self.page, component=self)
        return self._dom

    @property
    def ctx(self) -> JsCanvas.Canvas:
        """Return the 2D context options of the Canvas DOM component"""
        if self.__ctx is None:
            self._dom = JsCanvas.Canvas(page=self.page, component=self)
            self.__ctx = self._dom.getContext2D
        return self.__ctx

    def __str__(self):
        return "<%s %s>Your browser does not support the HTML5 canvas tag.</%s>" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
