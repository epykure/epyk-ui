"""
CSS Style module for the scroll bar in the page

Track
::-webkit-scrollbar
::-webkit-scrollbar-track

Thumb
::-webkit-scrollbar-thumb
::-webkit-scrollbar-thumb:hover
::-webkit-scrollbar-thumb:active
::-webkit-scrollbar-thumb:vertical
::-webkit-scrollbar-thumb:horizontal

Buttons
Up
::-webkit-scrollbar-button
::-webkit-scrollbar-button:vertical:decrement
::-webkit-scrollbar-button:vertical:decrement:hover

Down
::-webkit-scrollbar-button:vertical:increment
::-webkit-scrollbar-button:vertical:increment:hover

Left
::-webkit-scrollbar-button:horizontal:decrement
::-webkit-scrollbar-button:horizontal:decrement:hover

Right
::-webkit-scrollbar-button:horizontal:increment
::-webkit-scrollbar-button:horizontal:increment:hover
"""


from epyk.core.css.styles import CssStyle


class CssScrollBar(CssStyle.CssCls):
  attrs = {"width": "14px", "height": "14px"}
  cssId = {'reference': '::-webkit-scrollbar'}


class CssScrollBarTrack(CssStyle.CssCls):
  attrs = {"background": "#303030",
           "border": "solid 2px rgba(236, 0,0 , 0.5)"}
  cssId = {'reference': '::-webkit-scrollbar-track'}


class CssScrollBarTrackThumb(CssStyle.CssCls):
  attrs = {"background": "#ffcf17"}
  cssId = {'reference': '::-webkit-scrollbar-thumb'}


class CssScrollBarTrackThumbHover(CssStyle.CssCls):
  attrs = {"background": "green"}
  cssId = {'reference': '::-webkit-scrollbar-thumb:hover'}


class CssScrollBarTrackThumbActive(CssStyle.CssCls):
  attrs = {"background": "green"}
  cssId = {'reference': '::-webkit-scrollbar-thumb:active'}


class CssScrollBarTrackThumbHorizontal(CssStyle.CssCls):
  attrs = {
    "border-right": "solid 2px rgba(33,33,33,0.5)",
    "border-left": "solid 2px rgba(33,33,33,0.5)",
           }
  cssId = {'reference': '::-webkit-scrollbar-thumb:horizontal'}

