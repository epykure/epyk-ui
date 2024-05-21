

function chartHyr(data, options){
    var results = {datasets: [{data: data}]} ;
    if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(dataSet, null)}
    return results
}