
from epyk.core.html.options import Options


class OptionsJsonFmt(Options):

  @property
  def open(self):
    """  
    Default: 1 This number indicates up to how many levels the rendered tree should expand.
    Set it to 0 to make the whole tree collapsed or set it to Infinity to expand the tree deeply

    Related Pages:
    """
    return self._config_get(1)

  @open.setter
  def open(self, flag):
    self._config(flag)

  @property
  def hoverPreviewEnabled(self):
    """  
    Enable preview on hover.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    :prop flag:
    """
    return self._config_group_get('opts', False)

  @hoverPreviewEnabled.setter
  def hoverPreviewEnabled(self, flag):
    self._config_group('opts', flag)

  @property
  def hoverPreviewArrayCount(self):
    """  
    Number of array items to show in preview Any array larger than this number will be shown as Array[XXX]
    where XXX is length of the array.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    :prop num:
    """
    return self._config_group_get('opts', 100)

  @hoverPreviewArrayCount.setter
  def hoverPreviewArrayCount(self, num):
    self._config_group('opts', num)

  @property
  def hoverPreviewFieldCount(self):
    """  
    Number of object properties to show for object preview. Any object with more properties that thin number
    will be truncated.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    :prop num:
    """
    return self._config_group_get('opts', 5)

  @hoverPreviewFieldCount.setter
  def hoverPreviewFieldCount(self, num):
    self._config_group('opts', num)

  @property
  def animateOpen(self):
    """  
    Enable animation when expanding json object. True by default.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    :prop flag:
    """
    return self._config_group_get('opts', True)

  @animateOpen.setter
  def animateOpen(self, flag: bool):
    self._config_group('opts', flag)

  @property
  def animateClose(self):
    """  
    Enable animation when closing json object. True by default.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    :prop flag:
    """
    return self._config_group_get('opts', True)

  @animateClose.setter
  def animateClose(self, flag: bool):
    self._config_group('opts', flag)

  @property
  def useToJSON(self):
    """  
    use the toJSON method to render an object as a string as available.
    Usefull for objects like Date or Mongo's ObjectID that migh make more sense as a strign than as empty objects.
    True by default.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    :prop flag:
    """
    return self._config_group_get('opts', True)

  @useToJSON.setter
  def useToJSON(self, flag: bool):
    self._config_group('opts', flag)

  @property
  def sortPropertiesBy(self):
    """  
    use the given sorting function to deeply sort the object properties.

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    :prop flag:
    """
    return self._config_group_get('opts', None)

  @sortPropertiesBy.setter
  def sortPropertiesBy(self, flag: bool):
    self._config_group('opts', flag)


class OptionsLegend(Options):

  @property
  def style(self):
    """  

    :prop css_attrs:
    """
    return self.get({})

  @style.setter
  def style(self, css_attrs: dict):
    self.set(css_attrs)
