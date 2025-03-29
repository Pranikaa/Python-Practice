import qrcode
#create qr code for the name
# name = input("Enter your name:")
# img = qrcode.make(name)
# type(img) #qrcode.image.pil.pilImage
# img.save(f"{name}.png")

#create qr code for the website
name = input("Enter your name:")
img = qrcode.make("https://github.com/Pranikaa/Python-Training")
type(img)
img.save(f"{name}.png")
