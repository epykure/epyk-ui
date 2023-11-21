from epyk.core.html.options import Options
from typing import Any

        
class OptionSonificationPointgrouping(Options):

    @property
    def algorithm(self):
        """The grouping algorithm, deciding which points to keep when grouping a set of points together.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("minmax")

    @algorithm.setter
    def algorithm(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Whether or not to group points.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def groupTimespan(self):
        """The size of each group in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(15)

    @groupTimespan.setter
    def groupTimespan(self, num: float): self._config(num, js_type=False)

    @property
    def prop(self):
        """The data property for each point to compare when deciding which points to keep in the group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("y")

    @prop.setter
    def prop(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsActivewhen(Options):

    @property
    def crossingDown(self):
        """Track is only active when <code>prop</code> was above, and is now at or below this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @crossingDown.setter
    def crossingDown(self, num: float): self._config(num, js_type=False)

    @property
    def crossingUp(self):
        """Track is only active when <code>prop</code> was below, and is now at or above this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @crossingUp.setter
    def crossingUp(self, num: float): self._config(num, js_type=False)

    @property
    def max(self):
        """Track is only active when <code>prop</code> is below or at this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """Track is only active when <code>prop</code> is above or at this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def prop(self):
        """The point property to compare, for example <code>y</code> or <code>x</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @prop.setter
    def prop(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationDefaultspeechoptionsActivewhen(Options):

    @property
    def crossingDown(self):
        """Track is only active when <code>prop</code> was above, and is now at or below this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @crossingDown.setter
    def crossingDown(self, num: float): self._config(num, js_type=False)

    @property
    def crossingUp(self):
        """Track is only active when <code>prop</code> was below, and is now at or above this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @crossingUp.setter
    def crossingUp(self, num: float): self._config(num, js_type=False)

    @property
    def max(self):
        """Track is only active when <code>prop</code> is below or at this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """Track is only active when <code>prop</code> is above or at this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def prop(self):
        """The point property to compare, for example <code>y</code> or <code>x</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @prop.setter
    def prop(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationEvents(Options):

    @property
    def afterUpdate(self):
        """Called after updating the sonification.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @afterUpdate.setter
    def afterUpdate(self, value: Any): self._config(value, js_type=False)

    @property
    def beforePlay(self):
        """Called immediately when a play is requested.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @beforePlay.setter
    def beforePlay(self, value: Any): self._config(value, js_type=False)

    @property
    def beforeUpdate(self):
        """Called before updating the sonification.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @beforeUpdate.setter
    def beforeUpdate(self, value: Any): self._config(value, js_type=False)

    @property
    def onBoundaryHit(self):
        """Called when attempting to play an adjacent point or series, and there is none.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @onBoundaryHit.setter
    def onBoundaryHit(self, value: Any): self._config(value, js_type=False)

    @property
    def onEnd(self):
        """Called when play is completed.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @onEnd.setter
    def onEnd(self, value: Any): self._config(value, js_type=False)

    @property
    def onPlay(self):
        """Called on play.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @onPlay.setter
    def onPlay(self, value: Any): self._config(value, js_type=False)

    @property
    def onSeriesEnd(self):
        """Called when finished playing a series.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @onSeriesEnd.setter
    def onSeriesEnd(self, value: Any): self._config(value, js_type=False)

    @property
    def onSeriesStart(self):
        """Called on the beginning of playing a series.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @onSeriesStart.setter
    def onSeriesStart(self, value: Any): self._config(value, js_type=False)

    @property
    def onStop(self):
        """Called on pause, cancel, or if play is completed.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @onStop.setter
    def onStop(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksActivewhen(Options):

    @property
    def crossingDown(self):
        """Track is only active when <code>prop</code> was above, and is now at or below this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @crossingDown.setter
    def crossingDown(self, num: float): self._config(num, js_type=False)

    @property
    def crossingUp(self):
        """Track is only active when <code>prop</code> was below, and is now at or above this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @crossingUp.setter
    def crossingUp(self, num: float): self._config(num, js_type=False)

    @property
    def max(self):
        """Track is only active when <code>prop</code> is below or at this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """Track is only active when <code>prop</code> is above or at this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def prop(self):
        """The point property to compare, for example <code>y</code> or <code>x</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @prop.setter
    def prop(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationGlobaltracksActivewhen(Options):

    @property
    def crossingDown(self):
        """Track is only active when <code>prop</code> was above, and is now at or below this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @crossingDown.setter
    def crossingDown(self, num: float): self._config(num, js_type=False)

    @property
    def crossingUp(self):
        """Track is only active when <code>prop</code> was below, and is now at or above this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @crossingUp.setter
    def crossingUp(self, num: float): self._config(num, js_type=False)

    @property
    def max(self):
        """Track is only active when <code>prop</code> is below or at this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """Track is only active when <code>prop</code> is above or at this value.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def prop(self):
        """The point property to compare, for example <code>y</code> or <code>x</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @prop.setter
    def prop(self, text: str): self._config(text, js_type=False)

        
class OptionSonification(Options):

    @property
    def afterSeriesWait(self):
        """The time to wait in milliseconds after each data series when playing the series one after the other.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(700)

    @afterSeriesWait.setter
    def afterSeriesWait(self, num: float): self._config(num, js_type=False)

    @property
    def defaultInstrumentOptions(self) -> 'OptionSonificationDefaultinstrumentoptions':
        """Default sonification options for all instrument tracks. """
        return self._config_sub_data("defaultInstrumentOptions", OptionSonificationDefaultinstrumentoptions)

    @property
    def defaultSpeechOptions(self) -> 'OptionSonificationDefaultspeechoptions':
        """Default sonification options for all speech tracks. """
        return self._config_sub_data("defaultSpeechOptions", OptionSonificationDefaultspeechoptions)

    @property
    def duration(self):
        """The total duration of the sonification, in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(6000)

    @duration.setter
    def duration(self, num: float): self._config(num, js_type=False)

    @property
    def enabled(self):
        """Enable sonification functionality for the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def events(self) -> 'OptionSonificationEvents':
        """Set up event handlers for the sonification. """
        return self._config_sub_data("events", OptionSonificationEvents)

    @property
    def globalContextTracks(self) -> 'OptionSonificationGlobalcontexttracks':
        """Context tracks to add globally, an array of either instrument tracks, speech tracks, or a mix. """
        return self._config_sub_data("globalContextTracks", OptionSonificationGlobalcontexttracks)

    @property
    def globalTracks(self) -> 'OptionSonificationGlobaltracks':
        """Global tracks to add to every series. """
        return self._config_sub_data("globalTracks", OptionSonificationGlobaltracks)

    @property
    def masterVolume(self):
        """Overall/master volume for the sonification, from 0 to 1.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(0.7)

    @masterVolume.setter
    def masterVolume(self, num: float): self._config(num, js_type=False)

    @property
    def order(self):
        """What order to play the data series in, either <code>sequential</code> where the series play individually one after the other, or <code>simultaneous</code> where the series play all at once.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("sequential")

    @order.setter
    def order(self, text: str): self._config(text, js_type=False)

    @property
    def pointGrouping(self) -> 'OptionSonificationPointgrouping':
        """Options for grouping data points together when sonifying. """
        return self._config_sub_data("pointGrouping", OptionSonificationPointgrouping)

    @property
    def showCrosshair(self):
        """Show X and Y axis crosshairs (if they exist) as the chart plays.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @showCrosshair.setter
    def showCrosshair(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showTooltip(self):
        """Show tooltip as the chart plays.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @showTooltip.setter
    def showTooltip(self, flag: bool): self._config(flag, js_type=False)

    @property
    def updateInterval(self):
        """How long to wait between each recomputation of the sonification, if the chart updates rapidly.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(200)

    @updateInterval.setter
    def updateInterval(self, num: float): self._config(num, js_type=False)

        
class OptionSonificationGlobaltracksPointgrouping(Options):

    @property
    def algorithm(self):
        """The grouping algorithm, deciding which points to keep when grouping a set of points together.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("minmax")

    @algorithm.setter
    def algorithm(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Whether or not to group points.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def groupTimespan(self):
        """The size of each group in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(15)

    @groupTimespan.setter
    def groupTimespan(self, num: float): self._config(num, js_type=False)

    @property
    def prop(self):
        """The data property for each point to compare when deciding which points to keep in the group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("y")

    @prop.setter
    def prop(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationGlobaltracksMappingVolume(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingTremoloSpeed(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingTremoloDepth(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingTremolo(Options):

    @property
    def depth(self) -> 'OptionSonificationGlobaltracksMappingTremoloDepth':
        """Map to tremolo depth, from 0 to 1. """
        return self._config_sub_data("depth", OptionSonificationGlobaltracksMappingTremoloDepth)

    @property
    def speed(self) -> 'OptionSonificationGlobaltracksMappingTremoloSpeed':
        """Map to tremolo speed, from 0 to 1. """
        return self._config_sub_data("speed", OptionSonificationGlobaltracksMappingTremoloSpeed)

        
class OptionSonificationGlobaltracksMappingTime(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingRate(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingPlaydelay(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingPitch(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("y")

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("c6")

    @max.setter
    def max(self, text: str): self._config(text, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("c2")

    @min.setter
    def min(self, text: str): self._config(text, js_type=False)

    @property
    def scale(self):
        """Map pitches to a musical scale.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @scale.setter
    def scale(self, value: Any): self._config(value, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("yAxis")

    @within.setter
    def within(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationGlobaltracksMappingPan(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingNoteduration(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingLowpassResonance(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingLowpassFrequency(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingLowpass(Options):

    @property
    def frequency(self) -> 'OptionSonificationGlobaltracksMappingLowpassFrequency':
        """Map to filter frequency in Hertz from 1 to 20,000Hz. """
        return self._config_sub_data("frequency", OptionSonificationGlobaltracksMappingLowpassFrequency)

    @property
    def resonance(self) -> 'OptionSonificationGlobaltracksMappingLowpassResonance':
        """Map to filter resonance in dB. """
        return self._config_sub_data("resonance", OptionSonificationGlobaltracksMappingLowpassResonance)

        
class OptionSonificationGlobaltracksMappingFrequency(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingHighpassFrequency(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingGapbetweennotes(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMapping(Options):

    @property
    def frequency(self) -> 'OptionSonificationGlobaltracksMappingFrequency':
        """Frequency in Hertz of notes. """
        return self._config_sub_data("frequency", OptionSonificationGlobaltracksMappingFrequency)

    @property
    def gapBetweenNotes(self) -> 'OptionSonificationGlobaltracksMappingGapbetweennotes':
        """Gap in milliseconds between notes if pitch is mapped to an array of notes. """
        return self._config_sub_data("gapBetweenNotes", OptionSonificationGlobaltracksMappingGapbetweennotes)

    @property
    def highpass(self) -> 'OptionSonificationGlobaltracksMappingHighpass':
        """Mapping options for the highpass filter. """
        return self._config_sub_data("highpass", OptionSonificationGlobaltracksMappingHighpass)

    @property
    def lowpass(self) -> 'OptionSonificationGlobaltracksMappingLowpass':
        """Mapping options for the lowpass filter. """
        return self._config_sub_data("lowpass", OptionSonificationGlobaltracksMappingLowpass)

    @property
    def noteDuration(self) -> 'OptionSonificationGlobaltracksMappingNoteduration':
        """Note duration determines for how long a note plays, in milliseconds. """
        return self._config_sub_data("noteDuration", OptionSonificationGlobaltracksMappingNoteduration)

    @property
    def pan(self) -> 'OptionSonificationGlobaltracksMappingPan':
        """Pan refers to the stereo panning position of the sound. """
        return self._config_sub_data("pan", OptionSonificationGlobaltracksMappingPan)

    @property
    def pitch(self) -> 'OptionSonificationGlobaltracksMappingPitch':
        """Musical pitch refers to how high or low notes are played. """
        return self._config_sub_data("pitch", OptionSonificationGlobaltracksMappingPitch)

    @property
    def playDelay(self) -> 'OptionSonificationGlobaltracksMappingPlaydelay':
        """Milliseconds to wait before playing, comes in addition to the time determined by the <code>time</code> mapping. """
        return self._config_sub_data("playDelay", OptionSonificationGlobaltracksMappingPlaydelay)

    @property
    def rate(self) -> 'OptionSonificationGlobaltracksMappingRate':
        """Rate mapping for speech tracks. """
        return self._config_sub_data("rate", OptionSonificationGlobaltracksMappingRate)

    @property
    def text(self):
        """Text mapping for speech tracks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def time(self) -> 'OptionSonificationGlobaltracksMappingTime':
        """Time mapping determines what time each point plays. """
        return self._config_sub_data("time", OptionSonificationGlobaltracksMappingTime)

    @property
    def tremolo(self) -> 'OptionSonificationGlobaltracksMappingTremolo':
        """Mapping options for tremolo effects. """
        return self._config_sub_data("tremolo", OptionSonificationGlobaltracksMappingTremolo)

    @property
    def volume(self) -> 'OptionSonificationGlobaltracksMappingVolume':
        """The volume of notes, from 0 to 1. """
        return self._config_sub_data("volume", OptionSonificationGlobaltracksMappingVolume)

        
class OptionSonificationGlobaltracks(Options):

    @property
    def activeWhen(self) -> 'OptionSonificationGlobaltracksActivewhen':
        """Define a condition for when a track should be active and not. """
        return self._config_sub_data("activeWhen", OptionSonificationGlobaltracksActivewhen)

    @property
    def instrument(self):
        """Instrument to use for playing.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("piano")

    @instrument.setter
    def instrument(self, text: str): self._config(text, js_type=False)

    @property
    def mapping(self) -> 'OptionSonificationGlobaltracksMapping':
        """Mapping options for the audio parameters. """
        return self._config_sub_data("mapping", OptionSonificationGlobaltracksMapping)

    @property
    def midiName(self):
        """Name to use for a track when exporting to MIDI.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @midiName.setter
    def midiName(self, text: str): self._config(text, js_type=False)

    @property
    def pointGrouping(self) -> 'OptionSonificationGlobaltracksPointgrouping':
        """Options for point grouping, specifically for instrument tracks. """
        return self._config_sub_data("pointGrouping", OptionSonificationGlobaltracksPointgrouping)

    @property
    def roundToMusicalNotes(self):
        """Round pitch mapping to musical notes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @roundToMusicalNotes.setter
    def roundToMusicalNotes(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showPlayMarker(self):
        """Show play marker (tooltip and/or crosshair) for a track.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @showPlayMarker.setter
    def showPlayMarker(self, flag: bool): self._config(flag, js_type=False)

    @property
    def type(self):
        """Type of track.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("instrument")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationGlobaltracksMappingHighpassResonance(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobaltracksMappingHighpass(Options):

    @property
    def frequency(self) -> 'OptionSonificationGlobaltracksMappingHighpassFrequency':
        """Map to filter frequency in Hertz from 1 to 20,000Hz. """
        return self._config_sub_data("frequency", OptionSonificationGlobaltracksMappingHighpassFrequency)

    @property
    def resonance(self) -> 'OptionSonificationGlobaltracksMappingHighpassResonance':
        """Map to filter resonance in dB. """
        return self._config_sub_data("resonance", OptionSonificationGlobaltracksMappingHighpassResonance)

        
class OptionSonificationGlobalcontexttracksPointgrouping(Options):

    @property
    def algorithm(self):
        """The grouping algorithm, deciding which points to keep when grouping a set of points together.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("minmax")

    @algorithm.setter
    def algorithm(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Whether or not to group points.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def groupTimespan(self):
        """The size of each group in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(15)

    @groupTimespan.setter
    def groupTimespan(self, num: float): self._config(num, js_type=False)

    @property
    def prop(self):
        """The data property for each point to compare when deciding which points to keep in the group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("y")

    @prop.setter
    def prop(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingVolume(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingTremoloSpeed(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingTremoloDepth(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingTremolo(Options):

    @property
    def depth(self) -> 'OptionSonificationGlobalcontexttracksMappingTremoloDepth':
        """Map to tremolo depth, from 0 to 1. """
        return self._config_sub_data("depth", OptionSonificationGlobalcontexttracksMappingTremoloDepth)

    @property
    def speed(self) -> 'OptionSonificationGlobalcontexttracksMappingTremoloSpeed':
        """Map to tremolo speed, from 0 to 1. """
        return self._config_sub_data("speed", OptionSonificationGlobalcontexttracksMappingTremoloSpeed)

        
class OptionSonificationGlobalcontexttracksMappingTime(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingRate(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingPlaydelay(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingPitch(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("y")

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("c6")

    @max.setter
    def max(self, text: str): self._config(text, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("c2")

    @min.setter
    def min(self, text: str): self._config(text, js_type=False)

    @property
    def scale(self):
        """Map pitches to a musical scale.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @scale.setter
    def scale(self, value: Any): self._config(value, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("yAxis")

    @within.setter
    def within(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingPan(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingNoteduration(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingLowpassResonance(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingLowpassFrequency(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingLowpass(Options):

    @property
    def frequency(self) -> 'OptionSonificationGlobalcontexttracksMappingLowpassFrequency':
        """Map to filter frequency in Hertz from 1 to 20,000Hz. """
        return self._config_sub_data("frequency", OptionSonificationGlobalcontexttracksMappingLowpassFrequency)

    @property
    def resonance(self) -> 'OptionSonificationGlobalcontexttracksMappingLowpassResonance':
        """Map to filter resonance in dB. """
        return self._config_sub_data("resonance", OptionSonificationGlobalcontexttracksMappingLowpassResonance)

        
class OptionSonificationGlobalcontexttracksMappingFrequency(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingHighpassFrequency(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingGapbetweennotes(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMapping(Options):

    @property
    def frequency(self) -> 'OptionSonificationGlobalcontexttracksMappingFrequency':
        """Frequency in Hertz of notes. """
        return self._config_sub_data("frequency", OptionSonificationGlobalcontexttracksMappingFrequency)

    @property
    def gapBetweenNotes(self) -> 'OptionSonificationGlobalcontexttracksMappingGapbetweennotes':
        """Gap in milliseconds between notes if pitch is mapped to an array of notes. """
        return self._config_sub_data("gapBetweenNotes", OptionSonificationGlobalcontexttracksMappingGapbetweennotes)

    @property
    def highpass(self) -> 'OptionSonificationGlobalcontexttracksMappingHighpass':
        """Mapping options for the highpass filter. """
        return self._config_sub_data("highpass", OptionSonificationGlobalcontexttracksMappingHighpass)

    @property
    def lowpass(self) -> 'OptionSonificationGlobalcontexttracksMappingLowpass':
        """Mapping options for the lowpass filter. """
        return self._config_sub_data("lowpass", OptionSonificationGlobalcontexttracksMappingLowpass)

    @property
    def noteDuration(self) -> 'OptionSonificationGlobalcontexttracksMappingNoteduration':
        """Note duration determines for how long a note plays, in milliseconds. """
        return self._config_sub_data("noteDuration", OptionSonificationGlobalcontexttracksMappingNoteduration)

    @property
    def pan(self) -> 'OptionSonificationGlobalcontexttracksMappingPan':
        """Pan refers to the stereo panning position of the sound. """
        return self._config_sub_data("pan", OptionSonificationGlobalcontexttracksMappingPan)

    @property
    def pitch(self) -> 'OptionSonificationGlobalcontexttracksMappingPitch':
        """Musical pitch refers to how high or low notes are played. """
        return self._config_sub_data("pitch", OptionSonificationGlobalcontexttracksMappingPitch)

    @property
    def playDelay(self) -> 'OptionSonificationGlobalcontexttracksMappingPlaydelay':
        """Milliseconds to wait before playing, comes in addition to the time determined by the <code>time</code> mapping. """
        return self._config_sub_data("playDelay", OptionSonificationGlobalcontexttracksMappingPlaydelay)

    @property
    def rate(self) -> 'OptionSonificationGlobalcontexttracksMappingRate':
        """Rate mapping for speech tracks. """
        return self._config_sub_data("rate", OptionSonificationGlobalcontexttracksMappingRate)

    @property
    def text(self):
        """Text mapping for speech tracks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def time(self) -> 'OptionSonificationGlobalcontexttracksMappingTime':
        """Time mapping determines what time each point plays. """
        return self._config_sub_data("time", OptionSonificationGlobalcontexttracksMappingTime)

    @property
    def tremolo(self) -> 'OptionSonificationGlobalcontexttracksMappingTremolo':
        """Mapping options for tremolo effects. """
        return self._config_sub_data("tremolo", OptionSonificationGlobalcontexttracksMappingTremolo)

    @property
    def volume(self) -> 'OptionSonificationGlobalcontexttracksMappingVolume':
        """The volume of notes, from 0 to 1. """
        return self._config_sub_data("volume", OptionSonificationGlobalcontexttracksMappingVolume)

        
class OptionSonificationGlobalcontexttracks(Options):

    @property
    def activeWhen(self) -> 'OptionSonificationGlobalcontexttracksActivewhen':
        """Define a condition for when a track should be active and not. """
        return self._config_sub_data("activeWhen", OptionSonificationGlobalcontexttracksActivewhen)

    @property
    def instrument(self):
        """Instrument to use for playing.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("piano")

    @instrument.setter
    def instrument(self, text: str): self._config(text, js_type=False)

    @property
    def mapping(self) -> 'OptionSonificationGlobalcontexttracksMapping':
        """Mapping options for the audio parameters. """
        return self._config_sub_data("mapping", OptionSonificationGlobalcontexttracksMapping)

    @property
    def midiName(self):
        """Name to use for a track when exporting to MIDI.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @midiName.setter
    def midiName(self, text: str): self._config(text, js_type=False)

    @property
    def pointGrouping(self) -> 'OptionSonificationGlobalcontexttracksPointgrouping':
        """Options for point grouping, specifically for instrument tracks. """
        return self._config_sub_data("pointGrouping", OptionSonificationGlobalcontexttracksPointgrouping)

    @property
    def roundToMusicalNotes(self):
        """Round pitch mapping to musical notes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @roundToMusicalNotes.setter
    def roundToMusicalNotes(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showPlayMarker(self):
        """Show play marker (tooltip and/or crosshair) for a track.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @showPlayMarker.setter
    def showPlayMarker(self, flag: bool): self._config(flag, js_type=False)

    @property
    def timeInterval(self):
        """Set a context track to play periodically every <code>timeInterval</code> milliseconds while the sonification is playing.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @timeInterval.setter
    def timeInterval(self, num: float): self._config(num, js_type=False)

    @property
    def type(self):
        """Type of track.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("instrument")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

    @property
    def valueInterval(self):
        """Set a context track to play periodically every <code>valueInterval</code> units of a data property <code>valueProp</code> while the sonification is playing.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @valueInterval.setter
    def valueInterval(self, num: float): self._config(num, js_type=False)

    @property
    def valueMapFunction(self):
        """How to map context events to time when using the <code>valueInterval</code> option.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("linear")

    @valueMapFunction.setter
    def valueMapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def valueProp(self):
        """The point property to play context for when using <code>valueInterval</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("x")

    @valueProp.setter
    def valueProp(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingHighpassResonance(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationGlobalcontexttracksMappingHighpass(Options):

    @property
    def frequency(self) -> 'OptionSonificationGlobalcontexttracksMappingHighpassFrequency':
        """Map to filter frequency in Hertz from 1 to 20,000Hz. """
        return self._config_sub_data("frequency", OptionSonificationGlobalcontexttracksMappingHighpassFrequency)

    @property
    def resonance(self) -> 'OptionSonificationGlobalcontexttracksMappingHighpassResonance':
        """Map to filter resonance in dB. """
        return self._config_sub_data("resonance", OptionSonificationGlobalcontexttracksMappingHighpassResonance)

        
class OptionSonificationDefaultspeechoptionsPointgrouping(Options):

    @property
    def algorithm(self):
        """The grouping algorithm, deciding which points to keep when grouping a set of points together.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("last")

    @algorithm.setter
    def algorithm(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Whether or not to group points.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def groupTimespan(self):
        """The size of each group in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(15)

    @groupTimespan.setter
    def groupTimespan(self, num: float): self._config(num, js_type=False)

    @property
    def prop(self):
        """The data property for each point to compare when deciding which points to keep in the group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("y")

    @prop.setter
    def prop(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationDefaultspeechoptionsMappingVolume(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultspeechoptionsMappingTime(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultspeechoptionsMappingRate(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultspeechoptionsMappingPlaydelay(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultspeechoptionsMappingPitch(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("undefined")

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("undefined")

    @max.setter
    def max(self, text: str): self._config(text, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("undefined")

    @min.setter
    def min(self, text: str): self._config(text, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("undefined")

    @within.setter
    def within(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationDefaultspeechoptionsMapping(Options):

    @property
    def pitch(self) -> 'OptionSonificationDefaultspeechoptionsMappingPitch':
        """Speech pitch (how high/low the voice is) multiplier. """
        return self._config_sub_data("pitch", OptionSonificationDefaultspeechoptionsMappingPitch)

    @property
    def playDelay(self) -> 'OptionSonificationDefaultspeechoptionsMappingPlaydelay':
        """Milliseconds to wait before playing, comes in addition to the time determined by the <code>time</code> mapping. """
        return self._config_sub_data("playDelay", OptionSonificationDefaultspeechoptionsMappingPlaydelay)

    @property
    def rate(self) -> 'OptionSonificationDefaultspeechoptionsMappingRate':
        """Speech rate (speed) multiplier. """
        return self._config_sub_data("rate", OptionSonificationDefaultspeechoptionsMappingRate)

    @property
    def text(self):
        """The text to announce for speech tracks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def time(self) -> 'OptionSonificationDefaultspeechoptionsMappingTime':
        """Time mapping determines what time each point plays. """
        return self._config_sub_data("time", OptionSonificationDefaultspeechoptionsMappingTime)

    @property
    def volume(self) -> 'OptionSonificationDefaultspeechoptionsMappingVolume':
        """Volume of the speech announcement. """
        return self._config_sub_data("volume", OptionSonificationDefaultspeechoptionsMappingVolume)

        
class OptionSonificationDefaultspeechoptions(Options):

    @property
    def activeWhen(self) -> 'OptionSonificationDefaultspeechoptionsActivewhen':
        """Define a condition for when a track should be active and not. """
        return self._config_sub_data("activeWhen", OptionSonificationDefaultspeechoptionsActivewhen)

    @property
    def language(self):
        """The language to speak in for speech tracks, as an IETF BCP 47 language tag.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("en-US")

    @language.setter
    def language(self, text: str): self._config(text, js_type=False)

    @property
    def mapping(self) -> 'OptionSonificationDefaultspeechoptionsMapping':
        """Mapping configuration for the speech/audio parameters. """
        return self._config_sub_data("mapping", OptionSonificationDefaultspeechoptionsMapping)

    @property
    def pointGrouping(self) -> 'OptionSonificationDefaultspeechoptionsPointgrouping':
        """Options for point grouping, specifically for instrument tracks. """
        return self._config_sub_data("pointGrouping", OptionSonificationDefaultspeechoptionsPointgrouping)

    @property
    def preferredVoice(self):
        """Name of the voice synthesis to prefer for speech tracks.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @preferredVoice.setter
    def preferredVoice(self, text: str): self._config(text, js_type=False)

    @property
    def showPlayMarker(self):
        """Show play marker (tooltip and/or crosshair) for a track.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @showPlayMarker.setter
    def showPlayMarker(self, flag: bool): self._config(flag, js_type=False)

    @property
    def type(self):
        """Type of track.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("speech")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsPointgrouping(Options):

    @property
    def algorithm(self):
        """The grouping algorithm, deciding which points to keep when grouping a set of points together.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("minmax")

    @algorithm.setter
    def algorithm(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Whether or not to group points.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def groupTimespan(self):
        """The size of each group in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(15)

    @groupTimespan.setter
    def groupTimespan(self, num: float): self._config(num, js_type=False)

    @property
    def prop(self):
        """The data property for each point to compare when deciding which points to keep in the group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("y")

    @prop.setter
    def prop(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingVolume(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingTremoloSpeed(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingTremoloDepth(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingTremolo(Options):

    @property
    def depth(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingTremoloDepth':
        """Map to tremolo depth, from 0 to 1. """
        return self._config_sub_data("depth", OptionSonificationDefaultinstrumentoptionsMappingTremoloDepth)

    @property
    def speed(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingTremoloSpeed':
        """Map to tremolo speed, from 0 to 1. """
        return self._config_sub_data("speed", OptionSonificationDefaultinstrumentoptionsMappingTremoloSpeed)

        
class OptionSonificationDefaultinstrumentoptionsMappingTime(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingPlaydelay(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingPitch(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("y")

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("c6")

    @max.setter
    def max(self, text: str): self._config(text, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("c2")

    @min.setter
    def min(self, text: str): self._config(text, js_type=False)

    @property
    def scale(self):
        """Map pitches to a musical scale.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @scale.setter
    def scale(self, value: Any): self._config(value, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("yAxis")

    @within.setter
    def within(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingPan(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingNoteduration(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingLowpassResonance(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingLowpassFrequency(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingLowpass(Options):

    @property
    def frequency(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingLowpassFrequency':
        """Map to filter frequency in Hertz from 1 to 20,000Hz. """
        return self._config_sub_data("frequency", OptionSonificationDefaultinstrumentoptionsMappingLowpassFrequency)

    @property
    def resonance(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingLowpassResonance':
        """Map to filter resonance in dB. """
        return self._config_sub_data("resonance", OptionSonificationDefaultinstrumentoptionsMappingLowpassResonance)

        
class OptionSonificationDefaultinstrumentoptionsMappingFrequency(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingHighpassFrequency(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingGapbetweennotes(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMapping(Options):

    @property
    def frequency(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingFrequency':
        """Frequency in Hertz of notes. """
        return self._config_sub_data("frequency", OptionSonificationDefaultinstrumentoptionsMappingFrequency)

    @property
    def gapBetweenNotes(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingGapbetweennotes':
        """Gap in milliseconds between notes if pitch is mapped to an array of notes. """
        return self._config_sub_data("gapBetweenNotes", OptionSonificationDefaultinstrumentoptionsMappingGapbetweennotes)

    @property
    def highpass(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingHighpass':
        """Mapping options for the highpass filter. """
        return self._config_sub_data("highpass", OptionSonificationDefaultinstrumentoptionsMappingHighpass)

    @property
    def lowpass(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingLowpass':
        """Mapping options for the lowpass filter. """
        return self._config_sub_data("lowpass", OptionSonificationDefaultinstrumentoptionsMappingLowpass)

    @property
    def noteDuration(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingNoteduration':
        """Note duration determines for how long a note plays, in milliseconds. """
        return self._config_sub_data("noteDuration", OptionSonificationDefaultinstrumentoptionsMappingNoteduration)

    @property
    def pan(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingPan':
        """Pan refers to the stereo panning position of the sound. """
        return self._config_sub_data("pan", OptionSonificationDefaultinstrumentoptionsMappingPan)

    @property
    def pitch(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingPitch':
        """Musical pitch refers to how high or low notes are played. """
        return self._config_sub_data("pitch", OptionSonificationDefaultinstrumentoptionsMappingPitch)

    @property
    def playDelay(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingPlaydelay':
        """Milliseconds to wait before playing, comes in addition to the time determined by the <code>time</code> mapping. """
        return self._config_sub_data("playDelay", OptionSonificationDefaultinstrumentoptionsMappingPlaydelay)

    @property
    def time(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingTime':
        """Time mapping determines what time each point plays. """
        return self._config_sub_data("time", OptionSonificationDefaultinstrumentoptionsMappingTime)

    @property
    def tremolo(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingTremolo':
        """Mapping options for tremolo effects. """
        return self._config_sub_data("tremolo", OptionSonificationDefaultinstrumentoptionsMappingTremolo)

    @property
    def volume(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingVolume':
        """The volume of notes, from 0 to 1. """
        return self._config_sub_data("volume", OptionSonificationDefaultinstrumentoptionsMappingVolume)

        
class OptionSonificationDefaultinstrumentoptions(Options):

    @property
    def activeWhen(self) -> 'OptionSonificationDefaultinstrumentoptionsActivewhen':
        """Define a condition for when a track should be active and not. """
        return self._config_sub_data("activeWhen", OptionSonificationDefaultinstrumentoptionsActivewhen)

    @property
    def instrument(self):
        """Instrument to use for playing.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("piano")

    @instrument.setter
    def instrument(self, text: str): self._config(text, js_type=False)

    @property
    def mapping(self) -> 'OptionSonificationDefaultinstrumentoptionsMapping':
        """Mapping options for the audio parameters. """
        return self._config_sub_data("mapping", OptionSonificationDefaultinstrumentoptionsMapping)

    @property
    def midiName(self):
        """Name to use for a track when exporting to MIDI.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @midiName.setter
    def midiName(self, text: str): self._config(text, js_type=False)

    @property
    def pointGrouping(self) -> 'OptionSonificationDefaultinstrumentoptionsPointgrouping':
        """Options for point grouping, specifically for instrument tracks. """
        return self._config_sub_data("pointGrouping", OptionSonificationDefaultinstrumentoptionsPointgrouping)

    @property
    def roundToMusicalNotes(self):
        """Round pitch mapping to musical notes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @roundToMusicalNotes.setter
    def roundToMusicalNotes(self, flag: bool): self._config(flag, js_type=False)

    @property
    def showPlayMarker(self):
        """Show play marker (tooltip and/or crosshair) for a track.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(True)

    @showPlayMarker.setter
    def showPlayMarker(self, flag: bool): self._config(flag, js_type=False)

    @property
    def type(self):
        """Type of track.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("instrument")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingHighpassResonance(Options):

    @property
    def mapFunction(self):
        """How to perform the mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapFunction.setter
    def mapFunction(self, value: Any): self._config(value, js_type=False)

    @property
    def mapTo(self):
        """A point property to map the mapping parameter to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @mapTo.setter
    def mapTo(self, text: str): self._config(text, js_type=False)

    @property
    def max(self):
        """The maximum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @max.setter
    def max(self, num: float): self._config(num, js_type=False)

    @property
    def min(self):
        """The minimum value for the audio parameter.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @min.setter
    def min(self, num: float): self._config(num, js_type=False)

    @property
    def value(self):
        """A fixed value to use for the prop when mapping.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @value.setter
    def value(self, num: float): self._config(num, js_type=False)

    @property
    def within(self):
        """What data values to map the parameter within.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get(None)

    @within.setter
    def within(self, value: Any): self._config(value, js_type=False)

        
class OptionSonificationDefaultinstrumentoptionsMappingHighpass(Options):

    @property
    def frequency(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingHighpassFrequency':
        """Map to filter frequency in Hertz from 1 to 20,000Hz. """
        return self._config_sub_data("frequency", OptionSonificationDefaultinstrumentoptionsMappingHighpassFrequency)

    @property
    def resonance(self) -> 'OptionSonificationDefaultinstrumentoptionsMappingHighpassResonance':
        """Map to filter resonance in dB. """
        return self._config_sub_data("resonance", OptionSonificationDefaultinstrumentoptionsMappingHighpassResonance)
