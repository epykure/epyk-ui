

function geoChoroplethCountry(htmlObj, data, options, callbacks){
    fetch(options.options._mapFile).then(
      function(r){r.json().then(function(geoData){
          var chartContext = options;
          chartContext.data = {labels: [], datasets: [{label: 'Countries', data: [] }]};
          geoData.features.forEach(function(g){
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