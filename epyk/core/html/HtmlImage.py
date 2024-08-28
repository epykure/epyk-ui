#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import io
import base64

from typing import Union, Optional, List
from epyk.core.py import primitives
from epyk.core.py import types

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
    tag = "img"

    def __init__(self, page, image, path, align, html_code, width, height, profile, options):
        if path is None and image is not None:
            if Defaults.SERVER_PATH is not None and not (image.startswith("http") or image.startswith("data:")):
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
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlImg(self, page=self.page)
        return self._dom

    def goto(self, url: str, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
             target: str = "_blank", source_event: str = None):
        """Click event which redirect to another page.

        :param url: the url.
        :param js_funcs: Optional. The Javascript Events triggered before the redirection
        :param profile: Optional. A flag to set the component performance storage
        :param target: Optional. The target attribute specifies where to open the linked document
        :param source_event: Optional. The event source
        """
        js_funcs = js_funcs or []
        self.style.css.cursor = 'pointer'
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_funcs.append(self.js.location.open_new_tab(url, target))
        return self.click(js_funcs, profile, source_event)

    def from_plot(self, plt):
        """Load an image from a plt object from matplotlib.

        Usage::

          x = np.arange(0, 15, 0.1)
          y = np.sin(x)
          plt.plot(x, y)

          img2 = page.ui.img(width=(50, "%"))
          img2.from_plot(plt)
          img2.style.css.display = "inline-block"

        :param plt: matplotlib.pyplot. The ploting features in matplotlib.

        :return: self to allow the chaining
        """
        str_io = io.BytesIO()
        plt.savefig(str_io, format='jpg')
        str_io.seek(0)
        plt.close(1)
        return self.from_base64(base64.b64encode(str_io.read()).decode("utf-8"))

    def from_base64(self, text: str):
        """Load an image from a base64 string.

        Usage::

          x = np.arange(0, 15, 0.1)
          y = np.sin(x)
          plt.plot(x, y)

          str_io = io.BytesIO()
          plt.savefig(str_io, format='jpg')
          str_io.seek(0)

          self.from_base64(base64.b64encode(str_io.read()).decode("utf-8"))

        :param text: The encoded picture

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

    def loading(self, status: bool = True, label: str = "https://loading.io/mod/spinner/spinner/sample.gif",
                *args, **kwargs) -> str:
        """Loading feature for image.

        Usage::

            chart_obj.loading()
            ....
            chart_obj.loading(False)

        :param status: Optional. Specific the status of the display of the loading component
        :param label: Optional. Picture full path
        """
        if status:
            return ''' 
document.getElementById('%(htmlId)s').src = "error_link";
document.getElementById('%(htmlId)s').onerror = function(){this.onerror=null;this.src=%(label)s;}
''' % {"htmlId": self.htmlCode, 'label': JsUtils.jsConvertData(label, None)}

        return ""

    def __str__(self):
        if self.val["image"] is not None:
            self.attr["src"] = "%(path)s/%(image)s" % self.val
        return '<%s %s />%s' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.helper)


class AnimatedImage(Html.Html):
    name = 'Animated Picture'
    tag = "div"

    def __init__(self, page, image, text, title, html_code, url, path, width, height, options, profile):
        if path is None:
            if Defaults.SERVER_PATH is not None and not (image.startswith("http") or image.startswith("data:")):
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
        self.title = page.ui.tags.h2(title, html_code=self.sub_html_code("title")).css({"display": 'block'})
        self.text = page.ui.tags.p(text, html_code=self.sub_html_code("text")).css({"display": 'block'})
        self.a = page.ui.tags.a("Enter", url, html_code=self.sub_html_code("link")).css({"width": "100px", "background": "white"})
        self.a.style.add_classes.image.info_link()
        self.div = page.ui.div([self.title, self.text, self.a], html_code=self.sub_html_code("menu"), width=(100, "%"))
        self.div.style.add_classes.image.mask()
        self.div.style.css.position = "absolute"
        self.div.style.css.padding = 10
        self.div.options.managed = False
        self.style.css.position = "relative"

    def from_plot(self, plt):
        """Load an image from a plt object from matplotlib.

        Usage::

          x = np.arange(0, 15, 0.1)
          y = np.sin(x)
          plt.plot(x, y)

          img2 = page.ui.img(width=(50, "%"))
          img2.from_plot(plt)
          img2.style.css.display = "inline-block"

        :param plt: matplotlib.pyplot. The plotting features in matplotlib

        :return: self to allow the chaining.
        """
        str_io = io.BytesIO()
        plt.savefig(str_io, format='jpg')
        str_io.seek(0)
        plt.close(1)
        return self.from_base64(base64.b64encode(str_io.read()).decode("utf-8"))

    def from_base64(self, text: str):
        """Load an image from a base64 string.

        Usage::

          x = np.arange(0, 15, 0.1)
          y = np.sin(x)
          plt.plot(x, y)

          str_io = io.BytesIO()
          plt.savefig(str_io, format='jpg')
          str_io.seek(0)

          self.from_base64(base64.b64encode(str_io.read()).decode("utf-8"))

        :param text: The encoded picture

        :return: self to allow the chaining
        """
        self.img.val["path"] = "data:image"
        self.img.val["image"] = "png;base64,%s" % text
        return self

    def __str__(self):
        return '''<%(tag)s %(cssAttr)s>%(div)s%(img)s</%(tag)s>''' % {
          "cssAttr": self.get_attrs(css_class_names=self.style.get_classes()), 'img': self.img.html(),
          'div': self.div.html(), "tag": self.tag}


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
                    rec = {"image": rec, 'title': "picture %s" % (i + 1)}
                if 'path' not in rec:
                    rec['path'] = path
                if rec.get('selected') is not None:
                    selected = i
                img = page.ui.img(rec["image"], path=rec["path"], width=width,
                                  html_code=self.sub_html_code("title", auto_inc=True),
                                  height=(height[0] - 60 if height[0] is not None else None, height[1]))
                img_title = page.ui.tags.h3(rec['title'], html_code=self.sub_html_code("label", auto_inc=True))
                div = page.ui.layouts.div([img_title, img], html_code=self.sub_html_code("panel", auto_inc=True)).css(
                    {"display": 'none', "text-align": "center"})
                div.title = img_title
                div.img = img
            else:
                div = page.ui.layouts.div(rec, html_code=self.sub_html_code("panel", auto_inc=True)).css(
                    {"display": 'none', "text-align": "center"})
            div.set_attrs(name="name", value=self.i_name)
            div.options.managed = False
            self.items.append(div)
        self.__point_display = options.get('points', True)
        self.infinity = options.get('infinity', False)
        self.container = self.page.ui.layouts.div().css({"display": 'block', "width": "100%", "text-align": "center"})
        self.container.options.managed = False
        if 'arrows' in options:
            self.next = self.page.ui.icon(
                options.get("arrows-right", "fas fa-chevron-right"),
                html_code=self.sub_html_code("next")).css(
                {"position": 'absolute', "font-size": '35px', "padding": '8px', "right": '10px', 'top': '50%'})
            self.next.options.managed = False
            self.previous = self.page.ui.icon(
                options.get("arrows-left", "fas fa-chevron-left"),
                html_code=self.sub_html_code("prev")).css(
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

    @property
    def i_name(self) -> str:
        """Images common names"""
        return "%s_img" % self.html_code

    def add_plot(self, plot, title: str = "", width: types.SIZE_TYPE = "auto"):
        """
        :param plot: matplotlib.pyplot. The plotting features in matplotlib
        :param title: Optional. The chart title
        :param width: Optional.

        :return: self to allow the chaining.
        """
        img = self.page.ui.img(width=width)
        img.from_plot(plot)
        title = self.page.ui.tags.h3(title)
        div = self.page.ui.layouts.div([title, img], html_code=self.sub_html_code("panel", auto_inc=True)).css(
            {"display": 'none', "text-align": "center"})
        div.title = title
        div.img = img
        div.set_attrs(name="name", value=self.i_name)
        div.options.managed = False
        self.items.append(div)
        return self

    def set_nav_dots(self, selected: int = 0):
        """

        :param selected:

        :return: self to allow the chaining.
        """
        self.items[selected].css({"display": 'block'})
        self.points = self.page.ui.navigation.points(
            len(self.items), html_code=self.sub_html_code("points"), options={"managed": False})
        return self

    def from_base64_list(self, values: List[str], width: Union[str, tuple] = "auto"):
        """

        :param values:
        :param width: Optional.

        :return: self to allow the chaining.
        """
        for val in values:
            img = self.page.ui.img(width=width)
            img.from_base64(val)
            div = self.page.ui.layouts.div([img], html_code=self.sub_html_code("panel", auto_inc=True)).css(
                {"display": 'none', "text-align": "center"})
            div.img = img
            div.set_attrs(name="name", value=self.i_name)
            div.options.managed = False
            self.items.append(div)
        return self

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: str = None, on_ready: bool = False):
        """Add click event on this component.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: optional. The reference of the component
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__click_items.extend(js_funcs)
        return self

    def __str__(self):
        self.container._vals = self.items
        self.attr['data-last_picture'] = len(self.items) - 1
        self.points.style.css.cursor = "pointer"
        if not self.__point_display:
            self.points.style.css.display = 'none'
        self.points.click([
                              self.page.js.getElementsByName(self.i_name).css({"display": 'none'}),
                              self.page.js.getElementById("%s_panel_' + data.position +'" % self.html_code).css(
                                  {"display": 'block'})
                          ] + self.__click_items)
        if hasattr(self.next, 'html'):
            self.next.click([
                data.primitives.float(self.dom.attr("data-current_picture").toString().parseFloat().add(1),
                                      'picture_index'),
                self.js.if_(self.page.js.object('picture_index') <= self.dom.attr('data-last_picture'), [
                    self.dom.attr("data-current_picture", self.page.js.object('picture_index')),
                    "(function(){var clickEvent = new Event('click'); %s.dispatchEvent(clickEvent)})()" %
                    self.page.js.getElementsByName(self.sub_html_code("points"))[
                        self.dom.getAttribute('data-current_picture').toString().parseFloat()]]).else_(
                    [self.dom.attr("data-current_picture", -1), self.next.dom.events.trigger("click")
                     ] if self.infinity else None)
            ])
        if hasattr(self.previous, 'html'):
            self.previous.click([
                data.primitives.float(self.dom.attr("data-current_picture").toString().parseFloat().add(-1),
                                      'picture_index'),
                self.js.if_(self.page.js.object('picture_index') >= 0, [
                    self.dom.attr("data-current_picture", self.page.js.object('picture_index')),
                    "(function(){var clickEvent = new Event('click'); %s.dispatchEvent(clickEvent) })()" %
                    self.page.js.getElementsByName(self.sub_html_code("points"))[
                        self.dom.getAttribute('data-current_picture').toString().parseFloat()]]).else_(
                    [self.dom.attr("data-current_picture", len(self.items)),
                     self.previous.dom.events.trigger("click")] if self.infinity else None)
            ])
        return '''<div %(strAttr)s>%(img_cont)s%(points)s%(next)s%(previous)s</div>
      ''' % {'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), 'img_cont': self.container.html(),
             "points": self.points.html(), 'next': self.next.html() if hasattr(self.next, 'html') else '',
             'previous': self.previous.html() if hasattr(self.previous, 'html') else ''}


class Icon(Html.Html):
    name = 'Icon'
    builder_module = "HtmlIcon"
    tag = "i"

    def __init__(self, page, value, width, height, color, tooltip, options, html_code, profile, text: str = ""):
        if options['icon_family'] is not None and options['icon_family'] != 'bootstrap-icons':
            self.requirements = (options['icon_family'],)
        super(Icon, self).__init__(page, text, css_attrs={"color": color, "width": width, "height": height},
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
            self.attr['class'].add("bi")
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

    def goto(self, url: str, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
             target: str = "_blank", source_event: str = None):
        """Click event which redirect to another page.

        :param url: The url text
        :param js_funcs: Optional. The Javascript Events triggered before the redirection
        :param profile: Optional. A flag to set the component performance storage
        :param target: Optional. The name (type) of the href link
        :param source_event: Optional. The event source
        """
        js_funcs = js_funcs or []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_funcs.append(self.js.location.open_new_tab(url, target))
        return self.click(js_funcs, profile, source_event)

    @property
    def dom(self) -> JsHtml.JsHtmlIcon:
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlIcon(self, page=self.page)
        return self._dom

    @property
    def style(self) -> GrpClsImage.ClassIcon:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsImage.ClassIcon(self)
        return self._styleObj

    def spin(self):
        """Add the spin class to the font awesome icon.
        `Fontawesome <https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons>`_
        """
        if 'font-awesome' in self.requirements:
            self.attr['class'].add("fa-spin")
        return self

    def pulse(self):
        """Add the pulse class to the font awesome icon.
        `Fontawesome <https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons>`_
        """
        if 'font-awesome' in self.requirements:
            self.attr['class'].add("fa-pulse")
        return self

    def border(self):
        """Add a border to the icon.
        `Fontawesome <https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons>`_
        """
        if 'font-awesome' in self.requirements:
            self.attr['class'].add("fa-border")
        return self

    def size(self, value: int):
        """Icons inherit the font-size of their parent container which allow them to match any text you might use with
        them. With the following classes, we can increase or decrease the size of icons relative to that inherited
        font-size.
        `Fontawesome <https://fontawesome.com/how-to-use/on-the-web/styling/sizing-icons>`_

        :param value: The value of the size factor for the icon
        """
        if 'font-awesome' in self.requirements:
            if isinstance(value, int):
                self.attr['class'].add("fa-%sx" % value)
            else:
                self.attr['class'].add("fa-%s" % value)
        return self

    def fixed_width(self):
        """Add a class of fa-fw on the HTML element referencing your icon to set one or more icons to the same fixed
        width.
        `Fontawesome <https://fontawesome.com/how-to-use/on-the-web/styling/fixed-width-icons>`_
        """
        if 'font-awesome' in self.requirements:
            self.attr['class'].add("fa-fw")
        return self

    def rotate(self, value: int):
        """To arbitrarily rotate and flip icons, use the fa-rotate-* and fa-flip-* classes when you reference an icon.
        `Fontawesome <https://fontawesome.com/how-to-use/on-the-web/styling/rotating-icons>`_

        :param value: The rotation angle
        """
        if 'font-awesome' in self.requirements:
            self.attr['class'].add("fa-rotate-%s" % value)
        return self

    def flip(self, direction: str = 'h'):
        """To arbitrarily rotate and flip icons, use the fa-rotate-* and fa-flip-* classes when you reference an icon.

        This will use the font-awesome flip classes.

        `Fontawesome <https://fontawesome.com/how-to-use/on-the-web/styling/rotating-icons>`_

        :param direction: Optional. The direction reference (h or v)
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
        """Use fa-border and fa-pull-right or fa-pull-left for easy pull quotes or article icons.
        `Fontawesome <https://fontawesome.com/how-to-use/on-the-web/styling/bordered-pulled-icons>`_

        :param position: Optional. The icon pull position
        """
        if 'font-awesome' in self.requirements:
            self.attr['class'].add("fa-pull-%s" % position)
        return self

    def set_icon(self, value: str):
        """Add the icon class reference to the CSS class attribute of the component.

        :param value: An icon class reference
        """
        self.attr['class'].add(value)
        return self

    def hover_colors(self, color_hover: str, color_out: str = None):
        """Change the color of the button background when the mouse is hover.

        Usage::

          page.ui.icons.capture().icon.hover_colors("red", "yellow")

        :param color_hover: The color of the icon when mouse hover
        :param color_out: Optional. The color of the icon when mouse out
        """
        if color_out is None:
            color_out = self.page.theme.success.base
        else:
            self.css({"color": color_out})
        self.set_attrs(name="onmouseover", value="this.style.color='%s'" % color_hover)
        self.set_attrs(name="onmouseout", value="this.style.color='%s'" % color_out)
        return self

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
              on_ready: bool = False):
        """The onclick event occurs when the user clicks on an element.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        """
        self.style.css.cursor = "pointer"
        return super(Icon, self).click(js_funcs, profile, source_event, on_ready=on_ready)

    def press(self, js_press_funcs: types.JS_FUNCS_TYPES = None, js_release_funcs: types.JS_FUNCS_TYPES = None,
              profile: types.PROFILE_TYPE = None, pressed_class: str = None, on_ready: bool = False):
        """Special click event to keep in memory the state of the component.

        Usage::

          i = page.ui.icon("Click Me")

        :param js_press_funcs: Optional. Javascript functions
        :param js_release_funcs: Optional. Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param pressed_class: Optional. The CSS class when component's status is pressed
        :param on_ready: Optional. Event when component is ready on HTML side
        """
        self.style.css.cursor = "pointer"
        self.style.css.border_radius = 20
        self.style.css.remove("color")
        self.style.add_classes.button.basic()
        self.aria.pressed = False
        if pressed_class is None:
            self.page.properties.css.add_text(
                ".event-pressed {background-color: %s; color: %s; border: 1px solid %s" % (
                    self.page.theme.notch(), self.page.theme.greys[0], self.page.theme.notch()), "event-pressed")
            pressed_class = "event-pressed"
        if not isinstance(js_press_funcs, list):
            js_press_funcs = [js_press_funcs]
        js_press_funcs.insert(0, self.dom.setAttribute("aria-pressed", True))
        js_press_funcs.append(self.dom.addClass(pressed_class))
        str_fnc = "if(%s.getAttribute('aria-pressed') == 'false'){%s}" % (
            self.dom.varId, JsUtils.jsConvertFncs(js_press_funcs, toStr=True))
        if js_release_funcs is not None:
            if not isinstance(js_release_funcs, list):
                js_release_funcs = [js_release_funcs]
            js_release_funcs.insert(0, self.dom.setAttribute("aria-pressed", False))
            js_release_funcs.append(self.dom.removeClass(pressed_class))
            str_fnc = "%s else{%s}" % (str_fnc, JsUtils.jsConvertFncs(js_release_funcs, toStr=True))
        return self.on("click", str_fnc, profile, on_ready=on_ready)

    def __str__(self):
        return '<%s %s>%s</%s>%s' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val, self.tag, self.badge)


class IconToggle(Icon):

    def add_components(self, components: List[Html.Html]):
        """Add a list of components.

        :param components: The HTML components.
        """
        self._linked_components = components
        return self

    def click(self, js_on_off_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
              source_event: str = None, on_ready: bool = False):
        """The onclick event occurs when the user clicks on an element.

        :param js_on_off_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
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
    tag = "p"

    def __init__(self, page: primitives.PageModel, symbol: str, top: tuple, options: Optional[dict],
                 profile: Optional[Union[dict, bool]], html_code: str = None):
        super(Emoji, self).__init__(page, symbol, html_code=html_code, options=options, profile=profile)
        self.style.css.margin_top = '%s%s' % (top[0], top[1])

    @property
    def dom(self) -> JsHtml.JsHtmlRich:
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript by default.

        :return: A Javascript Dom object
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtmlRich(self, page=self.page)
        return self._dom

    def __str__(self):
        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.val, self.tag)


class Badge(Html.Html):
    name = 'Badge'
    requirements = (cssDefaults.ICON_FAMILY, 'bootstrap')
    _option_cls = OptButton.OptionsBadge
    tag = "span"

    def __init__(self, page: primitives.PageModel, text, width, height, label, icon, background_color,
                 color, url, tooltip, html_code, options, profile):
        super(Badge, self).__init__(
            page, None, html_code=html_code, css_attrs={"width": width, "height": height}, profile=profile,
            options=options)
        self.add_label(label, html_code=self.html_code,
                       css={"vertical-align": "middle", "width": 'none', "height": 'none'})
        if self.options.badge_position == 'left':
            self.add_icon(icon, html_code=self.html_code, css={"float": 'None', 'margin-left': "5px"}, position="after",
                          family=options.get("icon_family"))
        else:
            self.add_icon(icon, html_code=self.html_code, css={"float": 'left', 'margin-left': "5px"},
                          family=options.get("icon_family"))
        if hasattr(self.icon, 'css') and width[0] is not None:
            self.icon.css({"font-size": "%s%s" % (width[0], width[1])})
        self.link = None
        if url is not None:
            self.link = self.page.ui.links.external(text, url, html_code=self.sub_html_code("link")).css(
                {"color": "inherit", 'display': 'inline-block', "padding": "2px", "width": "auto"})
            self.link.options.managed = False
        else:
            self.link = self.page.ui.text(text, html_code=self.sub_html_code("link")).css(
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

    @property
    def dom(self) -> JsHtml.JsHtml:
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript available for a DOM element by default.

        Usage::

          div = page.ui.div(htmlCode="testDiv")
          print(div.dom.content)

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtml.JsHtml(component=self, page=self.page)
            self._dom.varName = "document.getElementById('%s').querySelector('div[name=badge-value]')" % self.html_code
        return self._dom

    @property
    def options(self) -> OptButton.OptionsBadge:
        """ Property to the options specific to the HTML component. """
        return super().options

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              source_event: str = None, on_ready: bool = False):
        """The onclick event occurs when the user clicks on an element.

        :param js_funcs: The Javascript functions.
        :param profile: Optional. A flag to set the component performance storage.
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item).
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
        """
        self.icon.style.add_classes.icon.standard()
        return super(Badge, self).click(js_funcs, profile, source_event, on_ready=on_ready)

    def __str__(self):
        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.link, self.tag)


class Figure(HtmlContainer.Div):
    name = 'Figure container'
    tag = "figure"

    def __str__(self):
        rows = []
        for component in self.val:
            if hasattr(component, 'html'):
                if self._sort_propagate:
                    component.sortable(self._sort_options)
                rows.append(component.html())
            else:
                rows.append(str(component))

        return "<%s %s>%s</%s>%s" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(rows), self.tag, self.helper)


class SlideShow(Html.Html):
    name = 'Slide Show'
    tag = "div"
    requirements = ('tiny-slider',)
    _option_cls = OptImg.OptionsTinySlider

    def __init__(self, page, images, width, height, options, profile):
        super(SlideShow, self).__init__(page, [], css_attrs={"width": width, "height": height},
                                        profile=profile, options=options)
        for i in images:
            self.add(i)

    def add_plot(self, plot, width: tuple = (220, 'px')):
        """
        :param plot: matplotlib.pyplot. The plotting features in matplotlib.
        :param width: Optional.

        :return: self to allow the chaining.
        """
        img = self.page.ui.img(width=width, html_code=self.sub_html_code("img", auto_inc=True))
        img.style.css.display = "inline-block"
        img.from_plot(plot)
        self.add(img)
        return self

    @property
    def style(self) -> GrpClsImage.ClassTinySlider:
        """Property to the CSS Style of the component. """
        if self._styleObj is None:
            self._styleObj = GrpClsImage.ClassTinySlider(self)
        return self._styleObj

    @property
    def js(self) -> JsTinySlider.TinySlider:
        """The tiny slider javascript events.

        Return the Javascript internal object.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsTinySlider.TinySlider(page=self.page, js_code=self.js_code, set_var=False, component=self)
        return self._js

    @property
    def dom(self) -> JsHtmlTinySlider.JsHtmlTinySlider:
        """Return all the Javascript functions defined for an HTML Component.

        Those functions will use plain javascript by default.

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtmlTinySlider.JsHtmlTinySlider(self, page=self.page)
        return self._dom

    def _events(self, event, js_funcs: types.JS_FUNCS_TYPES, source_event: str, profile: types.PROFILE_TYPE = None,
                add: bool = True):
        """
        :param event: The event type
        :param js_funcs: The JavaScript fragments
        :param source_event: The source target for the event
        :param profile: Optional. A flag to set the component performance storage
        :param add: Optional.
        """
        if add:
            self.onReady(["%s.on('%s', function (info, eventName) {%s})" % (
                source_event, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))])
        else:
            self.onReady(["%s.off('%s', function (info, eventName) {%s})" % (
                source_event, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))])
        return self

    def add_index_changed(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                          source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("indexChanged", js_funcs, source_event or "%s.events" % self.js_code, profile)

    def rem_index_changed(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                          source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("indexChanged", js_funcs, source_event or "%s.events" % self.js_code, profile, add=False)

    def add_transition_start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                             source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("transitionStart", js_funcs, source_event or "%s.events" % self.js_code, profile)

    def rem_transition_start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                             source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("transitionStart", js_funcs, source_event or "%s.events" % self.js_code, profile, add=False)

    def add_transition_end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                           source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("transitionEnd", js_funcs, source_event or "%s.events" % self.js_code, profile)

    def rem_transition_end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                           source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("transitionEnd", js_funcs, source_event or "%s.events" % self.js_code, profile, add=False)

    def add_new_breakpoint_start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                                 source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("newBreakpointStart", js_funcs, source_event or self.js_code, profile)

    def rem_new_breakpoint_start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                                 source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("newBreakpointStart", js_funcs, source_event or self.js_code, profile, add=False)

    def add_new_breakpoint_end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                               source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("newBreakpointEnd", js_funcs, source_event or self.js_code, profile)

    def rem_new_breakpoint_end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                               source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("newBreakpointEnd", js_funcs, source_event or self.js_code, profile, add=False)

    def add_touch_start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                        source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("touchStart", js_funcs, source_event or self.js_code, profile)

    def rem_touch_start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                        source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("touchStart", js_funcs, source_event or self.js_code, profile, add=False)

    def add_touch_move(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                       source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("touchMove", js_funcs, source_event or self.js_code, profile)

    def rem_touch_move(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                       source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("touchMove", js_funcs, source_event or self.js_code, profile, add=False)

    def add_touch_end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                      source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("touchEnd", js_funcs, source_event or self.js_code, profile)

    def rem_touch_dnd(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                      source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("touchEnd", js_funcs, source_event or self.js_code, profile, add=False)

    def add_drag_start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                       source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("dragStart", js_funcs, source_event or self.js_code, profile)

    def rem_drag_start(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                       source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("dragStart", js_funcs, source_event or self.js_code, profile, add=False)

    def add_drag_move(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                      source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("dragMove", js_funcs, source_event or self.js_code, profile)

    def rem_drag_move(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                      source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("dragMove", js_funcs, source_event or self.js_code, profile, add=False)

    def add_drag_end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                     source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("dragEnd", js_funcs, source_event or self.js_code, profile)

    def rem_drag_end(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                     source_event: str = None):
        """
        :param js_funcs: The JavaScript fragments
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source target for the event
        """
        return self._events("dragEnd", js_funcs, source_event or self.js_code, profile, add=False)

    def refresh(self):
        """Component refresh function. Javascript function which can be called in any Javascript event. """
        return self.build([], self._jsStyles)

    @property
    def options(self) -> OptImg.OptionsTinySlider:
        """The tiny slider options.

        `Package Doc <https://github.com/ganlanyuan/tiny-slider>`_
        """
        return super().options

    def empty(self):
        """Empty all the values already defined on the Python side.

        This will be called before the JavaScript Transpilation.
        """
        self._vals = []
        self.components = {}
        return self

    def add(self, component: Html.Html, **kwargs):
        """Add a component to the slider container.

        :param component: A component to be added to the slider container
        """
        if not hasattr(component, 'options'):
            component = self.page.ui.div(component, html_code=self.sub_html_code("panel", auto_inc=True))
        component.options.managed = False
        self.val.append(component)
        self.components[component.html_code] = component
        return self

    def __len__(self):
        return len(self.val)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        rows = [htmlObj.html() for htmlObj in self.val]
        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), "".join(rows), self.tag)


class Background(HtmlContainer.Div):

    def build(self, value: Union[str, list, primitives.JsDataModel] = None, options: dict = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None,
              dataflows: List[dict] = None, **kwargs) -> str:
        """
        :param value: Optional. Component data
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. A DOM component reference in the page
        :param dataflows: Chain of data transformations
        """
        if isinstance(value, dict):
            js_data = "{%s}" % ",".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in value.items()])
        else:
            js_data = JsUtils.dataFlows(data, dataflows, self.page)
        options, js_options = options or {}, []
        for k, v in options.items():
            if isinstance(v, dict):
                row = ["%s: %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
                js_options.append("%s: {%s}" % (k, ", ".join(row)))
            else:
                js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
        return '''%s.style.backgroundImage = "url('" + %s +"')"''' % (component_id or self.dom.varId, js_data)
