

class Icons:

  def __init__(self, context):
    self.context = context

  def icon(self, icon, text="", tooltip=None, position="center", width=(25, 'px'), height=(25, 'px'), htmlCode=None,
           options=None, profile=None):
    """
    Description:
    ------------
    Add icon using Bootstrap icons framework.

    Related Pages:

      https://icons.getbootstrap.com/

    Attributes:
    ----------
    :param icon:
    """
    component = self.context.rptObj.ui.tags.i(text, width=width, height=height, tooltip=tooltip, htmlCode=htmlCode,
                                         options=options, profile=profile)
    component.attr["class"].add(icon)
    component.style.css.inline_block()
    component.style.css.text_align = position
    component.style.css.font_size = "%spx" % (width[0] - 10)
    return component

  def warning(self, icon="bi bi-exclamation-triangle-fill", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    component.style.css.color = self.context.rptObj.theme.warning[1]
    return component

  def danger(self, icon="bi bi-x-octagon-fill", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    component.style.css.color = self.context.rptObj.theme.danger[1]
    return component

  def clock(self, icon="bi bi-clock", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    return component

  def next(self, icon="bi bi-caret-right-fill", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    return component

  def previous(self, icon="bi bi-caret-left-fill", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    return component

  def zoom_in(self, icon="bi bi-zoom-in", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    return component

  def zoom_out(self, icon="bi bi-zoom-ou", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    return component

  def delete(self, icon="bi bi-trash-fill", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    return component

  def capture(self, icon="bi bi-clipboard", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    return component

  def table(self, icon="bi bi-tabl", text="", tooltip=None, position="center", width=(25, 'px'),
             height=(25, 'px'), htmlCode=None, options=None, profile=None):
    component = self.icon(icon, text, tooltip, position, width, height, htmlCode, options, profile)
    return component

