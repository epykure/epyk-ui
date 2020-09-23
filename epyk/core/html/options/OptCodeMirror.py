#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options
from epyk.core.js import Imports


class OptionsCode(Options):

  @property
  def value(self):
    """
    Description:
    ------------
    The starting value of the editor. Can be a string, or a document object.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(True)

  @value.setter
  def value(self, value):
    self._config(value)

  @property
  def mode(self):
    """
    Description:
    ------------
    The mode to use. When not given, this will default to the first mode that was loaded.
    It may be a string, which either simply names the mode or is a MIME type associated with the mode.

    add extra addon: /mode/javascript/javascript.js

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get("")

  @mode.setter
  def mode(self, value):
    Imports.extend('codemirror-%s' % value, [('%s.min.js' % value, 'codemirror/%%(version)s/mode/%s/' % value)], version="codemirror", required=["codemirror"])
    self._report.jsImports.add('codemirror-%s' % value)
    self._config(value)

  @property
  def lineSeparator(self):
    """
    Description:
    ------------
    Explicitly set the line separator for the editor.
    By default (value null), the document will be split on CRLFs as well as lone CRs and LFs, and a single LF will be used as line separator in all output (such as getValue).
    When a specific string is given, lines will only be split on that string, and output will, by default, use that same separator.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get()

  @lineSeparator.setter
  def lineSeparator(self, value):
    self._config(value)

  @property
  def gutters(self):
    """
    Description:
    ------------
    Can be used to add extra gutters (beyond or instead of the line number gutter).
    Should be an array of CSS class names or class name / CSS string pairs, each of which defines a width (and optionally a background), and which will be used to draw the background of the gutters.
    May include the CodeMirror-linenumbers class, in order to explicitly set the position of the line number gutter (it will default to be to the right of all other gutters).
    These class names are the keys passed to setGutterMarker.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get()

  @gutters.setter
  def gutters(self, value):
    self._config(value)

  @property
  def theme(self):
    """
    Description:
    ------------
    The theme to style the editor with.
    You must make sure the CSS file defining the corresponding .cm-s-[name] styles is loaded (see the theme directory in the distribution).
    The default is "default", for which colors are included in codemirror.css.
    It is possible to use multiple theming classes at once—for example "foo bar" will assign both the cm-s-foo and the cm-s-bar classes to the editor.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get()

  @theme.setter
  def theme(self, value):
    self._config(value)

  @property
  def indentUnit(self):
    """
    Description:
    ------------
    How many spaces a block (whatever that means in the edited language) should be indented. The default is 2.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(2)

  @indentUnit.setter
  def indentUnit(self, value):
    self._config(value)

  @property
  def smartIndent(self):
    """
    Description:
    ------------
    Whether to use the context-sensitive indentation that the mode provides (or just indent the same as the line before). Defaults to true.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(True)

  @smartIndent.setter
  def smartIndent(self, value):
    self._config(value)

  @property
  def tabSize(self):
    """
    Description:
    ------------
    The width of a tab character. Defaults to 4.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(4)

  @tabSize.setter
  def tabSize(self, value):
    self._config(value)

  @property
  def indentWithTabs(self):
    """
    Description:
    ------------
    Whether, when indenting, the first N*tabSize spaces should be replaced by N tabs. Default is false.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @indentWithTabs.setter
  def indentWithTabs(self, value):
    self._config(value)

  @property
  def electricChars(self):
    """
    Description:
    ------------
    Configures whether the editor should re-indent the current line when a character is typed that might change its proper indentation (only works if the mode supports indentation).
    Default is true.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(True)

  @electricChars.setter
  def electricChars(self, value):
    self._config(value)

  @property
  def direction(self):
    """
    Description:
    ------------
    Flips overall layout and selects base paragraph direction to be left-to-right or right-to-left.
    Default is "ltr". CodeMirror applies the Unicode Bidirectional Algorithm to each line, but does not autodetect base direction — it's set to the editor direction for all lines.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get("ltr")

  @direction.setter
  def direction(self, value):
    self._config(value)

  @property
  def rtlMoveVisually(self):
    """
    Description:
    ------------
    Determines whether horizontal cursor movement through right-to-left (Arabic, Hebrew) text is visual (pressing the left arrow moves the cursor left) or logical (pressing the left arrow moves to the next lower index in the string, which is visually right in right-to-left text). The default is false on Windows, and true on other platforms.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @rtlMoveVisually.setter
  def rtlMoveVisually(self, value):
    self._config(value)

  @property
  def keyMap(self):
    """
    Description:
    ------------
    Configures the key map to use. The default is "default", which is the only key map defined in codemirror.js itself.
    Extra key maps are found in the key map directory. See the section on key maps for more information.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get("default")

  @keyMap.setter
  def keyMap(self, value):
    self._config(value)

  @property
  def lineWrapping(self):
    """
    Description:
    ------------
    Whether CodeMirror should scroll or wrap for long lines. Defaults to false (scroll).

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @lineWrapping.setter
  def lineWrapping(self, value):
    self._config(value)

  @property
  def lineNumbers(self):
    """
    Description:
    ------------
    Whether to show line numbers to the left of the editor.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(True)

  @lineNumbers.setter
  def lineNumbers(self, value):
    self._config(value)

  @property
  def firstLineNumber(self):
    """
    Description:
    ------------
    At which number to start counting lines. Default is 1.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(1)

  @firstLineNumber.setter
  def firstLineNumber(self, value):
    self._config(value)

  @property
  def fixedGutter(self):
    """
    Description:
    ------------
    Determines whether the gutter scrolls along with the content horizontally (false) or whether it stays fixed during horizontal scrolling (true, the default).

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(True)

  @fixedGutter.setter
  def fixedGutter(self, value):
    self._config(value)

  @property
  def scrollbarStyle(self):
    """
    Description:
    ------------
    Chooses a scrollbar implementation. The default is "native", showing native scrollbars.
    The core library also provides the "null" style, which completely hides the scrollbars. Addons can implement additional scrollbar models.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get("native")

  @scrollbarStyle.setter
  def scrollbarStyle(self, value):
    self._config(value)

  @property
  def coverGutterNextToScrollbar(self):
    """
    Description:
    ------------
    When fixedGutter is on, and there is a horizontal scrollbar, by default the gutter will be visible to the left of this scrollbar.
    If this option is set to true, it will be covered by an element with class CodeMirror-gutter-filler.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @coverGutterNextToScrollbar.setter
  def coverGutterNextToScrollbar(self, value):
    self._config(value)

  @property
  def inputStyle(self):
    """
    Description:
    ------------
    Selects the way CodeMirror handles input and focus.
    he core library defines the "textarea" and "contenteditable" input models. On mobile browsers, the default is "contenteditable". On desktop browsers, the default is "textarea".

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get("textarea")

  @inputStyle.setter
  def inputStyle(self, value):
    self._config(value)

  @property
  def readOnly(self):
    """
    Description:
    ------------
    This disables editing of the editor content by the user. If the special value "nocursor" is given (instead of simply true), focusing of the editor is also disallowed.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @readOnly.setter
  def readOnly(self, value):
    self._config(value)

  @property
  def screenReaderLabel(self):
    """
    Description:
    ------------
    This label is read by the screenreaders when CodeMirror text area is focused. This is helpful for accessibility.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get("")

  @screenReaderLabel.setter
  def screenReaderLabel(self, value):
    self._config(value)

  @property
  def showCursorWhenSelecting(self):
    """
    Description:
    ------------
    Whether the cursor should be drawn when a selection is active. Defaults to false.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @showCursorWhenSelecting.setter
  def showCursorWhenSelecting(self, value):
    self._config(value)

  @property
  def lineWiseCopyCut(self):
    """
    Description:
    ------------
    When enabled, which is the default, doing copy or cut when there is no selection will copy or cut the whole lines that have cursors on them.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(True)

  @lineWiseCopyCut.setter
  def lineWiseCopyCut(self, value):
    self._config(value)

  @property
  def pasteLinesPerSelection(self):
    """
    Description:
    ------------
    When pasting something from an external source (not from the editor itself), if the number of lines matches the number of selection,
    CodeMirror will by default insert one line per selection. You can set this to false to disable that behavior.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @pasteLinesPerSelection.setter
  def pasteLinesPerSelection(self, value):
    self._config(value)

  @property
  def selectionsMayTouch(self):
    """
    Description:
    ------------
    Determines whether multiple selections are joined as soon as they touch (the default) or only when they overlap (true).

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(True)

  @selectionsMayTouch.setter
  def selectionsMayTouch(self, value):
    self._config(value)

  @property
  def historyEventDelay(self):
    """
    Description:
    ------------
    The period of inactivity (in milliseconds) that will cause a new history event to be started when typing or deleting. Defaults to 1250.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(1250)

  @historyEventDelay.setter
  def historyEventDelay(self, value):
    self._config(value)

  @property
  def tabindex(self):
    """
    Description:
    ------------
    The tab index to assign to the editor. If not given, no tab index will be assigned.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get()

  @tabindex.setter
  def tabindex(self, value):
    self._config(value)

  @property
  def autofocus(self):
    """
    Description:
    ------------
    Can be used to make CodeMirror focus itself on initialization. Defaults to off.
    When fromTextArea is used, and no explicit value is given for this option, it will be set to true when either the source textarea is focused, or it has an autofocus attribute and no other element is focused.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @autofocus.setter
  def autofocus(self, value):
    self._config(value)

  @property
  def dragDrop(self):
    """
    Description:
    ------------
    Controls whether drag-and-drop is enabled. On by default.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(True)

  @dragDrop.setter
  def dragDrop(self, value):
    self._config(value)

  @property
  def cursorBlinkRate(self):
    """
    Description:
    ------------
    Half-period in milliseconds used for cursor blinking.
    The default blink rate is 530ms. By setting this to zero, blinking can be disabled. A negative value hides the cursor entirely.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(530)

  @cursorBlinkRate.setter
  def cursorBlinkRate(self, value):
    self._config(value)

  @property
  def cursorScrollMargin(self):
    """
    Description:
    ------------
    How much extra space to always keep above and below the cursor when approaching the top or bottom of the visible view in a scrollable document. Default is 0.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(0)

  @cursorScrollMargin.setter
  def cursorScrollMargin(self, value):
    self._config(value)

  @property
  def cursorHeight(self):
    """
    Description:
    ------------
    Determines the height of the cursor. Default is 1, meaning it spans the whole height of the line.
    For some fonts (and by some tastes) a smaller height (for example 0.85), which causes the cursor to not reach all the way to the bottom of the line, looks better

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(1)

  @cursorHeight.setter
  def cursorHeight(self, value):
    self._config(value)

  @property
  def matchBrackets(self):
    """
    Description:
    ------------
    Defines an option matchBrackets which, when set to true or an options object, causes matching brackets to be highlighted whenever the cursor is next to them.
    It also adds a method matchBrackets that forces this to happen once, and a method findMatchingBracket that can be used to run the bracket-finding algorithm that this uses internally.
    It takes a start position and an optional config object.
    By default, it will find the match to a matchable character either before or after the cursor (preferring the one before), but you can control its behavior with these options:

    Add extra addon: addon/selection/active-line.js

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @matchBrackets.setter
  def matchBrackets(self, value): # matchbrackets.js
    Imports.extend('codemirror-matchbrackets', [('matchbrackets.min.js', 'codemirror/%(version)s/addon/edit/')], version="codemirror", required=["codemirror"])
    self._report.jsImports.add('codemirror-matchbrackets')
    self._config(value)

  @property
  def styleActiveLine(self):
    """
    Description:
    ------------
    Defines a styleActiveLine option that, when enabled, gives the wrapper of the line that contains the cursor the class CodeMirror-activeline, adds a background with the class CodeMirror-activeline-background, and adds the class CodeMirror-activeline-gutter to the line's gutter space is enabled.

    Add extra addon: addon/edit/matchbrackets.js

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(False)

  @styleActiveLine.setter
  def styleActiveLine(self, value):
    Imports.extend('codemirror-active-line', [('active-line.min.js', 'codemirror/%(version)s/addon/selection/')], version="codemirror", required=["codemirror"])
    self._report.jsImports.add('codemirror-active-line')
    self._config(value)
