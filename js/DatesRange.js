

function datesRange(htmlObj, data, options){
    if (!options?.input?.element){options.input.element = document.getElementById(htmlObj.id + "_input")};
    let pickerId = htmlObj.id + 'Id'; setCss(options.input.element, options, true);
    if (!window[pickerId]){window[pickerId] = new easepick.create(options.input);}
    if (data) {
        if (options.input.plugins.includes("RangePlugin")){
            let dates = data.split(options.input.RangePlugin.delimiter);
            window[pickerId].setStartDate(dates[0]); window[pickerId].setEndDate(dates[1]);
        } else {
            window[pickerId].setDate(data);
        }
    };
    if ("label" in options){
        label(document.getElementById(htmlObj.id + "_label"), options.label.value || "" , options.label)
    }
}