
function hchartsBubble(data, options){
    if (data){
        let labels = []; let temp = {}; let dataset = [];

        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
            if (!labels.includes(rec[options.x_axis])){labels.push(rec[options.x_axis]);}
            options.y_columns.forEach(function(series){
                if (options.rDim){
                     temp[series][rec[options.x_axis]] = {y: rec[series], x: rec[options.x_axis], z: rec[options.rDim[0]]}
                }
                else {
                    temp[series][rec[options.x_axis]] = {y: rec[series], x: rec[options.x_axis], z: 2}
                }
             })
        });
        let datasets = [];
        options.y_columns.forEach(function(series){
          let dataset = [];
          labels.forEach(function(x){
             dataset.push(temp[series][x])});
          datasets.push({name: series, data: dataset});
        })
        options.series = datasets;
    };
    return options
}