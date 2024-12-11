
function ekRadarECharts(data, options){
    let chartContext = getChartContext(options); chartContext.series = [] ;

    var yDefs ; var xDefs ;
    if (typeof options._ek.chart.y_columns === 'function') {
        yDefs = options._ek.chart.y_columns(data, options)} else {yDefs = options._ek.chart.y_columns} ;
    if (typeof options._ek.chart.x_axis === 'function') {
        xDefs = options._ek.chart.x_axis(data, options)} else {xDefs = options._ek.chart.x_axis} ;

    let indicatorAttrs = {};
    if (options._ek) {
        if(options._ek.chart.indicator){
            indicatorAttrs = options._ek.chart.indicator ;
        };
        if (yDefs){
            yDefs.forEach(function(value){
                let dataset = {data: [], type: options._ek.chart.type, name: value};
            })
        }
    };
    if (!chartContext.radar){chartContext.radar = {}}
    chartContext.radar.indicator = [] ;
    if (data && data.length > 0){
        chartContext.series = []; options.series = [];
        var temp = {}; var labels = []; var uniqLabels = {};
        yDefs.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
          yDefs.forEach(function(name){
          if(rec[name] !== undefined){
            let seriesLabel = rec[xDefs];
            if (!(rec[xDefs] in uniqLabels)){
              labels.push(seriesLabel);
              if (seriesLabel in indicatorAttrs){
                chartContext.radar.indicator.push(Object.assign({}, {name: seriesLabel}, indicatorAttrs[seriesLabel])) ;
              } else {chartContext.radar.indicator.push({name: seriesLabel});}
              uniqLabels[seriesLabel] = true};
            temp[name][seriesLabel] = rec[name]}})
        });

        let dataSet = {data: [], type: options._ek.chart.type, color: options._ek.colors};
        yDefs.forEach(function(series, i){
            let values = [];
            labels.forEach(function(x){
                if (temp[series][x] == undefined){values.push(null)} else {values.push(temp[series][x])}
            });
            if (typeof options._ek.series !== 'undefined'){
              values = Object.assign(values, options._ek.series)}
            if ((typeof options._ek.names !== 'undefined') && (typeof options._ek.names[series] !== 'undefined')){
              values = Object.assign(values, options._ek.names[series])};
            let dataSeries = {name: series, value: values} ;
            if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(dataSeries, i)} ;
            dataSet.data.push(dataSeries);
        });
        chartContext.series.push(dataSet);
    };
    return chartContext
}