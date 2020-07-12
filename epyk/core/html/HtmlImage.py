#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core.html import Html
from epyk.core.html import Defaults
from epyk.core.html.options import OptButton

from epyk.core.css.styles import GrpClsImage

# The list of Javascript classes
from epyk.core.js.html import JsHtml


class Image(Html.Html):
  name = 'Picture'

  def __init__(self, report, image, path, align, htmlCode, width, height, profile, options):
    if path is None:
      path = Defaults.SERVER_PATH or os.path.split(image)[0]
    super(Image, self).__init__(report, {'path': path, 'image': image}, htmlCode=htmlCode, profile=profile,
                                css_attrs={"width": width, "height": height})
    self._jsStyles = options
    if align is not None:
      # https://www.w3schools.com/howto/howto_css_image_center.asp
      if align == "center":
        self.css({"margin-left": "auto", "margin-right": "auto", "display": "block"})
      elif align == "right":
        self.css({"margin-left": "auto", "margin-right": "0", "display": "block"})

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
      if(typeof data.path === 'undefined'){data.path = '%s'};
      htmlObj.src = data.path + "/" + data.image; 
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}
      ''' % Defaults.SERVER_PATH

  def __str__(self):
    self.attr["src"] = "%(path)s/%(image)s" % self.val
    return '<img %s />%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class AnimatedImage(Html.Html):
  name = 'Animated Picture'

  def __init__(self, report, image, text, title, url, path, width, height, profile):
    if path is None:
      path = Defaults.SERVER_PATH or os.path.split(image)[0]
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

  def __init__(self, report, images, path, selected, width, height, profile):
    if path is None:
      path = Defaults.SERVER_PATH or os.path.split(images[0])[0]
    self.items, self.__click_items = [], []
    super(ImgCarrousel, self).__init__(report, "", css_attrs={"width": width, "height": height}, profile=profile)
    for i, rec in enumerate(images):
      if not isinstance(rec, dict):
        rec = {"image": rec, 'title': "picture %s" % (i+1)}
      if not 'path' in rec:
        rec['path'] = path
      if rec.get('selected') is not None:
        selected = i
      img = report.ui.img(rec["image"], path=rec["path"], width=width, height=(height[0] - 60, height[1]))
      div = report.ui.layouts.div([report.ui.tags.h3(rec['title']), img], htmlCode="%s_img_%s" % (self.htmlCode, i)).css({"display": 'none', "text-align": "center"})
      div.set_attrs(name="name", value="%s_img" % self.htmlCode)
      div.options.managed = False
      self.items.append(div)
    self.items[selected].css({"display": 'block'})
    self.css({'padding-top': '20px', 'padding': "2px", 'margin': 0})

  def __getitem__(self, i):
    return self.items[i]

  def click(self, jsFncs, profile=False, source_event=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
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
    img_cont = self._report.ui.layouts.div(self.items).css({"display": 'block', "width": "100%", "text-align": "center"})
    img_cont.options.managed = False
    points = self._report.ui.navigation.points(len(self.items))
    points.options.managed = False
    points.click([
      self._report.js.getElementsByName("%s_img" % self.htmlCode).css({"display": 'none'}),
      self._report.js.getElementById("%s_img_' + data.position +'" % self.htmlCode).css({"display": 'block'})
    ] + self.__click_items)
    return '''<div %(strAttr)s>%(img_cont)s%(points)s</div>
      ''' % {'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()),
             'img_cont': img_cont.html(), "points": points.html()}


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

  def set_icon(self, value):
    """

    :param value:

    :return:
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

  def __init__(self, report, symbole, top, profile):
    super(Emoji, self).__init__(report, symbole, profile=profile)
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
