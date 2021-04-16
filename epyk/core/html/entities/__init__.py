#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.entities import EntHtml4
from epyk.core.html.entities import EntUtf8
from epyk.core.html.entities import EntHtml5_A
from epyk.core.html.entities import EntHtml5_B
from epyk.core.html.entities import EntHtml5_C
from epyk.core.html.entities import EntHtml5_D

from epyk.core.html import Defaults


class Entities:
  """

  """

  word_break = '<wbr>'
  word_break_hyphen = '&shy;'
  non_breaking_space = '&#160;'
  less_than = '&#60;'
  greater_than = '&#62;'
  ampersand = '&#38;'
  double_quotation_mark = '&#34;'
  single_quotation_mark_apostrophe = '&#39;'
  cent = '&#162;'
  pound = '&#163;'
  yen = '&#165;'
  euro = '&#8364;'
  copyright = '&#169;'
  registered_trademark = '&#174;'

  @property
  def html4(self):
    """

    Related Pages:

      https://www.w3schools.com/charsets/ref_html_entities_4.asp
    """
    return EntHtml4

  @property
  def utf8(self):
    """

    Related Pages:

      https://www.utf8-chartable.de/unicode-utf8-table.pl?start=8256&utf8=string-literal&unicodeinhtml=hex
      https://www.utf8-chartable.de/unicode-utf8-table.pl?start=128&number=128&utf8=string-literal&unicodeinhtml=hex
    """
    return EntUtf8

  @property
  def html5_a(self):
    """

    Related Pages:

      https://www.w3schools.com/charsets/ref_html_entities_a.asp
    """
    return EntHtml5_A

  @property
  def html5_b(self):
    """

    Related Pages:

      https://www.w3schools.com/charsets/ref_html_entities_b.asp
    """
    return EntHtml5_B

  @property
  def html5_c(self):
    """

    Related Pages:

      https://www.w3schools.com/charsets/ref_html_entities_c.asp
    """
    return EntHtml5_C

  @property
  def html5_d(self):
    """

    Related Pages:

      https://www.w3schools.com/charsets/ref_html_entities_d.asp
    """
    return EntHtml5_D

  @property
  def exts(self):
    """
    Bespoke Entities extensions from the Default layer
    """
    return Defaults.ENTITIES_ADD_ON
