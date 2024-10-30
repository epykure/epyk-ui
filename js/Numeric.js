

function numeric(htmlObj, data, options){
    data = getDataFromTemplate(data, options); setCss(htmlObj, options, true);
    let fontDom = htmlObj.querySelector('font');
    if(!fontDom){
        fontDom = document.createElement("font"); fontDom.classList.add("html-num-font");
        htmlObj.appendChild(fontDom)
    };
    if (options.type_number == 'money'){
        if ((options.templateMode == 'loading') || (options.templateMode == 'error')){
            fontDom.innerHTML = data
        } else {
            fontDom.innerHTML = accounting.formatMoney(
            data, options.symbol, options.digits, options.thousand_sep, options.decimal_sep, options.format)}}
    else {
        if ((options.templateMode == 'loading') || (options.templateMode == 'error')){
            fontDom.innerHTML = data
        } else {
            fontDom.innerHTML = accounting.formatNumber(
            data, options.digits, options.thousand_sep, options.decimal_sep)}
        }
}