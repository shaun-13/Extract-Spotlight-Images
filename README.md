# Extract-Spotlight-Images
This repository contains instructions and program for extracting Windows Spotlight Images (the photos on the lock-screen) and setting it as your Desktop Wallpaper.

# Table of contents
1. [How to run this program](#how_to)
    1. [Prerequisites](#prerequisites) 
    1. [Create an automated scheduled task](#scheduled_task)
    1. [Change your Desktop Background settings](#change_desktop_bg)
2. [Troubleshooting](#troubleshooting)
    1. [Finding your Windows Spotlight folder](#find_spotlight_folder)
    1. [Change destination folder](#change_destination_folder)

## <a name="how-to"></a> How to run this program 

## <a name="prerequisites"></a> Prerequisites: 
1. [Python 3](https://www.python.org/downloads/) must be installed
1. The following set of instructions assumes you are running Windows 10

### Download or clone this repository 
1. Download this repository as .zip or clone this repository
1. Extract the files into your preferred location

### <a name="scheduled_task"></a> Create an automated scheduled task 
1. Press <kbd>⊞ Win</kbd> + <kbd>R</kbd>
1. Open Task Scheduler by entering <kbd>taskschd.msc</kbd> and press <kbd>Enter</kbd>
1. In the left panel, under '**Task Scheduler (Local)**' , click on '**Task Scheduler Library**'
1. In the right panel, under '**Actions**', left click '**Create Task...**'
1. In the 'Name' field, enter 'Extract Spotlight Images'
1. Skip the rest of the fields
1. Click on the '**Triggers**' tab
1. Click on '**New...**' button
1. Make sure '**Begin the task:**' is set to 'On a schedule'
1. Under '**Settings**', select '**Daily**'
1. Leave the rest of the field as default
1. Click the '**OK**' button
1. Click on the '**Action**' tab
1. Click on '**New...**' button
1. Make sure the '**Action:**' field is set to '**Start a program**'
1. Under '**Program/script**', click on '**Browse...**' and navigate to the unzipped folder, click on '**spotlight.bat**' and click '**Open**'
1. Click on the '**Ok**' button
1. Click on the '**Settings**' tab
1. Check the box '**Run task as soon as possible after a scheduled start is missed**'
1. Press '**Ok**'
1. Your task has been created
1. In the Task Scheduler Library, locate the newly created task '**Extract Spotlight Images**', right-click and press '**Run**'
1. If a Windows Security Prompt appears, click on the prompt and allow Python.exe to have the necessary file permissions
1. **END**
### <a name="change_desktop_bg"></a> Change your Desktop Background settings 
1. Press <kbd>⊞ Win</kbd> + <kbd>R</kbd>
1. Open the Windows Background Settings by entering <kbd>control /name Microsoft.Personalization /page pageWallpaper</kbd> and press <kbd>Enter</kbd>
1. Make sure the '**Background**' option is set to '**Slideshow**'
1. Under the '**Choose albums for your slideshow**', click '**Browse**', paste this file path into the explorer window <kbd>%userprofile%/Pictures/Spotlight Images</kbd>, press <kbd>Enter</kbd> and select the **Spotlight Images** folder
1. You can choose to keep the rest of the default settings or edit to your preference (e.g. shuffle on/off and duration before the next image) 

## <a name="troubleshooting"></a> Troubleshooting 
- Feel free to open an [**Issue**](https://github.com/shaun-13/Extract-Spotlight-Images/issues/new) if there are any problems!

### <a name="find_spotlight_folder"></a> If program is unable to find the Windows Spotlight Images, your Windows Spotlight Images folder may be located on a different filepath. 
**Follow these steps to troubleshoot:** 
1. Locate your Windows Spotlight Images folder. To do so, open Windows Explorer, copy and path this file path in the address bar and hit <kbd>Enter</kbd>: %userprofile%/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/
1. If this file path is correct, you should see a folder containing many files with filename like 'df3313abf4e5440a273f95f869689b87fbe878e63355c7f1f02412116bb46cd1' and with the .FILE extension
1. If this file path is not found for you, follow these navigation steps:
```
Start at C: (or the drive letter your Windows Operating System is installed in)
C:
| Users
    | <Your_Username e.g. Shaun_Desktop>
        | AppData
            | Local
                | Packages
                    | Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy (or something similar)
                        | LocalState
                            | Assets
```
4. This should be correct folder. Copy this file path
1. Edit ``spotlight.py`` in the following way:

``` python
#ORIGINAL: 
src = os.path.join(os.environ['USERPROFILE'], 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/')

# TO CHANGE: 
src = 'PASTE COPIED FILE PATH HERE'

# NOTE:
# 1. Change all '\' in the copied file path to '/'  
# 2. Add a '/' at the end of the filepath i.e. 'C:/...LocalState/Assets/'
# 3. Enclose the file path in single quotation marks ' ' e.g. 'C:/Users/shaun_com/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'

```

### <a name="change_destination_folder"></a> To change the default folder where the Windows Spotlight Images are downloaded to (default: 'C:/Users/\<YOUR_COMPUTER_NAME\>/Pictures/Spotlight Images/')
1. Edit ``spotlight.py`` in the following way:

``` python
# ORIGINAL: 
dst = os.path.join(os.environ['USERPROFILE'], 'Pictures/Spotlight Images/')

# TO CHANGE: 
dst = 'C:/YOUR_SPECIFIED_FILE_PATH/'

# NOTE:
# 1. Change all '\' in the file path to '/'  
# 2. Add a '/' at the end of the path e.g. 'C:/.../Images/mySpotlightImages/'
# 3. Enclose the file path in single quotation marks ' '
# e.g. 'C:/Users/shaun_com/Desktop/Images/mySpotlightImages'
```

# Enjoy!


