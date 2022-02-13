
from typing import Union
from epyk.core.py import primitives
from epyk.core.html import Html


class Asset(Html.Html):

  imports = None

  def __init__(self, page: primitives.PageModel, vals, html_code: str = None, options: dict = None,
               profile: Union[dict, bool] = None, css_attrs: dict = None):
    super(Asset, self).__init__(page, vals, html_code, options, profile, css_attrs)
    #
    if self.imports is not None:
      for path, class_names in self.imports.items():
        if path not in page._props['web']['modules']:
          page._props['web']['modules'][path] = set()
        for class_name in class_names:
          page._props['web']['modules'][path].add(class_name)

