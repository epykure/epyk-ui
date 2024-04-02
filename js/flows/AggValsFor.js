
function aggValsFor(records, {columns, attrs = null, filters = null}){
    let tempResult = {};
    columns.forEach(function(c){
        tempResult[c] = {};
        records.forEach(function(v){
            if(typeof tempResult[c][v[c]] === "undefined"){tempResult[c][v[c]] = 0};
            tempResult[c][v[c]]++;
        })
    });
    let result = {};
    for (const [col, colValues] of Object.entries(tempResult)) {
        let items = Object.keys(colValues).map(function(key){return [key, colValues[key]]});
        items.sort(function(first, second){return second[1] - first [1]});
        result[col] = [];
        items.forEach(function(it){
            result[col].push(it[0])
        })
    }
    if(attrs){
        for (const [col, colValues] of Object.entries(attrs)) {
            if(typeof result[col] !== "undefined"){result[col].concat(colValues)}
            else{result[col] = colValues}
        }
    };
    return result
}