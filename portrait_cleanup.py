#!/usr/bin/env python
import os
import cv2

dst = os.path.join(os.environ['USERPROFILE'], 'Pictures/Spotlight Images/')

def portrait_cleanup(dst):
    """
    Checks the destination folder for any images in portrait orientation and deletes them
        Parameters:
            dst (str): the file path of the folder that the copied Windows Spotlight Images will be stored in. 
    """
    print("Portrait Spotlight Images Cleanup is running...\n")
    for filename in os.listdir(dst):
        if ".jpg" not in filename:
            continue
        dst_filename = dst + filename
        im = cv2.imread(dst_filename)
        # h is the image height, and w is the width. Note that for portrait images w is always less that h
        h, w, c = im.shape
        if w < h:
            print("File removed: " + filename + " \nHeight: " + str(h) + " \nWidth: " + str(w) + "\n" )
            os.remove(dst_filename) 

if __name__ == "__main__":
    portrait_cleanup(dst)