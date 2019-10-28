"""
Wrapper to the HTML Image components
"""

import re

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpClsImage


class Image(Html.Html):
  name, category, callFnc = 'Picture', 'Image', 'img'
  _grpCls = CssGrpClsImage.CssClassImage

  def __init__(self, report, image, path, align, htmlCode, width, height, serverSettings, profile):
    if path is None:
      path = "/img" if report.run.report_name is None else "/img/%s" % report.run.report_name
    super(Image, self).__init__(report, {'path': path, 'image': image}, code=htmlCode, width=width[0], widthUnit=width[1],
                                height=height[0], heightUnit=height[1], profile=profile)
    self.css({'margin': '5px 5px 5px 0', 'display': 'block'})
    self._jsStyles = {}
    if align is not None:
      self.css({"text-align": align})

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' htmlObj.empty();
      var img = $("<img src=\'" + data.path + "/" + data.image + "\' />").css(jsStyles);
      htmlObj.append(img)''', 'Javascript Object builder')

  @property
  def val(self): return '$("#%s img").prop("src")' % self.htmlId

  def cssImg(self, css):
    self._jsStyles.update(css)
    return self

  def __str__(self):
    return '<div %s></div>%s' % (self.strAttr(pyClassNames=self.defined), self.helper)

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
  _grpCls = CssGrpClsImage.CssClassImageAnimated

  def __init__(self, report, image, text, title, url, path, width, height, serverSettings, profile):
    if path is None:
      path = "/img"
    super(AnimatedImage, self).__init__(report, {'path': path, 'image': image, 'text': text, "title": title, 'url': url},
                                        width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    self.width = width[0]

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, ''' 
      htmlObj.find('img').attr('src', data.path + "/" + data.image);
      htmlObj.find('div').find('h2').html(data.title); htmlObj.find('div').find('p').html(data.text); 
      if (data.url != null){htmlObj.find('a').attr('href', data.url)}''')

  def __str__(self):
    return '''
      <div %s>
        <img />
        <div class="mask"><h2></h2><p></p><a class="info" style="cursor:pointer">Enter</a></div>
      </div>''' % self.strAttr(pyClassNames=self.defined)


class ImgCarrousel(Html.Html):
  name, category, callFnc = 'Picture Carrousel', 'Images', 'carrousel'
  _grpCls = CssGrpClsImage.CssClassImageCarrousel

  def __init__(self, report, images, path, width, height, serverSettings, profile):
    if path is None:
      path = "/img"
    for rec in images:
      if not 'path' in rec:
        rec['path'] = path
    super(ImgCarrousel, self).__init__(report, images, width=width[0], widthUnit=width[1], height=height[0],
                                       heightUnit=height[1], profile=profile)
    self.css({'padding-top': '20px', 'display': 'block', 'padding': 0, 'margin': 0})

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, '''
      var i = 0; var htmlId = htmlObj.attr('id');
      data.forEach(function(rec){
        if (i == 0) {
          htmlObj.append('<li style="display:inline-block" id="'+ htmlId +'_picture_'+ i +'"><img src="'+ rec.path +'/'+ rec.image +'" /><h2>'+ rec.title +'</h2></li>');
          $('#'+ htmlId +'_bullets').append("<label style='background:%(color)s' for='"+ i +"' name='img-selector'></label>")
        } else {  
          htmlObj.append('<li style="display:none" id="'+ htmlId +'_picture_'+ i +'"><img src="'+ rec.path +'/'+ rec.image +'" /><h2>'+ rec.title +'</h2></li>');
          $('#'+ htmlId +'_bullets').append("<label for='"+ i +"' name='img-selector'></label>")}
      i = i + 1})''' % {'color': self.getColor('colors', 9)}, 'Javascript Object builder')

  def __str__(self):
    self._report.jsOnLoadFnc.add('''
      $("label[for][name=img-selector]").click(function(){
        for (var i=0; i < %(count)s; i++) {$('#%(htmlId)s_picture_'+ i ).css('display', 'none')}
        $("label[for][name=img-selector").css('background', '%(grey)s');
        $('#%(htmlId)s_picture_'+ parseInt($(this).attr('for'))).css('display', 'inline-block'); 
        $("label[for='"+ $(this).attr('for') +"'][name=img-selector").css('background', '%(color)s')})
    ''' % {'htmlId': self.htmlId, 'count': len(self.vals), 'color': self.getColor('colors', 9), 'grey': self.getColor('greys', 2)})
    return '''
      <ul %(strAttr)s></ul>
      <div id="%(htmlId)s_bullets" %(clsTag)s></div>
      ''' % {'strAttr': self.strAttr(pyClassNames=self.defined),
             'htmlId': self.htmlId, 'clsTag': self._report.style.getClsTag(self.defined.clsAltMap)}


class Icon(Html.Html):
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  name, category, callFnc = 'Icon', 'Images', 'icon'

  def __init__(self, report, value, size, width, height, tooltip, profile):
    super(Icon, self).__init__(report, value, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                               profile=profile)
    self.css({'vertical-align': 'middle', "display": 'inline-block', "margin": "auto 0", "padding": "auto 0",
              "font-size": "%s%s" % (size[0], size[1]) if size is not None else 'inherit'})
    self.attr['class'].add(value)
    if tooltip is not None:
      self.addAttr("title", tooltip)

  @property
  def val(self):
    return self.dom.getAttribute("class")

  @property
  def jsQueryData(self):
    return "{event_val: $(this).attr('class'), event_code: '%s'}" % self.htmlId

  def click(self, jsFncs):
    self.css({"cursor": 'pointer'})
    return super(Icon, self).click(jsFncs)

  def jsToggleIcon(self, icon):
    return '''
      if (%(jqId)s.hasClass('%(icon)s')){%(jqId)s.removeClass('%(icon)s').addClass('%(newIcon)s')}
      else {%(jqId)s.removeClass('%(newIcon)s').addClass('%(icon)s')} ''' % {'jqId': self.jqId, 'newIcon': icon, 'icon': self.vals}

  def onDocumentReady(self):
    self._report.jsOnLoadFnc.add("%(jsId)s.attr('class', ''); %(jsId)s.addClass('%(icon)s')" % {'jsId': self.jqId, 'icon': self.vals})

  def onDocumentLoadFnc(self): return True

  def __str__(self):
    return '<i aria-hidden="true" %s></i>' % (self.strAttr(pyClassNames=self.pyStyle))


"""
    if self.stack is not None:
      # report.icon("fas fa-file").stack = {"icon": "fab fa-python", "class": "fa-stack-1x fa-inverse"}
      # https://fontawesome.com/how-to-use/on-the-web/styling/stacking-icons
      return '''
        <span class="fa-stack fa-2x">
          <i class="%(icon)s fa-stack-%(sizeIcon)sx"></i>
          <i class="%(icon2)s %(clss2)s"></i>
        </span>
        ''' % {"strAttr": self.strAttr(pyClassNames=self.pyStyle), 'icon': self.vals, "sizeIcon": self.vals,
               "icon2": self.stack['icon'], 'clss2': self.stack.get('class', '') }
"""


class Emoji(Html.Html):
  name, category, callFnc = 'Emoji', 'Image', 'emoji'
  mocks = 'heart_eyes'

  def __init__(self, report, icon_name, top, profile):
    super(Emoji, self).__init__(report, icon_name, profile=profile)
    self.vals.lower().replace('.png', '')
    self.css({'margin-top': '%s%s' % (top[0], top[1])})

  def __str__(self):
    return '<img src="/static/images/emojis/%s.png" style="width:25px;height:auto"/>' % self.vals


class Badge(Html.Html):
  name, category, callFnc = 'Badge', 'Image', 'badge'
  __reqCss = ['bootstrap', 'font-awesome']

  def __init__(self, report, text, label, icon, size, background_color, color, tooltip, profile):
    super(Badge, self).__init__(report, text, profile=profile)
    # Add the components label and icon
    self.prepend_child(report.ui.texts.label(label, color="inherit", width=(None, "px"), height=(None, "px")).css({"float": None})) if label is not None else ""
    self.prepend_child(report.ui.images.icon(icon)) if icon is not None else ""
    # Update the CSS Style of the component
    color = 'inherit' if color is None else color
    background_color = self.getColor("success", 1) if background_color is None else background_color
    self.css({'background-color': background_color, 'color': color, 'padding': "1px 3px", 'margin': '0px 2px',
              'font-size': "%s%s" % (size[0], size[1]) if size is not None else 'inherit'})
    self.attr['class'].add("badge") # From bootstrap
    if tooltip is not None:
      self.tooltip(tooltip)

  @property
  def container(self):
    return self.dom

  def __str__(self):
    return '<span %s>%s</span>' % (self.strAttr(), self.vals)
