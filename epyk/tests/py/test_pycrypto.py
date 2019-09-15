
from epyk.core.py import PyCrypto


#import doctest
#doctest.testmod()
message = "http://192.168.0.34:5000/reports/run/examples/TestSlider?slider_1788657270680=[FormatDate($(%27&slider_2122911917784=[FormatDate($(%27&slider_1662408041416=[FormatDate($(%27&slider_1526638297440=[FormatDate($(%27&slider_2905684505600=[FormatDate($(%27#"
crt = PyCrypto.PyCrypto()


encrypted = crt.encrypt(message)
print(encrypted)
print(len(encrypted))
decrypted = crt.decrypt(encrypted)
print(decrypted)