
function hchartsBar(data, options){
    if (data){
        let labels = []; let temp = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
            if (!labels.includes(rec[options.x_axis])){labels.push(rec[options.x_axis]);}
            options.y_columns.forEach(function(series){
                temp[series][rec[options.x_axis]] = rec[series]
             })
        });
        if (Array.isArray(options.xAxis)){options.xAxis[0].categories = labels;}
        else {options.xAxis.categories = labels;}
        let datasets = [];
        options.y_columns.forEach(function(series){
          let dataset = [];
          labels.forEach(function(x){
                dataset.push(temp[series][x])});
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