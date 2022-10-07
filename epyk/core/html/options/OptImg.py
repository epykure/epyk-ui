#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html.options import Options


class OptionsImage(Options):
  component_properties = ('color', )

  @property
  def background(self):
    """  
    """
    return self._config_get(None)

  @background.setter
  def background(self, color):
    self._config(color)

  @property
  def color(self):
    """  
    """
    return self._config_get(self.page.theme.colors[-1])

  @color.setter
  def color(self, color: str):
    self._config(color)


class OptionsTinySlider(Options):
  component_properties = ('container', 'items', 'loop', 'mouseDrag')

  @property
  def container(self):
    """  
    The slider container element or selector.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("#%s" % self.component.htmlCode)

  @container.setter
  def container(self, value: str):
    self._config(value)

  @property
  def controls(self):
    """  
    Controls the display and functionalities of controls components (prev/next buttons). If true, display the controls
    and add all functionalities.
    For better accessibility, when a prev/next button is focused, user will be able to control the slider
    using left/right arrow keys.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @controls.setter
  def controls(self, flag: bool):
    self._config(flag)

  @property
  def mouseDrag(self):
    """  
    Changing slides by dragging them.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @mouseDrag.setter
  def mouseDrag(self, flag: bool):
    if flag:
      self.component.style.css.cursor = "pointer"
    self._config(flag)

  @property
  def controlsPosition(self):
    """  
    Controls controls position.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("top")

  @controlsPosition.setter
  def controlsPosition(self, flag: bool):
    self._config(flag)

  @property
  def controlsText(self):
    """  
    Text or markup in the prev/next buttons.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(["prev", "next"])

  @controlsText.setter
  def controlsText(self, flag: bool):
    self._config(flag)

  @property
  def controlsContainer(self):
    """  
    The container element/selector around the prev/next buttons.
    controlsContainer must have at least 2 child elements.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @controlsContainer.setter
  def controlsContainer(self, flag: bool):
    self._config(flag)

  @property
  def mode(self):
    """  
    Controls animation behaviour.

    With carousel everything slides to the side, while gallery uses fade animations and changes all slides at once.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("carousel")

  @mode.setter
  def mode(self, value: str):
    if value not in ["carousel", "gallery"]:
      raise ValueError("Value not recognised for tiny carousel mode: %s" % value)

    self._config(value)

  @property
  def axis(self):
    """  
    The axis of the slider.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("horizontal")

  @axis.setter
  def axis(self, value: str):
    if value not in ["horizontal", "vertical"]:
      raise ValueError("Value not recognised for tiny carousel axis: %s" % value)

    self._config(value)

  @property
  def items(self):
    """  
    Number of slides being displayed in the viewport.
    If slides less or equal than items, the slider won't be initialized.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(1)

  @items.setter
  def items(self, num: int):
    self._config(num)

  @property
  def gutter(self):
    """  
    Space between slides (in "px").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(0)

  @gutter.setter
  def gutter(self, num: int):
    self._config(num)

  @property
  def edgePadding(self):
    """  
    Space on the outside (in "px").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(0)

  @edgePadding.setter
  def edgePadding(self, num: int):
    self._config(num)

  @property
  def fixedWidth(self):
    """  
    Controls width attribute of the slides.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @fixedWidth.setter
  def fixedWidth(self, value: int):
    self._config(value)

  @property
  def autoWidth(self):
    """  
    If true, the width of each slide will be its natural width as a inline-block box.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoWidth.setter
  def autoWidth(self, flag: bool):
    self._config(flag)

  @property
  def slideBy(self):
    """  
    Number of slides going on one "click".

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(1)

  @slideBy.setter
  def slideBy(self, value: int):
    self._config(value)

  @property
  def viewportMax(self):
    """  
    Maximum viewport width for fixedWidth/autoWidth

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @viewportMax.setter
  def viewportMax(self, value: int):
    self._config(value)

  @property
  def center(self):
    """  
    Center the active slide in the viewport.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @center.setter
  def center(self, value: bool):
    self._config(value)

  @property
  def prevButton(self):
    """  
    Customized previous buttons.
    This option will be ignored if controlsContainer is a Node element or a CSS selector.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @prevButton.setter
  def prevButton(self, value: bool):
    self._config(value)

  @property
  def nextButton(self):
    """  
    Customized next buttons.
    This option will be ignored if controlsContainer is a Node element or a CSS selector.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @nextButton.setter
  def nextButton(self, value: bool):
    self._config(value)

  @property
  def nav(self):
    """  
    Controls the display and functionalities of nav components (dots).
    If true, display the nav and add all functionalities.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @nav.setter
  def nav(self, value: bool):
    self._config(value)

  @property
  def navPosition(self):
    """  
    Controls nav position.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get('top')

  @navPosition.setter
  def navPosition(self, value: str):
    self._config(value)

  @property
  def navContainer(self):
    """  
    The container element/selector around the dots.
    navContainer must have at least same number of children as the slides.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @navContainer.setter
  def navContainer(self, value: bool):
    self._config(value)

  @property
  def navAsThumbnails(self):
    """  
    Indicate if the dots are thumbnails.
    If true, they will always be visible even when more than 1 slides displayed in the viewport.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @navAsThumbnails.setter
  def navAsThumbnails(self, value: bool):
    self._config(value)

  @property
  def arrowKeys(self):
    """  
    Allows using arrow keys to switch slides.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @arrowKeys.setter
  def arrowKeys(self, value: bool):
    self._config(value)

  @property
  def speed(self):
    """  
    Speed of the slide animation (in "ms").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(300)

  @speed.setter
  def speed(self, num: int):
    self._config(num)

  @property
  def autoplay(self):
    """  
    Toggles the automatic change of slides.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoplay.setter
  def autoplay(self, flag: bool):
    self._config(flag)

  @property
  def autoplayPosition(self):
    """  
    Controls autoplay position.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get('top')

  @autoplayPosition.setter
  def autoplayPosition(self, text: str):
    self._config(text)

  @property
  def autoplayTimeout(self):
    """  
    Time between 2 autoplay slides change (in "ms").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(5000)

  @autoplayTimeout.setter
  def autoplayTimeout(self, num: int):
    self._config(num)

  @property
  def autoplayDirection(self):
    """  
    Direction of slide movement (ascending/descending the slide index).

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get('forward')

  @autoplayDirection.setter
  def autoplayDirection(self, text: str):
    self._config(text)

  @property
  def autoplayText(self):
    """  
    Text or markup in the autoplay start/stop button.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(["start", "stop"])

  @autoplayText.setter
  def autoplayText(self, text: str):
    self._config(text)

  @property
  def autoplayHoverPause(self):
    """  
    Stops sliding on mouseover.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoplayHoverPause.setter
  def autoplayHoverPause(self, flag: bool):
    self._config(flag)

  @property
  def autoplayButton(self):
    """  
    The customized autoplay start/stop button or selector.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoplayButton.setter
  def autoplayButton(self, flag: bool):
    self._config(flag)

  @property
  def autoplayButtonOutput(self):
    """  
    Output autoplayButton markup when autoplay is true but a customized autoplayButton is not provided.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @autoplayButtonOutput.setter
  def autoplayButtonOutput(self, flag: bool):
    self._config(flag)

  @property
  def autoplayResetOnVisibility(self):
    """  
    Pauses the sliding when the page is invisible and resumes it when the page become visiable again. (Page Visibility API)

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @autoplayResetOnVisibility.setter
  def autoplayResetOnVisibility(self, flag: bool):
    self._config(flag)

  @property
  def animateIn(self):
    """  
    Name of intro animation class

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("tns-fadeIn")

  @animateIn.setter
  def animateIn(self, value: str):
    self._config(value)

  @property
  def animateOut(self):
    """  
    Name of outro animation class

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("tns-fadeOut")

  @animateOut.setter
  def animateOut(self, value: str):
    self._config(value)

  @property
  def animateNormal(self):
    """  
    Name of default animation class.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("tns-normal")

  @animateNormal.setter
  def animateNormal(self, value: str):
    self._config(value)

  @property
  def animateDelay(self):
    """  
    Time between each gallery animation (in "ms").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @animateDelay.setter
  def animateDelay(self, flag: bool):
    self._config(flag)

  @property
  def loop(self):
    """  
    Moves throughout all the slides seamlessly.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @loop.setter
  def loop(self, flag: bool):
    self._config(flag)

  @property
  def rewind(self):
    """  
    Moves to the opposite edge when reaching the first or last slide.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @rewind.setter
  def rewind(self, flag: bool):
    self._config(flag)

  @property
  def autoHeight(self):
    """  
    Height of slider container changes according to each slide's height.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoHeight.setter
  def autoHeight(self, flag: bool):
    self._config(flag)

  @property
  def responsive(self):
    """  
    Defines options for different viewport widths (see Responsive Options).

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @responsive.setter
  def responsive(self, flag: bool):
    self._config(flag)

  @property
  def lazyload(self):
    """  
    Defines options for different viewport widths (see Responsive Options).

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @lazyload.setter
  def lazyload(self, flag: bool):
    self._config(flag)

  @property
  def preventScrollOnTouch(self):
    """  
    Defines options for different viewport widths (see Responsive Options).

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @preventScrollOnTouch .setter
  def preventScrollOnTouch(self, flag: bool):
    self._config(flag)

  @property
  def nested(self):
    """  
    Define the relationship between nested sliders. (see demo)
    Make sure you run the inner slider first, otherwise the height of the inner slider container will be wrong

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @nested.setter
  def nested(self, flag: bool):
    self._config(flag)

  @property
  def freezable(self):
    """  
    Indicate whether the slider will be frozen (controls, nav, autoplay and other functions will stop work) when all
    slides can be displayed in one page.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @freezable.setter
  def freezable(self, flag: bool):
    self._config(flag)

  @property
  def disable(self):
    """  
    Disable slider.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @disable.setter
  def disable(self, flag: bool):
    self._config(flag)

  @property
  def startIndex(self):
    """  
    The initial index of the slider.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(0)

  @startIndex.setter
  def startIndex(self, num: int):
    self._config(num)

  @property
  def onInit(self):
    """  
    Callback to be run on initialization.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @onInit.setter
  def onInit(self, flag: bool):
    self._config(flag)

  @property
  def useLocalStorage(self):
    """  
    Save browser capability variables to localStorage and without detecting them everytime the slider runs if
    set to true.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @useLocalStorage.setter
  def useLocalStorage(self, flag: bool):
    self._config(flag)

  @property
  def nonce(self):
    """  
    Optional Nonce attribute for inline style tag to allow slider usage without `unsafe-inline Content Security
    Policy source.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @nonce.setter
  def nonce(self, flag: bool):
    self._config(flag)
