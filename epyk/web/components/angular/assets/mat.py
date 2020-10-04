
from epyk.web.components.angular.assets import asset


class AssetMtb(asset.Asset):
  pass


class AutoComplete(AssetMtb):
  name = 'mat-autocomplete'
  imports = {"@angular/material/autocomplete": ["MatAutocompleteModule"]}

  def __str__(self):
    return '''
<mat-autocomplete #auto="matAutocomplete">
'''
