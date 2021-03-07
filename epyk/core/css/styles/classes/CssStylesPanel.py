"""
CSS Style module for the Panels components
"""

from epyk.core.css.styles.classes import CssStyle

"""
.meow:after {
  content: " ";
	border-top: 11px solid #222;
	border-left: 8px solid transparent;
	border-right: 8px solid transparent;
  position: relative;
  top: 111px;
  right: -140px;
}
"""


class CssPanelArrowDown(CssStyle.Style):
  _after = {"content": '" "', "border-left": "50px solid transparent",
         "border-right": "50px solid transparent", "position": "relative",
         "width": 0, "margin": "auto", "display": "block", "bottom": "2px"}

  def customize(self):
    self.after.css({"border-top": "15px solid %s" % self.page.theme.success[1]})

"""
.meow {
  height: 100px;
  width: 300px;
  margin: 30px;
  background: #222222;
}

.meow:after {
  content: " ";
	border-bottom: 20px solid #222;
	border-left: 20px solid transparent;
	border-right: 20px solid transparent;
  position: relative;
  top: -38px; --111px;
  right: -130px;
}
"""


class CssPanelArrowUp(CssStyle.Style):
  _after = {"content": '" "', "border-left": "50px solid transparent",
         "border-right": "50px solid transparent", "position": "relative",
         "width": 0, "display": "block", "bottom": '45px'}

  def customize(self):
    self.after.css({"border-bottom": "15px solid %s" % self.page.theme.success[1]})
