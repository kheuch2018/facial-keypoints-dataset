from PIL import Image
import pandas as pd

import os


data=pd.read_csv('training.csv')
data.dropna(inplace=True)
def getimage(each):
    img = Image.new( 'RGB', (96,96), "black") 
    pixels = img.load() # create the pixel map
    
    cot=[int(i) for i in each.split(' ')]
    for i in range(img.size[0]):    # for every pixel:
        for j in range(img.size[1]):
            pixels[i,j] = (cot[i+j*96],cot[i+j*96],cot[i+j*96]) # set the colour accordingly
    return img

if __name__=='__main__':
    try:
        os.mkdir(os.getcwd()+'/imgs')
    except:
        print('X')

    print('there are '+str(len(data.Image))+' images in total\nstart extracting......')
    for i in range(1,len(data.Image)+1):
        row = data.iloc[i-1]
        getimage(row['Image']).save(os.getcwd()+'/imgs/'+str(i)+'.jpg')
    
    