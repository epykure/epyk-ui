

function filterPivot(records, {column, value, key, convertFunc=null}){
    let s = {}; let result = [];
    records.forEach(function(t){
        let val = t[value];
        if (convertFunc){val = convertFunc(val)}
        if (t[key] in s){s[t[key]][t[column]] = val}
        else {s[t[key]] = {[t[column]]: val}}
    });
    for (const [key, values] of Object.entries(s)){result.push(Object.assign(values, {[key]: key}))};
    return result
}
