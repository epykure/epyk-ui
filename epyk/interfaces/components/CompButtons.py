""" .. _CompButtons:

Button Interfaces
=================

"""
# Check if pandas is available in the current environment
# if it is the case this module can handle DataFrame directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False

from epyk.core import html


class Buttons(object):
  def __init__(self, context):
    self.context = context

  def _recordSet(self, recordSet, column):
    """
    Attributes:
    ----------
    :param recordSet:
    :param column:
    :return:
    """
    data = None
    is_converted = False
    if has_pandas:
      if isinstance(recordSet, pd.DataFrame):
        data = [{'name': r, 'value': r} for r in recordSet[column].unique().tolist()]
        is_converted = True

    if not is_converted:
      result = {}
      for rec in recordSet:
        result[rec[column]] = {'name': rec[column], 'value': rec[column]}
      data = [result[k] for k in sorted(result.keys())]
    return data

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
    Standard button

    Usage::

      rptObj.ui.button("Test")


    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Attributes:
    ----------
    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component

    :return: The Button HTML object
    """
    html_button = html.HtmlButton.Button(self.context.rptObj, text, icon, width, height, htmlCode=htmlCode,
                                         tooltip=tooltip, profile=profile, options=options)
    return html_button

  def small(self, text="", icon=None, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None,
             profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param tooltip:
    :param profile:
    :param options:
    """
    html_button = html.HtmlButton.Button(self.context.rptObj, text, icon, width, height, htmlCode=htmlCode,
                                         tooltip=tooltip, profile=profile, options=options)
    html_button.style.css.line_height = 12
    html_button.style.css.padding = 2
    return html_button

  def important(self, text="", icon=None, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
    Same as Standard button but used to attract user attention

    Usage::

      rptObj.ui.buttons.important("Important")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

      https://www.w3schools.com/tags/tag_button.asp
      http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Attributes:
    ----------
    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component

    :return: The Button HTML object
    """
    html_button = html.HtmlButton.Button(self.context.rptObj, text, icon, width, height, htmlCode=htmlCode,
                                         tooltip=tooltip, profile=profile, options=options)
    html_button.style.add_classes.button.important()
    return html_button

  def validate(self, text="", width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Description:
    -----------

    Usage::

      rptObj.ui.buttons.validate()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

        https://www.w3schools.com/tags/tag_button.asp
        http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Attributes:
    ----------
    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    html_but = html.HtmlButton.Button(self.context.rptObj, text, 'fas fa-check-circle', width, height, htmlCode=htmlCode,
                                      tooltip=tooltip, profile=profile, options=options)
    return html_but

  def remove(self, text="", width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Description:
    -----------
    Button with cross icon

    Usage::

      rptObj.ui.buttons.remove()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

			https://www.w3schools.com/tags/tag_button.asp
    http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Attributes:
    ----------
    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component

    :return: The Button HTML object
    """
    html_but = html.HtmlButton.Button(self.context.rptObj, text, 'fas fa-trash-alt', width, height, htmlCode=htmlCode,
                             tooltip=tooltip, profile=profile, options=options)
    return html_but

  def phone(self, text="", width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Description:
    -----------

    Usage::

      rptObj.ui.buttons.phone()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

			https://www.w3schools.com/tags/tag_button.asp
    http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Attributes:
    ----------
    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component

    :return: The Button HTML object
    """
    html_button = html.HtmlButton.Button(self.context.rptObj, text, 'fas fa-phone', width, height, htmlCode=htmlCode,
                                         tooltip=tooltip, profile=profile, options=options)
    return html_button

  def mail(self, text="", width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.buttons.mail()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Button`

    Related Pages:

			https://www.w3schools.com/tags/tag_button.asp
    http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    Attributes:
    ----------
    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    html_but = html.HtmlButton.Button(self.context.rptObj, text, 'fas fa-envelope', width, height, htmlCode=htmlCode,
                                      tooltip=tooltip, profile=profile, options=options)
    return html_but

  def radio(self, recordSet=None, checked=None, htmlCode=None, label=None, width=(100, '%'), height=(None, "px"), radioVisible=False,
            event=None, withRemoveButton=False, column=None, align='left', filters=None, tooltip='', allSelected=False,
            radioType="row", helper=None, profile=None):
    """
    Description:
    ------------
    Creates a radio HTML component

    Usage::

      rptObj.ui.buttons.radio(df, dfColumn="A", htmlCode="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlRadio.Radio`

    Related Pages:

			https://www.w3schools.com/bootstrap/bootstrap_forms_inputs.asp

    Attributes:
    ----------
    :param recordSet:
    :param checked:
    :param htmlCode:
    :param label:
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param radioVisible:
    :param event:
    :param withRemoveButton:
    :param column:
    :param align:
    :param filters:
    :param tooltip:
    :param allSelected:
    :param radioType:
    :param profile:
    """
    recordSet = recordSet or []

    if column is not None:
      recordSet = self._recordSet(recordSet, column)
    if isinstance(recordSet, list) and recordSet and not isinstance(recordSet[0], dict):
      tmpVals = [{'value': str(v)} for v in recordSet]
      tmpVals[0]['checked'] = True
      recordSet = tmpVals
    html_radio = html.HtmlRadio.Radio(self.context.rptObj, recordSet, htmlCode, label, width,
                      height, radioVisible, event, withRemoveButton, align, filters, tooltip, radioType, helper, profile)
    return html_radio

  def toggle(self, recordSet=None, label=None, color=None, width=(None, '%'), height=(20, 'px'), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.buttons.toggle({'on': "true", 'off': 'false'})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlRadio.Switch`

    Related Pages:
http://thecodeplayer.com/walkthrough/pure-css-on-off-toggle-switch
    https://codepen.io/mburnette/pen/LxNxNg

    Attributes:
    ----------
    :param recordSet:
    :param label:
    :param color:
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode:
    :param profile:
    """
    html_toggle = html.HtmlRadio.Switch(self.context.rptObj, recordSet, label, color, width, height, htmlCode, profile)
    return html_toggle

  def checkboxes(self, records=None, title=None, color=None, width=(100, "%"), height=(None, "px"), align='left',
               htmlCode=None, tooltip='', dfColumn=None, icon="fas fa-check", options=None, profile=None):
    """
    Description:
    ------------
    Python wrapper to the HTML checkbox elements

    Usage::

      rptObj.ui.buttons.checkboxes(data)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Checkbox`

    Related Pages:

			https://www.w3schools.com/howto/howto_css_custom_checkbox.asp

    Attributes:
    ----------
    :param records:
    :param title:
    :param color:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param tooltip:
    :param dfColumn:
    :param icon:
    :param profile:
    """
    if dfColumn is not None:
      if has_pandas and issubclass(type(records), pd.DataFrame):
        # if globalFilter:
        #   dataId = id(records)
        #   dataCode = "df_code_%s" % dataId
        #   globalFilter = {'jsId': dataCode, 'colName': dfColumn, 'allSelected': options.get("all_selected", False), 'operation': 'in'}
        #   if not dataCode in self.context.rptObj.jsSources:
        #     self.context.rptObj.jsSources[dataCode] = {'dataId': dataId, 'containers': [], 'data': records}
        #     self.context.rptObj.jsSources[dataCode]['containers'].append(self)
        if options.get("all_selected", False):
          records = [{"value": rec, "checked": True} for rec in records[dfColumn].unique().tolist()]
        else:
          records = records[dfColumn].unique().tolist()
    elif isinstance(records, list) and len(records) > 0:
      if not isinstance(records[0], dict):
        records = [{"value": rec} for rec in records]
    html_boxes = html.HtmlButton.Checkbox(self.context.rptObj, records, title, color, width,
                                             height, align, htmlCode, tooltip, icon, options or {}, profile)
    return html_boxes

  def check(self, flag=False, tooltip=None, width=(None, "px"), height=(20, "px"), label=None, icon=None, htmlCode=None,
            profile=None, options=None):
    """
    Description:
    ------------
    Wrapper to the check box button object

    Usage::

      rptObj.ui.buttons.check(label="Label")
      rptObj.ui.buttons.check(True, label="Label")
      rptObj.ui.buttons.check(True, label="Label", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.CheckButton`

    Related Pages:
Attributes:
    ----------
    :param flag: Optional. The value of the checkbox. Default False
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param label: Optional. The component label content
    :param icon: Optional. The icon to be used in the check component
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    html_but = html.HtmlButton.CheckButton(self.context.rptObj, flag, tooltip, width, height, icon, label, htmlCode, options or {}, profile)
    return html_but

  def menu(self, record, text="", icon=None, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Description:
    -----------
    Button with an underlying items menu

    Usage::

      tree5 = rptObj.ui.buttons.menu(["A", "B", "C"], 'Menu')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.ButtonMenu`

    Related Pages:

			https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_js_dropdown_hover

    Attributes:
    ----------
    :param record:
    :param text:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param tooltip:
    :param profile:
    :param options:
    """
    html_button = html.HtmlButton.ButtonMenu(self.context.rptObj, record, text, icon, width, height, htmlCode=htmlCode,
                                              tooltip=tooltip, profile=profile, options=options)
    return html_button
