import PIL
import os
from PIL import Image


PhotoDir = (input('Enter Your Folder Path : ')+ '/')
Photos = os.listdir(PhotoDir)
print(Photos)
a = len(Photos)

if "Compress Photo" not in Photos:
    os.makedirs(PhotoDir+'Compress Photo')

else:
    a = a - 1

CompressImagePath = os.listdir(PhotoDir+'Compress Photo' + '/')



for i in range(0, a):
    try:

        if '.jpeg' in Photos[i] or '.JPEG' in Photos[i] or  '.jpg' in Photos[i] or '.JPG' in Photos[i] or '.png' in Photos[i] or '.PNG' in Photos[i] or '.gif' in Photos[i] or '.GIF' in Photos[i] or '.raw' in Photos[i] or '.RAW' in Photos[i]:
            
            image = PIL.Image.open(PhotoDir+Photos[i])

            try:

                if Photos[i] in CompressImagePath[i]:
                   continue

            except:
                print(Photos[i] + ' Not in Compress Photo')
            

            
            width, height = image.size
            print(Photos[i], '|',width,',', height, '|')
            persentage = height / width

            if width > 800:
                width = 800
                    
            image = image.resize((width, int(width*persentage)), PIL.Image.ANTIALIAS)
            
            image.save(PhotoDir+'Compress Photo/'+Photos[i]+".webp", quality= 100) #, optimize=True, quality= 50

        else:
            continue

    except:
        print('Error ---> ',Photos[i])
