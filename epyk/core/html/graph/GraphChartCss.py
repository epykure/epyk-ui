#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js import JsUtils


class ChartCss(Html.Html):
  requirements = ('charts.css', )
  name = 'ChartCss'

  def __init__(self,  report, width, height, html_code, options, profile):
    super(ChartCss, self).__init__(
      report, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.attr["class"].clear()
    self.attr["class"].add("charts-css line")

  def __str__(self):
    return '''
<table %s>

  <caption> Front End Developer Salary </caption>

  <tbody>
    <tr>
      <td style="--start: 0.2; --size: 0.4"> <span class="data"> $ 40K </span> </td>
    </tr>
    <tr>
      <td style="--start: 0.4; --size: 0.8"> <span class="data"> $ 80K </span> </td>
    </tr>
    <tr>
      <td style="--start: 0.8; --size: 0.6"> <span class="data"> $ 60K </span> </td>
    </tr>
    <tr>
      <td style="--start: 0.6; --size: 1.0"> <span class="data"> $ 100K </span> </td>
    </tr>
    <tr>
      <td style="--start: 1.0; --size: 0.3"> <span class="data"> $ 30K </span> </td>
    </tr>
  </tbody>

</table>
''' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChartCssBar(Html.Html):
  requirements = ('charts.css', )
  name = 'ChartCss Bar'

  def __init__(self,  report, width, height, html_code, options, profile):
    super(ChartCssBar, self).__init__(
      report, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.attr["class"].clear()
    self.attr["class"].add("charts-css [ column ] [ show-primary-axis show-4-secondary-axes ] [ data-spacing-4 reverse-data ]")

  def __str__(self):
    return '''
  <table %s>
    <caption> Front End Developer Salary </caption>
    <thead>
      <tr>
        <th scope="col"> Year </th>
        <th scope="col"> Income </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th scope="row"> 2016 </th>
        <td style="--size: calc( 40 / 100 );"> $ 40K </td>
      </tr>
      <tr>
        <th scope="row"> 2017 </th>
        <td style="--size: calc( 60 / 100 );"> $ 60K </td>
      </tr>
      <tr>
        <th scope="row"> 2018 </th>
        <td style="--size: calc( 75 / 100 );"> $ 75K </td>
      </tr>
      <tr>
        <th scope="row"> 2019 </th>
        <td style="--size: calc( 90 / 100 );"> $ 90K </td>
      </tr>
      <tr>
        <th scope="row"> 2020 </th>
        <td style="--size: calc( 100 / 100 );"> $ 100K <br> </td>
      </tr>
    </tbody>

  </table> 
  ''' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChartCssBarStacked(ChartCssBar):
  requirements = ('charts.css', )
  name = 'ChartCss Stacked Bar'

  def __init__(self,  report, width, height, html_code, options, profile):
    super(ChartCssBar, self).__init__(
      report, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.attr["class"].clear()
    self.attr["class"].add("charts-css column multiple stacked")
