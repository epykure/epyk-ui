

function datePicker(htmlObj, data, options){
    let inputId = document.getElementById(htmlObj.id + "_input"); setCss(inputId, options, true);
    if(data == null || options?.input?.dateJsOvr){data = options.input.dateJsOvr} ;
    $(inputId).datepicker(options.input).datepicker('setDate', data)
}