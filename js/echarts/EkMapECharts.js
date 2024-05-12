

function ekMapECharts(data, options){
    if (typeof options.y_columns !== 'undefined') {
        options._ek.chart.y_columns = options.y_columns;
        delete options.y_columns;
    };
    if (typeof options.x_axis !== 'undefined') {
        options._ek.chart.x_axis = options.x_axis;
        delete options.x_axis;
    };
    if (typeof options.names !== 'undefined') {
        options._ek.names = options.names;
        delete options.names;
    };

    let chartContext = {series: []};
    Object.assign(chartContext, options);
    delete chartContext._ek;

    if (options._ek) {
        if (options._ek.chart.y_columns){
            options._ek.chart.y_columns.forEach(function(value){
                let dataset = {data: [], type: options._ek.chart.type, name: value};
            })
        }
    };

    if (data && data.length > 0){
        chartContext.series = []; options.series = [];
        var temp = {}; var labels = []; var uniqLabels = {};
        options._ek.chart.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
          options._ek.chart.y_columns.forEach(function(name){
          if(rec[name] !== undefined){
            if (!(rec[options._ek.chart.x_axis] in uniqLabels)){
              labels.push(rec[options._ek.chart.x_axis]); uniqLabels[rec[options._ek.chart.x_axis]] = true};
            temp[name][rec[options._ek.chart.x_axis]] = rec}})
        });

        options._ek.chart.y_columns.forEach(function(series, i){
            let seriesType = options._ek.chart.type ;
            if ((typeof options._ek.names !== 'undefined') && (typeof options._ek.names[series] !== 'undefined') && (typeof options._ek.names[series].type !== 'undefined')){
                seriesType = options._ek.names[series].type
            } else if ((typeof options._ek.series !== 'undefined') && typeof options._ek.series.type !== 'undefined') {
                seriesType = options._ek.series.type
            };
            let dataSet = {data: [], type: seriesType, name: series, color: options._ek.colors[i]};
            labels.forEach(function(x){
                if (temp[series][x] == undefined){dataSet.data.push(null)} else {
                    if (seriesType != "map"){
                        dataSet.dimensions = ['lng', 'lat'];
                        let vector = [x, temp[series][x][series]];
                        if (typeof options._ek.params !== 'undefined'){
                            options._ek.params.forEach(function(p){vector.push(temp[series][x][p])})};
                        dataSet.data.push(vector)
                    } else {
                        let vector = {"name": x, "value": temp[series][x][series]};
                        Object.assign(vector, options);
                        dataSet.data.push(vector)
                    }
                }
            });
            if (typeof options._ek.series !== 'undefined'){
              dataSet = Object.assign(dataSet, options._ek.series)}
            if ((typeof options._ek.names !== 'undefined') && (typeof options._ek.names[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options._ek.names[series])}
            chartContext.series.push(dataSet)
        })
    };
    return chartContext
}
