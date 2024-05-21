
function ekPlotECharts(data, options){
    let chartContext = {series: []};
    Object.assign(chartContext, options);
    delete chartContext._ek;

    if (data && data.length > 0){chartContext.series = data};
    if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(chartContext, null)}
    return chartContext
}