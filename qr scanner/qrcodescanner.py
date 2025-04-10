import qrcode 

myqr = qrcode.make("https://srikarimaleshcaterers.com.au/")
myqr.save("Srikarimaleshcaterers.png", scale=8)
