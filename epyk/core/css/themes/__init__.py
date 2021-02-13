from . import ThemeDark as darks
from . import ThemeRed as reds
from . import ThemeGreen as greens
from . import ThemeBlue as blues


DIV_STYLE = '<div style="display:block;background-color:%s;width:20px;height:18px;margin-top:3px !IMPORTANT;border:1px solid black;margin:auto;vertical-align:middle">&nbsp;</div>'

REGISTERED_THEMES = [
  {"value": 'Theme.ThemeDefault', 'name': '', 'content': DIV_STYLE % '#1b5e20'},
  {"value": 'ThemeBlue.Blue', 'name': '', 'content': DIV_STYLE % '#0d47a1'},
  {"value": 'ThemeBlue.BlueGrey', 'name': '', 'content': DIV_STYLE % '#263238'},
  {"value": 'ThemeBlue.LightBlue', 'name': '', 'content': DIV_STYLE % '#01579B'},
  {"value": 'ThemeDark.Dark', 'name': '', 'content': DIV_STYLE % '#eceff1'},
  {"value": 'ThemeDark.Grey', 'name': '', 'content': DIV_STYLE % '#eceff1'},
  {"value": 'ThemeGreen.Green', 'name': '', 'content': DIV_STYLE % '#1b5e20'},
  {"value": 'ThemeGreen.Teal', 'name': '', 'content': DIV_STYLE % '#004D40'},
  {"value": 'ThemeGreen.LightGreen', 'name': '', 'content': DIV_STYLE % '#33691E'},
  {"value": 'ThemeRed.Red', 'name': '', 'content': DIV_STYLE % '#B71C1C'},
  {"value": 'ThemeRed.Pink', 'name': '', 'content': DIV_STYLE % '#d598a3'},
]