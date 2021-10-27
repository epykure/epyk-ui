
import os


DOC = '''

name	String	Required. A unique name for the data set.
format	Format	An object that specifies the format for parsing the data file or values. See the format reference for more.
source	String | String[ ]	The name of one or more data sets to use as the source for this data set. The source property is useful in combination with a transform pipeline to derive new data. If string-valued, indicates the name of the source data set. If array-valued, specifies a collection of data source names that should be merged (unioned) together.
url	String	A URL from which to load the data set. Use the format property to ensure the loaded data is correctly parsed. If the format property is not specified, the data is assumed to be in a row-oriented JSON format.
values	Any	The full data set, included inline. The values property allows data to be included directly within the specification itself. While most commonly an array of objects, other data types (such as CSV strings) may be used, subject to the format settings.
async	Boolean	≥ 5.9 A boolean flag (default false) indicating if dynamic data loading or reformatting should occur asynchronously. If true, dataflow evaluation will complete, data loading will occur in the background, and the dataflow will be re-evaluated when loading is complete. If false, dataflow evaluation will block until loading is complete and then continue within the same evaluation cycle. The use of async can allow multiple dynamic datasets to be loaded simultaneously while still supporting interactivity. However, the use of async can cause datasets to remain empty while the rest of the dataflow is evaluated, potentially affecting downstream computation.
on	Trigger[ ]	An array of updates to insert, remove, & toggle data values, or clear the data when trigger conditions are met. See the trigger reference for more.
transform	Transform[ ]	An array of transforms to perform on the input data. The output of the transform pipeline then becomes the value of this data set. See the transform reference for more.

'''

URL = "https://vega.github.io/vega/docs/transforms/aggregate/"


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
  def %(label)s(self, %(value)s):
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
    rec = line.split("\t")
    if len(rec) > 0:
      types = list(map(lambda x: x.strip(), rec[1].strip().split("|")))
      rec[2] = rec[2].replace(". ", ". \n    ")
      if "[\u202f]" in rec[1]:
        pass
        #fp.write(DT_PROP % {"default": "", "value": 'text', 'label': rec[0], "url": URL, "description": rec[2]})
      if "Expression" in types:
        fp.write(DT_JS % {"default": "", "value": 'text', 'label': rec[0], "url": URL, "description": rec[2]})
      elif 'Array' in types or 'Number[\u202f]' in types or 'Array[\u202f]' in types:
        fp.write(DT_PROP % {"default": "", "value": 'values', 'label': rec[0], "url": URL, "description": rec[2]})
      elif "String" in types or "URL" in types:
        fp.write(DT_PROP % {"default": "", "value": 'text', 'label': rec[0], "url": URL, "description": rec[2]})
      elif "Color" in types:
        fp.write(DT_PROP % {"default": "", "value": 'code', 'label': rec[0], "url": URL, "description": rec[2]})
      elif 'Number' in types:
        fp.write(DT_PROP % {"default": "", "value": 'num', 'label': rec[0], "url": URL, "description": rec[2]})
      elif 'Boolean' in types:
        fp.write(DT_PROP % {"default": "", "value": 'flag', 'label': rec[0], "url": URL, "description": rec[2]})
      elif 'Any' in types:
        fp.write(DT_PROP % {"default": "", "value": 'record', 'label': rec[0], "url": URL, "description": rec[2]})
      else:
        print(rec)
