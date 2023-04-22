

function c3Scatter(data, options){
    if(data.python){
        result = {'columns': [], type: options.type};
        result['columns'].push(['x'].concat(data.labels));
        data.series.forEach(function(name, i){
          result['columns'].push([name].concat(data.datasets[i]))});
      } else {
        var tempVal = {}; var tempX = {}; var labels = [];
        options.y_columns.forEach(function(series){tempVal[series] = [series]; tempX[series +"_x"] = [series +"_x"]});
        data.forEach(function(rec){
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              tempVal[name].push(rec[name]); tempX[name +"_x"].push(rec[options.x_column])}})});
        result = {'columns': [], 'xs': {}, type: options.type, axes: options.axis};
        options.y_columns.forEach(function(series){
          result.columns.push(tempX[series +"_x"]); result.columns.push(tempVal[series]);
          result.xs[series] = series +"_x"})
      }; return result
}