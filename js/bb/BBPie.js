

function bBPie(data, options){
    if(data.python){
        result = {'columns': [], type: options.type};
        result['columns'].push(['x'].concat(data.labels));
        data.series.forEach(function(name, i){
          result['columns'].push([name].concat(data.datasets[i]));
        });
      } else {
        var temp = {}; var labels = {}; var yDefs; var xDefs;
        if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
        if (typeof options.x_column === 'function') {xDefs = options.x_column(data, options)} else {xDefs = options.x_column} ;
        data.forEach(function(rec){
          if(!(rec[xDefs] in temp)){temp[rec[xDefs]] = {}};
          yDefs.forEach(function(name){
            labels[name] = true;
            if(rec[name] !== undefined){
              if(!(name in temp[rec[xDefs]])){temp[rec[xDefs]][name] = rec[name]}
              else{temp[rec[xDefs]][name] += rec[name]}}})});
        columns = []; var labels = Object.keys(labels); var count = 0;
        for(var series in temp){
          var values = [series]; count += 1;
          labels.forEach(function(label){
            if(temp[series][label] !== undefined){values.push(temp[series][label])} else{values.push(null)}});
          columns.push(values)};
        var result = {columns: columns, type: options.type};
      };
      if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(result, null)} ;
      return result
}