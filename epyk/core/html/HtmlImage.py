"""
Wrapper to the HTML Image components
"""

import re

from epyk.core.html import Html
from epyk.core.html import Options
from epyk.core.html import Defaults

from epyk.core.css import Defaults_css
from epyk.core.css.styles import GrpClsImage

# The list of Javascript classes
from epyk.core.js.html import JsHtml


class Image(Html.Html):
  name, category, callFnc = 'Picture', 'Image', 'img'
  # _grpCls = CssGrpClsImage.CssClassImage

  def __init__(self, report, image, path, align, htmlCode, width, height, profile, options):
    if path is None:
      path = Defaults.SERVER_PATH if report.run.report_name is None else "%s/%s" % (Defaults.SERVER_PATH, report.run.report_name)
    super(Image, self).__init__(report, {'path': path, 'image': image}, code=htmlCode, profile=profile,
                                css_attrs={"width": width, "height": height})
    # self.css({'margin': '5px 5px 5px 0', 'display': 'block'})
    self._jsStyles = options
    if align is not None:
      self.css({"text-align": align})

  @property
  def _js__builder__(self):
    return '''
      if(typeof data.path === 'undefined'){data.path = '%s'};
      htmlObj.src = data.path + "/" + data.image; 
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}
      ''' % Defaults.SERVER_PATH

  def __str__(self):
    self.attr["src"] = "%(path)s/%(image)s" % self.val
    return '<img %s></img>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val): return re.findall("!\[([a-zA-Z 0-9]*)\]\(([:a-zA-Z \-\"/.0-9]*)\)", val)

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report=None):
    for name, image in regExpResult:
      val = val.replace("![%s](%s)" % (name, image), "report.img('%s')" % image)
      if report is not None:
        getattr(report, 'img')(image)
    return [val]

  @classmethod
  def jsMarkDown(cls, vals):
    return "![alt text](%s/images/%s)" % (vals['path'], vals['image'])


class AnimatedImage(Html.Html):
  name, category, callFnc = 'Animated Picture', 'Images', 'animatedimg'
  __reqJs, cssCls = ['jquery'], ['view']
  # _grpCls = CssGrpClsImage.CssClassImageAnimated

  def __init__(self, report, image, text, title, url, path, width, height, profile):
    if path is None:
      path = Defaults.SERVER_PATH if report.run.report_name is None else "%s/%s" % (Defaults.SERVER_PATH, report.run.report_name)
    super(AnimatedImage, self).__init__(report, {'path': path, 'image': image, 'text': text, "title": title, 'url': url},
                                        width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    self.width = width[0]

  @property
  def _js__builder__(self):
    return ''' 
      htmlObj.querySelector('img').src = data.path + "/" + data.image;
      htmlObj.querySelector('div').querySelector('h2').innerHTML = data.title; 
      htmlObj.querySelector('div').querySelector('p').text = data.text; 
      if (data.url != null){htmlObj.querySelector('a').href = data.url}'''

  def __str__(self):
    return '''
      <div %s>
        <img />
        <div class="mask"><h2></h2><p></p><a class="info" style="cursor:pointer">Enter</a></div>
      </div>''' % self.get_attrs(pyClassNames=self.defined)


class ImgCarrousel(Html.Html):
  name, category, callFnc = 'Carrousel', 'Images', 'carrousel'
  # _grpCls = CssGrpClsImage.CssClassImageCarrousel

  def __init__(self, report, images, path, width, height, profile):
    if path is None:
      path = Defaults.SERVER_PATH if report.run.report_name is None else "%s/%s" % (Defaults.SERVER_PATH, report.run.report_name)
    imgs = []
    for i, rec in enumerate(images):
      if not isinstance(rec, dict):
        rec = {"image": rec, 'title': "picture %s" % (i+1)}
      if not 'path' in rec:
        rec['path'] = path
      imgs.append(rec)
    super(ImgCarrousel, self).__init__(report, imgs, width=width[0], widthUnit=width[1], height=height[0],
                                       heightUnit=height[1], profile=profile)
    self.css({'padding-top': '20px', 'display': 'block', 'padding': 0, 'margin': 0})

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
    # self._report.jsOnLoadFnc.add('''
    #   $("label[for][name=img-selector]").click(function(){
    #     for (var i=0; i < %(count)s; i++) {$('#%(htmlId)s_picture_'+ i ).css('display', 'none')}
    #     $("label[for][name=img-selector").css('background', '%(grey)s');
    #     $('#%(htmlId)s_picture_'+ parseInt($(this).attr('for'))).css('display', 'inline-block');
    #     $("label[for='"+ $(this).attr('for') +"'][name=img-selector").css('background', '%(color)s')})
    # ''' % {'htmlId': self.htmlId, 'count': len(self.vals), 'color': self.getColor('colors', 9), 'grey': self.getColor('greys', 2)})
    return '''
      <ul %(strAttr)s></ul>
      <div id="%(htmlId)s_bullets" %(clsTag)s></div>
      ''' % {'strAttr': self.get_attrs(pyClassNames=self.defined), 'htmlId': self.htmlId,
             'clsTag': self._report.style.getClsTag(self.defined.clsAltMap)}


class Icon(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Icon', 'Images', 'icon'

  def __init__(self, report, value, width, height, color, tooltip, profile):
    super(Icon, self).__init__(report, value, css_attrs={"color": color, "width": width, "height": height},
                               profile=profile)
    self.attr['class'].add(value)
    self.attr['aria-hidden'] = 'true'
    if tooltip is not None:
      self.set_attrs(name="title", value=tooltip)

  @property
  def dom(self):
    """
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

    :rtype: GrpClsImage.ClassIcon
    """
    if self._styleObj is None:
      self._styleObj = GrpClsImage.ClassIcon(self)
    return self._styleObj

  def hover_colors(self, color_hover, color_out=None):
    """
    Change the color of the button background when the mouse is hover

    Example
    rptObj.ui.icons.capture().icon.hover_colors("red", "yellow")

    :param color_hover: The color of the icon when mouse hover
    :param color_out: Optional. The color of the icon when mouse out

    """
    if color_out is None:
      color_out = self._report.theme.success[1]
    else:
      self.css({"color": color_out})
    self.set_attrs(name="onmouseover", value="this.style.color='%s'" % color_hover)
    self.set_attrs(name="onmouseout", value="this.style.color='%s'" % color_out)
    return self

  def click(self, jsFncs, profile=False):
    self.style.css.cursor = "pointer"
    return super(Icon, self).click(jsFncs, profile)

  @property
  def _js__builder__(self):
    return '''htmlObj.classList = []; data.split(' ').forEach(function(cls){htmlObj.classList.add(cls)});
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}'''

  def __str__(self):
    return '<i %s></i>' % (self.get_attrs(pyClassNames=self.style.get_classes()))


class Emoji(Html.Html):
  name, category, callFnc = 'Emoji', 'Images', 'emoji'

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
  name, category, callFnc = 'Badge', 'Images', 'badge'
  __reqCss = ['bootstrap', 'font-awesome']

  def __init__(self, report, text, label, icon, background_color, color, url, tooltip, options, profile):
    super(Badge, self).__init__(report, None, css_attrs={"color": color, 'background-color': background_color},
                                profile=profile)
    self.add_label(label, css={"vertical-align": "middle", "width": 'none', "height": 'none'})
    self.options = Options.OptionsBadge(self, options)
    if self.options.badge_position == 'left':
      self.add_icon(icon, css={"float": 'None', "font-size": Defaults_css.font(5)}, position="after")
    else:
      self.add_icon(icon, css={"float": 'left', "font-size": Defaults_css.font(5)})
    self.link = None
    if url is not None:
      self.link = self._report.ui.links.external(text, url).css({"color": "inherit", 'display': 'inline-block',
          "padding": "2px 2px 0 2px", "border-radius": "20px", "width": "auto", "height": Defaults_css.font()})
      self.link.inReport = False
    else:
      self.link = self._report.ui.text(text).css({"color": "inherit", 'display': 'inline-block',
          "padding": "2px 2px 0 2px", "border-radius": "20px", "width": "auto", "height": Defaults_css.font()})
    self.link.css(self.options.badge_css)
    self.link.inReport = False
    self.attr['class'].add("badge") # From bootstrap
    if tooltip is not None:
      self.tooltip(tooltip)

  def __str__(self):
    if self.link is not None:
      return '<span %s>%s</span>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.link)

    return '<span %s>%s</span>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.link)
