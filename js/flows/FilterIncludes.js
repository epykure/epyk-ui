
function filterIncludes(records, {key, values, caseSensitive=true, emptyAll=true}){
    if (values.length == 0){if(emptyAll){return records} else {return []}};
    let vUp = values;
    if (!caseSensitive){
        vUp = [];
        values.forEach(function(t){vUp.push(t.toUpperCase())});
    };
    let n = [];
    records.forEach(function(e){
        if (caseSensitive){ if(vUp.includes(e[key])){n.push(e)}}
        else {if(vUp.includes(e[key].toUpperCase())){n.push(e)}}
    });
    return n
}