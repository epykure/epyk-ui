

function chartPie(data, options){
    if(data.python){
        data.datasets.forEach(function(dataset, i){
          result = dataset;
        });
      } else {
        var temp = {}; var labels = {};
        data.forEach(function(rec){
          if(!(rec[options.x_axis] in temp)){temp[rec[options.x_axis]] = {}};
          options.y_columns.forEach(function(name){
            labels[name] = true; if(rec[name] !== undefined) {
              if (!(name in temp[rec[options.x_axis]])){temp[rec[options.x_axis]][name] = rec[name]}
              else {temp[rec[options.x_axis]][name] += rec[name]}}  }) ;
        });
        var labels = Object.keys(labels); result = [];
        for(var series in temp){
          var values = {y: 0, x: series};
          labels.forEach(function(label){
            if(temp[series][label] !== undefined){values.y = temp[series][label]}});
          result.push(values)}
      }; return result
}