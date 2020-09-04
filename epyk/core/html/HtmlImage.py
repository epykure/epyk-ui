#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core.html import Html
from epyk.core.html import HtmlContainer
from epyk.core.html import Defaults
from epyk.core.html.options import OptButton
from epyk.core.html.options import OptImg

from epyk.core.css.styles import GrpClsImage

# The list of Javascript classes
from epyk.core.js.html import JsHtml
from epyk.core.js.html import JsHtmlTinySlider
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsTinySlider

from epyk.core import data


class Image(Html.Html):
  name = 'Picture'

  def __init__(self, report, image, path, align, htmlCode, width, height, profile, options):
    if path is None:
      if Defaults.SERVER_PATH is not None and not image.startswith("http"):
        path = Defaults.SERVER_PATH
      else:
        path = os.path.split(image)[0]
        image = os.path.split(image)[-1]
    super(Image, self).__init__(report, {'path': path, 'image': image}, htmlCode=htmlCode, profile=profile,
                                css_attrs={"width": width, "height": height})
    self._jsStyles = options
    if align is not None:
      # https://www.w3schools.com/howto/howto_css_image_center.asp
      if align == "center":
        self.css({"margin-left": "auto", "margin-right": "auto", "display": "block"})
      elif align == "right":
        self.css({"margin-left": "auto", "margin-right": "0", "display": "block"})

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlImg
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlImg(self, report=self._report)
    return self._dom

  def goto(self, url, jsFncs=None, profile=False, name="_blank", source_event=None):
    """
    Description:
    -----------
    Click event which redirect to another page.

    Attributes:
    ----------
    :param jsFncs: List. The Javascript Events triggered before the redirection
    :param profile: Boolean. Optional
    :param source_event: String. Optional. The event source.
    """
    jsFncs = jsFncs or []
    self.style.css.cursor = 'pointer'
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    jsFncs.append(self.js.location.open_new_tab(url, name))
    return self.click(jsFncs, profile, source_event)

  @property
  def _js__builder__(self):
    return '''
      if (typeof image !== 'undefined'){
        if(typeof data.path === 'undefined'){data.path = '%s'};
        htmlObj.src = data.path + "/" + data.image}
      else { htmlObj.src = data }
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}
      ''' % Defaults.SERVER_PATH

  def __str__(self):
    self.attr["src"] = "%(path)s/%(image)s" % self.val
    return '<img %s />%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class AnimatedImage(Html.Html):
  name = 'Animated Picture'

  def __init__(self, report, image, text, title, url, path, width, height, options, profile):
    if path is None:
      if Defaults.SERVER_PATH is not None and not image.startswith("http"):
        path = Defaults.SERVER_PATH
      else:
        path = os.path.split(image)[0]
        image = os.path.split(image)[-1]
    super(AnimatedImage, self).__init__(report, {'path': path, 'image': image, 'text': text, "title": title, 'url': url},
                                        css_attrs={"width": width, "height": height, 'overflow': 'hidden', 'display': 'block'}, profile=profile)
    self.img = report.ui.img(image, path=path, width=(width[0]-5, width[1]), height=("auto", ''))
    self.img.options.managed = False
    self.title = report.ui.tags.h2(title).css({"display": 'block'})
    self.text = report.ui.tags.p(text).css({"display": 'block'})
    self.a = report.ui.tags.a("Enter", url).css({"width": "100px"})
    self.a.style.add_classes.image.info_link()
    self.div = report.ui.div([self.title, self.text, self.a], width=(width[0]-2, width[1])).css({"padding": "5px"})
    self.div.style.add_classes.image.mask()
    self.div.options.managed = False

  def __str__(self):
    return '''<div %(cssAttr)s>%(div)s%(img)s</div>
      ''' % {"cssAttr": self.get_attrs(pyClassNames=self.style.get_classes()), 'img': self.img.html(), 'div': self.div.html()}


class ImgCarrousel(Html.Html):
  name = 'Carrousel'

  def __init__(self, report, images, path, selected, width, height, options, profile):
    self.items, self.__click_items = [], []
    super(ImgCarrousel, self).__init__(report, "", css_attrs={"width": width, "height": height}, profile=profile)
    self.attr['data-current_picture'] = 0
    for i, rec in enumerate(images):
      if not hasattr(rec, 'options'):
        if not isinstance(rec, dict):
          rec = {"image": rec, 'title': "picture %s" % (i+1)}
        if not 'path' in rec:
          rec['path'] = path
        if rec.get('selected') is not None:
          selected = i
        img = report.ui.img(rec["image"], path=rec["path"], width=width, height=(height[0] - 60 if height[0] is not None else None, height[1]))
        div = report.ui.layouts.div([report.ui.tags.h3(rec['title']), img], htmlCode="%s_img_%s" % (self.htmlCode, i)).css(
          {"display": 'none', "text-align": "center"})
      else:
        div = report.ui.layouts.div(rec, htmlCode="%s_img_%s" % (self.htmlCode, i)).css({"display": 'none', "text-align": "center"})
      div.set_attrs(name="name", value="%s_img" % self.htmlCode)
      div.options.managed = False
      self.items.append(div)
    self.__point_display = options.get('points', True)
    self.__inifity = options.get('inifity', False)
    self.container = self._report.ui.layouts.div().css({"display": 'block', "width": "100%", "text-align": "center"})
    self.container.options.managed = False
    if 'arrows' in options:
      self.next = self._report.ui.icon(options.get("arrows-right", "fas fa-chevron-right")).css({"position": 'absolute',
                 "font-size": '35px', "padding": '8px', "right": '10px', 'top': '50%'})
      self.next.options.managed = False

      self.previous = self._report.ui.icon(options.get("arrows-left", "fas fa-chevron-left")).css({"position": 'absolute',
                 "font-size": '35px', "padding": '8px', "left": '10px', 'top': '50%'})
      self.previous.options.managed = False

      if options.get("keyboard", False):
        self._report.body.keyup.left([self.previous.dom.events.trigger("click")])
        self._report.body.keyup.right([self.next.dom.events.trigger("click")])
    else:
      self.next, self.previous = "", ""
    if not options.get('arrows', True):
      self.next.style.css.display = "none"
      self.previous.style.css.display = "none"
    self.items[selected].css({"display": 'block'})
    self.css({'padding-top': '20px', 'padding': "2px", 'margin': 0, 'position': 'relative'})

  def __getitem__(self, i):
    return self.items[i]

  def click(self, jsFncs, profile=False, source_event=None):
    """
    Description:
    ------------
    Add click event on this component

    Attributes:
    ----------
    :param jsFncs: String or List. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. optional. The reference of the component
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__click_items.extend(jsFncs)
    return self

  @property
  def _js__builder__(self):
    return '''
      data.forEach(function(rec, i){
        var li = document.createElement('li');
        if (i == 0) {li.style.display = 'block'} else{li.style.display = 'none'};
        var img = document.createElement('img'); img.src = rec.path +'/'+ rec.image; li.appendChild(img);
        var title = document.createElement('h3'); title.innerHTML = rec.title; li.appendChild(title); 
        htmlObj.appendChild(li);
        var label = document.createElement('label'); label.style.backgroundColor = '%(color)s'; 
        label.style.borderRadius = '20px'; label.for = i; label.innerHTML = '&nbsp;'; 
        document.getElementById(htmlObj.id +'_bullets').appendChild(label)
      })''' % {'color': self._report.theme.colors[9]}

  def __str__(self):
    self.container._vals = self.items
    self.attr['data-last_picture'] = len(self.items)-1
    points = self._report.ui.navigation.points(len(self.items), htmlCode="%s_points" % self.htmlCode)
    points.options.managed = False
    points.style.css.cursor = "pointer"
    if not self.__point_display:
      points.style.css.display = 'none'
    points.click([
      self._report.js.getElementsByName("%s_img" % self.htmlCode).css({"display": 'none'}),
      self._report.js.getElementById("%s_img_' + data.position +'" % self.htmlCode).css({"display": 'block'})
    ] + self.__click_items)

    if hasattr(self.next, 'html'):
      self.next.click([
        data.primitives.float(self.dom.attr("data-current_picture").toString().parseFloat().add(1), 'picture_index'),
        self.js.if_(self._report.js.object('picture_index') <= self.dom.attr('data-last_picture'), [
          self.dom.attr("data-current_picture", self._report.js.object('picture_index')),
          "(function(){var clickEvent = new Event('click'); %s.dispatchEvent(clickEvent)})()" %
          self._report.js.getElementsByName("%s_points" % self.htmlCode)[
            self.dom.getAttribute('data-current_picture').toString().parseFloat()]]).else_([
              self.dom.attr("data-current_picture", -1),
              self.next.dom.events.trigger("click")
        ] if self.__inifity else None)
      ])
    if hasattr(self.previous, 'html'):
      self.previous.click([
        data.primitives.float(self.dom.attr("data-current_picture").toString().parseFloat().add(-1), 'picture_index'),
        self.js.if_(self._report.js.object('picture_index') >= 0, [
          self.dom.attr("data-current_picture", self._report.js.object('picture_index')),
          "(function(){var clickEvent = new Event('click'); %s.dispatchEvent(clickEvent) })()" %
          self._report.js.getElementsByName("%s_points" % self.htmlCode)[
            self.dom.getAttribute('data-current_picture').toString().parseFloat()]]).else_([
              self.dom.attr("data-current_picture", len(self.items)),
              self.previous.dom.events.trigger("click")
        ] if self.__inifity else None)
      ])
    return '''<div %(strAttr)s>%(img_cont)s%(points)s%(next)s%(previous)s</div>
      ''' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'img_cont': self.container.html(),
             "points": points.html(), 'next': self.next.html() if hasattr(self.next, 'html') else '', 'previous': self.previous.html() if hasattr(self.previous, 'html') else ''}


class Icon(Html.Html):
  name = 'Icon'

  def __init__(self, report, value, width, height, color, tooltip, options, profile):
    self.requirements = (options['icon_family'], )
    super(Icon, self).__init__(report, "", css_attrs={"color": color, "width": width, "height": height}, profile=profile)
    if options['icon_family'] == 'office-ui-fabric-core':
      self.attr['class'].add("ms-Icon")
      if not value.startswith("ms-Icon--"):
        value = "ms-Icon--%s" % value
    elif options['icon_family'] == 'material-design-icons':
      self.attr['class'].add("material-icons")
      self._vals = value
      value = ""
    if value is not None:
      self.attr['class'].add(value)
    self.attr['aria-hidden'] = 'true'
    if tooltip is not None:
      self.set_attrs(name="title", value=tooltip)

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlIcon
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlIcon(self, report=self._report)
    return self._dom

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component

    :rtype: GrpClsImage.ClassIcon
    """
    if self._styleObj is None:
      self._styleObj = GrpClsImage.ClassIcon(self)
    return self._styleObj

  def spin(self):
    """
    Description:
    ------------

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons
    """
    if 'font-awesome' in self.requirements:
      self.attr['class'].add("fa-spin")
    return self

  def pulse(self):
    """
    Description:
    ------------

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons
    """
    if 'font-awesome' in self.requirements:
      self.attr['class'].add("fa-pulse")
    return self

  def border(self):
    """
    Description:
    ------------

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons
    """
    if 'font-awesome' in self.requirements:
      self.attr['class'].add("fa-border")
    return self

  def size(self, value):
    """
    Description:
    ------------
    Icons inherit the font-size of their parent container which allow them to match any text you might use with them.
    With the following classes, we can increase or decrease the size of icons relative to that inherited font-size.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/sizing-icons

    Attributes:
    ----------
    :param value:
    """
    if 'font-awesome' in self.requirements:
      if isinstance(value, int):
        self.attr['class'].add("fa-%sx" % value)
      else:
        self.attr['class'].add("fa-%s" % value)
    return self

  def fixed_width(self):
    """
    Description:
    ------------

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/fixed-width-icons
    """
    if 'font-awesome' in self.requirements:
      self.attr['class'].add("fa-fw")
    return self

  def rotate(self, value):
    """
    Description:
    ------------
    To arbitrarily rotate and flip icons, use the fa-rotate-* and fa-flip-* classes when you reference an icon.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/rotating-icons

    Attributes:
    ----------
    :param value: Integer. The rotation angle
    """
    if 'font-awesome' in self.requirements:
      self.attr['class'].add("fa-rotate-%s" % value)
    return self

  def flip(self, direction='h'):
    """
    Description:
    ------------
    To arbitrarily rotate and flip icons, use the fa-rotate-* and fa-flip-* classes when you reference an icon.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/rotating-icons

    Attributes:
    ----------
    :param direction:
    """
    if 'font-awesome' in self.requirements:
      if direction.lower() == 'h':
        self.attr['class'].add("fa-flip-horizontal")
      elif direction.lower() == 'v':
        self.attr['class'].add("fa-flip-vertical")
      else:
        self.attr['class'].add("fa-flip-both")
    return self

  def pull(self, position='left'):
    """
    Description:
    ------------
    Use fa-border and fa-pull-right or fa-pull-left for easy pull quotes or article icons.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons

    Attributes:
    ----------
    :param position:
    """
    if 'font-awesome' in self.requirements:
        self.attr['class'].add("fa-pull-%s" % position)
    return self

  def set_icon(self, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    """
    self.attr['class'].add(value)
    return self

  def hover_colors(self, color_hover, color_out=None):
    """
    Description:
    ------------
    Change the color of the button background when the mouse is hover

    Usage::

      rptObj.ui.icons.capture().icon.hover_colors("red", "yellow")

    Attributes:
    ----------
    :param color_hover: String. The color of the icon when mouse hover
    :param color_out: Optional, String. The color of the icon when mouse out
    """
    if color_out is None:
      color_out = self._report.theme.success[1]
    else:
      self.css({"color": color_out})
    self.set_attrs(name="onmouseover", value="this.style.color='%s'" % color_hover)
    self.set_attrs(name="onmouseout", value="this.style.color='%s'" % color_out)
    return self

  def click(self, jsFncs, profile=False, source_event=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    :param source_event:
    """
    self.style.css.cursor = "pointer"
    return super(Icon, self).click(jsFncs, profile, source_event)

  @property
  def _js__builder__(self):
    return '''htmlObj.classList = []; data.split(' ').forEach(function(cls){htmlObj.classList.add(cls)});
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<i %s>%s</i>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val)


class Emoji(Html.Html):
  name = 'Emoji'

  def __init__(self, report, symbole, top, options, profile):
    super(Emoji, self).__init__(report, symbole, options=options, profile=profile)
    self.style.css.margin_top = '%s%s' % (top[0], top[1])

  @property
  def _js__builder__(self):
    return '''
      htmlObj.innerHTML = data; 
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, report=self._report)
    return self._dom

  def __str__(self):
    return '<p %s>%s</p>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val)


class Badge(Html.Html):
  name = 'Badge'
  requirements = ('font-awesome', 'bootstrap')

  def __init__(self, report, text, width, height, label, icon, background_color, color, url, tooltip, options, profile):
    super(Badge, self).__init__(report, None, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_label(label, css={"vertical-align": "middle", "width": 'none', "height": 'none'})
    self.__options = OptButton.OptionsBadge(self, options)
    if self.options.badge_position == 'left':
      self.add_icon(icon, css={"float": 'None', 'margin-left': "5px"}, position="after", family=options.get("icon_family"))
    else:
      self.add_icon(icon, css={"float": 'left', 'margin-left': "5px"}, family=options.get("icon_family"))
    if hasattr(self.icon, 'css') and width[0] is not None:
      self.icon.css({"font-size": "%s%s" % (width[0], width[1])})
    self.link = None
    if url is not None:
      self.link = self._report.ui.links.external(text, url).css({"color": "inherit", 'display': 'inline-block',
          "padding": "2px", "width": "auto"})
      self.link.options.managed = False
    else:
      self.link = self._report.ui.text(text).css({'display': 'inline-block',
          "padding": "2px", "width": "auto"})
    self.link.css(self.options.badge_css)
    self.link.css({"color": color, "border-radius": "20px", 'margin-left': '2px', 'position': 'relative', 'right': '12px',
                   'background': background_color, 'top': "-5px"})
    self.link.options.managed = False
    self.attr['class'].add("badge") # From bootstrap
    if tooltip is not None:
      self.tooltip(tooltip)

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the options specific to the HTML component

    :rtype: OptButton.OptionsBadge
    """
    return self.__options

  def click(self, jsFncs, profile=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    :param source_event:
    """
    self.icon.style.add_classes.icon.standard()
    return super(Badge, self).click(jsFncs, profile, source_event)

  def __str__(self):
    return '<span %s>%s</span>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.link)


class Figure(HtmlContainer.Div):
  name = 'Figure container'

  def __str__(self):
    rows = []
    for htmlObj in self.val:
      if hasattr(htmlObj, 'html'):
        if self._sort_propagate:
          htmlObj.sortable(self._sort_options)
        rows.append(htmlObj.html())
      else:
        rows.append(str(htmlObj))

    return "<figure %s>%s</figure>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(rows), self.helper)


class SlideShow(Html.Html):
  name = 'Slide Show'
  requirements = ('tiny-slider', )

  def __init__(self, report, images, width, height, options, profile):
    super(SlideShow, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptImg.OptionsTinySlider(self, options)
    for i in images:
      self.add(i)

  @property
  def jsonId(self):
    """
    Description:
    ------------
    Return the Javascript variable of the json object
    """
    return "%s_obj" % self.htmlCode

  @property
  def js(self):
    """
    Description:
    -----------
    The tiny slider javascript events

    Return the Javascript internal object

    :return: A Javascript object

    :rtype: JsTinySlider.TinySlider
    """
    if self._js is None:
      self._js = JsTinySlider.TinySlider(self._report, varName=self.jsonId, setVar=False, parent=self)
    return self._js

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlTinySlider.JsHtmlTinySlider
    """
    if self._dom is None:
      self._dom = JsHtmlTinySlider.JsHtmlTinySlider(self, report=self._report)
    return self._dom

  def _events(self, event, jsFncs, source_event, profile=False, add=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param event: String. The event type
    :param jsFncs: List or String. The JavaScript fragments
    :param source_event: String
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param add:
    """
    if add:
      self.onReady(["%s.on('%s', function (info, eventName) {%s})" % (source_event, event, JsUtils.jsConvertFncs(jsFncs, toStr=True))])
    else:
      self.onReady(["%s.off('%s', function (info, eventName) {%s})" % (source_event, event, JsUtils.jsConvertFncs(jsFncs, toStr=True))])
    return self

  def addIndexChanged(self, jsFncs, profile=False, source_event=None):
    return self._events("indexChanged", jsFncs, source_event or "%s.events" % self.jsonId, profile)

  def remIndexChanged(self, jsFncs, profile=False, source_event=None):
    return self._events("indexChanged", jsFncs, source_event or "%s.events" % self.jsonId, profile, add=False)

  def addTransitionStart(self, jsFncs, profile=False, source_event=None):
    return self._events("transitionStart", jsFncs, source_event or "%s.events" %self.jsonId, profile)

  def remTransitionStart(self, jsFncs, profile=False, source_event=None):
    return self._events("transitionStart", jsFncs, source_event or "%s.events" %self.jsonId, profile, add=False)

  def addTransitionEnd(self, jsFncs, profile=False, source_event=None):
    return self._events("transitionEnd", jsFncs, source_event or "%s.events" % self.jsonId, profile)

  def remTransitionEnd(self, jsFncs, profile=False, source_event=None):
    return self._events("transitionEnd", jsFncs, source_event or "%s.events" % self.jsonId, profile, add=False)

  def addNewBreakpointStart(self, jsFncs, profile=False, source_event=None):
    return self._events("newBreakpointStart", jsFncs, source_event or self.jsonId, profile)

  def remNewBreakpointStart(self, jsFncs, profile=False, source_event=None):
    return self._events("newBreakpointStart", jsFncs, source_event or self.jsonId, profile, add=False)

  def addNewBreakpointEnd(self, jsFncs, profile=False, source_event=None):
    return self._events("newBreakpointEnd", jsFncs, source_event or self.jsonId, profile)

  def remNewBreakpointEnd(self, jsFncs, profile=False, source_event=None):
    return self._events("newBreakpointEnd", jsFncs, source_event or self.jsonId, profile, add=False)

  def addTouchStart(self, jsFncs, profile=False, source_event=None):
    return self._events("touchStart", jsFncs, source_event or self.jsonId, profile)

  def remTouchStart(self, jsFncs, profile=False, source_event=None):
    return self._events("touchStart", jsFncs, source_event or self.jsonId, profile, add=False)

  def addTouchMove(self, jsFncs, profile=False, source_event=None):
    return self._events("touchMove", jsFncs, source_event or self.jsonId, profile)

  def remTouchMove(self, jsFncs, profile=False, source_event=None):
    return self._events("touchMove", jsFncs, source_event or self.jsonId, profile, add=False)

  def addTouchEnd(self, jsFncs, profile=False, source_event=None):
    return self._events("touchEnd", jsFncs, source_event or self.jsonId, profile)

  def remTouchEnd(self, jsFncs, profile=False, source_event=None):
    return self._events("touchEnd", jsFncs, source_event or self.jsonId, profile, add=False)

  def addDragStart(self, jsFncs, profile=False, source_event=None):
    return self._events("dragStart", jsFncs, source_event or self.jsonId, profile)

  def remDragStart(self, jsFncs, profile=False, source_event=None):
    return self._events("dragStart", jsFncs, source_event or self.jsonId, profile, add=False)

  def addDragMove(self, jsFncs, profile=False, source_event=None):
    return self._events("dragMove", jsFncs, source_event or self.jsonId, profile)

  def remDragMove(self, jsFncs, profile=False, source_event=None):
    return self._events("dragMove", jsFncs, source_event or self.jsonId, profile, add=False)

  def addDragEnd(self, jsFncs, profile=False, source_event=None):
    return self._events("dragEnd", jsFncs, source_event or self.jsonId, profile)

  def remDragEnd(self, jsFncs, profile=False, source_event=None):
    return self._events("dragEnd", jsFncs, source_event or self.jsonId, profile, add=False)

  def refresh(self):
    """
    Description:
    -----------
    Component refresh function. Javascript function which can be called in any Javascript event
    """
    return self.build([], self._jsStyles)

  @property
  def options(self):
    """
    Description:
    ------------
    The tiny slider options

    https://github.com/ganlanyuan/tiny-slider

    :rtype: OptImg.OptionsTinySlider
    """
    return self.__options

  def add(self, component):
    """
    Description:
    ------------
    Add a component to the slider container

    Attributes:
    ----------
    :param component: HTML Component. A component to be added to the slider container
    """
    if not hasattr(component, 'options'):
      component = self._report.ui.div(component)
    component.options.managed = False
    self.val.append(component)
    self.components[component.htmlCode] = component
    return self

  @property
  def _js__builder__(self):
    return "window[ htmlObj.id + '_obj'] = tns(options)"

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    rows = [htmlObj.html() for htmlObj in self.val]
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(rows))
