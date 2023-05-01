

function c3Pie(data, options){
    if(data.python){
        result = {'columns': [], type: options.type};
        result['columns'].push(['x'].concat(data.labels));
        data.series.forEach(function(name, i){
          result['columns'].push([name].concat(data.datasets[i]));
        });
      } else {
        var temp = {}; var labels = {};
        data.forEach(function(rec){
          if(!(rec[options.x_column] in temp)){temp[rec[options.x_column]] = {}};
          options.y_columns.forEach(function(name){
            labels[name] = true;
            if(rec[name] !== undefined){
              if(!(name in temp[rec[options.x_column]])){
                temp[rec[options.x_column]][name] = rec[name]}
              else{temp[rec[options.x_column]][name] += rec[name]}}})});
        columns = []; var labels = Object.keys(labels); var count = 0;
        for(var series in temp){
          var values = [series]; count += 1;
          labels.forEach(function(label){
            if(temp[series][label] !== undefined){values.push(temp[series][label])} else{values.push(null)}});
          columns.push(values)};
        var result = {columns: columns, type: options.type}
      }; return result
}
