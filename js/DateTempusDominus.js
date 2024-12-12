
function tempusDominus4(htmlObj, data, options){
    delete options.builder; $('#' + htmlObj.id).datetimepicker(options) ;
    if (data) {
        const date = new Date(data);
        window[htmlObj.id + "Id"].datetimepicker('date', date) ;
    }
}


function tempusDominus5(htmlObj, data, options){
    window[htmlObj.id + "Id"] = $(htmlObj);
    delete options.builder; window[htmlObj.id + "Id"].datetimepicker(options) ;
    if (data) {
        const date = new Date(data);
        window[htmlObj.id + "Id"].datetimepicker('date', date) ;
    }
}


function tempusDominus6(htmlObj, data, options){
    delete options.builder; window[htmlObj.id + "Id"] = new tempusDominus.TempusDominus(htmlObj, options) ;
    if (data) {
        const date = new Date(data);
        window[htmlObj.id + "Id"].dates.setValue(tempusDominus.DateTime.convert(date))}
}
