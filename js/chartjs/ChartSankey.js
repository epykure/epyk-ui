
function chartSankey(data, options){
    if(Array.isArray(data)){
        datasets = [{data: data}];
        if (typeof options.props !== 'undefined'){
           for(var attr in options.props[0]){datasets[0][attr] = options.props[0][attr]}}
        else if(typeof options.commons !== 'undefined'){
            for(var attr in options.commons){datasets[0][attr] = options.commons[attr]};}
        if (typeof options.datasets !== 'undefined'){
                  dataSet = Object.assign(datasets[0], options.datasets[0])}
    }
    else {
        datasets = [];
        for (var series in data) {datasets.push({data: data[series], label: series})}
        datasets.forEach(function(dataset, i){
            if ((typeof options.props !== 'undefined') && (typeof options.props[series] !== 'undefined')){
               for(var attr in options.props[series]){dataset[attr] = options.props[series][attr]}}
            else if(typeof options.commons !== 'undefined'){
                for(var attr in options.commons){dataset[attr] = options.commons[attr]};}
            if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
                      dataSet = Object.assign(dataset, options.datasets[series])}
        })
    }
    return {datasets: datasets}
}