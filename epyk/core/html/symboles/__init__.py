#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.symboles import SymbSmileys
from epyk.core.html.symboles import SymbHtml
from epyk.core.html.symboles import SymbArrows
from epyk.core.html.symboles import SymbCurrencies
from epyk.core.html.symboles import SymbLetters
from epyk.core.html.symboles import SymbEmojis
from epyk.core.html.symboles import SymbMaths
from epyk.core.html.symboles import SymbPunctuations
from epyk.core.html.symboles import SymbShapes


class Symboles(object):

  @property
  def shapes(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/charsets/ref_utf_geometric.asp
    """
    return SymbShapes

  @property
  def punctuations(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/charsets/ref_utf_punctuation.asp
    """
    return SymbPunctuations

  @property
  def maths(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/charsets/ref_utf_math.asp
    """
    return SymbMaths

  @property
  def emojis(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/charsets/ref_emoji.asp
    """
    return SymbEmojis

  @property
  def letters(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/charsets/ref_utf_letterlike.asp
    """
    return SymbLetters

  @property
  def currencies(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/charsets/ref_utf_currency.asp
    """
    return SymbCurrencies

  @property
  def smileys(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/charsets/ref_emoji_smileys.asp
    """
    return SymbSmileys

  @property
  def html(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/html/html_symbols.asp
      https://www.w3schools.com/charsets/ref_utf_math.asp
    """
    return SymbHtml

  @property
  def arrows(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/charsets/ref_utf_arrows.asp
    """
    return SymbArrows


if __name__ == '__main__':
  data = '''
†	dagger	02020	8224
ℸ	daleth	02138	8504
↡	Darr	021A1	8609
⇓	dArr	021D3	8659
↓	darr	02193	8595
‐	dash	02010	8208
⫤	Dashv	02AE4	10980
⊣	dashv	022A3	8867
⤏	dbkarow	0290F	10511
˝	dblac	002DD	733
Ď	Dcaron	0010E	270
ď	dcaron	0010F	271
Д	Dcy	00414	1044
д	dcy	00434	1076
ⅅ	DD	02145	8517
ⅆ	dd	02146	8518
‡	ddagger	02021	8225
⇊	ddarr	021CA	8650
⤑	DDotrahd	02911	10513
⩷	ddotseq	02A77	10871
°	deg	000B0	176
∇	Del	02207	8711
Δ	Delta	00394	916
δ	delta	003B4	948
⦱	demptyv	029B1	10673
⥿	dfisht	0297F	10623
𝔇	Dfr	1D507	120071
𝔡	dfr	1D521	120097
⥥	dHar	02965	10597
⇃	dharl	021C3	8643
⇂	dharr	021C2	8642
´	DiacriticalAcute	000B4	180
˙	DiacriticalDot	002D9	729
˝	DiacriticalDoubleAcute	002DD	733
`	DiacriticalGrave	00060	96
˜	DiacriticalTilde	002DC	732
⋄	diam	022C4	8900
⋄	Diamond	022C4	8900
⋄	diamond	022C4	8900
♦	diamondsuit	02666	9830
♦	diams	02666	9830
¨	die	000A8	168
ⅆ	DifferentialD	02146	8518
ϝ	digamma	003DD	989
⋲	disin	022F2	8946
÷	div	000F7	247
÷	divide	000F7	247
⋇	divideontimes	022C7	8903
⋇	divonx	022C7	8903
Ђ	DJcy	00402	1026
ђ	djcy	00452	1106
⌞	dlcorn	0231E	8990
⌍	dlcrop	0230D	8973
$	dollar	00024	36
𝔻	Dopf	1D53B	120123
𝕕	dopf	1D555	120149
¨	Dot	000A8	168
˙	dot	002D9	729
⃜	DotDot	020DC	8412
≐	doteq	02250	8784
≑	doteqdot	02251	8785
≐	DotEqual	02250	8784
∸	dotminus	02238	8760
∔	dotplus	02214	8724
⊡	dotsquare	022A1	8865
⌆	doublebarwedge	02306	8966
∯	DoubleContourIntegral	0222F	8751
¨	DoubleDot	000A8	168
⇓	DoubleDownArrow	021D3	8659
⇐	DoubleLeftArrow	021D0	8656
⇔	DoubleLeftRightArrow	021D4	8660
⫤	DoubleLeftTee	02AE4	10980
⟸	DoubleLongLeftArrow	027F8	10232
⟺	DoubleLongLeftRightArrow	027FA	10234
⟹	DoubleLongRightArrow	027F9	10233
⇒	DoubleRightArrow	021D2	8658
⊨	DoubleRightTee	022A8	8872
⇑	DoubleUpArrow	021D1	8657
⇕	DoubleUpDownArrow	021D5	8661
∥	DoubleVerticalBar	02225	8741
↓	DownArrow	02193	8595
⇓	Downarrow	021D3	8659
↓	downarrow	02193	8595
⤓	DownArrowBar	02913	10515
⇵	DownArrowUpArrow	021F5	8693
̑	DownBreve	00311	785
⇊	downdownarrows	021CA	8650
⇃	downharpoonleft	021C3	8643
⇂	downharpoonright	021C2	8642
⥐	DownLeftRightVector	02950	10576
⥞	DownLeftTeeVector	0295E	10590
↽	DownLeftVector	021BD	8637
⥖	DownLeftVectorBar	02956	10582
⥟	DownRightTeeVector	0295F	10591
⇁	DownRightVector	021C1	8641
⥗	DownRightVectorBar	02957	10583
⊤	DownTee	022A4	8868
↧	DownTeeArrow	021A7	8615
⤐	drbkarow	02910	10512
⌟	drcorn	0231F	8991
⌌	drcrop	0230C	8972
𝒟	Dscr	1D49F	119967
𝒹	dscr	1D4B9	119993
Ѕ	DScy	00405	1029
ѕ	dscy	00455	1109
⧶	dsol	029F6	10742
Đ	Dstrok	00110	272
đ	dstrok	00111	273
⋱	dtdot	022F1	8945
▿	dtri	025BF	9663
▾	dtrif	025BE	9662
⇵	duarr	021F5	8693
⥯	duhar	0296F	10607
⦦	dwangle	029A6	10662
Џ	DZcy	0040F	1039
џ	dzcy	0045F	1119
⟿	dzigrarr	027FF	10239
  '''

  for rec in data.split("\n"):
    split_line = rec.split("\t")
    if len(split_line) == 4:
      code = "&#%s" % split_line[3] if not split_line[3].startswith("&#") else split_line[3]
      print("%s = '%s'" % (split_line[1].strip().replace(" ", "_").replace("-", "_"), code))
    if len(split_line) > 4 and split_line[4].strip() != "":
      if split_line[1].endswith(";"):
        code = split_line[1]
      else:
        code = "&#%s" % split_line[1].strip() if not split_line[1].startswith("&#") else split_line[1].strip()
      if code == "&#" or code == '':
        continue

      names = split_line[4].split("=")
      for name in names:
        print("%s = '%s'" % (name.strip().replace(" ", "_").replace("-", "_").upper(), code))
