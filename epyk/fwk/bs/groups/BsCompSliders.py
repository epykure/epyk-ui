

class Components:

  def __init__(self, ui):
    self.page = ui.page

  def progressbar(self, number=0, total=100, label=None, category=None, width=(100, '%'), height=(20, 'px'),
                  html_code=None, options=None, profile=None):
    """
    Description:
    -----------
    Documentation and examples for using Bootstrap custom progress bars featuring support for stacked bars,
    animated backgrounds, and text labels.

    Usage::

      page.web.bs.sliders.progressbar(30, label="Quantity")

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/progress/

    Attributes:
    ----------
    :param number: Number. Optional. The initial value.
    :param label: Component | String. Optional. The label on the slider component.
    :param total: Number. Optional. The maximum value.
    :param category: String. Optional. The bootstrap background category.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    progress = self.page.web.std.div(label, width=(number, "%"), html_code=html_code, options=options, profile=profile)
    progress.attr["class"].initialise(["progress-bar"])
    progress.attr["role"] = "progressbar"
    progress.aria.valuenow = number
    progress.aria.valuemin = 0
    progress.aria.valuemax = total
    if category is not None:
      progress.attr["class"].add("bg-%s" % category)
    container = self.page.web.std.div(progress, width=width, height=height)
    container.attr["class"].initialise(["progress"])
    return container

  def multibars(self, values=None, total=100, labels=None, categories=None, width=(100, '%'), height=(20, 'px'),
                html_code=None, options=None, profile=None):
    """
    Description:
    -----------
    Include multiple progress bars in a progress component if you need.

    Usage::

      page.web.bs.sliders.multibars([30, 35], labels=["Quantity1", "Quantity 2"], categories=[None, "success", "info"])

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/progress/#multiple-bars

    Attributes:
    ----------
    :param values: Number. Optional. The initial values for the sliders.
    :param total: Number. Optional. The maximum value.
    :param labels: ist<SComponent | String>. Optional. The labels on the slider components.
    :param categories: List<String>. Optional. The bootstrap background categories
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bars = []
    if values is not None:
      for i, value in enumerate(values):
        if labels is not None and i < len(labels):
          progress = self.page.web.std.div(
            labels[i], width=(value, "%"), html_code=html_code, options=options, profile=profile)
        else:
          progress = self.page.web.std.div(width=(value, "%"), html_code=html_code, options=options, profile=profile)
        progress.attr["class"].initialise(["progress-bar"])
        if categories is not None and i < len(categories):
          if categories[i] is not None:
            progress.attr["class"].add("bg-%s" % categories[i])
        progress.attr["role"] = "progressbar"
        progress.aria.valuenow = value
        progress.aria.valuemin = 0
        progress.aria.valuemax = total
        bars.append(progress)
    container = self.page.web.std.div(bars, width=width, height=height)
    container.attr["class"].initialise(["progress"])
    return container

  def slider(self, number=0, minimum=0, maximum=100, step=None, width=(100, '%'), height=(None, 'px'), html_code=None,
             options=None, profile=None):
    """
    Description:
    -----------
    Use our custom range inputs for consistent cross-browser styling and built-in customization.

    Usage::

      slider =  page.web.bs.sliders.slider(30)
      page.ui.button("Test").click([
        page.js.console.log(slider.dom.content),
        slider.build(90)
      ])

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/range/

    Attributes:
    ----------
    :param number: Number. Optional. The initial value.
    :param minimum: Number. Optional. The minimum value.
    :param maximum: Number. Optional.  The maximum value.
    :param step: Number. Optional. The step value.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    slider = self.page.web.std.input(
      number, width=width, height=height, html_code=html_code, options=options, profile=profile)
    slider.attr["class"].initialise(["form-range"])
    slider.attr["min"] = minimum
    slider.attr["max"] = maximum
    if step is not None:
      slider.attr["step"] = step
    slider.attr["type"] = "range"
    return slider

