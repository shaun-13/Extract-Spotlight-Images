#!/usr/bin/env python
import shutil
import os
import cv2

### CHANGE src FILEPATH HERE ###
# 'src' is the file path containing the Windows Spotlight Images
src = os.path.join(os.environ['USERPROFILE'], 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/')
### CHANGE dst FILEPATH HERE ###
# 'dst' is the file path containing the copied Windows Spotlight Images to be used as your Desktop Background
dst = os.path.join(os.environ['USERPROFILE'], 'Pictures/Spotlight Images/')

def copy_spotlight(src, dst):
    """
    This function copies the Windows Spotlight Images into a user specified folder to be used as Windows Desktop Background.
    This function takes in 2 arguments:
        src (str): the file path containing the Windows Spotlight Images
        dst (str): the file path of the folder that the copied Windows Spotlight Images will be stored in. 
    """
    # Checks if destination folder exists and creates one (including all parent and subfolders) if the dst file path does not exist
    if not os.path.exists(dst):
        os.makedirs(dst)

    for filename in os.listdir(src):
        # skips files smaller than 250KB
        statinfo = os.stat(src + filename)
        if (statinfo.st_size < 250000):
            continue

        # Only selects the file if the file name is NOT in the dst folder
        # filename in src folder could already have .jpg suffix
        if not (os.path.exists(dst + filename + '.jpg')) or (os.path.exists( dst + filename)):
            statinfo = os.stat(src + filename)
            
            # Copies the file from src to dst folder
            shutil.copy2(os.path.join(src, filename), dst)

            # change the file to a .jpg file
            new_dst_file_name = os.path.join( dst + filename + '.jpg')
            os.rename(os.path.join(dst, filename), new_dst_file_name)
            
            im = cv2.imread(new_dst_file_name)
            # h is the image height, and w is the width. Note that for portrait images w is always less that h
            h, w, c = im.shape
            # mark portrait images for deletion
            if w < h:
                os.remove(new_dst_file_name)

if __name__ == "__main__":
    copy_spotlight(src, dst)