
import os


DOC = '''

count	The total count of data objects in the group.
valid	The count of field values that are not missing or NaN.
missing	The count of null, undefined, or empty string ('') field values.
distinct	The count of distinct field values.
sum	The sum of field values.
product	The product of field values. ≥ 5.10
mean	The mean (average) field value.
average	The mean (average) field value. Identical to mean.
variance	The sample variance of field values.
variancep	The population variance of field values.
stdev	The sample standard deviation of field values.
stdevp	The population standard deviation of field values.
stderr	The standard error of field values.
median	The median field value.
q1	The lower quartile boundary of field values.
q3	The upper quartile boundary of field values.
ci0	The lower boundary of the bootstrapped 95% confidence interval of the mean field value.
ci1	The upper boundary of the bootstrapped 95% confidence interval of the mean field value.
min	The minimum field value.
max	The maximum field value.
argmin	An input data object containing the minimum field value.
argmax	An input data object containing the maximum field value.
values	The list of data objects in the group.

'''

URL = "https://vega.github.io/vega/docs/transforms/aggregate/"

DOC_ENUM = '''
  def %(label)s(self):
    """
    Description:
    ------------
    %(description)s
    
    Related Pages:

      %(url)s
    """
    self._set_value()
'''

DOC_ENUM_NAME = '''
  def %(name)s(self):
    """
    Description:
    ------------
    %(description)s

    Related Pages:

      %(url)s
    """
    self._set_value(name="%(label)s")
'''

OUT_PATH = r"C:\tmps"

with open(os.path.join(OUT_PATH, "DOC.TXT"), "w", encoding='utf-8') as fp:
  for line in DOC.strip().split("\n"):
    rec = line.split("\t")
    rec[1] = rec[1].replace(". ", ". \n    ")
    if "-" in rec[0]:
      name = rec[0].replace("-", "_")
      fp.write(DOC_ENUM_NAME % {"name": name, "label": rec[0], "description": rec[1], "url": URL})
    else:
      fp.write(DOC_ENUM % {"label": rec[0], "description": rec[1], "url": URL})
