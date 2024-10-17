

function chartLine(data, options){
    if(data.python){
        result = [];
        data.datasets.forEach(function(rec, i){
          let dataSet = {key: data.series[i], values: rec, labels: data.labels} ;
          result.push( dataSet )})
      } else {
        var temp = {}; var labels = []; var uniqLabels = {}; var yDefs; var xDefs;
        if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
        if (typeof options.x_axis === 'function') {xDefs = options.x_axis(data, options)} else {xDefs = options.x_axis} ;
        yDefs.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
          yDefs.forEach(function(name){
            if(typeof rec[name] !== undefined){
              if (!(rec[xDefs] in uniqLabels)){
                labels.push(rec[xDefs]); uniqLabels[rec[xDefs]] = true};
              temp[name][rec[xDefs]] = rec[name]}})
        }); result = [];
        yDefs.forEach(function(series, i){
          dataSet = {key: series, values: [], labels: labels};
          labels.forEach(function(x, i){
            var value = temp[series][x];
            if (isNaN(value)) {value = null};
            if (value !== undefined) {dataSet.values.push({y: value, x: i, label: x})}
          });
          if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(dataSet, i)}
          result.push(dataSet)})
      }; return result
}