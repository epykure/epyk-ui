
from epyk.core.html.HtmlSelect import Option
from epyk.core.html.Html import Component
from epyk.core.data.DataPy import SelectionBox
from epyk.fwk.mdc.dom import DomMdcSnackbar


class Text(Component):
  css_classes = ["mdc-text-field", "mdc-text-field--filled"]
  name = "Material Design Text"
  str_repr = '''
<label {attrs}>
  <span class="mdc-text-field__ripple"></span>
  <span class="mdc-floating-label" {attrs}>{text}</span>
  <input class="mdc-text-field__input" type="text" aria-labelledby="my-label-id">
  <span class="mdc-line-ripple"></span>
</label>
'''

  _js__builder__ = "window[htmlObj.id] = new mdc.textField.MDCTextField(htmlObj)"


class Button(Component):
  css_classes = ["mdc-button"]
  name = "Material Design Button"
  str_repr = '''
<button {attrs}>
   <span class="mdc-button__ripple"></span>
   <span class="mdc-button__label">Text Button</span>
</button>
'''
  _js__builder__ = "console.log(mdc)"


class Check(Component):
  css_classes = ["mdc-checkbox"]
  name = "Material Design Checkbox"
  str_repr = '''
<div {attrs}>
    <input type="checkbox" class="mdc-checkbox__native-control" id="checkbox-1"/>
    <div class="mdc-checkbox__background">
      <svg class="mdc-checkbox__checkmark" viewBox="0 0 24 24">
        <path class="mdc-checkbox__checkmark-path" fill="none" d="M1.73,12.91 8.1,19.28 22.79,4.59"/>
      </svg>
      <div class="mdc-checkbox__mixedmark"></div>
    </div>
    <div class="mdc-checkbox__ripple"></div>
  </div>
'''
  _js__builder__ = "window[htmlObj.id] = new mdc.checkbox.MDCCheckbox(htmlObj)"


class Toggle(Component):
  css_classes = ["mdc-switch"]
  name = "Material Design Toggle"
  str_repr = '''
<button {attrs}>
  <div class="mdc-switch__track"></div>
  <div class="mdc-switch__handle-track">
    <div class="mdc-switch__handle">
      <div class="mdc-switch__shadow">
        <div class="mdc-elevation-overlay"></div>
      </div>
      <div class="mdc-switch__ripple"></div>
      <div class="mdc-switch__icons">
        <svg class="mdc-switch__icon mdc-switch__icon--on" viewBox="0 0 24 24">
          <path d="M19.69,5.23L8.96,15.96l-4.23-4.23L2.96,13.5l6,6L21.46,7L19.69,5.23z" />
        </svg>
        <svg class="mdc-switch__icon mdc-switch__icon--off" viewBox="0 0 24 24">
          <path d="M20 13H4v-2h16v2z" />
        </svg>
      </div>
    </div>
  </div>
</button>
<label for="{htmlCode}">off/on</label>
'''
  _js__builder__ = "console.log(mdc); window[htmlObj.id] = new mdc.switchControl.MDCSwitch(htmlObj)"


class ProgressBar(Component):
  css_classes = ["mdc-linear-progress", "mdc-linear-progress--indeterminate"]
  name = "Material Design Progress Indicator"

  str_repr = '''
<div role="progressbar" {attrs} aria-label="Example Progress Bar" aria-valuemin="0" aria-valuemax="10" aria-valuenow="5">
  <div class="mdc-linear-progress__buffer">
    <div class="mdc-linear-progress__buffer-bar"></div>
    <div class="mdc-linear-progress__buffer-dots"></div>
  </div>
  <div class="mdc-linear-progress__bar mdc-linear-progress__primary-bar">
    <span class="mdc-linear-progress__bar-inner"></span>
  </div>
  <div class="mdc-linear-progress__bar mdc-linear-progress__secondary-bar">
    <span class="mdc-linear-progress__bar-inner"></span>
  </div>
</div>
'''
  _js__builder__ = "window[htmlObj.id] = new mdc.linearProgress.MDCLinearProgress(htmlObj)"


class Select(Component):
  css_classes = ["mdc-select", "mdc-select--filled", "demo-width-class"]
  name = "Material Design Select"

  str_repr = '''
<div {attrs}>
  <div class="mdc-select__anchor">
    <span class="mdc-select__ripple"></span>
    <span class="mdc-floating-label mdc-floating-label--float-above">Pick a Food Group</span>
    <span class="mdc-select__selected-text-container">
      <span class="mdc-select__selected-text">Vegetables</span>
    </span>
    <span class="mdc-select__dropdown-icon">
      <svg
          class="mdc-select__dropdown-icon-graphic"
          viewBox="7 10 10 5" focusable="false">
        <polygon
            class="mdc-select__dropdown-icon-inactive"
            stroke="none"
            fill-rule="evenodd"
            points="7 10 12 15 17 10">
        </polygon>
        <polygon
            class="mdc-select__dropdown-icon-active"
            stroke="none"
            fill-rule="evenodd"
            points="7 15 12 10 17 15">
        </polygon>
      </svg>
    </span>
    <span class="mdc-line-ripple"></span>
  </div>

  <div class="mdc-select__menu demo-width-class mdc-menu mdc-menu-surface">
    <ul class="mdc-deprecated-list">
      <li class="mdc-deprecated-list-item" data-value="">
        <span class="mdc-deprecated-list-item__ripple"></span>
      </li>
      <li class="mdc-deprecated-list-item" data-value="grains">
        <span class="mdc-deprecated-list-item__ripple"></span>
        <span class="mdc-deprecated-list-item__text">Bread, Cereal, Rice, and Pasta</span>
      </li>
      <li class="mdc-deprecated-list-item mdc-deprecated-list-item--selected" data-value="vegetables" aria-selected="true">
        <span class="mdc-deprecated-list-item__ripple"></span>
        <span class="mdc-deprecated-list-item__text">Vegetables</span>
      </li>
      <li class="mdc-deprecated-list-item" data-value="fruit">
        <span class="mdc-deprecated-list-item__ripple"></span>
        <span class="mdc-deprecated-list-item__text">Fruit</span>
      </li>
    </ul>
  </div>
</div>
'''
  _js__builder__ = "window[htmlObj.id] = new mdc.select.MDCSelect(htmlObj)"


class TopAppBar(Component):
  css_classes = ["mdc-top-app-bar"]
  name = "Material Design Select"

  str_repr = '''
<header {attrs}>
  <div class="mdc-top-app-bar__row">
    <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start">
      <button class="material-icons mdc-top-app-bar__navigation-icon mdc-icon-button" aria-label="Open navigation menu">menu</button>
      <span class="mdc-top-app-bar__title">Page title</span>
    </section>
    <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end" role="toolbar">
      <button class="material-icons mdc-top-app-bar__action-item mdc-icon-button" aria-label="Favorite">favorite</button>
      <button class="material-icons mdc-top-app-bar__action-item mdc-icon-button" aria-label="Search">search</button>
      <button class="material-icons mdc-top-app-bar__action-item mdc-icon-button" aria-label="Options">more_vert</button>
    </section>
  </div>
</header>
<main class="mdc-top-app-bar--fixed-adjust">
  App content
</main>
'''
  _js__builder__ = "window[htmlObj.id] = new mdc.topAppBar.MDCTopAppBar(htmlObj)"


class Slider(Component):
  css_classes = ["mdc-slider"]
  name = "Material Design Slider"

  str_repr = '''
<div {attrs}>
  <input class="mdc-slider__input" type="range" min="0" max="100" value="50" name="volume" aria-label="Continuous slider demo">
  <div class="mdc-slider__track">
    <div class="mdc-slider__track--inactive"></div>
    <div class="mdc-slider__track--active">
      <div class="mdc-slider__track--active_fill"></div>
    </div>
  </div>
  <div class="mdc-slider__thumb">
    <div class="mdc-slider__thumb-knob"></div>
  </div>
</div>
'''
  _js__builder__ = "window[htmlObj.id] = new mdc.slider.MDCSlider(htmlObj)"


class Snackbar(Component):
  css_classes = ["mdc-snackbar", "mdc-snackbar--open"]
  name = "Material Design Snackbar"

  str_repr = '''
<aside {attrs}>
  <div class="mdc-snackbar__surface" role="status" aria-relevant="additions">
    <div class="mdc-snackbar__label" aria-atomic="false">
      Can't send photo. Retry in 5 seconds.
    </div>
    <div class="mdc-snackbar__actions" aria-atomic="true">
      <button type="button" class="mdc-button mdc-snackbar__action">
        <div class="mdc-button__ripple"></div>
        <span class="mdc-button__label">Retry</span>
      </button>
    </div>
  </div>
</aside>
'''
  _js__builder__ = "window[htmlObj.id] = new mdc.snackbar.MDCSnackbar(htmlObj); console.log(window[htmlObj.id])"

  @property
  def dom(self) -> DomMdcSnackbar.DomSnackbar:
    """
    Description:
    -----------
    The common DOM properties.
    """
    if self._dom is None:
      self._dom = DomMdcSnackbar.DomSnackbar(component=self, page=self.page)
    return self._dom


class Chip(Component):
  css_classes = ["mdc-chip-set"]
  name = "Material Design Chip"

  str_repr = '''
<span {attrs} role="grid">
  <span class="mdc-evolution-chip-set__chips" role="presentation">
    <span class="mdc-evolution-chip" role="row" id="c0">
      <span class="mdc-evolution-chip__cell mdc-evolution-chip__cell--primary" role="gridcell">
        <button class="mdc-evolution-chip__action mdc-evolution-chip__action--primary rounded" style="border:none" type="button" tabindex="0">
          <span class="mdc-evolution-chip__ripple mdc-evolution-chip__ripple--primary"></span>
          <span class="mdc-evolution-chip__text-label">Chip one</span>
        </button>
      </span>
    </span>
    <span class="mdc-evolution-chip" role="row" id="c1">
      <span class="mdc-evolution-chip__cell mdc-evolution-chip__cell--primary" role="gridcell">
        <button class="mdc-evolution-chip__action mdc-evolution-chip__action--primary rounded" style="border:none" type="button" tabindex="-1">
          <span class="mdc-evolution-chip__ripple mdc-evolution-chip__ripple--primary"></span>
          <span class="mdc-evolution-chip__text-label">Chip two</span>
        </button>
      </span>
    </span>
  </span>
</span>
'''
  _js__builder__ = "window[htmlObj.id] = new mdc.chips.MDCChipSet(htmlObj)"
