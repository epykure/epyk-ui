
class Components:

  def __init__(self, ui):
    self.page = ui.page

  def dialog(self, text, width=(100, '%'), height=(20, 'px'), html_code=None, helper=None, options=None, profile=None):
    pass

  def acknowledge(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass

  def popup(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass

  def error(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass

  def info(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass

  def success(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass

