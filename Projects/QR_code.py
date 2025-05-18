# encoder decoder 

import qrcode

data = "I am Anamta"

img = qrcode.make(data)

img.save('D:/downloads/qr_code.png')
