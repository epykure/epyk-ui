

function externalLink(htmlObj, data, options){
    if (options.templateMode == 'loading'){data = options.templateLoading(data); htmlObj.href = "javascript: void(0)"}
    else if (options.templateMode == 'error'){data = options.templateError(data); htmlObj.href = "javascript: void(0)"}
    else if (typeof options.template !== 'undefined' && data){data = options.template(data)}
    if(typeof data === 'undefined'){data = {text: ''}}
    var text = "";
    if((typeof data.text !== 'undefined') && (data.text)){text = data.text}
    else if (data.text) {text = data.text}
    else {text = data}
    if (options.type_number == 'money'){
        text = accounting.formatMoney(text, options.symbol, options.digits, options.thousand_sep,
        options.decimal_sep, options.format)}
    else if (options.type_number == 'number'){
        text = accounting.formatNumber(text, options.digits, options.thousand_sep, options.decimal_sep)}
    if(typeof data.icon !== 'undefined'){
        htmlObj.innerHTML = '<i class="'+ data.icon +'" style="margin-right:5px"></i>'+ text;}
    else {htmlObj.innerHTML = text}; if(typeof data.url !== 'undefined'){htmlObj.href = data.url}
}