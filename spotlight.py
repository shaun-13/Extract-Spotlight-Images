#!/usr/bin/env python
import shutil
import os

# 'src' is the file path containing the Windows Spotlight Images

# For troubleshooting 'src' file path issues:
# Copy and paste this file path: %userprofile%/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/
# into your Windows Explorer and hit 'Enter'

# If this file path is correct, you should see a folder containing many FILE type files with names like 'df3313abf4e5440a273f95f869689b87fbe878e63355c7f1f02412116bb46cd1'

# If you are unable to find this file path, follow this file navigation path:
# Start at C: (or the drive letter your OS is installed in)
# >C:
#     >Users
#         >USERNAME (could be your laptop name or your personalized name e.g. shaun_com)
#             >AppData
#                 >Local
#                     >Packages
#                         >Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy
#                             >LocalState
#                                 >Assets
# Click on the Windows Explorer's address bar and copy this file path that you have just navigated to
# In the source code below replace: 
# ORIGINAL: src = os.path.join(os.environ['USERPROFILE'], 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/')
# NEW: src = 'PASTE COPIED FILE PATH HERE'
# 1. Change all '\' in the copied file path to '/'  
# 2. Add a '/' after 'C:/...LocalState/Assets/'
# 3. Enclose the file path in single quotation marks ' '
# e.g. 'C:/Users/shaun_com/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'
src = os.path.join(os.environ['USERPROFILE'], 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/')

# 'dst' is the file path containing the copied Windows Spotlight Images to be used as your Desktop Background
# To change the destination folder:
# ORIGINAL: dst = os.path.join(os.environ['USERPROFILE'], 'Pictures/Spotlight Images/')
# NEW: dst = 'C:/YOUR_SPECIFIED_FILE_PATH/'
# 1. Change all '\' in the file path to '/'  
# 2. Add a '/' at the end of the path e.g. 'C:/.../Images/mySpotlightImages/'
# 3. Enclose the file path in single quotation marks ' '
# e.g. 'C:/Users/shaun_com/Desktop/Images/mySpotlightImages'
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
                #print(filename)
                # Copies the file from src to dst folder
                shutil.copy2(os.path.join(src, filename), dst)

                # Extract the full file path of this file in the dst folder
                dst_file = os.path.join(dst, filename)

                # Creates a new file name by appending '.jpg' to the original file name
                new_dst_file_name = os.path.join( dst + filename + '.jpg')

                # Renames the file to the file path specified in new_dst_file_name
                # This also changes the file to a .jpg file
                os.rename(dst_file, new_dst_file_name)

                # If using Image Module
                # with Image.open(new_dst_file_name) as im:
                #     if im.size[0] == 1080:
                #         img_to_delete.append(new_dst_file_name)

                # open image for reading in binary mode
                with open(new_dst_file_name,'rb') as img_file:

                    # height of image (in 2 bytes) is at 164th position
                    img_file.seek(165)
                    # # read the 2 bytes
                    # a = img_file.read(2)
                    # # calculate height
                    # height = (a[0] << 8) + a[1]
                    # next 2 bytes is width
                    x = img_file.read(2)
                    # calculate width
                    width = (x[0] << 8) + x[1]
                    
                    if width <= 1080: # Picture is in potrait orientation
                        img_to_delete.append(new_dst_file_name)

    #Deletes all pictures in potrait orientation
    for img in img_to_delete:
        os.remove(img)

if __name__ == "__main__":
    copy_spotlight(src, dst)

