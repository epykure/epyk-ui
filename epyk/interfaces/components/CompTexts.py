"""
Module in charge of all the Text components
"""

from epyk.core import html


class Texts(object):

  def __init__(self, context):
    self.context = context

  def text(self, text="", size=(None, "px"), color=None, align='left', width=(100, "%"), height=(None, "px"),
           htmlCode=None, tooltip=None, helper=None, profile=None):
    """
    Add the HTML text component to the page

    Example
    rptObj.ui.text("this is a test")

    Documentation
    https://www.w3schools.com/tags/tag_font.asp

    :param text: The string value to be displayed in the component
    :param size: Optional, A tuple with a integer for the size and its unit
    :param color: Optional. The color of the text
    :param align: Optional. The position of the icon in the line (left, right, center)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param helper:
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlText.Text

    :return: The text HTML object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Text(self.context.rptObj, text, size, color, align, width,
                                                    height, htmlCode, tooltip, helper, profile))

  def label(self, text=None, size=(None, "px"), color=None, align='center', width=(100, "px"), height=(23, "px"), htmlCode=None,
            tooltip='', profile=None):
    """
    The <label> tag defines a label for a <button>, <input>, <meter>, <output>, <progress>, <select>, or <textarea> element...

    The for attribute of the <label> tag should be equal to the id attribute of the related element to bind them together.

    Example
    rptObj.ui.texts.label("Test")
    rptObj.ui.texts.label("this is a test", color="red")

    Documentation
    https://www.w3schools.com/tags/tag_label.asp

    :param text: Optional. The string value to be displayed in the component
    :param size: Optional, A tuple with a integer for the size and its unit
    :param color: Optional. The color of the text
    :param align: Optional. The position of the icon in the line (left, right, center)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage

    :return: The text HTML object

    :rtype: html.HtmlText.Label
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Label(self.context.rptObj, text, size, color, align, width, height, htmlCode, tooltip, profile))

  def span(self, text=None, size=(None, "px"), color=None, align='center', width=(100, 'px'), height=("23", 'px'), htmlCode=None,
           tooltip=None, profile=None):
    """
    The <span> tag is used to group inline-elements in a document.

    The <span> tag provides no visual change by itself.

    The <span> tag provides a way to add a hook to a part of a text or a part of a document.

    Example
    rptObj.ui.texts.span("Test")

    Documentation
    https://www.w3schools.com/tags/tag_span.asp

    :param text: Optional. The string value to be displayed in the component
    :param size: Optional, A tuple with a integer for the size and its unit
    :param color: Optional. The color of the text
    :param align: Optional. The position of the icon in the line (left, right, center)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage

    :return:

    :rtype: html.HtmlText.Label
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Span(self.context.rptObj, text, size, color, align, width,
                                                    height, htmlCode, tooltip, profile))

  def highlights(self, text=None, title="", icon=None, type="danger", size=(None, "px"), color=None, width=(100, "%"),
                 height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")

    Documentation
    https://getbootstrap.com/docs/4.3/components/alerts/

    :param text: Optional. The string value to be displayed in the component
    :param title:
    :param icon:
    :param type: Optional, The type of the warning. Can be (primary, secondary, success, danger, warning, info, light,
                dark). Default danger
    :param size:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:

    :rtype: html.HtmlText.Highlights

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Highlights(self.context.rptObj, text, title, icon, type, size, color, width,
                                                          height, htmlCode, helper, profile))

  def formula(self, text=None, size=(None, "px"), width=(100, "%"), color=None, helper=None, profile=None):
    """
    Interface to the mathjs Formulas object

    Example
    rptObj.ui.texts.formula("$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$", helper="This is a formula")

    Documentation
    https://www.w3schools.com/tags/tag_font.asp

    :param text: Optional. The string value to be displayed in the component
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param color: Optional. The color of the text
    :param helper:
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlTextComp.Formula

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlTextComp.Formula(self.context.rptObj, text, size, width, color, helper, profile))

  def code(self, text="", size=(None, 'px'), color=None, width=(90, '%'), height=(None, 'px'), edit=True, htmlCode=None,
           helper=None, profile=None):
    """
    Python Wrapper to the Bootstrap CODE Tag

    Example
    rptObj.ui.texts.code("This is a code")

    Documentation
    https://v4-alpha.getbootstrap.com/content/code/

    :param text:
    :param size:
    :param color:
    :param width:
    :param height:
    :param edit:
    :param htmlCode:
    :param helper:
    :param profile:

    :rtype: html.HtmlText.Code

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Code(self.context.rptObj, text, size, color, width, height,
                                                    edit, htmlCode, helper, profile))

  def paragraph(self, text="", size=(None, 'px'), color=None, background_color=None, border=False, width=(100, "%"),
                height=(None, 'px'), htmlCode=None, encoding="UTF-8", dataSrc=None, helper=None, profile=None):
    """
    Python Wrapper to the HTML P Tag

    Example
    rptObj.ui.texts.paragraph("This is a paragraph", helper="Paragraph helper")

    Documentation
    https://www.w3schools.com/html/html_styles.asp

    :param text:
    :param size:
    :param color:
    :param background_color:
    :param border:
    :param width:
    :param height:
    :param htmlCode:
    :param encoding:
    :param dataSrc:
    :param profile:

    :rtype: html.HtmlText.Paragraph

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Paragraph(self.context.rptObj, text, size, color, background_color, border,
                                                         width, height, htmlCode, encoding, dataSrc, helper, profile))

  def preformat(self, text=None, size=(None, "px"), color=None, width=(90, '%'), height=(None, 'px'),
                htmlCode=None, dataSrc=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.texts.preformat("This is a pre formatted text")

    Documentation
    https://www.w3schools.com/html/html_styles.asp

    :param text:
    :param size:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param dataSrc:
    :param helper:
    :param profile:

    :rtype: html.HtmlText.Preformat

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Pre(self.context.rptObj, text, size, color, width,
                                                         height, htmlCode, dataSrc, helper, profile))

  def blockquote(self, text=None, author=None, size=(None, "px"), color=None, width=(None, '%'), height=(None, 'px'),
                 htmlCode=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.texts.blockquote("This is a code")

    Documentation
    https://v4-alpha.getbootstrap.com/content/typography/

    :param text:
    :param author:
    :param size:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:

    :rtype: html.HtmlText.BlockQuote

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.BlockQuote(self.context.rptObj, text, author, size, color, width,
                                                          height, htmlCode, helper, profile))

  def up_down(self, recordSet=None, size=(None, "px"), color=None, label=None, dataSrc=None, helper=None, profile=None):
    """
    Up and down Text component

    Example
    rptObj.ui.texts.up_down({'previous': 240885, 'value': 240985})

    Documentation
    https://fontawesome.com/

    :param recordSet:
    :param size:
    :param color:
    :param label:
    :param dataSrc:
    :param helper:
    :param profile:

    :rtype: html.HtmlTextComp.UpDown

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlTextComp.UpDown(self.context.rptObj, recordSet, size, color, label, dataSrc, helper, profile))

  def number(self, number=None, label=None, icon=None, size=(None, "px"), color=None, tooltip='', htmlCode=None,
             helper=None, profile=None):
    """

    Example
    rptObj.ui.texts.number(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Documentation

    :param number:
    :param label:
    :param icon:
    :param size:
    :param color:
    :param tooltip:
    :param htmlCode:
    :param helper:
    :param profile:

    :rtype: html.HtmlText.Numeric

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Numeric(self.context.rptObj, number, label, icon, size, color, tooltip,
                                                       htmlCode, helper, profile))

  def title(self, text=None, size=(None, 'px'), level=None, name=None, contents=None, color=None, picture=None, icon=None,
            marginTop=5, htmlCode=None, width=(100, "%"), height=(None, "px"), align=None, profile=None):
    """

    Example
    rptObj.ui.title("Test")
    rptObj.ui.title("Test", level=2)

    Documentation
    https://www.w3schools.com/tags/tag_hn.asp

    :param text:
    :param size:
    :param level:
    :param name:
    :param contents:
    :param color:
    :param picture:
    :param icon:
    :param marginTop:
    :param htmlCode:
    :param width:
    :param height:
    :param align:
    :param profile:
    :rtype: html.HtmlText.Title
    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Title(self.context.rptObj, text, size, level, name, contents, color,
                                                     picture, icon, marginTop, htmlCode, width, height, align, profile))

  def fieldset(self, legend=None, size=(None, 'px'), width=(100, "%"), height=(None, "px"), helper=None, profile=None):
    """

    Example
    rptObj.ui.texts.fieldset("legend")

    Documentation
    https://www.w3schools.com/tags/tag_legend.asp
    https://www.w3schools.com/tags/tag_fieldset.asp

    :param legend:
    :param size:
    :param width:
    :param height:
    :param profile:
    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlText.Fieldset(self.context.rptObj, legend, size, width=width, height=height,
                                                        helper=helper, profile=profile))
