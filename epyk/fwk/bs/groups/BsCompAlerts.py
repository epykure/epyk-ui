
from typing import List
from epyk.core.py import types
from epyk.core.py import primitives


class Components:

  def __init__(self, ui):
    self.page = ui.page

  def alert(self, kind: str = None, components: List[primitives.HtmlModel] = None, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
            profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Add alert to the page.

    Usage::

      page.web.bs.alerts.primary("This is an alert", options={"close": True})

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param kind: Optional. The Bootstrap predefined category.
    :param components: Optional. The alert sub components.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    content = self.page.web.std.div(
      components, width=width, height=height, html_code=html_code, options=options, profile=profile)
    content.attr["class"].initialise(["alert"])
    if kind is not None:
      content.attr["class"].add("alert-%s" % kind)
    content.attr["role"] = "alert"
    if options is not None and options.get("close"):
      btn = self.page.web.std.button()
      btn.attr["class"].initialise(["btn-close"])
      btn.attr["data-bs-dismiss"] = "alert"
      btn.attr["aria-label"] = "Close"
      btn.attr["type"] = "button"
      btn.options.managed = False
      content.val.append(btn)
    return content

  def primary(self, components: List[primitives.HtmlModel] = None, width: types.SIZE_TYPE = (100, '%'),
              height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
              options: dict = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Add alert to the page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Optional. The alert sub components.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    content = self.alert("primary", components, width, height, html_code, options, profile)
    return content

  def secondary(self, components: List[primitives.HtmlModel] = None, width: types.SIZE_TYPE = (100, '%'),
                height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
                options: dict = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Add alert to the page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Optional. The alert sub-components.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    content = self.alert("secondary", components, width, height, html_code, options, profile)
    return content

  def success(self, components: List[primitives.HtmlModel] = None, width: types.SIZE_TYPE = (100, '%'),
              height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
              options: dict = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Add alert to the page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Optional. The alert sub-components.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    content = self.alert("secondary", components, width, height, html_code, options, profile)
    return content

  def danger(self, components: List[primitives.HtmlModel] = None, width: types.SIZE_TYPE = (100, '%'),
             height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
             profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Add alert to the page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Optional. The alert sub-components.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    content = self.alert("danger", components, width, height, html_code, options, profile)
    return content

  def warning(self, components: List[primitives.HtmlModel] = None, width: types.SIZE_TYPE = (100, '%'),
              height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
              profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Add alert to the page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Optional. The alert sub components.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    content = self.alert("warning", components, width, height, html_code, options, profile)
    return content

  def info(self, components: List[primitives.HtmlModel] = None, width: types.SIZE_TYPE = (100, '%'),
           height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
           profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Add alert to the page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Optional. The alert sub-components.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height:  Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options:  Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    content = self.alert("info", components, width, height, html_code, options, profile)
    return content

  def light(self, components: List[primitives.HtmlModel] = None, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
            profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Add alert to the page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Optional. The alert sub-components.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    content = self.alert("light", components, width, height, html_code, options, profile)
    return content

  def dark(self, components: List[primitives.HtmlModel] = None, width: types.SIZE_TYPE = (100, '%'),
           height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
           profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Add alert to the page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Optional. The alert sub-components.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    content = self.alert("dark", components, width, height, html_code, options, profile)
    return content

