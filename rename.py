#!/usr/bin/env python
import os

dst = os.path.join(os.environ['USERPROFILE'], 'Pictures/Spotlight Images/')

def rename(dst):
    print("Checking for files with duplicate .jpg extensions...")
    for filename in os.listdir(dst):
        if ".jpg" not in filename:
            continue
        dst_filename = dst + filename
        dst_filename_list = dst_filename.split(".")
        if dst_filename_list.count("jpg") > 1:
            new_filename = ".".join(dst_filename_list[:-1])
            try: 
                os.rename(dst_filename, new_filename)
            except FileExistsError:              
                os.remove(dst_filename)

if __name__ == "__main__":
    rename(dst)