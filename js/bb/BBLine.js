

function bBLine(data, options){
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
        data.forEach(function(rec, i){
          yDefs.forEach(function(name){
            if(rec[name] !== undefined){
              var label = rec[xDefs];
              if (!(label in uniqLabels)){var label = ""+ rec[xDefs];
                labels.push(label); uniqLabels[label] = true};
                temp[name][label] = rec[name]}})});
        columns = [];
        yDefs.forEach(function(series){
          dataSet = [series];
          labels.forEach(function(x){
            if(temp[series][x] == undefined){dataSet.push(null)} else {dataSet.push(temp[series][x])}});
          columns.push(dataSet)
        });
        var result = {columns: columns, type: options.type, categories: labels};
        if (typeof(options.axis) !== "undefined"){result.axis = options.axis}
      };
      if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(result, null)} ;
      return result
}