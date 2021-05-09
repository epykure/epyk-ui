
import os


class Jupyter:

  @property
  def built_in(self):
    """
    Description:
    ------------
    Get the list of external packages installed to the Jupyter instance.

    """
    import notebook

    nb_path = os.path.split(notebook.__file__)[0]
    return os.listdir(os.path.join(nb_path, 'static', 'components'))

