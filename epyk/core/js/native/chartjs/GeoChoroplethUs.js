

function geoChoroplethUs(htmlObj, data, options, mapFile){
    fetch(mapFile).then(
          function(r){r.json().then(function(geoData){
              const nation = ChartGeo.topojson.feature(geoData, geoData.objects.nation).features[0];
              const states = ChartGeo.topojson.feature(geoData, geoData.objects.states).features;
              var chartContext = options;
              chartContext.data = {labels: [], datasets: [{label: 'Countries', outline: nation, data: []}]};
              states.forEach(function(g){
                  chartContext.data.labels.push(g.properties.name);
                  if (g.properties.name in data){
                    chartContext.data.datasets[0].data.push({value: data[g.properties.name], feature: g})}
                  else {chartContext.data.datasets[0].data.push({value: 0, feature: g})}
              });
              if(typeof window[htmlObj.id + '_obj'] !== 'undefined'){
                window[htmlObj.id + '_obj'].data = chartContext.data;
                window[htmlObj.id + '_obj'].update()
              } else {
                window[htmlObj.id + '_obj'] = new Chart(htmlObj.getContext("2d"), chartContext);
              }
              callbacks()
          })}
        )
}