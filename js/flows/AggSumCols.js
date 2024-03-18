
function aggSumCols(records, {columns, key, attrs = null, convertFunc = null}){
    let result = [];
    records.forEach(function(v){
        let newRec = {}; Object.assign(newRec, v); let sumRec = 0;
        columns.forEach(function(c){
            if(typeof v[c] !== 'undefined'){
                if(convertFunc){sumRec += convertFunc(v[c])}
                else {sumRec += v[c]}
            }});
        newRec[key] = sumRec;
        result.push(newRec)
        });
    if(attrs){for(let attr in attrs){result[attr] = attrs[attr]}};
    return result
}