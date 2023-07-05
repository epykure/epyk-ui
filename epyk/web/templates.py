####################################
#   Angular
ANGULAR_COMPONENT = """
import { ViewChild, Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { %(asset_class)s }  from "%(asset_path)s.js";


@Component({
  selector: '%(selector)s',
  standalone: true,
  imports: [CommonModule],
  templateUrl: '%(asset_path)s.html',
  styleUrls: ['%(asset_path)s.css']
})

export class %(asset_class)sComponent {
  %(js)s;

  ngOnInit() {
    this.component = new %(asset_class)s(this.input.nativeElement, %(init_value)s, %(init_options)s);
  }
}

"""


ANGULAR_COMPONENT_SPEC = """
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { %(asset_class)sComponent } from './%(selector)s.component';
"""

ANGULAR_ROUTER = '''
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
'''


####################################
#   React
REACT_COMPONENT = """
import React, { Component } from 'react'
import "%(asset_path)s.css";
import { %(asset_class)s } from "%(asset_path)s.js";

export class %(asset_class)sComponent extends Component {

   constructor(props){
       super(props);
       %(js)s
  }

  componentDidMount() {
        // this.dom will be defined with the id tag to the html component
        this.component = new %(asset_class)s(this.dom.current, %(init_value)s, %(init_options)s)
  }

  render(){
    return (
        %(html)s
    )
  }
}

export default %(asset_class)sComponent;
"""


REACT_APP = """
%(require)s
import './%(app_class)s.css';

function %(app_class)s() {
  %(js)s
  
  return (
      %(html)s
  );
}

export default %(app_class)s;
"""


######################
#   .vue extension - known as a Single-File Component
#   https://vuejs.org/guide/scaling-up/sfc.html
#   https://vuejs.org/api/sfc-spec.html#src-imports
VUE_COMPONENT = """
<style src="%(asset_path)s.css" scoped></style>
<script src="%(asset_path)s.js" setup></script>
<template src="%(asset_path)s.html"></template>
"""


####################################
#   Svelte
SVELTE_COMPONENT = """
<script>
    %(css)s
</script>

%(html)s

<script>
    %(js)s
</script>
"""


####################################
#   NodeJs
NODE_ROUTER = '''
%(require)s

var MAP_ROUTES = %(map)s;

http.createServer(function(request, response) {
    let url = parser.parse(request.url, true);  
    fs.readFile('./%(app_path)s/'+ MAP_ROUTES[url.path] +'.html', function (err, html) {
      if (err) {throw err;} 
      response.writeHeader(200, {"Content-Type": "text/html"});  
      response.write(html);  
      response.end();  
    });
}).listen(%(port)s);
'''


NODE_LAUNCHER = '''
var http = require('http');
var url = require('url');
var fs = require('fs');

fs.readFile('./%(app_path)s/%(selector)s.html', function (err, html) {
    if (err) {throw err;}       
    http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.write(html);  
        response.end();  
    }).listen(%(port)s);
}); '''