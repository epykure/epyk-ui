"""
HTML Definition for extra layouts and feedbacks components
"""

import json

from epyk.core.html import Html


class Hr(Html.Html):
  name, category, callFnc = 'Line delimiter', 'Layouts', 'hr'
  __pyStyle = ['CssHr']

  def __init__(self, report, color, count, size, background_color, height, align, profile):
    super(Hr, self).__init__(report, count, height=height[0], heightUnit=height[1], profile=profile)
    if color is not None:
      self.css('color', color)
    if align == "center":
      self.css('margin', "auto")
    self.size, self.background_color = size, background_color if background_color is not None else self._report.getColor('greys', 2)

  def __str__(self):
    hr = '<hr style="height:%spx;background-color:%s">' % ("%s%s" % (self.size[0], self.size[1]), self.background_color) if self.size is not None else '<hr style="background-color:%s" />' % self.backgroundColor
    return '<div %s>%s</div>' % (self.strAttr(pyClassNames=self.pyStyle), "".join(self.vals * [hr]))

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val): return True if val.strip() == '***' else None

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report=None):
    if report is not None:
      getattr(report, cls.callFnc)()
    return ["report.%s()" % cls.callFnc]

  @classmethod
  def jsMarkDown(self, vals): return "***"

  def to_word(self, document):
    document.add_paragraph("_________________________________")


class Newline(Html.Html):
  name, category, callFnc = 'New line', 'Layouts', 'new_line'

  def html(self):
    return "".join(['<br />'] * self.vals)

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val): return True if val.strip() == '' else None

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report=None):
    if report is not None:
      getattr(report.ui.layouts, cls.callFnc)()
    return ["report.ui.%s.%s()" % (cls.category.lower(), cls.callFnc)]

  @classmethod
  def jsMarkDown(self, vals): return ""

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    document.add_page_break()


class Stars(Html.Html):
  name, category, callFnc = 'Stars', 'Rich', 'stars'
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']

  def __init__(self, report, val, label, color, align, best, htmlCode, helper, profile):
    super(Stars, self).__init__(report, val, htmlCode=htmlCode, profile=profile)
    # Add the HTML components
    self.add_label(label, {"margin-left": "5px", "text-align": "left",  "display": "inline-block", 'float': 'None'}, position="after")
    self.add_helper(helper)
    self.best = best
    self.css({'text-align': align})
    self._jsStyles = {'color':  self.getColor("success", 1) if color is None else color}

  @property
  def id_container(self):
    return self.htmlId

  @property
  def val(self):
    return "%s.parent().data('level')" % self.jqId

  @property
  def jqId(self): return "$('#%s span')" % self.htmlId

  @property
  def jsQueryData(self):
    if self.htmlCode is not None:
      return "{%s: $(this).data('level'), event_val: $(this).data('level'), event_code: '%s'}" % (self.htmlCode, self.htmlId)

    return "{event_val: $(this).data('level'), event_code: '%s'}" % self.htmlId

  def click(self, js_fncs):
    """
    Add the event click and double click to the starts item

    Example
    stars = rptObj.ui.rich.stars(3, label="test Again")
    stars.click(rptObj.js.console.log("test").toStr())

    :param js_fncs: An array of Js functions or string. Or a string with the Js

    :return:
    """
    self.css({"cursor": "pointer"})
    if not isinstance(js_fncs, list):
      js_fncs = [js_fncs]
    array = list(js_fncs)
    js_fncs.append("%s(%s, data.event_val, %s)" % (self.__class__.__name__, self.jqId, json.dumps(self._jsStyles)))
    # Add the double click to remove all the stars
    array.append("%s(%s, 0, %s)" % (self.__class__.__name__, self.jqId, json.dumps(self._jsStyles)))
    self.dblclick(array)
    return super(Stars, self).click(js_fncs)

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      htmlObj.parent().data('level', data);
      htmlObj.each(function(i){
        if (i < data){$(this).css('color', jsStyles.color)}
        else {$(this).css('color', '')}})''', 'Javascript Object builder')

  def __str__(self):
    stars = ["<div %s>" % self.strAttr(pyClassNames=self.pyStyle)]
    for i in range(self.best):
      stars.append('<span data-level="%s" class="fa fa-star"></span>' % (i+1))
    stars.append("%s</div>" % self.helper)
    return "".join(stars)


class Help(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome', 'jqueryui']
  name, category, callFnc = 'Info', 'Texts', 'help'

  def __init__(self, report, val, width, profile):
    super(Help, self).__init__(report, val, width=width[0], widthUnit=width[1], profile=profile)
    self.css({"cursor": "pointer", "float": "right"})
    self.attr['class'].add("fas fa-question-circle")

  def onDocumentReady(self):
    self._report.jsOnLoadFnc.add('%(jqId)s.attr("title", %(jsVal)s); %(jqId)s.tooltip()' % {"jqId": self.jqId, "jsVal": self.jsVal})

  def onDocumentLoadFnc(self): return True

  def __str__(self):
    return '<i %s></i>' % self.strAttr()

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document): pass

  def to_pdf(self, document): pass

  def to_xls(self, workbook, worksheet, cursor): pass


class Loading(Html.Html):
  name, category = 'Loading', 'Others'
  __pyStyle = ['CssDivLoading']
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  inReport = False

  def __str__(self):
    self.loadStyle()
    if self.vals is None:
      return '<div %s><i style="margin:auto;font-size:20px" class="fas fa-spinner fa-spin"></i><br />Loading...</div>' % (self.strAttr(withId=False, pyClassNames=self.pyStyle))

    return '<div %s><i style="margin:auto;font-size:20px" class="fas fa-spinner fa-spin"></i><br />%s...</div>' % (self.strAttr(withId=False, pyClassNames=self.pyStyle), self.vals)
