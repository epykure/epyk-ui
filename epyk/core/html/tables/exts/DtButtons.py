
from epyk.core.data.DataClass import DataClass


class InnerButtons(DataClass):

  @property
  def text(self):
    """
    Description:
    -----------
    Being able to let your users know what will happen when they activate a button is obviously fundamentally important to the Buttons extension and this option provides exactly that ability.
    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.text
    """
    return self._attrs['text']

  @text.setter
  def text(self, val):
    self._attrs['text'] = val

  @property
  def action(self):
    """
    Description:
    -----------
    This function defined the action that the button will take when activated by the end user.
    This will normally be to perform some operation on the DataTable, but can be absolutely anything since the function can be defined by yourself.
    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.action
    """
    return self._attrs['action']

  @action.setter
  def action(self, val):
    self._attrs['action'] = val

  @property
  def attr(self):
    """
    Description:
    -----------
    This option provides the ability to set any arbitrary attribute on the button's HTML element in the document.
    This can be useful for customisation of attributes such as ARIA assistive attributes, setting a custom id for selection / styling, custom data parameters, etc.
    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.attr
    """
    return self._attrs['attr']

  @attr.setter
  def attr(self, val):
    self._attrs['attr'] = val

  @property
  def className(self):
    """
    Description:
    -----------
    Set the class name for the button.
    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.className
    """
    return self._attrs['className']

  @className.setter
  def className(self, val):
    self._attrs['className'] = val

  @property
  def available(self):
    """
    Description:
    -----------
    Ensure that any requirements have been satisfied before initialising a button
    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.available
    """
    return self._attrs['available']

  @available.setter
  def available(self, val):
    self._attrs['available'] = val

  @property
  def enabled(self):
    """
    Description:
    -----------
    This option provides the ability to set the initial enabled state of a button using a boolean value.
    It is most likely to be of use when using the API methods that can control the button's enabled state after initialisation:
    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.enabled
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def extend(self):
    """
    Description:
    -----------
    Define which button type the button should be based on.

    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.extend
    """
    return self._attrs["extend"]

  @extend.setter
  def extend(self, val):
    self._attrs["extend"] = val

  @property
  def key(self):
    """
    Description:
    -----------
    Define an activation key for a button.

    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.key
    """
    return self._attrs["key"]

  @key.setter
  def key(self, val):
    self._attrs["key"] = val

  @property
  def name(self):
    """
    Description:
    -----------
    Define a name for a button.

    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.name
    """
    return self._attrs["name"]

  @name.setter
  def name(self, val):
    self._attrs["name"] = val

  @property
  def tag(self):
    """
    Description:
    -----------
    Define a tag  for a button.

    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.tag
    """
    return self._attrs["tag"]

  @tag.setter
  def tag(self, val):
    self._attrs["tag"] = val

  @property
  def titleAttr(self):
    """
    Description:
    -----------
    This option provides the ability to set the title attribute for the button.
    This can be used to provide a detailed description of the button, or a simple text name if you choose to display an icon in the button rather than text (using the buttons.buttons.text option).

    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.titleAttr
    """
    return self._attrs["titleAttr"]

  @titleAttr.setter
  def titleAttr(self, val):
    self._attrs["titleAttr"] = val

class Buttons(DataClass):

  class Dom(DataClass):

    class Container(DataClass):
      @property
      def tag(self):
        return self._attrs['tag']

      @tag.setter
      def tag(self, val):
        self._attrs['tag'] = val

      @property
      def className(self):
        return self._attrs['className']

      @className.setter
      def className(self, val):
        self._attrs['className'] = val


    class ButtonLiner(DataClass):
      @property
      def tag(self):
        return self._attrs['tag']

      @tag.setter
      def tag(self, val):
        self._attrs['tag'] = val

      @property
      def className(self):
        return self._attrs['className']

      @className.setter
      def className(self, val):
        self._attrs['className'] = val


    class Collection(DataClass):
      @property
      def tag(self):
        return self._attrs['tag']

      @tag.setter
      def tag(self, val):
        self._attrs['tag'] = val

      @property
      def className(self):
        return self._attrs['className']

      @className.setter
      def className(self, val):
        self._attrs['className'] = val


    class DomButton(DataClass):
      @property
      def tag(self):
        return self._attrs['tag']

      @tag.setter
      def tag(self, val):
        self._attrs['tag'] = val

      @property
      def className(self):
        return self._attrs['className']

      @className.setter
      def className(self, val):
        self._attrs['className'] = val

      @property
      def disabled(self):
        return self._attrs['disabled']

      @disabled.setter
      def disabled(self, val):
        self._attrs['disabled'] = val

      @property
      def active(self):
        return self._attrs['active']

      @active.setter
      def active(self, val):
        self._attrs['active'] = val


    @property
    def buttonContainer(self):
      """
      Description:
      -----------
      This option provides the ability for each button to be wrapped in another element.
      This can be useful for cases where the styling framework requires a list of buttons,
      where the list element is just a container and not the button itself (Zurb Foundation requires this for example).
      Related Pages:

      https://datatables.net/reference/option/buttons.buttons.buttonContainer
      """
      return self.sub_data('buttonContainer', self.Container)

    @property
    def buttonLiner(self):
      """
      Description:
      -----------
      This option controls the HTML tag that is used as the liner for each button.
      This can be particularly useful for adding complex styling rules to buttons.
      It can also be disabled if you wish to have minimal markup in your document.
      Related Pages:

      https://datatables.net/reference/option/buttons.buttons.buttonLiner
      """
      return self.sub_data('buttonLiner', self.ButtonLiner)

    @property
    def collection(self):
      """
      Description:
      -----------
      This option controls the HTML tag that is used for the element that is displayed when a collection button is triggered.
      It in turn contains the sub-buttons of the collection.
      Related Pages:

      https://datatables.net/reference/option/buttons.buttons.collection
      """
      return self.sub_data('collection', self.Collection)

    @property
    def button(self):
      """
      Description:
      -----------
      This option controls the HTML tag that is used to create each individual button.
      With this option the tag type and class name can be specified using the tag and className properties of this object.
      Related Pages:

      https://datatables.net/reference/option/buttons.buttons.button
      """
      return self.sub_data('button', self.DomButton)


  @property
  def enabled(self):
    """
    Description:
    -----------
    This option provides the ability to set the initial enabled state of a button using a boolean value.
    It is most likely to be of use when using the API methods that can control the button's enabled state after initialisation:
    Related Pages:

      https://datatables.net/reference/option/buttons.buttons.enabled
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def buttons(self):
    return self.sub_data_enum('buttons', InnerButtons)

  @property
  def dom(self):
    return self.sub_data('dom', self.Dom)

  @property
  def name(self):
    """
    Description:
    -----------
    Set a name for the instance for the group selector.
    Related Pages:

      https://datatables.net/reference/option/buttons.name
    """
    return self._attrs['name']

  @name.setter
  def name(self, val):
    self._attrs['name'] = val