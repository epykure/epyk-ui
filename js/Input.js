

function input(htmlObj, data, options){
    if((typeof options !== 'undefined')){
        if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}
        if(typeof options.formatMoney !== 'undefined'){ htmlObj.value = accounting.formatMoney(data,
            options.formatMoney.symbol, options.formatMoney.digit,
            options.formatMoney.thousand, options.formatMoney.decimal)}
        else if(typeof options.formatNumber !== 'undefined'){ htmlObj.value = accounting.formatNumber(data,
            options.formatNumber.digit, options.formatNumber.thousand)}
        else if(typeof options.toFixed !== 'undefined'){ htmlObj.value = accounting.toFixed(data, options.toFixed) }
        else {
        htmlObj.value = data; }
    }
    else {
        htmlObj.value = data;
    }
}