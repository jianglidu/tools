#!/usr/bin/python evn

import  os
import re
import sys
from collections import Counter
def search(tag1, tag2):
    variant = list()
    base = r'/web_share/Project_2019/21plus/210samples'
    outfile = open(r'/home/jiangli/tmp/21plus/searching_res.txt', 'w')
    outfile.write('#search words:{0}, {1}'.format(tag1, tag2)+'\n')
    count = 0
    for dirpath, dirfile, filenames in os.walk(base):
        for filename in filenames:
            if filename.endswith('.cat.txt'):
                filepath = os.path.join(dirpath, filename)
                with open(filepath) as file:
                    for line in file:
                        if tag1 in line and tag2 in line:
                            outfile.write(filename+'\t'+line)
                            count += 1
    print(count)
tag1 = 'NTRK3'
tag2 = '88137424'
search(tag1, tag2)
