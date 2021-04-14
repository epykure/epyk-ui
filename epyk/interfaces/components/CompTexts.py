#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Texts:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def text(self, text="", color=None, align='left', width=('auto', ""), height=(None, "px"),
           html_code=None, tooltip=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Add the HTML text component to the page.

    Usage:
    -----

      page.ui.text("this is a test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Text`

    Related Pages:

      https://www.w3schools.com/tags/tag_font.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/markdown.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/postit.py

    Attributes:
    ----------
    :param text: String. The string value to be displayed in the component.
    :param color: String. Optional. The color of the text.
    :param align: String. Optional. The position of the icon in the line (left, right, center).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. The component options.
    :param helper: String. Optional. A tooltip helper.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dfl_options = {"reset": False, "markdown": False, "maxlength": None}
    if options is not None:
      dfl_options.update(options)
    text = self.page.py.encode_html(text)
    text_comp = html.HtmlText.Text(
      self.page, text, color, align, width, height, html_code, tooltip, dfl_options, helper, profile)
    if width[0] == 'auto':
      text_comp.style.css.display = "inline-block"
    if align in ["center", 'right']:
      text_comp.style.css.margin = "auto"
      text_comp.style.css.display = "block"
    return text_comp

  @html.Html.css_skin()
  def block(self, text="", color=None, align='left', width=(100, "%"), height=(None, "px"),
            html_code=None, tooltip=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Add the HTML text component to the page.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.text("this is a test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Text`

    Related Pages:

      https://www.w3schools.com/tags/tag_font.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/markdown.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/postit.py

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component.
    :param color: String. Optional. The color of the text.
    :param align: String. Optional. The position of the icon in the line (left, right, center).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    text_comp = self.text(text, color, align, width, height, html_code, tooltip, options, helper, profile)
    text_comp.style.css.display = "inline-block"
    text_comp.style.css.text_align = "left"
    return text_comp

  @html.Html.css_skin()
  def absolute(self, text, size_notch=None, top=(50, "%"), left=(50, "%"), bottom=None, align='left',
               width=('auto', ""), height=(None, "px"), html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param size_notch:
    :param top: Tuple. Optional. A tuple with the integer for the component's distance to the top of the page.
    :param left: Tuple. Optional. A tuple with the integer for the component's distance to the left of the page.
    :param bottom: Tuple. Optional. A tuple with the integer for the component's distance to the bottom of the page.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    left = Arguments.size(left, unit="%")
    top = Arguments.size(top, unit="%")
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"reset": False, "markdown": False, "maxlength": None}
    if options is not None:
      dfl_options.update(options)
    text = self.page.py.encode_html(text)
    text_comp = html.HtmlText.Text(
      self.page, text, None, align, width, height, html_code, None, dfl_options, None, profile)
    text_comp.style.css.position = "absolute"
    text_comp.style.css.display = "block"
    text_comp.style.css.left = "%s%s" % (left[0], left[1])
    if bottom is not None:
      text_comp.style.css.bottom = "%s%s" % (bottom[0], bottom[1])
      text_comp.style.css.transform = "translate(%s%s, %s)" % (-left[0], left[1], text_comp.style.css.bottom)
    else:
      text_comp.style.css.top = "%s%s" % (top[0], top[1])
      text_comp.style.css.transform = "translate(%s%s, -%s)" % (-left[0], left[1], text_comp.style.css.top)
    if size_notch is not None:
      text_comp.style.css.font_size = self.page.body.style.globals.font.normal(size_notch)
    if width[0] == 'auto':
      text_comp.style.css.display = "inline-block"
    return text_comp

  @html.Html.css_skin()
  def label(self, text="", color=None, align='center', width=(100, "px"), height=('auto', ""), html_code=None,
            tooltip='', profile=None, options=None):
    """
    Description:
    ------------
    The <label> tag defines a label for a <button>, <input>, <meter>, <output>, <progress>, <select>,
    or <textarea> element...

    The for attribute of the <label> tag should be equal to the id attribute of the related element to bind
    them together.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.label("Test")
      page.ui.texts.label("this is a test", color="red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Label`

    Related Pages:

      https://www.w3schools.com/tags/tag_label.asp

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component.
    :param color: String. Optional. The color of the text.
    :param align: String. Optional. The position of the icon in the line (left, right, center).
    :param width: Tuple | Integer. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Integer. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"markdown": True}
    if options is not None:
      dflt_options.update(options)
    text = self.page.py.encode_html(text)
    html_label = html.HtmlText.Label(self.page, text, color, align, width, height, html_code, tooltip,
                                     profile, dflt_options)
    return html_label

  @html.Html.css_skin()
  def span(self, text="", color=None, align='center', width=None, height=None, html_code=None,
           tooltip=None, options=None, profile=None):
    """
    Description:
    ------------
    The <span> tag is used to group inline-elements in a document.

    The <span> tag provides no visual change by itself.

    The <span> tag provides a way to add a hook to a part of a text or a part of a document.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.span("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Span`

    Related Pages:

      https://www.w3schools.com/tags/tag_span.asp

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component.
    :param color: String. Optional. The color of the text.
    :param align: String. Optional. The position of the icon in the line (left, right, center).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_label = html.HtmlText.Span(self.page, text, color, align, width, height, html_code, tooltip, options, profile)
    return html_label

  @html.Html.css_skin()
  def highlights(self, text=None, title=None, icon=None, type="danger", color=None, width=('auto', ""),
                 height=(None, "px"), html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Provide contextual feedback messages for typical user actions with the handful of available and flexible
    alert messages.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")
      page.ui.texts.highlights("Server configuration at: %s" % SERVER_PATH, icon="fas fa-exclamation-triangle")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Highlights`

    Related Pages:

      https://getbootstrap.com/docs/4.3/components/alerts/

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param title: String. Optional.
    :param icon: String. Optional. The component icon content from font-awesome references
    :param type: Optional, The type of the warning. Can be (primary, secondary, success, danger, warning, info, light,
                 dark). Default danger
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    html_light = html.HtmlText.Highlights(self.page, text, title, icon, type, color, width,
                                          height, html_code, helper, options or {}, profile)
    return html_light

  @html.Html.css_skin()
  def note(self, text=None, title="", icon=None, type="success", color=None, width=(None, "%"), height=(None, "px"),
           html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Provide contextual feedback messages for typical user actions with the handful of available and flexible
    alert messages.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Highlights`

    Related Pages:

      https://getbootstrap.com/docs/4.3/components/alerts/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modal.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/popup_info.py

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component.
    :param title:
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param type: Optional. The type of the warning. Can be (primary, secondary, success, danger, warning, info, light,
                 dark). Default danger.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if type not in ['success', 'warning', 'danger']:
      raise Exception("This type %s is not recognised" % type)

    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_light = html.HtmlText.Highlights(self.page, text, title, icon, type, color, width,
                                          height, html_code, helper, options or {}, profile)
    html_light.style.css.border_left = "4px solid %s" % getattr(self.page.theme, type)[1]
    html_light.style.css.border_radius = 0
    return html_light

  @html.Html.css_skin()
  def formula(self, text=None, width=(100, "%"), height=(None, 'px'), html_code=None, color=None, helper=None,
              align="left", options=None, profile=None):
    """
    Description:
    ------------
    Interface to the mathjax Formulas object.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.formula("$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$", helper="This is a formula")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.Formula`

    Related Pages:

      https://mathjax.org/docs/index.html

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param align: String. Optional. The text-align property within this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_formula = html.HtmlTextComp.Formula(self.page, text, width, height, color, html_code, helper, options, profile)
    html_formula.style.css.text_align = align
    if align in ["center", 'right']:
      html_formula.style.css.margin = "auto"
      html_formula.style.css.display = "block"
    return html_formula

  @html.Html.css_skin()
  def code(self, text="", language='python', color=None, width=(90, '%'), height=(200, 'px'), html_code=None,
           options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Python Wrapper to the Bootstrap CODE Tag.
    This entry point compare to the ui.codes will be by default readonly.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.code("This is a code")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://v4-alpha.getbootstrap.com/content/code/

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param language: String. Optional. The language used in the code cell.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': language, 'matchBrackets': True, 'styleActiveLine': True,
                    'autoRefresh': True, 'readOnly': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(
      self.page, text, color, width, height, html_code, dflt_options, helper, profile)
    return html_code

  @html.Html.css_skin()
  def paragraph(self, text="", color=None, background_color=None, border=False, width=(100, "%"),
                height=(None, 'px'), html_code=None, encoding="UTF-8", helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Python Wrapper to the HTML P Tag.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.paragraph("This is a paragraph", helper="Paragraph helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Paragraph`

    Related Pages:

      https://www.w3schools.com/html/html_styles.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param color: String. Optional. The font color in the component. Default inherit.
    :param background_color: String.
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param encoding: String. Optional.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"reset": True, 'markdown': False, "classes": []}
    if options is not None:
      dflt_options.update(options)
    text = self.page.py.encode_html(text.strip())
    text = text.replace("\n\n", "<br><br>")
    if dflt_options.get("initial-letter", False):
      text = '<span style="line-height:%spx;font-size:%spx;vertical-align:bottom">%s</span>%s' % (
        dflt_options.get("initial-letter"), options.get("initial-letter"), text[0], text[1:])
    html_paragraph = html.HtmlText.Paragraph(self.page, text, color, background_color, border, width, height,
                                             html_code, encoding, helper, dflt_options, profile)
    return html_paragraph

  @html.Html.css_skin()
  def preformat(self, text=None, color=None, width=(90, '%'), height=(None, 'px'), html_code=None, options=None,
                helper=None, profile=None):
    """
    Description:
    ------------
    Preformatted text:
    The <pre> tag defines preformatted text.
    Text in a <pre> element is displayed in a fixed-width font (usually Courier), and it preserves both spaces
    and line breaks.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.preformat("This is a pre formatted text")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Pre`

    Related Pages:

      https://www.w3schools.com/html/html_styles.asp
      https://www.w3schools.com/tags/tag_pre.asp

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"reset": True, 'markdown': False}
    if options is not None:
      dflt_options.update(options)
    text = self.page.py.encode_html(text)
    html_pre = html.HtmlText.Pre(
      self.page, text, color, width, height, html_code, dflt_options, helper, profile)
    return html_pre

  @html.Html.css_skin()
  def blockquote(self, text=None, author=None, color=None, width=(None, '%'), height=(None, 'px'),
                 html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    The <blockquote> tag specifies a section that is quoted from another source.
    Browsers usually indent <blockquote> elements.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.blockquote("This is a code")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.BlockQuote`

    Related Pages:

      https://v4-alpha.getbootstrap.com/content/typography/
      https://www.w3schools.com/TAGS/tag_blockquote.asp

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component.
    :param author: String. Optional. The quote's author.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    html_blockquote = html.HtmlText.BlockQuote(
      self.page, text, author, color, width, height, html_code, helper, options, profile)
    return html_blockquote

  @html.Html.css_skin()
  def up_down(self, record=None, components=None, color=None, label=None, width=(100, "%"), height=(330, "px"),
              options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Up and down Text component.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.up_down({'previous': 240885, 'value': 240985})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.UpDown`

    Related Pages:

      https://fontawesome.com/

    Attributes:
    ----------
    :param record: Dictionary. Optional. The component inputs.
    :param components: HTML Component. List of HTML component to be added.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param label: String. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"digits": 0, 'thousand_sep': ",", 'decimal_sep': ".",
                    'font_size': self.page.body.style.globals.font.normal(),
                    'red': self.page.theme.danger[1], 'green': self.page.theme.success[1],
                    'orange': self.page.theme.warning[1]}
    if options is not None:
      dflt_options.update(options)
    html_up_down = html.HtmlTextComp.UpDown(
      self.page, record, components, color, label, width, height, dflt_options, helper, profile)
    return html_up_down

  @html.Html.css_skin()
  def number(self, number=0, title=None, label=None, icon=None, color=None, align="left", tooltip='', html_code=None,
             options=None, helper=None, width=(150, 'px'), profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.number(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Numeric`

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param number: Integer. Optional. The value to be displayed to the component. Default 0.
    :param title: String. Optional. The text title.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param align: String. Optional. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    dflt_options = {"digits": 0, "thousand_sep": ',', "decimal_sep": '.'}
    if options is not None:
      dflt_options.update(options)
    html_number = html.HtmlText.Numeric(self.page, number, title, label, icon, color, tooltip, html_code,
                                        dflt_options, helper, width, profile)
    if align == "center":
      html_number.style.css.margin = "auto"
      html_number.style.css.display = "block"
    return html_number

  @html.Html.css_skin()
  def title(self, text="", level=None, name=None, contents=None, color=None, picture=None, icon=None,
            top=5, html_code=None, width=("auto", ""), height=(None, "px"), align=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a title.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.title("Test")
      page.ui.title("Test", level=2)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Title`

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param level:
    :param name:
    :param contents:
    :param color: String. Optional. The font color in the component. Default inherit.
    :param picture:
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param top: Integer. Optional. The margin top in pixel.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"reset": True, 'markdown': False}
    if options is not None:
      dflt_options.update(options)
    text = self.page.py.encode_html(text)
    html_title = html.HtmlText.Title(self.page, text, level, name, contents, color, picture, icon,
                                     top, html_code, width, height, align, dflt_options, profile)
    html_title.style.css.text_transform = "uppercase"
    return html_title

  @html.Html.css_skin()
  def fieldset(self, legend="", width=(100, "%"), height=(None, "px"), helper=None, options=None, profile=None):
    """
    Description:
    ------------
    The <fieldset> tag is used to group related elements in a form.
    The <fieldset> tag draws a box around the related elements.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.fieldset("legend")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Fieldset`

    Related Pages:

      https://www.w3schools.com/tags/tag_legend.asp
      https://www.w3schools.com/tags/tag_fieldset.asp

    Attributes:
    ----------
    :param legend: String. Optional. The legend value.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_fieldset = html.HtmlText.Fieldset(self.page, legend, width=width, height=height, helper=helper,
                                           options=options, profile=profile)
    return html_fieldset

  @html.Html.css_skin()
  def col(self, text, label, align='left', width=('auto', ""), height=(None, "px"), html_code=None, options=None,
          profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param label: String. Optional. The text of label to be added to the component.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    div.label = self.page.ui.text(
      label, options=options, html_code=html_code if html_code is None else "%s_label" % html_code, profile=profile)
    div.label.style.css.display = 'block'
    div.label.style.css.margin_bottom = 10
    div.label.style.css.color = self.page.theme.greys[6]
    div.text = self.page.ui.text(
      text, options=options, html_code=html_code if html_code is None else "%s_text" % html_code, profile=profile)
    div.text.style.css.bold()
    div.text.style.css.margin_bottom = 10
    div.text.style.css.display = 'block'
    div.text.style.css.font_factor(5)
    div.style.css.margin = 4
    div.add(div.label)
    div.add(div.text)
    return div

  @html.Html.css_skin()
  def alert(self, text=None, title=None, icon=None, type=None, color=None, width=('400', "px"), height=(None, "px"),
            html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Provide contextual feedback messages for typical user actions with the handful of available and flexible
    alert messages.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")
      page.ui.texts.highlights("Server configuration at: %s" % SERVER_PATH,  icon="fas fa-exclamation-triangle")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Highlights`

    Related Pages:

      https://getbootstrap.com/docs/4.3/components/alerts/

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component.
    :param title: String. Optional.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param type: Optional, The type of the warning. Can be (primary, secondary, success, danger, warning, info, light,
                 dark). Default danger.
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    html_light = html.HtmlText.Highlights(
      self.page, text, title, icon, type or "info", color, width, height, html_code, helper, options or {}, profile)
    html_light.style.css.position = "fixed"
    html_light.style.css.bottom = 10
    html_light.style.css.padding = "15px 20px"
    html_light.style.css.border_radius = 10
    if type is None:
      html_light.style.css.color = self.page.theme.greys[0]
      html_light.style.css.background_color = self.page.theme.colors[-1]
    html_light.style.css.right = 10
    html_light.style.css.z_index = 1500
    return html_light

  @property
  def references(self):
    """
    Description:
    ------------
    More custom toggles icons.
    """
    return TextReferences(self)

  @html.Html.css_skin()
  def button(self, text, icon=None, width=('auto', ""), tooltip=None, height=(None, "px"), html_code=None, profile=None,
             options=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    c = self.page.ui.text(
      text, tooltip=tooltip, width=width, html_code=html_code, height=height, profile=profile, options=options)
    c.add_icon(icon, html_code=html_code)
    c.style.add_classes.div.background_hover()
    c.style.css.border_radius = 5
    c.style.css.font_size = self.page.body.style.globals.font.normal(-2)
    c.style.css.padding = '1px 2px'
    return c


class TextReferences:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def book(self, text, author=None, name=None, edition=None, year=None, page=None, html_code=None, profile=None,
           options=None):
    """
    Description:
    ------------
    Shortcut to quote an extra from a book.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:


    Attributes:
    ----------
    :param text: String. Optional. The text of the quote.
    :param author: String. Optional. The author.
    :param name: String. Optional.
    :param edition:
    :param year:
    :param page:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    content = "« %s » <sup style='cursor:pointer;color:blue;text-decoration:underline' title='%s. %s, %s. %s, p. %s'>&#x2a;</sup>"
    text = self.page.ui.text(content % (text, author, name, edition, year, page), html_code=html_code, options=options,
                             profile=profile)
    text.style.css.color = self.page.theme.colors[4]
    return text

  @html.Html.css_skin()
  def website(self, author=None, name=None, site=None, url=None, html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    Shortcut to data reference from another website.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://en.wikipedia.org/wiki/Wikipedia:Citing_sources
      https://apastyle.apa.org/style-grammar-guidelines/references/examples/webpage-website-references

    Attributes:
    ----------
    :param author: String. Optional. The author.
    :param name: String. Optional. The name of the page.
    :param site: String. Optional. The website name.
    :param url: String. Optional. The url link to the data.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    split_url = url.split("/")
    if site is None:
      site = split_url[2]
    if name is None:
      name = split_url[-1]
    if author is not None:
      text = self.page.ui.text("%s, %s, <a style='font-style:italic' href='%s'>%s</a>" % (
        author, name, url, site.upper()), align="right", html_code=html_code, options=options, profile=profile)
    else:
      text = self.page.ui.text("%s, <a style='font-style:italic' href='%s'>%s</a>" % (
         name, url, site.upper()), align="right", html_code=html_code, options=options, profile=profile)
    text.style.css.color = self.page.theme.colors[4]
    return text

  def github(self, url=None, html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    Shortcut to data reference from github.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://en.wikipedia.org/wiki/Wikipedia:Citing_sources
      https://apastyle.apa.org/style-grammar-guidelines/references/examples/webpage-website-references

    Attributes:
    ----------
    :param url: String. Optional. The url link to the data.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    split_url = url.split("/")
    author, name = split_url[3], split_url[4]
    site = "github"
    text = self.page.ui.text("%s, %s: <a style='font-style:italic' href='%s'>%s</a>" % (
      author, site, url, name), align="right", html_code=html_code, options=options, profile=profile)
    text.style.css.color = self.page.theme.colors[4]
    return text
