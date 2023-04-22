


function slides(htmlObj, data, options){
    let index = htmlObj.getAttribute("data-current_slide");
      if(options.showdown){var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data)}
      document.getElementsByName(htmlObj.id)[index].innerHTML = data;
}