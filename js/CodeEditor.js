function codeEditor(htmlObj, data, options){
    setCss(htmlObj, options, true);
    if (data != null){
       if(options.stringify){htmlObj.setValue(JSON.stringify(data, null, 2))} else {htmlObj.setValue(data)}
       Object.keys(options).forEach(function(key){htmlObj.setOption(key, options[key])})
    }
}