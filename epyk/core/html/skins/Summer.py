
# https://codepen.io/JulianLaval/pen/KpLXOO

from epyk.core.html.graph import GraphCanvas
from epyk.core.html.options import OptSkins


class Lights(GraphCanvas.Canvas):
  name = 'Skin Lights'
  _option_cls = OptSkins.OptionsSkin

  _js__builder__ = '''
      var c = init(htmlObj);
      
      class firefly{
        constructor(){
          this.x = Math.random()*w;
          this.y = Math.random()*h;
          this.s = Math.random()*2;
          this.ang = Math.random()*2*Math.PI;
          this.v = this.s*this.s/4;
        }
        move(){
          this.x += this.v*Math.cos(this.ang);
          this.y += this.v*Math.sin(this.ang);
          this.ang += Math.random()*20*Math.PI/180-10*Math.PI/180;
        }
        show(){
          c.beginPath();
          c.arc(this.x,this.y,this.s,0,2*Math.PI);
          c.fillStyle="#fddba3";
          c.fill();
        }
      }
      
      let f = [];
      
      function draw() {
        if(f.length < 100){
          for(let j = 0; j < 10; j++){
           f.push(new firefly());
        }
           }
        //animation
        for(let i = 0; i < f.length; i++){
          f[i].move();
          f[i].show();
          if(f[i].x < 0 || f[i].x > w || f[i].y < 0 || f[i].y > h){
             f.splice(i,1);
             }
        }
      }
      
      let mouse = {};
      let last_mouse = {};
      
      htmlObj.addEventListener(
        "mousemove",
        function(e) {
          last_mouse.x = mouse.x;
          last_mouse.y = mouse.y;
      
          mouse.x = e.pageX - this.offsetLeft;
          mouse.y = e.pageY - this.offsetTop;
        },
        false
      );
      function init(htmlObj) {
          c = htmlObj.getContext("2d"),
          w = (htmlObj.width = window.innerWidth),
          h = (htmlObj.height = window.innerHeight);
        c.fillStyle = "rgba(30,30,30,1)";
        c.fillRect(0, 0, w, h);
        return c;
      }
      
      window.requestAnimFrame = (function() {
        return (
          window.requestAnimationFrame ||
          window.webkitRequestAnimationFrame ||
          window.mozRequestAnimationFrame ||
          window.oRequestAnimationFrame ||
          window.msRequestAnimationFrame ||
          function(callback) {
            window.setTimeout(callback);
          }
        );
      });
      
      function loop() {
        window.requestAnimFrame(loop);
        c.clearRect(0, 0, w, h);
        draw();
      }
      
      window.addEventListener("resize", function() {
        (w = htmlObj.width = window.innerWidth),
        (h = htmlObj.height = window.innerHeight);
        loop();
      });
      
      loop();
      setInterval(loop, 1000 / 60);  
    '''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<canvas %s>Your browser does not support the HTML5 canvas tag.</canvas>" % (
      self.get_attrs(css_class_names=self.style.get_classes()))

