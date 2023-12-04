

function chartBar(data, options){
    if(data.python){
        result = [];
        data.datasets.forEach(function(rec, i){
          result.push( {key: data.series[i], values: rec, labels: data.labels} )})
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}}) ;
        data.forEach(function(rec){
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_axis] in uniqLabels)){
                labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true};
              temp[name][rec[options.x_axis]] = rec[name]}})
        }); var result = [];
        options.y_columns.forEach(function(series){
          dataSet = {key: series, values: [], labels: labels};
          labels.forEach(function(x, i){
            var value = temp[series][x];
            if (isNaN(value)) { value = null};
            if (value !== undefined) {dataSet.values.push({y: value, x: i, label: x})}
          }); result.push(dataSet)})
      };
    return result
}