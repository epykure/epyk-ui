
from epyk.core.html.options import Options
from epyk.core.html.options import Enums
from epyk.core.js.packages import packageImport
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChart


class EnumMarks(Enums):

  def arc(self):
    """  
    Circular arcs, including pie and donut slices.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def area(self):
    """  
    Filled areas with horizontal or vertical alignment.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def image(self):
    """  
    Images, including icons or photographs.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def group(self):
    """  
    Containers for other marks, useful for sub-plots.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def line(self):
    """  
    Stroked lines, often used for showing change over time.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def path(self):
    """  
    Arbitrary paths or polygons, defined using SVG path syntax.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def rect(self):
    """  
    Rectangles, as in bar charts and timelines.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def rule(self):
    """  
    Rules are line segments, often used for axis ticks and grid lines.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def shape(self):
    """  
    A special variant of path marks for faster drawing of cartographic maps.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def symbol(self):
    """  
    Plotting symbols, including circles, squares and other shapes.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def text(self):
    """  
    Text labels with configurable fonts, alignment and angle.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()

  def trail(self):
    """  
    Lines that can change size based on underlying data.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    self._set_value()


class EnumAxisTypes(Enums):

  def albers(self):
    """  
    The Albersâ€™ equal-area conic projection.
    This is a U.S.-centric configuration of "conicEqualArea".

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def albersUsa(self):
    """  
    A U.S.-centric composite with projections for the lower 48 states, Hawaii, and Alaska (scaled to 0.35 times the
    true relative area).

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def azimuthalEqualArea(self):
    """  
    The azimuthal equal-area projection.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def azimuthalEquidistant(self):
    """  
    The azimuthal equidistant projection.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def conicConformal(self):
    """  
    The conic conformal projection.
    The parallels default to [30Â°, 30Â°] resulting in flat top.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def conicEqualArea(self):
    """  
    The Albersâ€™ equal-area conic projection.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def conicEquidistant(self):
    """  
    The conic equidistant projection.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def equalEarth(self):
    """  
    The Equal Earth projection, by Bojan Å avriÄ et al., 2018.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def equirectangular(self):
    """  
    The equirectangular (plate carrÃ©e) projection, akin to using longitude, latitude directly.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def gnomonic(self):
    """  
    The gnomonic projection.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def identity(self):
    """  
    The identity transform, which can be used to translate, scale, and clip planar geometry.
    Also supports additional boolean reflectX and reflectY parameters.
    â‰¥ 3.3

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def mercator(self):
    """  
    The spherical Mercator projection.
    Uses a default clipExtent such that the world is projected to a square, clipped to approximately Â±85Â° latitude.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def mollweide(self):
    """  
    An equal-area, pseudocylindrical map projection generally used for global maps of the world or night sky.
    â‰¥ 5.9

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def naturalEarth1(self):
    """  
    The Natural Earth projection is a pseudocylindrical projection designed by Tom Patterson.
    It is neither conformal nor equal-area, but appealing to the eye for small-scale maps of the whole world.
    â‰¥ 4.0

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def orthographic(self):
    """  
    The orthographic projection.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def stereographic(self):
    """  
    The stereographic projection.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()

  def transverseMercator(self):
    """  
    The transverse spherical Mercator projection.
    Uses a default clipExtent such that the world is projected to a square, clipped to approximately Â±85Â° latitude.

    Related Pages:

      https://vega.github.io/vega/docs/projections/
    """
    self._set_value()


class EnumOrients(Enums):

  def left(self):
    """  
    Place the legend to the left of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/legends/
    """
    self._set_value()

  def right(self):
    """  
    Place the legend to the right of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/legends/
    """
    self._set_value()

  def top(self):
    """  
    Place the legend above the top of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/legends/
    """
    self._set_value()

  def bottom(self):
    """  
    Place the legend below the bottom of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/legends/
    """
    self._set_value()

  def top_left(self):
    """  
    Place the legend inside the upper left corner of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/legends/
    """
    self._set_value(name="top-left")

  def top_right(self):
    """  
    Place the legend inside the upper right corner of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/legends/
    """
    self._set_value(name="top-right")

  def bottom_left(self):
    """  
    Place the legend inside the lower left corner of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/legends/
    """
    self._set_value(name="bottom-left")

  def bottom_right(self):
    """  
    Place the legend inside the lower right corner of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/legends/
    """
    self._set_value(name="bottom-right")

  def none(self):
    """  
    Do not perform automatic layout.
    Allows custom layout by setting the legendX and legendY properties of the legend.

    Related Pages:

      https://vega.github.io/vega/docs/legends/
    """
    self._set_value()


class EnumAggregateTypes(Enums):

  def count(self):
    """  
    The total count of data objects in the group.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def valid(self):
    """  
    The count of field values that are not missing or NaN.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def missing(self):
    """  
    The count of null, undefined, or empty string ('') field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def distinct(self):
    """  
    The count of distinct field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def sum(self):
    """  
    The sum of field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def product(self):
    """  
    The product of field values.
    â‰¥ 5.10

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def mean(self):
    """  
    The mean (average) field value.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def average(self):
    """  
    The mean (average) field value.
    Identical to mean.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def variance(self):
    """  
    The sample variance of field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def variancep(self):
    """  
    The population variance of field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def stdev(self):
    """  
    The sample standard deviation of field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def stdevp(self):
    """  
    The population standard deviation of field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def stderr(self):
    """  
    The standard error of field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def median(self):
    """  
    The median field value.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def q1(self):
    """  
    The lower quartile boundary of field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def q3(self):
    """  
    The upper quartile boundary of field values.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def ci0(self):
    """  
    The lower boundary of the bootstrapped 95% confidence interval of the mean field value.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def ci1(self):
    """  
    The upper boundary of the bootstrapped 95% confidence interval of the mean field value.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def min(self):
    """  
    The minimum field value.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def max(self):
    """  
    The maximum field value.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def argmin(self):
    """  
    An input data object containing the minimum field value.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def argmax(self):
    """  
    An input data object containing the maximum field value.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()

  def values(self):
    """  
    The list of data objects in the group.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    self._set_value()


class OptSignalOnEvent(Options):

  @property
  def event(self):
    return self._config_get()

  @event.setter
  def event(self, text):
    self._config(text)

  @property
  def events(self):
    return self._config_get()

  @events.setter
  def events(self, text):
    self._config(text)

  @property
  def update(self):
    return self._config_get()

  @update.setter
  def update(self, text):
    self._config(text)

  @property
  def force(self):
    return self._config_get()

  @force.setter
  def force(self, flag):
    self._config(flag)


class OptSignal(Options):

  @property
  def name(self):
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def value(self):
    return self._config_get()

  @value.setter
  def value(self, values):
    self._config(values)

  def on(self, events):

    scale = self._config_sub_data_enum("on", OptSignalOnEvent)
    scale.events = events
    return scale


class OptScaleDomain(Options):

  @property
  def data(self):
    return self._config_get()

  @data.setter
  def data(self, text):
    self._config(text)

  @property
  def field(self):
    return self._config_get()

  @field.setter
  def field(self, text):
    self._config(text)


class OptScale(Options):

  @property
  def name(self):
    """  
    Required.
    A unique name for the scale.
    Scales and projections share the same namespace; names must be unique across both.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def type(self):
    """  
    The type of scale (default linear).
    See the scale type reference for more.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @type.setter
  def type(self, text):
    self._config(text)

  @property
  def domainMax(self):
    """  
    Sets the maximum value in the scale domain, overriding the domain property.
    The domainMax property is only intended for use with scales having continuous domains.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @domainMax.setter
  def domainMax(self, num):
    self._config(num)

  @property
  def domainMin(self):
    """  
    Sets the minimum value in the scale domain, overriding the domain property.
    The domainMin property is only intended for use with scales having continuous domains.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @domainMin.setter
  def domainMin(self, num):
    self._config(num)

  @property
  def domainMid(self):
    """  
    Inserts a single mid-point value into a two-element domain.
    The mid-point value must lie between the domain minimum and maximum values.
    This property can be useful for setting a midpoint for diverging color scales.
    The domainMid property is only intended for use with scales supporting continuous, piecewise domains.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @domainMid.setter
  def domainMid(self, num):
    self._config(num)

  @property
  def interpolate(self):
    """  
    The interpolation method for range values.
    By default, continuous scales use a general interpolator for numbers, dates, strings and colors (in RGB space) is used.
    For color ranges, this property allows interpolation in alternative color spaces.
    Legal values include rgb, hsl, hsl-long, lab, hcl, hcl-long, cubehelix and cubehelix-long (‘-long’ variants use longer paths in polar coordinate spaces).
    If object-valued, this property accepts an object with a string-valued type property and an optional numeric gamma property applicable to rgb and cubehelix interpolators.
    For more, see the d3-interpolate documentation.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @interpolate.setter
  def interpolate(self, text):
    self._config(text)

  @property
  def reverse(self):
    """  
    A boolean flag (default false) that reverses the order of the scale range.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @reverse.setter
  def reverse(self, flag):
    self._config(flag)

  @property
  def range(self):
    """

    :return:
    """
    return self._config_get()

  @range.setter
  def range(self, value):
    self._config(value)

  @property
  def round(self):
    """  
    A boolean flag (default false) that rounds numeric output values to integers.
    Helpful for snapping to a pixel grid.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @round.setter
  def round(self, flag):
    self._config(flag)

  @property
  def clamp(self):
    """  
    A boolean indicating if output values should be clamped to the range (default false).
    If clamping is disabled and the scale is passed a value outside the domain, the scale may return a value outside the range through extrapolation.
    If clamping is enabled, the output value of the scale is always within the scale’s range.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @clamp.setter
  def clamp(self, flag):
    self._config(flag)

  @property
  def padding(self):
    """  
    Expands the scale domain to accommodate the specified number of pixels on each of the scale range.
    The scale range must represent pixels for this parameter to function as intended.
    Padding adjustment is performed prior to all other adjustments, including the effects of the zero, nice, domainMin, and domainMax properties.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @padding.setter
  def padding(self, num):
    self._config(num)

  @property
  def nice(self):
    """  
    Extends the domain so that it starts and ends on nice round values (default false).
    This method typically modifies the scale’s domain, and may only extend the bounds to the nearest round value.
    Nicing is useful if the domain is computed from data and may be irregular.
    For example, for a domain of [0.201479…, 0.996679…], a nice domain might be [0.2, 1.0].
    Domain values set via domainMin and domainMax (but not domainRaw) are subject to nicing.
    Using a number value for this parameter (representing a desired tick count) allows greater control over the step size used to extend the bounds, guaranteeing that the returned ticks will exactly cover the domain.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @nice.setter
  def nice(self, num):
    self._config(num)

  @property
  def zero(self):
    """  
    Boolean flag indicating if the scale domain should include zero.
    The default value is true for linear, sqrt and pow, and false otherwise.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @zero.setter
  def zero(self, flag):
    self._config(flag)


class OptScaleQuantLog(Options):

  @property
  def base(self):
    """  
    The base of the logarithm (default 10).

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @base.setter
  def base(self, num):
    self._config(num)


class OptScaleQuantExpo(Options):

  @property
  def exponent(self):
    """  
    The exponent to use in the scale transform (default 1).

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @exponent.setter
  def exponent(self, num):
    self._config(num)


class OptScaleQuantLogScales(Options):

  @property
  def constant(self):
    """  
    A constant determining the slope of the symlog function around zero (default 1).

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @constant.setter
  def constant(self, num):
    self._config(num)


class OptScaleTime(OptScale):

  @property
  def nice(self):
    """  
    If specified, modifies the scale domain to use a more human-friendly value range.
    For time and utc scale types, the nice value can additionally be a string indicating the desired time interval.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @nice.setter
  def nice(self, value):
    self._config(value)


class OptScaleBand(OptScale):

  @property
  def align(self):
    """  
    The alignment of elements within the scale range.
    This value must lie in the range [0,1].
    A value of 0.5 (default) indicates that the bands should be centered within the range.
    A value of 0 or 1 may be used to shift the bands to one side, say to position them adjacent to an axis.
    For more, see this explainer for D3 band align.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @align.setter
  def align(self, num):
    self._config(num)

  @property
  def domainImplicit(self):
    """  
    A boolean flag (default false) indicating if an ordinal domain should be implicitly extended with new values.
    If false, the scale will return undefined for values not explicitly included in the domain.
    If true, new values will be appended to the domain and the matching range value will be returned.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @domainImplicit.setter
  def domainImplicit(self, flag):
    self._config(flag)

  @property
  def padding(self):
    """  
    Sets paddingInner and paddingOuter to the same padding value (default 0).
    This value must lie in the range [0,1].

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @padding.setter
  def padding(self, num):
    self._config(num)

  @property
  def paddingInner(self):
    """  
    The inner padding (spacing) within each band step, as a fraction of the step size (default 0).
    This value must lie in the range [0,1].

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @paddingInner.setter
  def paddingInner(self, num):
    self._config(num)

  @property
  def paddingOuter(self):
    """  
    The outer padding (spacing) at the ends of the scale range, as a fraction of the step size (default 0).
    This value must lie in the range [0,1].

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @paddingOuter.setter
  def paddingOuter(self, num):
    self._config(num)


class OptScaleBins(OptScale):

  @property
  def bind(self):
    pass


class OptScalePoint(OptScale):

  @property
  def align(self):
    """  
    The alignment of elements within the scale range.
    This value must lie in the range [0,1].
    A value of 0.5 (default) indicates that the points should be centered within the range.
    A value of 0 or 1 may be used to shift the points to one side, say to position them adjacent to an axis.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @align.setter
  def align(self, num):
    self._config(num)

  @property
  def padding(self):
    """  
    An alias for paddingOuter (default 0).
    This value must lie in the range [0,1].

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @padding.setter
  def padding(self, num):
    self._config(num)

  @property
  def paddingOuter(self):
    """  
    The outer padding (spacing) at the ends of the scale range, as a fraction of the step size (default 0).
    This value must lie in the range [0,1].

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @paddingOuter.setter
  def paddingOuter(self, num):
    self._config(num)


class OptProjection(Options):

  @property
  def name(self):
    """  
    Required.
    A unique name for the projection.
    Projections and scales share the same namespace; names must be unique across both.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def type(self):
    """  
    The cartographic projection to use.
    The default is "mercator".
    This value is case-insensitive, for example "albers" and "Albers" indicate the same projection type.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @type.setter
  def type(self, text):
    self._config(text)

  @property
  def types(self):
    pass

  @property
  def clipAngle(self):
    """  
    The projectionâ€™s clipping circle radius, specified as an angle in degrees.
    If null, switches to antimeridian cutting rather than small-circle clipping.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @clipAngle.setter
  def clipAngle(self, num):
    self._config(num)

  @property
  def clipExtent(self):
    """  
    The projectionâ€™s viewport clip extent, as a set of pixel bounds.
    The extent bounds are specified as an array [[x0, y0], [x1, y1]], where x0 is the left-side of the viewport,
    y0 is the top, x1 is the right and y1 is the bottom.
    If null, no viewport clipping is performed.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @clipExtent.setter
  def clipExtent(self, values):
    self._config(values)

  @property
  def scale(self):
    """  
    The projectionâ€™s scale factor.
    The default scale is projection-specific.
    The scale factor corresponds linearly to the distance between projected points; however, scale factor values
    are not equivalent across projections.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @scale.setter
  def scale(self, num):
    self._config(num)

  @property
  def translate(self):
    """  
    The projectionâ€™s translation offset as a two-element array [tx, ty].
    If translate is not specified, returns the current translation offset which defaults to [480, 250].
    The translation offset determines the pixel coordinates of the projectionâ€™s center.
    The default translation offset places (0Â°,0Â°) at the center of a 960Ã—500 area.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @translate.setter
  def translate(self, values):
    self._config(values)

  @property
  def center(self):
    """  
    The projectionâ€™s center, a two-element array of longitude and latitude in degrees.
    The default value is [0, 0].

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @center.setter
  def center(self, values):
    self._config(values)

  @property
  def rotate(self):
    """  
    The projectionâ€™s three-axis rotation angles.
    The value must be a two- or three-element array of numbers [lambda, phi, gamma] specifying the rotation angles
    in degrees about each spherical axis.
    (These correspond to yaw, pitch and roll.) The default value is [0, 0, 0].

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @rotate.setter
  def rotate(self, values):
    self._config(values)

  @property
  def parallels(self):
    """  
    For conic projections, the two standard parallels that define the map layout.
    The default depends on the specific conic projection used.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @parallels.setter
  def parallels(self, values):
    self._config(values)

  @property
  def pointRadius(self):
    """  
    The default radius (in pixels) to use when drawing GeoJSON Point and MultiPoint geometries.
    This parameter sets a constant default value.
    To modify the point radius in response to data, see the corresponding parameter of the GeoPath and GeoShape transforms.
    The default value is 4.5.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @pointRadius.setter
  def pointRadius(self, num):
    self._config(num)

  @property
  def precision(self):
    """  
    The threshold for the projection's adaptive resampling in pixels.
    This value corresponds to the Douglasâ€“Peucker distance.
    If precision is not specified, returns the projectionâ€™s current resampling precision which defaults to
    âˆš0.5 â‰… 0.70710â€¦

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @precision.setter
  def precision(self, num):
    self._config(num)

  @property
  def fit(self):
    """  
    GeoJSON data to which the projection should attempt to automatically fit the translate and scale parameters.
    If object-valued, this parameter should be a GeoJSON Feature or FeatureCollection.
    If array-valued, each array member may be a GeoJSON Feature, FeatureCollection, or a sub-array of GeoJSON Features.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @fit.setter
  def fit(self, values):
    self._config(values)

  @property
  def extent(self):
    """  
    Used in conjunction with fit, provides the pixel area to which the projection should be automatically fit.
    The extent bounds are specified as an array [[x0, y0], [x1, y1]], where x0 is the left side of the extent,
    y0 is the top, x1 is the right and y1 is the bottom.

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @extent.setter
  def extent(self, values):
    self._config(values)

  @property
  def size(self):
    """  
    Used in conjunction with fit, provides the width and height in pixels of the area to which the projection should
    be automatically fit.
    This parameter is equivalent to an extent of [[0,0], size].

    Related Pages:

      https://vega.github.io/vega/docs/scales/
    """
    return self._config_get()

  @size.setter
  def size(self, values):
    self._config(values)


class OptOpacity(Options):
  @property
  def value(self):
    """  

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @value.setter
  def value(self, num):
    self._config(num)

  @property
  def test(self):
    """  

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @test.setter
  def test(self, jsData):
    self._config(jsData)


class OptUpdate(Options):

  def add_opacity(self, value, test=None):
    """  

    :rtype: OptOpacity
    """
    scale = self._config_sub_data_enum("opacity", OptOpacity)
    scale.value = value
    #scale.test = "!length(data('selected')) || indata('selected', 'value', datum.value)"
    scale = self._config_sub_data_enum("opacity", OptOpacity)
    scale.value = 1
    return scale


class OptLabel(Options):

  @property
  def interactive(self):
    """  

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @interactive.setter
  def interactive(self, flag):
    self._config(flag)

  @property
  def name(self):
    """  

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def update(self):
    """

    :rtype: OptUpdate
    """
    return self._config_sub_data("update", OptUpdate)


class OptAxe(Options):

  @property
  def scale(self):
    """  
    Required.
    The name of the scale backing the axis component.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @scale.setter
  def scale(self, text):
    self._config(text)

  @property
  def orient(self):
    """  
    Required.
    The orientation of the axis.
    See the axis orientation reference.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @orient.setter
  def orient(self, text):
    self._config(text)

  @property
  def bandPosition(self):
    """  
    An interpolation fraction indicating where, for band scales, axis ticks should be positioned.
    A value of 0 places ticks at the left edge of their bands.
    A value of 0.5 places ticks in the middle of their bands.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @bandPosition.setter
  def bandPosition(self, num):
    self._config(num)

  @property
  def domain(self):
    """  
    A boolean flag indicating if the domain (the axis baseline) should be included as part of the axis (default true).

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @domain.setter
  def domain(self, flag):
    self._config(flag)

  @property
  def domainCap(self):
    """  
    The stroke cap for the axis domain line.
    One of "butt" (default), "round" or "square".
    â‰¥ 5.11

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @domainCap.setter
  def domainCap(self, text):
    self._config(text)

  @property
  def domainColor(self):
    """  
    Color of axis domain line.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @domainColor.setter
  def domainColor(self, code):
    self._config(code)

  @property
  def domainDash(self):
    """  
    Stroke dash of axis domain lines (or [] for solid lines).
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @domainDash.setter
  def domainDash(self, values):
    self._config(values)

  @property
  def domainDashOffset(self):
    """  
    The pixel offset at which to start the domain dash array.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @domainDashOffset.setter
  def domainDashOffset(self, num):
    self._config(num)

  @property
  def domainOpacity(self):
    """  
    Opacity of axis domain line.
    â‰¥ 4.1

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @domainOpacity.setter
  def domainOpacity(self, num):
    self._config(num)

  @property
  def domainWidth(self):
    """  
    Stroke width of axis domain line.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @domainWidth.setter
  def domainWidth(self, num):
    self._config(num)

  @property
  def format(self):
    """  
    The format specifier pattern for axis labels.
    For numerical values, must be a legal d3-format specifier.
    For date-time values, must be a legal d3-time-format specifier or a TimeMultiFormat object.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @format.setter
  def format(self, text):
    self._config(text)

  @property
  def formatType(self):
    """  
    Specifies the type of format to use ("number", "time", "utc") for scales that do not have a strict domain data type.
    This property is useful for formatting date-time values for band or point scales.
    If specified, the format property must have a valid specifier pattern for the given type.
    Supported â‰¥ 5.1, UTC support â‰¥ 5.8.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @formatType.setter
  def formatType(self, text):
    self._config(text)

  @property
  def grid(self):
    """  
    A boolean flag indicating if grid lines should be included as part of the axis (default false).

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @grid.setter
  def grid(self, flag):
    self._config(flag)

  @property
  def gridCap(self):
    """  
    The stroke cap for axis grid lines.
    One of "butt" (default), "round" or "square".
    â‰¥ 5.11

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gridCap.setter
  def gridCap(self, text):
    self._config(text)

  @property
  def gridColor(self):
    """  
    Color of axis grid lines.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gridColor.setter
  def gridColor(self, code):
    self._config(code)

  @property
  def gridDash(self):
    """  
    Stroke dash of axis grid lines (or [] for solid lines).

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gridDash.setter
  def gridDash(self, values):
    self._config(values)

  @property
  def gridDashOffset(self):
    """  
    The pixel offset at which to start the grid dash array.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gridDashOffset.setter
  def gridDashOffset(self, num):
    self._config(num)

  @property
  def gridOpacity(self):
    """  
    Opacity of axis grid lines.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gridOpacity.setter
  def gridOpacity(self, num):
    self._config(num)

  @property
  def gridScale(self):
    """  
    The name of the scale to use for including grid lines.
    By default grid lines are driven by the same scale as the ticks and labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gridScale.setter
  def gridScale(self, text):
    self._config(text)

  @property
  def gridWidth(self):
    """  
    Stroke width of axis grid lines.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gridWidth.setter
  def gridWidth(self, num):
    self._config(num)

  @property
  def labels(self):
    """  
    A boolean flag indicating if labels should be included as part of the axis (default true).

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labels.setter
  def labels(self, flag):
    self._config(flag)

  @property
  def labelAlign(self):
    """  
    Horizontal text alignment of axis tick labels, overriding the default setting for the current axis orientation.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelAlign.setter
  def labelAlign(self, text):
    self._config(text)

  @property
  def labelAngle(self):
    """  
    Angle in degrees of axis tick labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelAngle.setter
  def labelAngle(self, num):
    self._config(num)

  @property
  def labelBaseline(self):
    """  
    Vertical text baseline of axis tick labels, overriding the default setting for the current axis orientation.
    One of alphabetic (default), top, middle, bottom, line-top, or line-bottom.
    The line-top and line-bottom values â‰¥ 5.10 operate similarly to top and bottom, but are calculated relative to the lineHeight rather than fontSize alone.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelBaseline.setter
  def labelBaseline(self, text):
    self._config(text)

  @property
  def labelBound(self):
    """  
    Indicates if labels should be hidden if they exceed the axis range.
    If false (the default) no bounds overlap analysis is performed.
    If true, labels will be hidden if they exceed the axis range by more than 1 pixel.
    If this property is a number, it specifies the pixel tolerance: the maximum amount by which a label bounding box may exceed the axis range.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelBound.setter
  def labelBound(self, num):
    self._config(num)

  @property
  def labelColor(self):
    """  
    Text color of axis tick labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelColor.setter
  def labelColor(self, code):
    self._config(code)

  @property
  def labelFlush(self):
    """  
    Indicates if labels at the beginning or end of the axis should be aligned flush with the scale range.
    If a number, indicates a pixel distance threshold: labels with anchor coordinates within the threshold distance for an axis end-point will be flush-adjusted.
    If true, a default threshold of 1 pixel is used.
    Flush alignment for a horizontal axis will left-align labels near the beginning of the axis and right-align labels near the end.
    For vertical axes, bottom and top text baselines will be applied instead.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFlush.setter
  def labelFlush(self, num):
    self._config(num)

  @property
  def labelFlushOffset(self):
    """  
    Indicates the number of pixels by which to offset flush-adjusted labels (default 0).
    For example, a value of 2 will push flush-adjusted labels 2 pixels outward from the center of the axis.
    Offsets can help the labels better visually group with corresponding axis ticks.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFlushOffset.setter
  def labelFlushOffset(self, num):
    self._config(num)

  @property
  def labelFont(self):
    """  
    Font name for axis tick labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFont.setter
  def labelFont(self, text):
    self._config(text)

  @property
  def labelFontSize(self):
    """  
    Font size of axis tick labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFontSize.setter
  def labelFontSize(self, num):
    self._config(num)

  @property
  def labelFontStyle(self):
    """  
    Font style of axis tick labels (e.g., normal or italic).
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFontStyle.setter
  def labelFontStyle(self, text):
    self._config(text)

  @property
  def labelFontWeight(self):
    """  
    Font weight of axis tick labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFontWeight.setter
  def labelFontWeight(self, text):
    self._config(text)

  @property
  def labelLimit(self):
    """  
    The maximum allowed length in pixels of axis tick labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelLimit.setter
  def labelLimit(self, num):
    self._config(num)

  @property
  def labelLineHeight(self):
    """  
    Line height in pixels for multi-line label text or label text with "line-top" or "line-bottom" baseline.
    â‰¥ 5.10

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelLineHeight.setter
  def labelLineHeight(self, num):
    self._config(num)

  @property
  def labelOffset(self):
    """  
    Position offset in pixels to apply to labels, in addition to tickOffset.
    â‰¥ 5.10

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelOffset.setter
  def labelOffset(self, num):
    self._config(num)

  @property
  def labelOpacity(self):
    """  
    Opacity of axis tick labels.
    â‰¥ 4.1

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelOpacity.setter
  def labelOpacity(self, num):
    self._config(num)

  @property
  def labelOverlap(self):
    """  
    The strategy to use for resolving overlap of axis labels.
    If false (the default), no overlap reduction is attempted.
    If set to true or "parity", a strategy of removing every other label is used (this works well for standard linear axes).
    If set to "greedy", a linear scan of the labels is performed, removing any label that overlaps with the last
    visible label (this often works better for log-scaled axes).

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelOverlap.setter
  def labelOverlap(self, text):
    self._config(text)

  @property
  def labelPadding(self):
    """  
    The padding in pixels between labels and ticks.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelPadding.setter
  def labelPadding(self, num):
    self._config(num)

  @property
  def labelSeparation(self):
    """  
    The minimum separation that must be between label bounding boxes for them to be considered non-overlapping (default 0).
    This property is ignored if labelOverlap resolution is not enabled.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelSeparation.setter
  def labelSeparation(self, num):
    self._config(num)

  @property
  def minExtent(self):
    """  
    The minimum extent in pixels that axis ticks and labels should use.
    This determines a minimum offset value for axis titles.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @minExtent.setter
  def minExtent(self, num):
    self._config(num)

  @property
  def maxExtent(self):
    """  
    The maximum extent in pixels that axis ticks and labels should use.
    This determines a maximum offset value for axis titles.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @maxExtent.setter
  def maxExtent(self, num):
    self._config(num)

  @property
  def offset(self):
    """  
    The orthogonal offset in pixels by which to displace the axis from its position along the edge of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @offset.setter
  def offset(self, num):
    self._config(num)

  @property
  def position(self):
    """  
    The anchor position of the axis in pixels (default 0).
    For x-axes with top or bottom orientation, this sets the axis group x coordinate.
    For y-axes with left or right orientation, this sets the axis group y coordinate.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @position.setter
  def position(self, num):
    self._config(num)

  @property
  def ticks(self):
    """  
    A boolean flag indicating if ticks should be included as part of the axis (default true).

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @ticks.setter
  def ticks(self, flag):
    self._config(flag)

  @property
  def tickBand(self):
    """  
    Indicates the type of tick style to use in conjunction with band scales.
    One of "center" (default) to center ticks in the middle of the band interval, or "extent" to place ticks at band
    extents (interval boundaries).
    If specified, this property may override the settings of bandPosition, tickExtra, and tickOffset.
    â‰¥ 5.8

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickBand.setter
  def tickBand(self, text):
    self._config(text)

  @property
  def tickCap(self):
    """  
    The stroke cap for axis tick marks.
    One of "butt" (default), "round" or "square".
    â‰¥ 5.11

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickCap.setter
  def tickCap(self, text):
    self._config(text)

  @property
  def tickColor(self):
    """  
    Color of axis ticks.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickColor.setter
  def tickColor(self, code):
    self._config(code)

  @property
  def tickCount(self):
    """  
    A desired number of ticks, for axes visualizing quantitative scales.
    The resulting number may be different so that values are â€œniceâ€ (multiples of 2, 5, 10) and lie within the
    underlying scaleâ€™s range.
    For scales of type time or utc, the tick count can instead be a time interval specifier.
    Legal string values are "millisecond", "second", "minute", "hour", "day", "week", "month", and "year".
    Alternatively, an object-valued interval specifier of the form {"interval": "month", "step": 3} includes a desired
    number of interval steps.
    Here, ticks are generated for each quarter (Jan, Apr, Jul, Oct) boundary.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickCount.setter
  def tickCount(self, text):
    self._config(text)

  @property
  def tickDash(self):
    """  
    Stroke dash of axis tick marks (or [] for solid lines).
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickDash.setter
  def tickDash(self, values):
    self._config(values)

  @property
  def tickDashOffset(self):
    """  
    The pixel offset at which to start the tick mark dash array.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickDashOffset.setter
  def tickDashOffset(self, num):
    self._config(num)

  @property
  def tickMinStep(self):
    """  
    The minimum desired step between axis ticks, in terms of scale domain values.
    For example, a value of 1 indicates that ticks should not be less than 1 unit apart.
    If tickMinStep is specified, the tickCount value will be adjusted, if necessary, to enforce the minimum step value.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickMinStep.setter
  def tickMinStep(self, num):
    self._config(num)

  @property
  def tickExtra(self):
    """  
    Boolean flag indicating if an extra axis tick should be added for the initial position of the axis.
    This flag is useful for styling axes for band scales such that ticks are placed on band boundaries rather in the
    middle of a band.
    Use in conjunction with "bandPosition": 1 and an axis "padding" value of 0.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickExtra.setter
  def tickExtra(self, flag):
    self._config(flag)

  @property
  def tickOffset(self):
    """  
    Position offset in pixels to apply to ticks, labels, and gridlines.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickOffset.setter
  def tickOffset(self, num):
    self._config(num)

  @property
  def tickOpacity(self):
    """  
    Opacity of axis ticks.
    â‰¥ 4.1

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickOpacity.setter
  def tickOpacity(self, num):
    self._config(num)

  @property
  def tickRound(self):
    """  
    Boolean flag indicating if pixel position values should be rounded to the nearest integer.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickRound.setter
  def tickRound(self, flag):
    self._config(flag)

  @property
  def tickSize(self):
    """  
    The length in pixels of axis ticks.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickSize.setter
  def tickSize(self, num):
    self._config(num)

  @property
  def tickWidth(self):
    """  
    Width in pixels of axis ticks.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickWidth.setter
  def tickWidth(self, num):
    self._config(num)

  @property
  def title(self):
    """  
    A title for the axis (none by default).
    For versions â‰¥ 5.7, a string array specifies a title with multiple lines of text.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @title.setter
  def title(self, text):
    self._config(text)

  @property
  def titleAnchor(self):
    """  
    The anchor position for placing the axis title.
    One of "start", "middle", "end", or null (default, for automatic determination).
    For example, with an orient of "bottom" these anchor positions map to a left-, center-, or right-aligned title.
    The anchor point is determined relative to the axis scale range.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleAnchor.setter
  def titleAnchor(self, text):
    self._config(text)

  @property
  def titleAlign(self):
    """  
    Horizontal text alignment of the axis title.
    One of "left", "center", or "right".
    If specified, this value overrides automatic alignment based on the titleAnchor value.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleAlign.setter
  def titleAlign(self, text):
    self._config(text)

  @property
  def titleAngle(self):
    """  
    Angle in degrees of the axis title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleAngle.setter
  def titleAngle(self, num):
    self._config(num)

  @property
  def titleBaseline(self):
    """  
    Vertical text baseline of the axis title.
    One of alphabetic (default), top, middle, bottom, line-top, or line-bottom.
    The line-top and line-bottom values â‰¥ 5.10 operate similarly to top and bottom, but are calculated relative to
    the lineHeight rather than fontSize alone.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleBaseline.setter
  def titleBaseline(self, text):
    self._config(text)

  @property
  def titleColor(self):
    """  
    Text color of the axis title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleColor.setter
  def titleColor(self, code):
    self._config(code)

  @property
  def titleFont(self):
    """  
    Font name of the axis title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleFont.setter
  def titleFont(self, text):
    self._config(text)

  @property
  def titleFontSize(self):
    """  
    Font size of the axis title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleFontSize.setter
  def titleFontSize(self, num):
    self._config(num)

  @property
  def titleFontStyle(self):
    """  
    Font style of the axis title (e.g., normal or italic).
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleFontStyle.setter
  def titleFontStyle(self, text):
    self._config(text)

  @property
  def titleFontWeight(self):
    """  
    Font weight of axis title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleFontWeight.setter
  def titleFontWeight(self, text):
    self._config(text)

  @property
  def titleLimit(self):
    """  
    The maximum allowed length in pixels of the axis title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleLimit.setter
  def titleLimit(self, num):
    self._config(num)

  @property
  def titleLineHeight(self):
    """  
    Line height in pixels for multi-line title text or title text with "line-top" or "line-bottom" baseline.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleLineHeight.setter
  def titleLineHeight(self, num):
    self._config(num)

  @property
  def titleOpacity(self):
    """  
    Opacity of axis title.
    â‰¥ 4.1

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleOpacity.setter
  def titleOpacity(self, num):
    self._config(num)

  @property
  def titlePadding(self):
    """  
    The padding in pixels between the axis labels and axis title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titlePadding.setter
  def titlePadding(self, num):
    self._config(num)

  @property
  def titleX(self):
    """  
    Custom X position of the axis title relative to the axis group, overriding the standard layout.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleX.setter
  def titleX(self, num):
    self._config(num)

  @property
  def titleY(self):
    """  
    Custom Y position of the axis title relative to the axis group, overriding the standard layout.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleY.setter
  def titleY(self, num):
    self._config(num)

  @property
  def translate(self):
    """  
    Coordinate space translation offset for axis layout.
    By default, axes are translated by a 0.5 pixel offset for both the x and y coordinates in order to align stroked
    lines with the pixel grid.
    However, for vector graphics output these pixel-specific adjustments may be undesirable, in which case translate
    can be changed (for example, to zero).
    â‰¥ 5.8

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @translate.setter
  def translate(self, num):
    self._config(num)

  @property
  def values(self):
    """  
    Explicitly set the visible axis tick and label values.
    The array entries should be legal values in the backing scale domain.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @values.setter
  def values(self, values):
    self._config(values)

  @property
  def zindex(self):
    """  
    The integer z-index indicating the layering of the axis group relative to other axis, mark, and legend groups.
    The default value is 0 and axes and grid lines are drawn behind any marks defined in the same specification level.
    Higher values (1) will cause axes and grid lines to be drawn on top of marks.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @zindex.setter
  def zindex(self, num):
    self._config(num)


class OptMark(Options):

  @property
  def type(self):
    """  
    Required.
    The graphical mark type.
    Must be one of the supported mark types.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @type.setter
  def type(self, text):
    self._config(text)

  @property
  def interactive(self):
    """  
    A boolean flag (default true) indicating if the marks can serve as input event sources.
    If false, no mouse or touch events corresponding to the marks will be generated.
    This property can also take a Signal value to dynamically toggle interactive status.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @interactive.setter
  def interactive(self, flag):
    self._config(flag)

  @property
  def name(self):
    """  
    A unique name for the mark.
    This name can be used to refer to these marks within an event stream definition.
    SVG renderers will add this name value as a CSS class name on the enclosing SVG group (g) element containing
    the mark instances.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def role(self):
    """  
    A metadata string indicating the role of the mark.
    SVG renderers will add this role value (prepended with the prefix role-) as a CSS class name on the enclosing SVG
    group (g) element containing the mark instances.
    Roles are used internally by Vega to guide layout.
    Do not set this property unless you know which layout effect you are trying to achieve.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @role.setter
  def role(self, text):
    self._config(text)

  @property
  def style(self):
    """  
    A string or array of strings indicating the name of custom styles to apply to the mark.
    A style is a named collection of mark property defaults defined within the configuration.
    These properties will be applied to the markâ€™s enter encoding set, with later styles overriding earlier styles.
    Any properties explicitly defined within the markâ€™s encode block will override a style default.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @style.setter
  def style(self, text):
    self._config(text)

  @property
  def zindex(self):
    """  
    The integer z-index indicating the layering of this mark set relative to other marks, axes, or legends.
    The default value is 0; higher values (1) will cause this mark set to be drawn on top of other mark, axis,
    or legend definitions with lower z-index values.
    Note that this value applies to the all marks in a set, not individual mark items.
    To adjust the ordering of items within a set, use the zindex encoding channel.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @zindex.setter
  def zindex(self, num):
    self._config(num)

  @property
  def align(self):
    """  
    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @align.setter
  def align(self, text):
    self._config(text)

  @property
  def dx(self):
    """  
    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @dx.setter
  def dx(self, text):
    self._config(text)


class OptMarkClip(Options):

  @property
  def path(self):
    """  
    An SVG path string describing the clipping region.
    The path is assumed to lie relative to the coordinate system of the enclosing group.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @path.setter
  def path(self, text):
    self._config(text)

  @property
  def sphere(self):
    """  
    The name of a cartographic projection with which to clip all marks to the projected sphere of the globe.
    This option is useful in conjunction with map projections that otherwise included projected content
    (such as graticule lines) outside the bounds of the globe.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @sphere.setter
  def sphere(self, text):
    self._config(text)


class OptMarkFrom(Options):

  @property
  def path(self):
    """  
    An SVG path string describing the clipping region.
    The path is assumed to lie relative to the coordinate system of the enclosing group.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @path.setter
  def path(self, text):
    self._config(text)

  @property
  def sphere(self):
    """  
    The name of a cartographic projection with which to clip all marks to the projected sphere of the globe.
    This option is useful in conjunction with map projections that otherwise included projected content (such as graticule lines) outside the bounds of the globe.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @sphere.setter
  def sphere(self, text):
    self._config(text)


class OptMarkFacet(Options):

  @property
  def name(self):
    """  
    Required.
    The name of the generated facet data source.
    Marks defined with the faceted group mark can reference this data source to visualize the local data partition.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def data(self):
    """  
    Required.
    The name of the source data set from which the facet partitions are generated.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return self._config_get()

  @data.setter
  def data(self, text):
    self._config(text)


class OptLegendEncode(Options):

  @property
  def labels(self):
    """

    :rtype: OptLabel
    """
    return self._config_sub_data("labels", OptLabel)

  @property
  def symbols(self):
    """

    :rtype: OptLabel
    """
    return self._config_sub_data("symbols", OptLabel)


class OptLegend(Options):

  @property
  def type(self):
    """  
    The type of legend to include.
    One of symbol for discrete symbol legends, or gradient for a continuous color gradient.
    If gradient is used only the fill or stroke scale parameters are considered.
    If unspecified, the type will be inferred based on the scale parameters used and their backing scale types.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @type.setter
  def type(self, text):
    self._config(text)

  @property
  def direction(self):
    """  
    The direction of the legend, one of "vertical" (default) or "horizontal".

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @direction.setter
  def direction(self, text):
    self._config(text)

  @property
  def orient(self):
    """  
    The orientation of the legend, determining where the legend is placed relative to a chartâ€™s data rectangle (default right).
    See the legend orientation reference.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @orient.setter
  def orient(self, text):
    self._config(text)

  @property
  def fill(self):
    """  
    The name of a scale that maps to a fill color.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @fill.setter
  def fill(self, text):
    self._config(text)

  @property
  def encode(self):
    """

    :rtype: OptLegendEncode
    """
    return self._config_sub_data("encode", OptLegendEncode)

  @property
  def opacity(self):
    """  
    The name of a scale that maps to an opacity value.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @opacity.setter
  def opacity(self, text):
    self._config(text)

  @property
  def shape(self):
    """  
    The name of a scale that maps to a shape value.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @shape.setter
  def shape(self, text):
    self._config(text)

  @property
  def size(self):
    """  
    The name of a scale that maps to a size (area) value.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @size.setter
  def size(self, text):
    self._config(text)

  @property
  def stroke(self):
    """  
    The name of a scale that maps to a stroke color.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @stroke.setter
  def stroke(self, text):
    self._config(text)

  @property
  def strokeDash(self):
    """  
    The name of a scale that maps to a stroke dash value.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @strokeDash.setter
  def strokeDash(self, text):
    self._config(text)

  @property
  def strokeWidth(self):
    """  
    The name of a scale that maps to a stroke width value.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @strokeWidth.setter
  def strokeWidth(self, text):
    self._config(text)

  @property
  def format(self):
    """  
    The format specifier pattern for legend labels.
    For numerical values, must be a legal d3-format specifier.
    For date-time values, must be a legal d3-time-format specifier or a TimeMultiFormat object.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @format.setter
  def format(self, text):
    self._config(text)

  @property
  def formatType(self):
    """  
    Specifies the type of format to use ("number", "time", "utc") for scales that do not have a strict domain data type.
    This property is useful for formatting date-time values for ordinal scales.
    If specified, the format property must have a valid specifier pattern for the given type.
    Supported â‰¥ 5.1, UTC support â‰¥ 5.8.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @formatType.setter
  def formatType(self, text):
    self._config(text)

  @property
  def gridAlign(self):
    """  
    The alignment to apply to symbol legends rows and columns.
    The supported string values are all, each (the default), and none.
    For more information, see the grid layout documentation.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gridAlign.setter
  def gridAlign(self, text):
    self._config(text)

  @property
  def clipHeight(self):
    """  
    The height in pixels to clip symbol legend entries and limit their size.
    By default no clipping is performed.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @clipHeight.setter
  def clipHeight(self, num):
    self._config(num)

  @property
  def columns(self):
    """  
    The number of columns in which to arrange symbol legend entries.
    A value of 0 or lower indicates a single row with one column per entry.
    The default is 0 for horizontal symbol legends and 1 for vertical symbol legends.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @columns.setter
  def columns(self, num):
    self._config(num)

  @property
  def columnPadding(self):
    """  
    The horizontal padding in pixels between symbol legend entries.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @columnPadding.setter
  def columnPadding(self, num):
    self._config(num)

  @property
  def rowPadding(self):
    """  
    The vertical padding in pixels between symbol legend entries.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @rowPadding.setter
  def rowPadding(self, num):
    self._config(num)

  @property
  def cornerRadius(self):
    """  
    Corner radius for the full legend.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @cornerRadius.setter
  def cornerRadius(self, num):
    self._config(num)

  @property
  def fillColor(self):
    """  
    Background fill color for the full legend.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @fillColor.setter
  def fillColor(self, code):
    self._config(code)

  @property
  def offset(self):
    """  
    The offset in pixels by which to displace the legend from the data rectangle and axes.
    If provided, this value will override any values specified in the legend config.
    If multiple offset values are specified for a collection of legends with the same orient value, the maximum offset
    will be used.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @offset.setter
  def offset(self, num):
    self._config(num)

  @property
  def padding(self):
    """  
    The padding between the border and content of the legend group.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @padding.setter
  def padding(self, num):
    self._config(num)

  @property
  def strokeColor(self):
    """  
    Border stroke color for the full legend.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @strokeColor.setter
  def strokeColor(self, code):
    self._config(code)

  @property
  def gradientLength(self):
    """  
    The length in pixels of the primary axis of a color gradient.
    This value corresponds to the height of a vertical gradient or the width of a horizontal gradient.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gradientLength.setter
  def gradientLength(self, num):
    self._config(num)

  @property
  def gradientOpacity(self):
    """  
    Opacity of the color gradient.
    â‰¥ 4.1

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gradientOpacity.setter
  def gradientOpacity(self, num):
    self._config(num)

  @property
  def gradientThickness(self):
    """  
    The thickness in pixels of the color gradient.
    This value corresponds to the width of a vertical gradient or the height of a horizontal gradient.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gradientThickness.setter
  def gradientThickness(self, num):
    self._config(num)

  @property
  def gradientStrokeColor(self):
    """  
    Stroke color of the color gradient border.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gradientStrokeColor.setter
  def gradientStrokeColor(self, code):
    self._config(code)

  @property
  def gradientStrokeWidth(self):
    """  
    Stroke width of the color gradient border.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @gradientStrokeWidth.setter
  def gradientStrokeWidth(self, num):
    self._config(num)

  @property
  def labelAlign(self):
    """  
    Horizontal text alignment for legend labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelAlign.setter
  def labelAlign(self, text):
    self._config(text)

  @property
  def labelBaseline(self):
    """  
    Vertical text baseline for legend labels.
    One of alphabetic (default), top, middle, bottom, line-top, or line-bottom.
    The line-top and line-bottom values â‰¥ 5.10 operate similarly to top and bottom, but are calculated relative to
    the lineHeight rather than fontSize alone.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelBaseline.setter
  def labelBaseline(self, text):
    self._config(text)

  @property
  def labelColor(self):
    """  
    Text color for legend labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelColor.setter
  def labelColor(self, code):
    self._config(code)

  @property
  def labelFont(self):
    """  
    Font name for legend labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFont.setter
  def labelFont(self, text):
    self._config(text)

  @property
  def labelFontSize(self):
    """  
    Font size in pixels for legend labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFontSize.setter
  def labelFontSize(self, num):
    self._config(num)

  @property
  def labelFontStyle(self):
    """  
    Font style of legend labels (e.g., normal or italic).
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFontStyle.setter
  def labelFontStyle(self, text):
    self._config(text)

  @property
  def labelFontWeight(self):
    """  
    Font weight of legend labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelFontWeight.setter
  def labelFontWeight(self, text):
    self._config(text)

  @property
  def labelLimit(self):
    """  
    The maximum allowed length in pixels of legend labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelLimit.setter
  def labelLimit(self, num):
    self._config(num)

  @property
  def labelOffset(self):
    """  
    Offset in pixels between legend labels their corresponding symbol or gradient.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelOffset.setter
  def labelOffset(self, num):
    self._config(num)

  @property
  def labelOpacity(self):
    """  
    Opacity of legend labels.
    â‰¥ 4.1

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelOpacity.setter
  def labelOpacity(self, num):
    self._config(num)

  @property
  def labelOverlap(self):
    """  
    The strategy to use for resolving overlap of labels in gradient legends.
    If false, no overlap reduction is attempted.
    If set to true (default) or "parity", a strategy of removing every other label is used.
    If set to "greedy", a linear scan of the labels is performed, removing any label that overlaps with the last visible label.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelOverlap.setter
  def labelOverlap(self, text):
    self._config(text)

  @property
  def labelSeparation(self):
    """  
    The minimum separation that must be between label bounding boxes for them to be considered non-overlapping (default 0).
    This property is ignored if labelOverlap resolution is not enabled.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @labelSeparation.setter
  def labelSeparation(self, num):
    self._config(num)

  @property
  def legendX(self):
    """  
    The pixel x-coordinate of the legend group.
    Only applied if the orient value is "none".
    â‰¥ 5.4

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @legendX.setter
  def legendX(self, num):
    self._config(num)

  @property
  def legendY(self):
    """  
    The pixel y-coordinate of the legend group.
    Only applied if the orient value is "none".
    â‰¥ 5.4

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @legendY.setter
  def legendY(self, num):
    self._config(num)

  @property
  def symbolDash(self):
    """  
    Stroke dash of symbol outlines (or [] for solid lines).
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolDash.setter
  def symbolDash(self, values):
    self._config(values)

  @property
  def symbolDashOffset(self):
    """  
    The pixel offset at which to start the symbol dash array.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolDashOffset.setter
  def symbolDashOffset(self, num):
    self._config(num)

  @property
  def symbolFillColor(self):
    """  
    Fill color for legend symbols.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolFillColor.setter
  def symbolFillColor(self, code):
    self._config(code)

  @property
  def symbolLimit(self):
    """  
    The maximum number of allowed entries for a symbol legend.
    If the number of entries exceeds the limit, entries will be dropped and replaced with an ellipsis.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolLimit.setter
  def symbolLimit(self, num):
    self._config(num)

  @property
  def symbolOffset(self):
    """  
    Horizontal pixel offset for legend symbols.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolOffset.setter
  def symbolOffset(self, num):
    self._config(num)

  @property
  def symbolOpacity(self):
    """  
    Opacity of legend symbols.
    â‰¥ 4.1

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolOpacity.setter
  def symbolOpacity(self, num):
    self._config(num)

  @property
  def symbolSize(self):
    """  
    Default symbol area size (in pixels2).

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolSize.setter
  def symbolSize(self, num):
    self._config(num)

  @property
  def symbolStrokeColor(self):
    """  
    Stroke color for legend symbols.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolStrokeColor.setter
  def symbolStrokeColor(self, code):
    self._config(code)

  @property
  def symbolStrokeWidth(self):
    """  
    Default legend symbol stroke width.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolStrokeWidth.setter
  def symbolStrokeWidth(self, num):
    self._config(num)

  @property
  def symbolType(self):
    """  
    Default symbol mark shape type (such as "circle") for legend symbols.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @symbolType.setter
  def symbolType(self, text):
    self._config(text)

  @property
  def tickCount(self):
    """  
    The desired number of tick values for quantitative legends.
    For scales of type time or utc, the tick count can instead be a time interval specifier.
    Legal string values are "millisecond", "second", "minute", "hour", "day", "week", "month", and "year".
    Alternatively, an object-valued interval specifier of the form {"interval": "month", "step": 3} includes a desired
    number of interval steps.
    Here, ticks are generated for each quarter (Jan, Apr, Jul, Oct) boundary.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickCount.setter
  def tickCount(self, text):
    self._config(text)

  @property
  def tickMinStep(self):
    """  
    The minimum desired step between tick values for quantitative legends, in terms of scale domain values.
    For example, a value of 1 indicates that ticks should not be less than 1 unit apart.
    If tickMinStep is specified, the tickCount value will be adjusted, if necessary, to enforce the minimum step value.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @tickMinStep.setter
  def tickMinStep(self, num):
    self._config(num)

  @property
  def title(self):
    """  
    The title for the legend (none by default).
    For versions â‰¥ 5.7, a string array specifies a title with multiple lines of text.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @title.setter
  def title(self, text):
    self._config(text)

  @property
  def titleAnchor(self):
    """  
    The anchor position for placing the legend title.
    One of "start", "middle", "end", or null (default, for automatic determination).
    For example, with a titleOrient of "top" these anchor positions map to a left-, center-, or right-aligned title
    relative to the legend contents.
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleAnchor.setter
  def titleAnchor(self, text):
    self._config(text)

  @property
  def titleAlign(self):
    """  
    Horizontal text alignment of the legend title.
    One of "left", "center", or "right".
    If specified, this value overrides automatic alignment based on the titleOrient and titleAnchor values.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleAlign.setter
  def titleAlign(self, text):
    self._config(text)

  @property
  def titleBaseline(self):
    """  
    Vertical text baseline of the legend title.
    One of alphabetic (default), top, middle, bottom, line-top, or line-bottom.
    The line-top and line-bottom values â‰¥ 5.10 operate similarly to top and bottom, but are calculated relative to
    the lineHeight rather than fontSize alone.
    If specified, this value overrides the automatic baseline based on the titleOrient and titleAnchor values.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleBaseline.setter
  def titleBaseline(self, text):
    self._config(text)

  @property
  def titleColor(self):
    """  
    Text color of the legend title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleColor.setter
  def titleColor(self, code):
    self._config(code)

  @property
  def titleFont(self):
    """  
    Font name of the legend title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleFont.setter
  def titleFont(self, text):
    self._config(text)

  @property
  def titleFontSize(self):
    """  
    Font size in pixels of the legend title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleFontSize.setter
  def titleFontSize(self, num):
    self._config(num)

  @property
  def titleFontStyle(self):
    """  
    Font style of the legend title (e.g., normal or italic).
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleFontStyle.setter
  def titleFontStyle(self, text):
    self._config(text)

  @property
  def titleFontWeight(self):
    """  
    Font weight of the legend title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleFontWeight.setter
  def titleFontWeight(self, text):
    self._config(text)

  @property
  def titleLimit(self):
    """  
    The maximum allowed length in pixels of the legend title.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleLimit.setter
  def titleLimit(self, num):
    self._config(num)

  @property
  def titleLineHeight(self):
    """  
    Line height in pixels for multi-line title text or title text with "line-top" or "line-bottom" baseline.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleLineHeight.setter
  def titleLineHeight(self, num):
    self._config(num)

  @property
  def titleOpacity(self):
    """  
    Opacity of the legend title.
    â‰¥ 4.1

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleOpacity.setter
  def titleOpacity(self, num):
    self._config(num)

  @property
  def titleOrient(self):
    """  
    The orientation of the title legend, determining where it is placed relative to the legend contents.
    One of "top" (default), "left", "bottom", or "right".
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titleOrient.setter
  def titleOrient(self, text):
    self._config(text)

  @property
  def titlePadding(self):
    """  
    The padding between the legend title and entries.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @titlePadding.setter
  def titlePadding(self, num):
    self._config(num)

  @property
  def values(self):
    """  
    Explicitly set the visible legend values.
    The array entries should be legal values in the backing scale domain.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @values.setter
  def values(self, values):
    self._config(values)

  @property
  def zindex(self):
    """  
    The integer z-index indicating the layering of the legend group relative to other axis, mark, and legend groups.
    The default value is 0.

    Related Pages:

      https://vega.github.io/vega/docs/axes/
    """
    return self._config_get()

  @zindex.setter
  def zindex(self, num):
    self._config(num)


class OptTitle(Options):

  @property
  def text(self):
    """  
    Required.
    The title text.
    For versions â‰¥ 5.7, a string array specifies multiple lines of text.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @text.setter
  def text(self, text):
    self._config(text)

  @property
  def orient(self):
    """  
    The orientation of the title and subtitle relative to the chart.
    One of top (the default), bottom, left, or right.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @orient.setter
  def orient(self, text):
    self._config(text)

  @property
  def align(self):
    """  
    Horizontal text alignment of the title and subtitle.
    If specified, this value overrides automatic alignment based on the anchor value.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @align.setter
  def align(self, text):
    self._config(text)

  @property
  def anchor(self):
    """  
    The anchor position for placing the title and subtitle.
    One of start, middle (the default), or end.
    For example, with an orientation of top these anchor positions map to a left-, center-, or right-aligned title.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @anchor.setter
  def anchor(self, text):
    self._config(text)

  @property
  def angle(self):
    """  
    Angle in degrees of the title and subtitle text.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @angle.setter
  def angle(self, num):
    self._config(num)

  @property
  def baseline(self):
    """  
    Vertical baseline of the title and subtitle text.
    One of alphabetic (default), top, middle, bottom, line-top, or line-bottom.
    The line-top and line-bottom values â‰¥ 5.10 operate similarly to top and bottom, but are calculated relative to the lineHeight rather than fontSize alone.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @baseline.setter
  def baseline(self, text):
    self._config(text)

  @property
  def color(self):
    """  
    Text color of the title text.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @color.setter
  def color(self, code):
    self._config(code)

  @property
  def dx(self):
    """  
    Horizontal offset added to the title and subtitle x-coordinate.
    â‰¥ 5.2

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @dx.setter
  def dx(self, num):
    self._config(num)

  @property
  def dy(self):
    """  
    Vertical offset added to the title and subtitle y-coordinate.
    â‰¥ 5.2

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @dy.setter
  def dy(self, num):
    self._config(num)

  @property
  def font(self):
    """  
    Font name of the title text.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @font.setter
  def font(self, text):
    self._config(text)

  @property
  def fontSize(self):
    """  
    Font size in pixels of the title text.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @fontSize.setter
  def fontSize(self, num):
    self._config(num)

  @property
  def fontStyle(self):
    """  
    Font style of the title text (e.g., normal or italic).
    â‰¥ 5.0

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @fontStyle.setter
  def fontStyle(self, text):
    self._config(text)

  @property
  def fontWeight(self):
    """  
    Font weight of the title text.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @fontWeight.setter
  def fontWeight(self, text):
    self._config(text)

  @property
  def frame(self):
    """  
    The reference frame for the anchor position, one of "bounds" (the default, to anchor relative to the full bounding box) or "group" (to anchor relative to the group width or height).

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @frame.setter
  def frame(self, text):
    self._config(text)

  @property
  def interactive(self):
    """  
    A boolean flag indicating if the title element should respond to input events such as mouse hover.
    Deprecated: use a custom encode block instead.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @interactive.setter
  def interactive(self, flag):
    self._config(flag)

  @property
  def limit(self):
    """  
    The maximum allowed length in pixels of title and subtitle text.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @limit.setter
  def limit(self, num):
    self._config(num)

  @property
  def lineHeight(self):
    """  
    Line height in pixels for multi-line title text or title text with "line-top" or "line-bottom" baseline.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @lineHeight.setter
  def lineHeight(self, num):
    self._config(num)

  @property
  def name(self):
    """  
    A mark name property to apply to the title text mark.
    Deprecated: use a custom encode block instead.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def offset(self):
    """  
    The orthogonal offset in pixels by which to displace the title from its position along the edge of the chart.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @offset.setter
  def offset(self, num):
    self._config(num)

  @property
  def style(self):
    """  
    A mark style property to apply to the title text mark.
    If not specified, a default style of "group-title" is applied.
    Deprecated: use a custom encode block instead.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @style.setter
  def style(self, text):
    self._config(text)

  @property
  def subtitle(self):
    """  
    Optional subtitle text, placed beneath the primary text.
    A string array specifies multiple lines of text.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @subtitle.setter
  def subtitle(self, text):
    self._config(text)

  @property
  def subtitleColor(self):
    """  
    Text color of the subtitle text.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @subtitleColor.setter
  def subtitleColor(self, code):
    self._config(code)

  @property
  def subtitleFont(self):
    """  
    Font name of the subtitle text.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @subtitleFont.setter
  def subtitleFont(self, text):
    self._config(text)

  @property
  def subtitleFontSize(self):
    """  
    Font size in pixels of the subtitle text.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @subtitleFontSize.setter
  def subtitleFontSize(self, num):
    self._config(num)

  @property
  def subtitleFontStyle(self):
    """  
    Font style of the subtitle text (e.g., normal or italic).
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @subtitleFontStyle.setter
  def subtitleFontStyle(self, text):
    self._config(text)

  @property
  def subtitleFontWeight(self):
    """  
    Font weight of the subtitle text.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @subtitleFontWeight.setter
  def subtitleFontWeight(self, text):
    self._config(text)

  @property
  def subtitleLineHeight(self):
    """  
    Line height in pixels for multi-line subtitle text.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @subtitleLineHeight.setter
  def subtitleLineHeight(self, num):
    self._config(num)

  @property
  def subtitlePadding(self):
    """  
    Padding in pixels between title and subtitle text.
    â‰¥ 5.7

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @subtitlePadding.setter
  def subtitlePadding(self, num):
    self._config(num)

  @property
  def zindex(self):
    """  
    The integer z-index indicating the layering of the title group relative to other axis, mark, and legend groups.
    The default value is 0.

    Related Pages:

      https://vega.github.io/vega/docs/title/
    """
    return self._config_get()

  @zindex.setter
  def zindex(self, num):
    self._config(num)


class OptTransAgg(Options):

  @property
  def cross(self):
    """  
    Indicates if the full cross-product of all groupby values should be included in the aggregate output (default false).
    If set to true, all possible combinations of groupby field values will be considered and zero count groups will be generated and returned for combinations that do not occur in the data itself.
    Cross-product output act as if the drop parameter is false.
    In the case of streaming updates, the number of output groups will increase if new groupby field values are observed; all prior groups will be retained.
    This parameter can be useful for generating facets that include groups for all possible partitions of the data.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    return self._config_get()

  @cross.setter
  def cross(self, flag):
    self._config(flag)

  @property
  def drop(self):
    """  
    Indicates if empty (zero count) groups should be dropped (default true).
    When a data stream updates (for example, in response to interactive filtering), aggregation groups may become empty.
    By default, the group is removed from the output.
    However, in some cases (such as histograms), one may wish to retain empty groups.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    return self._config_get()

  @drop.setter
  def drop(self, flag):
    self._config(flag)


class OptData(Options):

  @property
  def name(self):
    """  
    Required.
    A unique name for the data set.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    return self._config_get()

  @name.setter
  def name(self, text):
    self._config(text)

  @property
  def source(self):
    """  
    The name of one or more data sets to use as the source for this data set.
    The source property is useful in combination with a transform pipeline to derive new data.
    If string-valued, indicates the name of the source data set.
    If array-valued, specifies a collection of data source names that should be merged (unioned) together.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    return self._config_get()

  @source.setter
  def source(self, text):
    self._config(text)

  @property
  def url(self):
    """  
    A URL from which to load the data set.
    Use the format property to ensure the loaded data is correctly parsed.
    If the format property is not specified, the data is assumed to be in a row-oriented JSON format.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    return self._config_get()

  @url.setter
  def url(self, text):
    self._config(text)

  @property
  def values(self):
    """  
    The full data set, included inline.
    The values property allows data to be included directly within the specification itself.
    While most commonly an array of objects, other data types (such as CSV strings) may be used, subject to the format settings.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    return self._config_get()

  @values.setter
  def values(self, record):
    self._config(record)

  @property
  def async_loading(self):
    """  
    ≥ 5.9 A boolean flag (default false) indicating if dynamic data loading or reformatting should occur asynchronously.
    If true, dataflow evaluation will complete, data loading will occur in the background, and the dataflow will be re-evaluated when loading is complete.
    If false, dataflow evaluation will block until loading is complete and then continue within the same evaluation cycle.
    The use of async can allow multiple dynamic datasets to be loaded simultaneously while still supporting interactivity.
    However, the use of async can cause datasets to remain empty while the rest of the dataflow is evaluated, potentially affecting downstream computation.

    Related Pages:

      https://vega.github.io/vega/docs/transforms/aggregate/
    """
    return self._config_get()

  @async_loading.setter
  def async_loading(self, flag):
    self._config(flag)


class OptEncodingAxe(Options):

  @property
  def aggregate(self):
    return self._config_get()

  @aggregate.setter
  def aggregate(self, text):
    self._config(text)

  @property
  def aggregates(self):
    """  
    Graphical marks visually encode data using geometric primitives such as rectangles, lines, and plotting symbols.

    Related Pages:

      https://vega.github.io/vega/docs/marks/
    """
    return EnumAggregateTypes(self, "aggregate")

  @property
  def bin(self):
    return self._config_get()

  @bin.setter
  def bin(self, flag):
    self._config(flag)

  @property
  def field(self):
    return self._config_get()

  @field.setter
  def field(self, text):
    self._config(text)

  @property
  def type(self):
    return self._config_get()

  @type.setter
  def type(self, text):
    self._config(text)

  @property
  def data(self):
    return self._config_get()

  @data.setter
  def data(self, text):
    self._config(text)

  @property
  def datum(self):
    return self._config_get()

  @datum.setter
  def datum(self, values):
    self._config(values)

  @property
  def axis(self):
    """

    :rtype: OptEncodingAxe
    """
    return self._config_sub_data("axis", OptAxe)

  @property
  def legend(self):
    """

    :rtype: OptLegend
    """
    return self._config_sub_data("legend", OptLegend)


class OptEncoding(Options):

  @property
  def x(self):
    """

    :rtype: OptEncodingAxe
    """
    return self._config_sub_data("x", OptEncodingAxe)

  @property
  def y(self):
    return self._config_sub_data("y", OptEncodingAxe)

  @property
  def color(self):
    return self._config_sub_data("color", OptEncodingAxe)

  @property
  def size(self):
    """

    https://vega.github.io/vega-lite/examples/circle_github_punchcard.html

    :return:
    """
    return self._config_sub_data("size", OptEncodingAxe)

  @property
  def text(self):
    return self._config_get()

  @text.setter
  def text(self, value):
    self._config(value)


class OptRepeat(Options):

  @property
  def layer(self):
    return self._config_get()

  @layer.setter
  def layer(self, values):
    self._config(values)


class OptSpec(Options):

  @property
  def mark(self):
    return self._config_get()

  @mark.setter
  def mark(self, value):
    self._config(value)

  @property
  def encoding(self):
    return self._config_sub_data("encoding", OptEncoding)

  def add_signal(self, name, value=None):
    """  
    Signals are dynamic variables that parameterize a visualization and can drive interactive behaviors.

    Usage::

      https://vega.github.io/vega/docs/signals/

    :param name: String. A unique name for the signal.

    :rtype: OptSignal
    """
    s = self._config_sub_data_enum("signals", OptSignal)
    s.name = name
    s.value = value
    return s


class OptionsLayer(OptChart.OptionsChart):

  @property
  def description(self):
    """  
    A text description of the visualization.
    In versions ≥ 5.10, the description determines the aria-label attribute for the container element of a Vega view.

    Related Pages:

      https://vega.github.io/vega/docs/specification/
    """
    return self._config_get()

  @description.setter
  def description(self, text):
    self._config(text)

  @property
  def width(self):
    """  
    The width in pixels of the data rectangle.
    If signal-valued ≥ 5.10, the provided expression is used as the update property for the underlying width signal definition.

    Related Pages:

      https://vega.github.io/vega/docs/specification/
    """
    return self._config_get()

  @width.setter
  def width(self, num):
    self._config(num)

  @property
  def height(self):
    """  
    The height in pixels of the data rectangle.
    If signal-valued ≥ 5.10, the provided expression is used as the update property for the underlying height signal definition.

    Related Pages:

      https://vega.github.io/vega/docs/specification/
    """
    return self._config_get()

  @height.setter
  def height(self, num):
    self._config(num)

  @property
  def padding(self):
    """  
    The padding in pixels to add around the visualization.
    If a number, specifies padding for all sides.
    If an object, the value should have the format {"left": 5, "top": 5, "right": 5, "bottom": 5}.
    Padding is applied after autosize layout completes.
    If signal-valued ≥ 5.10, the provided expression is used as the update property for the underlying padding signal
    definition, and should evaluate to either a padding object or number.

    Related Pages:

      https://vega.github.io/vega/docs/specification/
    """
    return self._config_get()

  @padding.setter
  def padding(self, num):
    self._config(num)

  @property
  def autosize(self):
    """  
    Sets how the visualization size should be determined.
    If a string, should be one of pad (default), fit, fit-x, fit-y, or none.
    Object values can additionally specify parameters for content sizing and automatic resizing.
    See the autosize section below for more.
    If signal-valued ≥ 5.10, the provided expression is used as the update property for the underlying autosize signal
    definition, and should evaluate to a complete autosize object.

    Related Pages:

      https://vega.github.io/vega/docs/specification/
    """
    return self._config_get()

  @autosize.setter
  def autosize(self, text):
    self._config(text)

  @property
  def data(self):
    """

    :rtype: OptData
    """
    return self._config_sub_data("data", OptData)

  @property
  def spec(self):
    """

    :rtype: OptSpec
    """
    return self._config_sub_data("spec", OptSpec)

  @property
  def repeat(self):
    """

    :rtype: OptData
    """
    return self._config_sub_data("repeat", OptRepeat)

  def parent_width(self, percent):
    self._config("%s / 100 * (function(component){return component.clientWidth - (parseFloat(component.style.paddingLeft || 0) + parseFloat(component.style.paddingRight || 0)) })(%s)" % (percent, self.component.dom.varId), name="width", js_type=True)

  @property
  def mark(self):
    return self._config_get()

  @mark.setter
  def mark(self, value):
    self._config(value)

  @property
  def marks(self):
      """  Graphical marks visually encode data using geometric primitives such as rectangles, lines, and plotting symbols.

      Related Pages:

        https://vega.github.io/vega/docs/marks/
      """
      return EnumMarks(self, "mark")

  @property
  def encoding(self):
    return self._config_sub_data("encoding", OptEncoding)

  def add_projection(self, name):
    """  
    Cartographic projections map (longitude, latitude) pairs to projected (x, y) coordinates.

    Related Pages:

      https://vega.github.io/vega/docs/projections/

    :param name: String. A unique name for the projection.

    :rtype: OptProjection
    """
    scale = self._config_sub_data_enum("projection", OptProjection)
    scale.name = name
    return scale

  def add_scale(self, name, range=None):
    """  
    Scales map data values (numbers, dates, categories, etc.) to visual values (pixels, colors, sizes).

    Related Pages:

      https://vega.github.io/vega/docs/scales/

    :param name: String. A unique name for the scale.
    :param range: String

    :rtype: OptScale
    """
    scale = self._config_sub_data_enum("scales", OptScale)
    scale.name = name
    if range is not None:
      scale.range = range
    return scale

  def add_axe(self, scale, orient):
    """  
    Axes visualize spatial scale mappings using ticks, grid lines and labels.

    Related Pages:

      https://vega.github.io/vega/docs/axes/

    :param scale: String. The name of the scale backing the axis component.
    :param orient: String. The orientation of the axis.

    :rtype: OptAxe
    """
    s = self._config_sub_data_enum("axes", OptAxe)
    s.scale = scale
    s.orient = orient
    return s

  def add_legend(self, kind, title=None):
    """  
    Legends visualize scale mappings for visual values such as color, shape and size.

    Related Pages:

      https://vega.github.io/vega/docs/legends/

    Usage::

      https://vega.github.io/vega/examples/interactive-legend/

    :param kind: String. The type of legend to include.
    :param title: String. The title for the legend (none by default).

    :rtype: OptLegend
    """
    s = self._config_sub_data_enum("legends", OptLegend)
    s.type = kind
    if title is not None:
      s.title = title
    return s

  def add_signal(self, name, value=None):
    """  
    Signals are dynamic variables that parameterize a visualization and can drive interactive behaviors.

    Usage::

      https://vega.github.io/vega/docs/signals/

    :param name: String. A unique name for the signal.

    :rtype: OptSignal
    """
    s = self._config_sub_data_enum("signals", OptSignal)
    s.name = name
    s.value = value
    return s

  def add_mark(self, kind):
    """  
    Graphical marks visually encode data using geometric primitives such as rectangles, lines, and plotting symbols.

    Usage::

      https://vega.github.io/vega/docs/marks/

    :param kind: String. The graphical mark type.

    :rtype: OptMark
    """
    s = self._config_sub_data_enum("mark", OptMark)
    s.type = kind
    return s

  def add_layer(self):
    """  

    """
    s = self._config_sub_data_enum("layer", OptionsLayer)
    return s


class OptionsChart(OptionsLayer):
  component_properties = ("schema", )
  with_builder = False

  @property
  def schema(self):
    """
    The URL for the Vega schema.

    https://vega.github.io/vega/docs/specification/
    """
    return self._config_get("https://vega.github.io/schema/vega/v5.json", name="$schema")

  @schema.setter
  def schema(self, value):
    self._config(value, name="$schema")
