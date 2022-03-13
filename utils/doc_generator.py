
import os

FIELDS = {"default": "", "description": ""}
COLUMNS = ["label", "types", "default"]

DOC = '''

backgroundColor	Color	'rgba(0, 0, 0, 0.8)'	Background color of the tooltip.
titleColor	Color	'#fff'	Color of title text.
titleFont	Font	{weight: 'bold'}	See Fonts.
titleAlign	string	'left'	Horizontal alignment of the title text lines. more...
titleSpacing	number	2	Spacing to add to top and bottom of each title line.
titleMarginBottom	number	6	Margin to add on bottom of title section.
bodyColor	Color	'#fff'	Color of body text.
bodyFont	Font	{}	See Fonts.
bodyAlign	string	'left'	Horizontal alignment of the body text lines. more...
bodySpacing	number	2	Spacing to add to top and bottom of each tooltip item.
footerColor	Color	'#fff'	Color of footer text.
footerFont	Font	{weight: 'bold'}	See Fonts.
footerAlign	string	'left'	Horizontal alignment of the footer text lines. more...
footerSpacing	number	2	Spacing to add to top and bottom of each footer line.
footerMarginTop	number	6	Margin to add before drawing the footer.
padding	Padding	6	Padding inside the tooltip.
caretPadding	number	2	Extra distance to move the end of the tooltip arrow away from the tooltip point.
caretSize	number	5	Size, in px, of the tooltip arrow.
cornerRadius	number|object	6	Radius of tooltip corner curves.
multiKeyBackground	Color	'#fff'	Color to draw behind the colored boxes when multiple items are in the tooltip.
displayColors	boolean	TRUE	If true, color boxes are shown in the tooltip.
boxWidth	number	bodyFont.size	Width of the color box if displayColors is true.
boxHeight	number	bodyFont.size	Height of the color box if displayColors is true.
boxPadding	number	1	Padding between the color box and the text.
usePointStyle	boolean	FALSE	Use the corresponding point style (from dataset options) instead of color boxes, ex: star, triangle etc. (size is based on the minimum value between boxWidth and boxHeight).
borderColor	Color	'rgba(0, 0, 0, 0)'	Color of the border.
borderWidth	number	0	Size of the border.
rtl	boolean		true for rendering the tooltip from right to left.
textDirection	string	canvas' default	This will force the text direction 'rtl' or 'ltr on the canvas for rendering the tooltips, regardless of the css specified on the canvas
xAlign	string	undefined	Position of the tooltip caret in the X direction. more
yAlign	string	undefined	

'''

URL = "https://www.chartjs.org/docs/3.7.0/configuration/tooltip.html"

DT_PROP = '''
  @property
  def %(label)s(self):
    """
    Description:
    ------------
    %(description)s
    
    Related Pages:

      %(url)s
    """
    return self._config_get(%(default)s)

  @%(label)s.setter
  def %(label)s(self, %(value)s: %(type)s):
    self._config(%(value)s)
'''


DT_JS = '''
  def set_%(label)s(self, jsFncs, profile=None):
    """
    Description:
    ------------
    %(description)s
    
    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._config(
      "function (value){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile),
      name="%(label)s", js_type=True)
'''

OUT_PATH = r"C:\tmps"

with open(os.path.join(OUT_PATH, "DOC.TXT"), "w", encoding='utf-8') as fp:
  for line in DOC.strip().split("\n"):
    row = line.split("\t")
    if len(row) > 0:
      rec = dict(zip(COLUMNS, row))
      rec["url"] = URL
      rec["default"] = {"TRUE": "True", "FALSE": "False", "undefined": "None"}.get(rec.get("default", ""), rec.get("default", ""))
      if "." in rec.get("default"):
        rec["default"] = ""
      types = list(map(lambda x: x.strip(), rec["types"].strip().lower().split("|")))
      rec["description"] = rec.get("description", "").replace(". ", ". \n    ")
      if "[\u202f]" in rec["types"]:
        pass
        #fp.write(DT_PROP % {"default": "", "value": 'text', 'label': rec[0], "url": URL, "description": rec[2]})
      for f, dflt in FIELDS.items():
        if f not in rec:
          rec[f] = dflt
      if "expression" in types:
        rec["value"] = 'text'
        fp.write(DT_JS % {"default": "", "value": 'text', 'label': rec[0], "url": URL, "description": rec[2]})
      elif 'array' in types or 'Number[\u202f]' in types or 'Array[\u202f]' in types:
        rec["type"] = 'list'
        rec["value"] = 'values'
        fp.write(DT_PROP % rec)
      elif "string" in types or "URL" in types:
        rec["type"] = 'str'
        rec["value"] = 'text'
        fp.write(DT_PROP % rec)
      elif "color" in types:
        rec["type"] = 'str'
        rec["value"] = 'code'
        fp.write(DT_PROP % rec)
      elif 'number' in types:
        rec["type"] = 'float'
        rec["value"] = 'num'
        fp.write(DT_PROP % rec)
      elif 'boolean' in types:
        rec["type"] = 'bool'
        rec["value"] = 'flag'
        fp.write(DT_PROP % rec)
      elif 'any' in types:
        rec["type"] = 'Any'
        rec["value"] = 'record'
        fp.write(DT_PROP % rec)
      else:
        print(rec)
