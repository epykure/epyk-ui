
from epyk.core.html.options import Options


class OptionsJsonFmt(Options):

  @property
  def open(self):
    """
    Description:
    ------------
    Default: 1 This number indicates up to how many levels the rendered tree should expand.
    Set it to 0 to make the whole tree collapsed or set it to Infinity to expand the tree deeply

    Related Pages:
"""
    return self._config_get(1)

  @open.setter
  def open(self, bool):
    self._config(bool)

  @property
  def hoverPreviewEnabled(self):
    """
    Description:
    ------------
    Enable preview on hover.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    Attributes:
    ----------
    """
    return self._report._jsStyles.get('opts', {}).get('hoverPreviewEnabled', False)

  @hoverPreviewEnabled.setter
  def hoverPreviewEnabled(self, bool):
    self._report._jsStyles.setdefault('opts', {})['hoverPreviewEnabled'] = bool

  @property
  def hoverPreviewArrayCount(self):
    """
    Description:
    ------------
    Number of array items to show in preview Any array larger than this number will be shown as Array[XXX] where XXX is length of the array.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    Attributes:
    ----------
    """
    return self._report._jsStyles.get('opts', {}).get('hoverPreviewArrayCount', 100)

  @hoverPreviewArrayCount.setter
  def hoverPreviewArrayCount(self, num):
    self._report._jsStyles.setdefault('opts', {})['hoverPreviewArrayCount'] = num

  @property
  def hoverPreviewFieldCount(self):
    """
    Description:
    ------------
    Number of object properties to show for object preview. Any object with more properties that thin number will be truncated.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    Attributes:
    ----------
    """
    return self._report._jsStyles.get('opts', {}).get('hoverPreviewFieldCount', 5)

  @hoverPreviewFieldCount.setter
  def hoverPreviewFieldCount(self, num):
    self._report._jsStyles.setdefault('opts', {})['hoverPreviewFieldCount'] = num

  @property
  def animateOpen(self):
    """
    Description:
    ------------
    Enable animation when expanding json object. True by default.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    Attributes:
    ----------
    """
    return self._report._jsStyles.get('opts', {}).get('animateOpen', True)

  @animateOpen.setter
  def animateOpen(self, bool):
    self._report._jsStyles.setdefault('opts', {})['animateOpen'] = bool

  @property
  def animateClose(self):
    """
    Description:
    ------------
    Enable animation when closing json object. True by default.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    Attributes:
    ----------
    """
    return self._report._jsStyles.get('opts', {}).get('animateClose', True)

  @animateClose.setter
  def animateClose(self, bool):
    self._report._jsStyles.setdefault('opts', {})['animateClose'] = bool

  @property
  def useToJSON(self):
    """
    Description:
    ------------
    use the toJSON method to render an object as a string as available.
    Usefull for objects like Date or Mongo's ObjectID that migh make more sense as a strign than as empty objects. True by default.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    Attributes:
    ----------
    """
    return self._report._jsStyles.get('opts', {}).get('useToJSON', True)

  @useToJSON.setter
  def useToJSON(self, bool):
    self._report._jsStyles.setdefault('opts', {})['useToJSON'] = bool

  @property
  def sortPropertiesBy(self):
    """
    Description:
    ------------
    use the given sorting function to deeply sort the object properties.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    Attributes:
    ----------
    """
    return self._report._jsStyles.get('opts', {}).get('sortPropertiesBy')

  @sortPropertiesBy.setter
  def sortPropertiesBy(self, bool):
    self._report._jsStyles.setdefault('opts', {})['sortPropertiesBy'] = bool
