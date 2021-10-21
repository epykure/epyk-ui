
from epyk.fwk.ftw import PkgImports
from epyk.core.css import Defaults as Defaults_css
from epyk.fwk.ftw import groups
from epyk.interfaces import Arguments
from epyk.fwk.ftw.html import HtmlFtwForms


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.FLUENTUI)
    self.page.imports.reload()
    Defaults_css.ICON_FAMILY = 'office-ui-fabric-core'   # Set the default family for icons to rely on Fluent UI
    Defaults_css.ICON_MAPPINGS[Defaults_css.ICON_FAMILY] = PkgImports.ICON_MAPPINGS

    self.page.jsImports.add("fabric-ui")
    self.page.cssImport.add("fabric-ui/components")

    self.select = self.lists.select
    self.button = self.buttons.button
    self.toggle = self.buttons.toggle
    self.check = self.buttons.check
    self.icon = self.page.ui.images.icon

  def label(self, text=None, width=(100, "px"), height=(None, "px"), html_code=None, tooltip='', options=None,
            profile=None):
    """
    Description:
    -----------
    Labels give a name or title to a component or group of components.
    Labels should be in close proximity to the component or group they are paired with.

    Related Pages:

      https://developer.microsoft.com/en-us/fabric-js/components/label/label

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param html_code:
    :param tooltip:
    :param options:
    :param profile:
    """
    component = self.page.web.std.tags.label(text, width, height, html_code, tooltip, options, profile)
    component.add_style(["ms-Label"], clear_first=True)
    if options is not None and options.get("disabled"):
      component.attr["class"].add("is-disabled")
    if options is not None and options.get("required"):
      component.attr["class"].add("is-required")
    return component

  def link(self, text="", url="", icon=None, align="left", tooltip=None, helper=None, height=(None, 'px'),
           decoration=False, html_code=None, options=None, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://developer.microsoft.com/en-us/fabric-js/components/link/link

    Attributes:
    ----------
    :param text:
    :param url:
    :param icon:
    :param align:
    :param tooltip:
    :param helper:
    :param height:
    :param decoration:
    :param html_code:
    :param options:
    :param profile:
    """
    component = self.page.web.std.link(
      text, url, icon, align, tooltip, helper, height, decoration, html_code, options, profile)
    component.add_style(["ms-Link"], clear_first=True)
    return component

  def loading(self, text="Loading...", width=(None, "%"), height=(None, "%"), options=None,
              profile=None):
    """
    Description:
    -----------
    A Spinner is an outline of a circle which animates around itself indicating to the user that things are processing.
    A Spinner is shown when it's unsure how long a task will take making it the indeterminate version of a
    ProgressIndicator.

    Related Pages:

      https://developer.microsoft.com/en-us/fabric-js/components/spinner/spinner

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlFtwForms.Spinner(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    if options is not None and options.get("large"):
      html_but.attr["class"].add("ms-Spinner--large")
    return html_but

  @property
  def buttons(self):
    """
    Description:
    ------------

    Related Pages:

      https://developer.microsoft.com/en-us/fabric-js/components/checkbox/checkbox
    """
    return groups.FtwCompBtns.Components(self)

  @property
  def lists(self):
    """
    Description:
    ------------
    Customize the native <select>s with custom CSS that changes the element’s initial appearance.

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/select/
      https://getbootstrap.com/docs/5.1/components/list-group/
    """
    return groups.FtwCompLists.Components(self)
