
import os
from epyk.core.html import Html
from typing import Union
from epyk.core.py import primitives, types
from epyk.customs.data.html import HtmlDashboard
from epyk.customs.data.html import HtmlProgress
from epyk.core.html import Defaults
from epyk.interfaces import Arguments


class Components:

  def __init__(self, ui):
    self.page = ui.page

  def pivots(self, rows: Union[list, primitives.HtmlModel] = None, columns: Union[list, primitives.HtmlModel] = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = ('auto', ""), html_code: str = None,
             options: Union[dict, bool] = None,
             profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param columns: Optional. The list of key from the record to be used as columns in the table.
    :param rows: Optional. The list of key from the record to be used as rows in the table.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    options = options or {}
    dflt_options = {"sub_chart": False, "max": {"rows": 1}, "columns": "", 'rows': ""}
    if options is not None:
      dflt_options.update(options)
    component = HtmlDashboard.Pivots(self.page, width, height, html_code, options, profile)
    if rows is None or not hasattr(rows, "options"):
      row_options = dict(dflt_options)
      row_options["max"] = dflt_options.get("max", {}).get("rows")
      row_options["delete"] = dflt_options.get("delete_rows", True)
      component.rows = self.page.ui.lists.drop(html_code="%s_rows" % component.htmlCode, options=row_options)
      if row_options["max"] == 1:
        component.rows.style.css.min_height = 20
      component.rows.style.css.margin_top = 0
      if rows is not None:
        component.rows.add_items(rows)
    else:
      component.rows = rows

    if dflt_options.get("sub_chart"):
      component.sub_rows = self.page.ui.lists.drop(
        html_code="%s_sub_rows" % component.htmlCode, options={"max": 1})
      component.sub_rows.style.css.min_height = 20
      component.sub_rows.style.css.margin_top = 0
      component.sub_rows.options.managed = False
    else:
      component.sub_rows = None
    component.rows.options.managed = False
    if columns is None or not hasattr(columns, "options"):
      columns_options = dict(dflt_options)
      columns_options["max"] = dflt_options.get("max", {}).get("columns")
      columns_options["delete"] = dflt_options.get("delete_columns", True)
      component.columns = self.page.ui.lists.drop(
        html_code="%s_columns" % component.htmlCode, options=columns_options)
      component.columns.style.css.margin_top = 0
      if columns is not None:
        component.rows.add_items(columns)
    else:
      component.columns = columns
    component.columns.options.managed = False
    component.style.css.margin_top = 5
    component.style.css.margin_bottom = 5
    return component

  def filters(self, items=None, button=None, width: types.SIZE_TYPE = ("auto", ""),
              height: types.SIZE_TYPE = (60, "px"), html_code: str = None, helper: str = None,
              options: Union[dict, bool] = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param items:
    :param button:
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional. The value to be displayed to the helper icon.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    options = options or {}
    container = self.page.ui.div(width=width)
    if options.get("select", 'select') == 'input':
      container.select = self.page.ui.inputs.autocomplete(
        html_code="%s_select" % html_code if html_code is not None else html_code,
        width=(Defaults.TEXTS_SPAN_WIDTH, 'px'))
      container.select.style.css.text_align = "left"
      container.select.style.css.padding_left = 5
      container.select.options.liveSearch = True
    else:
      container.select = self.page.ui.select(
        html_code="%s_select" % html_code if html_code is not None else html_code)
      container.select.attr['data-width'] = '%spx' % options.get('width', Defaults.TEXTS_SPAN_WIDTH)
      container.select.options.liveSearch = True
    if options.get("autocomplete"):
      container.input = self.page.ui.inputs.autocomplete(
        html_code="%s_input" % html_code if html_code is not None else html_code,
        width=(Defaults.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
    else:
      container.input = self.page.ui.input(
        html_code="%s_input" % html_code if html_code is not None else html_code,
        width=(Defaults.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
    container.input.style.css.text_align = 'left'
    container.input.style.css.padding_left = 5
    container.input.style.css.margin_left = 10
    if button is None:
      button = self.page.ui.buttons.colored("add")
      button.style.css.margin_left = 10
    container.button = button
    container.clear = self.page.ui.icon("fas fa-times")
    container.clear.style.css.color = self.page.theme.danger.base
    container.clear.style.css.margin_left = 20
    container.clear.tooltip("Clear all filters")
    container.add(self.page.ui.div([container.select, container.input, container.button, container.clear]))
    container.filters = self.page.ui.panels.filters(
      items, container.select.dom.content, (100, '%'), height, html_code, helper, options, profile)
    container.add(container.filters)
    container.clear.click([
      container.filters.dom.clear()
    ])
    container.button.click([
      container.filters.dom.add(container.input.dom.content, container.select.dom.content)
    ])
    container.input.enter(container.button.dom.events.trigger("click"))
    return container


class ProgressComponents:

  def __init__(self, ui):
    self.page = ui.page

  def gauge(self, value: float, width: types.SIZE_TYPE = (90, 'px'), height: types.SIZE_TYPE = (45, "px"),
            html_code: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    Related Pages:

      https://codepen.io/jagathish/pen/ZXzbzN

    Attributes:
    ----------
    :param value:
    :param width:
    :param height:
    :param html_code:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    return HtmlProgress.Gauge(
      value, page=self.page, width=width, height=height, html_code=html_code, options=options, profile=profile)

  def circle(self, value: float, width: types.SIZE_TYPE = (90, 'px'), height: types.SIZE_TYPE = (90, "px"),
             html_code: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    return HtmlProgress.Circle(
      value, page=self.page, width=width, height=height, html_code=html_code, options=options, profile=profile)


class Gallery:

  def __init__(self, ui):
    self.page = ui.page

  def mosaic(self, pictures: list = None, columns: int = 6, path: str = None, width: types.SIZE_TYPE = (None, '%'),
             height: types.SIZE_TYPE = ('auto', ''), options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Mosaic of pictures.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param pictures: Optional. The list with the pictures.
    :param columns: Optional. The number of column for the mosaic component.
    :param path: Optional. The path for the picture.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    dflt_options = {"extensions": ['jpg']}
    if options is not None:
      dflt_options.update(options)
    grid = self.page.ui.grid(width=width, height=height, options=dflt_options, profile=profile)
    grid.style.css.margin_top = 20
    grid.style.css.overflow = 'hidden'
    grid.style.css.margin_bottom = 20
    row = self.page.ui.row(options=dflt_options)
    grid.pictures = []
    if path is not None and pictures is None:
      pictures = []
      for img in os.listdir(path):
        ext_img = img.split(".")[-1]
        if ext_img.lower() in dflt_options["extensions"]:
          pictures.append(img)
      if 'static' in dflt_options:
        path = dflt_options['static']
    pictures = pictures or []
    for i, picture in enumerate(pictures):
      if dflt_options.get("max") is not None and len(grid.pictures) > dflt_options.get("max"):
        break

      if i % columns == 0:
        grid.add(row)
        row = self.page.ui.row(options=dflt_options)
      if not hasattr(picture, 'options'):
        picture = self.page.ui.img(
          self.page.py.encode_html(picture), path=self.page.py.encode_html(path),
          html_code="%s_%s" % (grid.htmlCode, i))
        picture.attr["data-next"] = "%s_%s" % (grid.htmlCode, min(i + 1, len(pictures) - 1))
        picture.attr["data-previous"] = "%s_%s" % (grid.htmlCode, max(i - 1, 0))
        picture.style.css.max_height = 200
        picture.style.css.margin = 5
        grid.pictures.append(picture)
        if dflt_options.get('zoom', True):
          picture.style.effects.zoom()
      row.add(picture)
      picture.parent = row[-1]
    if dflt_options.get('focus', True):
      grid.image = self.page.studio.blog.picture("", path=path, align="center")
      grid.image.style.css.width = "calc(90% - 20px)"
      grid.image.style.css.max_height = 450
      grid.image.style.css.border_radius = 20
      grid.image.style.css.position = "absolute"
      grid.image.style.css.margin = "auto"
      grid.image.style.css.top = 0
      grid.image.style.css.bottom = 0
      grid.image.style.css.left = 0
      grid.image.style.css.right = 0
      if dflt_options.get('arrows', True):
        grid.next = self.page.ui.icon(dflt_options.get("arrows-right", "fas fa-chevron-right")).css(
          {"position": 'absolute', 'background': 'white', 'cursor': 'pointer', 'z-index': '1010',
           "font-size": '35px', "padding": '8px', "right": '10px', 'top': '50%'})
        grid.next.options.managed = False
        grid.previous = self.page.ui.icon(dflt_options.get("arrows-left", "fas fa-chevron-left")).css(
          {"position": 'absolute', 'background': 'white', 'cursor': 'pointer',  'z-index': '1010',
           "font-size": '35px', "padding": '8px', "left": '10px', 'top': '50%'})
        grid.previous.options.managed = False
        grid.next.click([
          grid.image.build(
            self.page.js.getElementById(grid.next.dom.getAttribute("value")).getAttribute("src")),
          grid.previous.dom.setAttribute("value", self.page.js.getElementById(
            grid.next.dom.getAttribute("value")).getAttribute("data-previous")),
          grid.next.dom.setAttribute("value", self.page.js.getElementById(
            grid.next.dom.getAttribute("value")).getAttribute("data-next"))
        ])

        grid.previous.click([
          grid.image.build(
            self.page.js.getElementById(grid.previous.dom.getAttribute("value")).getAttribute("src")),
          grid.next.dom.setAttribute("value", self.page.js.getElementById(
            grid.previous.dom.getAttribute("value")).getAttribute("data-next")),
          grid.previous.dom.setAttribute("value", self.page.js.getElementById(
            grid.previous.dom.getAttribute("value")).getAttribute("data-previous"))
        ])
        grid.popup = self.page.ui.layouts.popup([grid.previous, grid.image, grid.next])
      else:
        grid.popup = self.page.ui.layouts.popup([grid.image])

      if dflt_options.get("keyboard", True) and dflt_options.get('arrows', True):
        self.page.body.keyup.left([grid.previous.dom.events.trigger("click")])
        self.page.body.keyup.right([grid.next.dom.events.trigger("click")])

      grid.popup.options.top = 0
      for i, r in enumerate(grid.pictures):
        r.click([
          grid.next.dom.setAttribute("value", r.dom.getAttribute("data-next")),
          grid.previous.dom.setAttribute("value", r.dom.getAttribute("data-previous")),
          grid.image.build(r.dom.content),
          grid.popup.dom.show()])
    if len(row):
      for c in row:
        c.set_size(12 // columns)
      grid.add(row)
    return grid

  def carousel(self, images: list = None, path: str = None, selected: int = 0, width: types.SIZE_TYPE = (100, "%"),
               height: types.SIZE_TYPE = (300, "px"), options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param images: Optional. The list with the pictures.
    :param path: Optional. The path for the picture.
    :param selected: Optional. The selected index.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    dfl_options = {"extensions": ['jpg']}
    if options is not None:
      dfl_options.update(options)
    if path is not None and images is None:
      images = []
      for img in os.listdir(path):
        ext_img = img.split(".")[-1]
        if ext_img.lower() in dfl_options["extensions"]:
          images.append({"image": img, 'title': ''})
      if len(images) > 5:
        dfl_options.update({'points': False, "arrows": True, "keyboard": True})
    images = images or []
    c = self.page.ui.images.carousel(images, path, selected, width, height, dfl_options, profile)
    return c

  def pagination(self, count: int, selected: int = 1, width: types.SIZE_TYPE = (100, '%'),
                 height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: types.OPTION_TYPE = None,
                 profile: types.PROFILE_TYPE = False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param count: The pagination count of items.
    :param selected: Optional. The selected value.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    p = self.page.ui.navigation.indices(
      count, selected=selected, width=width, height=height, options=options, html_code=html_code, profile=profile)
    p.style.css.text_align = "center"
    return p

  def heroes(self, url: str, path: str = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (500, "px"), align: str = "center", html_code: str = None,
             options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Related Pages:

      https://www.w3schools.com/cssref/pr_background-image.asp

    Attributes:
    ----------
    :param url: Optional. The picture url.
    :param path: Optional. The picture path.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align: Optional. The text-align property within this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    options = options or {}
    img = self.page.ui.div(
      width=width, height=height, align=align, html_code=html_code, options=options, profile=profile)
    if path is not None:
      img.style.css.background_image = "url(%s/%s)" % (path.replace("\\", "/"), url)
    else:
      img.style.css.background_image = "url(%s)" % url
    img.style.css.background_position = "center center"
    img.style.css.background_repeat = "no-repeat"
    img.style.css.background_size = "cover"
    if options.get("fixed", True):
      img.style.css.background_attachment = "fixed"
    img.style.css.position = "relative"
    return img

  def fixed(self, url: str, path: str = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (300, "px"), align: str = "center", html_code: str = None,
            options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param url: Optional. The url link.
    :param path: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align: Optional. The text-align property within this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    options = options or {}
    img = self.page.ui.div(
      width=width, height=height, align=align, html_code=html_code, options=options, profile=profile)
    if path is not None:
      img.style.css.background_image = "url(%s/%s)" % (path.replace("\\", "/"), url)
    else:
      img.style.css.background_image = "url(%s)" % url
    img.style.css.background_position = "center center"
    img.style.css.background_repeat = "no-repeat"
    img.style.css.background_size = "cover"
    if options.get("fixed", True):
      img.style.css.background_attachment = "fixed"
    return img

  def link(self, img: str, url: str = "#", path: str = None, width: types.SIZE_TYPE = (100, "%"),
           height: types.SIZE_TYPE = (None, "px"), align: str = "center", options: types.OPTION_TYPE = None,
           html_code: str = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Set a background as an image.
    This is wrapping the image.background base component.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Attributes:
    ----------
    :param img:
    :param url: Optional. The url link.
    :param path: Optional. The picture path.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align: Optional. The text-align property within this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    img = self.page.ui.images.img(
      img, path=path, width=width, height=height, align=align, html_code=html_code, options=options, profile=profile)
    img.style.effects.reduce()
    img.style.css.cursor = "pointer"
    img.goto(url)
    return img

  def overlay(self, img: str, text: str = None, path: str = None, width: types.SIZE_TYPE = (100, "%"),
              height: types.SIZE_TYPE = (None, "px"), align: str = "center", options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Related Pages:

      https://www.w3schools.com/howto/howto_css_image_overlay_slide.asp

    Attributes:
    ----------
    :param img:
    :param text: Optional. The content.
    :param path: Optional. The picture path.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param align: Optional. The text-align property within this component.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    options = options or {}
    container = self.page.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    container.style.css.position = "relative"
    container.style.css.box_sizing = "border-box"
    container.img = self.page.ui.images.img(
      img, path=path, width=(100, "%"), height=(None, "px"), align="center", options=options, profile=profile)
    container.img.style.css.display = "block"
    container.img.style.css.width = "100%"
    container.add(container.img)
    container.attr['class'].clear()
    container.attr['class'].add("container_overlay")
    container.overlay = self.page.ui.div(
      width=width, height=height, align=align, options=options, profile=profile)
    if text is not None:
      if hasattr(text, 'options'):
        container.text = text
      else:
        container.text = self.page.ui.div(
          text, width=(100, "%"), height=height, align=align, options=options, profile=profile)
      if options.get("direction") is None:
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_title")
        container.overlay.style.css.opacity = 0
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.bottom = 0
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(".container_overlay:hover .test_overlay_title {opacity: 1 !IMPORTANT;}")
      elif options.get("direction") == 'top':
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_top")
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.width = "100%"
        container.overlay.style.css.height = 0
        container.overlay.style.css.transition = ".5s ease"
        container.overlay.style.css.overflow = "hidden"
        container.overlay.style.css.bottom = 0
        container.overlay.style.css.right = 0
        container.overlay.style.css.left = 0
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(".container_overlay:hover .test_overlay_top {height: 100% !IMPORTANT;}")
      elif options.get("direction") == 'bottom':
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_bottom")
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.width = "100%"
        container.overlay.style.css.height = 0
        container.overlay.style.css.transition = ".5s ease"
        container.overlay.style.css.overflow = "hidden"
        container.overlay.style.css.bottom = "100%"
        container.overlay.style.css.right = 0
        container.overlay.style.css.left = 0
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(
          ".container_overlay:hover .test_overlay_bottom {height: 100% !IMPORTANT; bottom: 0 !IMPORTANT}")
      elif options.get("direction") == 'right':
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_right")
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.width = 0
        container.overlay.style.css.height = "100%"
        container.overlay.style.css.transition = ".5s ease"
        container.overlay.style.css.overflow = "hidden"
        container.overlay.style.css.bottom = 0
        container.overlay.style.css.right = 0
        container.overlay.style.css.left = "100%"
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(
          ".container_overlay:hover .test_overlay_right {width: 100% !IMPORTANT; left: 0 !IMPORTANT}")
      elif options.get("direction") == 'left':
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_left")
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.width = 0
        container.overlay.style.css.height = "100%"
        container.overlay.style.css.transition = ".5s ease"
        container.overlay.style.css.overflow = "hidden"
        container.overlay.style.css.bottom = 0
        container.overlay.style.css.right = "100%"
        container.overlay.style.css.left = 0
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(
          ".container_overlay:hover .test_overlay_left {width: 100% !IMPORTANT; right: 0 !IMPORTANT}")
      container.style.css.cursor = 'pointer'
      container.overlay.add(container.text)
    container.add(container.overlay)
    return container

  def wallpaper(self, url: str, width: types.SIZE_TYPE = (100, "%"),
                height: types.SIZE_TYPE = (300, "px"), size: str = "cover",
                margin: int = 0, align: str = "center",
                position: str = "middle", options: types.OPTION_TYPE = None,
                profile: types.PROFILE_TYPE = False):
    """
    Description:
    ------------
    Set a background as an image.
    This is wrapping the image.background base component.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param url: Optional. The url link.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param size:
    :param margin:
    :param align: Optional. The text-align property within this component.
    :param position: Optional. The position compared to the main component tag.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    background = self.page.ui.images.wallpaper(
      url, width=width, height=height, size=size, margin=margin, align=align, position=position, options=options,
      profile=profile)
    return background

  def animated(self, image: str = None, text: str = "", title: str = "", url: str = None, path: str = None,
               width: types.SIZE_TYPE = (200, "px"), height: types.SIZE_TYPE = (200, "px"),
               html_code: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param image: Optional.
    :param text: Optional. The value to be displayed to the component.
    :param title: Optional. A panel title. This will be attached to the title property.
    :param url: Optional. The url link.
    :param path: Optional. The picture path.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    a = self.page.ui.images.animated(
      image, text=text, title=title, url=url, path=path, width=width, height=height, html_code=html_code,
      options=options, profile=profile)
    return a

  def folders(self, path: str, columns: int = 6, images: dict = None, position: str = "top", width: types.SIZE_TYPE = (None, '%'),
              height: types.SIZE_TYPE = ('auto', ''), options: types.OPTION_TYPE = None,
              profile: types.OPTION_TYPE = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param path: Optional. The picture path.
    :param columns:
    :param images:
    :param position:
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    dflt_options = {"extensions": ['jpg']}
    if options is not None:
      dflt_options.update(options)
    grid = self.page.ui.grid(width=width, height=height, options=dflt_options, profile=profile)
    pictures = []
    for f in os.listdir(path):
      folder_path = os.path.join(path, f)
      if not os.path.isfile(folder_path):
        for i in os.listdir(folder_path):
          ext_img = i.split(".")[-1]
          if ext_img.lower() in dflt_options["extensions"]:
            pictures.append({"name": self.page.py.encode_html(i),
                             'path': self.page.py.encode_html(folder_path),
                             'title': self.page.py.encode_html(f)})
            if images is not None and f in images:
              pictures[-1].update(images[f])
            break
    grid.pictures = []
    row = self.page.ui.row(position=position)
    viewer = self.page.ui.img(
      pictures[0]["name"], path=pictures[0]["path"], width=(100, '%'), height=('auto', ''))
    viewer.style.css.border = "1px solid %s" % self.page.theme.greys[7]
    for i, picture in enumerate(pictures):
      if i % columns == 0:
        grid.add(row)
        row = self.page.ui.row(position=position)
      pic = self.page.ui.img(picture["name"], path=picture["path"])
      pic.style.css.cursor = "pointer"
      pic.click([
        viewer.build(pic.dom.content)
      ])
      pic.tooltip(picture["title"])
      pic.style.css.max_height = 200
      pic.style.css.margin = 5
      pic.style.css.z_index = 0
      grid.pictures.append(pic)
      row.add(pic)
      pic.parent = row[-1]

    grid.style.css.margin_top = 20
    grid.style.css.overflow = 'hidden'
    grid.style.css.margin_bottom = 20
    if len(row):
      for c in row:
        c.set_size(12 // columns)
      grid.add(row)

    if len(grid.pictures) > 4 * columns:
      grid.style.css.height = 300
      text = self.page.ui.text("See more", align="right")
      text.click([
        grid.dom.css({"height": 'auto'}),
        text.dom.css({"display": 'none'}),
      ])
      col = self.page.ui.div([grid, text])
      col.options.managed = False
      viewer.style.css.margin_top = 25
      container = self.page.ui.row([col, viewer], position="top")
    else:
      container = self.page.ui.row([grid, viewer])
    container.style.css.display = "flex"
    container.style.css.align_items = "flex-start"
    container.options.autoSize = False
    container[1].style.css.top = 30
    container[1].style.css.position = 'sticky'
    container[0].attr['class'].add("col-8")
    container[1].attr['class'].add("col-4")
    return container

  def list(self, path: str, urls: dict = None, width: types.SIZE_TYPE = ('auto', ''),
           height: types.SIZE_TYPE = ('auto', ''), options: types.OPTION_TYPE = None,
           profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param path: Optional. The picture path.
    :param urls: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    rows = []
    for f in os.listdir(path):
      folder_path = os.path.join(path, f)
      if not os.path.isfile(folder_path):
        div = self.page.ui.div(self.page.py.encode_html(f))
        div.style.css.padding = "5px 0 0 10px"
        div.style.add_classes.div.color_hover()
        if urls is not None and f in urls:
          url = urls[f]
        else:
          url = "%s.html" % Html.cleanData(f)
        div.click([self.page.js.navigateTo(url)])
        hr = self.page.ui.layouts.hr(background_color=self.page.theme.greys[3])
        hr.style.css.margin = "0 5px"
        hr.style.css.width = "calc(100% - 10px)"
        rows.append(self.page.ui.col([div, hr]))
    return self.page.ui.list(rows, width=width, height=height, options=options, profile=profile)
