
function filterRename(records, {names, keepOrigin = false}){
    let result = [];
    records.forEach(function(e){
        let rec = {};
        for (const [c, v] of Object.entries(e)) {
            if (c in names){rec[names[c]] = v; if(keepOrigin){rec[c] = v}}
            else {rec[c] = v}
        }
        if (rec){result.push(rec)}
    });
    return result
}
