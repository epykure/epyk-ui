#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import importlib

from epyk.core.py import PyCrypto
from epyk.core.py import PyHash
from epyk.core.py import PyRest
from epyk.core.py import PyDates
from epyk.core.py import PyGeo
from epyk.core.py import PyMarkdown

from epyk.core.js.Imports import requires
from epyk.core.html import entities


# https://www.utf8-chartable.de/unicode-utf8-table.pl?unicodeinhtml=dec

UTF8_TO_HTML = {
  b'\xe2\x80\x99': "'",
  b'\xe2\x81\x80': entities.EntUtf8.CHARACTER_TIE,
  b'\xe2\x81\x81': entities.EntUtf8.CARET_INSERTION_POINT,
  b'\xe2\x81\x82': entities.EntUtf8.ASTERISM,
  b'\xe2\x81\x83': entities.EntUtf8.HYPHEN_BULLET,
  b'\xe2\x81\x84': entities.EntUtf8.FRACTION_SLASH,
  b'\xe2\x81\x85': entities.EntUtf8.LEFT_SQUARE_BRACKET_WITH_QUILL,
  b'\xe2\x81\x86': entities.EntUtf8.RIGHT_SQUARE_BRACKET_WITH_QUILL,
  b'\xe2\x81\x87': entities.EntUtf8.DOUBLE_QUESTION_MARK,
  b'\xe2\x81\x88': entities.EntUtf8.QUESTION_EXCLAMATION_MARK,
  b'\xe2\x81\x89': entities.EntUtf8.EXCLAMATION_QUESTION_MARK,
  b'\xe2\x81\x8a': entities.EntUtf8.TIRONIAN_SIGN_ET,
  b'\xe2\x81\x8b': entities.EntUtf8.REVERSED_PILCROW_SIGN,
  b'\xe2\x81\x8c': entities.EntUtf8.BLACK_LEFTWARDS_BULLET,
  b'\xe2\x81\x8d': entities.EntUtf8.BLACK_RIGHTWARDS_BULLET,
  b'\xe2\x81\x8e': entities.EntUtf8.LOW_ASTERISK,
  b'\xe2\x81\x8f': entities.EntUtf8.REVERSED_SEMICOLON,
  b'\xe2\x81\x90': entities.EntUtf8.CLOSE_UP,
  b'\xe2\x81\x91': entities.EntUtf8.TWO_ASTERISKS_ALIGNED_VERTICALLY,
  b'\xe2\x81\x92': entities.EntUtf8.COMMERCIAL_MINUS_SIGN,
  b'\xe2\x81\x93': entities.EntUtf8.SWUNG_DASH,
  b'\xe2\x81\x94': entities.EntUtf8.INVERTED_UNDERTIE,
  b'\xe2\x81\x95': entities.EntUtf8.FLOWER_PUNCTUATION_MARK,
  b'\xe2\x81\x96': entities.EntUtf8.THREE_DOT_PUNCTUATION,
  b'\xe2\x81\x97': entities.EntUtf8.QUADRUPLE_PRIME,
  b'\xe2\x81\x98': entities.EntUtf8.FOUR_DOT_PUNCTUATION,
  b'\xe2\x81\x99': entities.EntUtf8.FIVE_DOT_PUNCTUATION,
  b'\xe2\x81\x9a': entities.EntUtf8.TWO_DOT_PUNCTUATION,
  b'\xe2\x81\x9b': entities.EntUtf8.FOUR_DOT_MARK,
  b'\xe2\x81\x9c': entities.EntUtf8.DOTTED_CROSS,
  b'\xe2\x81\x9d': entities.EntUtf8.TRICOLON,
  b'\xe2\x81\x9e': entities.EntUtf8.VERTICAL_FOUR_DOTS,
  b'\xe2\x81\xa0': entities.EntUtf8.WORD_JOINER,
  b'\xe2\x81\xa1': entities.EntUtf8.FUNCTION_APPLICATION,
  b'\xe2\x81\xa2': entities.EntUtf8.INVISIBLE_TIMES,
  b'\xe2\x81\xa3': entities.EntUtf8.INVISIBLE_SEPARATOR,
  b'\xe2\x81\xa4': entities.EntUtf8.INVISIBLE_PLUS,
  b'\xe2\x81\xa6': entities.EntUtf8.LEFT_TO_RIGHT_ISOLATE,
  b'\xe2\x81\xa7': entities.EntUtf8.RIGHT_TO_LEFT_ISOLATE,
  b'\xe2\x81\xa8': entities.EntUtf8.FIRST_STRONG_ISOLATE,
  b'\xe2\x81\xa9': entities.EntUtf8.POP_DIRECTIONAL_ISOLATE,
  b'\xe2\x81\xaa': entities.EntUtf8.INHIBIT_SYMMETRIC_SWAPPING,
  b'\xe2\x81\xab': entities.EntUtf8.ACTIVATE_SYMMETRIC_SWAPPING,
  b'\xe2\x81\xac': entities.EntUtf8.INHIBIT_ARABIC_FORM_SHAPING,
  b'\xe2\x81\xad': entities.EntUtf8.ACTIVATE_ARABIC_FORM_SHAPING,
  b'\xe2\x81\xae': entities.EntUtf8.NATIONAL_DIGIT_SHAPES,
  b'\xe2\x81\xaf': entities.EntUtf8.NOMINAL_DIGIT_SHAPES,
  b'\xe2\x81\xb0': entities.EntUtf8.SUPERSCRIPT_ZERO,
  b'\xe2\x81\xb1': entities.EntUtf8.SUPERSCRIPT_LATIN_SMALL_LETTER_I,
  b'\xe2\x81\xb4': entities.EntUtf8.SUPERSCRIPT_FOUR,
  b'\xe2\x81\xb5': entities.EntUtf8.SUPERSCRIPT_FIVE,
  b'\xe2\x81\xb6': entities.EntUtf8.SUPERSCRIPT_SIX,
  b'\xe2\x81\xb7': entities.EntUtf8.SUPERSCRIPT_SEVEN,
  b'\xe2\x81\xb8': entities.EntUtf8.SUPERSCRIPT_EIGHT,
  b'\xe2\x81\xb9': entities.EntUtf8.SUPERSCRIPT_NINE,
  b'\xe2\x81\xba': entities.EntUtf8.SUPERSCRIPT_PLUS_SIGN,
  b'\xe2\x81\xbb': entities.EntUtf8.SUPERSCRIPT_MINUS,
  b'\xe2\x81\xbc': entities.EntUtf8.SUPERSCRIPT_EQUALS_SIGN,
  b'\xe2\x81\xbd': entities.EntUtf8.SUPERSCRIPT_LEFT_PARENTHESIS,
  b'\xe2\x81\xbe': entities.EntUtf8.SUPERSCRIPT_RIGHT_PARENTHESIS,
  b'\xe2\x81\xbf': entities.EntUtf8.SUPERSCRIPT_LATIN_SMALL_LETTER_N,
  b'\xe2\x82\x80': entities.EntUtf8.SUBSCRIPT_ZERO,
  b'\xe2\x82\x81': entities.EntUtf8.SUBSCRIPT_ONE,
  b'\xe2\x82\x82': entities.EntUtf8.SUBSCRIPT_TWO,
  b'\xe2\x82\x83': entities.EntUtf8.SUBSCRIPT_THREE,
  b'\xe2\x82\x84': entities.EntUtf8.SUBSCRIPT_FOUR,
  b'\xe2\x82\x85': entities.EntUtf8.SUBSCRIPT_FIVE,
  b'\xe2\x82\x86': entities.EntUtf8.SUBSCRIPT_SIX,
  b'\xe2\x82\x87': entities.EntUtf8.SUBSCRIPT_SEVEN,
  b'\xe2\x82\x88': entities.EntUtf8.SUBSCRIPT_EIGHT,
  b'\xe2\x82\x89': entities.EntUtf8.SUBSCRIPT_NINE,
  b'\xe2\x82\x8a': entities.EntUtf8.SUBSCRIPT_PLUS_SIGN,
  b'\xe2\x82\x8b': entities.EntUtf8.SUBSCRIPT_MINUS,
  b'\xe2\x82\x8c': entities.EntUtf8.SUBSCRIPT_EQUALS_SIGN,
  b'\xe2\x82\x8d': entities.EntUtf8.SUBSCRIPT_LEFT_PARENTHESIS,
  b'\xe2\x82\x8e': entities.EntUtf8.SUBSCRIPT_RIGHT_PARENTHESIS,
  b'\xe2\x82\x90': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_A,
  b'\xe2\x82\x91': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_E,
  b'\xe2\x82\x92': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_O,
  b'\xe2\x82\x93': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_X,
  b'\xe2\x82\x94': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_SCHWA,
  b'\xe2\x82\x95': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_H,
  b'\xe2\x82\x96': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_K,
  b'\xe2\x82\x97': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_L,
  b'\xe2\x82\x98': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_M,
  b'\xe2\x82\x99': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_N,
  b'\xe2\x82\x9a': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_P,
  b'\xe2\x82\x9b': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_S,
  b'\xe2\x82\x9c': entities.EntUtf8.LATIN_SUBSCRIPT_SMALL_LETTER_T,
  b'\xe2\x82\xa0': entities.EntUtf8.EURO_CURRENCY_SIGN,
  b'\xe2\x82\xa1': entities.EntUtf8.COLON_SIGN,
  b'\xe2\x82\xa2': entities.EntUtf8.CRUZEIRO_SIGN,
  b'\xe2\x82\xa3': entities.EntUtf8.FRENCH_FRANC_SIGN,
  b'\xe2\x82\xa4': entities.EntUtf8.LIRA_SIGN,
  b'\xe2\x82\xa5': entities.EntUtf8.MILL_SIGN,
  b'\xe2\x82\xa6': entities.EntUtf8.NAIRA_SIGN,
  b'\xe2\x82\xa7': entities.EntUtf8.PESETA_SIGN,
  b'\xe2\x82\xa8': entities.EntUtf8.RUPEE_SIGN,
  b'\xe2\x82\xa9': entities.EntUtf8.WON_SIGN,
  b'\xe2\x82\xaa': entities.EntUtf8.NEW_SHEQEL_SIGN,
  b'\xe2\x82\xab': entities.EntUtf8.DONG_SIGN,
  b'\xe2\x82\xac': entities.EntUtf8.EURO_SIGN,
  b'\xe2\x82\xad': entities.EntUtf8.KIP_SIGN,
  b'\xe2\x82\xae': entities.EntUtf8.TUGRIK_SIGN,
  b'\xe2\x82\xaf': entities.EntUtf8.DRACHMA_SIGN,
  b'\xe2\x82\xb0': entities.EntUtf8.GERMAN_PENNY_SIGN,
  b'\xe2\x82\xb1': entities.EntUtf8.PESO_SIGN,
  b'\xe2\x82\xb2': entities.EntUtf8.GUARANI_SIGN,
  b'\xe2\x82\xb3': entities.EntUtf8.AUSTRAL_SIGN,
  b'\xe2\x82\xb4': entities.EntUtf8.HRYVNIA_SIGN,
  b'\xe2\x82\xb5': entities.EntUtf8.CEDI_SIGN,
  b'\xe2\x82\xb6': entities.EntUtf8.LIVRE_TOURNOIS_SIGN,
  b'\xe2\x82\xb7': entities.EntUtf8.SPESMILO_SIGN,
  b'\xe2\x82\xb8': entities.EntUtf8.TENGE_SIGN,
  b'\xe2\x82\xb9': entities.EntUtf8.INDIAN_RUPEE_SIGN,
  b'\xe2\x82\xba': entities.EntUtf8.TURKISH_LIRA_SIGN,
  b'\xe2\x82\xbb': entities.EntUtf8.NORDIC_MARK_SIGN,
  b'\xe2\x82\xbc': entities.EntUtf8.MANAT_SIGN,
  b'\xe2\x82\xbd': entities.EntUtf8.RUBLE_SIGN,
  b'\xe2\x82\xbe': entities.EntUtf8.LARI_SIGN,
  b'\xe2\x82\xbf': entities.EntUtf8.BITCOIN_SIGN,
  b'\xe2\x83\x90': entities.EntUtf8.COMBINING_LEFT_HARPOON_ABOVE,
  b'\xe2\x83\x91': entities.EntUtf8.COMBINING_RIGHT_HARPOON_ABOVE,
  b'\xe2\x83\x92': entities.EntUtf8.COMBINING_LONG_VERTICAL_LINE_OVERLAY,
  b'\xe2\x83\x93': entities.EntUtf8.COMBINING_SHORT_VERTICAL_LINE_OVERLAY,
  b'\xe2\x83\x94': entities.EntUtf8.COMBINING_ANTICLOCKWISE_ARROW_ABOVE,
  b'\xe2\x83\x95': entities.EntUtf8.COMBINING_CLOCKWISE_ARROW_ABOVE,
  b'\xe2\x83\x96': entities.EntUtf8.COMBINING_LEFT_ARROW_ABOVE,
  b'\xe2\x83\x97': entities.EntUtf8.COMBINING_RIGHT_ARROW_ABOVE,
  b'\xe2\x83\x98': entities.EntUtf8.COMBINING_RING_OVERLAY,
  b'\xe2\x83\x99': entities.EntUtf8.COMBINING_CLOCKWISE_RING_OVERLAY,
  b'\xe2\x83\x9a': entities.EntUtf8.COMBINING_ANTICLOCKWISE_RING_OVERLAY,
  b'\xe2\x83\x9b': entities.EntUtf8.COMBINING_THREE_DOTS_ABOVE,
  b'\xe2\x83\x9c': entities.EntUtf8.COMBINING_FOUR_DOTS_ABOVE,
  b'\xe2\x83\x9d': entities.EntUtf8.COMBINING_ENCLOSING_CIRCLE,
  b'\xe2\x83\x9e': entities.EntUtf8.COMBINING_ENCLOSING_SQUARE,
  b'\xe2\x83\x9f': entities.EntUtf8.COMBINING_ENCLOSING_DIAMOND,
  b'\xe2\x83\xa0': entities.EntUtf8.COMBINING_ENCLOSING_CIRCLE_BACKSLASH,
  b'\xe2\x83\xa1': entities.EntUtf8.COMBINING_LEFT_RIGHT_ARROW_ABOVE,
  b'\xe2\x83\xa2': entities.EntUtf8.COMBINING_ENCLOSING_SCREEN,
  b'\xe2\x83\xa3': entities.EntUtf8.COMBINING_ENCLOSING_KEYCAP,
  b'\xe2\x83\xa4': entities.EntUtf8.COMBINING_ENCLOSING_UPWARD_POINTING_TRIANGLE,
  b'\xe2\x83\xa5': entities.EntUtf8.COMBINING_REVERSE_SOLIDUS_OVERLAY,
  b'\xe2\x83\xa6': entities.EntUtf8.COMBINING_DOUBLE_VERTICAL_STROKE_OVERLAY,
  b'\xe2\x83\xa7': entities.EntUtf8.COMBINING_ANNUITY_SYMBOL,
  b'\xe2\x83\xa8': entities.EntUtf8.COMBINING_TRIPLE_UNDERDOT,
  b'\xe2\x83\xa9': entities.EntUtf8.COMBINING_WIDE_BRIDGE_ABOVE,
  b'\xe2\x83\xaa': entities.EntUtf8.COMBINING_LEFTWARDS_ARROW_OVERLAY,
  b'\xe2\x83\xab': entities.EntUtf8.COMBINING_LONG_DOUBLE_SOLIDUS_OVERLAY,
  b'\xe2\x83\xac': entities.EntUtf8.COMBINING_RIGHTWARDS_HARPOON_WITH_BARB_DOWNWARDS,
  b'\xe2\x83\xad': entities.EntUtf8.COMBINING_LEFTWARDS_HARPOON_WITH_BARB_DOWNWARDS,
  b'\xe2\x83\xae': entities.EntUtf8.COMBINING_LEFT_ARROW_BELOW,
  b'\xe2\x83\xaf': entities.EntUtf8.COMBINING_RIGHT_ARROW_BELOW,
  b'\xe2\x83\xb0': entities.EntUtf8.COMBINING_ASTERISK_ABOVE,
  b'\xe2\x84\x80': entities.EntUtf8.ACCOUNT_OF,
  b'\xe2\x84\x81': entities.EntUtf8.ADDRESSED_TO_THE_SUBJECT,
  b'\xe2\x84\x82': entities.EntUtf8.DOUBLE_STRUCK_CAPITAL_C,
  b'\xe2\x84\x83': entities.EntUtf8.DEGREE_CELSIUS,
  b'\xe2\x84\x84': entities.EntUtf8.CENTRE_LINE_SYMBOL,
  b'\xe2\x84\x85': entities.EntUtf8.CARE_OF,
  b'\xe2\x84\x86': entities.EntUtf8.CADA_UNA,
  b'\xe2\x84\x87': entities.EntUtf8.EULER_CONSTANT,
  b'\xe2\x84\x88': entities.EntUtf8.SCRUPLE,
  b'\xe2\x84\x89': entities.EntUtf8.DEGREE_FAHRENHEIT,
  b'\xe2\x84\x8a': entities.EntUtf8.SCRIPT_SMALL_G,
  b'\xe2\x84\x8b': entities.EntUtf8.SCRIPT_CAPITAL_H,
  b'\xe2\x84\x8c': entities.EntUtf8.BLACK_LETTER_CAPITAL_H,
  b'\xe2\x84\x8d': entities.EntUtf8.DOUBLE_STRUCK_CAPITAL_H,
  b'\xe2\x84\x8e': entities.EntUtf8.PLANCK_CONSTANT,
  b'\xe2\x84\x8f': entities.EntUtf8.PLANCK_CONSTANT_OVER_TWO_PI,
  b'\xe2\x84\x90': entities.EntUtf8.SCRIPT_CAPITAL_I,
  b'\xe2\x84\x91': entities.EntUtf8.BLACK_LETTER_CAPITAL_I,
  b'\xe2\x84\x92': entities.EntUtf8.SCRIPT_CAPITAL_L,
  b'\xe2\x84\x93': entities.EntUtf8.SCRIPT_SMALL_L,
  b'\xe2\x84\x94': entities.EntUtf8.L_B_BAR_SYMBOL,
  b'\xe2\x84\x95': entities.EntUtf8.DOUBLE_STRUCK_CAPITAL_N,
  b'\xe2\x84\x96': entities.EntUtf8.NUMERO_SIGN,
  b'\xe2\x84\x97': entities.EntUtf8.SOUND_RECORDING_COPYRIGHT,
  b'\xe2\x84\x98': entities.EntUtf8.SCRIPT_CAPITAL_P,
  b'\xe2\x84\x99': entities.EntUtf8.DOUBLE_STRUCK_CAPITAL_P,
  b'\xe2\x84\x9a': entities.EntUtf8.DOUBLE_STRUCK_CAPITAL_Q,
  b'\xe2\x84\x9b': entities.EntUtf8.SCRIPT_CAPITAL_R,
  b'\xe2\x84\x9c': entities.EntUtf8.BLACK_LETTER_CAPITAL_R,
  b'\xe2\x84\x9d': entities.EntUtf8.DOUBLE_STRUCK_CAPITAL_R,
  b'\xe2\x84\x9e': entities.EntUtf8.PRESCRIPTION_TAKE,
  b'\xe2\x84\x9f': entities.EntUtf8.RESPONSE,
  b'\xe2\x84\xa0': entities.EntUtf8.SERVICE_MARK,
  b'\xe2\x84\xa1': entities.EntUtf8.TELEPHONE_SIGN,
  b'\xe2\x84\xa2': entities.EntUtf8.TRADE_MARK_SIGN,
  b'\xe2\x84\xa3': entities.EntUtf8.VERSICLE,
  b'\xe2\x84\xa4': entities.EntUtf8.DOUBLE_STRUCK_CAPITAL_Z,
  b'\xe2\x84\xa5': entities.EntUtf8.OUNCE_SIGN,
  b'\xe2\x84\xa6': entities.EntUtf8.OHM_SIGN,
  b'\xe2\x84\xa7': entities.EntUtf8.INVERTED_OHM_SIGN,
  b'\xe2\x84\xa8': entities.EntUtf8.BLACK_LETTER_CAPITAL_Z,
  b'\xe2\x84\xa9': entities.EntUtf8.TURNED_GREEK_SMALL_LETTER_IOTA,
  b'\xe2\x84\xaa': entities.EntUtf8.KELVIN_SIGN,
  b'\xe2\x84\xab': entities.EntUtf8.ANGSTROM_SIGN,
  b'\xe2\x84\xac': entities.EntUtf8.SCRIPT_CAPITAL_B,
  b'\xe2\x84\xad': entities.EntUtf8.BLACK_LETTER_CAPITAL_C,
  b'\xe2\x84\xae': entities.EntUtf8.ESTIMATED_SYMBOL,
  b'\xe2\x84\xaf': entities.EntUtf8.SCRIPT_SMALL_E,
  b'\xe2\x84\xb0': entities.EntUtf8.SCRIPT_CAPITAL_E,
  b'\xe2\x84\xb1': entities.EntUtf8.SCRIPT_CAPITAL_F,
  b'\xe2\x84\xb2': entities.EntUtf8.TURNED_CAPITAL_F,
  b'\xe2\x84\xb3': entities.EntUtf8.SCRIPT_CAPITAL_M,
  b'\xe2\x84\xb4': entities.EntUtf8.SCRIPT_SMALL_O,
  b'\xe2\x84\xb5': entities.EntUtf8.ALEF_SYMBOL,
  b'\xe2\x84\xb6': entities.EntUtf8.BET_SYMBOL,
  b'\xe2\x84\xb7': entities.EntUtf8.GIMEL_SYMBOL,
  b'\xe2\x84\xb8': entities.EntUtf8.DALET_SYMBOL,
  b'\xe2\x84\xb9': entities.EntUtf8.INFORMATION_SOURCE,
  b'\xe2\x84\xba': entities.EntUtf8.ROTATED_CAPITAL_Q,
  b'\xe2\x84\xbb': entities.EntUtf8.FACSIMILE_SIGN,
  b'\xe2\x84\xbc': entities.EntUtf8.DOUBLE_STRUCK_SMALL_PI,
  b'\xe2\x84\xbd': entities.EntUtf8.DOUBLE_STRUCK_SMALL_GAMMA,
  b'\xe2\x84\xbe': entities.EntUtf8.DOUBLE_STRUCK_CAPITAL_GAMMA,
  b'\xe2\x84\xbf': entities.EntUtf8.DOUBLE_STRUCK_CAPITAL_PI,
  b'\xc2\xa1': entities.EntUtf8.INVERTED_EXCLAMATION_MARK,
  b'\xc2\xa2': entities.EntUtf8.CENT_SIGN,
  b'\xc2\xa3': entities.EntUtf8.POUND_SIGN,
  b'\xc2\xa4': entities.EntUtf8.CURRENCY_SIGN,
  b'\xc2\xa5': entities.EntUtf8.YEN_SIGN,
  b'\xc2\xa6': entities.EntUtf8.BROKEN_BAR,
  b'\xc2\xa7': entities.EntUtf8.SECTION_SIGN,
  b'\xc2\xa8': entities.EntUtf8.DIAERESIS,
  b'\xc2\xa9': entities.EntUtf8.COPYRIGHT_SIGN,
  b'\xc2\xaa': entities.EntUtf8.FEMININE_ORDINAL_INDICATOR,
  b'\xc2\xab': entities.EntUtf8.LEFT_POINTING_DOUBLE_ANGLE_QUOTATION_MARK,
  b'\xc2\xac': entities.EntUtf8.NOT_SIGN,
  b'\xc2\xad': entities.EntUtf8.SOFT_HYPHEN,
  b'\xc2\xae': entities.EntUtf8.REGISTERED_SIGN,
  b'\xc2\xaf': entities.EntUtf8.MACRON,
  b'\xc2\xb0': entities.EntUtf8.DEGREE_SIGN,
  b'\xc2\xb1': entities.EntUtf8.PLUS_MINUS_SIGN,
  b'\xc2\xb2': entities.EntUtf8.SUPERSCRIPT_TWO,
  b'\xc2\xb3': entities.EntUtf8.SUPERSCRIPT_THREE,
  b'\xc2\xb4': entities.EntUtf8.ACUTE_ACCENT,
  b'\xc2\xb5': entities.EntUtf8.MICRO_SIGN,
  b'\xc2\xb6': entities.EntUtf8.PILCROW_SIGN,
  b'\xc2\xb7': entities.EntUtf8.MIDDLE_DOT,
  b'\xc2\xb8': entities.EntUtf8.CEDILLA,
  b'\xc2\xb9': entities.EntUtf8.SUPERSCRIPT_ONE,
  b'\xc2\xba': entities.EntUtf8.MASCULINE_ORDINAL_INDICATOR,
  b'\xc2\xbb': entities.EntUtf8.RIGHT_POINTING_DOUBLE_ANGLE_QUOTATION_MARK,
  b'\xc2\xbc': entities.EntUtf8.VULGAR_FRACTION_ONE_QUARTER,
  b'\xc2\xbd': entities.EntUtf8.VULGAR_FRACTION_ONE_HALF,
  b'\xc2\xbe': entities.EntUtf8.VULGAR_FRACTION_THREE_QUARTERS,
  b'\xc2\xbf': entities.EntUtf8.INVERTED_QUESTION_MARK,
  b'\xc3\x80': entities.EntUtf8.LATIN_CAPITAL_LETTER_A_WITH_GRAVE,
  b'\xc3\x81': entities.EntUtf8.LATIN_CAPITAL_LETTER_A_WITH_ACUTE,
  b'\xc3\x82': entities.EntUtf8.LATIN_CAPITAL_LETTER_A_WITH_CIRCUMFLEX,
  b'\xc3\x83': entities.EntUtf8.LATIN_CAPITAL_LETTER_A_WITH_TILDE,
  b'\xc3\x84': entities.EntUtf8.LATIN_CAPITAL_LETTER_A_WITH_DIAERESIS,
  b'\xc3\x85': entities.EntUtf8.LATIN_CAPITAL_LETTER_A_WITH_RING_ABOVE,
  b'\xc3\x86': entities.EntUtf8.LATIN_CAPITAL_LETTER_AE,
  b'\xc3\x87': entities.EntUtf8.LATIN_CAPITAL_LETTER_C_WITH_CEDILLA,
  b'\xc3\x88': entities.EntUtf8.LATIN_CAPITAL_LETTER_E_WITH_GRAVE,
  b'\xc3\x89': entities.EntUtf8.LATIN_CAPITAL_LETTER_E_WITH_ACUTE,
  b'\xc3\x8a': entities.EntUtf8.LATIN_CAPITAL_LETTER_E_WITH_CIRCUMFLEX,
  b'\xc3\x8b': entities.EntUtf8.LATIN_CAPITAL_LETTER_E_WITH_DIAERESIS,
  b'\xc3\x8c': entities.EntUtf8.LATIN_CAPITAL_LETTER_I_WITH_GRAVE,
  b'\xc3\x8d': entities.EntUtf8.LATIN_CAPITAL_LETTER_I_WITH_ACUTE,
  b'\xc3\x8e': entities.EntUtf8.LATIN_CAPITAL_LETTER_I_WITH_CIRCUMFLEX,
  b'\xc3\x8f': entities.EntUtf8.LATIN_CAPITAL_LETTER_I_WITH_DIAERESIS,
  b'\xc3\x90': entities.EntUtf8.LATIN_CAPITAL_LETTER_ETH,
  b'\xc3\x91': entities.EntUtf8.LATIN_CAPITAL_LETTER_N_WITH_TILDE,
  b'\xc3\x92': entities.EntUtf8.LATIN_CAPITAL_LETTER_O_WITH_GRAVE,
  b'\xc3\x93': entities.EntUtf8.LATIN_CAPITAL_LETTER_O_WITH_ACUTE,
  b'\xc3\x94': entities.EntUtf8.LATIN_CAPITAL_LETTER_O_WITH_CIRCUMFLEX,
  b'\xc3\x95': entities.EntUtf8.LATIN_CAPITAL_LETTER_O_WITH_TILDE,
  b'\xc3\x96': entities.EntUtf8.LATIN_CAPITAL_LETTER_O_WITH_DIAERESIS,
  b'\xc3\x97': entities.EntUtf8.MULTIPLICATION_SIGN,
  b'\xc3\x98': entities.EntUtf8.LATIN_CAPITAL_LETTER_O_WITH_STROKE,
  b'\xc3\x99': entities.EntUtf8.LATIN_CAPITAL_LETTER_U_WITH_GRAVE,
  b'\xc3\x9a': entities.EntUtf8.LATIN_CAPITAL_LETTER_U_WITH_ACUTE,
  b'\xc3\x9b': entities.EntUtf8.LATIN_CAPITAL_LETTER_U_WITH_CIRCUMFLEX,
  b'\xc3\x9c': entities.EntUtf8.LATIN_CAPITAL_LETTER_U_WITH_DIAERESIS,
  b'\xc3\x9d': entities.EntUtf8.LATIN_CAPITAL_LETTER_Y_WITH_ACUTE,
  b'\xc3\x9e': entities.EntUtf8.LATIN_CAPITAL_LETTER_THORN,
  b'\xc3\x9f': entities.EntUtf8.LATIN_SMALL_LETTER_SHARP_S,
  b'\xc3\xa0': entities.EntUtf8.LATIN_SMALL_LETTER_A_WITH_GRAVE,
  b'\xc3\xa1': entities.EntUtf8.LATIN_SMALL_LETTER_A_WITH_ACUTE,
  b'\xc3\xa2': entities.EntUtf8.LATIN_SMALL_LETTER_A_WITH_CIRCUMFLEX,
  b'\xc3\xa3': entities.EntUtf8.LATIN_SMALL_LETTER_A_WITH_TILDE,
  b'\xc3\xa4': entities.EntUtf8.LATIN_SMALL_LETTER_A_WITH_DIAERESIS,
  b'\xc3\xa5': entities.EntUtf8.LATIN_SMALL_LETTER_A_WITH_RING_ABOVE,
  b'\xc3\xa6': entities.EntUtf8.LATIN_SMALL_LETTER_AE,
  b'\xc3\xa7': entities.EntUtf8.LATIN_SMALL_LETTER_C_WITH_CEDILLA,
  b'\xc3\xa8': entities.EntUtf8.LATIN_SMALL_LETTER_E_WITH_GRAVE,
  b'\xc3\xa9': entities.EntUtf8.LATIN_SMALL_LETTER_E_WITH_ACUTE,
  b'\xc3\xaa': entities.EntUtf8.LATIN_SMALL_LETTER_E_WITH_CIRCUMFLEX,
  b'\xc3\xab': entities.EntUtf8.LATIN_SMALL_LETTER_E_WITH_DIAERESIS,
  b'\xc3\xac': entities.EntUtf8.LATIN_SMALL_LETTER_I_WITH_GRAVE,
  b'\xc3\xad': entities.EntUtf8.LATIN_SMALL_LETTER_I_WITH_ACUTE,
  b'\xc3\xae': entities.EntUtf8.LATIN_SMALL_LETTER_I_WITH_CIRCUMFLEX,
  b'\xc3\xaf': entities.EntUtf8.LATIN_SMALL_LETTER_I_WITH_DIAERESIS,
  b'\xc3\xb0': entities.EntUtf8.LATIN_SMALL_LETTER_ETH,
  b'\xc3\xb1': entities.EntUtf8.LATIN_SMALL_LETTER_N_WITH_TILDE,
  b'\xc3\xb2': entities.EntUtf8.LATIN_SMALL_LETTER_O_WITH_GRAVE,
  b'\xc3\xb3': entities.EntUtf8.LATIN_SMALL_LETTER_O_WITH_ACUTE,
  b'\xc3\xb4': entities.EntUtf8.LATIN_SMALL_LETTER_O_WITH_CIRCUMFLEX,
  b'\xc3\xb5': entities.EntUtf8.LATIN_SMALL_LETTER_O_WITH_TILDE,
  b'\xc3\xb6': entities.EntUtf8.LATIN_SMALL_LETTER_O_WITH_DIAERESIS,
  b'\xc3\xb7': entities.EntUtf8.DIVISION_SIGN,
  b'\xc3\xb8': entities.EntUtf8.LATIN_SMALL_LETTER_O_WITH_STROKE,
  b'\xc3\xb9': entities.EntUtf8.LATIN_SMALL_LETTER_U_WITH_GRAVE,
  b'\xc3\xba': entities.EntUtf8.LATIN_SMALL_LETTER_U_WITH_ACUTE,
  b'\xc3\xbb': entities.EntUtf8.LATIN_SMALL_LETTER_U_WITH_CIRCUMFLEX,
  b'\xc3\xbc': entities.EntUtf8.LATIN_SMALL_LETTER_U_WITH_DIAERESIS,
  b'\xc3\xbd': entities.EntUtf8.LATIN_SMALL_LETTER_Y_WITH_ACUTE,
  b'\xc3\xbe': entities.EntUtf8.LATIN_SMALL_LETTER_THORN,
  b'\xc3\xbf': entities.EntUtf8.LATIN_SMALL_LETTER_Y_WITH_DIAERESIS,
  b'\xe2\x80\x94': entities.EntUtf8.EM_DASH,

}


WINDOWS_1252_TO_UTF8 = {
    0x80: b'\xe2\x82\xac', # â‚¬
    0x82: b'\xe2\x80\x9a', # â€š
    0x83: b'\xc6\x92',     # Æ’
    0x84: b'\xe2\x80\x9e', # â€ž
    0x85: b'\xe2\x80\xa6', # â€¦
    0x86: b'\xe2\x80\xa0', # â€
    0x87: b'\xe2\x80\xa1', # â€¡
    0x88: b'\xcb\x86',     # Ë†
    0x89: b'\xe2\x80\xb0', # â€°
    0x8a: b'\xc5\xa0',     # Å
    0x8b: b'\xe2\x80\xb9', # â€¹
    0x8c: b'\xc5\x92',     # Å’
    0x8e: b'\xc5\xbd',     # Å½
    0x91: b'\xe2\x80\x98', # â€˜
    0x92: b'\xe2\x80\x99', # â€™
    0x93: b'\xe2\x80\x9c', # â€œ
    0x94: b'\xe2\x80\x9d', # â€
    0x95: b'\xe2\x80\xa2', # â€¢
    0x96: b'\xe2\x80\x93', # â€“
    0x97: b'\xe2\x80\x94', # â€”
    0x98: b'\xcb\x9c',     # Ëœ
    0x99: b'\xe2\x84\xa2', # â„¢
    0x9a: b'\xc5\xa1',     # Å¡
    0x9b: b'\xe2\x80\xba', # â€º
    0x9c: b'\xc5\x93',     # Å“
    0x9e: b'\xc5\xbe',     # Å¾
    0x9f: b'\xc5\xb8',     # Å¸
    0xa0: b'\xc2\xa0',     # Â
    0xa1: b'\xc2\xa1',     # Â¡
    0xa2: b'\xc2\xa2',     # Â¢
    0xa3: b'\xc2\xa3',     # Â£
    0xa4: b'\xc2\xa4',     # Â¤
    0xa5: b'\xc2\xa5',     # Â¥
    0xa6: b'\xc2\xa6',     # Â¦
    0xa7: b'\xc2\xa7',     # Â§
    0xa8: b'\xc2\xa8',     # Â¨
    0xa9: b'\xc2\xa9',     # Â©
    0xaa: b'\xc2\xaa',     # Âª
    0xab: b'\xc2\xab',     # Â«
    0xac: b'\xc2\xac',     # Â¬
    0xad: b'\xc2\xad',     # Â­
    0xae: b'\xc2\xae',     # Â®
    0xaf: b'\xc2\xaf',     # Â¯
    0xb0: b'\xc2\xb0',     # Â°
    0xb1: b'\xc2\xb1',     # Â±
    0xb2: b'\xc2\xb2',     # Â²
    0xb3: b'\xc2\xb3',     # Â³
    0xb4: b'\xc2\xb4',     # Â´
    0xb5: b'\xc2\xb5',     # Âµ
    0xb6: b'\xc2\xb6',     # Â¶
    0xb7: b'\xc2\xb7',     # Â·
    0xb8: b'\xc2\xb8',     # Â¸
    0xb9: b'\xc2\xb9',     # Â¹
    0xba: b'\xc2\xba',     # Âº
    0xbb: b'\xc2\xbb',     # Â»
    0xbc: b'\xc2\xbc',     # Â¼
    0xbd: b'\xc2\xbd',     # Â½
    0xbe: b'\xc2\xbe',     # Â¾
    0xbf: b'\xc2\xbf',     # Â¿
    0xc0: b'\xc3\x80',     # Ã€
    0xc1: b'\xc3\x81',     # Ã
    0xc2: b'\xc3\x82',     # Ã‚
    0xc3: b'\xc3\x83',     # Ãƒ
    0xc4: b'\xc3\x84',     # Ã„
    0xc5: b'\xc3\x85',     # Ã…
    0xc6: b'\xc3\x86',     # Ã†
    0xc7: b'\xc3\x87',     # Ã‡
    0xc8: b'\xc3\x88',     # Ãˆ
    0xc9: b'\xc3\x89',     # Ã‰
    0xca: b'\xc3\x8a',     # ÃŠ
    0xcb: b'\xc3\x8b',     # Ã‹
    0xcc: b'\xc3\x8c',     # ÃŒ
    0xcd: b'\xc3\x8d',     # Ã
    0xce: b'\xc3\x8e',     # ÃŽ
    0xcf: b'\xc3\x8f',     # Ã
    0xd0: b'\xc3\x90',     # Ã
    0xd1: b'\xc3\x91',     # Ã‘
    0xd2: b'\xc3\x92',     # Ã’
    0xd3: b'\xc3\x93',     # Ã“
    0xd4: b'\xc3\x94',     # Ã”
    0xd5: b'\xc3\x95',     # Ã•
    0xd6: b'\xc3\x96',     # Ã–
    0xd7: b'\xc3\x97',     # Ã—
    0xd8: b'\xc3\x98',     # Ã˜
    0xd9: b'\xc3\x99',     # Ã™
    0xda: b'\xc3\x9a',     # Ãš
    0xdb: b'\xc3\x9b',     # Ã›
    0xdc: b'\xc3\x9c',     # Ãœ
    0xdd: b'\xc3\x9d',     # Ã
    0xde: b'\xc3\x9e',     # Ãž
    0xdf: b'\xc3\x9f',     # ÃŸ
    0xe0: b'\xc3\xa0',     # Ã
    0xe1: b'\xa1',     # Ã¡
    0xe2: b'\xc3\xa2',     # Ã¢
    0xe3: b'\xc3\xa3',     # Ã£
    0xe4: b'\xc3\xa4',     # Ã¤
    0xe5: b'\xc3\xa5',     # Ã¥
    0xe6: b'\xc3\xa6',     # Ã¦
    0xe7: b'\xc3\xa7',     # Ã§
    0xe8: b'\xc3\xa8',     # Ã¨
    0xe9: b'\xc3\xa9',     # Ã©
    0xea: b'\xc3\xaa',     # Ãª
    0xeb: b'\xc3\xab',     # Ã«
    0xec: b'\xc3\xac',     # Ã¬
    0xed: b'\xc3\xad',     # Ã­
    0xee: b'\xc3\xae',     # Ã®
    0xef: b'\xc3\xaf',     # Ã¯
    0xf0: b'\xc3\xb0',     # Ã°
    0xf1: b'\xc3\xb1',     # Ã±
    0xf2: b'\xc3\xb2',     # Ã²
    0xf3: b'\xc3\xb3',     # Ã³
    0xf4: b'\xc3\xb4',     # Ã´
    0xf5: b'\xc3\xb5',     # Ãµ
    0xf6: b'\xc3\xb6',     # Ã¶
    0xf7: b'\xc3\xb7',     # Ã·
    0xf8: b'\xc3\xb8',     # Ã¸
    0xf9: b'\xc3\xb9',     # Ã¹
    0xfa: b'\xc3\xba',     # Ãº
    0xfb: b'\xc3\xbb',     # Ã»
    0xfc: b'\xc3\xbc',     # Ã¼
    0xfd: b'\xc3\xbd',     # Ã½
    0xfe: b'\xc3\xbe',     # Ã¾
    }


class PyExt(object):
  class __internal(object):
    _props = {}

  def __init__(self, report=None):
    self._report = report if report is not None else self.__internal()
    self.hash = PyHash.SipHash().hashId
    self.today = self.dates.today
    self.now = self.dates.now
    self.cob = self.dates.cob
    self.request = self.requests.request
    if 'py' not in self._report._props:
      self._report._props['py'] = {}

  @property
  def dates(self):
    """
    Description:
    ------------
    This is a simple wrapper to the datetime Python module.

    No external package is required to use this interface.

    Usage:
    -----

    :return: A PyDate object
    """
    return PyDates.PyDates(self._report)

  @property
  def requests(self):
    """
    Description:
    ------------
    This is a simple wrapper to the internal Python modules to run REST calls.

    No external package is required to use this interface.

    Usage:
    -----

    :return: A PyRest object
    """
    return PyRest.PyRest(self._report)

  @property
  def crypto(self):
    """
    Description:
    ------------
    Property to the internal cryptography module.

    This will rely on the package cryptography. This should be added to the python environment before using it.
    This package can be installed using the usual pip install function.

    Usage:
    -----

    Related Pages:

      https://pypi.org/project/cryptography/
      https://cryptography.io/en/latest/
    """
    return PyCrypto.PyCrypto(self._report)

  @property
  def geo(self):
    """
    Description:
    ------------
    Property to some predefined Geolocation functions

    Usage:
    -----

    """
    return PyGeo.PyGeo(self._report)

  @property
  def markdown(self):
    """
    Description:
    ------------
    Property to the Markdown String conversion

    Usage:
    -----

    """
    return PyMarkdown.MarkDown(self._report)

  def import_lib(self, lib_name, folder="libs", report_name=None, path=None):
    """
    Description:
    ------------
    Import dynamically a python module.

    Usage:
    -----------

      page.py.import_lib("test.py", folder="tables", path=r"filePath")

    Attributes:
    ----------
    :param lib_name: The python module name
    :param folder: The internal folder with the libraries to be imported
    :param report_name: Optional, the report name in which the library is defined. Default current folder
    :param path: Optional, the path to be added to the classpath

    :return: The imported Python module
    """
    lib_name = lib_name.replace(".py", "")
    if path is not None:
      if path not in sys.path:
        sys.path.append(path)
      return importlib.import_module('%s.%s' % (folder, lib_name))

    else:
      if report_name is None:
        return importlib.import_module('%s.%s.%s' % (self._report.run.report_name, folder, lib_name))

      return importlib.import_module('%s.%s.%s' % (report_name, folder, lib_name))

  def import_package(self, package, sub_module=None):
    """
    Description:
    ------------
    Install the external Python package.
    This can automatically installed it from the Python Index online repository is missing

    Usage:
    -----

      >>> PyExt().import_package("sqlalchemy").__name__
      'sqlalchemy'

    Attributes:
    ----------
    :param package: The Python Package Name
    :param sub_module: The sub module or class within the package

    :return: The installed Python module
    """
    package_alias = "%s_%s" % (package, sub_module) if sub_module is not None else package
    if not package_alias in self._report._props:
      self._report._props[package_alias] = requires(package, reason='Missing Package', package=sub_module, install=package)
    return self._report._props[package_alias]

  @staticmethod
  def encode_html(text, encoding="utf-8"):
    """
    Description:
    ------------

    Usage:
    -----


    Attributes:
    ----------
    :param text: String. a test to encode with HTML special symbols
    :param encoding: String. teh encoding type
    """
    if not isinstance(text, str):
      return text

    if encoding.lower() not in ["utf-8", 'cp1252']:
      raise Exception("Only Windows-1252 and UTF-8 are supported")

    text = bytes(text, encoding)
    endcoding_map = UTF8_TO_HTML if encoding.lower() == "utf-8" else WINDOWS_1252_TO_UTF8
    for k, v in endcoding_map.items():
      text = text.replace(k, bytes(v, encoding))
    return text.decode(encoding)

  @staticmethod
  def format_number(value, digits=0, thousand_sep=",", decimal_sep="."):
    """
    Description:
    ------------

    Usage:
    -----


    Attributes:
    ----------
    :param value:
    :param digits:
    :param thousand_sep:
    :param decimal_sep:
    """
    text = "%.2f" % round(value, digits)
    if decimal_sep in text:
      e, d = text.split(decimal_sep)
    else:
      e, d = text, ""

    r = []
    for i, c in enumerate(e[::-1]):
      if i > 0 and i % 3 == 0:
        r.append(thousand_sep)
      r.append(c)
    if not digits:
      return "".join(reversed(r))

    return "%s%s%s" % ("".join(reversed(r)), decimal_sep, d[:digits])

  @staticmethod
  def format_money(text, digits=0, thousand_sep=",", decimal_sep=".", symbol="£", format="%s%v"):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param text:
    :param digits:
    :param thousand_sep:
    :param decimal_sep:
    :param symbol:
    :param format:
    """
    text = PyExt.format_number(text, digits, thousand_sep, decimal_sep)
    if symbol not in ["£"]:
      format = "%v %s"
    conv_format = format.replace("%s", "%(text)s").replace("%v", "%(value)s")
    return conv_format % {"text": PyExt.encode_html(symbol), 'value': text}
