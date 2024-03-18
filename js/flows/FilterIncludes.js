
function filterIncludes(records, {key, values, caseSensitive=true, emptyAll=true}){
    if (v.length == 0){if(emptyAll){return records} else {return []}};
    let vUp = values;
    if (!caseSensitive){
        vUp = []
        values.forEach(function(t){vUp.push(t.toUpperCase())});
    };
    let n = [];
    records.forEach(function(e){
        if (caseSensitive){ if(vUp.includes(e[k])){n.push(e)}}
        else {if(vUp.includes(e[k].toUpperCase())){n.push(e)}}
    });
    return n
}