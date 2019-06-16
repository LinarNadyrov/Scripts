#!/usr/bin/python3
# coding: utf-8 

import os
import datetime
import shutil
import re
import time
import os.path

# Недельные бэкапы с площадок
src_path1 = "/rpool/w/dump/"

# Бэкап lxc 320 
src_path2 = "/mnt/pve/p2-data-nfs/dump/"

# Подключенный HDD
dst_path1 = "/mnt/external2/W/"

# Регулярные выражения
backup_file = "(\.|107|640+)"
pattern1 = "(320)+_\w*-\d*_\d*_\d*-\d*_\d*_\d*.(\.tgz)"
pattern2 = "(\w*)-(\w*)-(\.|320+)-\w*-\w*.(\.tar.gz)"
pattern3 = "(\w*)-(\w*)-"+backup_file+"-\w*-\w*.(\.tar.gz)"
#"(320+)_\w*-\w*-\w*.(\.tgz)|" + backup_file + "-(\d*_\d*_\d*-\d*_\d*_\d*)+(\.tar.gz|lzo)"

# Удаляем все данные в подключенным HDD 
dst_path_backup = [element for element in os.listdir(dst_path1)]
for element in dst_path_backup:
     os.remove(os.path.join(dst_path1, element))

# Перенос данных с src_path1
files_list=os.listdir(src_path1)
i = 0
for elements in files_list:
     files_list[i] = src_path1 + elements
     i+=1

i = 0 
for i in files_list:
     shutil.move(i, dst_path1)

# Перенос данных с src_path2
files_list=os.listdir(src_path2)
i = 0
for elements in files_list:
     files_list[i] = src_path2 + elements
     i+=1

i = 0 
for i in files_list:
    if re.search(pattern1, i):
         shutil.move(i, dst_path1)
    elif re.search(pattern2, i):
         shutil.move(i, dst_path1)
   

