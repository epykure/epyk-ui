#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html.options import Options


class OptionsImage(Options):
  component_properties = ('color', )

  @property
  def background(self):
    """
    Description:
    ------------
    """
    return self._config_get(None)

  @background.setter
  def background(self, color):
    self._config(color)

  @property
  def color(self):
    """
    Description:
    ------------
    """
    return self._config_get(self.component.page.theme.colors[-1])

  @color.setter
  def color(self, color):
    self._config(color)


class OptionsTinySlider(Options):
  component_properties = ('container', 'items', 'loop', 'mouseDrag')

  @property
  def container(self):
    """
    Description:
    ------------
    The slider container element or selector.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("#%s" % self._report.htmlCode)

  @container.setter
  def container(self, value):
    self._config(value)

  @property
  def controls(self):
    """
    Description:
    ------------
    Controls the display and functionalities of controls components (prev/next buttons). If true, display the controls and add all functionalities.
    For better accessibility, when a prev/next button is focused, user will be able to control the slider using left/right arrow keys.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @controls.setter
  def controls(self, flag):
    self._config(flag)

  @property
  def mouseDrag(self):
    """
    Description:
    ------------
    Changing slides by dragging them.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @mouseDrag.setter
  def mouseDrag(self, flag):
    if flag:
      self.component.style.css.cursor = "pointer"
    self._config(flag)

  @property
  def controlsPosition(self):
    """
    Description:
    ------------
    Controls controls position.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("top")

  @controlsPosition.setter
  def controlsPosition(self, flag):
    self._config(flag)

  @property
  def controlsText(self):
    """
    Description:
    ------------
    Text or markup in the prev/next buttons.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(["prev", "next"])

  @controlsText.setter
  def controlsText(self, flag):
    self._config(flag)

  @property
  def controlsContainer(self):
    """
    Description:
    ------------
    The container element/selector around the prev/next buttons.
    controlsContainer must have at least 2 child elements.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @controlsContainer.setter
  def controlsContainer(self, flag):
    self._config(flag)

  @property
  def mode(self):
    """
    Description:
    ------------
    Controls animation behaviour.

    With carousel everything slides to the side, while gallery uses fade animations and changes all slides at once.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("carousel")

  @mode.setter
  def mode(self, value):
    if value not in ["carousel", "gallery"]:
      raise Exception("Value not recognised for tiny carousel mode: %s" % value)

    self._config(value)

  @property
  def axis(self):
    """
    Description:
    ------------
    The axis of the slider.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("horizontal")

  @axis.setter
  def axis(self, value):
    if value not in ["horizontal", "vertical"]:
      raise Exception("Value not recognised for tiny carousel axis: %s" % value)

    self._config(value)

  @property
  def items(self):
    """
    Description:
    ------------
    Number of slides being displayed in the viewport.
    If slides less or equal than items, the slider won't be initialized.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(1)

  @items.setter
  def items(self, num):
    self._config(num)

  @property
  def gutter(self):
    """
    Description:
    ------------
    Space between slides (in "px").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(0)

  @gutter.setter
  def gutter(self, num):
    self._config(num)

  @property
  def edgePadding(self):
    """
    Description:
    ------------
    Space on the outside (in "px").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(0)

  @edgePadding.setter
  def edgePadding(self, num):
    self._config(num)

  @property
  def fixedWidth(self):
    """
    Description:
    ------------
    Controls width attribute of the slides.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @fixedWidth.setter
  def fixedWidth(self, value):
    self._config(value)

  @property
  def autoWidth(self):
    """
    Description:
    ------------
    If true, the width of each slide will be its natural width as a inline-block box.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoWidth.setter
  def autoWidth(self, bool):
    self._config(bool)

  @property
  def slideBy(self):
    """
    Description:
    ------------
    Number of slides going on one "click".

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(1)

  @slideBy.setter
  def slideBy(self, value):
    self._config(value)

  @property
  def viewportMax(self):
    """
    Description:
    ------------
    Maximum viewport width for fixedWidth/autoWidth

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @viewportMax.setter
  def viewportMax(self, value):
    self._config(value)

  @property
  def center(self):
    """
    Description:
    ------------
    Center the active slide in the viewport.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @center.setter
  def center(self, value):
    self._config(value)

  @property
  def prevButton(self):
    """
    Description:
    ------------
    Customized previous buttons.
    This option will be ignored if controlsContainer is a Node element or a CSS selector.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @prevButton.setter
  def prevButton(self, value):
    self._config(value)

  @property
  def nextButton(self):
    """
    Description:
    ------------
    Customized next buttons.
    This option will be ignored if controlsContainer is a Node element or a CSS selector.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @nextButton.setter
  def nextButton(self, value):
    self._config(value)

  @property
  def nav(self):
    """
    Description:
    ------------
    Controls the display and functionalities of nav components (dots).
    If true, display the nav and add all functionalities.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @nav.setter
  def nav(self, value):
    self._config(value)

  @property
  def navPosition(self):
    """
    Description:
    ------------
    Controls nav position.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get('top')

  @navPosition.setter
  def navPosition(self, value):
    self._config(value)

  @property
  def navContainer(self):
    """
    Description:
    ------------
    The container element/selector around the dots.
    navContainer must have at least same number of children as the slides.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @navContainer.setter
  def navContainer(self, value):
    self._config(value)

  @property
  def navAsThumbnails(self):
    """
    Description:
    ------------
    Indicate if the dots are thumbnails.
    If true, they will always be visible even when more than 1 slides displayed in the viewport.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @navAsThumbnails.setter
  def navAsThumbnails(self, value):
    self._config(value)

  @property
  def arrowKeys(self):
    """
    Description:
    ------------
    Allows using arrow keys to switch slides.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @arrowKeys.setter
  def arrowKeys(self, value):
    self._config(value)

  @property
  def speed(self):
    """
    Description:
    ------------
    Speed of the slide animation (in "ms").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(300)

  @speed.setter
  def speed(self, num):
    self._config(num)

  @property
  def autoplay(self):
    """
    Description:
    ------------
    Toggles the automatic change of slides.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoplay.setter
  def autoplay(self, num):
    self._config(num)

  @property
  def autoplayPosition(self):
    """
    Description:
    ------------
    Controls autoplay position.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get('top')

  @autoplayPosition.setter
  def autoplayPosition(self, num):
    self._config(num)

  @property
  def autoplayTimeout(self):
    """
    Description:
    ------------
    Time between 2 autoplay slides change (in "ms").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(5000)

  @autoplayTimeout.setter
  def autoplayTimeout(self, num):
    self._config(num)

  @property
  def autoplayDirection(self):
    """
    Description:
    ------------
    Direction of slide movement (ascending/descending the slide index).

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get('forward')

  @autoplayDirection.setter
  def autoplayDirection(self, num):
    self._config(num)

  @property
  def autoplayText(self):
    """
    Description:
    ------------
    Text or markup in the autoplay start/stop button.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(["start", "stop"])

  @autoplayText.setter
  def autoplayText(self, num):
    self._config(num)

  @property
  def autoplayHoverPause(self):
    """
    Description:
    ------------
    Stops sliding on mouseover.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoplayHoverPause.setter
  def autoplayHoverPause(self, num):
    self._config(num)

  @property
  def autoplayButton(self):
    """
    Description:
    ------------
    The customized autoplay start/stop button or selector.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoplayButton.setter
  def autoplayButton(self, num):
    self._config(num)

  @property
  def autoplayButtonOutput(self):
    """
    Description:
    ------------
    Output autoplayButton markup when autoplay is true but a customized autoplayButton is not provided.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @autoplayButtonOutput.setter
  def autoplayButtonOutput(self, bool):
    self._config(bool)

  @property
  def autoplayResetOnVisibility(self):
    """
    Description:
    ------------
    Pauses the sliding when the page is invisible and resumes it when the page become visiable again. (Page Visibility API)

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @autoplayResetOnVisibility.setter
  def autoplayResetOnVisibility(self, bool):
    self._config(bool)

  @property
  def animateIn(self):
    """
    Description:
    ------------
    Name of intro animation class

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("tns-fadeIn")

  @animateIn.setter
  def animateIn(self, value):
    self._config(value)

  @property
  def animateOut(self):
    """
    Description:
    ------------
    Name of outro animation class

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("tns-fadeOut")

  @animateOut.setter
  def animateOut(self, value):
    self._config(value)

  @property
  def animateNormal(self):
    """
    Description:
    ------------
    Name of default animation class.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get("tns-normal")

  @animateNormal.setter
  def animateNormal(self, value):
    self._config(value)

  @property
  def animateDelay(self):
    """
    Description:
    ------------
    Time between each gallery animation (in "ms").

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @animateDelay.setter
  def animateDelay(self, value):
    self._config(value)

  @property
  def loop(self):
    """
    Description:
    ------------
    Moves throughout all the slides seamlessly.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @loop.setter
  def loop(self, value):
    self._config(value)

  @property
  def rewind(self):
    """
    Description:
    ------------
    Moves to the opposite edge when reaching the first or last slide.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @rewind.setter
  def rewind(self, value):
    self._config(value)

  @property
  def autoHeight(self):
    """
    Description:
    ------------
    Height of slider container changes according to each slide's height.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @autoHeight.setter
  def autoHeight(self, value):
    self._config(value)

  @property
  def responsive(self):
    """
    Description:
    ------------
    Defines options for different viewport widths (see Responsive Options).

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @responsive.setter
  def responsive(self, value):
    self._config(value)

  @property
  def lazyload(self):
    """
    Description:
    ------------
    Defines options for different viewport widths (see Responsive Options).

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @lazyload.setter
  def lazyload(self, value):
    self._config(value)

  @property
  def preventScrollOnTouch (self):
    """
    Description:
    ------------
    Defines options for different viewport widths (see Responsive Options).

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @preventScrollOnTouch .setter
  def preventScrollOnTouch (self, value):
    self._config(value)

  @property
  def nested(self):
    """
    Description:
    ------------
    Define the relationship between nested sliders. (see demo)
    Make sure you run the inner slider first, otherwise the height of the inner slider container will be wrong

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @nested.setter
  def nested(self, value):
    self._config(value)

  @property
  def freezable(self):
    """
    Description:
    ------------
    Indicate whether the slider will be frozen (controls, nav, autoplay and other functions will stop work) when all slides can be displayed in one page.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @freezable.setter
  def freezable(self, value):
    self._config(value)

  @property
  def disable(self):
    """
    Description:
    ------------
    Disable slider.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @disable.setter
  def disable(self, value):
    self._config(value)

  @property
  def startIndex(self):
    """
    Description:
    ------------
    The initial index of the slider.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(0)

  @startIndex.setter
  def startIndex(self, num):
    self._config(num)

  @property
  def onInit(self):
    """
    Description:
    ------------
    Callback to be run on initialization.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @onInit.setter
  def onInit(self, value):
    self._config(value)

  @property
  def useLocalStorage(self):
    """
    Description:
    ------------
    Save browser capability variables to localStorage and without detecting them everytime the slider runs if set to true.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(True)

  @useLocalStorage.setter
  def useLocalStorage(self, value):
    self._config(value)

  @property
  def nonce(self):
    """
    Description:
    ------------
    Optional Nonce attribute for inline style tag to allow slider usage without `unsafe-inline Content Security Policy source.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return self._config_get(False)

  @nonce.setter
  def nonce(self, value):
    self._config(value)
