# coding: utf-8 

import os
import datetime
import shutil
import re
import time
import os.path
import glob
import operator

src_path1 = "."

# Подключенный HDD
dst_path1 = "/mnt/external2/W/"

def get_oldest_file(files, _invert=False):
    """ Find and return the oldest file of input file names.
    Only one wins tie. Values based on time distance from present.
    Use of `_invert` inverts logic to make this a youngest routine,
    to be used more clearly via `get_youngest_file`.
    """
    gt = operator.lt if _invert else operator.gt
    # Check for empty list.
    if not files:
        return None
    # Raw epoch distance.
    now = time.time()
    # Select first as arbitrary sentinel file, storing name and age.
    oldest = files[0], now - os.path.getctime(files[0])
    # Iterate over all remaining files.
    for f in files[1:]:
        age = now - os.path.getctime(f)
        if gt(age, oldest[1]):
            # Set new oldest.
            oldest = f, age
    # Return just the name of oldest file.
    return oldest[0]

def get_youngest_file(files):
    return get_oldest_file(files, _invert=True)

# Указываем файлы которые нужно переносить 
list = ["205","230","232","307","323","327","329","524","528","531"]
pattern1 = "vzdump-lxc-"
pattern2 = "*.tar.gz"

for i in list:
    file_elements = pattern1+i+pattern2
    files = glob.glob(file_elements)
    # print ('=========================================================')
    # print ('oldest:', get_oldest_file(files))
    # print ('youngest:', get_youngest_file(files))
    # print ('=========================================================\n')
    shutil.move(get_youngest_file(files), dst_path1)
