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
  Description:
  ------------
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
    Description:
    ------------
    Add a Jquery UI slider object to the page

    Usage:
    ------
    rptObj.ui.slider(recordSet=[1, 2, 3, 4, 5, 6, 7])

    Related Pages:
    --------------
    https://jqueryui.com/slider/

    Attributes:
    ----------
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
    attrs = {} if attrs is None else attrs
    if htmlCode is not None:
      attrs.update({"htmlCode": htmlCode, "changeUrl": False})
    html_slider = html.HtmlEvent.Slider(self.context.rptObj, value, type, range, animate, step, min,
                                        max, width, height, globalFilter, recordSet, color, attrs, helper, profile)
    self.context.register(html_slider)
    return html_slider

  def progressbar(self, number=None, total=100, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None,
                  helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a progress bar component to the page

    Usage:
    ------
    rptObj.ui.sliders.progressbar(300)

    Related Pages:
    --------------
    https://jqueryui.com/progressbar/

    Attributes:
    ----------
    :param number: A number (by default between 0 and 100)
    :param total: A number
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode:
    :param attrs:
    :param helper:
    :param profile:
    """
    if htmlCode is not None:
      attrs.update({"htmlCode": htmlCode, "changeUrl": False})
    html_pr = html.HtmlEvent.ProgressBar(self.context.rptObj, number, total, width, height,  attrs or {}, helper, options, profile)
    self.context.register(html_pr)
    return html_pr
