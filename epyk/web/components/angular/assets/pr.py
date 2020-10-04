
from epyk.web.components.angular.assets import asset


class AssetNgB(asset.Asset):
  pass


class AutoComplete(AssetNgB):
  name = 'p-autocomplete'
  imports = {"primeng/calendar": ["AutoCompleteModule"]}

  def __str__(self):
    return '''
<p-autoComplete [(ngModel)]="text" [suggestions]="results" (completeMethod)="search($event)"></p-autoComplete>
'''


class Calendar(AssetNgB):
  name = 'p-calendar'
  imports = {"primeng/autocomplete": ["CalendarModule"]}

  def __str__(self):
    return '''
<p-calendar [(ngModel)]="value"></p-calendar>
'''


class Checkbox(AssetNgB):
  name = 'p-calendar'
  imports = {"primeng/checkbox": ["CheckboxModule"]}

  def __str__(self):
    return '''
<p-checkbox name="groupname" value="val1" [(ngModel)]="selectedValues"></p-checkbox>
'''


class Chip(AssetNgB):
  name = 'p-calendar'
  imports = {"primeng/chips": ["ChipsModule"]}

  def __str__(self):
    return '''
<p-chips [(ngModel)]="values"></p-chips>
'''


class Dropdown(AssetNgB):
  name = 'p-calendar'
  imports = {"primeng/dropdown": ["DropdownModule"], 'primeng/api': ['SelectItem']}

  def __str__(self):
    return '''
<p-dropdown [options]="cities1" [(ngModel)]="selectedCity1"></p-dropdown>
'''


class Switch(AssetNgB):
  name = 'p-switch'
  imports = {"primeng/inputswitch": ["InputSwitchModule"]}

  def __str__(self):
    return '''
<p-inputSwitch [(ngModel)]="checked1"></p-inputSwitch>
'''


class Input(AssetNgB):
  name = 'p-input'
  imports = {"primeng/inputtext": ["InputTextModule"]}

  def __str__(self):
    return '''
<input type="text" pInputText />
'''


class Rating(AssetNgB):
  name = 'p-rating'
  imports = {"primeng/rating": ["RatingModule"]}

  def __str__(self):
    return '''
<p-rating [(ngModel)]="val"></p-rating>
'''


class Slider(AssetNgB):
  name = 'p-rating'
  imports = {"primeng/slider": ["SliderModule"]}

  def __str__(self):
    return '''
<p-slider [(ngModel)]="val"></p-slider>
'''


class Button(AssetNgB):
  name = 'p-rating'
  imports = {"primeng/button": ["ButtonModule"]}

  def __str__(self):
    return '''
<p-button label="Click"></p-button>
'''


class Listbox(AssetNgB):
  name = 'p-listbox'
  imports = {"primeng/listbox": ["ListboxModule"]}

  def __str__(self):
    return '''
<p-listbox [options]="cities1" [(ngModel)]="selectedCity1"></p-listbox>
'''


class MultiSelect(AssetNgB):
  name = 'p-rating'
  imports = {"primeng/multiselect": ["MultiSelectModule"]}

  def __str__(self):
    return '''
<p-multiSelect [options]="cities1" [(ngModel)]="selectedCities1"></p-multiSelect>
'''


class TriStateCheckbox(AssetNgB):
  name = 'p-triStateCheckbox'
  imports = {"primeng/tristatecheckbox": ["TriStateCheckboxModule"]}

  def __str__(self):
    return '''
<p-triStateCheckbox [(ngModel)]="value" label="Item Label"></p-triStateCheckbox>
'''


class ToggleButton(AssetNgB):
  name = 'p-toggleButton'
  imports = {"primeng/togglebutton": ["ToggleButtonModule"]}

  def __str__(self):
    return '''
<p-toggleButton [(ngModel)]="checked"></p-toggleButton>
'''
