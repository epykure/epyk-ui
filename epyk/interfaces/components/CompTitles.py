
from epyk.core import html
from epyk.core.css import Defaults_css


class Titles(object):

  def __init__(self, context):
    self.context = context

  def head(self, text=None, options=None, tooltip="", width=(100, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.color = self.context.rptObj.theme.colors[-1]
    html_title.style.css.border_left = '5px solid %s' % self.context.rptObj.theme.colors[-1]
    html_title.style.css.font_size = Defaults_css.font(15)
    html_title.style.css.text_transform = 'uppercase'
    html_title.style.css.margin_left = 2
    html_title.style.css.padding_left = 2
    html_title.style.css.bold()
    return html_title

  def headline(self, text=None, options=None, tooltip="", width=(100, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(4)
    html_title.style.css.color = self.context.rptObj.theme.colors[-1]
    html_title.style.css.font_style = 'italic'
    return html_title

  def title(self, text=None, options=None, tooltip="", width=(100, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(6)
    return html_title

  def rubric(self, text=None, options=None, tooltip="", width=(100, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.border_left = '3px solid %s' % self.context.rptObj.theme.colors[-1]
    html_title.style.css.font_size = Defaults_css.font(6)
    return html_title

  def caption(self, text=None, options=None, tooltip="", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(4)
    html_title.style.css.color = self.context.rptObj.theme.colors[-1]
    return html_title

  def underline(self, text=None, options=None, tooltip="", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip,
                                           dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(6)
    html_title.style.css.border_bottom = '2px solid %s' % self.context.rptObj.theme.colors[-1]
    return html_title
