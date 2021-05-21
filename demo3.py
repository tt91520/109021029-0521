from PIL import Image, ImageDraw

newImg = Image.new('RGBA', (300, 300), "#778888")
drawObj = ImageDraw.Draw(newImg)
for i in range(100, 200, 3):
    for j in range(100, 200, 3):
        drawObj.point([i, j], fill="Red")
        

drawObj.line([(3, 3), (296, 3), (296, 296), (3, 296), (3,3)], fill="#0000ff")
drawObj.line([(13, 13), (283, 13), (283, 283), (13, 283), (13,13)], fill="#0000ff")
drawObj.line([(23, 23), (273, 23), (273, 273), (23, 273), (23,23)], fill="#0000ff")

for x in range(150, 300, 10):
    drawObj.line([(x, 0), (300, x-150)],  fill="#000000")
for y in range(0, 300, 10):
    drawObj.line([(y, 0), (y-150, 0)],  fill="#000000")

newImg.save("testImag.png")
