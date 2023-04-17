

function chartLine(data, options){
    if(data.python){
        result = {datasets: [], labels: data.labels};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
          if(typeof dataset.hoverBackgroundColor === "undefined"){
            dataset.hoverBackgroundColor = options.background_colors[i]};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
          result.datasets.push(dataset) })
      } else{
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
          options.y_columns.forEach(function(name){
          if(rec[name] !== undefined){
            if (!(rec[options.x_axis] in uniqLabels)){
              labels.push(rec[options.x_axis]); uniqLabels[rec[options.x_axis]] = true};
            temp[name][rec[options.x_axis]] = rec[name]}})
        });
        result = {datasets: [], labels: labels};
        options.y_columns.forEach(function(series, i){
            dataSet = {label: series, data: [], backgroundColor: options.background_colors[i], type: options.type,
                 hoverBackgroundColor: options.colors[i], borderColor: options.colors[i],
                 borderColor: options.colors[i], borderWidth: 1, hoverBorderColor: options.colors[i]};
            if ((typeof options.props !== 'undefined') && (typeof options.props[series] !== 'undefined')){
              for(var attr in options.props[series]){dataSet[attr] = options.props[series][attr]}}
            else if(typeof options.commons !== 'undefined'){
              for(var attr in options.commons){dataSet[attr] = options.commons[attr]}}
              labels.forEach(function(x){
                if (temp[series][x] == undefined){dataSet.data.push(null)} else {dataSet.data.push(temp[series][x])}});
            if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options.datasets[series])}
          result.datasets.push(dataSet)});
          if (typeof options.labels !== "undefined"){ result.labels = options.labels}
      }; return result
}