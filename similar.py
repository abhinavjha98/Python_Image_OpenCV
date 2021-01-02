from PIL import Image
from PIL import ImageChops

image_one = Image.open('images/tooth.jpg')
image_two = Image.open('tooth.jpg')

diff = ImageChops.difference(image_one, image_two)

if diff.getbbox():
    diff.show()
        
