
from epyk.core.html import Html
from epyk.core.html.options import OptPanel
from epyk.core.js.packages import JsQuery


class Popup(Html.Html):
  requirements = ('bootstrap', )
  name = 'Popup Container'

  def __init__(self, report, components, width, height, options, profile):
    super(Popup, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.height, self.width = "%s%s" % (height[0], height[1]) if height is not None else "100%", width
    self.__options = OptPanel.OptionPopup(self, options)
    if not isinstance(components, list):
      components = [components]
    for component in components:
      self.__add__(component)

    if self.options.background:
      self.frameWidth = "%s%s" % (width[0], width[1])
      self.css({'width': '100%', 'position': 'fixed', 'height': '100%', 'background-color': 'rgba(0,0,0,0.4)', 'left': 0, 'top': 0, 'margin': 'auto'})
      self.css({'display': 'none', 'z-index': '10000', 'text-align': 'center', 'padding-top': '100px', 'padding-left': self.options.margin, 'padding-right': self.options.margin})
    else:
      self.frameWidth = "100%"
      self.css({'position': 'absolute', 'margin': 0, 'padding': 0, 'display': 'none', 'z-index': '10000'})

    if self.options.draggable:
      self.draggable(source_event=JsQuery.decorate_var(self.dom.querySelector("#%s_content" % self.htmlCode)))
    self.set_attrs(name="name", value="report_popup")
    self.keyup.escape(self.dom.hide().r, source_event="document")

  @property
  def options(self):
    """
    Property to set all the possible object for a button

    :rtype: OptPanel.OptionPopup
    """
    return self.__options

  def html(self):
    trTitle, closePopup = '', ''
    str_html = "\n".join([val.html() if hasattr(val, 'html') else str(val) for val in self.val])
    content = '''
      <table id="%(htmlCode)s_table" style="width:%(frameWidth)s;margin:auto">
        %(title)s
        <tr>
          <td style="padding:10px">
            <div style="width:100%%;text-align:right">%(closePopup)s</div>
            <div  class='scroll_content' id="%(htmlCode)s_content" style="overflow:auto;width:100%%">%(objects)s</div>
          </td>
        </tr>
      </table>''' % {'title': trTitle, 'htmlCode': self.htmlCode, 'objects': str_html, 'height': self.height, "frameWidth": self.frameWidth, 'closePopup': closePopup}
    return '''<div %s>%s</div>''' % (self.get_attrs(pyClassNames=self.style.get_classes()), content)
