#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.graph import GraphCanvas
from epyk.core.html.options import OptSkins


class Matrix(GraphCanvas.Canvas):
  name = 'Skin Matrix'
  _option_cls = OptSkins.OptionsSkin

  _js__builder__ = '''
      var ctx = htmlObj.getContext("2d"); htmlObj.height = window.innerHeight; htmlObj.width = window.innerWidth;
      var matrix = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%+-/~{[|`]}";
      matrix = matrix.split(""); var columns = htmlObj.width / options.font_size; var drops = [];
      for(var x = 0; x < columns; x++){drops[x] = 1}
      function draw()
      {
          ctx.fillStyle = "rgba(0, 0, 0, 0.04)"; ctx.fillRect(0, 0, htmlObj.width, htmlObj.height);
          ctx.fillStyle = options.color; ctx.font = options.font_size + "px arial";
          for(var i = 0; i < drops.length; i++)
          {
              var text = matrix[Math.floor(Math.random()*matrix.length)];
              ctx.fillText(text, i* options.font_size, drops[i]* options.font_size);
              if(drops[i]* options.font_size > htmlObj.height && Math.random() > 0.975){ drops[i] = 0};
              drops[i]++;
          }
      }
      setInterval(draw, 35);
    '''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<canvas %s>Your browser does not support the HTML5 canvas tag.</canvas>" % (
      self.get_attrs(pyClassNames=self.style.get_classes()))


class Doctor(GraphCanvas.Canvas):
  name = 'Skin Doctor'
  _option_cls = OptSkins.OptionsSkin

  _js__builder__ = '''
      var ctx = htmlObj.getContext ( "2d" );
      ctx.save (); ctx.shadowColor = '#555555'; ctx.shadowBlur = 10; ctx.shadowOffsetX = 2; ctx.shadowOffsetY = 2;
      ctx.beginPath (); ctx.lineWidth = 1; 
      ctx.strokeStyle = 'rgba( 20, 50, 20, 1 )'; ctx.rect ( 0, 0, htmlObj.width, htmlObj.height ); ctx.fill ();
      ctx.stroke (); ctx.closePath (); ctx.beginPath (); ctx.arc(350, 25, 20, 0, 2 * Math.PI, false );
      ctx.fillStyle = 'rgba( 200, 200, 100, 1 )'; ctx.fill(); ctx.lineWidth = 1; 
      ctx.strokeStyle = 'rgba( 180, 179, 80, 1 )'; ctx.stroke(); ctx.closePath (); ctx.beginPath ();
      ctx.arc( 350, 85, 20, 0, 2 * Math.PI, false ); ctx.fillStyle = 'rgba( 200, 200, 100, 1 )'; ctx.fill();
      ctx.lineWidth = 1; ctx.strokeStyle = 'rgba( 180, 179, 80, 1 )'; ctx.stroke();
      ctx.closePath (); var screenWidth = 400, screenHeight = 150, screenTop = 0, screenLeft = 0;
  
      function screenBackgroundRender ( a ) {
        ctx.beginPath (); ctx.fillStyle = 'rgba( 20, 20, 20, ' + a + ' )';
        ctx.fillRect ( screenLeft, screenTop, screenWidth, screenHeight ); ctx.closePath (); ctx.beginPath ();
        for ( var j = 10 + screenTop; j < screenTop + screenHeight; j = j + 10 ) {
          ctx.moveTo( screenLeft, j ); ctx.lineTo( screenLeft + screenWidth, j )}
        for ( var i = 10 + screenLeft; i < screenLeft + screenWidth; i = i + 10 ) {
          ctx.moveTo( i, screenTop ); ctx.lineTo( i, screenTop + screenHeight )}
        ctx.lineWidth = 1; ctx.strokeStyle = 'rgba( 20, 50, 20, ' + a + ' )'; ctx.stroke (); ctx.closePath ()
      };
      
      ctx.shadowBlur = 0; ctx.shadowOffsetX = 0; ctx.shadowOffsetY = 0; 
      PosX = screenLeft; PosY = screenTop + screenHeight / 2;
      setInterval ( function () {
        ctx.restore (); screenBackgroundRender ( 0.06 )
        ctx.beginPath (); ctx.moveTo( PosX, PosY );
        PosX = PosX + 1;
        if ( PosX >= screenLeft + screenWidth * 40 / 100 && PosX < screenLeft + screenWidth * 45 / 100 ) {
          PosY = PosY - screenHeight * 3 / 100;
        }
        if ( PosX >= screenLeft + screenWidth * 45 / 100 && PosX < screenLeft + screenWidth * 55 / 100 ) {
          PosY = PosY + screenHeight * 3 / 100;
        }
        if ( PosX >= screenLeft + screenWidth * 55 / 100 && PosX < screenLeft + screenWidth * 60 / 100 ) {
          PosY = PosY - screenHeight * 3 / 100;
        }
        if ( PosX >= screenLeft + screenWidth * 60 / 100 && PosX <= screenLeft + screenWidth ) {
          PosY = screenTop + screenHeight / 2;
        }
        if ( PosX > screenLeft + screenWidth ) { PosX = screenLeft; ctx.moveTo( PosX, PosY )}
        ctx.lineTo( PosX, PosY ); ctx.lineWidth = 2; ctx.strokeStyle = '#33ff33'; ctx.stroke (); ctx.closePath ();
      }, 6 );
    '''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<canvas %s>Your browser does not support the HTML5 canvas tag.</canvas>" % (
      self.get_attrs(pyClassNames=self.style.get_classes()))
