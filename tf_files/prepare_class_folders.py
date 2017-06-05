"""
Script that resizes images and saves them to class folders
"""
from __future__ import print_function
import numpy as numpy
import pandas as pd 
import os
import glob
import cv2

# get images metadata
imgs = pd.read_csv("images_data.csv")

# list of directories after unzipping
dir_list = ["ISIC_MSK-1_1",
            "ISIC_MSK-1_2",
            "ISIC_MSK-2_1",
            "ISIC_MSK-3_1",
            "ISIC_MSK-4_1",
            "ISIC_MSK-5_1",
            "ISIC_SONIC_1",
            "ISIC_UDA-1_1",
            "ISIC_UDA-2_1"
            ]

# go trough folders, get image by image, resize it and save to appropriate folder
for dir in dir_list:
    p = dir + "/*jpg"  
    for filename in glob.glob(p):
        name = filename[-16:-4]
        df = imgs.set_index("filename")
        im_class = df.loc[name]["ben_mal"]
        print(im_class)
        image = cv2.imread(filename)
        resized = cv2.resize(image, (299, 299), interpolation=cv2.INTER_AREA)
        print("resized: ", name)
        try:
            res_path = im_class + "/" + name + ".jpg"
            cv2.imwrite(res_path, resized)
            print("saved: ", res_path)
        except:
            print("not saved: ", name)
        
        