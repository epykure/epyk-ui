"""
CSS Style module for the Image components
"""


from epyk.core.css.styles import CssStyle


class CssImgBasic(CssStyle.CssCls):
  attrs = {'display': 'inline-block', 'position': 'relative', 'height': 'auto', 'max-height': '100%', 'max-width': '100%'}
  cssId = {'child': 'img'}


class CssImgParagraph(CssStyle.CssCls):
  attrs = {'transform': 'scale(1.1)', 'font-style': 'italic', 'padding': '10px', 'position': 'relative'}
  hover = {'transition': 'all 0.2s linear'}
  cssId = {'child': 'p'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.rptObj.theme.colors[0]})


class CssImgH2(CssStyle.CssCls):
  attrs = {'opacity': '0', 'transition': 'all 0.2s ease-in-out', 'text-transform': 'uppercase', 'text-align': 'center',
           'position': 'relative', 'padding': '10px', 'margin': '20px 0 0 0'}
  hover = {'opacity': 1, 'transform': 'translateY(0px)'}
  cssId = {'child': 'h2'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.rptObj.theme.colors[0]})


class CssImgMask(CssStyle.CssCls):
  attrs = {'opacity': '0', 'transition': 'all 0.4s ease-in-out', 'width': '100%', 'height': '100%', 'position': 'absolute',
           'overflow': 'hidden', 'top': '0', 'left': '0'}
  hover = {'opacity': 1}
  cssId = {'child': '.mask'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.rptObj.theme.success[0]})


class CssImgAInfo(CssStyle.CssCls):
  attrs = {'opacity': '0', 'transition': 'all 0.2s ease-in-out', 'display': 'inline-block', 'text-decoration': 'none',
           'padding': '7px 14px', 'position': 'relative', 'top': '70%', 'text-transform': 'uppercase', 'box-shadow': '0 0 1px #000'}
  hover = {'opacity': '1', 'transform': 'translateY(0px)', 'box-shadow': '0 0 5px #000', 'transition-delay': '0.2s'}
  cssId = {'child': 'a.info'}

  def customize(self, style, eventsStyles):
    style.update({'background-color': self.rptObj.theme.colors[0], 'color': self.rptObj.theme.colors[-1]})


class CssImg(CssStyle.CssCls):
  attrs = {'transition': 'all 0.2s linear', 'display': 'block', 'height': 'auto', 'margin': 'auto', 'max-height': '100%',
           'max-width': '100%', 'position': 'relative'}
  hover = {'transform': 'scale(1.1)'}
  cssId = {'child': 'img'}


class CssContent(CssStyle.CssCls):
  attrs = {'width': '100%', 'height': '70%', 'position': 'absolute', 'overflow': 'hidden', 'top': '20%', 'left': '0'}
  cssId = {'child': '.content'}


class CssView(CssStyle.CssCls):
  attrs = {'height': '70%', 'margin': '10px', 'float': 'left', 'overflow': 'hidden', 'position': 'relative',
           'text-align': 'center', 'cursor': 'default'}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.rptObj.theme.greys[5]})
    eventsStyles['hover'].update({'border': "1px solid %s" % self.rptObj.theme.success[1]})


class CssCarrouselLi(CssStyle.CssCls):
  attrs = {'list-style': 'none', 'display': 'none', 'padding': '0', 'margin': '0'}
  cssId = {'child': 'li'}


class CssCarrouselLabel(CssStyle.CssCls):
  attrs = {'background': 'black', 'padding': '10px', 'border-radius': '50%', 'display': 'inline-block', 'text-align': 'center'}
  cssId = {'child': 'label'}
  childrenTag = 'label'


class CssCarrouselH2(CssStyle.CssCls):
  attrs = {'position': 'absolute', 'top': '10px', 'padding': '10px'}
  cssId = {'child': 'h2'}

