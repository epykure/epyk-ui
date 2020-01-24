"""
CSS Style module for the Panels components
"""


from epyk.core.css.styles import CssStyle


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


class CssPanelArrowDown(CssStyle.CssCls):
  after = {"content": '" "', "border-left": "15px solid transparent",
           "border-right": "15px solid transparent",
           "position": "relative",
           #"top": "25px",
           "width": "10px", "margin": "auto",
           "display": "block", "bottom": "2px"
           #"right": '15px'
           }

  def customize(self, style, eventsStyles):
    eventsStyles['after'].update({"border-top": "15px solid %s" % self.rptObj.theme.success[1]})

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


class CssPanelArrowUp(CssStyle.CssCls):
  after = {"content": '" "', "border-left": "15px solid transparent",
           "border-right": "15px solid transparent",
           "position": "relative",
           "width": "10px", "left": "37px",
           "display": "block", "bottom": '74px'
           }

  def customize(self, style, eventsStyles):
    eventsStyles['after'].update({"border-bottom": "15px solid %s" % self.rptObj.theme.success[1]})
