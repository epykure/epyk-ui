
from epyk.interfaces import Arguments
from epyk.fwk.bs.html import HtmlBsWidgets


class Components:

  def __init__(self, ui):
    self.page = ui.page

  def img(self, image=None, path=None, thumbnail=False, width=(100, "%"), height=(None, "px"), align="center",
          html_code=None, profile=None, tooltip=None, options=None):
    """
    Description:
    -----------
    Add image component to the page.

    Usage::

      e = page.web.bs.images.img("https://www.citationbonheur.fr/wp-content/uploads/2018/09/L_influence_du_paysage_sur_le_bonheur.jpg")

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/images/

    Attributes:
    ----------
    :param image: String. Optional. The image file name.
    :param path: String. Optional. Optional. TString. The image file path.
    :param thumbnail: Boolean. Optional. you can set thumbnail to give an image a rounded 1px border appearance.
    :param width: Tuple. Optional. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Optional. Tuple. The component height in pixel or percentage.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    component = self.page.web.std.img(image, path, width, height, align, html_code, profile, tooltip, options)
    component.attr["class"].initialise(["img-fluid"])
    if thumbnail:
      component.attr["class"].add("img-thumbnail")
    return component

  def badge(self, text="", category="primary", width=(None, "px"), height=(None, "px"), tooltip=None, options=None,
            profile=None):
    """
    Description:
    -----------
    Documentation and examples for badges, our small count and labeling component.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/badge/

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param category: String. Optional. The Bootstrap predefined category.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.web.std.tags.span(
      text, width=width, height=height, tooltip=tooltip, options=options, profile=profile)
    component.attr["class"].initialise(["badge"])
    component.style.css.margin = 2
    if category is not None:
      component.attr["class"].add("bg-%s" % category)
    return component

  def pill(self, text="", category="primary", icon=None, width=(None, "px"), height=(None, "px"), tooltip=None,
           options=None, profile=None):
    """
    Description:
    -----------
    Documentation and examples for badges, our small count and labeling component.

    Usage::

      b1 = page.web.bs.images.pill(category="secondary", icon="bi-x-square-fill")

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/badge/

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param category: String. Optional. The Bootstrap predefined category.
    :param icon: String. Optional. A string with the value of the icon to display from Bootstrap.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    values = []
    if icon is not None:
      values.append(self.page.web.bs.icon(icon))
    if text:
      values.append(text)
    component = self.page.web.std.tags.span(
      values, width=width, height=height, tooltip=tooltip, options=options, profile=profile)
    component.attr["class"].initialise(["badge", "rounded-pill"])
    component.style.css.margin = 2
    if category is not None:
      component.attr["class"].add("bg-%s" % category)
    return component

  def carousel(self, images=None, active=None, width=(100, "%"), height=(300, "px"), html_code=None, options=None,
               profile=None):
    """
    Description:
    -----------
    Add carousel component.

    TODO: Fix component and add js events.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/carousel/

    Usages::

      page.web.bs.images.carousel([
      r"/static/template_3.PNG",
      "/static/v1.6.PNG"])

    Attributes:
    ----------
    :param images: List<String>. Optional. The image paths.
    :param active: Boolean. optional.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsCarousel(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    component.attr["data-bs-ride"] = "carousel"
    if images is not None:
      for image in images:
        component.add_item(image, active=active)
    return component
