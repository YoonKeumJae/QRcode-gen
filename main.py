import qrcode 

link = input("Enter the link: ")
name = input("Enter the name of the file: ")
qr = qrcode.make(link)
qr.save(name + ".png")
