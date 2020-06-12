import os
import pandas as pd
import numpy as np
import sys
import cv2
from PIL import Image
fercsv = pd.read_csv("fer2013.csv")
#change the path to train while converting training images
path = "test//"
labelmap = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
names=['emotion','pixels','usage']
for i in fercsv.index:
    #uncomment below line and comment the line 15 to do the same for training
    #if fercsv.loc[i,'Usage']=="Training" 
    if fercsv.loc[i,'Usage']=="PublicTest" or fercsv.loc[i,'Usage']=="PrivateTest" :
        if fercsv.loc[i,'emotion']==0:
            if not os.path.exists(path+"anger"):
                os.mkdir(path+"anger")
        elif fercsv.loc[i,'emotion']==1:
            if not os.path.exists(path+"disgust"):
                os.mkdir(path+"disgust")
        elif fercsv.loc[i,'emotion']==2:
            if not os.path.exists(path+"fear"):
                os.mkdir(path+"fear")  
        elif fercsv.loc[i,'emotion']==3:
            if not os.path.exists(path+"happy"):
                os.mkdir(path+"happy") 
        elif fercsv.loc[i,'emotion']==4:
            if not os.path.exists(path+"sad"):
                os.mkdir(path+"sad")
        elif fercsv.loc[i,'emotion']==5:
            if not os.path.exists(path+"surprise"):
                os.mkdir(path+"surprise")                                                                  
        elif fercsv.loc[i,'emotion']==6:
            if not os.path.exists(path+"neutral"):
                os.mkdir(path+"neutral")
        img = fercsv.loc[i,'pixels'].split()
        #print(img)
        pixels = np.array(img ,'float32')
        image = pixels.reshape(48, 48)
        #cv2.imshow("image",image)
        #cv2.waitKey(0)
        #print(type(image))
        dest_path = "test/"+labelmap[fercsv.loc[i,'emotion']]+"/"
        filename = str(i)+".png"
        im = Image.fromarray(image,)
        cv2.imwrite(dest_path+filename,image)
        #im.save(dest_path+filename)
        #im.show()

