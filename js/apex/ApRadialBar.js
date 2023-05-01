

function apRadialBar(data, options){
    if (typeof data === 'number'){data = {values: [data]}}
    else {
      if (typeof data.values === 'number'){
        data.values = [data.values]; if (typeof data.labels !== 'undefined'){data.labels = [data.labels]}}}
    result = {series: data.values};
    if (typeof data.labels !== 'undefined'){result.labels = data.labels}
    return result
}