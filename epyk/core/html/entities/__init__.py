#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import EntHtml4, EntUtf8, EntHtml5_A, EntHtml5_B, EntHtml5_C, EntHtml5_D
from .. import Defaults


class Entities:

    word_break: str = '<wbr>'
    word_break_hyphen: str = '&shy;'
    non_breaking_space: str = '&#160;'
    less_than: str = '&#60;'
    greater_than: str = '&#62;'
    ampersand: str = '&#38;'
    double_quotation_mark: str = '&#34;'
    single_quotation_mark_apostrophe: str = '&#39;'
    cent: str = '&#162;'
    pound: str = '&#163;'
    yen: str = '&#165;'
    euro: str = '&#8364;'
    copyright: str = '&#169;'
    registered_trademark: str = '&#174;'

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
