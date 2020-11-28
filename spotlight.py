#!/usr/bin/env python
import shutil
import os

### CHANGE src FILEPATH HERE ###
# 'src' is the file path containing the Windows Spotlight Images
src = os.path.join(os.environ['USERPROFILE'], 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/')

### CHANGE dst FILEPATH HERE ###
# 'dst' is the file path containing the copied Windows Spotlight Images to be used as your Desktop Background
dst = os.path.join(os.environ['USERPROFILE'], 'Pictures/Spotlight Images/')

def copy_spotlight(src, dst):
    """
    This function takes in 2 arguments:
        src (str): the file path containing the Windows Spotlight Images
        dst (str): the file path of the folder that the copied Windows Spotlight Images will be stored in. 
    This is also the folder that Windows Desktop Background will use the images from
    and copies the Windows Spotlight Images into the user specified folder (dst) to be used as your Windows Desktop Background
    """
    # Checks if destination (dst) file exists
    # and creates one (including all parent and subfolders) if the dst file path does not exsist
    if not os.path.exists(dst):
        os.makedirs(dst)

    # Array to store the file paths of the images that are to be deleted, i.e. images that are 1080x1920 instead of 1920x1080
    img_to_delete = []

    # for loop that iterates through the src directory
    for filename in os.listdir(src):
        
        # Only selects the file if the file name is NOT in the dst folder
        if not (os.path.exists( dst + filename + '.jpg' )):
            statinfo = os.stat(src + filename)
            
            # Only selects the file if it is bigger than 250KB
            if (statinfo.st_size > 250000):

                # Copies the file from src to dst folder
                shutil.copy2(os.path.join(src, filename), dst)

                # Extract the full file path of this file in the dst folder
                dst_file = os.path.join(dst, filename)

                # Creates a new file name by appending '.jpg' to the original file name
                new_dst_file_name = os.path.join( dst + filename + '.jpg')

                # Renames the file to the file path specified in new_dst_file_name
                # This also changes the file to a .jpg file
                os.rename(dst_file, new_dst_file_name)

                # open image for reading in binary mode
                with open(new_dst_file_name,'rb') as img_file:

                    # height of image (in 2 bytes) is at 164th position
                    img_file.seek(163)
                    # read the 2 bytes
                    x = img_file.read(2)
                    # calculate height
                    height = (x[0] << 8) + x[1]
                    # next 2 bytes is width
                    x = img_file.read(2)
                    # calculate width
                    width = (x[0] << 8) + x[1]
                    
                    if (width < height): # Picture is in portrait orientation
                        img_to_delete.append(new_dst_file_name)

    #Deletes all pictures in portrait orientation
    for img in img_to_delete:
        os.remove(img)

if __name__ == "__main__":
    copy_spotlight(src, dst)

