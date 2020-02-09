"""
Module for the HTML Selects components
"""

from epyk.core.html import Html
from epyk.core.html import Options

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsList

#
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsSelect


class Option(Html.Html):
  name, category, callFnc = 'Select Option', 'Lists', None
  builder_name = False

  def __init__(self, report, value, text, icon, selected):
    super(Option, self).__init__(report, text)
    self.set_attrs(name="value", value=value)
    if selected:
      self.set_attrs(name="selected", value=selected)
    if icon is not None:
      self.set_attrs(name="data-icon", value=icon)

  def __str__(self):
    return "<option %s>%s</option>" % (self.get_attrs(pyClassNames=self.defined), self.val)


class Optgroup(Html.Html):
  name, category, callFnc = 'Select Option', 'Lists', None
  builder_name = False

  def __init__(self, report, data, label):
    super(Optgroup, self).__init__(report, data)
    self.set_attrs(name="label", value=label)

  def __str__(self):
    val = "".join([v.html() for v in self.val])
    return "<optgroup %s>%s</optgroup>" % (self.get_attrs(pyClassNames=self.defined), val)


class Select(Html.Html):
  __reqCss, __reqJs = ['select'], ['select']
  name, category, callFnc = 'Select', 'Lists', 'select'
  # _grpCls = CssGrpClsList.CssClassListSelectMin

  def __init__(self, report, records, htmlCode, width, height, filter, profile, multiple, options):
    super(Select, self).__init__(report, records, htmlCode=htmlCode, width=width[0], widthUnit=width[1],
                                 height=height[0],  heightUnit=height[1], globalFilter=filter, profile=profile)
    self.selected = None
    self.style.addCls(self.defined.clsAltMap)
    self._jsStyles = options

  @property
  def dom(self):
    """
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object
    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsSelect.JSelect(self, report=self._report)
    return self._dom

  @property
  def _js__builder__(self):
    return '''%s.selectpicker(options).selectpicker('refresh')''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def change(self, jsFncs, profile=False):
    return self.on("change", jsFncs, profile)

  def __str__(self):
    options, opt_groups = [], {}
    for val in self.val:
      opt = Option(self._report, val['value'], val['name'], None, self.selected is not None and self.selected == val['value'])
      opt.inReport = False
      if 'group' in val:
        opt_groups.setdefault(val['group'], []).append(opt)
      else:
        options.append(opt.html())
    data = options
    for k in sorted(opt_groups):
      opt_rp = Optgroup(self._report, opt_groups[k], k)
      opt_rp.inReport = False
      data.append(opt_rp.html())
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<select %s>%s</select>" % (self.get_attrs(pyClassNames=self.defined), "".join(data))

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_xls(self, workbook, worksheet, cursor):
    if self.htmlId in self._report.http:
      cell_title = self._jsStyles["title"] if self._jsStyles.get("title") is not None else 'Input'
      cell_format = workbook.add_format({'bold': True})
      worksheet.write(cursor['row'], 0, cell_title, cell_format)
      cursor['row'] += 1
      worksheet.write(cursor['row'], 0, self._report.http[self.htmlId])
      cursor['row'] += 2

  def to_word(self, document):
    p = document.add_paragraph()
    p.add_run("Selected: ")
    selected = ""
    for rec in self.vals:
      if rec.get('selected', False):
        selected = rec['value']
    runner = p.add_run(selected)
    runner.bold = True
