

function numeric(htmlObj, data, options){
    if (options.templateMode == 'loading'){data = options.templateLoading(data)}
    else if (options.templateMode == 'error'){data = options.templateError(data)}
    else if (typeof options.template !== 'undefined' && data){data = options.template(data)}
    if (options.type_number == 'money'){
        if ((options.templateMode == 'loading') || (options.templateMode == 'error')){
            htmlObj.querySelector('font').innerHTML = data
        } else {
            htmlObj.querySelector('font').innerHTML = accounting.formatMoney(
            data, options.symbol, options.digits, options.thousand_sep, options.decimal_sep, options.format)}}
    else {
        if ((options.templateMode == 'loading') || (options.templateMode == 'error')){
            htmlObj.querySelector('font').innerHTML = data
        } else {
            htmlObj.querySelector('font').innerHTML = accounting.formatNumber(
            data, options.digits, options.thousand_sep, options.decimal_sep)}
        }
}