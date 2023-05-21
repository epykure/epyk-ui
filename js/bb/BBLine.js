

function bBLine(data, options){
    if(data.python){
        result = {'columns': [], type: options.type};
        result['columns'].push(['x'].concat(data.labels));
        data.series.forEach(function(name, i){
          result['columns'].push([name].concat(data.datasets[i]));
        });
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec, i){
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              var label = rec[options.x_column];
              if (!(label in uniqLabels)){var label = ""+ rec[options.x_column];
                labels.push(label); uniqLabels[label] = true};
                temp[name][label] = rec[name]}})});
        columns = [];
        options.y_columns.forEach(function(series){
          dataSet = [series];
          labels.forEach(function(x){
            if(temp[series][x] == undefined){dataSet.push(null)}
            else {dataSet.push(temp[series][x])}}); columns.push(dataSet)});
        var result = {columns: columns, type: options.type, categories: labels}
        if (typeof(options.axis) !== "undefined"){result.axis = options.axis}
      }; return result
}