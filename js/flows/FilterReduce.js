
function filterReduce(records, {columns, addUndefined=true, defaultValue=null}){
    let result = [];
    records.forEach(function(e){
        let rec = {};
        columns.forEach(function(c){
            if (c in e){rec[c] = e[c]}
            else if (addUndefined){rec[c] = defaultValue}
        });
        if (rec){result.push(rec);}
    });
    return result
}