
from epyk.core.css.styles import GrpClsInput


class BsClsInput(GrpClsInput.ClassInput):

  def size(self, breakpoint):
    """
    https://getbootstrap.com/docs/5.0/forms/form-control/

    :param breakpoint:
    """
    self.component.attr["class"].add("form-control-%s" % breakpoint)

  def plain_text(self):
    """
    https://getbootstrap.com/docs/5.0/forms/form-control/
    """
    self.component.attr["class"].add("form-control-plaintext")


class BsClsSelect(GrpClsInput.ClassInput):

  def size(self, breakpoint):
    """
    Description:
    ------------
    You may also choose from small and large custom selects to match our similarly sized text inputs.

    https://getbootstrap.com/docs/5.0/forms/select/


    :param breakpoint: String. Optional. Grid system category, with
      - xs (for phones - screens less than 768px wide)
      - sm (for tablets - screens equal to or greater than 768px wide)
      - md (for small laptops - screens equal to or greater than 992px wide)
      - lg (for laptops and desktops - screens equal to or greater than 1200px wide)
    """
    self.component.attr["class"].add("form-select-%s" % breakpoint)
