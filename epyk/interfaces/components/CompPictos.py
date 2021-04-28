#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html import graph
from epyk.interfaces import Arguments


class Pictogram:

  def __init__(self, ui):
    self.page = ui.page

  def path(self, path, fill=None, stroke=None, width=(33, "px"), height=(25, "px"), viewbox=(150, 100), options=None,
           profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param path:
    :param fill:
    :param stroke:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param viewbox:
    :param options:
    :param profile:
    """
    x, y = path.split(",", 1)
    width = Arguments.size(width, unit='px')
    height = Arguments.size(height, unit="px")
    html_svg = graph.GraphSvg.SVG(self.page, width=(viewbox[0], "px"), height=(viewbox[1], "px"))
    html_svg.style.css.width = width[0]
    html_svg.style.css.height = height[0]
    html_svg.path(fill=fill or self.page.theme.greys[-1], stroke=stroke, x=x[1:] if x.startswith("M") else x, y=y)
    return html_svg

  def paths(self, paths, fill=None, stroke=None, width=(33, "px"), height=(25, "px"), viewbox=(150, 100)):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param paths:
    :param fill:
    :param stroke:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param viewbox:
    """
    width = Arguments.size(width, unit='px')
    height = Arguments.size(height, unit="px")
    html_svg = graph.GraphSvg.SVG(self.page, width=(viewbox[0], "px"), height=(viewbox[1], "px"))
    html_svg.style.css.width = width[0]
    html_svg.style.css.height = height[0]
    for path in paths:
      x, y = path.split(",", 1)
      html_svg.path(fill=fill or self.page.theme.greys[-1], stroke=stroke, x=x[1:] if x.startswith("M") else x, y=y)
    return html_svg

  def arrow(self, width=(21, "px"), height=(12, "px")):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    html_svg = graph.GraphSvg.SVG(self.page, width=width, height=height)
    html_svg.style.css.width = 21
    html_svg.style.css.height = 12
    html_svg.path(fill="rgb(0, 117, 235)", x=0.0917969,
             y="5.84215C0.0917969 5.42793 0.427583 5.09215 0.841797 5.09215H18.8418C19.256 5.09215 19.5918 5.42793 19.5918 5.84215C19.5918 6.25636 19.256 6.59215 18.8418 6.59215H0.841797C0.427583 6.59215 0.0917969 6.25636 0.0917969 5.84215Z")
    html_svg.path(fill="rgb(0, 117, 235)", x=14.2706,
             y="0.315129C14.5635 0.0222357 15.0384 0.0222357 15.3313 0.315129L20.1313 5.11513C20.2719 5.25578 20.351 5.44655 20.351 5.64546C20.351 5.84437 20.2719 6.03514 20.1313 6.17579L15.3313 10.9758C15.0384 11.2687 14.5635 11.2687 14.2706 10.9758C13.9777 10.6829 13.9777 10.208 14.2706 9.91513L18.5403 5.64546L14.2706 1.37579C13.9777 1.0829 13.9777 0.608022 14.2706 0.315129Z")
    html_svg.style.hover({"margin-left": '4px'})
    return html_svg

  def flam(self, width=(619, "px"), height=(423, "px")):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    html_svg = graph.GraphSvg.SVG(self.page, width=(619, "px"), height=(423, "px"))
    html_svg.style.css.width = 200
    html_svg.style.css.height = 100
    html_svg.path(fill="red", x=31.5, y="49.6C55 41.5 59 20.4 56 1c0-.7.6-1.2 1.2-1C79.7 11 105 35 105 71c0 27.6-21.4 52-52.5 52a50 50 0 0 1-28.2-92.7c.6-.4 1.4 0 1.4.7.3 3.7 1.3 13 5.4 18.6h.4z")
    return html_svg

  def gout(self):
    """"""
    svg = graph.GraphSvg.SVG(self.page, width=(1199.96, "px"), height=(1014.39, "px"))
    svg.style.css.width = 33
    svg.style.css.height = 33
    svg.path(fill='#2dbeff', x=531.96,
             y="418l4-21c-69.8-47.6-157.2-69.3-247-54l54.4-308.4L146.66 0c-17.5 38.4-96.5 218.6-130.7 418-27.5 159.8-26.2 332 58.5 453 18.2 26 40.2 49.7 66.7 70.4 77 60.3 170.2 83.8 261 68.4 83.4-14 154.4-57.7 204.3-118.2-5.5-6.7-10.8-13.6-15.7-20.7-85-121.2-86-293.3-58.7-453z")

    return svg

  def team(self, fill=None, border=None, width=(50, "px"), height=(30, "px")):
    """
    Description:
    ------------

    Usage::

    Related Pages:

      https://uxwing.com/business-team-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    svg = self.path(fill=fill, stroke=border, width=width, height=height, viewbox=(150, 80),
                    path="M91.95,64.68l1.99-7.59l-1.37-1.5c-0.62-0.9-0.75-1.69-0.41-2.37c0.74-1.47,2.28-1.2,3.72-1.2 c1.51,0,3.37-0.29,3.84,1.6c0.16,0.63-0.04,1.29-0.48,1.97l-1.37,1.5l1.19,4.56l7.89-6.86l4.09,0.1c-1.41-2.83-3.2-5.23-5.28-7.49 c3.92,1.52,7.93,3.02,10.9,4.88c1.89,1.18,2.86,2.08,3.63,3.51c1.62,3.05,1.8,5.78,2.04,9.08l0.57,2.86h-22.24l0.02,0.07h-8.51 c-0.19,1.95-1.31,3.08-3.5,3.24H61.68H34.24c-2.2-0.17-3.32-1.3-3.5-3.27l0.76-12.04c0.21-2.78,0.99-4.98,2.26-6.66 c0.84-1.11,1.88-1.93,3.03-2.57c3.65-2.03,12.17-2.63,15.48-5.61l5.07,14.91l2.55-8.85l-1.25-1.37c-0.56-0.82-0.69-1.54-0.37-2.16 c0.68-1.34,2.08-1.09,3.39-1.09c1.37,0,3.06-0.26,3.49,1.46c0.14,0.57-0.04,1.17-0.44,1.79l-1.25,1.37l2.55,8.85l4.59-14.91 c3.31,2.98,11.84,3.58,15.48,5.61c1.15,0.64,2.2,1.46,3.03,2.57c1.27,1.68,2.05,3.87,2.26,6.66L91.95,64.68L91.95,64.68z M15.29,48.25l3.4,9.99l1.71-5.93l-0.84-0.92c-0.38-0.55-0.46-1.03-0.25-1.45c0.45-0.9,1.39-0.73,2.27-0.73 c0.92,0,2.05-0.17,2.34,0.98c0.1,0.38-0.03,0.79-0.29,1.2l-0.84,0.92l1.71,5.93l3.08-9.99c0.45,0.4,1.07,0.74,1.8,1.03 c-0.25,0.53-0.48,1.09-0.68,1.67c-0.52,1.51-0.86,3.19-1,5.06l0.01,0c0,0.04-0.01,0.09-0.01,0.13l-0.74,11.58h-5.35H2.35 C0.87,67.61,0.12,66.85,0,65.53l0.51-7.34c0.14-1.86,0.67-3.33,1.52-4.46c0.56-0.74,1.26-1.29,2.03-1.72 C6.5,50.65,13.07,50.25,15.29,48.25L15.29,48.25z M13.62,34.09c-0.33,0.03-0.58,0.1-0.76,0.22c-0.1,0.07-0.18,0.16-0.23,0.26 c-0.06,0.12-0.08,0.28-0.08,0.45c0.02,0.55,0.31,1.29,0.88,2.14l0.01,0.02l0,0l1.9,3.02c0.76,1.2,1.55,2.43,2.53,3.33 c0.93,0.85,2.06,1.43,3.56,1.43c1.62,0,2.8-0.6,3.77-1.5c1.01-0.95,1.81-2.25,2.6-3.55l2.13-3.51c0.43-0.98,0.56-1.57,0.42-1.85 c-0.09-0.17-0.44-0.22-1.02-0.17c-0.37,0.08-0.76,0.01-1.17-0.2l1.07-3.2c-3.91-0.05-6.58-0.73-9.75-2.75 c-1.04-0.66-1.35-1.42-2.39-1.35c-0.79,0.15-1.45,0.5-1.97,1.07c-0.5,0.54-0.88,1.28-1.13,2.23l0.63,3.83 C14.3,34.21,13.96,34.23,13.62,34.09L13.62,34.09z M30.55,33.14c0.46,0.14,0.8,0.4,1,0.81c0.32,0.65,0.2,1.62-0.41,3l0,0 c-0.01,0.03-0.02,0.05-0.04,0.08l-2.16,3.56c-0.84,1.38-1.69,2.76-2.83,3.83c-1.19,1.12-2.66,1.86-4.67,1.85 c-1.88,0-3.29-0.72-4.45-1.78c-1.11-1.02-1.96-2.32-2.76-3.6l-1.9-3.02c-0.71-1.06-1.07-2.02-1.1-2.82 c-0.01-0.39,0.05-0.74,0.2-1.04c0.15-0.33,0.38-0.6,0.7-0.81c0.15-0.1,0.33-0.19,0.52-0.26c-0.12-1.62-0.16-3.62-0.08-5.3 c0.04-0.41,0.12-0.82,0.23-1.23c0.49-1.73,1.7-3.13,3.21-4.09c0.53-0.34,1.11-0.62,1.73-0.84c3.65-1.32,8.48-0.6,11.07,2.2 c1.05,1.14,1.72,2.65,1.86,4.65L30.55,33.14L30.55,33.14z M49.65,19.77c-0.42,0.05-0.75,0.16-0.99,0.32 c-0.15,0.1-0.27,0.24-0.34,0.39c-0.08,0.18-0.12,0.41-0.12,0.67c0.02,0.83,0.46,1.92,1.32,3.18l0.02,0.02h0l2.83,4.51 c1.13,1.8,2.31,3.63,3.77,4.96c1.39,1.27,3.08,2.13,5.3,2.14c2.42,0.01,4.18-0.89,5.62-2.23c1.51-1.41,2.71-3.36,3.89-5.3 l3.18-5.24c0.64-1.46,0.84-2.34,0.63-2.76c-0.13-0.27-0.69-0.33-1.63-0.24c-0.07,0.01-0.14,0.01-0.21,0c-0.39,0-0.81-0.1-1.27-0.31 l1.43-4.78c-5.84-0.07-9.83-1.09-14.55-4.11c-1.55-0.99-2.02-2.12-3.57-2.01c-1.17,0.23-2.16,0.75-2.94,1.59 c-0.75,0.81-1.32,1.91-1.69,3.32l1.01,5.78C50.74,19.98,50.18,20,49.65,19.77L49.65,19.77z M75.05,18.34 c0.69,0.2,1.19,0.6,1.5,1.21c0.48,0.98,0.3,2.42-0.61,4.48l0,0c-0.02,0.04-0.04,0.08-0.06,0.11l-3.23,5.32 c-1.25,2.06-2.52,4.13-4.23,5.72c-1.78,1.67-3.97,2.78-6.97,2.77c-2.8-0.01-4.91-1.08-6.64-2.66c-1.66-1.52-2.92-3.46-4.12-5.37 l-2.83-4.51c-1.05-1.57-1.6-3.02-1.64-4.21c-0.02-0.58,0.08-1.1,0.3-1.56c0.23-0.49,0.57-0.9,1.04-1.21 c0.23-0.16,0.49-0.29,0.78-0.39c-0.17-2.41-0.23-5.39-0.12-7.9c0.06-0.61,0.18-1.22,0.35-1.83c0.72-2.59,2.54-4.67,4.79-6.1 c0.79-0.5,1.66-0.92,2.58-1.25c5.44-1.97,12.66-0.89,16.52,3.29c1.57,1.7,2.56,3.96,2.77,6.94L75.05,18.34L75.05,18.34z M84.88,42.96l2.5-0.07l2.07-0.05c-2.42-7.45-1.61-14.3,4.22-20.12c0.99,3.2,3.2,5.83,6.97,7.78c1.8,1.34,3.55,2.96,5.23,4.81 c0.3-1.23-0.84-2.73-2.23-4.27c1.28,0.63,2.46,1.52,3.29,3.22c0.97,1.98,0.95,3.64,0.64,5.79c-0.15,1-0.39,1.93-0.74,2.78h3.45 c3.64-7.79,1.33-19.34-6.11-24.24c-2.28-1.5-3.92-1.45-6.6-1.44c-3.07,0-4.63,0.1-7.26,1.83c-3.87,2.56-6.25,6.99-7.25,13.14 C82.87,35.19,82.74,40.49,84.88,42.96L84.88,42.96z"
    )
    return svg

  def tick(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Description:
    ------------

    Usage::

    Related Pages:

      https://uxwing.com/check-mark-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    svg = self.path(fill=fill or self.page.theme.success[-1], stroke=border, width=width, height=height,
                    path="M4.43,63.63c-2.869-2.755-4.352-6.42-4.427-10.11c-0.074-3.689,1.261-7.412,4.015-10.281 c2.752-2.867,6.417-4.351,10.106-4.425c3.691-0.076,7.412,1.255,10.283,4.012l24.787,23.851L98.543,3.989l1.768,1.349l-1.77-1.355 c0.141-0.183,0.301-0.339,0.479-0.466c2.936-2.543,6.621-3.691,10.223-3.495V0.018l0.176,0.016c3.623,0.24,7.162,1.85,9.775,4.766 c2.658,2.965,3.863,6.731,3.662,10.412h0.004l-0.016,0.176c-0.236,3.558-1.791,7.035-4.609,9.632l-59.224,72.09l0.004,0.004 c-0.111,0.141-0.236,0.262-0.372,0.368c-2.773,2.435-6.275,3.629-9.757,3.569c-3.511-0.061-7.015-1.396-9.741-4.016L4.43,63.63 L4.43,63.63z"
    )
    return svg

  def quote(self, fill=None, border=None, width=(33, "px"), height=(25, "px")):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    svg = self.path(fill=fill, stroke=border, width=width, height=height,
                    path="M106.97,92.81H84.89c-8.5,0-15.45-6.95-15.45-15.45c0-31.79-8.12-66.71,30.84-76.68 c17.65-4.51,22.25,14.93,3.48,16.27c-11.45,0.82-13.69,8.22-14.04,19.4h17.71c8.5,0,15.45,6.95,15.45,15.45v25.09 C122.88,85.65,115.72,92.81,106.97,92.81L106.97,92.81z M38.23,92.81H16.15c-8.5,0-15.45-6.95-15.45-15.45 c0-31.79-8.12-66.71,30.84-76.68C49.2-3.84,53.8,15.6,35.02,16.95c-11.45,0.82-13.69,8.22-14.04,19.4H38.7 c8.5,0,15.45,6.95,15.45,15.45v25.09C54.14,85.65,46.98,92.81,38.23,92.81L38.23,92.81z"
    )
    return svg

  def stack(self, fill=None, border=None, width=(33, "px"), height=(25, "px")):
    """
    Description:
    ------------

    Usage::

    Related Pages:

      https://uxwing.com/stack-icon/

    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    svg = self.path(fill=fill, stroke=border, width=width, height=height,
      path='M61.15,0L0,26.52l61.41,24.96l61.47-24.88L61.15,0L61.15,0z M122.88,57.12L95.46,45.31L62.73,58.56 c-0.88,0.36-1.83,0.33-2.65,0L27.27,45.22L0,57.05L61.41,82L122.88,57.12L122.88,57.12z M96.14,75.56L62.73,89.08 c-0.88,0.36-1.83,0.33-2.65,0L26.59,75.47L0,87.01l61.41,24.96l61.47-24.88L96.14,75.56L96.14,75.56z')
    return svg

  def faq(self, fill=None, border=None, width=(33, "px"), height=(25, "px")):
    """
    Description:
    ------------

    Usage::

    Related Pages:

      https://uxwing.com/faq-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    svg = self.path(fill=fill, stroke=border, width=width, height=height,
      path='M45.44,0H15.95c-4.4,0-8.17,1.55-11.3,4.65C1.51,7.75,0,11.52,0,15.95v28c0,4.44,1.55,8.21,4.65,11.3 c3.1,3.1,6.87,4.65,11.3,4.65h13.11c-0.92,3.52-2.04,6.87-3.45,10c-1.37,3.17-3.73,6.2-6.97,9.09c6.23-1.62,11.76-4.05,16.66-7.25 c4.86-3.17,9.09-7.15,12.57-11.83h10.56c4.4,0,8.17-1.58,11.3-4.65c3.13-3.1,4.65-6.87,4.65-11.3v-28c0-4.4-1.55-8.17-4.65-11.3 C66.64,1.51,62.87,0,58.43,0H45.44L45.44,0z M98.04,56.71h-9.34l-1.34,4.16h-8.41l10.04-25.22h9.02l9.99,25.22h-8.63L98.04,56.71 L98.04,56.71z M96.3,51.25l-2.91-9.06l-2.92,9.06H96.3L96.3,51.25z M48.41,37.7c1.09,0.72,1.81,1.18,2.14,1.36 c0.5,0.27,1.18,0.58,2.02,0.94l-2.43,4.65c-1.22-0.56-2.44-1.23-3.64-2c-1.2-0.78-2.04-1.36-2.52-1.74 c-1.94,0.79-4.37,1.19-7.29,1.19c-4.32,0-7.73-1.06-10.22-3.19c-2.95-2.51-4.42-6.05-4.42-10.6c0-4.42,1.29-7.86,3.87-10.31 c2.58-2.45,6.18-3.67,10.81-3.67c4.72,0,8.35,1.19,10.92,3.59c2.57,2.39,3.85,5.82,3.85,10.27C51.5,32.14,50.47,35.31,48.41,37.7 L48.41,37.7z M41.68,33.44c0.7-1.18,1.05-2.95,1.05-5.31c0-2.71-0.54-4.64-1.6-5.8c-1.07-1.16-2.54-1.74-4.42-1.74 c-1.75,0-3.17,0.59-4.25,1.78c-1.09,1.18-1.63,3.03-1.63,5.55c0,2.93,0.53,4.99,1.59,6.17c1.06,1.18,2.52,1.78,4.37,1.78 c0.6,0,1.16-0.06,1.69-0.16c-0.74-0.68-1.9-1.31-3.5-1.91l1.38-2.98c0.78,0.13,1.39,0.3,1.82,0.49c0.44,0.19,1.28,0.71,2.55,1.54 C41.01,33.03,41.33,33.23,41.68,33.44L41.68,33.44z M122.88,32.15v28c0,2.54-0.46,4.93-1.37,7.15c-0.92,2.22-2.25,4.23-4.09,6.02 c-0.77,0.77-1.62,1.48-2.46,2.08c-0.88,0.63-1.8,1.16-2.71,1.62c-0.04,0.04-0.11,0.04-0.14,0.07c-1.2,0.56-2.43,0.95-3.7,1.23 c-1.34,0.28-2.71,0.42-4.12,0.42H90.79c0.18,0.56,0.35,1.13,0.56,1.69c0.53,1.55,1.16,3.1,1.83,4.61v0.04 c0.6,1.41,1.44,2.75,2.47,4.09c1.06,1.37,2.32,2.71,3.84,4.09c1.09,0.95,1.2,2.61,0.21,3.7c-0.67,0.77-1.69,1.06-2.61,0.81 c-3.24-0.85-6.34-1.9-9.23-3.17c-2.89-1.27-5.63-2.75-8.21-4.44c-2.54-1.66-4.93-3.56-7.15-5.63c-1.87-1.76-3.63-3.7-5.28-5.74 h-9.23c-1.73,0-3.42-0.21-5-0.63c-1.58-0.42-3.1-1.09-4.54-1.97c-1.23-0.74-1.62-2.36-0.88-3.59c0.74-1.23,2.36-1.62,3.59-0.88 c0.99,0.6,2.04,1.06,3.2,1.37c1.13,0.32,2.36,0.46,3.63,0.46h10.53c0.81,0,1.58,0.35,2.11,1.06c1.66,2.22,3.49,4.26,5.49,6.13 c1.97,1.87,4.12,3.56,6.44,5.07c2.22,1.44,4.58,2.75,7.08,3.87c-0.49-0.81-0.88-1.62-1.27-2.43c-0.7-1.62-1.37-3.28-1.97-5.04 c-0.56-1.66-1.09-3.38-1.55-5.11c-0.11-0.28-0.14-0.6-0.14-0.92c0-1.44,1.16-2.64,2.64-2.64h16.94c1.06,0,2.04-0.11,2.99-0.32 c0.92-0.21,1.76-0.49,2.57-0.85c0.04-0.04,0.07-0.04,0.11-0.07c0.67-0.32,1.34-0.7,1.94-1.13c0.63-0.46,1.23-0.95,1.8-1.55 c1.3-1.3,2.29-2.75,2.92-4.3c0.63-1.55,0.95-3.28,0.95-5.14v-28c0-1.87-0.32-3.59-0.95-5.14c-0.63-1.55-1.62-2.99-2.92-4.3 c-1.3-1.3-2.75-2.29-4.3-2.92c-1.55-0.63-3.28-0.95-5.14-0.95H86.57c-1.44,0-2.64-1.16-2.64-2.64c0-1.44,1.16-2.64,2.64-2.64h17.72 c2.54,0,4.9,0.46,7.11,1.37c2.22,0.92,4.19,2.25,6.02,4.05c1.8,1.8,3.17,3.8,4.05,6.02c0.92,2.22,1.37,4.58,1.37,7.11H122.88 L122.88,32.15z')
    return svg

  def compass(self, fill=None, border=None, width=(33, "px"), height=(25, "px")):
    """
    Description:
    ------------

    Usage::

    Related Pages:

      https://uxwing.com/compass-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    svg = self.path(fill=fill, stroke=border, width=width, height=height,
      path='M76.7,57.5l-7.08,4.03c-0.03,0.52-0.12,1.04-0.25,1.54c-1.11,4.16-5.39,6.63-9.55,5.52 c-0.53-0.14-1.05-0.35-1.55-0.6l-7.51,4.27l30.26,22.29L76.7,57.5L76.7,57.5L76.7,57.5z M61.44,0c33.93,0,61.44,27.51,61.44,61.44 c0,33.93-27.51,61.44-61.44,61.44C27.51,122.88,0,95.36,0,61.44C0,27.51,27.51,0,61.44,0L61.44,0z M61.44,16.07 c25.05,0,45.37,20.32,45.37,45.37c0,25.05-20.32,45.37-45.37,45.37S16.07,86.49,16.07,61.44C16.07,36.39,36.39,16.07,61.44,16.07 L61.44,16.07z M46.85,65.79l7.21-4.1c-0.07-0.87,0-1.77,0.24-2.66c1.11-4.16,5.39-6.63,9.55-5.52c0.9,0.24,1.75,0.64,2.5,1.18 l6.43-3.66L42.53,28.75L46.85,65.79L46.85,65.79L46.85,65.79z')
    return svg

  def people(self, fill=None, border=None, width=(20, "px"), height=(48, "px")):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    """
    svg = self.paths(fill=fill, stroke=border, width=width, height=height, viewbox=(120, 100),
      paths=[
        'M77.223915,64.271744c10.880661,0 19.702522,-8.821869 19.702522,-19.703056c0,-10.880646 -8.821861,-19.702026 -19.702522,-19.702026c-10.881134,0 -19.702042,8.821381 -19.702042,19.702026c0,10.881187 8.820908,19.703056 19.702042,19.703056z',
        'M57.105,68.620438c-13.952663,0 -25.172991,11.379044 -25.172991,25.572006l0,60.49231c0,11.760712 17.211897,11.760712 17.211897,0l0,-55.313736l4.074154,0l0,151.457321c0,15.723877 22.919765,15.261169 22.919765,0l0,-87.91954l3.947754,0l0,87.91954c0,15.261169 23.046173,15.723877 23.046173,0l0,-151.457321l3.979103,0l0,55.313736c0,11.850937 17.122147,11.850937 17.090775,0l0,-60.130432c0,-13.08757 -10.163177,-25.906876 -25.482269,-25.906876l-41.614361,-0.027008z'
      ])
    return svg
