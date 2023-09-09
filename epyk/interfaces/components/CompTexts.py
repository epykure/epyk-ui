#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import types
from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.css import Defaults as default_css
from epyk.core.html import Defaults as default_html


class TextReferences:

  def __init__(self, ui):
    self.page = ui.page

  def book(self, text, author=None, name=None, edition=None, year=None, page=None, html_code=None, profile=None,
           options=None):
    """
    Shortcut to quote an extra from a book.

    :tags:
    :categories:

    Usage::

    Related Pages:


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
    html.Html.set_component_skin(text)
    return text

  def website(self, author=None, name=None, site=None, url=None, html_code=None, profile=None, options=None):
    """
    Shortcut to data reference from another website.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://en.wikipedia.org/wiki/Wikipedia:Citing_sources
      https://apastyle.apa.org/style-grammar-guidelines/references/examples/webpage-website-references

    :param author: String. Optional. The author.
    :param name: String. Optional. The name of the page.
    :param site: String. Optional. The website name.
    :param url: String. Optional. The url link to the data.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    dfl_options = {"link_css": {
      "font-style": "italic", "font-size": self.page.body.style.globals.font.normal(-3)}}
    if options is not None and options.get("link_css") is not None:
      dfl_options["link_css"] = dict(options.get("link_css"))
    split_url = url.split("/")
    if site is None:
      site = split_url[2]
    if name is None:
      name = split_url[-1]
    if author is not None:
      text = self.page.ui.text("%s, %s, <a style='%s' href='%s'>%s</a>" % (
        author, name, default_css.inline(dfl_options["link_css"]), url, site.upper()),
                               align="right", html_code=html_code, options=options, profile=profile)
    else:
      text = self.page.ui.text("%s, <a style='%s' href='%s'>%s</a>" % (
         name, default_css.inline(dfl_options["link_css"]), url, site.upper()),
                               align="right", html_code=html_code, options=options, profile=profile)
    text.style.css.color = self.page.theme.colors[4]
    html.Html.set_component_skin(text)
    return text

  def github(self, url=None, html_code=None, profile=None, options=None):
    """
    Shortcut to data reference from github.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://en.wikipedia.org/wiki/Wikipedia:Citing_sources
      https://apastyle.apa.org/style-grammar-guidelines/references/examples/webpage-website-references

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
    html.Html.set_component_skin(text)
    return text


class Texts:

  def __init__(self, ui):
    self.page = ui.page

  def text(self, text: str = "", color: str = None, align: str = 'left', width: types.SIZE_TYPE = ('auto', ""),
           height: types.SIZE_TYPE =(None, "px"), html_code: str = None, tooltip: str = None, options: dict = None,
           helper: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlText.Text:
    """
    Add the HTML text component to the page.

    Usage::

      page.ui.text("this is a test")

      txt = page.ui.text('''
        This text is ___really important___.
        This text is __*really important*__.
        This text is **_really important_**.  
        This is really***very***important text.
      ''')
      txt.options.markdown = True

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

    :param text: The string value to be displayed in the component.
    :param color: Optional. The color of the text.
    :param align: Optional. The position of the icon in the line (left, right, center).
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param options: Optional. The component options.
    :param helper: Optional. A tooltip helper.
    :param profile: A flag to set the component performance storage.
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
    html.Html.set_component_skin(text_comp)
    return text_comp

  def block(self, text: str = "", color: str = None, align: str = 'left', width: types.SIZE_TYPE =(100, "%"),
            height: types.SIZE_TYPE =(None, "px"), html_code: str = None, tooltip: str = None, options: dict = None,
            helper: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlText.Text:
    """
    Add the HTML text component to the page.

    :tags:
    :categories:

    Usage::

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

    :param text: Optional. The string value to be displayed in the component.
    :param color: Optional. The color of the text.
    :param align: Optional. The position of the icon in the line (left, right, center).
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param options: Optional. Specific Python options available for this component.
    :param helper: Optional. The value to be displayed to the helper icon.
    :param profile: Optional. A flag to set the component performance storage.
    """
    text_comp = self.text(text, color, align, width, height, html_code, tooltip, options, helper, profile)
    text_comp.style.css.display = "inline-block"
    text_comp.style.css.text_align = "left"
    html.Html.set_component_skin(text_comp)
    return text_comp

  def absolute(self, text: str, size_notch: int = None, top: types.SIZE_TYPE = (50, "%"),
               left: types.SIZE_TYPE = (50, "%"), bottom: types.SIZE_TYPE = None, align: str = 'left',
               width: types.SIZE_TYPE =('auto', ""), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
               options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlText.Text:
    """

    :tags:
    :categories:

    Usage::

    :param text: Optional. The value to be displayed to the component
    :param size_notch:
    :param top: Optional. A tuple with the integer for the component's distance to the top of the page
    :param left: Optional. A tuple with the integer for the component's distance to the left of the page
    :param bottom: Optional. A tuple with the integer for the component's distance to the bottom of the page
    :param align: Optional. The text-align property within this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
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
    html.Html.set_component_skin(text_comp)
    return text_comp

  def label(self, text: str = "", color: str = None, align: str = 'center',
            width: types.SIZE_TYPE = (default_html.INPUTS_MIN_WIDTH, "px"),
            height: types.SIZE_TYPE = ('auto', ""), html_code: str = None, tooltip: str = '',
            profile: types.PROFILE_TYPE = None, options: dict = None) -> html.HtmlText.Label:
    """
    The <label> tag defines a label for a <button>, <input>, <meter>, <output>, <progress>, <select>,
    or <textarea> element...

    The for attribute of the <label> tag should be equal to the id attribute of the related element to bind
    them together.

    :tags:
    :categories:

    Usage::

      page.ui.texts.label("Test")
      page.ui.texts.label("this is a test", color="red")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Label`

    Related Pages:

      https://www.w3schools.com/tags/tag_label.asp

    :param text: Optional. The string value to be displayed in the component
    :param color: Optional. The color of the text
    :param align: Optional. The position of the icon in the line (left, right, center)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"markdown": True}
    if options is not None:
      dflt_options.update(options)
    text = self.page.py.encode_html(text)
    html_label = html.HtmlText.Label(self.page, text, color, align, width, height, html_code, tooltip,
                                     profile, dflt_options)
    html.Html.set_component_skin(html_label)
    return html_label

  def span(self, text: str = "", color: str = None, align: str = 'center', width: types.SIZE_TYPE = None,
           height: types.SIZE_TYPE = None, html_code: str = None, tooltip: str = None, options: dict = None,
           profile: types.PROFILE_TYPE = None) -> html.HtmlText.Span:
    """
    The <span> tag is used to group inline-elements in a document.

    The <span> tag provides no visual change by itself.

    The <span> tag provides a way to add a hook to a part of a text or a part of a document.

    :tags:
    :categories:

    Usage::

      page.ui.texts.span("Test")

      span = page.ui.texts.span("youpi")
      span.mouse([
        span.dom.css("color", "red"),
        span.dom.css("cursor", "pointer").r],
        span.dom.css("color", "blue").r)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Span`

    Related Pages:

      https://www.w3schools.com/tags/tag_span.asp

    :param text: Optional. The string value to be displayed in the component
    :param color: Optional. The color of the text
    :param align: Optional. The position of the icon in the line (left, right, center)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_label = html.HtmlText.Span(self.page, text, color, align, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_label)
    return html_label

  def highlights(self, text: str = None, title: str = None, icon: str = None, type: str = "danger", color: str = None,
                 width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
                 helper: str = None, options: dict = None,
                 profile: types.PROFILE_TYPE = None) -> html.HtmlText.Highlights:
    """
    Provide contextual feedback messages for typical user actions with the handful of available and flexible
    alert messages.

    :tags:
    :categories:

    Usage::

      page.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")
      page.ui.texts.highlights("Server configuration at: %s" % SERVER_PATH, icon="fas fa-exclamation-triangle")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Highlights`

    Related Pages:

      https://getbootstrap.com/docs/4.3/components/alerts/

    :param text: Optional. The string value to be displayed in the component
    :param title: Optional.
    :param icon: Optional. The component icon content from font-awesome references
    :param type: Optional. The type of the warning. Can be (primary, secondary, success, danger, warning,
      info, light, dark). Default danger
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    html_light = html.HtmlText.Highlights(self.page, text, title, icon, type, color, width,
                                          height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(html_light)
    return html_light

  def note(self, text: str = None, title: str = "", icon: str = None, category: str = "success", color: str = None,
           width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"),
           html_code: str = None, helper: str = None, options: types.OPTION_TYPE = None,
           profile: types.PROFILE_TYPE = None) -> html.HtmlText.Highlights:
    """
    Provide contextual feedback messages for typical user actions with the handful of available and flexible
    alert messages.

    :tags:
    :categories:

    Usage::

      page.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Highlights`

    Related Pages:

      https://getbootstrap.com/docs/4.3/components/alerts/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modal.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/popup_info.py

    :param text: Optional. The string value to be displayed in the component
    :param title:
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param category: Optional. The type of the warning. Can be
      (primary, secondary, success, danger, warning, info, light, dark). Default danger
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. The value to be displayed to the helper icon
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    if category not in ['success', 'warning', 'danger']:
      raise ValueError("This type %s is not recognised" % category)

    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_light = html.HtmlText.Highlights(self.page, text, title, icon, category, color, width,
                                          height, html_code, helper, options or {}, profile)
    html_light.style.css.border_left = "4px solid %s" % getattr(self.page.theme, category)[1]
    html_light.style.css.border_radius = 0
    html.Html.set_component_skin(html_light)
    return html_light

  def formula(self, text: str = None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, 'px'),
              html_code: str = None, color: str = None, helper: str = None,
              align: str = "left", options: dict = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlTextComp.Formula:
    """
    Interface to the mathjax Formulas object.

    :tags:
    :categories:

    Usage::

      page.ui.texts.formula("$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$", helper="This is a formula")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.Formula`

    Related Pages:

      https://mathjax.org/docs/index.html

    :param text: Optional. The string value to be displayed in the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: Optional. The font color in the component. Default inherit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. The value to be displayed to the helper icon
    :param align: Optional. The text-align property within this component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_formula = html.HtmlTextComp.Formula(self.page, text, width, height, color, html_code, helper, options, profile)
    html_formula.style.css.text_align = "%s !IMPORTANT" % align
    if align in ["center", 'right']:
      html_formula.style.css.margin = "auto"
      html_formula.style.css.display = "block"
    html.Html.set_component_skin(html_formula)
    return html_formula

  def code(self, text: str = "", language: str = 'python', color: str = None, width: types.SIZE_TYPE = (90, '%'),
           height: types.SIZE_TYPE = (200, 'px'), html_code: str = None,
           options: dict = None, helper: str = None, profile: types.PROFILE_TYPE = None):
    """
    Python Wrapper to the Bootstrap CODE Tag.
    This entry point compare to the ui.codes will be by default readonly.

    :tags:
    :categories:

    Usage::

      page.ui.texts.code("This is a code")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://v4-alpha.getbootstrap.com/content/code/

    :param text: Optional. The string value to be displayed in the component
    :param language: Optional. The language used in the code cell
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: Optional. The font color in the component. Default inherit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. The value to be displayed to the helper icon
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': language, 'matchBrackets': True, 'styleActiveLine': True,
                    'autoRefresh': True, 'readOnly': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.CodeEditor(
      self.page, text, color, width, height, html_code, dflt_options, helper, profile)
    html.Html.set_component_skin(html_code)
    return html_code

  def paragraph(self, text: str = "", color: str = None, background_color: str = None, border: bool = False,
                width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
                encoding: str = "UTF-8", helper: str = None, options: dict = None,
                profile: types.PROFILE_TYPE = None) -> html.HtmlText.Paragraph:
    """
    Python Wrapper to the HTML P Tag.

    :tags:
    :categories:

    Usage::

      page.ui.texts.paragraph("This is a paragraph", helper="Paragraph helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Paragraph`

    Related Pages:

      https://www.w3schools.com/html/html_styles.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    :param text: Optional. The string value to be displayed in the component
    :param color: Optional. The font color in the component. Default inherit
    :param background_color:
    :param border:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param encoding: Optional.
    :param helper: Optional. The value to be displayed to the helper icon
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
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
    html.Html.set_component_skin(html_paragraph)
    return html_paragraph

  def preformat(self, text: str = None, color: str = None, width: types.SIZE_TYPE = (90, '%'),
                height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
                helper: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlText.Pre:
    """
    Preformatted text:
    The <pre> tag defines preformatted text.
    Text in a <pre> element is displayed in a fixed-width font (usually Courier), and it preserves both spaces
    and line breaks.

    :tags:
    :categories:

    Usage::

      page.ui.texts.preformat("This is a pre formatted text")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Pre`

    Related Pages:

      https://www.w3schools.com/html/html_styles.asp
      https://www.w3schools.com/tags/tag_pre.asp

    :param text: Optional. The string value to be displayed in the component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. The value to be displayed to the helper icon
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"reset": True, 'markdown': False}
    if options is not None:
      dfl_options.update(options)
    text = self.page.py.encode_html(text)
    html_pre = html.HtmlText.Pre(
      self.page, text, color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(html_pre)
    return html_pre

  def blockquote(self, text: str = None, author: str = None, color: str = None, width: types.SIZE_TYPE = (None, '%'),
                 height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, helper: str = None,
                 options: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlText.BlockQuote:
    """
    The <blockquote> tag specifies a section that is quoted from another source.
    Browsers usually indent <blockquote> elements.

    :tags:
    :categories:

    Usage::

      page.ui.texts.blockquote("This is a code")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.BlockQuote`

    Related Pages:

      https://v4-alpha.getbootstrap.com/content/typography/
      https://www.w3schools.com/TAGS/tag_blockquote.asp

    :param text: Optional. The string value to be displayed in the component
    :param author: Optional. The quote's author
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. The value to be displayed to the helper icon
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    html_blockquote = html.HtmlText.BlockQuote(
      self.page, text, author, color, width, height, html_code, helper, options, profile)
    html.Html.set_component_skin(html_blockquote)
    return html_blockquote

  def up_down(self, record=None, components=None, color=None, label: str = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
              options: types.OPTION_TYPE = None, helper: str = None, profile: types.PROFILE_TYPE = None):
    """
    Up and down Text component.

    :tags:
    :categories:

    Usage::

      page.ui.texts.up_down({'previous': 240885, 'value': 240985})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.UpDown`

    Related Pages:

      https://fontawesome.com/

    :param record: Optional. The component inputs
    :param components: List of HTML component to be added
    :param color: Optional. The font color in the component. Default inherit
    :param label: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param helper: Optional. The value to be displayed to the helper icon
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"digits": 0, 'thousand_sep': ",", 'decimal_sep': ".",
                    'font_size': self.page.body.style.globals.font.normal(),
                    'red': self.page.theme.danger.base, 'green': self.page.theme.success.base,
                    'orange': self.page.theme.warning.base}
    if options is not None:
      dflt_options.update(options)
    html_up_down = html.HtmlTextComp.UpDown(
      self.page, record, components, color, label, width, height, dflt_options, helper, profile)
    html.Html.set_component_skin(html_up_down)
    return html_up_down

  def number(self, number: int = 0, title: str = None, label: str = None, icon: str = None, color: str = None,
             align: str = "left", tooltip: str = '',
             html_code=None, options: types.OPTION_TYPE = None, helper: str = None,
             width: types.SIZE_TYPE = (150, 'px'), profile: types.PROFILE_TYPE = None):
    """

    :tags:
    :categories:

    Usage::

      page.ui.texts.number(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Numeric`

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    :param number: Optional. The value to be displayed to the component. Default 0
    :param title: Optional. The text title
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param color: Optional. The font color in the component. Default inherit
    :param align: Optional. The text-align property within this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param tooltip: Optional. A string with the value of the tooltip
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. The value to be displayed to the helper icon
    :param profile: Optional. A flag to set the component performance storage
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
    html.Html.set_component_skin(html_number)
    return html_number

  def title(self, text: Union[str, dict] = "", level=None, name: str = None, contents=None,
            color=None, picture: str = None, icon: str = None,
            top: int = 5, html_code: str = None, width: types.SIZE_TYPE = ("auto", ""),
            height: types.SIZE_TYPE = (None, "px"), align: str = None, options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None):
    """
    Add a title.

    :tags:
    :categories:

    Usage::

      page.ui.title("Test")
      page.ui.title("Test", level=2)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Title`

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp

    :param text: Optional. The value to be displayed to the component.
    :param level:
    :param name:
    :param contents:
    :param color: Optional. The font color in the component. Default inherit.
    :param picture:
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param top: Optional. The margin top in pixel
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. The text-align property within this component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if isinstance(text, dict):
      sub_title = self.page.ui.div(list(text.values())[0])
      sub_title.options.managed = False
      sub_title.style.css.italic()
      sub_title.style.css.color = self.page.theme.greys[4]
      sub_title.style.css.text_transform = "lowercase"
      sub_title.style.css.display = "inline"
      sub_title.style.css.font_size = self.page.body.style.globals.font.normal(-3)
      text = "<b>%s</b> %s" % (list(text.keys())[0], sub_title.html())
    dflt_options = {"reset": True, 'markdown': False}
    if options is not None:
      dflt_options.update(options)
    text = self.page.py.encode_html(text)
    if color is True:
      color = self.page.theme.notch()
    html_title = html.HtmlText.Title(self.page, text, level, name, contents, color, picture, icon,
                                     top, html_code, width, height, align, dflt_options, profile)
    html_title.style.css.text_transform = "uppercase"
    html.Html.set_component_skin(html_title)
    return html_title

  def fieldset(self, legend: str = "", width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"),
               helper: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    The <fieldset> tag is used to group related elements in a form.
    The <fieldset> tag draws a box around the related elements.

    :tags:
    :categories:

    Usage::

      page.ui.texts.fieldset("legend")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Fieldset`

    Related Pages:

      https://www.w3schools.com/tags/tag_legend.asp
      https://www.w3schools.com/tags/tag_fieldset.asp

    :param legend: Optional. The legend value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. The value to be displayed to the helper icon
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_fieldset = html.HtmlText.Fieldset(self.page, legend, width=width, height=height, helper=helper,
                                           options=options, profile=profile)
    html.Html.set_component_skin(html_fieldset)
    return html_fieldset

  def col(self, text: str, label: str, align: str = 'left', width: types.SIZE_TYPE = ('auto', ""),
          height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
          options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """

    :tags:
    :categories:

    Usage::

    :param text: Optional. The value to be displayed to the component
    :param label: Optional. The text of label to be added to the component
    :param align: Optional. The text-align property within this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
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
    html.Html.set_component_skin(div)
    return div

  def alert(self, text: str = None, title: str = None, icon: str = None, category: str = None, color: str = None,
            width: types.SIZE_TYPE = ('400', "px"), height: types.SIZE_TYPE = (None, "px"),
            html_code: str = None, helper: str = None, options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None):
    """
    Provide contextual feedback messages for typical user actions with the handful of available and flexible
    alert messages.

    :tags:
    :categories:

    Usage::

      page.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")
      page.ui.texts.highlights("Server configuration at: %s" % SERVER_PATH,  icon="fas fa-exclamation-triangle")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Highlights`

    Related Pages:

      https://getbootstrap.com/docs/4.3/components/alerts/

    :param text: Optional. The string value to be displayed in the component
    :param title: Optional.
    :param icon: Optional. The component icon content from font-awesome references
    :param category: Optional. The type of the warning. Can be (primary, secondary, success, danger, warning,
     info, light, dark). Default danger
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    text = self.page.py.encode_html(text)
    html_light = html.HtmlText.Highlights(
      self.page, text, title, icon, category or "info", color, width, height, html_code, helper, options or {}, profile)
    html_light.style.css.position = "fixed"
    html_light.style.css.bottom = 10
    html_light.style.css.padding = "15px 20px"
    html_light.style.css.border_radius = 10
    if category is None:
      html_light.style.css.color = self.page.theme.greys[0]
      html_light.style.css.background_color = self.page.theme.colors[-1]
    html_light.style.css.right = 10
    html_light.style.css.z_index = 1500
    html.Html.set_component_skin(html_light)
    return html_light

  @property
  def references(self) -> TextReferences:
    """
    More custom toggles icons.
    """
    return TextReferences(self)

  def button(self, text: str, icon: str = None, width: types.SIZE_TYPE = ('auto', ""), tooltip: str = None,
             height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
             profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None):
    """   

    :tags:
    :categories:

    Usage::

    Templates:

    :param text: Optional. The value to be displayed to the button
    :param icon: Optional. The component icon content from font-awesome references
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    c = self.page.ui.text(
      text, tooltip=tooltip, width=width, html_code=html_code, height=height, profile=profile, options=options)
    c.add_icon(icon, html_code=html_code)
    c.style.add_classes.div.background_hover()
    c.style.css.border_radius = 5
    c.style.css.font_size = self.page.body.style.globals.font.normal(-2)
    c.style.css.padding = '1px 2px'
    html.Html.set_component_skin(c)
    return c

  def date(self, value=None, label: str = None, icon: str = False, color: str = None,
           width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = (None, "px"),
           html_code: str = None, profile: types.PROFILE_TYPE = None,
           options: types.OPTION_TYPE = None, helper: str = None):
    """
    This component is based on the Jquery Date Picker object.

    :tags:
    :categories:

    Usage::

      page.ui.texts.date('2020-04-08', label="Date").included_dates(["2020-04-08", "2019-09-06"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

      https://jqueryui.com/datepicker/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/dates.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    html_dt = self.page.ui.date(
        value, label=label, icon=icon, color=color, width=width, height=height, html_code=html_code,
        profile=profile, options=options, helper=helper)
    html_dt.input.style.css.background = "inherit"
    html_dt.input.style.css.border = None
    html.Html.set_component_skin(html_dt)
    return html_dt
