

function fCharts(data, options){
    if(data.python){
      result = {'columns': [], type: options.type};
      result['columns'].push(['x'].concat(data.labels));
      data.series.forEach(function(name, i){
        result['columns'].push([name].concat(data.datasets[i]));
      });
    } else {
      var temp = {}; var labels = []; var uniqLabels = {};
      options.y_columns.forEach(function(series){temp[series] = {}});
      data.forEach(function(rec){
        options.y_columns.forEach(function(name){
          if(rec[name] !== undefined){
            if (!(rec[options.x_column] in uniqLabels)){
              labels.push(rec[options.x_column]); uniqLabels[rec[options.x_column]] = true};
            temp[name][rec[options.x_column]] = rec[name]}})});
      result = {labels: labels, datasets: []};
      options.y_columns.forEach(function(series, i){
        dataSet = {name: series, values: []};
        labels.forEach(function(x){
          if(temp[series][x] == undefined){dataSet.values.push(null)}
          else {dataSet.values.push(temp[series][x])}}); result.datasets.push(dataSet)});
    }; return result
}