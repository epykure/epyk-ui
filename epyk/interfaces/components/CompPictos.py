#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html import graph


class Pictogram(object):

  def __init__(self, context):
    self.context = context

  def arrow(self, width=(21, "px"), height=(12, "px")):
    html_svg = graph.GraphSvg.SVG(self.context.rptObj, width=(21, "px"), height=(12, "px"))
    html_svg.style.css.width = 21
    html_svg.style.css.height = 12
    html_svg.path(fill="rgb(0, 117, 235)", x=0.0917969,
             y="5.84215C0.0917969 5.42793 0.427583 5.09215 0.841797 5.09215H18.8418C19.256 5.09215 19.5918 5.42793 19.5918 5.84215C19.5918 6.25636 19.256 6.59215 18.8418 6.59215H0.841797C0.427583 6.59215 0.0917969 6.25636 0.0917969 5.84215Z")
    html_svg.path(fill="rgb(0, 117, 235)", x=14.2706,
             y="0.315129C14.5635 0.0222357 15.0384 0.0222357 15.3313 0.315129L20.1313 5.11513C20.2719 5.25578 20.351 5.44655 20.351 5.64546C20.351 5.84437 20.2719 6.03514 20.1313 6.17579L15.3313 10.9758C15.0384 11.2687 14.5635 11.2687 14.2706 10.9758C13.9777 10.6829 13.9777 10.208 14.2706 9.91513L18.5403 5.64546L14.2706 1.37579C13.9777 1.0829 13.9777 0.608022 14.2706 0.315129Z")
    html_svg.style.hover({"margin-left": '4px'})
    return html_svg

  def flam(self, width=(619, "px"), height=(423, "px")):
    html_svg = graph.GraphSvg.SVG(self.context.rptObj, width=(619, "px"), height=(423, "px"))
    html_svg.style.css.width = 200
    html_svg.style.css.height = 100
    html_svg.path(fill="red", x=31.5, y="49.6C55 41.5 59 20.4 56 1c0-.7.6-1.2 1.2-1C79.7 11 105 35 105 71c0 27.6-21.4 52-52.5 52a50 50 0 0 1-28.2-92.7c.6-.4 1.4 0 1.4.7.3 3.7 1.3 13 5.4 18.6h.4z")
    return html_svg

  def gout(self):
    """"""
    svg = graph.GraphSvg.SVG(self.context.rptObj, width=(1199.96, "px"), height=(1014.39, "px"))
    svg.style.css.width = 33
    svg.style.css.height = 33
    svg.path(fill='#2dbeff', x=531.96,
             y="418l4-21c-69.8-47.6-157.2-69.3-247-54l54.4-308.4L146.66 0c-17.5 38.4-96.5 218.6-130.7 418-27.5 159.8-26.2 332 58.5 453 18.2 26 40.2 49.7 66.7 70.4 77 60.3 170.2 83.8 261 68.4 83.4-14 154.4-57.7 204.3-118.2-5.5-6.7-10.8-13.6-15.7-20.7-85-121.2-86-293.3-58.7-453z")

    return svg
