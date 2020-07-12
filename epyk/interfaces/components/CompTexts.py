
from epyk.core import html
from epyk.core.html import Defaults_html
from epyk.core.css import Defaults_css


class Texts(object):

  def __init__(self, context):
    self.context = context

  def text(self, text="", color=None, align='left', width=('auto', ""), height=(None, "px"),
           htmlCode=None, tooltip=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Add the HTML text component to the page

    Usage::

      rptObj.ui.text("this is a test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Text`

    Related Pages:

      https://www.w3schools.com/tags/tag_font.asp

    Attributes:
    ----------
    :param text: The string value to be displayed in the component
    :param color: Optional. The color of the text
    :param align: Optional. The position of the icon in the line (left, right, center)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param options: Optional. The component options
    :param helper:
    :param profile: Optional. A flag to set the component performance storage

    :return: The text HTML object
    """
    if not isinstance(width, tuple):
      width = (width, 'px')
    dfl_options = {"reset": False, "markdown": False, "maxlength": None}
    if options is not None:
      dfl_options.update(options)
    text_comp = html.HtmlText.Text(self.context.rptObj, text, color, align, width, height, htmlCode, tooltip, dfl_options, helper, profile)
    if width[0] == 'auto':
      text_comp.style.css.display = "inline-block"
    if align == "center":
      text_comp.style.css.margin = "auto"
      text_comp.style.css.display = "block"
    return text_comp

  def absolute(self, text, size_notch=None, top=(50, "%"), left=(50, "%"), bottom=None, align='left', width=('auto', ""), height=(None, "px"), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param size_notch:
    :param top:
    :param left:
    :param align:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    :return:
    """
    dfl_options = {"reset": False, "markdown": False, "maxlength": None}
    if options is not None:
      dfl_options.update(options)
    text_comp = html.HtmlText.Text(self.context.rptObj, text, None, align, width, height, htmlCode, None, dfl_options, None, profile)
    text_comp.style.position = "absolute"
    text_comp.style.display = "block"
    if bottom is not None:
      text_comp.style.bottom = "%s%s" % (bottom[0], bottom[1])
    else:
      text_comp.style.top = "%s%s" % (top[0], top[1])
    text_comp.style.left = "%s%s" % (left[0], left[1])
    text_comp.style.transform = "translate(-%s, -%s)" % (text_comp.style.left, text_comp.style.top)
    if size_notch is not None:
      text_comp.style.font_size = Defaults_css.font(size_notch)
    if width[0] == 'auto':
      text_comp.style.css.display = "inline-block"
    return text_comp

  def label(self, text="", color=None, align='center', width=(100, "px"), height=('auto', ""), htmlCode=None,
            tooltip='', profile=None, options=None):
    """
    Description:
    ------------
    The <label> tag defines a label for a <button>, <input>, <meter>, <output>, <progress>, <select>, or <textarea> element...

    The for attribute of the <label> tag should be equal to the id attribute of the related element to bind them together.

    Usage::

      rptObj.ui.texts.label("Test")
      rptObj.ui.texts.label("this is a test", color="red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Label`

    Related Pages:

      https://www.w3schools.com/tags/tag_label.asp

    Attributes:
    ----------
    :param text: Optional. The string value to be displayed in the component
    :param color: Optional. The color of the text
    :param align: Optional. The position of the icon in the line (left, right, center)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    """
    dflt_options = {"markdown": True}
    if options is not None:
      dflt_options.update(options)
    html_label = html.HtmlText.Label(self.context.rptObj, text, color, align, width, height, htmlCode, tooltip,
                                     profile, dflt_options)
    return html_label

  def span(self, text="", color=None, align='center', width=None, height=None, htmlCode=None,
           tooltip=None, options=None, profile=None):
    """
    Description:
    ------------
    The <span> tag is used to group inline-elements in a document.

    The <span> tag provides no visual change by itself.

    The <span> tag provides a way to add a hook to a part of a text or a part of a document.

    Usage::

      rptObj.ui.texts.span("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Span`

    Related Pages:

      https://www.w3schools.com/tags/tag_span.asp

    Attributes:
    ----------
    :param text: Optional. The string value to be displayed in the component
    :param color: Optional. The color of the text
    :param align: Optional. The position of the icon in the line (left, right, center)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    """
    if width is None:
      width = (Defaults_html.TEXTS_SPAN_WIDTH, 'px')
    if height is None:
      height = (Defaults_html.LINE_HEIGHT, 'px')
    html_label = html.HtmlText.Span(self.context.rptObj, text, color, align, width, height, htmlCode, tooltip, options, profile)
    return html_label

  def highlights(self, text=None, title="", icon=None, type="danger", color=None, width=(None, "%"),
                 height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Provide contextual feedback messages for typical user actions with the handful of available and flexible alert messages.

    Usage::

      rptObj.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Highlights`

    Related Pages:

      https://getbootstrap.com/docs/4.3/components/alerts/

    Attributes:
    ----------
    :param text: Optional. The string value to be displayed in the component
    :param title:
    :param icon:
    :param type: Optional, The type of the warning. Can be (primary, secondary, success, danger, warning, info, light,
                 dark). Default danger
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:
    """
    html_light = html.HtmlText.Highlights(self.context.rptObj, text, title, icon, type, color, width,
                                          height, htmlCode, helper, options or {}, profile)
    return html_light

  def note(self, text=None, title="", icon=None, type="success", color=None, width=(None, "%"),
                 height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Provide contextual feedback messages for typical user actions with the handful of available and flexible alert messages.

    Usage::

      rptObj.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Highlights`

    Related Pages:

      https://getbootstrap.com/docs/4.3/components/alerts/

    Attributes:
    ----------
    :param text: Optional. The string value to be displayed in the component
    :param title:
    :param icon:
    :param type: Optional, The type of the warning. Can be (primary, secondary, success, danger, warning, info, light,
                 dark). Default danger
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:
    """
    if type not in ['success', 'warning', 'danger']:
      raise Exception("This type %s is not recognised" % type)

    html_light = html.HtmlText.Highlights(self.context.rptObj, text, title, icon, type, color, width,
                                          height, htmlCode, helper, options or {}, profile)
    html_light.style.css.border_left = "4px solid %s" % getattr(self.context.rptObj.theme, type)[1]
    html_light.style.css.border_radius = 0
    return html_light

  def formula(self, text=None, width=(100, "%"), color=None, helper=None, profile=None):
    """
    Description:
    ------------
    Interface to the mathjax Formulas object

    Usage::

      rptObj.ui.texts.formula("$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$", helper="This is a formula")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.Formula`

    Related Pages:

      https://mathjax.org/docs/index.html


    Attributes:
    ----------
    :param text: Optional. The string value to be displayed in the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param color: Optional. The color of the text
    :param helper:
    :param profile: Optional. A flag to set the component performance storage
    """
    html_formula = html.HtmlTextComp.Formula(self.context.rptObj, text, width, color, helper, profile)
    return html_formula

  def code(self, text="", language='python', color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None,
           options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Python Wrapper to the Bootstrap CODE Tag

    Usage::

      rptObj.ui.texts.code("This is a code")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://v4-alpha.getbootstrap.com/content/code/

    Attributes:
    ----------
    :param text:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param helper:
    :param profile:
    """
    dflt_options = {"lineNumbers": True, 'mode': language, 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code

  def paragraph(self, text="", color=None, background_color=None, border=False, width=(100, "%"),
                height=(None, 'px'), htmlCode=None, encoding="UTF-8", dataSrc=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Python Wrapper to the HTML P Tag

    Usage::

      rptObj.ui.texts.paragraph("This is a paragraph", helper="Paragraph helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Paragraph`

    Related Pages:

      https://www.w3schools.com/html/html_styles.asp

    Attributes:
    ----------
    :param text:
    :param color:
    :param background_color:
    :param border:
    :param width:
    :param height:
    :param htmlCode:
    :param encoding:
    :param dataSrc:
    :param profile:
    """
    dflt_options = {"reset": True, 'markdown': False, "classes": []}
    if options is not None:
      dflt_options.update(options)
    html_paragraph = html.HtmlText.Paragraph(self.context.rptObj, text, color, background_color, border, width, height,
                                             htmlCode, encoding, dataSrc, helper, dflt_options, profile)
    return html_paragraph

  def preformat(self, text=None, color=None, width=(90, '%'), height=(None, 'px'), htmlCode=None, dataSrc=None,
                options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Preformatted text:
    The <pre> tag defines preformatted text.
    Text in a <pre> element is displayed in a fixed-width font (usually Courier), and it preserves both spaces and line breaks.

    Usage::

      rptObj.ui.texts.preformat("This is a pre formatted text")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Pre`

    Related Pages:

      https://www.w3schools.com/html/html_styles.asp
      https://www.w3schools.com/tags/tag_pre.asp

    Attributes:
    ----------
    :param text:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param dataSrc:
    :param options:
    :param helper:
    :param profile:
    """
    dflt_options = {"reset": True, 'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_pre = html.HtmlText.Pre(self.context.rptObj, text, color, width, height, htmlCode, dataSrc, dflt_options, helper, profile)
    return html_pre

  def blockquote(self, text=None, author=None, color=None, width=(None, '%'), height=(None, 'px'),
                 htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    The <blockquote> tag specifies a section that is quoted from another source.
    Browsers usually indent <blockquote> elements.

    Usage::

      rptObj.ui.texts.blockquote("This is a code")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.BlockQuote`

    Related Pages:

      https://v4-alpha.getbootstrap.com/content/typography/
      https://www.w3schools.com/TAGS/tag_blockquote.asp

    Attributes:
    ----------
    :param text:
    :param author:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:
    """
    html_blockquote = html.HtmlText.BlockQuote(self.context.rptObj, text, author, color, width, height, htmlCode, helper, options, profile)
    return html_blockquote

  def up_down(self, rec=None, color=None, label=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Up and down Text component

    Usage::

      rptObj.ui.texts.up_down({'previous': 240885, 'value': 240985})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.UpDown`

    Related Pages:

      https://fontawesome.com/

    Attributes:
    ----------
    :param rec:
    :param color:
    :param label:
    :param options:
    :param helper:
    :param profile:
    """
    dflt_options = {"digits": 0, 'thousand_sep': ",", 'decimal_sep': ".", 'font_size': Defaults_css.font(),
                    'red': self.context.rptObj.theme.danger[1], 'green': self.context.rptObj.theme.success[1],
                    'orange': self.context.rptObj.theme.warning[1]}
    if options is not None:
      dflt_options.update(options)
    html_up_down = html.HtmlTextComp.UpDown(self.context.rptObj, rec, color, label, dflt_options, helper, profile)
    return html_up_down

  def number(self, number=0, title=None, label=None, icon=None, color=None, tooltip='', htmlCode=None,
             options=None, helper=None, width=(150, 'px'), profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.texts.number(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Numeric`

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param number: Optional. The value to be displayed to the component. Default now
    :param title:
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param color:
    :param tooltip:
    :param htmlCode:
    :param options:
    :param helper:
    :param profile:
    """
    dflt_options = {"digits": 0, "thousand_sep": ',', "decimal_sep": '.'}
    if options is not None:
      dflt_options.update(options)
    html_number = html.HtmlText.Numeric(self.context.rptObj, number, title, label, icon, color, tooltip, htmlCode,
                                        dflt_options, helper, width, profile)
    return html_number

  def title(self, text=None, level=None, name=None, contents=None, color=None, picture=None, icon=None,
            marginTop=5, htmlCode=None, width=("auto", ""), height=(None, "px"), align=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a title

    Usage::

      rptObj.ui.title("Test")
      rptObj.ui.title("Test", level=2)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Title`

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp

    Attributes:
    ----------
    :param text:
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
    :param options:
    :param profile:
    """
    dflt_options = {"reset": True, 'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlText.Title(self.context.rptObj, text, level, name, contents, color, picture, icon,
                                     marginTop, htmlCode, width, height, align, dflt_options, profile)
    return html_title

  def fieldset(self, legend="", width=(100, "%"), height=(None, "px"), helper=None, options=None, profile=None):
    """
    Description:
    ------------
    The <fieldset> tag is used to group related elements in a form.
    The <fieldset> tag draws a box around the related elements.

    Usage::

      rptObj.ui.texts.fieldset("legend")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Fieldset`

    Related Pages:

      https://www.w3schools.com/tags/tag_legend.asp
      https://www.w3schools.com/tags/tag_fieldset.asp

    Attributes:
    ----------
    :param legend:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    html_fieldset = html.HtmlText.Fieldset(self.context.rptObj, legend, width=width, height=height, helper=helper,
                                           options=options, profile=profile)
    return html_fieldset
