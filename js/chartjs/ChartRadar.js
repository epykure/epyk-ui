

function chartRadar(data, options){
    if(data.python){
        result = {datasets: [], labels: data.series};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
          if(typeof dataset.borderWidth === "undefined"){dataset.borderWidth  = 1};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
          result.datasets.push(dataset) })
      } else {
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
          options.y_columns.forEach(function(name){
            if(rec[name] !== undefined){
              if (!(rec[options.x_axis] in uniqLabels)){
                labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true};
              temp[name][rec[options.x_axis]] = rec[name]}})});
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
          dataSet = {label: series, data: [], backgroundColor: options.background_colors[i], fill: true, type: options.type,
                     borderColor: options.colors[i]};
          if ((typeof options.props !== 'undefined') && (typeof options.props[i] !== 'undefined')){
           for(var attr in options.props[i]){dataSet[attr] = options.props[i][attr]}}
          else if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){dataSet[attr] = options.commons[attr]};}
          labels.forEach(function(x){
            if (temp[series][x] == undefined) {dataSet.data.push(null)} else {dataSet.data.push(temp[series][x])}
          });
          if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options.datasets[series])}
          result.datasets.push(dataSet)}); if (typeof options.labels !== "undefined"){ result.labels = options.labels}
      }; return result
}