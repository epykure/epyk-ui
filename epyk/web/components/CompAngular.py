
from epyk.core.html import Html


class Router(Html.Html):
  name = 'router'

  def __str__(self):
    return "<router-outlet></router-outlet>"
