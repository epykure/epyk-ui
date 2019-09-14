


import os
  from epyk.core.js import JsHtml

  class HtmlComp(object):
    htmlId = "test"

  dom = JsHtml.JsHtml(HtmlComp())
  f = JsUtils.JsFile(os.path.basename(__file__).split(".")[0], path=r"C:\Users\olivier\Documents\youpi\jsFiles")

  f.writeJs([
    dom.hide(),
    dom.toggle()
  ])
  f.close()

  s = '''
  <xs:element name="item" maxOccurs="unbounded">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="title" type="xs:string"/>
      <xs:element name="note" type="xs:string" minOccurs="0"/>
      <xs:element name="quantity" type="xs:positiveInteger"/>
      <xs:element name="price" type="xs:decimal"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
  '''