"""
Script that augments all images form a folder
"""

from PIL import Image
import os

def augment_dir(dir, save_dir):
    """Augment images from folder
    Flip verticaly/horizontaly, rotate 90, 180 and 270 degrees
    and save original image and new versions to a new folder

    Keyword arguments:
    dir -- folder with original images
    save_dir -- folder to save augmented images
    """
    if os.path.isdir(dir) == False:
        print("Please specify correct path to images directory")

    if os.path.isdir(save_dir) == False:
        os.mkdir(save_dir)

    for image in os.listdir(dir):
        path = dir + "/" + image
        im = Image.open(path)
        path0 = save_dir + "/" + image + ".jpg"
        im.save(path0)
        im1 = im.transpose(0)
        path1 = save_dir + "/" + image + "1" + ".jpg"
        im1.save(path1)
        im2 = im.transpose(1)
        path2 = save_dir + "/" + image + "2" + ".jpg"
        im2.save(path2)
        im3 = im.transpose(2)
        path3 = save_dir + "/" + image + "3" + ".jpg"
        im3.save(path3)
        im4 = im.transpose(3)
        path4 = save_dir + "/" + image + "4" + ".jpg"
        im4.save(path4)
        im5 = im.transpose(4)
        path5 = save_dir + "/" + image + "5" + ".jpg"
        im5.save(path5)
        print("augmented: ", image)

