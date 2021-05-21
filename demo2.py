from PIL import Image
from PIL import ImageFilter

img1 = Image.open("車牌.jpg")
img2 = img1.filter(ImageFilter.DETAIL)
# img2.save("1.jpg")
img3 = img2.filter(ImageFilter.SHARPEN)
img3.save("1.jpg")