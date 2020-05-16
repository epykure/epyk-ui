

COMPONENT = '''
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