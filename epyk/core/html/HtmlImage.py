#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import io
import base64

from typing import Union, Optional, List
from epyk.core.py import primitives

from epyk.core.html import Html
from epyk.core.html import HtmlContainer
from epyk.core.html import Defaults
from epyk.core.html.options import OptButton
from epyk.core.html.options import OptImg

from epyk.core.css.styles import GrpClsImage
from epyk.core.css import Defaults as cssDefaults

# The list of Javascript classes
from epyk.core.js.html import JsHtml
from epyk.core.js.html import JsHtmlTinySlider
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsTinySlider

from epyk.core import data


class Image(Html.Html):
  name = 'Picture'

  def __init__(self, page, image, path, align, html_code, width, height, profile, options):
    if path is None and image is not None:
      if Defaults.SERVER_PATH is not None and not image.startswith("http"):
        path = Defaults.SERVER_PATH
      else:
        path = os.path.split(image)[0]
        image = os.path.split(image)[-1]
    super(Image, self).__init__(page, {'path': path, 'image': image}, html_code=html_code, profile=profile,
                                css_attrs={"width": width, "height": height})
    self._jsStyles = options
    if align is not None:
      """ https://www.w3schools.com/howto/howto_css_image_center.asp """
      if align == "center":
        self.css({"margin-left": "auto", "margin-right": "auto", "display": "block"})
      elif align == "right":
        self.css({"margin-left": "auto", "margin-right": "0", "display": "block"})

  @property
  def dom(self) -> JsHtml.JsHtmlImg:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlImg
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlImg(self, page=self.page)
    return self._dom

  def goto(self, url, js_funcs=None, profile=None, target="_blank", source_event=None):
    """
    Description:
    -----------
    Click event which redirect to another page.

    Attributes:
    ----------
    :param url: String. the url.
    :param js_funcs: List | String. Optional. The Javascript Events triggered before the redirection.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    :param target: String. Optional. The target attribute specifies where to open the linked document.
    :param source_event: String. Optional. The event source.
    """
    js_funcs = js_funcs or []
    self.style.css.cursor = 'pointer'
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.js.location.open_new_tab(url, target))
    return self.click(js_funcs, profile, source_event)

  def from_plot(self, plt):
    """
    Description:
    -----------
    Load a image from a plt object from matplotlib.

    Usage::

      x = np.arange(0, 15, 0.1)
      y = np.sin(x)
      plt.plot(x, y)

      img2 = page.ui.img(width=(50, "%"))
      img2.from_plot(plt)
      img2.style.css.display = "inline-block"

    Attributes:
    ----------
    :param plt: matplotlib.pyplot. The ploting features in matplotlib.

    :return: self to allow the chaining
    """
    str_io = io.BytesIO()
    plt.savefig(str_io, format='jpg')
    str_io.seek(0)
    plt.close(1)
    return self.from_base64(base64.b64encode(str_io.read()).decode("utf-8"))

  def from_base64(self, text: str):
    """
    Description:
    -----------
    Load a image from a base64 string.

    Usage::

      x = np.arange(0, 15, 0.1)
      y = np.sin(x)
      plt.plot(x, y)

      str_io = io.BytesIO()
      plt.savefig(str_io, format='jpg')
      str_io.seek(0)

      self.from_base64(base64.b64encode(str_io.read()).decode("utf-8"))

    Attributes:
    ----------
    :param str text: The encoded picture.

    :return: self to allow the chaining
    """
    self.val["path"] = "data:image"
    self.val["image"] = "png;base64,%s" % text
    return self

  _js__builder__ = '''
      if ((typeof data !== 'string') && (typeof data !== 'undefined')){
        if(typeof data.path === 'undefined'){data.path = '%s'}
        htmlObj.src = data.path + "/" + data.image}
      else {htmlObj.src = data}
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}    
      ''' % Defaults.SERVER_PATH

  def __str__(self):
    if self.val["image"] is not None:
      self.attr["src"] = "%(path)s/%(image)s" % self.val
    return '<img %s />%s' % (self.get_attrs(css_class_names=self.style.get_classes()), self.helper)


class AnimatedImage(Html.Html):
  name = 'Animated Picture'

  def __init__(self, page, image, text, title, html_code, url, path, width, height, options, profile):
    if path is None:
      if Defaults.SERVER_PATH is not None and not image.startswith("http"):
        path = Defaults.SERVER_PATH
      else:
        path = os.path.split(image)[0]
        image = os.path.split(image)[-1]
    super(AnimatedImage, self).__init__(page,
                                        {'path': path, 'image': image, 'text': text, "title": title, 'url': url},
                                        css_attrs={"width": width, "height": height, 'overflow': 'hidden',
                                                   'display': 'block'},
                                        options=options, profile=profile)
    self.img = page.ui.img(
      image, path=path, width="auto", html_code=html_code, height=(100, "%"), options=options)
    self.img.options.managed = False
    self.title = page.ui.tags.h2(title).css({"display": 'block'})
    self.text = page.ui.tags.p(text).css({"display": 'block'})
    self.a = page.ui.tags.a("Enter", url).css({"width": "100px", "background": "white"})
    self.a.style.add_classes.image.info_link()
    self.div = page.ui.div([self.title, self.text, self.a], width=(100, "%"))
    self.div.style.add_classes.image.mask()
    self.div.style.css.position = "absolute"
    self.div.style.css.padding = 10
    self.div.options.managed = False
    self.style.css.position = "relative"

  def from_plot(self, plt):
    """
    Description:
    -----------
    Load a image from a plt object from matplotlib.

    Usage::

      x = np.arange(0, 15, 0.1)
      y = np.sin(x)
      plt.plot(x, y)

      img2 = page.ui.img(width=(50, "%"))
      img2.from_plot(plt)
      img2.style.css.display = "inline-block"

    Attributes:
    ----------
    :param plt: matplotlib.pyplot. The ploting features in matplotlib.

    :return: self to allow the chaining.
    """
    str_io = io.BytesIO()
    plt.savefig(str_io, format='jpg')
    str_io.seek(0)
    plt.close(1)
    return self.from_base64(base64.b64encode(str_io.read()).decode("utf-8"))

  def from_base64(self, text: str):
    """
    Description:
    -----------
    Load a image from a base64 string.

    Usage::

      x = np.arange(0, 15, 0.1)
      y = np.sin(x)
      plt.plot(x, y)

      str_io = io.BytesIO()
      plt.savefig(str_io, format='jpg')
      str_io.seek(0)

      self.from_base64(base64.b64encode(str_io.read()).decode("utf-8"))

    Attributes:
    ----------
    :param str text: The encoded picture.

    :return: self to allow the chaining
    """
    self.img.val["path"] = "data:image"
    self.img.val["image"] = "png;base64,%s" % text
    return self

  def __str__(self):
    return '''<div %(cssAttr)s>%(div)s%(img)s</div>
      ''' % {"cssAttr": self.get_attrs(css_class_names=self.style.get_classes()), 'img': self.img.html(),
             'div': self.div.html()}


class ImgCarousel(Html.Html):
  name = 'Carousel'
  _option_cls = OptImg.OptionsImage

  def __init__(self, page, images, path, selected, width, height, options, profile):
    self.items, self.__click_items = [], []
    super(ImgCarousel, self).__init__(page, "", css_attrs={"width": width, "height": height}, profile=profile)
    self.attr['data-current_picture'] = 0
    for i, rec in enumerate(images):
      if not hasattr(rec, 'options'):
        if not isinstance(rec, dict):
          rec = {"image": rec, 'title': "picture %s" % (i+1)}
        if 'path' not in rec:
          rec['path'] = path
        if rec.get('selected') is not None:
          selected = i
        img = page.ui.img(rec["image"], path=rec["path"], width=width,
                          height=(height[0] - 60 if height[0] is not None else None, height[1]))
        img_title = page.ui.tags.h3(rec['title'])
        div = page.ui.layouts.div([img_title, img], html_code="%s_img_%s" % (self.htmlCode, i)).css(
          {"display": 'none', "text-align": "center"})
        div.title = img_title
        div.img = img
      else:
        div = page.ui.layouts.div(rec, html_code="%s_img_%s" % (self.htmlCode, i)).css(
          {"display": 'none', "text-align": "center"})
      div.set_attrs(name="name", value="%s_img" % self.htmlCode)
      div.options.managed = False
      self.items.append(div)
    self.__point_display = options.get('points', True)
    self.infinity = options.get('infinity', False)
    self.container = self.page.ui.layouts.div().css({"display": 'block', "width": "100%", "text-align": "center"})
    self.container.options.managed = False
    if 'arrows' in options:
      self.next = self.page.ui.icon(options.get("arrows-right", "fas fa-chevron-right")).css(
        {"position": 'absolute', "font-size": '35px', "padding": '8px', "right": '10px', 'top': '50%'})
      self.next.options.managed = False

      self.previous = self.page.ui.icon(options.get("arrows-left", "fas fa-chevron-left")).css(
        {"position": 'absolute', "font-size": '35px', "padding": '8px', "left": '10px', 'top': '50%'})
      self.previous.options.managed = False

      if options.get("keyboard", False):
        self.page.body.keyup.left([self.previous.dom.events.trigger("click")])
        self.page.body.keyup.right([self.next.dom.events.trigger("click")])
    else:
      self.next, self.previous = "", ""
    if not options.get('arrows', True):
      self.next.style.css.display = "none"
      self.previous.style.css.display = "none"

    if self.items:
      self.items[selected].css({"display": 'block'})
      self.set_nav_dots()
    self.css({'padding-top': '20px', 'padding': "2px", 'margin': 0, 'position': 'relative'})

  def __getitem__(self, i) -> Html.Html:
    return self.items[i]

  def add_plot(self, plot, title: str = "", width: Union[str, tuple] = "auto"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param plot: matplotlib.pyplot. The ploting features in matplotlib.
    :param title:
    :param width: Tuple | Value. Optional.

    :return: self to allow the chaining.
    """
    img = self.page.ui.img(width=width)
    img.from_plot(plot)
    title = self.page.ui.tags.h3(title)
    div = self.page.ui.layouts.div([title, img], html_code="%s_img_%s" % (self.htmlCode, len(self.items))).css(
      {"display": 'none', "text-align": "center"})
    div.title = title
    div.img = img
    div.set_attrs(name="name", value="%s_img" % self.htmlCode)
    div.options.managed = False
    self.items.append(div)
    return self

  def set_nav_dots(self, selected: int = 0):
    """
    Description:
    ------------

    :param int selected:

    :return: self to allow the chaining.
    """
    self.items[selected].css({"display": 'block'})
    self.points = self.page.ui.navigation.points(
      len(self.items), html_code="%s_points" % self.htmlCode, options={"managed": False})
    return self

  def from_base64_list(self, values, width: Union[str, tuple] = "auto"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param values:
    :param Union[str, tuple] width: Optional.

    :return: self to allow the chaining.
    """
    for val in values:
      img = self.page.ui.img(width=width)
      img.from_base64(val)
      div = self.page.ui.layouts.div([img], html_code="%s_img_%s" % (self.htmlCode, len(self.items))).css(
        {"display": 'none', "text-align": "center"})
      div.img = img
      div.set_attrs(name="name", value="%s_img" % self.htmlCode)
      div.options.managed = False
      self.items.append(div)
    return self

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    ------------
    Add click event on this component.

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] source_event: optional. The reference of the component.
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.__click_items.extend(js_funcs)
    return self

  _js__builder__ = '''
      data.forEach(function(rec, i){
        var li = document.createElement('li');
        if (i == 0) {li.style.display = 'block'} else{li.style.display = 'none'};
        var img = document.createElement('img'); img.src = rec.path +'/'+ rec.image; li.appendChild(img);
        var title = document.createElement('h3'); title.innerHTML = rec.title; li.appendChild(title); 
        htmlObj.appendChild(li);
        var label = document.createElement('label'); label.style.backgroundColor = options.color; 
        label.style.borderRadius = '20px'; label.for = i; label.innerHTML = '&nbsp;'; 
        document.getElementById(htmlObj.id +'_bullets').appendChild(label)
      })'''

  def __str__(self):
    self.container._vals = self.items
    self.attr['data-last_picture'] = len(self.items)-1
    self.points.style.css.cursor = "pointer"
    if not self.__point_display:
      self.points.style.css.display = 'none'
    self.points.click([
      self.page.js.getElementsByName("%s_img" % self.htmlCode).css({"display": 'none'}),
      self.page.js.getElementById("%s_img_' + data.position +'" % self.htmlCode).css({"display": 'block'})
    ] + self.__click_items)
    if hasattr(self.next, 'html'):
      self.next.click([
        data.primitives.float(self.dom.attr("data-current_picture").toString().parseFloat().add(1), 'picture_index'),
        self.js.if_(self.page.js.object('picture_index') <= self.dom.attr('data-last_picture'), [
          self.dom.attr("data-current_picture", self.page.js.object('picture_index')),
          "(function(){var clickEvent = new Event('click'); %s.dispatchEvent(clickEvent)})()" %
          self.page.js.getElementsByName("%s_points" % self.htmlCode)[
            self.dom.getAttribute('data-current_picture').toString().parseFloat()]]).else_([
              self.dom.attr("data-current_picture", -1),
              self.next.dom.events.trigger("click")
        ] if self.infinity else None)
      ])
    if hasattr(self.previous, 'html'):
      self.previous.click([
        data.primitives.float(self.dom.attr("data-current_picture").toString().parseFloat().add(-1), 'picture_index'),
        self.js.if_(self.page.js.object('picture_index') >= 0, [
          self.dom.attr("data-current_picture", self.page.js.object('picture_index')),
          "(function(){var clickEvent = new Event('click'); %s.dispatchEvent(clickEvent) })()" %
          self.page.js.getElementsByName("%s_points" % self.htmlCode)[
            self.dom.getAttribute('data-current_picture').toString().parseFloat()]]).else_([
              self.dom.attr("data-current_picture", len(self.items)),
              self.previous.dom.events.trigger("click")
        ] if self.infinity else None)
      ])
    return '''<div %(strAttr)s>%(img_cont)s%(points)s%(next)s%(previous)s</div>
      ''' % {'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), 'img_cont': self.container.html(),
             "points": self.points.html(), 'next': self.next.html() if hasattr(self.next, 'html') else '',
             'previous': self.previous.html() if hasattr(self.previous, 'html') else ''}


class Icon(Html.Html):
  name = 'Icon'

  def __init__(self, page, value, width, height, color, tooltip, options, html_code, profile):
    if options['icon_family'] is not None and options['icon_family'] != 'bootstrap-icons':
      self.requirements = (options['icon_family'],)
    super(Icon, self).__init__(page, "", css_attrs={"color": color, "width": width, "height": height},
                               html_code=html_code, profile=profile)
    if options['icon_family'] == 'office-ui-fabric-core':
      self.attr['class'].add("ms-Icon")
      if not value.startswith("ms-Icon--"):
        value = "ms-Icon--%s" % value
    elif options['icon_family'] == 'material-design-icons':
      self.attr['class'].add("material-icons")
      self._vals = value
      value = ""
    elif options['icon_family'] == 'bootstrap-icons':
      from epyk.fwk.bs import PkgImports
      if self.page.ext_packages is None:
        self.page.ext_packages = {}
      self.page.ext_packages.update(PkgImports.BOOTSTRAP)
      self.page.cssImport.add("bootstrap-icons")
    if value is not None:
      self.attr['class'].add(value)
    self.attr['aria-hidden'] = 'true'
    if tooltip is not None:
      self.tooltip(tooltip)

  def goto(self, url: str, js_funcs: Optional[Union[str, list]] = None, profile: Optional[Union[dict, bool]] = None,
           target: str = "_blank", source_event: Optional[str] = None):
    """
    Description:
    -----------
    Click event which redirect to another page.

    Attributes:
    ----------
    :param str url: The url text.
    :param Optional[Union[str, list]] js_funcs: Optional. The Javascript Events triggered before the redirection.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    :param str target: Optional. The name (type) of the href link.
    :param str source_event: Optional. The event source.
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.js.location.open_new_tab(url, target))
    return self.click(js_funcs, profile, source_event)

  @property
  def dom(self) -> JsHtml.JsHtmlIcon:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlIcon
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlIcon(self, page=self.page)
    return self._dom

  @property
  def style(self) -> GrpClsImage.ClassIcon:
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsImage.ClassIcon
    """
    if self._styleObj is None:
      self._styleObj = GrpClsImage.ClassIcon(self)
    return self._styleObj

  def spin(self):
    """
    Description:
    ------------
    Add the spin class to the font awesome icon.

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
    Add the pulse class to the font awesome icon.

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
    Add a border to the icon.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons
    """
    if 'font-awesome' in self.requirements:
      self.attr['class'].add("fa-border")
    return self

  def size(self, value: int):
    """
    Description:
    ------------
    Icons inherit the font-size of their parent container which allow them to match any text you might use with them.
    With the following classes, we can increase or decrease the size of icons relative to that inherited font-size.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/sizing-icons

    Attributes:
    ----------
    :param int value: The value of the size factor for the icon.
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
    Add a class of fa-fw on the HTML element referencing your icon to set one or more icons to the same fixed width.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/fixed-width-icons
    """
    if 'font-awesome' in self.requirements:
      self.attr['class'].add("fa-fw")
    return self

  def rotate(self, value: int):
    """
    Description:
    ------------
    To arbitrarily rotate and flip icons, use the fa-rotate-* and fa-flip-* classes when you reference an icon.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/rotating-icons

    Attributes:
    ----------
    :param int value: The rotation angle.
    """
    if 'font-awesome' in self.requirements:
      self.attr['class'].add("fa-rotate-%s" % value)
    return self

  def flip(self, direction: str = 'h'):
    """
    Description:
    ------------
    To arbitrarily rotate and flip icons, use the fa-rotate-* and fa-flip-* classes when you reference an icon.
    This will use the font-awesome flip classes.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/rotating-icons

    Attributes:
    ----------
    :param string direction: Optional. The direction reference (h or v).
    """
    if 'font-awesome' in self.requirements:
      if direction.lower() == 'h':
        self.attr['class'].add("fa-flip-horizontal")
      elif direction.lower() == 'v':
        self.attr['class'].add("fa-flip-vertical")
      else:
        self.attr['class'].add("fa-flip-both")
    return self

  def pull(self, position: str = 'left'):
    """
    Description:
    ------------
    Use fa-border and fa-pull-right or fa-pull-left for easy pull quotes or article icons.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons

    Attributes:
    ----------
    :param str position: Optional.
    """
    if 'font-awesome' in self.requirements:
        self.attr['class'].add("fa-pull-%s" % position)
    return self

  def set_icon(self, value: str):
    """
    Description:
    ------------
    Add the icon class reference to the CSS class attribute of the component.

    Attributes:
    ----------
    :param str value: An icon class reference.
    """
    self.attr['class'].add(value)
    return self

  def hover_colors(self, color_hover: str, color_out: str = None):
    """
    Description:
    ------------
    Change the color of the button background when the mouse is hover.

    Usage::

      page.ui.icons.capture().icon.hover_colors("red", "yellow")

    Attributes:
    ----------
    :param str color_hover: The color of the icon when mouse hover
    :param str color_out: Optional. The color of the icon when mouse out
    """
    if color_out is None:
      color_out = self.page.theme.success.base
    else:
      self.css({"color": color_out})
    self.set_attrs(name="onmouseover", value="this.style.color='%s'" % color_hover)
    self.set_attrs(name="onmouseout", value="this.style.color='%s'" % color_out)
    return self

  def click(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None, source_event: str = None,
            on_ready: bool = False):
    """
    Description:
    ------------
    The onclick event occurs when the user clicks on an element.

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Union[bool, dict] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] source_event: Optional. The JavaScript DOM source for the event (can be a sug item).
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.style.css.cursor = "pointer"
    return super(Icon, self).click(js_funcs, profile, source_event, on_ready=on_ready)

  _js__builder__ = '''
      if (typeof data !== 'undefined'){
      htmlObj.classList = []; data.split(' ').forEach(function(cls){htmlObj.classList.add(cls)});
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}}'''

  def __str__(self):
    return '<i %s>%s</i>' % (self.get_attrs(css_class_names=self.style.get_classes()), self.val)


class IconToggle(Icon):

  def add_components(self, components: List[Html.Html]):
    """
    Description:
    ------------
    Add a list of components.

    Attributes:
    ----------
    :param List[Html.Html] components: The HTML components.
    """
    self._linked_components = components
    return self

  def click(self, js_on_off_funcs: Union[list, str] = None, profile: Union[bool, dict] = None, source_event: str = None,
            on_ready: bool = False):
    """
    Description:
    ------------
    The onclick event occurs when the user clicks on an element.

    Attributes:
    ----------
    :param Union[list, str] js_on_off_funcs: The Javascript functions.
    :param Union[bool, dict] profile: Optional. A flag to set the component performance storage.
    :param str source_event: Optional. The JavaScript DOM source for the event (can be a sug item).
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.style.css.cursor = "pointer"
    if js_on_off_funcs is None:
      js_on_off_funcs = {}
    js_funcs_on = js_on_off_funcs.get("on", [])
    js_funcs_off = js_on_off_funcs.get("off", [])
    if getattr(self, "_linked_components", None) is not None:
      for c in self._linked_components:
        js_funcs_on.append(c.dom.hide().r)
    js_funcs_on.append(self.build(self.icon_off))
    if not isinstance(js_funcs_off, list):
      js_funcs_off = [js_funcs_off]
    if getattr(self, "_linked_components", None) is not None:
      for c in self._linked_components:
        js_funcs_off.append(c.dom.show().r)
    js_funcs_off.append(self.build(self.icon_on))
    return super(Icon, self).click(
      self.page.js.if_(self.dom.content.toString().indexOf(self.icon_on) >= 0, js_funcs_on).else_(js_funcs_off),
      profile, source_event, on_ready=on_ready)


class Emoji(Html.Html):
  name = 'Emoji'

  def __init__(self, page: primitives.PageModel, symbol: str, top: tuple, options: Optional[dict],
               profile: Optional[Union[dict, bool]]):
    super(Emoji, self).__init__(page, symbol, options=options, profile=profile)
    self.style.css.margin_top = '%s%s' % (top[0], top[1])

  _js__builder__ = '''
      htmlObj.innerHTML = data; 
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  @property
  def dom(self) -> JsHtml.JsHtmlRich:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlRich
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlRich(self, page=self.page)
    return self._dom

  def __str__(self):
    return '<p %s>%s</p>' % (self.get_attrs(css_class_names=self.style.get_classes()), self.val)


class Badge(Html.Html):
  name = 'Badge'
  requirements = (cssDefaults.ICON_FAMILY, 'bootstrap')
  _option_cls = OptButton.OptionsBadge

  def __init__(self, page: primitives.PageModel, text, width, height, label, icon, background_color,
               color, url, tooltip, options, profile):
    super(Badge, self).__init__(
      page, None, css_attrs={"width": width, "height": height}, profile=profile, options=options)
    self.add_label(label, html_code=self.htmlCode, css={"vertical-align": "middle", "width": 'none', "height": 'none'})
    if self.options.badge_position == 'left':
      self.add_icon(icon, html_code=self.htmlCode, css={"float": 'None', 'margin-left': "5px"}, position="after",
                    family=options.get("icon_family"))
    else:
      self.add_icon(icon, html_code=self.htmlCode, css={"float": 'left', 'margin-left': "5px"},
                    family=options.get("icon_family"))
    if hasattr(self.icon, 'css') and width[0] is not None:
      self.icon.css({"font-size": "%s%s" % (width[0], width[1])})
    self.link = None
    if url is not None:
      self.link = self.page.ui.links.external(text, url).css(
        {"color": "inherit", 'display': 'inline-block', "padding": "2px", "width": "auto"})
      self.link.options.managed = False
    else:
      self.link = self.page.ui.text(text).css(
        {'display': 'inline-block', "padding": "2px", "width": "auto"})
    self.link.css(self.options.badge_css)
    self.link.attr["name"] = "badge-value"
    self.link.css(
      {"color": color, "border-radius": "20px", 'margin-left': '2px', 'right': '12px',
       'background': background_color, 'top': "-5px"})
    self.link.options.managed = False
    self.attr['class'].add("badge")
    if tooltip is not None:
      self.tooltip(tooltip)

  _js__builder__ = '''
      htmlObj.innerHTML = data; 
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  @property
  def dom(self) -> JsHtml.JsHtml:
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript available for a DOM element by default.

    Usage::

      div = page.ui.div(htmlCode="testDiv")
      print(div.dom.content)

    :return: A Javascript Dom object.

    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtml(component=self, page=self.page)
      self._dom.varName = "document.getElementById('%s').querySelector('div[name=badge-value]')" % self.htmlCode
    return self._dom

  @property
  def options(self) -> OptButton.OptionsBadge:
    """
    Description:
    ------------
    Property to the options specific to the HTML component.

    :rtype: OptButton.OptionsBadge
    """
    return super().options

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    -----------
    The onclick event occurs when the user clicks on an element.

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: Optional. The JavaScript DOM source for the event (can be a sug item).
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.icon.style.add_classes.icon.standard()
    return super(Badge, self).click(js_funcs, profile, source_event, on_ready=on_ready)

  def __str__(self):
    return '<span %s>%s</span>' % (self.get_attrs(css_class_names=self.style.get_classes()), self.link)


class Figure(HtmlContainer.Div):
  name = 'Figure container'

  def __str__(self):
    rows = []
    for component in self.val:
      if hasattr(component, 'html'):
        if self._sort_propagate:
          component.sortable(self._sort_options)
        rows.append(component.html())
      else:
        rows.append(str(component))

    return "<figure %s>%s</figure>%s" % (
      self.get_attrs(css_class_names=self.style.get_classes()), "".join(rows), self.helper)


class SlideShow(Html.Html):
  name = 'Slide Show'
  requirements = ('tiny-slider', )
  _option_cls = OptImg.OptionsTinySlider

  def __init__(self, page, images, width, height, options, profile):
    super(SlideShow, self).__init__(page, [], css_attrs={"width": width, "height": height},
                                    profile=profile, options=options)
    for i in images:
      self.add(i)

  def add_plot(self, plot, width: tuple = (220, 'px')):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param plot: matplotlib.pyplot. The ploting features in matplotlib.
    :param tuple width: Optional.

    :return: self to allow the chaining.
    """
    img = self.page.ui.img(width=width)
    img.style.css.display = "inline-block"
    img.from_plot(plot)
    self.add(img)
    return self

  @property
  def style(self) -> GrpClsImage.ClassTinySlider:
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsImage.ClassTinySlider
    """
    if self._styleObj is None:
      self._styleObj = GrpClsImage.ClassTinySlider(self)
    return self._styleObj

  @property
  def jsonId(self):
    """
    Description:
    ------------
    Return the Javascript variable of the json object.
    """
    return "%s_obj" % self.htmlCode

  @property
  def js(self) -> JsTinySlider.TinySlider:
    """
    Description:
    -----------
    The tiny slider javascript events.

    Return the Javascript internal object.

    :return: A Javascript object

    :rtype: JsTinySlider.TinySlider
    """
    if self._js is None:
      self._js = JsTinySlider.TinySlider(self.page, js_code=self.jsonId, set_var=False, parent=self)
    return self._js

  @property
  def dom(self) -> JsHtmlTinySlider.JsHtmlTinySlider:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object.

    :rtype: JsHtmlTinySlider.JsHtmlTinySlider
    """
    if self._dom is None:
      self._dom = JsHtmlTinySlider.JsHtmlTinySlider(self, page=self.page)
    return self._dom

  def _events(self, event, js_funcs, source_event, profile=None, add=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param event: String. The event type.
    :param js_funcs: List | String. The JavaScript fragments.
    :param source_event: String. The source target for the event.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param add: Boolean. Optional.
    """
    if add:
      self.onReady(["%s.on('%s', function (info, eventName) {%s})" % (
        source_event, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))])
    else:
      self.onReady(["%s.off('%s', function (info, eventName) {%s})" % (
        source_event, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))])
    return self

  def add_index_changed(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                        source_event: Optional[str] = None):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("indexChanged", js_funcs, source_event or "%s.events" % self.jsonId, profile)

  def rem_index_changed(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                        source_event: Optional[str] = None):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("indexChanged", js_funcs, source_event or "%s.events" % self.jsonId, profile, add=False)

  def add_transition_start(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                           source_event: Optional[str] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("transitionStart", js_funcs, source_event or "%s.events" % self.jsonId, profile)

  def rem_transition_start(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                           source_event: Optional[str] = None):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("transitionStart", js_funcs, source_event or "%s.events" % self.jsonId, profile, add=False)

  def add_transition_end(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                         source_event: Optional[str] = None):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("transitionEnd", js_funcs, source_event or "%s.events" % self.jsonId, profile)

  def rem_transition_end(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                         source_event: Optional[str] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("transitionEnd", js_funcs, source_event or "%s.events" % self.jsonId, profile, add=False)

  def add_new_breakpoint_start(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                               source_event: Optional[str] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("newBreakpointStart", js_funcs, source_event or self.jsonId, profile)

  def rem_new_breakpoint_start(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                               source_event: Optional[str] = None):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("newBreakpointStart", js_funcs, source_event or self.jsonId, profile, add=False)

  def add_new_breakpoint_end(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                             source_event: Optional[str] = None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("newBreakpointEnd", js_funcs, source_event or self.jsonId, profile)

  def rem_new_breakpoint_end(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                             source_event: Optional[str] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("newBreakpointEnd", js_funcs, source_event or self.jsonId, profile, add=False)

  def add_touch_start(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                      source_event: Optional[str] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("touchStart", js_funcs, source_event or self.jsonId, profile)

  def rem_touch_start(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                      source_event: Optional[str] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("touchStart", js_funcs, source_event or self.jsonId, profile, add=False)

  def add_touch_move(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                     source_event: Optional[str] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("touchMove", js_funcs, source_event or self.jsonId, profile)

  def rem_touch_move(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                     source_event: Optional[str] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("touchMove", js_funcs, source_event or self.jsonId, profile, add=False)

  def add_touch_end(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                    source_event: Optional[str] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("touchEnd", js_funcs, source_event or self.jsonId, profile)

  def rem_touch_dnd(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                    source_event: Optional[str] = None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("touchEnd", js_funcs, source_event or self.jsonId, profile, add=False)

  def add_drag_start(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                     source_event: Optional[str] = None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("dragStart", js_funcs, source_event or self.jsonId, profile)

  def rem_drag_start(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                     source_event: Optional[str] = None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("dragStart", js_funcs, source_event or self.jsonId, profile, add=False)

  def add_drag_move(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                    source_event: Optional[str] = None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("dragMove", js_funcs, source_event or self.jsonId, profile)

  def rem_drag_move(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                    source_event: Optional[str] = None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("dragMove", js_funcs, source_event or self.jsonId, profile, add=False)

  def add_drag_end(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                   source_event: Optional[str] = None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("dragEnd", js_funcs, source_event or self.jsonId, profile)

  def rem_drag_end(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                   source_event: Optional[str] = None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param Union[list, str] js_funcs: The JavaScript fragments.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: The source target for the event.
    """
    return self._events("dragEnd", js_funcs, source_event or self.jsonId, profile, add=False)

  def refresh(self):
    """
    Description:
    -----------
    Component refresh function. Javascript function which can be called in any Javascript event.
    """
    return self.build([], self._jsStyles)

  @property
  def options(self) -> OptImg.OptionsTinySlider:
    """
    Description:
    ------------
    The tiny slider options.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider

    :rtype: OptImg.OptionsTinySlider
    """
    return super().options

  def empty(self):
    """
    Description:
    ------------
    Empty all the values already defined on the Python side.
    This will be called before the JavaScript Transpilation.
    """
    self._vals = []
    self.components = {}
    return self

  def add(self, component: Html.Html):
    """
    Description:
    ------------
    Add a component to the slider container.

    Attributes:
    ----------
    :param Html.Html component: A component to be added to the slider container
    """
    if not hasattr(component, 'options'):
      component = self.page.ui.div(component)
    component.options.managed = False
    self.val.append(component)
    self.components[component.htmlCode] = component
    return self

  def __len__(self):
    return len(self.val)

  _js__builder__ = '''
      if(typeof window[ htmlObj.id + '_obj'] !== 'undefined') {window[ htmlObj.id + '_obj'].destroy();} 
      window[ htmlObj.id + '_obj'] = tns(options)'''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    rows = [htmlObj.html() for htmlObj in self.val]
    return '<div %s>%s</div>' % (self.get_attrs(css_class_names=self.style.get_classes()), "".join(rows))


class Background(HtmlContainer.Div):

  def build(self, value: Union[str, list, primitives.JsDataModel] = None, options: dict = None,
            profile: Union[bool, dict] = None, component_id: str = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[str, list, primitives.JsDataModel] value:
    :param dict options: Optional. Specific Python options available for this component.
    :param Union[bool, dict] profile: Optional. A flag to set the component performance storage.
    :param str component_id: Optional. A DOM component reference in the page.
    """
    if isinstance(value, dict):
      js_data = "{%s}" % ",".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in value.items()])
    else:
      js_data = JsUtils.jsConvertData(value, None)
    options, js_options = options or {}, []
    for k, v in options.items():
      if isinstance(v, dict):
        row = ["%s: %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
        js_options.append("%s: {%s}" % (k, ", ".join(row)))
      else:
        js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
    return '''%s.style.backgroundImage = "url('" + %s +"')"''' % (component_id or self.dom.varId, js_data)
