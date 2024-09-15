
function itemTweet(htmlObj, data, options){
    if (typeof data !== "object"){data = {content: data, title: "", author: "..."}};
    if(options.showdown){var converter = new showdown.Converter(options.showdown); converter.setOption("display", "inline-block");
      data.content = converter.makeHtml(data.content).replace("<p>", "<p style='display:inline-block;margin:0'>")};

    if (typeof data.time === 'undefined'){
      const d = new Date();
      data.time = d.getFullYear() + '-' +('0' + (d.getMonth()+1)).slice(-2)+ '-' +  ('0' + d.getDate()).slice(-2) + ' '+d.getHours()+ ':'+('0' + (d.getMinutes())).slice(-2)+ ':'+d.getSeconds()
    }

    function hashCode(str) {
      var hash = 0; for (var i = 0; i < str.length; i++) {hash = str.charCodeAt(i) + ((hash << 5) - hash)} return hash};

    function intToRGB(i){
      var c = (i & 0x00FFFFFF).toString(16).toUpperCase(); return "00000".substring(0, 6 - c.length) + c};

    var item = document.createElement("DIV"); var title = document.createElement("DIV");
    var titleValue = document.createElement("DIV");
    titleValue.innerHTML = data.title;  titleValue.style.fontWeight = "bold";
    titleValue.style.fontSize = "15px"; titleValue.style.display = "inline-block";
    item.style.verticalAlign = "top";

    var dtime = document.createElement("DIV"); dtime.style.display = "inline-block"; dtime.style.fontSize = "12px";
    dtime.innerHTML = "@"+ data.time; title.appendChild(titleValue); title.appendChild(dtime);
    dtime.style.fontStyle = 'italic'; dtime.style.marginLeft = '5px';

    var msg = document.createElement("DIV"); msg.style.display = "inline-block"; msg.style.width = "calc(100% - 80px)";
    msg.style.padding = "2px";

    var avatar = document.createElement("DIV"); avatar.style.color = "white";
    avatar.style.background = "#"+ intToRGB(hashCode(data.author[data.author.length-1])); avatar.innerHTML = data.author;
    avatar.style.width = "30px"; avatar.style.height = "30px"; avatar.style.borderRadius = "30px";
    avatar.style.display = "inline-block"; avatar.style.margin = "5px"; avatar.style.fontWeight = "bold";
    avatar.style.fontSize = "20px"; avatar.style.textAlign = "center"; avatar.style.verticalAlign = "top";

    title.setAttribute('name', 'value'); item.setAttribute('data-valid', true);

    var content = document.createElement("DIV"); content.innerHTML = data.content;
    msg.appendChild(title); msg.appendChild(content);

    item.appendChild(avatar); item.appendChild(msg); item.style.margin = "10px 5px";
    item.style.width = "calc(100% - 10px)"; item.style.padding = "5px"; item.style.border = "1px solid #e9e9e9";
    htmlObj.appendChild(item);
}