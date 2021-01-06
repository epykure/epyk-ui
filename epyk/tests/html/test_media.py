
from epyk.core.Page import Report
from epyk.core.html import HtmlMedia

import inspect


def test_modules():
  """
  Check the list of modules in the package.
  """
  modules = ("Audio", "Media", "Youtube", "Source")
  for name, obj in inspect.getmembers(HtmlMedia):  # what do I do here?
    if inspect.isclass(obj):
      assert(obj.__name__ in modules)


def test_audio():
  """

  """
  page = Report()
  audio = page.ui.media.audio()
  assert(str(audio).startswith("<audio"))


def test_audio_mp3():
  """

  """
  page = Report()
  audio = page.ui.media.audio("test.mp3")
  return audio


print(test_audio_mp3())
