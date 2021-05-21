from PIL import Image
from PIL import ImageFilter
#PILLOW

img1 = Image.open("640.jpg")
img2 = img1.filter(ImageFilter.BLUR) #模糊
img2.save("out1.jpg")
img3 = img1.filter(ImageFilter.CONTOUR) #輪廓
img3.save("out2.jpg")
img4 = img1.filter(ImageFilter.DETAIL) #細節化
img4.save("out3.jpg")
img5 = img1.filter(ImageFilter.EDGE_ENHANCE) #邊緣增強
img5.save("out4.jpg")
img5 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE) #邊緣增強(MORE)
img5.save("out5.jpg")
img6 = img1.filter(ImageFilter.EMBOSS) #浮雕
img6.save("out6.jpg")
img7 = img1.filter(ImageFilter.FIND_EDGES) #尋找邊界
img7.save("out7.jpg")
img8 = img1.filter(ImageFilter.SMOOTH) #平滑
img8.save("out8.jpg")
img10 = img1.filter(ImageFilter.SMOOTH_MORE) #平滑(MORE)
img10.save("out10.jpg")
img9 = img1.filter(ImageFilter.SHARPEN) #銳化(對比加強)
img9.save("out9.jpg")