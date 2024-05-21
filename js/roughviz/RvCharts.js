

function rvCharts(data, options){
    if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(data, null)}
    return data
}