import PIL
import os
from PIL import Image


PhotoDir = (input('Enter Your Folder Path : ')+ '/')
Photos = os.listdir(PhotoDir)
print(Photos)
a = len(Photos)
os.makedirs(PhotoDir+'Compress Photo')

for i in range(0, a):
    image = PIL.Image.open(PhotoDir+Photos[i])
    width, height = image.size

    if width > 800:

        fixed_Width = 800
        height_percent = fixed_Width / width
        
        with_size = int(width) * float(height_percent)
        image = image.resize((with_size, fixed_height), PIL.Image.ANTIALIAS)
        image.save(PhotoDir+'Compress Photo/'+Photos[i])
        print(Photos[i], '|',width,',', height, '|')
        continue






    print(Photos[i], '|',width,',', height, '|')
    image = image.resize((width, height), PIL.Image.ANTIALIAS)
    image.save(PhotoDir+'Compress Photo/'+Photos[i])




