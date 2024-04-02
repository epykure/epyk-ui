
function aggSumBy(records, {columns, srcKeys, dstKey = null, attrs = null, convertFunc = null}){
    let result = []; var tmpResults = {}; if(srcKeys == ''){return records};
    let rdk = dstKey === null ? srcKeys :  dstKey;
    if (!Array.isArray(srcKeys)) {srcKeys = [srcKeys]}
    records.forEach(function(r){
        if(r){
            let sk = []; srcKeys.forEach(function(s){sk.push(r[s])}); let skKey = sk.join('#');
            if (!(skKey in tmpResults)){tmpResults[skKey] = {}; srcKeys.forEach(function(s){tmpResults[skKey][s] = r[s]});
               columns.forEach(function(c){tmpResults[skKey][c] = 0})};
            columns.forEach(function(c){
                if (convertFunc){tmpResults[skKey][c] += convertFunc(r[c])}
                else {tmpResults[skKey][c] += r[c]}})
        }
      });
    for(let v in tmpResults){result.push(tmpResults[v])};
    return result
}