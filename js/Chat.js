

function chat(htmlObj, data, options){
    let feed = document.createElement("p"); setCss(htmlObj, options, true);
    feed.style.margin = "0 0 5px 0";
    feed.innerHTML = getHtmlData(data, options); htmlObj.querySelector("div").prepend(feed);
    var now = new Date();
    var dateStringWithTime = moment(now).format('YYYY-MM-DD HH:mm:ss');
    var dateNews = document.createElement("p"); dateNews.style.margin = 0; dateNews.style.fontWeight = 'bold';
    dateNews.innerHTML = dateStringWithTime; htmlObj.querySelector("div").prepend(dateNews);
}