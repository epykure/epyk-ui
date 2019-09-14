"""
Common interface for the slider type of objects
"""

# Check if pandas is available in the current environment
# if it is the case this module can handle DataFrame directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False


from epyk.core import html


class Sliders(object):
  """
  This module is relying on some Jquery IU components

  The slider and progress bar components can be fully described on the corresponding website
    - https://jqueryui.com/progressbar/
    - https://jqueryui.com/slider/

  As this module will return those object, all the properties and changes defined in the documentation can be done.
  """
  def __init__(self, context):
    self.context = context

  def slider(self, value=0, type="integer", range=None, animate=True, step=1, min=0, max=100, width=(100, '%'),
             height=(None, 'px'), htmlCode=None, globalFilter=None, recordSet=None, column=None,
             color=None, attrs=None, helper=None, profile=None):
    """
    Add a Jquery UI slider object to the page

    Example
    rptObj.ui.slider(recordSet=[1, 2, 3,4 ,5, 6, 7])

    Documentation
    https://jqueryui.com/slider/

    :param value:
    :param type:
    :param range:
    :param animate:
    :param step:
    :param min:
    :param max:
    :param width:
    :param height:
    :param htmlCode:
    :param globalFilter:
    :param recordSet:
    :param column:
    :param color:
    :param helper:
    :param profile:
    :rtype: html.HtmlEvent.Slider
    :return:
    """
    if recordSet is not None:
      is_converted = False
      if column is not None:
        if has_pandas:
          if isinstance(recordSet, pd.DataFrame):
            recordSet = sorted(recordSet[column].unique().tolist())
            is_converted = True

        if not is_converted:
          result = set([])
          for rec in recordSet:
            result.add(rec[column])
          recordSet = sorted(list(result))

    if attrs is None:
      attrs = {}

    if htmlCode is not None:
      attrs.update({"htmlCode": htmlCode, "changeUrl": False})

    return self.context.register(html.HtmlEvent.Slider(self.context.rptObj, value, type, range, animate, step, min,
        max, width, height, globalFilter, recordSet, color, attrs, helper, profile))

  def progressbar(self, number=None, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None, helper=None, profile=None):
    """
    Add a progress bar component to the page

    Example
    rptObj.ui.sliders.progressbar(300)

    Documentation
    https://jqueryui.com/progressbar/

    :param number: A number between 0 and 100
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode:
    :param attrs:
    :param helper:
    :param profile:
    :rtype: html.HtmlEvent.ProgressBar
    :return:
    """
    if attrs is None:
      attrs = {}

    if htmlCode is not None:
      attrs.update({"htmlCode": htmlCode, "changeUrl": False})

    return self.context.register(html.HtmlEvent.ProgressBar(self.context.rptObj, number, width, height,
                                                            attrs, helper, profile))
