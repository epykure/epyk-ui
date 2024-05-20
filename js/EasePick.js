

function easePick(htmlObj, data, options){
    if (!options?.input?.element){options.input.element = document.getElementById(htmlObj.id + "_input")}
    const picker = new easepick.create(options.input);
    if (data) {
        if (options.input.plugins.includes("RangePlugin")){
            let dates = data.split(options.input.RangePlugin.delimiter) ;
            picker.setStartDate(dates[0]) ;
            picker.setEndDate(dates[1]) ;
        } else {
            picker.setDate(data) ;
        }
    } ;
    if ("label" in options){
        label(document.getElementById(htmlObj.id + "_label"), options.label.value || "" , options.label)
    }
}