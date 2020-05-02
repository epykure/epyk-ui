
from epyk.core.html import Html

from epyk.core.js.html import JsHtmlStepper
from epyk.core.html.options import OptPanel


class Stepper(Html.Html):

  def __init__(self, report, records, width, height, color, options):
    super(Stepper, self).__init__(report, records, css_attrs={"list-style-type": 'none', "width": width, "height": height})
    self.color = self._report.theme.greys[-1] if color is None else color
    self.css({'color': self.color, "display": "block", "margin": '0'})
    dflt_options = {'svg_style': {'display': 'block', 'width': 100, 'height': height[0]-20, #'padding': '0 5'
                                  },
                    'title_style': {},
                    'success': [
                      "red", "green", "blue"
                      #{"color": "red", "offset": "0%"},
                      #{"color": "green", "offset": "50%"},
                      #{"color": "#2121E5", "offset": "100%"}
                    ],
                    'shape': 'arrow', 'background': 'grey', 'text_colors': 'white'}
    dflt_options.update(options)
    self.__options = OptPanel.OptionsStepper(self, dflt_options)

    self.status_colors = {
      "success": {"border": self._report.theme.success[1], "background": self._report.theme.success[0], "stroke-width": 2, "stroke": self._report.theme.greys[-1]},
      "error": {"border": self._report.theme.danger[1], "background": self._report.theme.danger[0], "stroke-width": 2, "stroke": self._report.theme.greys[-1]},
      "pending": {"border": self._report.theme.warning[1], "background": self._report.theme.warning[1], "stroke-width": 1, "stroke": self._report.theme.greys[-1]},
      "default": {"border": self._report.theme.greys[5], "background": self._report.theme.greys[3], "stroke-width": 1, "stroke": self._report.theme.greys[-1]}}

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsHtmlStepper.Stepper
    """
    if self._dom is None:
      self._dom = JsHtmlStepper.Stepper(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    :rtype: OptPanel.OptionsStepper
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
      var width = options.svg_style.width; var height = options.svg_style.height;
      var attrs = ['name', 'text', 'title', 'tooltip'];
      var props = ['color', 'background', 'shape', 'title_color'];
      
      data.forEach(function(step, i){
        var li = document.createElement("LI") ;
        attrs.forEach(function(attr){ if (typeof step[attr] === 'undefined'){ step[attr] = ''}; });
        props.forEach(function(prop){ if (typeof step[prop] === 'undefined'){ step[prop] = options[prop]}; })
        
        var svgns = 'http://www.w3.org/2000/svg';

        var svg = document.createElementNS(svgns, 'svg');
        var defs = document.createElementNS(svgns, 'defs');
        var gradient = document.createElementNS(svgns, 'linearGradient');
        //var shape = document.createElementNS(svgns, 'rect');
        var shape = document.createElementNS(svgns, 'circle');
        
        for (var i = 0, length = options.colors.success.length; i < length; i++) {
            var stop = document.createElementNS(svgns, 'stop');
            stop.setAttribute('offset', options.colors.success[i].offset);
            stop.setAttribute('stop-color', options.colors.success[i].color);
            gradient.appendChild(stop)}
        
        gradient.id = 'Gradient'; gradient.setAttribute('x1', '0'); gradient.setAttribute('x2', '0'); 
        gradient.setAttribute('y1', '0'); gradient.setAttribute('y2', '1');
        
        defs.appendChild(gradient);
        
        
          var bubbleFactor = 2 ;
          var wbubble = width / bubbleFactor ;
          var hbubble = height / bubbleFactor ;
        shape.setAttribute('stroke', step.background);
        shape.setAttribute('stroke-width', 1);
        shape.setAttribute('cx', wbubble );
        shape.setAttribute('cy', hbubble);
        shape.setAttribute('r', hbubble);
        shape.setAttribute('fill', 'url(#Gradient)');
        
        /*
        // Arrows
        shape.setAttribute('points', '0 0,'+ (width-20)+' 0,'+(width-5) + ' ' + ((height-10)/2) +','+ (width-20) +' '+ (height-10) +',0 0'+ (height-10) +',15 '+ ((height-10)/2) +',0 0');
        shape.setAttribute('stroke', step.background);
        shape.setAttribute('name', 'signal');
        shape.setAttribute('fill', 'url(#Gradient)');
        
        /*
        // Triangle
        shape.setAttribute('points', ''+ ((width-10)/2) + ' 0,'+ (width - 10) +' '+ height +',5 '+ height);
        shape.setAttribute('stroke', step.background);
        shape.setAttribute('name', 'signal');
        shape.setAttribute('fill', 'url(#Gradient)');
        
        
        // Setup the <rect> element.
        shape.setAttribute('name', 'signal');
        shape.setAttribute('stroke', step.background);
        shape.setAttribute('fill', 'url(#Gradient)');
        shape.setAttribute('width', '100%');
        shape.setAttribute('height', '100%');
        */
        
        // Assign an id, classname, width and height
        svg.setAttribute('width', width +'px');
        svg.setAttribute('height', height +'px')
        svg.setAttribute('version', '1.1');
        svg.setAttribute('xmlns', svgns);
        
        svg.appendChild(defs);
        
        
        var line = document.createElementNS(svgns, 'line');
        line.setAttribute('x1', 0);
        line.setAttribute('stroke', 'grey');
        line.setAttribute('stroke-width', 2);
        line.setAttribute('x2', width);
        line.setAttribute('y1', height/2 );
        line.setAttribute('y2', height/2 );
        
        svg.appendChild(line);
        svg.appendChild(shape);
        
        /*
        if (step.shape == 'arrow') {



          var colors = options.colors[step.background] ;
          var colorBlink = options.colors[options.blink] ;
          var gradientLink = "<linearGradient id='grad_colors_link' x1='0%' x2='0%' y1='0%' y2='100%'><stop offset='"+ colorBlink.col_1[1] +"%' stop-color='"+ colorBlink.col_1[0] +"'  /><stop offset='"+ colorBlink.col_2[1] +"%' stop-color='"+ colorBlink.col_2[0] +"'  /><stop offset='"+ colorBlink.col_3[1] +"%' stop-color='"+ colorBlink.col_3[0] +"'  /></linearGradient>" ;
          var gradient = "<defs>" + gradientLink + "<linearGradient id='grad_" + i + "' x1='0%' x2='0%' y1='0%' y2='100%'><stop offset='"+ colos.col_1[1] +"%' stop-color'"+ colors.col_1[0] + "' /><stop offset='"+ colos.col_2[1] +"%' stop-color'"+ colors.col_2[0] + "' /><stop offset='"+ colos.col_3[1] +"%' stop-color'"+ colors.col_3[0] + "' /></linearGradient></defs>";
          var points ='0 0,'+ (width-20)+'0,'+(width-5) + ' ' + ((height-10)/2) +'.'+ (width-20) +' '+ (height-10) +',0 0'+ (height-10) +',15 '+ ((height-10)/2) +',0 0';
          var svg = $("<svg style='display:block;padding:5 0;width:"+ width +"px;height:"+ height +"px'>"+ gradient +"<polygon name='signal' points='"+points+"' stroke='"+ rec.background +"' fill='url(#grad_"+ i +")' stroke-width=1 /><text font-weight='bold' x=20 y="+ (height/2) + " fill='"+ step.color +">"+ step.text +"</text></svg>");
        
        } else if (step.shape == 'triangle'){
          var points = ''+ ((width-10)/2) + ' 0,'+ (width - 10) +' '+ height +',5 '+ height;
          var svg = $("<svg style='display:block;padding:0 5;width:"+ width +"px;height:"+ height +"px'><polygon name='signal' points='"+ points +"' fill='"+ step.background +"' ?><text font-weight='bold' x="+ (width/2-height/2 + 5) +" y="+ (height/2 + 5) +" fill='"+ step.color +"'>"+ step.text +"</text></svg>");
        } else if (rec.shape =='rectangle'){
          var svg = $("<svg style='display:block;padding:0 5' width='"+ width +"px' height='"+ height +"px'><rect name='signal' rx=10 width='"+ (width - 10) +"' height='"+ (height-40) +"' fill='"+ step.background +"' stroke='"+ step.background +"' stroke-width=1 /><text x=20 y="+ (height/2) +" fill='"+ step.color +"'>"+ step.text +"</text></svg>>");
        } else {
          var colors = options.colors[rec.background];
          var colorsBlink = options.colors[options.blink];
          var bubbleFactor = options.circle_factor ;
          var wbubble = width / bubbleFactor ;
          var hbubble = height / bubbleFactor ;
          
          if (i === 0){
            var svg = $("svg style='display:block;padding:0' width='"+ width +"px' height='"+ height +"px'>"+ gradient +"<line style='stroke:grey;stroke-width:2' x1='"+ (width/2) + "' y1='"+ ((height-10)/2) + "' x2='"+ width +"' y2='"+ ((height-10)/2) +"' /><circle name='signal' cx='"+ (wbubble + hbubble) +"' cy='"+ hbubble +"' cy="+ hbubble +"' r='"+ hbubble +"' fill='url(#grad_"+ i +")' stroke='"+ step.background +"' stroke-width=1 /><text x="+ (wbubble + 2) +" y="+ (height/2 + 5) +" fill='"+ step.color +"'>"+ step.text +"</text></svg>")
          } else if (i === (data.lenght-1)) {
            var svg = $("svg style='display:block;padding:0' width='"+ width +"px' height='"+ height +"px'>"+ gradient +"<line style='stroke:grey;stroke-width:2' x1='0' y1='"+ ((height-10)/2) + "' x2='"+ (width/2) +"' y2='"+ ((height-10)/2) +"' /><circle name='signal' cx='"+ (wbubble + hbubble) +"' cy='"+ hbubble +"' cy="+ hbubble +"' r='"+ hbubble +"' fill='url(#grad_"+ i +")' stroke='"+ step.background +"' stroke-width=1 /><text x="+ (wbubble + 2) +" y="+ (height/2 + 5) +" fill='"+ step.color +"'>"+ step.text +"</text></svg>")
          } else {
            var svg = $("svg style='display:block;padding:0' width='"+ width +"px' height='"+ height +"px'>"+ gradient +"<line style='stroke:grey;stroke-width:2' x1='0' y1='"+ ((height-10)/2) + "' x2='"+ width +"' y2='"+ ((height-10)/2) +"' /><circle name='signal' cx='"+ (wbubble + hbubble) +"' cy='"+ hbubble +"' cy="+ hbubble +"' r='"+ hbubble +"' fill='url(#grad_"+ i +")' stroke='"+ step.background +"' stroke-width=1 /><text x="+ (wbubble + 2) +" y="+ (height/2 + 5) +" fill='"+ step.color +"'>"+ step.text +"</text></svg>")
          }
        };
        */
        
        var span = document.createElement("SPAN"); span.setAttribute('name', step.name);
        span.setAttribute('name', 'label'); span.innerHTML = step.title;
        var div = document.createElement("DIV"); 
        div.setAttribute('title', step.tooltip);
        div.setAttribute('name', 'svg_holder');
        //li.style.margin = "0 5px";
        li.style.width = width +"px";
        span.style.display = "block";
        span.style["text-align"] = "center";
        span.style.width = width +"px";
        li.style.float = "left";
        div.appendChild(svg); div.appendChild(span); li.appendChild(div);
        htmlObj.appendChild(li)
      })    
      '''

  def add_step(self):
    """"""

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<ul %s></ul>' % self.get_attrs(pyClassNames=self.style.get_classes())
