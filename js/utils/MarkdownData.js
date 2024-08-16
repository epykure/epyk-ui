
function getHtmlData(data, options){
    let content;
    if (options.showdown){
        let converter = new showdown.Converter(options.showdown); content = converter.makeHtml(data.trim());
    } else {content = data;};
    return content;
}