

function news(htmlObj, data, options){
    var feed = document.createElement("p");
    feed.style.margin = "0 0 5px 0";
    if(options.showdown){
      var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data.trim())};
    feed.innerHTML = data; htmlObj.prepend(feed);

    if (options.dated){
      var now = new Date();
      var dateStringWithTime = moment(now).format('YYYY-MM-DD HH:mm:ss');
      var dateNews = document.createElement("p");
      dateNews.style.margin = 0;
      dateNews.style.fontWeight = 'bold';
      dateNews.innerHTML = dateStringWithTime;
      htmlObj.prepend(dateNews)}
}