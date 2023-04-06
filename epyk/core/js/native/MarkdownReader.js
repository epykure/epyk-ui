

function markdownReader(htmlObj, data, options){
    if (data !== ''){
        var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data); htmlObj.innerHTML = data;
        document.querySelectorAll('pre code').forEach((block) => {hljs.highlightBlock(block)});
      }

}