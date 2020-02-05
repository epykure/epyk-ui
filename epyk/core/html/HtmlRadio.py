"""
Module for the HTML radio components
"""

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.categories import CssGrpClsList

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml


class Radio(Html.Html):
  name, category, callFnc = 'Radio Buttons', 'Buttons', 'radio'

  def __init__(self, report, vals, htmlCode, label, width, height, radioVisible, event,
               withRemoveButton, align, filters, tooltip, radioType, helper, profile):
    items = []
    for v in vals:
      r = report.ui.inputs.radio(v.get('checked', False), v['value'])
      r.inReport = False
      items.append(r)
    super(Radio, self).__init__(report, items, htmlCode=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                heightUnit=height[1], globalFilter=filters, profile=profile)
    for v in self.val:
      v.set_attrs(name="name", value="radio_%s" % self.htmlId)

  def __getitem__(self, i):
    return self._vals[i]

  def __add__(self, val):
    r = self._report.ui.inputs.radio(False, val, group_name="radio_%s" % self.htmlId)
    r.inReport = False
    self._vals.append(r)
    return self

  def set_disable(self, text):
    """

    :param text:
    :return:
    """
    for v in self.val:
      if v.val["text"] == text:
        self._report._props.setdefault('js', {}).setdefault("builders", []).append(v.dom.attr("disabled", 'true').r)
    return self

  def set_checked(self, text):
    """

    :param text:
    :return:
    """
    for v in self.val:
      if v.val["text"] == text:
        v.val["value"] = True
    return self

  def __str__(self):
    row = self._report.ui.layouts.div(self.val)
    row.css({"width": 'none'})
    row.inReport = False
    return "<div %s>%s</div>%s" % (self.get_attrs(pyClassNames=self.defined), row.html(), self.helper)


class Switch(Html.Html):
  __reqCss, __reqJs = ['bootstrap'], ['bootstrap', 'jquery']
  name, category, callFnc = 'Switch Buttons', 'Buttons', 'switch'
  _grpCls = CssGrpClsList.CssClassSwitch

  def __init__(self, report, records, label, color, size, width, height, htmlCode, profile):
    self.width, self.jsChange, self.size = width[0], '', size
    super(Switch, self).__init__(report, records, htmlCode=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                 heightUnit=height[1], profile=profile)
    self.add_label(label) # add for
    self._clicks = {'on': [], 'off': []}
    self.color = 'inherit' if color is None else color
    self.css({"display": 'inline-block'})
    self.switch = self.dom.querySelector("label")

  @property
  def _js__builder__(self):
    return '''
      if (data.off == data.checked){htmlObj.querySelector("input").checked = false; htmlObj.querySelector("p").innerHTML = data.off}
      else {htmlObj.querySelector("input").checked = true; htmlObj.querySelector("p").innerHTML = data.on}'''

  def click(self, onFncs=None, offFncs=None):
    if onFncs is not None:
      self._clicks['on'].extend(onFncs)
    if offFncs is not None:
      self._clicks['off'].extend(offFncs)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(
      self.switch.onclick('''
        if(this.parentNode.querySelector('input').checked){%s; this.parentNode.querySelector('p').innerHTML = %s;
            this.parentNode.querySelector('input').checked = false}
        else {%s; this.parentNode.querySelector('input').checked = true; this.parentNode.querySelector('p').innerHTML = %s}
        ''' % (";".join(self._clicks["on"]), JsUtils.jsConvertData(self.val['off'], None),
               ";".join(self._clicks["off"]), JsUtils.jsConvertData(self.val['on'], None))).toStr())
    return '''
      <div %s>
        <input type="checkbox"/>
        <label style="width:50px;display:inline-block" for="switch">&nbsp;</label>
        <p style="display:inline-block;margin-left:3px;font-weight:bold" title="%s">%s</p>
      </div>''' % (self.get_attrs(pyClassNames=self.defined), self.val.get('text', ''), self.val['off'])
