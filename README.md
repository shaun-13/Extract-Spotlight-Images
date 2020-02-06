# Extract-Spotlight-Images
This repository contains instructions and program for extracting Windows Spotlight Images (the photos on the lock-screen) and setting it as your Desktop Wallpaper

## How to run this program

## Prerequisites:
1. [Python 3](https://www.python.org/downloads/) must be installed
1. The following set of instructions assumes you are running Windows 10

### Download or clone this repository
1. Download this repository as .zip or clone this repository
1. Extract the files into your preferred location

### Create an automated scheduled task
1. Press '**WIN**' + '**R**'
1. Enter '**taskschd.msc**' and press '**Enter**'
1. In the left panel, under '**Task Scheduler (Local)**' , left double-click on '**Task Scheduler Library**'
1. In the right panel, under '**Actions**', left click '**Create Task...**'
1. In the 'Name' field, enter 'Extract Spotlight Images'
1. You may skip the rest of the fields
1. Click on the '**Triggers**' tab
1. Click on '**New...**' button
1. Make sure '**Begin the task:**' is set to 'On a schedule'
1. Under '**Settings**', select '**Daily**' (you can choose not to edit the data/time value) 
1. Click the '**OK**' button
1. Click on the '**Action**' tab
1. Click on '**New...**' button
1. Make sure the '**Action:**' field is set to '**Start a program**'
1. Under '**Program/script**', click on '**Browse...**' and navigate to the unzipped folder, click on '**spotlight.bat**' and click '**Open**'
1. Click on the '**Ok**' button
1. Click on the '**Conditions**' tab
1. Uncheck all boxes
1. Click on the '**Settings**' tab
1. Check the box '**Run task as soon as possible after a scheduled start is missed**'
1. Press '**Ok**'
1. In the middle panel, locate the newly created task '**Extract Spotlight Images**', right-click and press '**Run**'
1. Close the Task Scheduler Window

### Change your Desktop Background settings
1. Press '**WIN**' + '**R**'
1. Enter '**control /name Microsoft.Personalization /page pageWallpaper**'
1. In the background settings windows, make sure the '**Background**' field is set to '**Slideshow**'
1. Under the '**Choose albums for your slideshow**', click '**Browse**', paste this file path into the explorer window **%userprofile%/Pictures/Spotlight Images**
1. You can choose to keep the rest of the default settings or edit to your preference 

## Troubleshooting
- Feel free to open an **Issue** if there are any problems!

# Enjoy!


