

 function aggCountBy(records, {column, attrs = null}){
    let tempDict = {};
    records.forEach(function(v){
        if (v){
        if(typeof v[column] !== 'undefined'){
            if(typeof tempDict[v[column]] === 'undefined'){tempDict[v[column]] = 0};
            tempDict[v[column]] += 1}}
    });
    let result = []; for(let key in tempDict){result.push({[column]: key, count: tempDict[key]})};
    return result
 }