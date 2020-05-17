

COMPONENT = '''
import { Component, OnInit, Input } from '@angular/core';

%(externalVars)s

@Component({
  selector: '%(htmlTag)s',
  templateUrl: './%(folder)s.component.html'
})

export class %(class)s implements OnInit {
  id: string; value: string;

  @Input() attrs = {};
  @Input() options = {};
  @Input() data = {};

  setStyles(object: any, css: any) {
    if(typeof css !== 'undefined'){
      for (var attr in css){
        object.style[attr] = css[attr];
      };
    }
  }

  build(htmlObj: any, data: any, options: any){
    %(build)s
  }

  refresh(data: any){
    this.build(document.getElementById(this.id), data, this.options);
  }

  constructor() { 
    this.attrs['css'] = %(css)s;
    this.options = %(options)s
  }

  ngOnInit(): void {
    this.id = this.attrs['id'];
  }

  ngAfterViewInit() {
    this.refresh(this.attrs['data']);
    this.setStyles(document.getElementById(this.id), this.attrs['css'])
  }  
}
'''

APP = '''
import { Component, OnInit } from '@angular/core';

%(externalVars)s

@Component({
  selector: '%(htmlTag)s',
  templateUrl: './%(folder)s.component.html',
  %(styleUrls)s
})
export class %(class)s implements OnInit {
  id: string;

  %(componentFunctionText)s

  constructor() {  }

  ngOnInit(): void {
  }
}
'''


COMPONENT_SPEC = '''
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { %(class)s } from './%(folder)s.component';

describe('%(class)s', () => {
  let component: %(class)s;
  let fixture: ComponentFixture<%(class)s>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ %(class)s ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(%(class)s);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

'''