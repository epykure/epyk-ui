

function c3Scatter(data, options){
    if(data.python){
        result = {'columns': [], type: options.type};
        result['columns'].push(['x'].concat(data.labels));
        data.series.forEach(function(name, i){
          result['columns'].push([name].concat(data.datasets[i]))});
      } else {
        var tempVal = {}; var tempX = {}; var labels = []; var yDefs; var xDefs;
        if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
        if (typeof options.x_column === 'function') {xDefs = options.x_column(data, options)} else {xDefs = options.x_column} ;
        yDefs.forEach(function(series){tempVal[series] = [series]; tempX[series +"_x"] = [series +"_x"]});
        data.forEach(function(rec){
          yDefs.forEach(function(name){
            if(rec[name] !== undefined){
              tempVal[name].push(rec[name]); tempX[name +"_x"].push(rec[xDefs])}})});
        result = {'columns': [], 'xs': {}, type: options.type, axes: options.axis};
        yDefs.forEach(function(series){
          result.columns.push(tempX[series +"_x"]); result.columns.push(tempVal[series]);
          result.xs[series] = series +"_x"})
      }; return result
}