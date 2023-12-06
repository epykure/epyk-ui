
function hchartsPie(data, options){
    if (data){
        let labels = []; let temp = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
            if (!labels.includes(rec[options.x_axis])){labels.push(rec[options.x_axis]);}
            options.y_columns.forEach(function(series){
                temp[series][rec[options.x_axis]] = rec[series]
             })
        });
        let datasets = [];
        options.y_columns.forEach(function(series){
          let dataset = [];
          labels.forEach(function(x){
            let point = {name: x, y: temp[series][x]};
            if ((typeof options.props !== 'undefined') && (typeof options.props[x] !== 'undefined')){
              for(var attr in options.props[x]){point[attr] = options.props[x][attr]}}

             dataset.push(point)});
          let seriesData = {name: series, data: dataset};
          if(typeof options.commons !== 'undefined'){
              for(var attr in options.commons){seriesData[attr] = options.commons[attr]}}
          if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              seriesData = Object.assign(seriesData, options.datasets[series])}
          datasets.push(seriesData);
        })
        options.series = datasets;
    };
    return options
}