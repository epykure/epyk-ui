#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Any
import collections.abc


def size(value: Any, unit: str = "%", toStr: bool = False):
    """ Wrapper to allow size arguments to be more flexible.
    By using this in the interface it is possible to then use float values instead of the usual tuples.

    `w3schools <https://www.w3schools.com/cssref/css_units.asp>`_

    :param value: The value for this argument
    :param unit: Optional. The unit for the argument. Default %
    :param toStr: Optional. Transform the tuple to string
    """
    if value is False:
        return None, ""

    if isinstance(value, tuple):
        if toStr:
            return "{}{}".format(value[0], value[1])

        return value

    elif value == "auto":
        return value, ''

    else:
        if isinstance(value, str):
            if value.endswith("%"):
                unit = value[-1:]
                value = int(value[:-1])
            else:
                unit = value[-2:]
                if unit not in ["cm", "mm", "in", "px", "pt", "pc", "em", "ex", "ch", "vw", "vh"]:
                    raise ValueError("Unit not recognised {}".format(unit))

                value = int(value[:-2])
        else:
            if value is not None and value > 100 and unit == "%":
                unit = "px"
    if toStr:
        if not value:
            return "auto"

        return "{}{}".format(value, unit)
    return value, unit


class Align:
    """ A string with the horizontal position of the component."""

    @property
    def center(self):
        return "center"

    @property
    def left(self):
        return "left"

    @property
    def right(self):
        return "right"


class Position:
    """ A string with the vertical position of the component."""

    @property
    def top(self):
        return "top"

    @property
    def bottom(self):
        return "bottom"

    @property
    def middle(self):
        return "middle"


class Size:
    """ A tuple with the integer for the component size and its unit."""

    @property
    def auto(self):
        return "auto", ''

    @staticmethod
    def px(value):
        return value, 'px'

    @staticmethod
    def percent(value):
        return value, '%'


class Color:
    """ The font color in the component. Default inherit."""

    @property
    def white(self):
        return ""


class Profile:
    """ A flag to set the component performance storage."""

    @property
    def true(self):
        return True

    def name(self, name: str):
        return {"name": name}


ICON = "The component icon content from font-awesome references"
COLOR = Color()
WIDTH = Size()
# "A tuple with the integer for the component height and its unit"
HEIGHT = Size()
PROFILE = Profile()
OPTIONS = "Specific Python options available for this component"
ALIGN = Align()
POSITION = Position()

DSC_TOP = "The top property affects the vertical position of a positioned element."
DSC_LEFT = "The left property affects the horizontal position of a positioned element."
DSC_RIGHT = "The right property affects the horizontal position of a positioned element."
DSC_LABEL = "The text of label to be added to the component"
DSC_HELPER = "A tooltip helper"
DSC_TOOLTIP = "A string with the value of the tooltip"
DSC_JSFNCS = "The Javascript functions"
DSC_HTMLCODE = "An identifier for this component (on both Python and Javascript side)"


def rupdate(d: dict, u: dict) -> dict:
    """Recursive nested dict update

    :param d: source dictionary
    :param u: dictionary to be merged
    """
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = rupdate(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def clean_opt(inputs: dict, options: dict) -> dict:
    """Clean the ECharts options.

    :param inputs: Input parameters
    :param options: New chart options
    """
    if inputs:
        if "params" in inputs:
            options.setdefault("ek", {}).setdefault("params", {}).update(inputs["params"])
            del inputs["params"]

        if "series" in inputs:
            options.setdefault("ek", {}).setdefault("series", {}).update(inputs["series"])
            del inputs["series"]

        if "names" in inputs:
            options.setdefault("ek", {}).setdefault("names", {}).update(inputs["names"])
            del inputs["names"]

        options.update(inputs)
    return options


def update_series(series, options: dict):
    """Update series object with input chart options.
    This will be used when common series properties are defined or some specific named properties are defined
    for a series.

    :param series:
    :param options:
    """
    if options and "series" in options["ek"]:
        series.set_attrs(options["ek"]["series"])
    if "names" in options["ek"] and series.name in options["ek"]["names"]:
        series.set_attrs(options["ek"]["names"][series.name])


def set_default(options: dict, dflt_attrs: dict):
    """Set options arguments if not already defined.
    This will do the update recursively.

    :param options: Component's options
    :param dflt_attrs: Component' default options
    """
    for k, v in dflt_attrs.items():
        if isinstance(v, dict):
            if k in options:
                set_default(options[k], v)
            else:
                options[k] = v
        else:
            if not k in options:
                options[k] = v


