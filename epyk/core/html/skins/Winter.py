#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.graph import GraphCanvas
from epyk.core.html.options import OptSkins


class WinterSnow(GraphCanvas.Canvas):
  name = 'Skin Winter Snow'
  _option_cls = OptSkins.OptionsSkin

  @property
  def cursors(self):
    pass

  _js__builder__ = '''
  var requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame ||
  function(callback){window.setTimeout(callback, 1000 / 60)}; window.requestAnimationFrame = requestAnimationFrame;
  window.flakes = []; window.flakeCount = 400; var mX = -100; var mY = -100;
  htmlObj.width = window.innerWidth; htmlObj.height = window.innerHeight;
  htmlObj.addEventListener("mousemove", function(e) {mX = e.clientX, mY = e.clientY});
  window.addEventListener("resize", function(){htmlObj.width = window.innerWidth; htmlObj.height = window.innerHeight});
  for (var i = 0; i < window.flakeCount; i++) {
    var x = Math.floor(Math.random() * htmlObj.width); var y = Math.floor(Math.random() * htmlObj.height);
    var size = (Math.random() * 3) + 2; var speed = (Math.random() * 1) + 0.5;
    var opacity = (Math.random() * 0.5) + 0.3;
    window.flakes.push({speed: speed, velY: speed, velX: 0, x: x, y: y, size: size, stepSize: (Math.random()) / 30,
        step: 0, opacity: opacity})};
  startSnow()
'''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    self.page.properties.js.add_constructor("resetSnow", '''
function resetSnow(flake){
  var canvas = document.getElementById("%s");
  flake.x = Math.floor(Math.random() * canvas.width); flake.y = 0; flake.size = (Math.random() * 3) + 2;
  flake.speed = (Math.random() * 1) + 0.5; flake.velY = flake.speed; flake.velX = 0;
  flake.opacity = (Math.random() * 0.5) + 0.3}''' % self.htmlCode)

    self.page.properties.js.add_constructor('startSnow', '''
function startSnow() { var mX = -100; var mY = -100;
  var canvas = document.getElementById("%s");  var ctx = canvas.getContext("2d"); 
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (var i = 0; i < window.flakeCount; i++) {
    var flake = window.flakes[i]; var x = mX; var y = mY; var minDist = 150; var x2 = flake.x; var y2 = flake.y;
    var dist = Math.sqrt((x2 - x) * (x2 - x) + (y2 - y) * (y2 - y)); var dx = x2 - x; var dy = y2 - y;
    if (dist < minDist) {
      var force = minDist / (dist * dist); var xcomp = (x - x2) / dist; var ycomp = (y - y2) / dist; 
      var deltaV = force / 2; flake.velX -= deltaV * xcomp; flake.velY -= deltaV * ycomp} 
    else {
      flake.velX *= .98; if (flake.velY <= flake.speed){flake.velY = flake.speed};
      flake.velX += Math.cos(flake.step += .05) * flake.stepSize}
    ctx.fillStyle = "rgba(255,255,255," + flake.opacity + ")";
    flake.y += flake.velY; flake.x += flake.velX;
    if (flake.y >= canvas.height || flake.y <= 0) {resetSnow(flake)}
    if (flake.x >= canvas.width || flake.x <= 0) {resetSnow(flake)}
    ctx.beginPath(); ctx.arc(flake.x, flake.y, flake.size, 0, Math.PI * 2); ctx.fill()}
  requestAnimationFrame(startSnow)}''' % self.htmlCode)
    return "<canvas %s>Your browser does not support the HTML5 canvas tag.</canvas>" % (
      self.get_attrs(css_class_names=self.style.get_classes()))


class Rains(GraphCanvas.Canvas):
  name = 'Skin Winter Rain'
  _option_cls = OptSkins.OptionsSkin

  _js__builder__ = '''
  htmlObj.width = window.innerWidth;
  htmlObj.height = window.innerHeight;
  
  if(htmlObj.getContext) {
    var ctx = htmlObj.getContext('2d');
    var w = htmlObj.width;
    var h = htmlObj.height;
    ctx.strokeStyle = 'rgba(174,194,224,0.5)';
    ctx.lineWidth = 1;
    ctx.lineCap = 'round';
    
    
    var init = [];
    var maxParts = 1000;
    for(var a = 0; a < maxParts; a++) {
      init.push({
        x: Math.random() * w,
        y: Math.random() * h,
        l: Math.random() * 1,
        xs: -4 + Math.random() * 4 + 2,
        ys: Math.random() * 10 + 10
      })
    }
    
    var particles = [];
    for(var b = 0; b < maxParts; b++) {
      particles[b] = init[b];
    }
    
    function draw() {
      ctx.clearRect(0, 0, w, h);
      for(var c = 0; c < particles.length; c++) {
        var p = particles[c];
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(p.x + p.l * p.xs, p.y + p.l * p.ys);
        ctx.stroke();
      }
      move();
    }
    
    function move() {
      for(var b = 0; b < particles.length; b++) {
        var p = particles[b];
        p.x += p.xs;
        p.y += p.ys;
        if(p.x > w || p.y > h) {
          p.x = Math.random() * w;
          p.y = -20;
        }
      }
    }
    
    setInterval(draw, 30);
    
  }

  '''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<canvas %s>Your browser does not support the HTML5 canvas tag.</canvas>" % (
      self.get_attrs(css_class_names=self.style.get_classes()))
