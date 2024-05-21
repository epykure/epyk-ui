

function fCharts(data, options){
    if(data.python){
      result = {'columns': [], type: options.type};
      result['columns'].push(['x'].concat(data.labels));
      data.series.forEach(function(name, i){
        result['columns'].push([name].concat(data.datasets[i]));
      });
    } else {
      var temp = {}; var labels = []; var uniqLabels = {}; var yDefs; var xDefs;
      if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
      if (typeof options.x_column === 'function') {xDefs = options.x_column(data, options)} else {xDefs = options.x_column} ;
      yDefs.forEach(function(series){temp[series] = {}});
      data.forEach(function(rec){
        yDefs.forEach(function(name){
          if(rec[name] !== undefined){
            if (!(rec[xDefs] in uniqLabels)){
              labels.push(rec[xDefs]); uniqLabels[rec[xDefs]] = true};
            temp[name][rec[xDefs]] = rec[name]}})});
      result = {labels: labels, datasets: []};
      yDefs.forEach(function(series, i){
        dataSet = {name: series, values: []};
        labels.forEach(function(x){
          if(temp[series][x] == undefined){dataSet.values.push(null)}
          else {dataSet.values.push(temp[series][x])}});
        if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(datasets, i)}
        result.datasets.push(dataSet)});
    }; return result
}