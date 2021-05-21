from PIL import Image, ImageDraw

newImg = Image.new('RGBA', (300, 300), "#778888")
drawObj = ImageDraw.Draw(newImg)
for i in range(100, 200, 3):
    for j in range(100, 200, 3):
        drawObj.point([i, j], fill="Red")
        

drawObj.line([(3, 3), (296, 3), (296, 296), (3, 296), (3,3)], fill="#0000ff")
drawObj.line([(13, 13), (283, 13), (283, 283), (13, 283), (13,13)], fill="#0000ff")
drawObj.line([(23, 23), (273, 23), (273, 273), (23, 273), (23,23)], fill="#0000ff")

for x in range(150, 300, 10): #右上
    drawObj.line([(x, 0), (300, x-150)],  fill="#000000") #(起始), (終點)
for y in range(150, 300, 10): #左下
    drawObj.line([(0, y), (y-150, 300)],  fill="#000000")
for z in range(150, 300, 10): #右下
    drawObj.line([(z, 300), (300, 450-z)],  fill="#000000")
for q in range(0, 150, 10): #左上
    drawObj.line([(q, 0), (0, 150-q)],  fill="#000000")

newImg.save("testImag.png")
