

function datesRange(htmlObj, data, options){
    if (!options?.input?.element){options.input.element = document.getElementById(htmlObj.id + "_input")}
    let pickerId = htmlObj.id + 'Id';
    if (!window[htmlObj.id + 'Id']){
        window[htmlObj.id + 'Id'] = new easepick.create(options.input);
    }
    if (data) {
        if (options.input.plugins.includes("RangePlugin")){
            let dates = data.split(options.input.RangePlugin.delimiter) ;
            window[htmlObj.id + 'Id'].setStartDate(dates[0]) ;
            window[htmlObj.id + 'Id'].setEndDate(dates[1]) ;
        } else {
            window[htmlObj.id + 'Id'].setDate(data) ;
        }
    } ;
    if ("label" in options){
        label(document.getElementById(htmlObj.id + "_label"), options.label.value || "" , options.label)
    }
}