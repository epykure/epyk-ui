

function aggProcessCols(records, {key, literal, attrs = null, convertFunc = null}){
    let result = [];
    records.forEach(function(rec){
        let newRec = {}; Object.assign(newRec, rec);
        newRec[key] = literal(rec);
        result.push(newRec)
    });
    if(attrs){for(let attr in attrs){result[attr] = attrs[attr]}};
    return result
}