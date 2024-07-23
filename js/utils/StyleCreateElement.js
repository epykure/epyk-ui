function createStyleElement(content){
    let cssStyle = document.createElement('style');
    cssStyle.type = 'text/css'; cssStyle.innerHTML = content;
    document.getElementsByTagName('head')[0].appendChild(cssStyle);
    return cssStyle
}