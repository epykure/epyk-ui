from epyk.core.html.graph import GraphD3
from epyk.core.html.options import OptChartD3


class ChartGeoD3(GraphD3.Script):
    name = 'D3 DataMaps'
    requirements = ('d3', 'topojson')
    _option_cls = OptChartD3.ChartGeo

    @property
    def options(self) -> OptChartD3.ChartGeo:
        """Property to the component options.
        Options can either impact the Python side or the Javascript builder.
        Python can pass some options to the JavaScript layer.

        'Datamaps <https://github.com/markmarkoh/datamaps>`_
        """
        return super().options

    def loader(self, frg: str):
        """Loader for the script.

        :param str frg: The javascript fragments.
        """
        self.builder_name = "D3GeoBuilder%s" % self.page.py.hash(frg)
        self._js__builder__ = '''
var paletteScale = d3.scale.linear()
   .domain([minValue,maxValue])
   .range(["#EFEFFF","#02386F"]);

if (!htmlObj.select("svg").empty()){htmlObj.select("svg").remove()}; 
var bubble_map = new Datamap()  %s
''' % frg
