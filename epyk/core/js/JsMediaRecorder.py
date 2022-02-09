
from typing import Union
from epyk.core.py import primitives


class MediaRecorder:

  def __init__(self, page: primitives.PageModel = None):
    self.page = page
    self._js = []

  def ondataavailable(self, js_funcs: Union[str, list]):
    pass

  def onstop(self, js_funcs: Union[str, list]):
    pass

  def start(self):
    pass

  def stop(self):
    pass
