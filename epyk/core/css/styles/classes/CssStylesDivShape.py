
from epyk.core.css import Colors
from epyk.core.css.styles.classes import CssStyle


class CssDivCircle(CssStyle.Style):
  _attrs = {
    "border-radius": '50%', 'padding': '3%'
  }

  def customize(self):
    rgb = Colors.getHexToRgb(self.page.theme.greys[-1])
    rgb_color = Colors.getHexToRgb(self.page.theme.colors[-1])
    self.css({
      'box-shadow': "0 0 %(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
        "r": rgb[0], "g": rgb[1], "b": rgb[2], 'opac': 0.5, 'size': 5}
    })
    self.hover.css({
      'box-shadow': "0 0 %(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
        "r": rgb_color[0], "g": rgb_color[1], "b": rgb_color[2], 'opac': 0.8, 'size': 5}
    })


class Parallelogram(CssStyle.Style):

  _attrs = {
    "transform": 'skew(10deg)', 'padding': '3%'
  }

  def customize(self):
    rgb = Colors.getHexToRgb(self.page.theme.greys[-1])
    rgb_color = Colors.getHexToRgb(self.page.theme.colors[-1])
    self.css({
      'box-shadow': "0 0 %(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
        "r": rgb[0], "g": rgb[1], "b": rgb[2], 'opac': 0.5, 'size': 5}
    })
    self.hover.css({
      'box-shadow': "0 0 %(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
        "r": rgb_color[0], "g": rgb_color[1], "b": rgb_color[2], 'opac': 0.8, 'size': 5}
    })


class CssDivPage(CssStyle.Style):
  _attrs = {
    "position": 'relative', 'padding': '3%',
  }
  _before = {'content': "''", 'position': 'absolute', 'top': "-4px",
             'right': "-4px", 'width': 0}

  def customize(self):
    rgb = Colors.getHexToRgb(self.page.theme.greys[-1])
    rgb_color = Colors.getHexToRgb(self.page.theme.colors[-1])
    self.css({
      'box-shadow': "0 0 %(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
        "r": rgb[0], "g": rgb[1], "b": rgb[2], 'opac': 0.5, 'size': 5}
    })
    self.hover.css({
      'box-shadow': "0 0 %(size)spx rgba(%(r)s, %(g)s, %(b)s, %(opac)s)" % {
        "r": rgb_color[0], "g": rgb_color[1], "b": rgb_color[2], 'opac': 0.8, 'size': 5}
    })
    self.before.css({
      'border-top': '20px solid %s' % self.page.theme.greys[0],
      'border-left': '20px solid %s' % self.page.theme.colors[2],

    })


class Octagon(CssStyle.Style):
  _attrs = {
    "position": 'relative', "padding": '25px 3%'
  }
  _before = {'content': "''", 'position': 'absolute', 'top': 0, "height": 0,
             'left': 0, 'width': "100%"}

  _after = {'content': "''", 'position': 'absolute', 'bottom': 0, "height": 0,
            'left': 0, 'width': "100%"}

  def customize(self):
    self.css({"background": self.page.theme.colors[0]})
    self.before.css({
      'border-bottom': '25px solid %s' % self.page.theme.colors[0],
      'border-right': '25px solid %s' % self.page.theme.greys[0],
      'border-left': '25px solid %s' % self.page.theme.greys[0],

    })
    self.after.css({
      'border-top': '25px solid %s' % self.page.theme.colors[0],
      'border-right': '25px solid %s' % self.page.theme.greys[0],
      'border-left': '25px solid %s' % self.page.theme.greys[0],

    })
