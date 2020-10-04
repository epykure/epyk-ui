
from epyk.core.html import Html


class Asset(Html.Html):

  imports = None

  def __init__(self, report, vals, htmlCode=None, options=None, profile=None, css_attrs=None):
    super(Asset, self).__init__(report, vals, htmlCode, options, profile, css_attrs)
    #
    if self.imports is not None:
      for path, classNames in self.imports.items():
        if not path in report._props['web']['modules']:
          report._props['web']['modules'][path] = set()
        for className in classNames:
          report._props['web']['modules'][path].add(className)

