

function c3Stanford(data, options){
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
        columns = []; columns.push(['x'].concat(labels));
        yDefs.forEach(function(series){
          dataSet = [series];
          labels.forEach(function(x){
            if(temp[series][x] == undefined){dataSet.push(null)}
            else {dataSet.push(temp[series][x])}}); columns.push(dataSet)});
        var result = {columns: columns, type: options.type, point: options.point}
      }; return result
}