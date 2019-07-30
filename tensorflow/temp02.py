from PIL import Image
img = Image.open("./test/screenShot.png")
Img = img.convert("L")
Img.save("temp02.png")