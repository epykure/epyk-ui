

function apCharts(data, options){
    if(data.python){
        result = {series: [], labels: data.labels};
        data.datasets.forEach(function(dataset, i){
          if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
          if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
          if(typeof dataset.hoverBackgroundColor === "undefined"){
            dataset.hoverBackgroundColor = options.background_colors[i]};
          if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
          dataset.name = data.series[i];
          result.series.push(dataset) })
      } else{
        var temp = {}; var labels = []; var uniqLabels = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
          options.y_columns.forEach(function(name){
          if(rec[name] !== undefined){
            if (!(rec[options.x_axis] in uniqLabels)){labels.push(rec[options.x_axis]);
            uniqLabels[rec[options.x_axis]] = true};
            temp[name][rec[options.x_axis]] = rec[name]}})
        });
        result = {series: [], labels: labels, xaxis: {}};
        options.y_columns.forEach(function(series, i){
            dataSet = {label: series, data: []};
            if ((typeof options.attrs !== 'undefined') && (typeof options.attrs[series] !== 'undefined')){
              for(var attr in options.attrs[series]){dataSet[attr] = options.attrs[series][attr]}}
            else if(typeof options.commons !== 'undefined'){
              for(var attr in options.commons){dataSet[attr] = options.commons[attr]}}
              labels.forEach(function(x){
                if (typeof temp[series][x] === "undefined"){dataSet.data.push(null)}
                else {dataSet.data.push({x: x, y: temp[series][x]})}});
          result.series.push(dataSet)})
      };
      return result;
}
