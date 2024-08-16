
function markdownReader(htmlObj, data, options){
    if (data !== ''){
        setCss(htmlObj, options, true); htmlObj.innerHTML = getHtmlData(data, options);
        document.querySelectorAll('pre code').forEach((block) => {hljs.highlightBlock(block)});
    }
}