

function chartPie(data, options){
    if(data.python){
        data.datasets.forEach(function(dataset, i){
          result = dataset;
        });
      } else {
        var temp = {}; var labels = {}; var yDefs; var xDefs;
        if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
        if (typeof options.x_axis === 'function') {xDefs = options.x_axis(data, options)} else {xDefs = options.x_axis} ;
        data.forEach(function(rec){
          if(!(rec[xDefs] in temp)){temp[rec[xDefs]] = {}};
          yDefs.forEach(function(name){
            labels[name] = true; if(rec[name] !== undefined) {
              if (!(name in temp[rec[xDefs]])){temp[rec[xDefs]][name] = rec[name]}
              else {temp[rec[xDefs]][name] += rec[name]}} }) ;
        });
        var labels = Object.keys(labels); result = []; var i = 0 ;
        for(var series in temp){
          var values = {y: 0, x: series};
          labels.forEach(function(label){
            if(temp[series][label] !== undefined){values.y = temp[series][label]}});
          if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(values, i)}
          result.push(values); i++ ;}
      }; return result
}