
function ekScatterECharts(data, options){
    let chartContext = getChartContext(options); chartContext.series = [] ;

    var yDefs ; var xDefs ;
    if (typeof options._ek.chart.y_columns === 'function') {
        yDefs = options._ek.chart.y_columns(data, options)} else {yDefs = options._ek.chart.y_columns} ;
    if (typeof options._ek.chart.x_axis === 'function') {
        xDefs = options._ek.chart.x_axis(data, options)} else {xDefs = options._ek.chart.x_axis} ;

    if (options._ek) {
        if (yDefs){
            yDefs.forEach(function(value){
                let dataset = {data: [], type: options._ek.chart.type, name: value};
            })
        }
    };

    if (data && data.length > 0){
        chartContext.series = []; options.series = [];
        var temp = {}; var labels = []; var uniqLabels = {};
        yDefs.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
          yDefs.forEach(function(name){
          if(rec[name] !== undefined){
            if (!(rec[xDefs] in uniqLabels)){
              labels.push(rec[xDefs]); uniqLabels[rec[xDefs]] = true};
            temp[name][rec[xDefs]] = rec}})
        });

        yDefs.forEach(function(series, i){
            let dataSet = {data: [], type: options._ek.chart.type, name: series, color: options._ek.colors[i]};
            labels.forEach(function(x){
                if (temp[series][x] == undefined){dataSet.data.push(null)} else {
                    let vector = [x, temp[series][x][series]];
                    if (typeof options._ek.params !== 'undefined'){
                        options._ek.params.forEach(function(p){vector.push(temp[series][x][p])})};
                    dataSet.data.push(vector)}});
            if (typeof options._ek.series !== 'undefined'){
              dataSet = Object.assign(dataSet, options._ek.series)}
            if ((typeof options._ek.names !== 'undefined') && (typeof options._ek.names[series] !== 'undefined')){
              dataSet = Object.assign(dataSet, options._ek.names[series])} ;
            if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(dataSet, i)} ;
            chartContext.series.push(dataSet)
        })
    };

    return chartContext
}