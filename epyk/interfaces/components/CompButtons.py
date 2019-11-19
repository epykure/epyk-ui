"""
Module dedicated to the Buttons Interface
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

  def button(self, text=None, icon=None, width=(None, "%"), height=(None, "px"), size=(None, 'px'),
             htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Standard button used in the framework

    Example
    rptObj.ui.button("Test")

    Documentation
    https://www.w3schools.com/tags/tag_button.asp
    http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size: Optional, A tuple with a integer for the size and its unit
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    size = self.context._size(size)
    html_obj = html.HtmlButton.Button(self.context.rptObj, text, icon, size, width, height, htmlCode=htmlCode,
                                      tooltip=tooltip, profile=profile, options=options or {})
    self.context.register(html_obj)
    return html_obj

  def validate(self, text=None, width=(None, "%"), height=(None, "px"), size=(None, 'px'), htmlCode=None,
               tooltip=None, profile=None, options=None):
    """
    Example
    rptObj.ui.buttons.validate()

    Documentation
    https://www.w3schools.com/tags/tag_button.asp
    http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size: Optional, A tuple with a integer for the size and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    size = self.context._size(size)
    html_obj = html.HtmlButton.Button(self.context.rptObj, text, 'fas fa-check-circle', size, width, height,
                                      htmlCode=htmlCode, tooltip=tooltip, profile=profile, options=options or {})
    self.context.register(html_obj)
    return html_obj

  def remove(self, text=None, width=(None, "%"), height=(None, "px"), size=(None, 'px'), htmlCode=None,
            tooltip=None, profile=None, options=None):
    """
    Example
    rptObj.ui.buttons.remove()

    Documentation
    https://www.w3schools.com/tags/tag_button.asp
    http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size: Optional, A tuple with a integer for the size and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    size = self.context._size(size)
    html_obj = html.HtmlButton.Button(self.context.rptObj, text, 'fas fa-trash-alt', size, width, height, htmlCode=htmlCode,
                             tooltip=tooltip, profile=profile, options=options or {})
    self.context.register(html_obj)
    return html_obj

  def phone(self, text=None, width=(None, "%"), height=(None, "px"), size=(None, 'px'), htmlCode=None,
            tooltip=None, profile=None, options=None):
    """
    Example
    rptObj.ui.buttons.phone()

    Documentation
    https://www.w3schools.com/tags/tag_button.asp
    http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size: Optional, A tuple with a integer for the size and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    size = self.context._size(size)
    html_obj = html.HtmlButton.Button(self.context.rptObj, text, 'fas fa-phone', size, width, height, htmlCode=htmlCode,
                             tooltip=tooltip, profile=profile, options=options or {})
    self.context.register(html_obj)
    return html_obj

  def mail(self, text=None, width=(None, "%"), height=(None, "px"), size=(None, 'px'), htmlCode=None,
           tooltip=None, profile=None, options=None):
    """
    Example
    rptObj.ui.buttons.mail()

    Documentation
    https://www.w3schools.com/tags/tag_button.asp
    http://www.kodingmadesimple.com/2015/04/custom-twitter-bootstrap-buttons-icons-images.html

    :param text: Optional. The value to be displayed to the button
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size: Optional, A tuple with a integer for the size and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    size = self.context._size(size)
    html_obj = html.HtmlButton.Button(self.context.rptObj, text, 'fas fa-envelope', size, width, height, htmlCode=htmlCode,
                                      tooltip=tooltip, profile=profile, options=options or {})
    self.context.register(html_obj)
    return html_obj

  def radio(self, recordSet=None, checked=None, htmlCode=None, label=None, width=(100, '%'), height=(None, "px"),
            radioVisible=False, event=None, withRemoveButton=False, column=None, align='left', filters=None,
            tooltip='', allSelected=False, radioType="row", helper=None, profile=None):
    """

    Example
    rptObj.ui.buttons.radio(df, dfColumn="A", htmlCode="test")

    radio = rptObj.ui.radio(["A", "B", "C"], checked="B")
    radio + "G"

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_forms_inputs.asp

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
    :param title:
    :param radioType:
    :param profile:
    """
    if column is not None:
      if filters is not None:
        if filters:
          dataId = id(recordSet)
          dataCode = "df_code_%s" % dataId
          filters = {'jsId': dataCode, 'colName': column, 'allSelected': allSelected, 'operation': 'in'}
          if not dataCode in self.context.rptObj.jsSources:
            self.context.rptObj.jsSources[dataCode] = {'dataId': dataId, 'containers': [], 'data': recordSet}
            self.context.rptObj.jsSources[dataCode]['containers'].append(self)
      recordSet = recordSet[column].unique().tolist()

    if isinstance(recordSet, list) and not isinstance(recordSet[0], dict):
      tmpVals = [{'value': str(v), 'checked': v == checked} for v in recordSet]
      if checked is None:
        tmpVals[0]['checked'] = True
      recordSet = tmpVals
    html_obj = html.HtmlRadio.Radio(self.context.rptObj, recordSet, htmlCode, label, width, height, radioVisible,
                                    event, withRemoveButton, align, filters, tooltip, radioType, helper, profile)
    self.context.register(html_obj)
    return html_obj

  def switch(self, recordSet=None, label=None, color=None, size=16, width=(150, '%'), height=(20, 'px'), htmlCode=None, profile=None):
    """
    Python wrapper to the HTML switch elements

    Example
    rptObj.ui.buttons.switch()

    Documentation
    http://thecodeplayer.com/walkthrough/pure-css-on-off-toggle-switch
    https://codepen.io/mburnette/pen/LxNxNg

    :param recordSet:
    :param label:
    :param color:
    :param size:
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode:
    :param profile:
    """
    html_obj = html.HtmlRadio.Switch(self.context.rptObj, recordSet or {'off': 'off', 'on': 'on'}, label, color, size, width, height, htmlCode, profile)
    self.context.register(html_obj)
    return html_obj

  def checkbox(self, records=None, title=None, color=None, width=(100, "%"), height=(None, "px"), align='left',
               htmlCode=None, globalFilter=None, tooltip='', dfColumn=None, icon="fas fa-check", options=None, profile=None):
    """
    Python wrapper to the HTML checkbox elements

    Example

    Documentation
    https://www.w3schools.com/howto/howto_css_custom_checkbox.asp

    :param records:
    :param title:
    :param color:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param globalFilter:
    :param tooltip:
    :param dfColumn:
    :param icon:
    :param profile:
    """
    if dfColumn is not None:
      if has_pandas and issubclass(type(records), pd.DataFrame):
        if globalFilter:
          dataId = id(records)
          dataCode = "df_code_%s" % dataId
          globalFilter = {'jsId': dataCode, 'colName': dfColumn, 'allSelected': options.get("all_selected", False), 'operation': 'in'}
          if not dataCode in self.context.rptObj.jsSources:
            self.context.rptObj.jsSources[dataCode] = {'dataId': dataId, 'containers': [], 'data': records}
            self.context.rptObj.jsSources[dataCode]['containers'].append(self)
        if options.get("all_selected", False):
          records = [{"value": rec, "checked": True} for rec in records[dfColumn].unique().tolist()]
        else:
          records = records[dfColumn].unique().tolist()
    elif isinstance(records, list) and len(records) > 0:
      if not isinstance(records[0], dict):
        records = [{"value": rec} for rec in records]
    html_obj = html.HtmlButton.Checkbox(self.context.rptObj, records, title, color, width, height, align, htmlCode,
                                        globalFilter, tooltip, icon, options or {}, profile)
    self.context.register(html_obj)
    return html_obj

  def check(self, flag=False, tooltip=None, width=(None, "px"), height=(20, "px"), label=None, icon=None, htmlCode=None,
            profile=None, options=None):
    """
    Wrapper to the check box button object

    Example
    rptObj.ui.buttons.check(label="Label")
    rptObj.ui.buttons.check(True, label="Label")
    rptObj.ui.buttons.check(True, label="Label", icon="fas fa-align-center")

    Documentation

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
    html_obj = html.HtmlButton.CheckButton(self.context.rptObj, flag, tooltip, width, height, icon, label, htmlCode,
                                           options or {}, profile)
    self.context.register(html_obj)
    return html_obj

  def zipfile(self, text, fileName, css_cls=None, css_attr=None, profile=None):
    """

    TODO: Add the memory zip files

    Documentation
    https://newseasandbeyond.wordpress.com/2014/01/27/creating-in-memory-zip-file-with-python/

    :param text:
    :param fileName:
    :param css_cls:
    :param css_attr:
    :param profile:
    """
    html_obj = html.HtmlFiles.DownloadMemoryZip(self.context.rptObj, text, fileName, css_cls, css_attr, profile)
    self.context.register(html_obj)
    return html_obj
