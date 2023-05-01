

function code(htmlObj, data, options){
    var editor_alias = "editor_"+ htmlObj.id;
       if (typeof window[editor_alias] === 'undefined'){
          window[editor_alias] = CodeMirror.fromTextArea(htmlObj, options)}
       window[editor_alias].setValue(data);
       Object.keys(options).forEach(
          function(key){ window[editor_alias].setOption(key, options[key])})
}