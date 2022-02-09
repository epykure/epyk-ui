
from epyk.core.html.options import Options


class OptionsSortable(Options):

  @property
  def group(self):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get()

  @group.setter
  def group(self, name: str):
    self.set(name)

  @property
  def sort(self):
    """
    Description:
    ------------
    sorting inside list

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(True)

  @sort.setter
  def sort(self, flag: bool):
    self.set(flag)

  @property
  def delay(self):
    """
    Description:
    ------------
    Time in milliseconds to define when the sorting should start

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(0)

  @delay.setter
  def delay(self, num: int):
    self.set(num)

  @property
  def delayOnTouchOnly(self):
    """
    Description:
    ------------
    Only delay if user is using touch

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(False)

  @delayOnTouchOnly.setter
  def delayOnTouchOnly(self, flag: bool):
    self.set(flag)

  @property
  def touchStartThreshold(self):
    """
    Description:
    ------------
    px, how many pixels the point should move before cancelling a delayed drag event

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(0)

  @touchStartThreshold.setter
  def touchStartThreshold(self, num: float):
    self.set(num)

  @property
  def disabled(self):
    """
    Description:
    ------------
    Disables the sortable if set to true.

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(False)

  @disabled.setter
  def disabled(self, flag: bool):
    self.set(flag)

  @property
  def store(self):
    """
    Description:
    ------------
    Disables the sortable if set to true.

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(None)

  @store.setter
  def store(self, flag: bool):
    self.set(flag)

  @property
  def animation(self):
    """
    Description:
    ------------
    ms, animation speed moving items when sorting, `0` — without animation

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(150)

  @animation.setter
  def animation(self, num: int):
    self.set(num)

  @property
  def easing(self):
    """
    Description:
    ------------
    Easing for animation. Defaults to null. See https://easings.net/ for examples.

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get("cubic-bezier(1, 0, 0, 1)")

  @easing.setter
  def easing(self, val):
    self.set(val)

  @property
  def handle(self):
    """
    Description:
    ------------
    Drag handle selector within list items

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(".my-handle")

  @handle.setter
  def handle(self, val):
    self.set(val)

  @property
  def filter(self):
    """
    Description:
    ------------
    Selectors that do not lead to dragging (String or Function)

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(".ignore-elements")

  @filter.setter
  def filter(self, val):
    self.set(val)

  @property
  def preventOnFilter(self):
    """
    Description:
    ------------
    Call `event.preventDefault()` when triggered `filter`

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(True)

  @preventOnFilter.setter
  def preventOnFilter(self, flag: bool):
    self.set(flag)

  @property
  def draggable(self):
    """
    Description:
    ------------
    Specifies which items inside the element should be draggable

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(".item")

  @draggable.setter
  def draggable(self, val):
    self.set(val)

  @property
  def dataIdAttr(self):
    """
    Description:
    ------------
    Specifies which items inside the element should be draggable

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get("data-id")

  @dataIdAttr.setter
  def dataIdAttr(self, val):
    self.set(val)

  @property
  def ghostClass(self):
    """
    Description:
    ------------
    Class name for the drop placeholder

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get("sortable-ghost")

  @ghostClass.setter
  def ghostClass(self, val: str):
    self.set(val)

  @property
  def chosenClass(self):
    """
    Description:
    ------------
    Class name for the chosen item

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get("sortable-chosen")

  @chosenClass.setter
  def chosenClass(self, val: str):
    self.set(val)

  @property
  def dragClass(self):
    """
    Description:
    ------------
    Class name for the dragging item

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get("sortable-drag")

  @dragClass.setter
  def dragClass(self, val: str):
    self.set(val)

  @property
  def swapThreshold(self):
    """
    Description:
    ------------
    Threshold of the swap zone

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(1)

  @swapThreshold.setter
  def swapThreshold(self, val):
    self.set(val)

  @property
  def invertSwap(self):
    """
    Description:
    ------------
    Will always use inverted swap zone if set to true

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(False)

  @invertSwap.setter
  def invertSwap(self, val):
    self.set(val)

  @property
  def invertedSwapThreshold(self):
    """
    Description:
    ------------
    Threshold of the inverted swap zone (will be set to swapThreshold value by default)

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(1)

  @invertedSwapThreshold.setter
  def invertedSwapThreshold(self, val):
    self.set(val)

  @property
  def direction(self):
    """
    Description:
    ------------
    Direction that the Sortable should sort in. Can be set to 'vertical', 'horizontal', or a function,
    which will be called whenever a target is dragged over.
    Must return 'vertical' or 'horizontal'.

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get('horizontal')

  @direction.setter
  def direction(self, val):
    self.set(val)

  @property
  def forceFallback(self):
    """
    Description:
    ------------
    ignore the HTML5 DnD behaviour and force the fallback to kick in

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(False)

  @forceFallback.setter
  def forceFallback(self, val: bool):
    self.set(val)

  @property
  def fallbackClass(self):
    """
    Description:
    ------------
    Class name for the cloned DOM Element when using forceFallback

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get("sortable-fallback")

  @fallbackClass.setter
  def fallbackClass(self, val):
    self.set(val)

  @property
  def fallbackOnBody(self):
    """
    Description:
    ------------
    Appends the cloned DOM Element into the Document's Body

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(False)

  @fallbackOnBody.setter
  def fallbackOnBody(self, val):
    self.set(val)

  @property
  def fallbackTolerance(self):
    """
    Description:
    ------------
    Specify in pixels how far the mouse should move before it's considered as a drag.

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(0)

  @fallbackTolerance.setter
  def fallbackTolerance(self, val):
    self.set(val)

  @property
  def dragoverBubble(self):
    """
    Description:
    ------------
    Specify in pixels how far the mouse should move before it's considered as a drag.

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(False)

  @dragoverBubble.setter
  def dragoverBubble(self, flag: bool):
    self.set(flag)

  @property
  def removeCloneOnHide(self):
    """
    Description:
    ------------
    Remove the clone element when it is not showing, rather than just hiding it

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(True)

  @removeCloneOnHide.setter
  def removeCloneOnHide(self, flag: bool):
    self.set(flag)

  @property
  def emptyInsertThreshold(self):
    """
    Description:
    ------------
    px, distance mouse must be from empty sortable to insert drag element into it

    Related Pages:

      https://github.com/SortableJS/Sortable
    """
    return self.get(5)

  @emptyInsertThreshold.setter
  def emptyInsertThreshold(self, flag: bool):
    self.set(flag)

