

function chartScatter(data, options){
    if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
          if(typeof dataset.hoverBackgroundColor === "undefined"){dataset.hoverBackgroundColor = options.colors[i]};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)} ;
          if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(dataset, i)}
          result.datasets.push(dataset)})
      } else {
        var temp = {}; var labels = [];
        var uniqLabels = {}; var yDefs; var xDefs;
        if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
        if (typeof options.x_axis === 'function') {xDefs = options.x_axis(data, options)} else {xDefs = options.x_axis} ;
        yDefs.forEach(function(series){temp[series] = []});
        data.forEach(function(rec){
          yDefs.forEach(function(name){
            if(rec[xDefs] !== undefined){
              labels.push(rec[xDefs]); var r = 2;
              if((options.rDim != undefined) && (rec[options.rDim] != undefined)){r = rec[options.rDim]};
              temp[name].push({y: rec[name], x: rec[xDefs], r: r})}})});
        result = {datasets: [], labels: labels};
        yDefs.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.colors[i], type: options.type};
          if ((typeof options.props !== 'undefined') && (typeof options.props[i] !== 'undefined')){
           for(var attr in options.props[i]){dataSet[attr] = options.props[i][attr]}}
          else if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x, i){dataSet.data = temp[series]});
          if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
                  dataSet = Object.assign(dataSet, options.datasets[series])} ;
          if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(dataSet, i)}
        result.datasets.push(dataSet)}); if (typeof options.labels !== "undefined"){ result.labels = options.labels}
    }; return result
}