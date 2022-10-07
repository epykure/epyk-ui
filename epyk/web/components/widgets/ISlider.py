
from epyk.core import Page


class IntSlider:

  def __init__(self, value, min=0, max=10, step=1, description='Test:', disabled=False, continuous_update=False, orientation='horizontal', readout=True, readout_format='d'):
    """  

    Related Pages:

      https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html

    :param value:
    :param min:
    :param max:
    :param step:
    :param description:
    :param disabled:
    :param continuous_update:
    :param orientation:
    :param readout:
    :param readout_format:
    """
    self.page = Page.Report()
    self.component = self.page.ui.slider(number=value, minimum=min, maximum=max)
    self.component.style.css.width = "200px"
    self.component.input.options.step = step
    if orientation == "orientation":
      self.component.style.css.height = "28px"
      self.component.options.css = {"height": "5px", "background": "#bdbdbd"}
      self.component.options.handler_css = {
        "top": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    else:
      self.component.style.css.height = self.component.style.css.width
      self.component.style.css.width = self.component.style.css.height
      self.component.options.css = {"width": "5px", "background": "#bdbdbd"}
      self.component.options.handler_css = {
        "left": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    self.component.options.orientation = orientation

  def _repr_html_(self):
    return self.page.outs.jupyter()._repr_html_()


class FloatSlider:
  def __init__(self, value, min=0, max=10, step=0.1, description='Test:', disabled=False, continuous_update=False, orientation='horizontal', readout=True, readout_format='d'):
    """  

    https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html
    """
    self.page = Page.Report()
    self.component = self.page.ui.slider(number=value, minimum=min, maximum=max)
    self.component.style.css.width = "200px"
    self.component.input.options.step = step
    if orientation == "orientation":
      self.component.style.css.height = "28px"
      self.component.options.css = {"height": "5px", "background": "#bdbdbd"}
      self.component.options.handler_css = {
        "top": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    else:
      self.component.style.css.height = self.component.style.css.width
      self.component.style.css.width = self.component.style.css.height
      self.component.options.css = {"width": "5px", "background": "#bdbdbd"}
      self.component.options.handler_css = {
        "left": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    self.component.options.orientation = orientation

  def _repr_html_(self):
    return self.page.outs.jupyter()._repr_html_()


class FloatLogSlider:
  def __init__(self, value=10, base=10, min=-10, max=10, step=0.2, description='Test:', disabled=False, continuous_update=False,
               orientation='horizontal', readout=True, readout_format='d'):
    """  

    https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html

    :param value:
    :param min: Integer. Optional. in exponent of base.
    :param max: Integer. Optional. Max exponent of base.
    :param step: Number. Optional. Exponent step
    :param description:
    :param disabled:
    :param continuous_update:
    :param orientation:
    :param readout:
    :param readout_format:
    """
    raise Exception("Not yet available")


class IntRangeSlider:
  def __init__(self, values, min=0, max=10, step=1, description='Test:', disabled=False, continuous_update=False, orientation='horizontal', readout=True, readout_format='d'):
    """  

    https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html
    """
    self.page = Page.Report()
    self.component = self.page.ui.sliders.range(minimum=min, maximum=max)
    self.component.style.css.width = "200px"
    self.component.input.options.step = step
    if orientation == "orientation":
      self.component.style.css.height = "28px"
      self.component.options.css = {"height": "5px", "background": "#bdbdbd"}
      self.component.options.handler_css = {
        "top": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    else:
      self.component.style.css.height = self.component.style.css.width
      self.component.style.css.width = self.component.style.css.height
      self.component.options.css = {"width": "5px", "background": "#bdbdbd"}
      self.component.options.handler_css = {
        "left": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    self.component.options.orientation = orientation

  def _repr_html_(self):
    return self.page.outs.jupyter()._repr_html_()


class FloatRangeSlider:
  def __init__(self, values, min=0, max=10, step=0.1, description='Test:', disabled=False, continuous_update=False, orientation='horizontal', readout=True, readout_format='d'):
    """  

    https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html
    """
    self.page = Page.Report()
    self.component = self.page.ui.sliders.range(minimum=min, maximum=max)
    self.component.style.css.width = "200px"
    self.component.input.options.step = step
    if orientation == "orientation":
      self.component.style.css.height = "28px"
      self.component.options.css = {"height": "5px", "background": "#bdbdbd"}
      self.component.options.handler_css = {
        "top": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    else:
      self.component.style.css.height = self.component.style.css.width
      self.component.style.css.width = self.component.style.css.height
      self.component.options.css = {"width": "5px", "background": "#bdbdbd"}
      self.component.options.handler_css = {
        "left": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    self.component.options.orientation = orientation

  def _repr_html_(self):
    return self.page.outs.jupyter()._repr_html_()
