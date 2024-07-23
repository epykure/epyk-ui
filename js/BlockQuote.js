

function blockQuote(htmlObj, data, options){
    var div = htmlObj.querySelector('div'); div.innerHTML = '';
    data.text.split("\\n").forEach(function(rec) {
        if(options.showdown){var converter = new showdown.Converter(options.showdown); rec = converter.makeHtml(rec)}
        var p = document.createElement("p"); p.style.margin = 0; p.style.padding = 0; p.innerHTML = rec; div.appendChild(p)});
    if(data.author != null){
        htmlObj.querySelector('div:last-child').innerHTML = '<small>by '+ data.author +'<cite></cite></small>'};
    setCss(htmlObj, options);
}