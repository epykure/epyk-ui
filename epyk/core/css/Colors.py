"""
Mapping table for the pre defined HTML colors

Related Pages:

      https://www.rapidtables.com/web/color/RGB_Color.html
"""

import random
import math


defined = {
  'MAROON': {'hex': '#800000', 'rgb': '(128,0,0)'},
  'DARK RED': {'hex': '#8B0000', 'rgb': '(139,0,0)'},
  'BROWN': {'hex': '#A52A2A', 'rgb': '(165,42,42)'},
  'FIREBRICK': {'hex': '#B22222', 'rgb': '(178,34,34)'},
  'CRIMSON': {'hex': '#DC143C', 'rgb': '(220,20,60)'},
  'RED': {'hex': '#FF0000', 'rgb': '(255,0,0)'},
  'TOMATO': {'hex': '#FF6347', 'rgb': '(255,99,71)'},
  'CORAL': {'hex': '#FF7F50', 'rgb': '(255,127,80)'},
  'INDIAN RED': {'hex': '#CD5C5C', 'rgb': '(205,92,92)'},
  'LIGHT CORAL': {'hex': '#F08080', 'rgb': '(240,128,128)'},
  'DARK SALMON': {'hex': '#E9967A', 'rgb': '(233,150,122)'},
  'SALMON': {'hex': '#FA8072', 'rgb': '(250,128,114)'},
  'LIGHT SALMON': {'hex': '#FFA07A', 'rgb': '(255,160,122)'},
  'ORANGE RED': {'hex': '#FF4500', 'rgb': '(255,69,0)'},
  'DARK ORANGE': {'hex': '#FF8C00', 'rgb': '(255,140,0)'},
  'ORANGE': {'hex': '#FFA500', 'rgb': '(255,165,0)'},
  'GOLD': {'hex': '#FFD700', 'rgb': '(255,215,0)'},
  'DARK GOLDEN ROD': {'hex': '#B8860B', 'rgb': '(184,134,11)'},
  'GOLDEN ROD': {'hex': '#DAA520', 'rgb': '(218,165,32)'},
  'PALE GOLDEN ROD': {'hex': '#EEE8AA', 'rgb': '(238,232,170)'},
  'DARK KHAKI': {'hex': '#BDB76B', 'rgb': '(189,183,107)'},
  'KHAKI': {'hex': '#F0E68C', 'rgb': '(240,230,140)'},
  'OLIVE': {'hex': '#808000', 'rgb': '(128,128,0)'},
  'YELLOW': {'hex': '#FFFF00', 'rgb': '(255,255,0)'},
  'YELLOW GREEN': {'hex': '#9ACD32', 'rgb': '(154,205,50)'},
  'DARK OLIVE GREEN': {'hex': '#556B2F', 'rgb': '(85,107,47)'},
  'OLIVE DRAB': {'hex': '#6B8E23', 'rgb': '(107,142,35)'},
  'LAWN GREEN': {'hex': '#7CFC00', 'rgb': '(124,252,0)'},
  'CHART REUSE': {'hex': '#7FFF00', 'rgb': '(127,255,0)'},
  'GREEN YELLOW': {'hex': '#ADFF2F', 'rgb': '(173,255,47)'},
  'DARK GREEN': {'hex': '#006400', 'rgb': '(0,100,0)'},
  'GREEN': {'hex': '#008000', 'rgb': '(0,128,0)'},
  'FOREST GREEN': {'hex': '#228B22', 'rgb': '(34,139,34)'},
  'LIME': {'hex': '#00FF00', 'rgb': '(0,255,0)'},
  'LIME GREEN': {'hex': '#32CD32', 'rgb': '(50,205,50)'},
  'LIGHT GREEN': {'hex': '#90EE90', 'rgb': '(144,238,144)'},
  'PALE GREEN': {'hex': '#98FB98', 'rgb': '(152,251,152)'},
  'DARK SEA GREEN': {'hex': '#8FBC8F', 'rgb': '(143,188,143)'},
  'MEDIUM SPRING GREEN': {'hex': '#00FA9A', 'rgb': '(0,250,154)'},
  'SPRING GREEN': {'hex': '#00FF7F', 'rgb': '(0,255,127)'},
  'SEA GREEN': {'hex': '#2E8B57', 'rgb': '(46,139,87)'},
  'MEDIUM AQUA MARINE': {'hex': '#66CDAA', 'rgb': '(102,205,170)'},
  'MEDIUM SEA GREEN': {'hex': '#3CB371', 'rgb': '(60,179,113)'},
  'LIGHT SEA GREEN': {'hex': '#20B2AA', 'rgb': '(32,178,170)'},
  'DARK SLATE GRAY': {'hex': '#2F4F4F', 'rgb': '(47,79,79)'},
  'TEAL': {'hex': '#008080', 'rgb': '(0,128,128)'},
  'DARK CYAN': {'hex': '#008B8B', 'rgb': '(0,139,139)'},
  'AQUA': {'hex': '#00FFFF', 'rgb': '(0,255,255)'},
  'CYAN': {'hex': '#00FFFF', 'rgb': '(0,255,255)'},
  'LIGHT CYAN': {'hex': '#E0FFFF', 'rgb': '(224,255,255)'},
  'DARK TURQUOISE': {'hex': '#00CED1', 'rgb': '(0,206,209)'},
  'TURQUOISE': {'hex': '#40E0D0', 'rgb': '(64,224,208)'},
  'MEDIUM TURQUOISE': {'hex': '#48D1CC', 'rgb': '(72,209,204)'},
  'PALE TURQUOISE': {'hex': '#AFEEEE', 'rgb': '(175,238,238)'},
  'AQUA MARINE': {'hex': '#7FFFD4', 'rgb': '(127,255,212)'},
  'POWDER BLUE': {'hex': '#B0E0E6', 'rgb': '(176,224,230)'},
  'CADET BLUE': {'hex': '#5F9EA0', 'rgb': '(95,158,160)'},
  'STEEL BLUE': {'hex': '#4682B4', 'rgb': '(70,130,180)'},
  'CORN FLOWER BLUE': {'hex': '#6495ED', 'rgb': '(100,149,237)'},
  'DEEP SKY BLUE': {'hex': '#00BFFF', 'rgb': '(0,191,255)'},
  'DODGER BLUE': {'hex': '#1E90FF', 'rgb': '(30,144,255)'},
  'LIGHT BLUE': {'hex': '#ADD8E6', 'rgb': '(173,216,230)'},
  'SKY BLUE': {'hex': '#87CEEB', 'rgb': '(135,206,235)'},
  'LIGHT SKY BLUE': {'hex': '#87CEFA', 'rgb': '(135,206,250)'},
  'MIDNIGHT BLUE': {'hex': '#191970', 'rgb': '(25,25,112)'},
  'NAVY': {'hex': '#000080', 'rgb': '(0,0,128)'},
  'DARK BLUE': {'hex': '#00008B', 'rgb': '(0,0,139)'},
  'MEDIUM BLUE': {'hex': '#0000CD', 'rgb': '(0,0,205)'},
  'BLUE': {'hex': '#0000FF', 'rgb': '(0,0,255)'},
  'ROYAL BLUE': {'hex': '#4169E1', 'rgb': '(65,105,225)'},
  'BLUE VIOLET': {'hex': '#8A2BE2', 'rgb': '(138,43,226)'},
  'INDIGO': {'hex': '#4B0082', 'rgb': '(75,0,130)'},
  'DARK SLATE BLUE': {'hex': '#483D8B', 'rgb': '(72,61,139)'},
  'SLATE BLUE': {'hex': '#6A5ACD', 'rgb': '(106,90,205)'},
  'MEDIUM SLATE BLUE': {'hex': '#7B68EE', 'rgb': '(123,104,238)'},
  'MEDIUM PURPLE': {'hex': '#9370DB', 'rgb': '(147,112,219)'},
  'DARK MAGENTA': {'hex': '#8B008B', 'rgb': '(139,0,139)'},
  'DARK VIOLET': {'hex': '#9400D3', 'rgb': '(148,0,211)'},
  'DARK ORCHID': {'hex': '#9932CC', 'rgb': '(153,50,204)'},
  'MEDIUM ORCHID': {'hex': '#BA55D3', 'rgb': '(186,85,211)'},
  'PURPLE': {'hex': '#800080', 'rgb': '(128,0,128)'},
  'THISTLE': {'hex': '#D8BFD8', 'rgb': '(216,191,216)'},
  'PLUM': {'hex': '#DDA0DD', 'rgb': '(221,160,221)'},
  'VIOLET': {'hex': '#EE82EE', 'rgb': '(238,130,238)'},
  'MAGENTA / FUCHSIA': {'hex': '#FF00FF', 'rgb': '(255,0,255)'},
  'ORCHID': {'hex': '#DA70D6', 'rgb': '(218,112,214)'},
  'MEDIUM VIOLET RED': {'hex': '#C71585', 'rgb': '(199,21,133)'},
  'PALE VIOLET RED': {'hex': '#DB7093', 'rgb': '(219,112,147)'},
  'DEEP PINK': {'hex': '#FF1493', 'rgb': '(255,20,147)'},
  'HOT PINK': {'hex': '#FF69B4', 'rgb': '(255,105,180)'},
  'LIGHT PINK': {'hex': '#FFB6C1', 'rgb': '(255,182,193)'},
  'PINK': {'hex': '#FFC0CB', 'rgb': '(255,192,203)'},
  'ANTIQUE WHITE': {'hex': '#FAEBD7', 'rgb': '(250,235,215)'},
  'BEIGE': {'hex': '#F5F5DC', 'rgb': '(245,245,220)'},
  'BISQUE': {'hex': '#FFE4C4', 'rgb': '(255,228,196)'},
  'BLANCHED ALMOND': {'hex': '#FFEBCD', 'rgb': '(255,235,205)'},
  'WHEAT': {'hex': '#F5DEB3', 'rgb': '(245,222,179)'},
  'CORN SILK': {'hex': '#FFF8DC', 'rgb': '(255,248,220)'},
  'LEMON CHIFFON': {'hex': '#FFFACD', 'rgb': '(255,250,205)'},
  'LIGHT GOLDEN ROD YELLOW': {'hex': '#FAFAD2', 'rgb': '(250,250,210)'},
  'LIGHT YELLOW': {'hex': '#FFFFE0', 'rgb': '(255,255,224)'},
  'SADDLE BROWN': {'hex': '#8B4513', 'rgb': '(139,69,19)'},
  'SIENNA': {'hex': '#A0522D', 'rgb': '(160,82,45)'},
  'CHOCOLATE': {'hex': '#D2691E', 'rgb': '(210,105,30)'},
  'PERU': {'hex': '#CD853F', 'rgb': '(205,133,63)'},
  'SANDY BROWN': {'hex': '#F4A460', 'rgb': '(244,164,96)'},
  'BURLY WOOD': {'hex': '#DEB887', 'rgb': '(222,184,135)'},
  'TAN': {'hex': '#D2B48C', 'rgb': '(210,180,140)'},
  'ROSY BROWN': {'hex': '#BC8F8F', 'rgb': '(188,143,143)'},
  'MOCCASIN': {'hex': '#FFE4B5', 'rgb': '(255,228,181)'},
  'NAVAJO WHITE': {'hex': '#FFDEAD', 'rgb': '(255,222,173)'},
  'PEACH PUFF': {'hex': '#FFDAB9', 'rgb': '(255,218,185)'},
  'MISTY ROSE': {'hex': '#FFE4E1', 'rgb': '(255,228,225)'},
  'LAVENDER BLUSH': {'hex': '#FFF0F5', 'rgb': '(255,240,245)'},
  'LINEN': {'hex': '#FAF0E6', 'rgb': '(250,240,230)'},
  'OLD LACE': {'hex': '#FDF5E6', 'rgb': '(253,245,230)'},
  'PAPAYA WHIP': {'hex': '#FFEFD5', 'rgb': '(255,239,213)'},
  'SEA SHELL': {'hex': '#FFF5EE', 'rgb': '(255,245,238)'},
  'MINT CREAM': {'hex': '#F5FFFA', 'rgb': '(245,255,250)'},
  'SLATE GRAY': {'hex': '#708090', 'rgb': '(112,128,144)'},
  'LIGHT SLATE GRAY': {'hex': '#778899', 'rgb': '(119,136,153)'},
  'LIGHT STEEL BLUE': {'hex': '#B0C4DE', 'rgb': '(176,196,222)'},
  'LAVENDER': {'hex': '#E6E6FA', 'rgb': '(230,230,250)'},
  'FLORAL WHITE': {'hex': '#FFFAF0', 'rgb': '(255,250,240)'},
  'ALICE BLUE': {'hex': '#F0F8FF', 'rgb': '(240,248,255)'},
  'GHOST WHITE': {'hex': '#F8F8FF', 'rgb': '(248,248,255)'},
  'HONEYDEW': {'hex': '#F0FFF0', 'rgb': '(240,255,240)'},
  'IVORY': {'hex': '#FFFFF0', 'rgb': '(255,255,240)'},
  'AZURE': {'hex': '#F0FFFF', 'rgb': '(240,255,255)'},
  'SNOW': {'hex': '#FFFAFA', 'rgb': '(255,250,250)'},
  'BLACK': {'hex': '#000000', 'rgb': '(0,0,0)'},
  'DIM GRAY / DIM GREY': {'hex': '#696969', 'rgb': '(105,105,105)'},
  'GRAY / GREY': {'hex': '#808080', 'rgb': '(128,128,128)'},
  'DARK GRAY / DARK GREY': {'hex': '#A9A9A9', 'rgb': '(169,169,169)'},
  'SILVER': {'hex': '#C0C0C0', 'rgb': '(192,192,192)'},
  'LIGHT GRAY / LIGHT GREY': {'hex': '#D3D3D3', 'rgb': '(211,211,211)'},
  'GAINSBORO': {'hex': '#DCDCDC', 'rgb': '(220,220,220)'},
  'WHITE SMOKE': {'hex': '#F5F5F5', 'rgb': '(245,245,245)'},
  'WHITE': {'hex': '#FFFFFF', 'rgb': '(255,255,255)'},
}


def getHexToRgb(hexColor):
  """
  Description:
  ------------
  Convert a hexadecimal color to a rgb code

  An RGB color value is specified with the rgb() function, which has the following syntax:
  rgb(red, green, blue)
  Each parameter (red, green, and blue) defines the intensity of the color and can be an integer between 0 and 255 or a percentage value (from 0% to 100%).
  For example, the rgb(0,0,255) value is rendered as blue, because the blue parameter is set to its highest value (255) and the others are set to 0.
  Also, the following values define equal color: rgb(0,0,255) and rgb(0%,0%,100%).

  Usage::

      ColorMaker().getHexToRgb('#213B68')
  [33, 59, 104]

  Related Pages:

      https://www.w3schools.com/cssref/css_colors_legal.asp

  Attributes:
  ----------
  :param hexColor: A String with a hexadecimal code color

  :return: The list with the rgb code color
  """
  if not hexColor.startswith("#"):
    raise Exception("Hexadecimal color should start with #")

  if not len(hexColor) == 7:
    raise Exception("Color should have a length of 7")

  return [int(hexColor[1:3], 16), int(hexColor[3:5], 16), int(hexColor[5:7], 16)]


def rgba(red, green, blue, alpha):
  """
  Description:
  -----------
  RGBA color values are an extension of RGB color values with an alpha channel - which specifies the opacity of the object.

  An RGBA color is specified with the rgba() function, which has the following syntax:
  rgba(red, green, blue, alpha)
  The alpha parameter is a number between 0.0 (fully transparent) and 1.0 (fully opaque).

  Related Pages:

      https://www.w3schools.com/cssref/css_colors_legal.asp

  Attributes:
  ----------
  :param red:
  :param green:
  :param blue:
  :param alpha:
  """
  return "rgba(%s, %s, %s, %s)" % (red, green, blue, alpha)


def getRgbToHex(rgbColor):
  """
  Description:
  ------------
  Convert a RGB color to a hexadecimal code.

  Usage::

      >>> ColorMaker().getRgbToHex([255, 0, 0])
  '#ff0000'

  Attributes:
  ----------
  :param rgbColor: A list corresponding to the RGB color code

  :return: String object defining the hexadecimal color code
  """
  color = []
  for val in rgbColor:
    val = hex(int(val)).lstrip('0x')
    if len(val) != 2:
      leadingZeros = ["0"] * (2 - len(val))
      val = "%s%s" % ("".join(leadingZeros), val)
    color.append(val)
  return "#%s" % "".join(color)


def randColor(seedNo=None):
  """
  Description:
  ------------
  Generate a random hexadecimal color code.

  Usage::

      >>> ColorMaker.randColor(10)
  '#9693DD'

  Attributes:
  ----------
  :param seedNo: Optional, The seed number used to generate random numbers

  :return: String with Hexadecimal color code
  """
  letters = '0123456789ABCDEF'
  color = ['#']
  if seedNo is not None:
    random.seed(seedNo)
  for i in range(6):
    color.append(letters[math.floor(random.random() * 16)])
  if seedNo is not None:
    random.seed(None) # Resent the seed to None
  return "".join(color)


def gradient(start, end, factor):
  """
  Description:
  ------------
  Deduce the color from a factor in a range of colors.

  Usage::

      >>> ColorMaker().gradient("#ffffff", "#FF0000", 0.2)
  '#ffcccc'

  Attributes:
  ----------
  :param start: The start hexadecimal color code
  :param end: The end hexadecimal color code
  :param factor: A factor in the range [0, 1]

  :return: The hexadecimal color code
  """
  if factor > 1:
    raise Exception("Gradient factor must be <= 1")

  rgbEnd = getHexToRgb(end)
  rgbDiff = [(rgbEnd[i] - val) * factor + val for i, val in enumerate(getHexToRgb(start))]
  return getRgbToHex(rgbDiff)


def colors(start, end, steps):
  """
  Description:
  ------------
  Generate a list of colors between two color codes.

  Usage::

      >>> colors("#ffffff", "#FF0000", 10)
  ['#ffffff', '#ffe2e2', '#ffc6c6', '#ffaaaa', '#ff8d8d', '#ff7171', '#ff5555', '#ff3838', '#ff1c1c', '#FF0000']

  Attributes:
  ----------
  :param start: The start hexadecimal color code
  :param end: The end hexadecimal color code
  :param steps: The number of colors in the array

  :return: A list of hexadecimal color codes
  """
  colors = [start]
  for i in range(steps-2):
    colors.append(gradient(start, end, 1.0 / (steps-1) * (i + 1)))
  colors.append(end)
  return colors


class HexColors(object):
  MAROON = '#800000'
  DARK_RED = '#8B0000'
  BROWN = '#A52A2A'
  FIREBRICK = '#B22222'
  CRIMSON = '#DC143C'
  RED = '#FF0000'
  TOMATO = '#FF6347'
  CORAL = '#FF7F50'
  INDIAN_RED = '#CD5C5C'
  LIGHT_CORAL = '#F08080'
  DARK_SALMON = '#E9967A'
  SALMON = '#FA8072'
  LIGHT_SALMON = '#FFA07A'
  ORANGE_RED = '#FF4500'
  DARK_ORANGE = '#FF8C00'
  ORANGE = '#FFA500'
  GOLD = '#FFD700'
  DARK_GOLDEN_ROD = '#B8860B'
  GOLDEN_ROD = '#DAA520'
  PALE_GOLDEN_ROD = '#EEE8AA'
  DARK_KHAKI = '#BDB76B'
  KHAKI = '#F0E68C'
  OLIVE = '#808000'
  YELLOW = '#FFFF00'
  YELLOW_GREEN = '#9ACD32'
  DARK_OLIVE_GREEN = '#556B2F'
  OLIVE_DRAB = '#6B8E23'
  LAWN_GREEN = '#7CFC00'
  CHART_REUSE = '#7FFF00'
  GREEN_YELLOW = '#ADFF2F'
  DARK_GREEN = '#006400'
  GREEN = '#008000'
  FOREST_GREEN = '#228B22'
  LIME = '#00FF00'
  LIME_GREEN = '#32CD32'
  LIGHT_GREEN = '#90EE90'
  PALE_GREEN = '#98FB98'
  DARK_SEA_GREEN = '#8FBC8F'
  MEDIUM_SPRING_GREEN = '#00FA9A'
  SPRING_GREEN = '#00FF7F'
  SEA_GREEN = '#2E8B57'
  MEDIUM_AQUA_MARINE = '#66CDAA'
  MEDIUM_SEA_GREEN = '#3CB371'
  LIGHT_SEA_GREEN = '#20B2AA'
  DARK_SLATE_GRAY = '#2F4F4F'
  TEAL = '#008080'
  DARK_CYAN = '#008B8B'
  AQUA = '#00FFFF'
  CYAN = '#00FFFF'
  LIGHT_CYAN = '#E0FFFF'
  DARK_TURQUOISE = '#00CED1'
  TURQUOISE = '#40E0D0'
  MEDIUM_TURQUOISE = '#48D1CC'
  PALE_TURQUOISE = '#AFEEEE'
  AQUA_MARINE = '#7FFFD4'
  POWDER_BLUE = '#B0E0E6'
  CADET_BLUE = '#5F9EA0'
  STEEL_BLUE = '#4682B4'
  CORN_FLOWER_BLUE = '#6495ED'
  DEEP_SKY_BLUE = '#00BFFF'
  DODGER_BLUE = '#1E90FF'
  LIGHT_BLUE = '#ADD8E6'
  SKY_BLUE = '#87CEEB'
  LIGHT_SKY_BLUE = '#87CEFA'
  MIDNIGHT_BLUE = '#191970'
  NAVY = '#000080'
  DARK_BLUE = '#00008B'
  MEDIUM_BLUE = '#0000CD'
  BLUE = '#0000FF'
  ROYAL_BLUE = '#4169E1'
  BLUE_VIOLET = '#8A2BE2'
  INDIGO = '#4B0082'
  DARK_SLATE_BLUE = '#483D8B'
  SLATE_BLUE = '#6A5ACD'
  MEDIUM_SLATE_BLUE = '#7B68EE'
  MEDIUM_PURPLE = '#9370DB'
  DARK_MAGENTA = '#8B008B'
  DARK_VIOLET = '#9400D3'
  DARK_ORCHID = '#9932CC'
  MEDIUM_ORCHID = '#BA55D3'
  PURPLE = '#800080'
  THISTLE = '#D8BFD8'
  PLUM = '#DDA0DD'
  VIOLET = '#EE82EE'
  ORCHID = '#DA70D6'
  MEDIUM_VIOLET_RED = '#C71585'
  PALE_VIOLET_RED = '#DB7093'
  DEEP_PINK = '#FF1493'
  HOT_PINK = '#FF69B4'
  LIGHT_PINK = '#FFB6C1'
  PINK = '#FFC0CB'
  ANTIQUE_WHITE = '#FAEBD7'
  BEIGE = '#F5F5DC'
  BISQUE = '#FFE4C4'
  BLANCHED_ALMOND = '#FFEBCD'
  WHEAT = '#F5DEB3'
  CORN_SILK = '#FFF8DC'
  LEMON_CHIFFON = '#FFFACD'
  LIGHT_GOLDEN_ROD_YELLOW = '#FAFAD2'
  LIGHT_YELLOW = '#FFFFE0'
  SADDLE_BROWN = '#8B4513'
  SIENNA = '#A0522D'
  CHOCOLATE = '#D2691E'
  PERU = '#CD853F'
  SANDY_BROWN = '#F4A460'
  BURLY_WOOD = '#DEB887'
  TAN = '#D2B48C'
  ROSY_BROWN = '#BC8F8F'
  MOCCASIN = '#FFE4B5'
  NAVAJO_WHITE = '#FFDEAD'
  PEACH_PUFF = '#FFDAB9'
  MISTY_ROSE = '#FFE4E1'
  LAVENDER_BLUSH = '#FFF0F5'
  LINEN = '#FAF0E6'
  OLD_LACE = '#FDF5E6'
  PAPAYA_WHIP = '#FFEFD5'
  SEA_SHELL = '#FFF5EE'
  MINT_CREAM = '#F5FFFA'
  SLATE_GRAY = '#708090'
  LIGHT_SLATE_GRAY = '#778899'
  LIGHT_STEEL_BLUE = '#B0C4DE'
  LAVENDER = '#E6E6FA'
  FLORAL_WHITE = '#FFFAF0'
  ALICE_BLUE = '#F0F8FF'
  GHOST_WHITE = '#F8F8FF'
  HONEYDEW = '#F0FFF0'
  IVORY = '#FFFFF0'
  AZURE = '#F0FFFF'
  SNOW = '#FFFAFA'
  BLACK = '#000000'
  SILVER = '#C0C0C0'
  GAINSBORO = '#DCDCDC'
  WHITE_SMOKE = '#F5F5F5'
  WHITE = '#FFFFFF'


class RgbColors(object):
  TRANSPARENT = "rgba(0, 0, 0, 0)"
  MAROON = 'rgb(128,0,0)'
  DARK_RED = 'rgb(139,0,0)'
  BROWN = 'rgb(165,42,42)'
  FIREBRICK = 'rgb(178,34,34)'
  CRIMSON = 'rgb(220,20,60)'
  RED = 'rgb(255,0,0)'
  TOMATO = 'rgb(255,99,71)'
  CORAL = 'rgb(255,127,80)'
  INDIAN_RED = 'rgb(205,92,92)'
  LIGHT_CORAL = 'rgb(240,128,128)'
  DARK_SALMON = 'rgb(233,150,122)'
  SALMON = 'rgb(250,128,114)'
  LIGHT_SALMON = 'rgb(255,160,122)'
  ORANGE_RED = 'rgb(255,69,0)'
  DARK_ORANGE = 'rgb(255,140,0)'
  ORANGE = 'rgb(255,165,0)'
  GOLD = 'rgb(255,215,0)'
  DARK_GOLDEN_ROD = 'rgb(184,134,11)'
  GOLDEN_ROD = 'rgb(218,165,32)'
  PALE_GOLDEN_ROD = 'rgb(238,232,170)'
  DARK_KHAKI = 'rgb(189,183,107)'
  KHAKI = 'rgb(240,230,140)'
  OLIVE = 'rgb(128,128,0)'
  YELLOW = 'rgb(255,255,0)'
  YELLOW_GREEN = 'rgb(154,205,50)'
  DARK_OLIVE_GREEN = 'rgb(85,107,47)'
  OLIVE_DRAB = 'rgb(107,142,35)'
  LAWN_GREEN = 'rgb(124,252,0)'
  CHART_REUSE = 'rgb(127,255,0)'
  GREEN_YELLOW = 'rgb(173,255,47)'
  DARK_GREEN = 'rgb(0,100,0)'
  GREEN = 'rgb(0,128,0)'
  FOREST_GREEN = 'rgb(34,139,34)'
  LIME = 'rgb(0,255,0)'
  LIME_GREEN = 'rgb(50,205,50)'
  LIGHT_GREEN = 'rgb(144,238,144)'
  PALE_GREEN = 'rgb(152,251,152)'
  DARK_SEA_GREEN = 'rgb(143,188,143)'
  MEDIUM_SPRING_GREEN = 'rgb(0,250,154)'
  SPRING_GREEN = 'rgb(0,255,127)'
  SEA_GREEN = 'rgb(46,139,87)'
  MEDIUM_AQUA_MARINE = 'rgb(102,205,170)'
  MEDIUM_SEA_GREEN = 'rgb(60,179,113)'
  LIGHT_SEA_GREEN = 'rgb(32,178,170)'
  DARK_SLATE_GRAY = 'rgb(47,79,79)'
  TEAL = 'rgb(0,128,128)'
  DARK_CYAN = 'rgb(0,139,139)'
  AQUA = 'rgb(0,255,255)'
  CYAN = 'rgb(0,255,255)'
  LIGHT_CYAN = 'rgb(224,255,255)'
  DARK_TURQUOISE = 'rgb(0,206,209)'
  TURQUOISE = 'rgb(64,224,208)'
  MEDIUM_TURQUOISE = 'rgb(72,209,204)'
  PALE_TURQUOISE = 'rgb(175,238,238)'
  AQUA_MARINE = 'rgb(127,255,212)'
  POWDER_BLUE = 'rgb(176,224,230)'
  CADET_BLUE = 'rgb(95,158,160)'
  STEEL_BLUE = 'rgb(70,130,180)'
  CORN_FLOWER_BLUE = 'rgb(100,149,237)'
  DEEP_SKY_BLUE = 'rgb(0,191,255)'
  DODGER_BLUE = 'rgb(30,144,255)'
  LIGHT_BLUE = 'rgb(173,216,230)'
  SKY_BLUE = 'rgb(135,206,235)'
  LIGHT_SKY_BLUE = 'rgb(135,206,250)'
  MIDNIGHT_BLUE = 'rgb(25,25,112)'
  NAVY = 'rgb(0,0,128)'
  DARK_BLUE = 'rgb(0,0,139)'
  MEDIUM_BLUE = 'rgb(0,0,205)'
  BLUE = 'rgb(0,0,255)'
  ROYAL_BLUE = 'rgb(65,105,225)'
  BLUE_VIOLET = 'rgb(138,43,226)'
  INDIGO = 'rgb(75,0,130)'
  DARK_SLATE_BLUE = 'rgb(72,61,139)'
  SLATE_BLUE = 'rgb(106,90,205)'
  MEDIUM_SLATE_BLUE = 'rgb(123,104,238)'
  MEDIUM_PURPLE = 'rgb(147,112,219)'
  DARK_MAGENTA = 'rgb(139,0,139)'
  DARK_VIOLET = 'rgb(148,0,211)'
  DARK_ORCHID = 'rgb(153,50,204)'
  MEDIUM_ORCHID = 'rgb(186,85,211)'
  PURPLE = 'rgb(128,0,128)'
  THISTLE = 'rgb(216,191,216)'
  PLUM = 'rgb(221,160,221)'
  VIOLET = 'rgb(238,130,238)'
  ORCHID = 'rgb(218,112,214)'
  MEDIUM_VIOLET_RED = 'rgb(199,21,133)'
  PALE_VIOLET_RED = 'rgb(219,112,147)'
  DEEP_PINK = 'rgb(255,20,147)'
  HOT_PINK = 'rgb(255,105,180)'
  LIGHT_PINK = 'rgb(255,182,193)'
  PINK = 'rgb(255,192,203)'
  ANTIQUE_WHITE = 'rgb(250,235,215)'
  BEIGE = 'rgb(245,245,220)'
  BISQUE = 'rgb(255,228,196)'
  BLANCHED_ALMOND = 'rgb(255,235,205)'
  WHEAT = 'rgb(245,222,179)'
  CORN_SILK = 'rgb(255,248,220)'
  LEMON_CHIFFON = 'rgb(255,250,205)'
  LIGHT_GOLDEN_ROD_YELLOW = 'rgb(250,250,210)'
  LIGHT_YELLOW = 'rgb(255,255,224)'
  SADDLE_BROWN = 'rgb(139,69,19)'
  SIENNA = 'rgb(160,82,45)'
  CHOCOLATE = 'rgb(210,105,30)'
  PERU = 'rgb(205,133,63)'
  SANDY_BROWN = 'rgb(244,164,96)'
  BURLY_WOOD = 'rgb(222,184,135)'
  TAN = 'rgb(210,180,140)'
  ROSY_BROWN = 'rgb(188,143,143)'
  MOCCASIN = 'rgb(255,228,181)'
  NAVAJO_WHITE = 'rgb(255,222,173)'
  PEACH_PUFF = 'rgb(255,218,185)'
  MISTY_ROSE = 'rgb(255,228,225)'
  LAVENDER_BLUSH = 'rgb(255,240,245)'
  LINEN = 'rgb(250,240,230)'
  OLD_LACE = 'rgb(253,245,230)'
  PAPAYA_WHIP = 'rgb(255,239,213)'
  SEA_SHELL = 'rgb(255,245,238)'
  MINT_CREAM = 'rgb(245,255,250)'
  SLATE_GRAY = 'rgb(112,128,144)'
  LIGHT_SLATE_GRAY = 'rgb(119,136,153)'
  LIGHT_STEEL_BLUE = 'rgb(176,196,222)'
  LAVENDER = 'rgb(230,230,250)'
  FLORAL_WHITE = 'rgb(255,250,240)'
  ALICE_BLUE = 'rgb(240,248,255)'
  GHOST_WHITE = 'rgb(248,248,255)'
  HONEYDEW = 'rgb(240,255,240)'
  IVORY = 'rgb(255,255,240)'
  AZURE = 'rgb(240,255,255)'
  SNOW = 'rgb(255,250,250)'
  BLACK = 'rgb(0,0,0)'
  SILVER = 'rgb(192,192,192)'
  GAINSBORO = 'rgb(220,220,220)'
  WHITE_SMOKE = 'rgb(245,245,245)'
  WHITE = 'rgb(255,255,255)'


class DefinedColors(object):

  @property
  def hex(self):
    """
    Description:
    ------------
    Returns the Hexadecimal predefined color codes

    Related Pages:

      https://www.rapidtables.com/web/color/RGB_Color.html
    """
    return HexColors

  @property
  def rgb(self):
    """
    Description:
    ------------
    Returns the RGB predefined color codes

    Related Pages:

      https://www.rapidtables.com/web/color/RGB_Color.html
    """
    return RgbColors

